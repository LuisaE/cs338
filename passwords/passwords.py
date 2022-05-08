# Names: Luisa Escosteguy, PJ Sangvong
import hashlib
import binascii
import random

dict = {}
dict_two_word = {}

def hash_string(word):
    encoded_password = word.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest() 
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string
 

def build_dictionary():
    words = [line.strip().lower() for line in open('temp/words.txt')]
    for word in words:
        digest_as_hex_string = hash_string(word)
        if digest_as_hex_string not in dict:
            dict[digest_as_hex_string] = word


def build_two_word_dict():
    '''
    Takes too long
    '''
    words = [line.strip().lower() for line in open('temp/words.txt')]
    for word1 in words:
        for word2 in words:
            word = word1+word2
            digest_as_hex_string = hash_string(word)
            if digest_as_hex_string not in dict:
                dict_two_word[digest_as_hex_string] = word


def crack_passwords1():
    passwords = [line.strip().lower() for line in open('temp/password1.txt')]
    with open('cracked1.txt', 'w') as f:
        for password in passwords:
            hash = password.split(":",2) 
            if hash[1] in dict:
                f.write(hash[0]+":"+dict[hash[1]]+"\n")


def crack_password(password_path, output_name, dict):
    passwords = [line.strip().lower() for line in open(password_path)]
    with open(output_name, 'w') as f:
        for password in passwords:
            hash = password.split(":",2) 
            if hash[1] in dict:
                f.write(hash[0]+":"+dict[hash[1]]+"\n")


def randomized_crack(password_path, output_name):
    words = [line.strip().lower() for line in open('temp/words.txt')]
    passwords = [line.strip().lower() for line in open(password_path)]
    passwords_dict = {}
    with open(output_name, 'w') as f:
        for password in passwords:
            hash = password.split(":",2) 
            passwords_dict[hash[1]] = hash[0]
        
        for _ in range(1000000000):
            rand_word1, rand_word2 = random.choices(words, k=2)
            rand_word = rand_word1 + rand_word2
            rand_hash = hash_string(rand_word)
            if rand_hash in passwords_dict:
                f.write(passwords_dict[rand_hash]+":"+rand_word+"\n") 
        


def part1():
    '''
    Cracks unsalted one-word passwords
    '''
    build_dictionary()
    crack_password('temp/password1.txt', 'cracked1.txt', dict)


def part2():
    '''
    Cracks unsalted two-word passwords
    '''
    # build_two_word_dict() # takes too long
    # crack_password('temp/password2.txt', 'cracked2.txt', dict_two_word)
    
    randomized_crack('temp/password2.txt', 'cracked2.txt')



if __name__ == '__main__':
    # part1()
    part2()
