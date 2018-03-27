from pyrsa_math import *

e,p,q,n,totient_euler = -1, -1, -1, -1, -1

def generate_keypair():
   print "generating keypair"

   init_global_var()
   generate_pubkey()
   generate_privkey()

def init_global_var():
   global p,q,n,totient_euler

   p = next_prime(45)   # contoh. harusnya di random, pake bignum
   q = next_prime(69)   # contoh. harusnya di random, pake bignum

   totient_euler = (p-1)*(q-1)
   n = p*q

def generate_pubkey():
   print "generating public key"
   
   global e,n

   e = next_prime(75)
   print "e = ", e

   fo = open("rsa.pub", "w")
   fo.write("-----BEGIN RSA PUBLIC KEY-----\n")
   fo.write(str(e) + "\n")
   fo.write(str(n) + "\n")
   fo.write("---END RSA PUBLIC KEY---")   

def generate_privkey():
   print "generating private key"
   global e,p,q,n

   d = modinv(e, totient_euler)

   print "p = ", p
   print "q = ", q
   print "n = ", n
   print "totient_euler = ", totient_euler
   print "e = ", e
   print "d = ", d

   fo = open("rsa.pri", "w")
   fo.write("-----BEGIN RSA PRIVATE KEY-----\n")
   fo.write(str(d) + "\n")
   fo.write(str(n) + "\n")
   fo.write("---END RSA PRIVATE KEY---")  