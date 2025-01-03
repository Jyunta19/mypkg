#!/bin/bash
# SPDX-FileCopyrightText: 2024 Jyunta Suzuki 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

# 必要なパッケージがインストールされているか確認
echo "Checking if required packages are installed..."
pip show psutil > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "psutil is not installed. Installing..."
    pip install psutil
fi

# ROS 2 workspaceのビルド
echo "Building ROS 2 workspace..."
cd ~/ros2_ws
colcon build --symlink-install

# ROS 2 workspaceのセットアップ
source ~/ros2_ws/install/setup.bash

# NetworkMonitorノードをバックグラウンドで起動
echo "Starting the NetworkMonitor node..."
ros2 run mypkg network_monitor &

# 少し待機してノードが起動するのを待つ
sleep 2

# トピックが公開されているか確認
echo "Checking if 'network_usage' topic is being published..."
ros2 topic list | grep "network_usage"

if [ $? -ne 0 ]; then
    echo "Error: 'network_usage' topic is not found."
    exit 1
fi

# サブスクライブして出力を確認（1回のみ取得）
echo "Subscribing to 'network_usage' topic and getting output once..."
ros2 topic echo /network_usage --once > result.log

# 少し待機して出力を取得
sleep 1

# 実行中のros2プロセスをすべて停止
echo "Stopping all ros2 processes..."
pkill -f ros2

# 終了メッセージ
echo "Test completed. Script has completely finished."

exit 0
