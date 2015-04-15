import socket

class Server:
    def __init__(self):
        self.socket = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345
        self.socket.bind((self.host,self.port))

    def start(self):
        while True:
            self.socket.listen(5)
            c, addr = self.socket.accept()
            print 'Got connection from :{address}'.format(address=addr)
            c.send('Thank you for connecting, now send me some stuff')
            data = ''
            
            while True:
                data = c.recv(1024)       
                print 'From client: %s' % data
                c.send(data.upper())
            print 'Closing connection for {address}'.format(address=addr)
            c.close()

server = Server()
server.start()
