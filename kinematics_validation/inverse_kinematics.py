import ikpy.chain
import ikpy.utils.plot as plot_utils
import numpy as np


def rad2deg(th):
    return th * 180 / np.pi


my_chain = ikpy.chain.Chain.from_urdf_file("robot_arm.urdf")
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))
target_position = [x, y, z]
angles = my_chain.inverse_kinematics(target_position)
print("Input position: (%s, %s, %s)" % (target_position[0],
                                        target_position[1],
                                        target_position[2]))
print("Angle for Rotating Arm: %s deg" % rad2deg(angles[1]))
print("Angle for Extending Arm: %s deg" % rad2deg(angles[2]))
print("Angle for Picking Arm: %s deg" % rad2deg(angles[3]))
print("Angle for Jaw Arm: %s deg" % rad2deg(angles[4]))
