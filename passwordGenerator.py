import random
import string

while 1:
    password_len = int (input("what length would you like your password to be:"))
  
    for x in range(0,password_len):
        def generator_password(password_len):
            alphabet = string.ascii_lowercase +string.ascii_uppercase+string.digits+string.punctuation
            return ''.join(random.choice(alphabet) for i in range(password_len))

   
    print(generator_password(password_len))
     