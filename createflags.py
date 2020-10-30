from random import randrange

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(25):
    letters = ''
    digits = ''
    for j in range(5):
        letters += alpha[randrange(26)]
    for k in range(5):
        digits += str(randrange(10))
    print("CAHSI-"+letters+"-"+digits)
