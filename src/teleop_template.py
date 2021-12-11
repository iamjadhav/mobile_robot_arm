import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

from sensor_msgs.msg import LaserScan

import math

msg = """
How to Operate the Robot !
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 10
turn = 3
scan_laser = None

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

# Function that obtains the LaserScan data and decides if an Obstacle is in the way
def obstacle(laser_points):
    global scan_laser;
    scan_laser = laser_points
    regions = [scan_laser.ranges[0], scan_laser.ranges[30],scan_laser.ranges[90],
               scan_laser.ranges[120], scan_laser.ranges[300]]

    if math.isnan(scan_laser.ranges[320]) or regions[0] < 15 or regions[1] < 15\
                 or regions[2] < 15 or regions[3] < 15 or regions[4] < 15:
        print " Obstacle Detected !! "
        pub_right.publish(control_turn * 0)
        pub_left.publish(control_turn * 0)
        pub_move.publish(control_speed * 0)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('bot_teleop')

    rospy.Subscriber('/scan', LaserScan, obstacle)

    pub_right = rospy.Publisher('/robot_arm/front_right_controller/command', Float64, queue_size = 10)   # Right wheel controller
    pub_left = rospy.Publisher('/robot_arm/front_left_controller/command', Float64, queue_size = 10)     # Left wheel controller
    pub_move = rospy.Publisher('/robot_arm/rear_controller/command', Float64, queue_size = 10)           # Rear wheel controller

    x = 1
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    speed = 8
    try:
        while scan_laser is None and not rospy.is_shutdown():
            rospy.sleep(.1)

        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0

                if (status == 14):
                    print msg
                status = (status + 1) % 15
            elif key == ' ' or key == 'k' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 10:
                    x = 0
                    th = 0
		    pass
                if (key == '\x03'):
                    break

            target_speed = speed * x
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.02 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.02 )
            else:
                control_speed = target_speed

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.1 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.1 )
            else:
                control_turn = target_turn


            # print " Moving along.. "
            pub_right.publish( control_turn * 3)      # Turn Right
            pub_left.publish( control_turn * 3)       # Turn Left
            pub_move.publish(- control_speed * 8)     # Move Forward

            rate.sleep()

    except:
        print e

    finally:
        pub_right.publish(control_turn * 3)          # Turn Right
        pub_left.publish(control_turn * 3)           # Turn Left
        pub_move.publish(- control_speed * 8)        # Move Forward

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
