# Caesar Cipher Shift and Decode

import sys
from random import randrange

flags = open(sys.argv[1],"r")
wordlist = open("/usr/share/wordlists/fasttrack.txt","r")

with open("/usr/share/wordlists/fasttrack.txt") as w:
	words = w.read().splitlines()

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if (char.isalpha()):
            #char = char.upper()
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
        
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result

# Only can decrypt uppercase
"""def decrypt(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol.upper() in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))"""


# Encrypt flags
print('Encoded Flag,'+'Flag,'+'Method of Encoding')
for f in flags:
	rand_string = ""
	f = f.rstrip("\n")
	for w in range(0,5):
		rand_string += words[randrange(len(words))] + " "
	s = randrange(25) + 1
	text = rand_string + f
	enc_text = encrypt(text, s)
	#print("Flag: " + f)
	#print("Cipher: " + enc_text)
	#print("Shift: Caesar " + str(s))
	#print("")
	print(f+','+enc_text+','+'Caesar '+str(s))
