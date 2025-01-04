#!/bin/bash
# SPDX-FileCopyrightText: 2024 Jyunta Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# ROS 2 のワークスペースを設定
dir=~
[ "$1" != "" ] && dir="$1"  # 引数でディレクトリを指定可能

cd $dir/ros2_ws
colcon build

# ROS 2 のセットアップファイルを動的に選択
if [ -f /opt/ros/humble/setup.bash ]; then
    source /opt/ros/humble/setup.bash
elif [ -f /opt/ros/foxy/setup.bash ]; then
    source /opt/ros/foxy/setup.bash
else
    echo "Error: No ROS 2 setup file found"
    exit 1
fi

# ワークスペースのセットアップ
source $dir/ros2_ws/install/setup.bash || { echo "Error: ~/ros2_ws/install/setup.bash not found"; exit 1; }

# ノードを起動し、ログファイルにリダイレクト
timeout 10 ros2 run mypkg date_countdown > /tmp/mypkg.log 2>&1 &

# ログファイルの出力内容を確認
echo "=== トピックの内容確認 ==="
sleep 2

cat /tmp/mypkg.log | grep '年明けまであと' || { echo "エラー: トピックに期待したメッセージが送信されていません"; exit 1; }

# テスト成功
echo "=== テスト成功 ==="

