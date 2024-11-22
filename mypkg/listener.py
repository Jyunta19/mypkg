import rclpy
from rclpy.node import Node
from person_msgs.msg import Person  # 修正: 正しいカスタムメッセージをインポート

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        # サブスクリプションを作成
        self.subscription = self.create_subscription(
            Person,  # 修正: メッセージ型
            "person",  # トピック名
            self.listener_callback,  # コールバック関数
            10  # キューサイズ
        )
        self.subscription  # 必要なため保持

    def listener_callback(self, msg):
        # メッセージを受信した際にログ出力
        self.get_logger().info(f"Listen: name={msg.name}, age={msg.age}")


def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    try:
        rclpy.spin(node)  
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()  
        rclpy.shutdown()  

if __name__ == "__main__":
    main()
