import collections
import string


Uppercase = collections.deque(string.ascii_uppercase)
Lowercase = collections.deque(string.ascii_lowercase)
Uppercase = ''.join(list(Uppercase))
message  = raw_input("type the message you want to decrypt: ")

#see all possible keys
for key in range(len(Uppercase)):
    translate = ''
    for symbol in message:
        if symbol in Uppercase:
            num = Uppercase.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(Uppercase)
            translate = translate + Uppercase[num]
        
        else:
            
            translate = translate+symbol
        
    print('Key #%s: %s' % (key, translate))
