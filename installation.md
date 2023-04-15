# <p align = "center">MITRA - ROS Workshop </p>

# <p align = "center">Setup Instructions</p>

# Installing Virtual Machine for Ubuntu Installation
`If your Laptop has Ubuntu 20.04 installed inside Virutal Box or as an dual boot you can skip this topic`

* Follow the following Official Ubuntu Documentation for getting started with installing Ubuntu in a Virtual Machine.
  
<p> 
  
  &emsp;&emsp;&emsp; 🔗 [Installing Ubuntu in Virtual Machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview) 
 
  * ***NOTE: Install Ubuntu Version 20.04 (and NOT v22.04)***
  </p>
  
* If you have any troubles in installing, refer to one of the following videos on youtube

<p> 
  
  &emsp;&emsp;&emsp; 🔗 [Video 1](https://www.youtube.com/watch?v=x5MhydijWmc) 
 
  </p>
  <p> 
  
  &emsp;&emsp;&emsp; 🔗 [Video 2](https://www.youtube.com/watch?v=CrmHoSG8zSU) 
 
  </p>

# Installing ROS 
* ***NOTE: If your computer has ROS Installed you can skip this topic***

`We have two different approaches of installing ros, (one line installation or step by step installation)`

> You are free to choose one of the following methods for installation.
>
> Both will exactly do the same thing but in different ways!!!

<details>
	<summary> <b><i> One - Line Installation </i></b> </summary>
  
  ### One Line Installation
 
* Open a new terminal using `Ctrl+Shift+T`
  ```
  wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
  ```
</details>

<details>
	<summary> <b><i> Step by Step Installation </i></b> </summary>
  
 ### Step 1:
* Open a new terminal using `Ctrl+Shift+T`
* Setup your computer to accept software from packages.ros.org
 ```
 sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

 ### Step 2:
* Set up your keys
 ```
 sudo apt install curl
```
```
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```


 ### Step 3:
* Make sure your Debian package index is up-to-date.
 ```
 sudo apt update
```

 ### Step 4:
* Installing the ROS recommended configuration.
 ```
 sudo apt install ros-noetic-desktop-full
```

 ### Step 5:
* Adding environment variables: To Automatically add ROS environment variables to your bash session every time a new shell terminal/bash is launched, enter the following commands (this step is similar as adding environmental variable in windows).
 ```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
* Sourcing bashrc ensures to use updated bashrc, or it can be done by re-opening new terminal.
```
source ~/.bashrc
```
### Step 6:
* Additional Dependencies: To install this tool and other dependencies for building ROS packages.

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```

### Step 7:
* Initialize rosdep: Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS. If you have not yet installed rosdep, do so as follows.

```
sudo apt install python3-rosdep
```
```
sudo rosdep init
```
```
rosdep update
```
  
</details>

* Ensure that you have competed installing using one of the two methods before proceeding!!!
## Checking the installation

* Run the below command on a new terminal after performing all the steps above, this will ensure that the ROS master is running perfectly on the system.

```
roscore
```
* The ouput should be similar to this
<p align="center">
  
![Running-ROSs-roscore-on-Ubuntu-20 04](https://user-images.githubusercontent.com/115358075/229424555-aba32ea7-37ef-44f2-84de-5dad04fbe261.jpg)

</p>

***Note: The version numbers may vary, which is of no issue 😊*** 
### 🥳 Hurray!!! You have installed ROS successfully!!!

# Installing Gazebo

* Update apt database with `apt` using the following command.
```
sudo apt update
```
* After updating apt database, We can install gazebo using apt by running the following command:
```
sudo apt -y install gazebo
```

## Testing the Gazebo installation
 * Type the following in a new terminal 
 ```
 roslaunch gazebo_ros empty_world.launch
 ```
 
 Got an empty world spawned 👀??
 
# Installing Visual Studio Code (VS-Code)

* Type the following in a new terminal
```
sudo snap install --classic code
```
***Note:***
* If you get a ERROR stating, Command sudo not found,
```
apt update && apt upgrade
apt install sudo
```
* If you get a ERROR stating, Command snap not found,
```
sudo apt update
sudo apt install snapd
```
 
 # Installing turtlesim
 
 * To install turtle sim, enter the following in a new terminal
 
 ```
 sudo apt-get install ros-noetic-turtlesim 
 ```
 
 * After installing the turtlesim package we will initialize rosdep which is a onetime initialization step. If the ROS works correctly we don’t need to initialize it again. The command will be,

```
sudo rosdep init
```
***Note: If the above statement throws an error stating, "ERROR: default sources list file already exists", you can ignore the error and proceed further***

* You can update the rosdep using the command
```
rosdep update
```
 
 ### 🥳 Hurray!!! We are done with the setup!!!  🥳
