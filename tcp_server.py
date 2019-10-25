import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1235))
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data == "close" or not data: break
        print "received data:", data, "@@@"
        conn.send(data)
    conn.close()
    if data == "close": break
