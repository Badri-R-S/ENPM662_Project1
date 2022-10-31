import rospy

from std_msgs.msg import Float64

def talker():
        pub_rear_l = rospy.Publisher('/662_bot/rear_wheel_left_joint_controller/command', Float64, queue_size=10)
        pub_rear_r = rospy.Publisher('/662_bot/rear_wheel_right_joint_controller/command', Float64, queue_size=10)
        pub_front_l = rospy.Publisher('/662_bot/front_wheel_left_steering_joint_controller/command', Float64, queue_size=10)
        pub_front_r = rospy.Publisher('/662_bot/front_wheel_right_steering_joint_controller/command', Float64, queue_size=10)
        rospy.init_node('publisher', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        i = 1
        while(i<=13):
           print("Publishing\n")
           vel_val = -5
           pub_rear_l.publish(vel_val)
           pub_rear_r.publish(vel_val)
           pub_front_l.publish(0)
           pub_front_r.publish(0)
           i+=1
           rospy.sleep(1)
   
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass