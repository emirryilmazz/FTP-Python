from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()
authorizer.add_user("user", "123456", "user", perm="elradfmw")
authorizer.add_anonymous("anonim", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1028), handler)
server.serve_forever()

