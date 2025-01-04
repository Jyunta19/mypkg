# ROS2 ネットワークモニター
## 概要
このROS2 パッケージは、ネットワークの送受信データ量をリアルタイムで監視する機能を持ちます。ネットワークの送信データ量と受信データ量を計測し、それぞれ「高」「中」「低」の分類をしてパブリッシュします。

## 使い方
1. パッケージをクローンします。
```
cd ~/ros2_ws/src
git clone https://github.com/Jyunta19/mypkg
```

2. パッケージをビルドします。
```
cd ~/ros2_ws
colcon build
```

3. コマンドを実行します。
```
ros2 run mypkg network_monitor
```

4. 以下が出力例です。  
```
[INFO] [1735948327.897915170] [network_monitor]: 送信済み: 送信データ量: 1058 B (中), 受信データ量: 696 B (中)
[INFO] [1735948328.897889044] [network_monitor]: 送信済み: 送信データ量: 0 B (低), 受信データ量: 0 B (低)
```

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10

## 動作環境
- Ubuntu 20.04 LTS
- ROS 2 バージョン: foxy

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

- このパッケージのコードの一部は，（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．

- © 2024 Jyunta Suzuki

