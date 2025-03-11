import os

command = "ping -c 1 " 
while True:
    hostname = input("Enter a hostname: ")
    response = os.popen(f'{command} {hostname}').read()
    print(response)
    if '1 packets transmitted, 1 received' in response:
        print(f"{hostname} is up!")
    else:
        print(f"{hostname} is down!")
    print()
