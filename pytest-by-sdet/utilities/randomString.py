import random
import string

def random_string_generator(size = 5, chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choices(chars,k=size))