from opcua import Server
import time
from datetime import datetime
server = Server()
server.set_endpoint("opc.tcp://localhost:4840")

uri = "http://local.opcua.server"
server.register_namespace(uri)
idx = 2


objects = server.get_objects_node()

tags = []
for i in range(1, 11):
    tag = objects.add_variable(idx, f"Tag{i}", i * 10)
    tag.set_writable()
    tags.append(tag)

server.start()
print("OPC UA Server started ")

try:
    while True:
        for i, tag in enumerate(tags):
            tag.set_value(i * 10 + datetime.now().second * 0.1)
        time.sleep(1)
except KeyboardInterrupt:
    server.stop()
    print("Server stopped")
