import rclpy
from rclpy.node import Node

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtlecontroller')
        self.get_logger().info("Turtle controller has been started")


def main(args =None):
    rclpy.init(args=args)
    node =  TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == '__main__':
    main()
    