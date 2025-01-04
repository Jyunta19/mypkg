# ROS2 年越しカウントダウンノード
## 概要
このROS2 パッケージは、年明けまでの日数をカウントダウンするノードを実装するものです。「date_countdown」ノードは、毎日更新される現在の日付と、年明けまでの残り日数をトピック 「/date_countdown_topic」 にパブリッシュします。

## 主な機能
- 現在の日付を取得し、年明けまでの日数を計算
- トピック「/date_countdown_topic」 を通じて情報をパブリッシュ
- 「date_countdown」ノードは、1秒ごと情報を更新して公開

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
ros2 run mypkg date_countdown
```

4. 別のターミナルでメッセージの確認
```
ros2 topic echo /date_countdown_topic
```

5. 以下が出力例です。  
```
[INFO] [1735965154.958659322] [date_countdown]: 今日の日付: 2025-01-04,  年明けまであと 361 日
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

