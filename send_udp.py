import socket

def send_udp_message(target_ip, target_port, message):
    """
    Sends a UDP message to the specified IP and port.

    :param target_ip: Target IP address (e.g., '192.168.1.1')
    :param target_port: Target port (e.g., 8080)
    :param message: Message string to send
    """
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the message
        udp_socket.sendto(message.encode(), (target_ip, target_port))
        print(f"Message sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        # Close the socket
        udp_socket.close()

# Example usage
if __name__ == "__main__":
    # Target IP and port
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))

    # Message to send
    message = input("Enter the message to send: ")

    # Send the message
    send_udp_message(target_ip, target_port, message)
