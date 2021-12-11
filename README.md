## Mobile Robot Arm
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
---

## Contributors

1) [Rajan Pande](https://github.com/rpande1996)
Graduate Student of M.Eng Robotics at University of Maryland. 
2) [Aditya Jadhav](https://github.com/iamjadhav)
Graduate Student of M.Eng Robotics at University of Maryland.

## Overview

In today’s rapidly advancing technological world, the ease of access to products and the speed as well as quality with which they are delivered are extremely important. Most of
the companies in the modern world are aware of the advantages these factors bring to their revenue. But to achieve these couple of objectives, they need to act smartly and reduce costs
wherever they can. Reducing production, packaging and shipment costs goes way beyond helping achieve those objectives. And of course, technology plays a significant part of that
advancement. Bringing down labor costs in terms of salary and benefits helps in reducing the aforementioned costs of the companies. Having smart, efficient and low-maintenance
workforce can lead to even greater benefits in saving revenue. Industrial Robots is the proven answer to this question of satisfying customer needs with speed and efficiency to stay or even
get ahead of the competition. Our aim is to build an Mobile Industrial Robot Arm that is designed to help with the loading and unloading of product shipment. While building this Robot Arm,
we intend to make use of smart sensing to have the robot become as automated as possible. The development of the packaging environment is also one of our main subtasks to implement the
entire system. We will be aiming to achieve maximum speed and efficiency in our process of loading and unloading by refining our system elements.

The results are avilable in the Demo section.
The technologies(libraries, tools, systems) used in order to build this project are listed in the next section.

## Technology Used

* Ubuntu 18.04 LTS
* ROS Melodic
* Python Programming Language
* CMake Build System
* SolidWorks Software
* IKpy Library
* Rviz
* Gazebo
* Numpy Library
* Sympy Library

## License 

```
MIT License

Copyright (c) 2021 Rajan Pande, Aditya Jadhav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```

## Demos

Gazebo Demo:

- [Final Pick and Place](https://www.youtube.com/watch?v=QyFkN3RfSUs)

Rviz Demo:

- [Rviz](https://www.youtube.com/watch?v=fZ4QtwVQR7c)


## How to Build and run scripts

- Setup: Navigate to the launch folder and open final_world.world file
and replace "/<your-workspace-location>/" with your workspace location. Otherwise the 
world will not load properly.

- Demo - cd into the catkin_ws/src and type in, 

```
git clone --recursive https://github.com/iamjadhav/mobile_robot_arm
cd ..
catkin_make
source devel/setup.bash
roslaunch robot_arm arm_launch.launch
```

- To run tele-op for mobile base or arm links, open another terminal,
cd into the src folder of the package and type,

```
python teleop_template.py/arm_movements.py
```

- FK and IK validation: cd into kinematics_validation folder of the package and run,

```
python forward_kinematics.py/inverse_kinematics.py
```

- Jacobian and T-matrices: cd into kinematics_validation folder of the package and run,

```
python jacobian_calculator.py
``` 


## Set of Assumptions 

- The environment of the robot (world) obeys gravity, and the surface is continuous
  and flat.
- The objects are placed on the edge of the platforms so as to be within the workspace
  of the Robot Arm when it moves closer to them.
- The obstacles are detected by the laser and a soft warning is displayed. It is
  assumed that the operator is on the lookout for such warnings when the robot arm
  is visibly close to any obstacle.
- The platform heights are adjusted according to the workspace of the robot arm.
- The end-effector of the robot arm is designed considering the shape of the object.
  They make grasping of the object drastically convenient.

