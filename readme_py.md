# How to Install and Use the Script on Kali Linux

### 1. Ensure Python 3 is Installed
Make sure Python 3 is installed on your Kali Linux machine. You can check the version by running:

```
bash
python3 --version
```
If Python 3 is not installed, install it with the following commands:

### 2. Install Required Python Libraries

You will need the `requests` library to run this script. Install it using `pip`:

```
sudo apt install python3-pip
pip3 install requests
```

### 3. Download or Clone the Script

Download or clone the script from your GitHub repository (or copy and paste the code above into a `.py file):

```
git clone https://github.com/Night-Witch/PCPC.git
cd PCPC
```

### 4. Run the Script
You can now run the script from the terminal by specifying the URL, username, and desired password length as arguments.

Usage example:

```
python3 credential_tester.py https://example.com/login myusername 6
```

This will attempt to brute-force a password of 6 characters for the specified username against the given URL.


### Explanation of Arguments:

- `<url>` : The URL of the server where you want to send the login attempts.
- `<username>` : The username for which the password will be brute-forced.
- `<passwordLength>` : The length of the password you want to brute-force.


## Example:

```
python3 credential_tester.py https://example.com/login admin 8
```

This command will brute-force all possible 8-character passwords for the user "admin" at the provided URL. The script will output the password when the server returns a "Success" message.
