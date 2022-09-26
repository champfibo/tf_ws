import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from nav_msgs.msg import Odometry


class FrameListener(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

     
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

   
        # Create turtle2 velocity publisher
        self.publisher = self.create_publisher(Odometry, 'odom2', 1)

        # Call on_timer function every second
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        # Store frame names in variables that will be used to
        # compute transformations
        from_frame_rel = 'map'
        to_frame_rel = 'base_link'

       
        try:
            t = self.tf_buffer.lookup_transform(
                to_frame_rel,
                from_frame_rel,
                rclpy.time.Time())
            
           
            odom2 = Odometry()
            odom2.header.stamp = self.get_clock().now().to_msg()
            

        # set the position
            odom2.pose.pose.position.x = t.transform.translation.x
            odom2.pose.pose.position.y = t.transform.translation.y
            odom2.pose.pose.position.z = t.transform.translation.z
            odom2.pose.pose.orientation.x = t.transform.rotation.x
            odom2.pose.pose.orientation.y = t.transform.rotation.y
            odom2.pose.pose.orientation.z = t.transform.rotation.z
            odom2.pose.pose.orientation.w = t.transform.rotation.w  

            self.publisher.publish(odom2)

        except TransformException as ex:
                self.get_logger().info(
                    f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
                

def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()