import hashlib

target = "" #enter your target/hash

#rockyou.txt is a file that contains the most popular passwords used
with open("rockyou.txt", "r") as file:
    for word in file:
        word = word.strip()
        #you turn the word into binary so that the sha1 algorithm can process it and then we turn it into hexadecimal
        if hashlib.sha1(word.encode()).hexdigest() == target:
            print(f"[+] The password is : {word}")
            break
