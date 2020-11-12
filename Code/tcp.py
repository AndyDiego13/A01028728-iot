import socket


#.AF_INET es un socket ip version 4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#UDP sock.SOCK_DEGRAM
#LA IP TWITTER Y EL PUERTO
s.connect(("104.244.42.1", 80))
#ENVIAS
s.send(b'GET / HTTP/1.1\r\n\r\n')#POR SER HTTP SI ES NECESARIO LA COMBINACIÓN DE /r/n
#se reciben los datos
data=s.recv(1024)#en lugar de un valor fijo pondremos un for
print(data)
s.close()