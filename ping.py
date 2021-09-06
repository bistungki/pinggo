import subprocess, os, sys, time

#https://stackoverflow.com/questions/29878003/python-ping-response-time
list_of_ip_addresses_or_host_names = ["8.8.8.8"]


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

while True:
    try:
        for ip in list_of_ip_addresses_or_host_names:
            result = subprocess.run(
                ['ping', '-c', '1', ip],
                text=True,
                capture_output=True,
                check=True)
            for line in result.stdout.splitlines():
                if "icmp_seq" in line:
                    timing = line.split('time=')[-1].split(' ms')[0]
                    # print(ip, timing)
                    timing = float(timing)
                    if timing <= 100:
                        print(style.GREEN + line)
                    elif timing > 100 and timing <= 400:
                        print(style.BLUE + line)
                    elif timing > 400 and timing < 800:
                        print(style.YELLOW + line)
                    else:
                        print(style.RED + line)
    except:
        pass
    time.sleep(1)