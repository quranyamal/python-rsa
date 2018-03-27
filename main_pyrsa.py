import sys, getopt

from pyrsa_keygen import *
from pyrsa_cipher import *

def main(argv):

   if len(argv)==0:
      print "usage: pyrsa.py <arg>"
      print "arg: genkeypair | encrypt | decrypt"
   elif argv[0] =='genkeypair':
      print generate_keypair()
   elif argv[0] == 'encrypt':
      if len(argv) != 4:
         print "usage: pyrsa.py encrypt <file_to_encrypt> <output_file> <pubkey_file>"
         print "exple: pyrsa.py encrypt message.txt cipher.txt rsa.pub"
      else:
         input_file = argv[1]
         output_file = argv[2] 
         pubkey = argv[3]
         encrypt(input_file, output_file, pubkey)
   elif argv[0] == 'decrypt':
      if len(argv) != 4:
         print "usage: pyrsa.py decrypt <file_to_decrypt> <output_file> <prikey_file>"
         print "exple: pyrsa.py decrypt cipher.txt decrypted-message.txt rsa.pri"
      else:
         input_file = argv[1]
         output_file = argv[2] 
         prikey = argv[3]
         decrypt(input_file, output_file, prikey)

if __name__ == "__main__":
   main(sys.argv[1:])