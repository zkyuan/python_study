"""
 * @author: zkyuan
 * @date: 2025/3/23 15:26
 * @description: web请求
"""
import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8080))

sock.listen(5)

while True:
    con, addr = sock.accept() # 阻塞等待浏览器请求
    data = con.recv(1024)
    print(f"客户端发送的请求：{data}")
    print()
    # con.send(b"message: 200, ok!") # 报错
    # 响应格式 \r\n\r\n后面是响应体
    con.send(b"HTTP/1.1 200 OK\r\nserver:yuan \r\n\r\nmessage: 200, ok!")

    con.close()

# 在浏览器使用localhost:8080访问