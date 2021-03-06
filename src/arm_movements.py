import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Move the Arm Links !!
---------------------------
Rotating (i), Picking(l) and Jaw Arm(o):
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

speed = 0.1
turn = 0.8

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('arm_teleop')

    pub_pick = rospy.Publisher('/robot_arm/picking_arm_controller/command', Float64, queue_size = 10)     # Picking Arm controller
    pub_rotate = rospy.Publisher('/robot_arm/rotating_arm_controller/command', Float64, queue_size = 10)  # Rotating Arm controller
    pub_jaw = rospy.Publisher('/robot_arm/jaw_arm_controller/command', Float64, queue_size = 10)          # Jaw Arm controller

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
        print msg
        print vels(speed,turn)
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0

                print vels(speed,turn)
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

            pub_pick.publish(control_turn)       # Picking Arm speed
            pub_rotate.publish(control_speed)    # Rotating Arm speed
            pub_jaw.publish(control_turn)        # Jaw Arm speed


    except:
        print e

    finally:
        pub_pick.publish(control_turn)       # Picking Arm speed
        pub_rotate.publish(control_speed)    # Rotating Arm speed
        pub_jaw.publish(control_turn)        # Jaw Arm speed

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
