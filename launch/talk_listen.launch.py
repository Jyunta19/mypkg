import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    battery_monitor = launch_ros.actions.Node(
        package='mypkg',       # パッケージの名前を指定
        executable='date_countdown',  # 実行するファイルを指定
        output='screen'        # ログを端末に出すための設定
    )

    return launch.LaunchDescription([battery_monitor])
