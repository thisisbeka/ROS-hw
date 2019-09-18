import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import std_msgs.msg

joints = ['base_to_right_wheel', 'base_to_left_wheel', 'base_to_right_wheel2','base_to_left_wheel2']

pub = None
rate = None

def send(deg):
    message = std_msgs.msg.Header()
    message.stamp = rospy.Time.now()
    msg = JointState()
    msg.header = message
    msg.name = joints
    msg.position = deg
    rospy.loginfo(msg)
    pub.publish(msg)
    rate.sleep()

def talker():
    global pub
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('my_teleop', anonymous=True)
    step = 0.04
    pos = 0.0
    pos2 = 0.0
    pos3 = 0.0
    global rate
    rate = rospy.Rate(5)
    for x in range(10):
        lst = [0, 0, pos]
        pos -= step
        send(lst)
    for x in range(10):
        lst = [pos2, pos3, pos]
        pos2 += 2 * step
        pos3 -= step
        send(lst)

    while not rospy.is_shutdown():
        rospy.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass