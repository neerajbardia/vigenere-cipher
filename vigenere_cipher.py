#vigenere cipher

def key_func(plain, key):                 					#function for key generation
	key = list(key) 
	if len(plain) == len(key): 
		return(key) 
	else: 
		for i in range(len(plain)-len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 

def encryption(plaintext, key): 							#encryption function
	cipher_text = [] 
	for i in range(len(plaintext)): 
		x=(ord(plaintext[i])+ord(key[i])) % 26
		x+=ord('A')
		cipher_text.append(chr(x)) 
	return("".join(cipher_text)) 
		
def decryption(cipher_text, key): 							#decryption function
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i])-ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x)) 
	return("" . join(orig_text)) 


#Initial execution

plain_text=input("Enter the plain text:")
KEY=input("Enter the key:")
key = key_func(plain_text,KEY)
print("Generated key:",key)
while (True):
    ch=0
    ch=int(input("1.Encryption \n2.Decryption \n3.Exit \nEnter your choice:"))
    if ch==1:
        cipher_text = encryption(plain_text,key)
        print("Cipher-Text :", cipher_text)
    elif ch==2:
        cipher_text=input("Enter the Cipher Text:")
        print("Plain-text:",decryption(cipher_text, key))
    else:
        exit()
