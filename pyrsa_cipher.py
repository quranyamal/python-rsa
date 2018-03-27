def get_key_values(filename):
   fo = open(filename, "r")
   s = fo.readline()
   s = fo.readline() # the key is in the second line
   e = int(s)
   s = fo.readline() # the key is in the second line
   n = int(s)

   return [e,n]


def get_message_blocks(inputfile):
   with open(inputfile, "r") as message_file:
      message = message_file.read()
   print "\nmessage = ", message   

   message_num = ""


   for ch in message:
      message_num += str(ord(ch))

   len_message_num = len(message_num)
   len_block = 3
   num_block = len_message_num/len_block + len_message_num%len_block

   print "num_block", num_block

   m = []
   for i in range(0, num_block):
      m_block = message_num[i*len_block:(i+1)*len_block]
      mi = int(m_block)
      print "m[",i ,"] = ", mi
      m.append(mi)

   return m   

def encrypt(inputfile, output, pubkey):
   print "encrypting:", inputfile, "| with key:", pubkey, "| save to:", output

   key = get_key_values(pubkey)
   message_blocks = get_message_blocks(inputfile)
   e,n = key[0],key[1]

   print "==== encrytpting ===="
   print
   print "message_blocks=",message_blocks
   print "e=",e," n=",n, "\n"

   cipher = []
   cipher_str = ""

   fo = open(output, "w")

   for i in range(0, len(message_blocks)):
      c = (message_blocks[i]**e) % n
      cipher.append(c)
      fo.write(str(c))
      fo.write("\n")

   print "cipher = ", cipher


def decrypt(inputfile, outputfile, prikey):
   print "==== decrypting ===="

   key = get_key_values(prikey)
   d,n = key[0],key[1]

   with open(inputfile, "r") as message_file:
      message = message_file.read()
   print "\nmessage = ", message  

   chipher_blocks = map(int,message.split())
   print chipher_blocks

   decoded = []
   plain_raw = ""
   for i in range(0, len(chipher_blocks)):
      p = (chipher_blocks[i]**d) % n
      decoded.append(p)
      print "decripting m-",i
      plain_raw += str(p)

   print decoded

   char_values = map(int,[plain_raw[i:i+2] for i in range(0, len(plain_raw), 2)])

   plain = ""

   for i in char_values:
      plain += str(unichr(i))

   print "plain text:",plain
   with open(outputfile, "w") as message_file:
      message = message_file.write(plain)