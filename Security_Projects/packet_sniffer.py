from scapy.all import sniff, IP


def packet_callback(packet):
    """Callback function to process each captured packet."""
    if IP in packet: # checks if packet has IP layer
        print(f"Packet: {packet[IP].src} -> {packet[IP].dst} | Protocal: {packet[IP].proto}") # .src get source IP | .dst get destination IP | .proto get protocals
    print(packet.summary()) # print summary of the packet


def start_sniffing():
    """Start sniffing packets on the network."""
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, count=10, filter="tcp")  # Capture only TCP packets
    

if __name__ == "__main__":
    start_sniffing()
