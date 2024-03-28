import socket

def get_daytime_TCP(server_address='time.nist.gov', port=13):
    try:
        # Create a socket object using TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to the server
            sock.connect((server_address, port))
            
            # Receive the response from the server
            response = sock.recv(1024)
            
            # Decode the response to a readable format
            daytime_str = response.decode('ascii')
            return daytime_str
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other error: {e}")

# Example usage
if __name__ == "__main__":
    daytime_string = get_daytime_TCP()
    if daytime_string:
        print("Daytime string received from server:")
        print(daytime_string)
    else:
        print("Failed to receive daytime string from server.")