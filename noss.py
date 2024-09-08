import argparse
from datetime import datetime
import socket
import ipinfo
import os

os.system(f'./tcpactro GET {args.url} {args.port} {args.time} 8500')