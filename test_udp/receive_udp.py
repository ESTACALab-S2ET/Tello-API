import socket

def receive_udp_message(listen_port):
    """
    Listens for UDP messages on the specified port.

    :param listen_port: Port to listen on (e.g., 8080)
    """
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    udp_socket.bind(("0.0.0.0", listen_port))
    print(f"Listening for UDP messages on port {listen_port}...")

    while True:
        # Receive data
        data, addr = udp_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode()}")

# Example usage
if __name__ == "__main__":
    listen_port = int(input("Enter the port to listen on: "))
    receive_udp_message(listen_port)
