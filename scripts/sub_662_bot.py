import rospy

from std_msgs.msg import Float64

right_front =  rospy.Publisher('/662_bot/front_wheel_right_steering_joint_controller/command', Float64, queue_size=10)
left_front = rospy.Publisher('/662_bot/front_wheel_left_steering_joint_controller/command', Float64, queue_size=10)
twist = Float64()


def straight_push(data):
    rospy.loginfo(rospy.get_caller_id() + "Forcing it to move straight")
    right_front.publish(0)
    left_front.publish(0)


    
    


def listener():
 
    rospy.init_node('662subscriber', anonymous=True)

    rospy.Subscriber("/662_bot/front_wheel_left_steering_joint_controller/command", Float64, straight_push)

    rospy.spin()
 
if __name__ == '__main__':
    listener()