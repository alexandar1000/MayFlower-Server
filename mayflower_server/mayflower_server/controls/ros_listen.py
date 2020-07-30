from __future__ import print_function
import roslibpy

client = roslibpy.Ros(host='parallels', port=9090)
client.run()

listener = roslibpy.Topic(client, '/boat_controls', 'std_msgs/String')
listener.subscribe(lambda message: print('Heard talking: ' + message['data']))

try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()