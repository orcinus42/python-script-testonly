#!/usr/bin/env python
#ftp_server
import SocketServer,time

class MyTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print "\033[32m Got a connection from:\033[0m", self.client_address[0]
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data :
                print "\033[31mClient is disconnected..\033[0m",self.client_address[0]
                break
            if self.data.split()[0] == 'put':
                print "Going to receive file ", self.data.split()[1]
                f = file('recv/%s' % self.data.split()[1], 'wb')
                self.request.send("ReadyToReceviceFile")
                while 1:
                    data = self.request.recv(4096)
                    if data == "FileSendDone":
                        print "Transfer is done..."
                        break
                    f.write(data)
                f.close()
            elif self.data.split()[0] == 'get':
				print "Going to send file ", self.data.split()[1]
				#f = file(self.data.split()[1])
				self.request.send("ReadyToSendFile")
				with open(self.data.split()[1]) as f:
					self.request.sendall(f.read())
					time.sleep(0.5)
				self.request.send("FileSendDone")


if __name__ == "__main__":
    HOST,PORT = "",9999
    server = SocketServer.ThreadingTCPServer((HOST,PORT), MyTCPHandler)
server.serve_forever()
