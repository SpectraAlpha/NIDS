#!/bin/bash

# Number of packets to generate
NUM_PACKETS=10

# Size of each packet in bytes
PACKET_SIZE=64

for ((i=1; i<=NUM_PACKETS; i++))
do
    # Generate a random packet
    RANDOM_PACKET=$(head -c $PACKET_SIZE /dev/urandom | base64)
    echo "Packet $i: $RANDOM_PACKET"
done
