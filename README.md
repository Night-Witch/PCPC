Replace the URL: Change url = "http://example.com/login" to the actual server address you want to test.
Username: Replace "myusername" in the call to brute_force_password with the actual username for which you are trying to guess the password.
Check for Success: Make sure the condition for success in the line if "Success" in response.text: accurately reflects the server's response. If the server returns a different text or status code, modify this condition accordingly.
Run the Program: This code will iterate through all possible combinations of passwords of length 4 for the specified username. You can change the length by modifying the last parameter in the call to brute_force_password.
