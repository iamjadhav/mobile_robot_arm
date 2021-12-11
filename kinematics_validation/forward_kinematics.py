import ikpy.chain
import numpy as np


def deg2rad(th):
    return th * np.pi / 180


my_chain = ikpy.chain.Chain.from_urdf_file("robot_arm.urdf")
th1 = float(input("Enter rotation (in deg) for Rotating Arm: "))
th2 = float(input("Enter rotation (in deg) for Extending Arm: "))
th3 = float(input("Enter rotation (in deg) for Picking Arm: "))
th4 = float(input("Enter rotation (in deg) for Jaw Arm: "))

target_angle = [0, deg2rad(th1), deg2rad(th2), deg2rad(th3), deg2rad(th4), 0]
position = my_chain.forward_kinematics(target_angle)

print("Input joint angles: (%s, %s, %s, %s, %s, %s)" % (target_angle[0],
                                                        target_angle[1],
                                                        target_angle[2],
                                                        target_angle[3],
                                                        target_angle[4],
                                                        target_angle[5]))
print("X coordinate for end effector: ", position[0, 3])
print("Y coordinate for end effector: ", position[1, 3])
print("Z coordinate for end effector: ", position[2, 3])
