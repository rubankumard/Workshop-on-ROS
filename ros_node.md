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
  
  &emsp;&emsp;&emsp; ➢ A ROS node, according to ROS wiki, is basically a process that performs computation. It is an executable program running inside your application. You will write many nodes and put them into packages. Nodes are combined into a graph and communicate with each other using ROS topics, services, actions, etc.
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
  
