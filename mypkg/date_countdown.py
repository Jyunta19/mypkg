#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Jyunta Suzuki 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta

class DateCountdownNode(Node):
    def __init__(self):
        super().__init__('date_countdown')
        self.publisher = self.create_publisher(String, '/date_countdown_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_date_countdown)
        self.current_date = datetime.now()

    def publish_date_countdown(self):
        remaining_days = (datetime(self.current_date.year + 1, 1, 1) - self.current_date).days
        msg = String()
        msg.data = f"今日の日付: {self.current_date.strftime('%Y-%m-%d')}, 年明けまであと {remaining_days} 日"
        self.publisher.publish(msg)
        self.current_date += timedelta(days=1)

def main():
    rclpy.init()
    node = DateCountdownNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

