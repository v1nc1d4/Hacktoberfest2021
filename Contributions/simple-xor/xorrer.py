#!/usr/bin/env python
#cyberpj
input=raw_input("\nPlease Enter A data to Xor! >>> ")
print "\n"
print "--------H E L L O - X O R-------------"

def encryptDecrypt(input):
	key = ['P','J'] #edit as your wish
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)


def main():
	print " \n"
	
	encrypted = encryptDecrypt(input);
	print "Your Input = ",input;print " "
	print "Encrypted >> "+encrypted.decode('utf-8')
	print " "
	
	decrypted = encryptDecrypt(encrypted);
	print("Decrypted >> "+decrypted);

	print " "
	pass


if __name__ == '__main__':
	main()



