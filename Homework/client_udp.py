import socket

def get_daytime_UDP(server_address='time.nist.gov', port=13):
    try:
        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Set a timeout to avoid indefinite blocking
            sock.settimeout(10)
            
            # Send an empty datagram to provoke a response
            sock.sendto(b'', (server_address, port))
            
            # Receive the response from the server
            response, _ = sock.recvfrom(1024) 
            
            # Decode the response into a human-readable format
            daytime_str = response.decode('ascii')
            
            return daytime_str
    except socket.timeout:
        print("Error: The request timed out. The server did not respond.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    daytime_string = get_daytime_UDP()
    if daytime_string:
        print("Daytime string received from server (UDP):")
        print(daytime_string)
    else:
        print("Failed to receive daytime string from server (UDP).")