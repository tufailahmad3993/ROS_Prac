import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircle (Node):

    def __init__ (self):
        super().__init__('draw_cricle')
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel' , 10)
        self.get_logger().info("Draw circle has been started")
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.send_velocity_command)

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = .4
        msg.linear.y = .4
        msg.angular.z = 2*3.14*.1
        self.cmd_vel_pub_.publish(msg)

        self.get_logger().info('Publishing: "%s"' % msg.linear.x)



def main(args = None):
    rclpy.init(args = args)
    draw_circle= DrawCircle()
    rclpy.spin(draw_circle)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    

