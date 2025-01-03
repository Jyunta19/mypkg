#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Jyunta Suzuki 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil
from collections import deque

class NetworkMonitor(Node):
    def __init__(self):
        super().__init__('network_monitor')
        self.publisher_ = self.create_publisher(String, 'network_usage', 10)
        self.timer = self.create_timer(1.0, self.publish_network_usage)
        
        # 前回の送受信データ量を記録
        self.previous_sent = psutil.net_io_counters().bytes_sent
        self.previous_recv = psutil.net_io_counters().bytes_recv

        # 差分の履歴を記録するキュー
        self.sent_data_history = deque(maxlen=10)
        self.recv_data_history = deque(maxlen=10)
        
        self.get_logger().info("ネットワークモニターノードが起動しました。")

    def classify_bandwidth(self, value, average):
        """
        データ量を分類 (高, 中, 低)
        """
        if value > average * 1.5:
            return "高"
        elif value > average * 0.5:
            return "中"
        else:
            return "低"

    def publish_network_usage(self):
        # 現在のネットワークの送受信量を取得
        net_io = psutil.net_io_counters()
        current_sent = net_io.bytes_sent
        current_recv = net_io.bytes_recv

        # 差分を計算
        sent_diff = current_sent - self.previous_sent
        recv_diff = current_recv - self.previous_recv

        # 差分を履歴に追加
        self.sent_data_history.append(sent_diff)
        self.recv_data_history.append(recv_diff)

        # 平均値を計算
        avg_sent = sum(self.sent_data_history) / len(self.sent_data_history)
        avg_recv = sum(self.recv_data_history) / len(self.recv_data_history)

        # データ量を分類
        sent_class = self.classify_bandwidth(sent_diff, avg_sent)
        recv_class = self.classify_bandwidth(recv_diff, avg_recv)

        # 前回のデータを更新
        self.previous_sent = current_sent
        self.previous_recv = current_recv

        # メッセージを生成
        msg = String()
        msg.data = (
            f"送信データ量: {sent_diff} B ({sent_class}), "
            f"受信データ量: {recv_diff} B ({recv_class})"
        )

        # パブリッシュ
        self.publisher_.publish(msg)
        self.get_logger().info(f"送信済み: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = NetworkMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

