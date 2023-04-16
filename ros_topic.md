# <p align = "center">MITRA - ROS Workshop </p>

# <p align = "center">Ros Node</p>

# ROS Topic

<p> 
  
  &emsp;&emsp;&emsp; ➢ Topics are named buses over which nodes exchange messages. 
</br>&emsp;&emsp;&emsp; ➢ Topics have anonymous publish/subscribe semantics, which decouples the production of information from its consumption.
</br>&emsp;&emsp;&emsp; ➢ In general, nodes are not aware of who they are communicating with.
</br>&emsp;&emsp;&emsp; ➢ Instead, nodes that are interested in data subscribe to the relevant topic; nodes that generate data publish to the relevant topic.
</br>&emsp;&emsp;&emsp; ➢ There can be multiple publishers and subscribers to a topic.
</br>&emsp;&emsp;&emsp; ➢ Topics are intended for unidirectional, streaming communication.
  </p>

 ## ROS Topic Tools
 
 * The common ROS Topic Tools are:
```
rostopic list
```
```
rostopic echo <\topic_name>
```

## ROS Topic List
 
* ROS Topic list is a command that helps us to know about the topics that are currently published by the nodes.

```
rostopic
```

## rqt Graph

<p> 
  
  &emsp;&emsp;&emsp; ➢ Rqt graph is a GUI plugin from the Rqt tool suite. With rqt graph you can visualize the ROS graph of your application. 
</br>&emsp;&emsp;&emsp; ➢ On one window you can see all your running nodes, as well as the communication between them. 
</br>&emsp;&emsp;&emsp; ➢ The nodes and topics will be displayed inside their namespace.</p>


### Run Roscore

* Open up a new terminal and run the following:
```
roscore
```
### Run Turtlesim

* Open a new terminal and run the following:
```
rosrun turtlesim turtlesim_node
```
### Run rqt_graph

* Open a new terminal and run the following
```
rosrun rqt_graph rqt_graph
```
> You will see a oval shape with `/turtlesim` inside

* Seems not really useful right?

## Run Telop key

* Open a new teminal and run the following:
```
rosrun turtlesim turtle_teleop_key
```

* Now you can control the turtle with your keyboard arrows!!

### Run rqt_graph again

* Open a new terminal and run the following
```
rosrun rqt_graph rqt_graph
```

* Seems quite not much useful now too right?
* Consider the following example:
![frames](https://user-images.githubusercontent.com/115358075/232322226-054cf25b-9610-4b90-b38a-9aa8e05b9cea.png)

* In such a scenario, rqt graphs can be very much useful!!

# Creating a Talker Node (Publisher)

* Navigate to the scripts folder:

```
cd ~/dexbot_ws/src/workshop_tutorial/scripts
code talker.py
```

* `talker.py` is going to have the following contents:

```#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chat', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        print("Exception Occured !!!")
```
* Save and close the editor.

* ***Don't forget to make the file executable!!***
```
chmod +x talker.py
```

* Run rostopic list, rostopic echo, rqt_graph and see what happens!!

# Creating a Listener Node:

* Navigate to the scripts folder:

```
cd ~/dexbot_ws/src/workshop_tutorial/scripts
code listener.py
```

* `listener.py` is going to have the following contents:

```
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard :"+data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        print("Exception Occured !!!")
```


* Run rostopic list, rostopic echo, rqt_graph and see what happens!!
