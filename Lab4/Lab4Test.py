import Lab4
import math

def display(message):
   encrypted = Lab4.encrypt(message)
   decrypted = Lab4.decrypt(encrypted)
   x = 0
   print("Message: ", message)
   print("Message encrypted: ", end='')
   i = 0
   while i < len(encrypted):
       print(encrypted[i], " ", end='')
       i = i + 1
   print()
   print("Message decrypted: ", end='')
   while x < len(decrypted):

       print(decrypted[x], end='')
       x = x + 1
   print()

message1 = "JACKET"
message2 = "LINEAR"
message3 = "QUIZ"
display(message1)
display(message2)
display(message3)
