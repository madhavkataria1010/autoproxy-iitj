import requests
import re
from subprocess import Popen, PIPE

def check_internet():
    ping_command = "ping -c 4 8.8.8.8"
    ping_process = Popen(ping_command, shell=True, stdout=PIPE, stderr=PIPE)
    ping_stdout, ping_stderr = ping_process.communicate()

    if ping_process.returncode == 0:
        print("Logged in via LG.")
        return True
    else:
        print("Error 101: Contact GPU daddy@IITJ")
        return False

response = requests.get('http://gstatic.com/generate_204')
html_content = response.text

token_match = re.search(r'window.location="https://gateway\.iitj\.ac\.in:1003/fgtauth\?([^"]+)"', html_content)

if not token_match:
    if not check_internet():
        exit()
else:
    token = token_match.group(1)
    fgtauth_url = f"https://gateway.iitj.ac.in:1003/fgtauth?{token}"

    auth_page_response = requests.get(fgtauth_url)
    auth_page_html = auth_page_response.text

    magic_match = re.search(r'name="magic" value="([^"]+)"', auth_page_html)
    redir_match = re.search(r'name="4Tredir" value="([^"]+)"', auth_page_html)

    if not magic_match or not redir_match:
        print("Could not find magic token or redirection URL in login page.")
        exit()

    magic = magic_match.group(1)
    redir_url = redir_match.group(1)

    username = '' # user name
    password = '' # Password 

    login_data = {
        'magic': magic,
        '4Tredir': redir_url,
        'username': username,
        'password': password
    }

    login_response = requests.post(redir_url, data=login_data)

    if login_response.status_code == 200:
        print("Logged in successfully")

        if check_internet():
            print("Internet connection is active.")
        else:
            print("Ping failed after login.")
    else:
        print(f"Login failed with status code: {login_response.status_code}")
