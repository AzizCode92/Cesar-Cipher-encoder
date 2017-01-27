#!/usr/bin/python


import collections
import string



def cesar_cipher(plaint_text, rotate_number,encoder):

    Uppercase = collections.deque(string.ascii_uppercase)
    Lowercase = collections.deque(string.ascii_lowercase)


    if encoder == False :
        rotate_number = (-1) * rotate_number
    Uppercase.rotate(rotate_number)
    Lowercase.rotate(rotate_number)
    Uppercase = ''.join(list(Uppercase))
    Lowercase = ''.join(list(Lowercase))

    return plaint_text , plaint_text.translate(string.maketrans(string.ascii_uppercase,Uppercase)).translate(string.maketrans(string.ascii_lowercase,Lowercase))



print cesar_cipher(raw_input("Type your plaintext/Ciphertext here : "), input("type the rotate_number : "),input("encoder (True)/decoder(False)?:") )
