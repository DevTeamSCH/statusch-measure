import sys
import dpkt
from struct import unpack
import matplotlib.pyplot as plt

print(sys.argv[1])
f = open(sys.argv[1], 'rb')
pcap = dpkt.pcap.Reader(f)

drier = []
washer = []
timestamps = []
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    udp = ip.data
    d, w = unpack('>HH', udp.data[4:8])
    # print(ts, "Length:", len(udp.data), "Drier:", d, "Washer:", w, "Raw:", udp.data[4:8])
    drier.append(d)
    washer.append(w)
    timestamps.append(ts*1_000_000)

plt.subplot(211)
plt.xlabel('Time')
plt.ylabel('Consumption')
plt.title('Dryer')
plt.plot(timestamps, drier)
plt.grid(True)
plt.subplot(212)
plt.xlabel('Time')
plt.ylabel('Consumption')
plt.title('Washing Machine')
plt.plot(timestamps, washer)
plt.grid(True)
plt.show()

