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