# utility file
# reusable helper functions
import os
import string

# returns a string with `length` characters chosen from `chars`
# len(generate_random_string(20) == 20

def random_string(length, chars=string.ascii_letters+string.digits):
    return ''.join([chars[i%len(chars)]\
        for i in [ord(x) for x in os.urandom(length)]])
