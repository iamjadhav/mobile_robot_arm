import kinpy as kp

chain = kp.build_chain_from_urdf(open("../urdf/robot_arm.urdf.xacro").read())
print(chain)
# lbr_iiwa_link_0_frame
#  	lbr_iiwa_link_1_frame
#  	 	lbr_iiwa_link_2_frame
#  	 	 	lbr_iiwa_link_3_frame
#  	 	 	 	lbr_iiwa_link_4_frame
#  	 	 	 	 	lbr_iiwa_link_5_frame
#  	 	 	 	 	 	lbr_iiwa_link_6_frame
#  	 	 	 	 	 	 	lbr_iiwa_link_7_frame
