from opcua import Client
from datetime import datetime
import time
import csv
import os

server_url = "opc.tcp://localhost:4840"
log = "logs"
os.makedirs(log, exist_ok=True)


def getLogFile():
    now = datetime.now()
    return os.path.join(log, f"OPC_Log_{now.strftime('%Y-%m-%d_%H')}.csv")


def writeHeader(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Timestamp_24hr",
                "EpochTime_UTC",
                "Tag1", "Tag2", "Tag3", "Tag4", "Tag5",
                "Tag6", "Tag7", "Tag8", "Tag9", "Tag10"
            ])


def main():
    client = Client(server_url)
    client.connect()
    print("Connected to OPC UA Server")
    objects = client.get_objects_node()
    children = objects.get_children()
    tag_nodes = []
    for node in children:
        name = node.get_browse_name().Name
        if name.startswith("Tag"):
            tag_nodes.append(node)
    tag_nodes = sorted(tag_nodes, key=lambda n: n.get_browse_name().Name)

    if len(tag_nodes) < 10:
        print("ERROR: Less than 10 tags found")
        return
    print("Found tags:", [n.get_browse_name().Name for n in tag_nodes])

    try:
        while True:
            now = datetime.now()
            epoch_time = int(now.timestamp())
            log_file = getLogFile()
            writeHeader(log_file)
            values = [node.get_value() for node in tag_nodes]
            with open(log_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    now.strftime("%Y-%m-%d %H:%M:%S"),
                    epoch_time,
                    *values
                ])
            print(f"Logged data at {now}")
            time.sleep(60)

    except KeyboardInterrupt:
        print("Stopping client")

    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
