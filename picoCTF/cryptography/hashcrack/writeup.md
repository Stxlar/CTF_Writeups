# 📝 Walkthrough – PicoCTF: Hash Crack

## 🔌 Step 1 – Connect to the Server

Run this command to start the challenge:

```bash
nc verbal-sleep.picoctf.net 52014
```

---

## 🧠 What's a Hash?

They first give you this hash:

```
482c811da5d5b4bc6d497ffa98491e38
```

A hash is the result of a string or data being processed by a one-way hash function (like **MD5** or **SHA1**). These functions are commonly used for verifying data integrity or storing passwords securely (well, they used to be... 😅).

---

## 🔍 Step 2 – Identify the Hash Type

There are different hashing algorithms, and each produces a hash of a specific length (in bits). To identify the hash type, you can count the bit length using Python:

```python
hex = "482c811da5d5b4bc6d497ffa98491e38"
print(int(hex, 16).bit_length())
```

Output:

```
127
```

Even though it says **127**, it's actually **128 bits**. That’s because `.bit_length()` excludes leading zeroes. Since the hash starts with `4` (which is `0100` in binary), one bit is dropped in the count.

If you search for "hash algorithms that generate 128-bit hashes", you’ll find that **MD5** is the most common one — though it's been broken for over 20 years.

Use an MD5 decryption tool (just search on google the following: MD5 decrypt) and input the hash. You’ll get:

```
password123
```

---

## 🔐 Step 3 – Crack the SHA-1 Hash

Next, they give you:

```
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
```

This is a **160-bit** hash → **SHA-1**.

Use an online SHA-1 decrypter. The result:

```
letmein
```

---

## 🔐 Step 4 – Crack the SHA-256 Hash

Final hash:

```
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
```

This is **256 bits**, which means it’s **SHA-256**.

Use a SHA-256 cracker (online or script-based). The result:

```
qwerty098
```

---

## 🏁 Final Step – Get the Flag

After entering all 3 cracked passwords, the challenge gives you the flag:

```
picoCTF{...}
```

---

## 📊 Hash Length Cheat Sheet

| Hash Type | Length (hex) | Bits | Example                    |
|-----------|---------------|------|----------------------------|
| MD5       | 32            | 128  | `482c811da5...`            |
| SHA-1     | 40            | 160  | `b7a875fc1e...`            |
| SHA-256   | 64            | 256  | `916e8c4f79...`            |

---

## 💡 Tip: Write Your Own Tools

Even though online tools are great, it’s better to script your own tools in Python (or whatever language you're comfortable with). Here's what I personally wrote/used:

---

### 🛠️ SHA-1 Cracker (with rockyou.txt)

```python
import hashlib

target = ""  # Enter your SHA-1 hash here

with open("rockyou.txt", "r", encoding="latin-1") as file:
    for word in file:
        word = word.strip()
        if hashlib.sha1(word.encode()).hexdigest() == target:
            print(f"[+] The password is : {word}")
            break
```

---

### 🛠️ SHA-256 Cracker (with rockyou.txt)

```python
import hashlib

target = ""  # Enter your SHA-256 hash here

with open("rockyou.txt", "r", encoding="latin-1") as file:
    for word in file:
        word = word.strip()
        if hashlib.sha256(word.encode()).hexdigest() == target:
            print(f"[+] The password is : {word}")
            break
```

---

✍️ Written by [Stxlar](https://github.com/Stxlar)
