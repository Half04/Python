import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if data and data != "close":
        conn.send(data)
    conn.close()
