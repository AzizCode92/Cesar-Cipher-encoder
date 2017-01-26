#!/usr/bin/python


import collections
import string



def cesar_cipher(plaint_text, rotate_number):
    
    Uppercase = collections.deque(string.ascii_uppercase)
    Lowercase = collections.deque(string.ascii_lowercase)
    
    Uppercase.rotate(rotate_number)
    Lowercase.rotate(rotate_number)
    
    Uppercase = ''.join(list(Uppercase))
    Lowercase = ''.join(list(Lowercase))
    return plaint_text , plaint_text.translate(string.maketrans(string.ascii_uppercase,Uppercase)).translate(string.maketrans(string.ascii_lowercase,Lowercase))

print cesar_cipher(raw_input("Type your plaintext here : "), input("type the rotate_number : ") ) 
