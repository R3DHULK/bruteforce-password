import hashlib

pass_found = 0

input_hash = input(" [+] Enter The Hashed Password : ")
pass_doc = input ("\n [+] Enter passwords filename including path : ")

try:
	pass_file = open(pass_doc, 'r')
except :
	print("\n\tError \n")
	print(pass_doc, "is not found.\n [?] Please give path of file correctly.")
	input(" \n[+] Enter To Exit")
	quit()
for word in pass_file:
	enc_word = word.encode('utf-8')
	hash_word = hashlib.md5(enc_word.strip())
	digest = hash_word.hexdigest()
	
	if digest == input_hash:
		
		print(" [+] Password found.\nThe password is : ", word)
		pass_found = 1
		break
		
if not pass_found:
	print(" [+] Password is not found in the", pass_doc, "file")
	print("\n")
input(" [+] Enter To Exit")
