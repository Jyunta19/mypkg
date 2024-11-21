import rclpy  # ROS 2のクライアントのためのライブラリ
from rclpy.node import Node  # ノードを実装するためのNodeクラス
from std_msgs.msg import Int16  # 通信の型

rclpy.init()
node = Node("talker")  # ノード作成
pub = node.create_publisher(Int16, "countup", 10)  # パブリッシャ作成
n = 0  # カウント用変数

def cb():
    global n  # 関数を抜けてもnがリセットされないようにしている
    msg = Int16()  # メッセージの「オブジェクト」
    msg.data = n  # msgオブジェクトの持つdataにnを結び付け
    pub.publish(msg)  # pubの持つpublishでメッセージ送信
    n += 1

def main():
    node.create_timer(0.5, cb)  # タイマー設定
    rclpy.spin(node)  # 実行（無限ループ）

