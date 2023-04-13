# <p align = "center">MITRA - ROS Workshop </p>

# <p align = "center">Creating a Workspace and Package</p>

# Catkin 
* Catkin is the official build system of ROS and the successor to the original ROS build system, rosbuild. catkin combines CMake macros and Python scripts to provide some functionality on top of CMake's normal workflow.

## Catkin Installation

<p> 
  
  &emsp;&emsp;&emsp; ➢ Catkin is included by default when ROS is installed. Catkin can also be installed from source or prebuilt packages. Most users will want to use the prebuilt packages, but installing it from source is also quite simple.
</br> 
&emsp;&emsp;&emsp; ➢ However if you wish to install catkin from source, enter this command in a new ubuntu terminal
  </p>
  

```
sudo apt-get install ros-noetic-catkin
```

## Catkin Workspace
<p> 
  
  &emsp;&emsp;&emsp; ➢ A catkin workspace is a folder where you modify, build, and install catkin packages.
  </p>

## Source Space
<p> 
  
  &emsp;&emsp;&emsp; ➢ The source space contains the source code of catkin packages.This is where you can extract/checkout/clone source code for the packages you want to build. 
  </br> &emsp;&emsp;&emsp; ➢Each folder within the source space contains one or more catkin packages.This space should remain unchanged by configuring, building, or installing. 
  </br> &emsp;&emsp;&emsp; ➢The root of the source space contains a symbolic link to catkin's boiler-plate 'toplevel' CMakeLists.txt file. This file is invoked by CMake during the configuration of the catkin projects in the workspace. 
  </br> &emsp;&emsp;&emsp; ➢It can be created by calling catkin_init_workspace in the source space directory.

## Development (Devel) Space
<p> 
  
  &emsp;&emsp;&emsp; ➢ The development space (or devel space) is where built targets are placed prior to being installed. The way targets are organized in the devel space is the same as their layout when they are installed. 
  </br> &emsp;&emsp;&emsp; ➢This provides a useful testing and development environment which does not require invoking the installation step. The location of the devel space is controlled by a catkin specific CMake variable called CATKIN_DEVEL_PREFIX, and it defaults to <build space>/develspace. 
  </br> &emsp;&emsp;&emsp; ➢This is the default behavior because it might be confusing to CMake users if they invoked cmake .. in a build folder and that modified things outside of the current directory. It is recommended, however, to set the devel space directory to be a peer of the build space directory.
  </p>
  
# Creating a Catkin Workspace

### Step 1:
* Create the root workspace directory (we’ll use mitra_ws)
```
cd 
mkdir --parents mitra_ws/src
cd mitra_ws
```

### Step 2:
* Initialize the catkin workspace
```
catkin init
```
* Look for the statement “Workspace configuration appears valid”, showing that your catkin workspace was created successfully.

### Step 3:
* Build the workspace. This command may be issued anywhere under the workspace root-directory
```
catkin build
```

 ***Check if the build is successful by***
```
ls
```
* See that the mitra_ws directory has build, devel directories.

### Step 3:
* Make the workspace visible to ROS. Source the setup file in the devel directory.
```
source devel/setup.bash
```
* This file MUST be sourced for every new terminal.
* To save typing, add this to your ~/.bashrc file, so it is automatically sourced for each new terminal: </br>
• gedit `~/.bashrc` </br>
• add to the end: `source ~/mitra_ws/devel/setup.bash`</br>
• save and close the editor </br>

# Catckin Package
<p> 
  
  &emsp;&emsp;&emsp; ➢ Software in ROS is organized in packages. A package might contain ROS nodes, a ROS-independent library, a dataset, configuration files, a third-party piece of software, or anything else that logically constitutes a useful module. 
  </br> &emsp;&emsp;&emsp; ➢ The goal of these packages it to provide this useful functionality in an easy-to-consume manner so that software can be easily reused. In general, ROS packages follow a "Goldilocks" principle:  </p>
  > Enough functionality to be useful, but not too much that the package is heavyweight and difficult to use from other software.

 # Creating Catkin Package
 
 ### Step 1:
 
 <p> 
  
  &emsp;&emsp;&emsp; ➢ First change to the source space directory of the catkin workspace you created:
  </p>
  
  ```
  cd ~/dexbot_ws/src
  ```
  
  ### Step 2:
   <p> 
  &emsp;&emsp;&emsp; ➢ Now use the catkin_create_pkg script to create a new package called 'workshop_tutorial' which depends on std_msgs, roscpp, and rospy
  </p>
  
  ```
  catkin_create_pkg workshop_tutorial std_msgs rospy roscpp
  ```
  
  ### Step 3:
  
  <p>
  &emsp;&emsp;&emsp; ➢ Now you need to build the packages in the catkin workspace:
  </p>
  
  ***Note: Always do Catkin make only at the root of workspace, or else you'll be in trouble***
  
  ```
  cd ~/dexbot_ws
  catkin_make

  ```
  
