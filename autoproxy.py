import requests
import re
from subprocess import Popen, PIPE

response = requests.get('http://gstatic.com/generate_204')
html_content = response.text

token_match = re.search(r'window.location="https://gateway\.iitj\.ac\.in:1003/fgtauth\?([^"]+)"', html_content)

if not token_match:
    ping_command = "ping -c 4 8.8.8.8"
    ping_process = Popen(ping_command, shell=True, stdout=PIPE, stderr=PIPE)
    ping_stdout, ping_stderr = ping_process.communicate()

    if ping_process.returncode == 0:
        print("Internet Working LG")
    else:
        print("Error 101:Contact GPU daddy@IITJ")
    exit()

token = token_match.group(1)
login_url = f"https://gateway.iitj.ac.in:1003/login?{token}"

username = 'b23ch1025'
password = 'Worldofdogsfullofshit,.98'

lynx_command = f'lynx -accept_all_cookies -auth="{username}:{password}" "{login_url}"'
process = Popen(lynx_command, shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

if process.returncode != 0:
    print(f"Error: {stderr.decode()}")
else:
    print(stdout.decode())
    print("Logged in")

    ping_command = "ping -c 4 8.8.8.8"
    ping_process = Popen(ping_command, shell=True, stdout=PIPE, stderr=PIPE)
    ping_stdout, ping_stderr = ping_process.communicate()

    if ping_process.returncode != 0:
        print(f"Ping error: {ping_stderr.decode()}")
    else:
        print(ping_stdout.decode())
