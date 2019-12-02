# utilities
generally useful things that were not made for any one specific project

1 - hashes.py : haveibeenpwned.com Pwned Passwords API checker python script

how to use - 
Make a file in the same directory as this script, called hashes.txt, that has utf-8 encoding (chances are it will unless another is intentionally selected).
Put all the passwords you want to check against the Pwned Passwords API in this file, line by line.
Run the script, and observe if it outputs 'Match found' after any Checking hash XX line. If it does, that means the last five characters of one of the password hashes were found in the API response.
The number shown matches the line in the file you put together, i.e. it's that passwords hash that had this hit.
It doens't necessarily mean that the entire hash was found, you will have to use the first five characters and the API to confirm.
This does provide a quick way to see if any passwords are in the database of pwned passwords.

See https://haveibeenpwned.com/ and particularly https://haveibeenpwned.com/API/v3 for background information.

Obviously, delete the file containing your passwords and clear your recycle bin after using this.
