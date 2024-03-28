import socket
import struct
import time

def get_time_UDP(server_address='time.nist.gov', port=37):
    try:
        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Set a timeout to avoid indefinite blocking
            sock.settimeout(10)
            
            # Send an empty datagram to provoke a response
            sock.sendto(b'', (server_address, port))
            
            # Receive the response from the server
            response, _ = sock.recvfrom(4)  
            
            # Unpack the response from network byte order to a local integer
            (time_since_epoch,) = struct.unpack('!I', response)
            
            # Convert the time to unix epoch time (since 1970)
            unix_epoch_time = time_since_epoch - 2208988800
            
            # Convert the epoch time to a human-readable format
            readable_time = time.ctime(unix_epoch_time)
            
            return readable_time
    except socket.timeout:
        print("Error: The request timed out. The server did not respond.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    time_string = get_time_UDP()
    if time_string:
        print("Time received from server (UDP):")
        print(time_string)
    else:
        print("Failed to receive time from server (UDP).")