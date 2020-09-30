    dict = {
   "A": 0, "B": 1,"C": 2, "D": 3,"E": 4,
   "F": 5, "G": 6,"H": 7, "I": 8,"J": 9,
   "K": 10,"L": 11, "M": 12, "N": 13, "O":14,
   "P": 15, "Q":16, "R":17, "S":18, "T":19, "U":20,
   "V": 21, "W": 22, "X":23,"Y":24, "Z":25
}
# Encrypts with affine and then with rsa
def encrypt(message):
   affine_enc = affine_encrypt(message)
   encrypted = rsa_encrypt(affine_enc)
   return encrypted

def affine_encrypt(message):
   # Affine encryption f(p) = (ap+b)mod26
   # Our key f(p) = (3p+4)mod26 where a = 3, b = 4
   a = 3
   b = 4
   x = 0
   affine_list = []  # List containing numbers for affine encryption
   while x < len(message):  # Loop terminates when x exceeds length of message
       num = dict[list(message)[x]]  # Translates letter to number form 0-25
       affine_list.append(num)  # Add number to list
       x = x + 1
   y = 0
   while y < len(affine_list):
       affine_list[y] = ((a * affine_list[y]) + b) % 26  # Affine encryption with f(p)
       y = y + 1
   affine_list = trans_eng(affine_list)
   return affine_list



def rsa_encrypt(affine):
   # RSA ENCRYPTION AFTER AFFINE ENCRYPTION
   # p = 53 q = 31 e = 11
   p = 53
   q = 61
   e = 11
   a = 0
   affine_list = []
   while a < len(affine):  # Loop terminates when x exceeds length of message
       num = dict[list(affine)[a]]  # Translates letter to number form 0-25
       affine_list.append(num)  # Add number to list
       a = a + 1
   if gcd((p - 1) * (q - 1), e) == 1:
       z = 0
       rsa_list = []
       while z < len(affine_list) - 1:  # This loop turns the list of numbers 4 digit blocks
           if affine_list[z + 1] < 10:  # Adds a 0 before second index if less than 10
                                        # Ex: Combining 12 and 4 ----> 1204 NOT 124
               block = int(str(affine_list[z]) + str(0) + str(affine_list[z + 1]))
           else:
               block = int(str(affine_list[z]) + str(affine_list[z + 1]))
           rsa_list.append(block)
           z = z + 2

       if len(affine_list) % 2 != 0:  # Adds leftover block if odd numbered
           rsa_list.append(affine_list[len(affine_list) - 1])
       x = 0
       while x < len(rsa_list):
           rsa_list[x] = rsa_list[x] ** e % (p * q)  ## RSA encryption with C^emodpq
           x = x + 1
       return rsa_list  # Returns rsa encrypted list

# Takes in an affine & rsa encrypted list
# Decrypts with rsa and then with affine
def decrypt(encrypted):
   first_dec = rsa_decrypt(encrypted)
   decrypted = affine_decrypt(first_dec)
   return decrypted

def rsa_decrypt(encrypted):
   # encrypted is a list
   # Returns a string list ready for affine decryption
   decrypted_list = []
   p = 53
   q = 61
   e = 11
   if gcd((p-1)*(q-1),e) == 1 :  # Check if inverse exists
       d = inverse_mod(e,(p-1)*(q-1))  # Finds decryption key through inverse of emod(p-1)(q-1)
   x = 0
   while x < len(encrypted):
       decrypted = str(encrypted[x]**d%(p*q))
       if len(str(decrypted)) <= 2:
           decrypted_list.append("00" + decrypted) # Adds 0 as a placeholder for a 4 digit block
                                                   # EX: Result of 14 ----> 0014
       else:
           decrypted_list.append(decrypted) # Apply M = C**dmod(p*q)
       x = x + 1
   decrypted_list = split_blocks(decrypted_list) # Splits blocks up
   return decrypted_list

def affine_decrypt(rsa_dec):
   # Decrypt affine with f(p) = 3p+4mod26 by using inverse of f(p)
   a = 3
   b = 4
   af_list = []
   x = 0
   inverse = inverse_mod(a, 26) # First find inverse of a
   while x < len(rsa_dec):
       c = inverse * (int(rsa_dec[x]) - b) % 26  # Multiply inverse of "a" by (p-b)mod26
       af_list.append(c)
       x = x + 1
   af_list = trans_eng(af_list)  # Translates back to letters
   return af_list

# Splits 4 digit blocks into respective forms
# Ex: 0401 = 4,1
# Ex: 318 = 3,18
def split_blocks(blocks):
# Returns an int list
# IMPORTANT NOTE: blocks is a string list and we must preserve the "00" placeholder for some cases
# Ex: Calling int(0014) will leave us with 14, but we want 0,14 after the split so we manually add a 0
   x = 0
   splitted = []
   while x < len(blocks):
       to_split = blocks[x]
       if (len(to_split) == 3) & (int(to_split[1]) == 0): # Ignores precursor "0" if block of length 3
           splitted.append(int(to_split[0]))
           splitted.append(int(to_split[2]))
       elif len(to_split) == 3:            # If block of length 3, split into 1st and last 2 digits
           splitted.append(int(to_split[0]))
           splitted.append(int(to_split[1:]))
       else:                               # Splits block into 2's if of length 4
           splitted.append(int(to_split[:2]))
           splitted.append(int(to_split[2:4]))
       x = x + 1
   return splitted

# Translates numbers into letters
def trans_eng(numbers):
   x = 0
   translated = []
   key_list = list(dict.keys())    # List of keys(letters)
   val_list = list(dict.values())  # List of values(numbers)
   while x < len(numbers):
       eng = key_list[val_list.index(int(numbers[x]))] # Gets key(letter) through calling index of value(number)
       translated.append(eng)
       x = x + 1
   return translated

def gcd(a,b):
   x = a
   y = b
   while(y!=0):
       r = x % y
       x = y
       y = r

   return x


def inverse_mod(inv, a):
   if (gcd(inv, a) == 1):
       x = 1
       while x < a:
           y = x * inv
           if (y % a == 1):
               return x
           x = x + 1
