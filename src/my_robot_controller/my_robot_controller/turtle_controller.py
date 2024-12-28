import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel' , 10)
        self.get_logger().info("turtle controller has been started")
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10 )

    def pose_callback(self, msg):
        cmd = Twist()
        msg = Pose()

        if msg.x > 9.0 or msg.x < 2.0 or msg.y > 9.0 or msg.y < 2.0 :
            cmd.linear.x = 1.0   
            cmd.angular.z = 0.1

        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_pub_.publish(cmd)


def main(args =None):
    rclpy.init(args=args)
    node =  TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == '__main__':
    main()
    