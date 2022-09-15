infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

encryption_key = {' ' : ' '} # written to handle spaces
contents = str(infile.read())

letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm:."
hash = "!@#$%^&*)(_+=-~1029384756ZxCvBnMaSdFgHjKlPoIuYtReWqQET"

for i in range(0, len(letters)):
    if letters[i] not in encryption_key:
        encryption_key[letters[i]] = hash[i]

encrypted_text = ""

for i in contents:
    encrypted_text += encryption_key[i]

outfile.write(encrypted_text)


