import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

class QueryClient(Node):
    def __init__(self):
        super().__init__('query_client')
        self.client = self.create_client(Query, 'query')

    def send_request(self, name):
        request = Query.Request()
        request.name = name
        future = self.client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        response = future.result()
        self.get_logger().info(f"Received response: {response.age}")

def main():
    rclpy.init()
    client = QueryClient()

    # "上田隆一"という名前を送信
    client.send_request('上田隆一')

    rclpy.spin(client)  # ノードをスピンして応答を待機

if __name__ == '__main__':
    main()

