import argparse
from datetime import datetime
import socket
import ipinfo
import os

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Simulate an attack command.')
parser.add_argument('url', type=str, help='URL to attack')
parser.add_argument('port', type=int, help='Port for attack')
parser.add_argument('time', type=int, help='Time duration of attack')
parser.add_argument('methods', type=str, help='Methods used')

# Parse the arguments
args = parser.parse_args()

# Now you can use `args` in the os.system call
os.system(f'./tcpactro GET {args.url} {args.port} {args.time} 8500')
