import socket
import time
import random
from data import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5505

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

step_time = [0.1]
random.shuffle(step_time)
pause = step_time[0]


byte = 255
values = []

freq_data = generate_octave_notes(c_sharp0)

for i in freq_data:
    quotent = i // byte
    remainder = i % byte
    values.append([quotent, remainder])

print(values)


for j in range(100):
    for quotent, remainder in values:
        combined_data = (quotent << 8) | remainder
        sock.sendto(combined_data.to_bytes(2, byteorder='big'), (UDP_IP, UDP_PORT))
        time.sleep(pause)
