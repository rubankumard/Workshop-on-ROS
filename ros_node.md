# <p align = "center">MITRA - ROS Workshop </p>

# <p align = "center">Ros Node</p>

# Roscore

<p> 
  
  &emsp;&emsp;&emsp; ➢ Roscore is a collection of nodes and programs that are pre-requisites of a ROS-based system. You must have a roscore running in order for ROS nodes to communicate. It is launched using the roscore command.
  </br>&emsp;&emsp;&emsp; ➢ Roscore is the first thing you should run when using ROS.
</p>

``` 
roscore
```

***You will see something similar to this***

```
... logging to /home/drk/.ros/log/221fcf1a-da0b-11ed-a3c7-a7e574dc0231/roslaunch-ruban-12245.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://ruban:35127/
ros_comm version 1.15.14


SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.15.14

NODES

auto-starting new master
process[master]: started with pid [12253]
ROS_MASTER_URI=http://ruban:11311/

setting /run_id to 221fcf1a-da0b-11ed-a3c7-a7e574dc0231
process[rosout-1]: started with pid [12265]
```

## ROS Node
<p> 
  
  &emsp;&emsp;&emsp; ➢ A ROS Node is a piece of software/executable that uses ROS to communicate with other ROS Nodes.
</br>&emsp;&emsp;&emsp; ➢ ROS Nodes are the building blocks of any ROS Application.
</br>&emsp;&emsp;&emsp; ➢ For example, if you have a wall-following robot then one ROS Node could get distance sensor values and another node can control the motors of the robot. So, these two nodes will communicate with each other in order to move the robot.
</br>&emsp;&emsp;&emsp; ➢ You can write your entire ROS Application in a single node but having multiple nodes ensures that if a node crashes it won’t crash your entire ROS application.
</br>&emsp;&emsp;&emsp; ➢ A ROS package can have multiple ROS Nodes.
</br>&emsp;&emsp;&emsp; ➢ Python and C++ are majorly used to write ROS Nodes.
</br> 
  &emsp;&emsp;&emsp; ➢ Consider this example:
  </p>

  ![ros_node_004](https://user-images.githubusercontent.com/115358075/231803333-6b511550-5f39-4cc5-b7ae-9f96b3e7df44.jpg)

  <p> 
  &emsp;&emsp;&emsp; ➢ Open a new terminal and run</br> </p>
  
 ```
 rosnode list
 ```
 
 > It will show `/rosout`
 
  <p>
&emsp;&emsp;&emsp; ➢ The rosnode info command returns information about a specific node.
  </p>
  
  ```
  rosnode info /rosout
  ```
  
  > This will give us info about the node
  
## Creating our own node

***Note: We are going to work in python for creating nodes, however the same can be done using C++, python being a modular language would be much easier for a beginner to work with when compared to C++. However if you are well-versed with C++ you are free to use them too.***

*We're now going to create a node inside the `workshop_tutorial` package that we created earlier*

**Step 1:**
```
cd ~/dexbot_ws/src/workshop_tutorial/
```
> If you have created the workspace inside any other directories, go to that directory and then type the above statement without the '~' in begining.

> ***If you have sourced the worspace in ~/.bashrc as in previous setup instruction, you can also use the following for moving to the workspace***
> ``` roscd workshop_tutorial ```

**Step 2:**
* Generally according to the global conventions, all the python or C++ scripts will be stored inside a directory named scripts
* To create a new folder,
```
mkdir scripts
cd scripts
```

**Step 3:**
* Creating a python script titled `first_node.py`
```
touch first_node.py
```

**Step 4:**
* Open the script with any text editor, `We're gonna use VS-Code`:
```
code first_node.py
```
> Wait for a few seconds, the VS-Code window will open shortly

**Step 5:**
* Type the following in the VS-Code window:
```
#!/usr/bin/env python3

import rospy

def main():    
   
    rospy.init_node('first_node', anonymous=True) # First Step is to declare the script as a ROS Node.

    rospy.loginfo("Hello World!")                 #Print the info on the console
    
    rospy.spin()                                  # To keep the node alive till it is killed by the user.
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
 ```
 
 *`Save the file and close the editor`*
 
 **Step 6:**
 * Type `ls` in terminal.
 * Now we have to make this script executable.
 ```
 chmod +x first_node.py
 ```
 * Type `ls` in terminal.

**Step 7:**
* Open a new terminal and run ROS Master:
```
roscore
```
* Open a new terminal and run ROS Node `first_node.py`
```
rosrun workshop_tutorial first_node.py
```
**Step 8:**
* You will get a output similar to this
```
[INFO] [1681530780.577452]: Hello World!

```
