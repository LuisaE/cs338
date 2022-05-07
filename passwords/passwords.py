# Names: Luisa Escosteguy, PJ Sangvong
import hashlib
import binascii

dict = {}

def build_dictionary():
    words = [line.strip().lower() for line in open('temp/words.txt')]
    for word in words:
        encoded_password = word.encode('utf-8')
        hasher = hashlib.sha256(encoded_password)
        digest = hasher.digest() 
        digest_as_hex = binascii.hexlify(digest)
        digest_as_hex_string = digest_as_hex.decode('utf-8')
        if digest_as_hex_string not in dict:
            dict[digest_as_hex_string] = word

def crack_passwords1():
    passwords = [line.strip().lower() for line in open('temp/password1.txt')]
    with open('cracked1.txt', 'w') as f:
        for password in passwords:
            hash = password.split(":",2) 
            if hash[1] in dict:
                f.write(hash[0]+":"+dict[hash[1]]+"\n")



build_dictionary()
crack_passwords1()
