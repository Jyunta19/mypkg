import rclpy
from rclpy.node import Node
from person_msgs.srv import Query  # person_msgs.srvをインポート

def cb(request, response):
    if request.name == "上田隆一":
        response.age = 46
    else:
        response.age = 255
    return response

def main():
    rclpy.init()
    node = Node("talker")

    srv = node.create_service(Query, "query", cb)  # サービスを作成
    rclpy.spin(node)  # ノードをスピンしてリクエストを待機

if __name__ == '__main__':
    main()

