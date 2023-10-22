# CYB333-Project
Objective:
To develop a simple secure and user-friendly password manager tool that allows users to generate, save, retrieve, and assess the strength of passwords.

Features:

Master Password Protection:

Before accessing any functionality, the user must enter a master password.
The master password is hashed using the SHA-256 algorithm for added security.
If the tool is run for the first time, the user will be prompted to set a master password.
Password Generation:

Generate a random password based on user-defined criteria:
Length of the password.
Inclusion of uppercase letters.
Inclusion of digits.
Inclusion of special characters.
Password Storage:

Save passwords securely in a file (passwords.txt).
Each entry will have the site or service name, username, and the password.
Password Retrieval:

Retrieve and display all saved passwords from the file.
Password Strength Assessment:

Check the strength of a generated or entered password.
Categorize the password as "Weak", "Moderate", or "Strong" based on its composition.
Break Time Estimation:

Estimate the time required to break the password using brute force.
Provide an estimation in years based on 10 billion guesses per second.
User Interface:
A simple command-line interface with the following options:

Generate a new password.
Save a password.
Retrieve saved passwords.
Exit the tool.
Security Measures:

Use of the getpass module to securely input passwords without displaying them on the screen.
Hashing the master password using the SHA-256 algorithm.
Regular expressions to assess password strength.
Dependencies:

Python Standard Libraries: random, string, getpass, re, hashlib, os.
Future Enhancements (Not part of the current scope):

Encrypt the passwords.txt file for added security.
Implement a search functionality to retrieve passwords for specific sites or services.
Integrate with a cloud storage solution for backup and synchronization across devices.
Conclusion:
The Password Manager Tool aims to provide a secure and efficient way for users to manage their passwords. With the integration of a master password and various features, users can ensure their passwords are both safe and strong.
