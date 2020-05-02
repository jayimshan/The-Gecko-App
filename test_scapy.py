import scapy.all as scapy

# Create an ARP packet
packet = scapy.ARP(op=2)
print(packet.show())
print(packet.summary())
scapy.send(packet)
# op = 1 = request
# op = 2 = response