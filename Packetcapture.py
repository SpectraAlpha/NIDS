from scapy.all import sniff, IP, TCP
import time

packet_lengths = []
fwd_packet_lengths = []
bwd_packet_lengths = []
fwd_packets = 0
bwd_packets = 0
start_time = time.time()

def packet_callback(packet):
    global fwd_packets, bwd_packets
    if IP in packet and TCP in packet:
        packet_length = len(packet)
        packet_lengths.append(packet_length)

        if packet[IP].src == 'source_ip':  # Replace 'source_ip' with the actual source IP
            fwd_packet_lengths.append(packet_length)
            fwd_packets += 1
        else:
            bwd_packet_lengths.append(packet_length)
            bwd_packets += 1

sniff(prn=packet_callback, store=0, timeout=60)  # Capture packets for 60 seconds

end_time = time.time()
duration = end_time - start_time

# Calculate features
avg_packet_size = np.mean(packet_lengths)
packet_length_mean = np.mean(packet_lengths)
packet_length_std = np.std(packet_lengths)
packet_length_variance = np.var(packet_lengths)
packet_length_max = np.max(packet_lengths)

fwd_packet_length_mean = np.mean(fwd_packet_lengths)
bwd_packet_length_mean = np.mean(bwd_packet_lengths)
bwd_packet_length_std = np.std(bwd_packet_lengths)
bwd_packet_length_max = np.max(bwd_packet_lengths)

fwd_packets_per_second = fwd_packets / duration
flow_packets_per_second = (fwd_packets + bwd_packets) / duration
flow_bytes_per_second = sum(packet_lengths) / duration

print(f"Avg Packet Size: {avg_packet_size}")
print(f"Packet Length Mean: {packet_length_mean}")
print(f"Packet Length Std: {packet_length_std}")
print(f"Packet Length Variance: {packet_length_variance}")
print(f"Packet Length Max: {packet_length_max}")
print(f"Fwd Packet Length Mean: {fwd_packet_length_mean}")
print(f"Bwd Packet Length Mean: {bwd_packet_length_mean}")
print(f"Bwd Packet Length Std: {bwd_packet_length_std}")
print(f"Bwd Packet Length Max: {bwd_packet_length_max}")
print(f"Fwd Packets/s: {fwd_packets_per_second}")
print(f"Flow Packets/s: {flow_packets_per_second}")
print(f"Flow Bytes/s: {flow_bytes_per_second}")
