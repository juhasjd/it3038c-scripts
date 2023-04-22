#The following script generates a 10 digit password with atleast 3 special char
#Idea for script comes from
#Simran Kaur Arora
#March 23, 2023

import secrets
import string

#defines the name of the variables, names the fuction, and sets the length of the password
def pw_gen(pw_length=10):
   abcs = string.ascii_letters
   numbers = string.digits
   specials = string.punctuation

   alphabet = abcs + numbers + specials
   password = ''

#starts password off as a weak password
   strong_pw = False

   while not strong_pw:
       password = ''
       for i in range(pw_length):
           password += ''.join(secrets.choice(alphabet))

#needs at least 3 special char for the password to be considered strong
       if (any(char in specials for char in password) and
               sum(char in numbers for char in password) >= 3):
           strong_pw = True

   return password


if __name__ == '__main__':
   print(pw_gen())