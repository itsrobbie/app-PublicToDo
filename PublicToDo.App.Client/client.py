import socket

class Client:
    def __init__(self):
        self.socket = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345

    def start(self):
        self.socket.connect((self.host, self.port))
        input = ''
        while input != 'Close':
            print 'From server: %s' % self.socket.recv(1024)
            input = raw_input('Robbie:')
            self.socket.send(input)
        self.socket.close

client = Client()
client.start()