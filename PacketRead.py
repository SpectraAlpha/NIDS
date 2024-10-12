import pandas as pd
import numpy as np

packet_lengths = []
fwd_packet_lengths = []
bwd_packet_lengths = []
fwd_packets = 0
bwd_packets = 0
start_time = time.time()

# Read packet lengths from the file
packet_lengths = pd.read_csv('packet_lengths.txt', header=None, names=['PacketLength'])

# Calculate features
avg_packet_size = packet_lengths['PacketLength'].mean()
packet_length_mean = packet_lengths['PacketLength'].mean()
packet_length_std = packet_lengths['PacketLength'].std()
packet_length_variance = packet_lengths['PacketLength'].var()
packet_length_max = packet_lengths['PacketLength'].max()

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