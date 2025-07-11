📝 Walkthrough – PicoCTF: Hash Crack
First, connect to the challenge server:

bash
Copy
Edit
nc verbal-sleep.picoctf.net 52014
They give you the first hash.
A hash is the result of a string or data being processed by a one-way hash function (like MD5 or SHA-1). These functions are used for verifying data integrity or storing passwords securely (well, they used to be 😅).

Here’s the first hash:

Copy
Edit
482c811da5d5b4bc6d497ffa98491e38
🔍 Step 1 – Identify the Hash Type
There are many hashing algorithms. To identify which one was used, we count how many bits the hash consists of.
Here’s a quick way to do that in Python:

python
Copy
Edit
hex = "482c811da5d5b4bc6d497ffa98491e38"
print(int(hex, 16).bit_length())
Output:

Copy
Edit
127
Even though it says 127, it’s actually a 128-bit hash. That’s because .bit_length() excludes leading 0s, and this hash starts with 4, which is 0100 in binary.

Looking up "hash algorithms that generate 128-bit", the most well-known is MD5 — which was broken over 20 years ago.

We use an MD5 online lookup tool, input the hash, and get:

nginx
Copy
Edit
password123
🔍 Step 2 – Crack the SHA-1 Hash
Next, they give us:

nginx
Copy
Edit
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Bit length: 160
This corresponds to SHA-1. Same deal — use an online SHA-1 lookup tool:

nginx
Copy
Edit
letmein
🔍 Step 3 – Crack the SHA-256 Hash
Final hash:

Copy
Edit
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Bit length: 256
This is SHA-256. Use a SHA-256 hash cracker or a script to brute-force:

nginx
Copy
Edit
qwerty098
🎉 Final Step
After entering the 3 cracked passwords, the challenge gives us the flag:

Copy
Edit
picoCTF{...} ✅
🔐 Hash Length Cheat Sheet
Hash Type	Length (hex)	Bits	Example
MD5	32	128	482c811da5...
SHA-1	40	160	b7a875fc1e...
SHA-256	64	256	916e8c4f79...

💡 Tip: Build Your Own Tools
Online hash lookup tools are useful, but for real challenges or automation, write your own scripts.

Here are two tools I built for this challenge:

🛠️ SHA-1 Cracker (using rockyou.txt)
python
Copy
Edit
import hashlib

target = ""  # Enter your SHA-1 hash

with open("rockyou.txt", "r", encoding="latin-1") as file:
    for word in file:
        word = word.strip()
        if hashlib.sha1(word.encode()).hexdigest() == target:
            print(f"[+] The password is: {word}")
            break
🛠️ SHA-256 Cracker (using rockyou.txt)
python
Copy
Edit
import hashlib

target = ""  # Enter your SHA-256 hash

with open("rockyou.txt", "r", encoding="latin-1") as file:
    for word in file:
        word = word.strip()
        if hashlib.sha256(word.encode()).hexdigest() == target:
            print(f"[+] The password is: {word}")
            break
