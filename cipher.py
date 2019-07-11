import sys
import os
import json
import fourCipher as fc


'''
def get_home_file_paths():
    dir_paths = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            dir_paths.append(os.path.join(root,name))
    print(dir_paths)
    return json.dumps(dir_paths)
'''


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'] 


def getData(dataInput): 	#get data from user

	
	data = []
	
	for char in dataInput.upper():
		if char.isalpha():
			data.append(char)
	return ''.join(data)
	
	
def makeMatrix(key): #creates a char array to be used as a matrix
	
	matrix = []
	counter = 0
	alphaCount = 0
	
	if key == '!':
		for char in alphabet:
			matrix.append(char)
	else:
		for char in key:
			matrix.append(char)
			counter += 1
		while (counter < len(alphabet)):
			if alphabet[alphaCount] not in key:
				matrix.append(alphabet[alphaCount])
				alphaCount += 1
				counter += 1
			else:
				alphaCount += 1
	
	return ''.join(matrix)

def printMatrix(matrix): #prints the char array as a matrix

	counter = 0
	for x in range(5):
		print("\n")
		for y in range(5):
			print (matrix[counter], end=' ')
			counter += 1
	print("\n\n")
			
	
	
def removeDuplicates(str): #removes duplicates from keys
    result=[]
    seen=set()
    for char in str:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
	

	
#evaluate function: used to determine which index position on the 
#    mirror matrix the key is located
def evaluate(ref1, ref2):	
	return ((int(ref1 / 5) * 5) + (ref2 % 5))

	
	
	
#searches for the position index of the message letter in the ref matrix
def search (ref, letter):
	counter = 0
	if letter == 'Z':
		return -1
	for char in ref:
		if ref[counter] == letter:
			return counter
		counter += 1
	pass
	
	
	

	
	
	
#Encryption function
#NOTE need to add a case when message last position is even to append original character
def encrypt(message , key1, key2):


	key1 = removeDuplicates(key1)
	matrix1 = makeMatrix(key1)
	
	
	key2 = removeDuplicates(key2)
	matrix2 = makeMatrix(key2)
	
	refMatrix = makeMatrix('!')
	
	#print ("*****Key 1 Block*****")
	#printMatrix(matrix1)
	#print ("*****Key 2 Block****")
	#printMatrix(matrix2)
	#print ("****Reference block*****")
	#printMatrix(refMatrix)
	
	encrypted = []
	counter = 0
	
	set = []
	
	while (counter < len(message)):
		
		aPosition = search(refMatrix, message[counter])
		if counter != len(message)-1:
			bPosition = search(refMatrix, message[counter + 1])
		if message[counter] != 'Z':
			set.append(matrix1[evaluate(aPosition,bPosition)])
		else:
			set.append('Z')
		
		if counter == len(message) - 1:
			return ''.join(set)
		elif message[counter] != 'Z':
			set.append(matrix2[evaluate(bPosition,aPosition)])
			#set.append(matrix1[evaluate(search(refMatrix,message[counter+1]),search(refMatrix,message[counter]))])
		else:
			set.append('Z')
		
		counter += 2
		#encrypted.append(set)

	return ''.join(set)
	
	
# DECRYPTION function
#NOTE need to add a case when message last position is even to append original character
def decrypt(message , key1, key2):


	key1 = removeDuplicates(key1)
	matrix1 = makeMatrix(key1)
	
	
	key2 = removeDuplicates(key2)
	matrix2 = makeMatrix(key2)
	
	refMatrix = makeMatrix('!')

	counter = 0
	
	set = []
	
	while (counter < len(message)):
		
		aPosition = search(matrix1, message[counter])
		if counter != len(message)-1:
			bPosition = search(matrix2, message[counter + 1])
		
		if message[counter] != 'Z':
			set.append(refMatrix[evaluate(aPosition,bPosition)])
		else:
			set.append('Z')
		

		if counter == len(message) - 1:
			return ''.join(set)
		elif message[counter] != 'Z':
			set.append(refMatrix[evaluate(bPosition,aPosition)])
			#set.append(matrix1[evaluate(search(refMatrix,message[counter+1]),search(refMatrix,message[counter]))])
		else:
			set.append('Z')
		
		counter += 2
		#encrypted.append(set)

	return ''.join(set)

	
#main function	
def main():

    key1 = []
    key2 = []
    msg = []
    enCr = []
    deCr = []

    key1 = getData(sys.argv[1])
    key2 = getData(sys.argv[2])
    msg = getData(sys.argv[3])
    #print ("****** Four Square Cipher *******\n")
    #print ("Key 1: ", key1)
    #print ("Key 2: ", key2)
    #print ("Key 3: ", key3)
        
    enCr = encrypt ( msg, key1 , key2)

    print ("<br><b>Encrypted message:</b> ", enCr)




    deCr = decrypt ( enCr, key1 , key2)
    print ("<br><br><b>Decrypted message:</b> ", deCr)



if __name__ == "__main__":
	main()

#print(encrypt ( msg, key1 , key2))
#print (msg)
#print (key1)
#print (key2)
#print(decrypt ( enCr, key1 , key2))





#print (enCr)
#print (deCr)

'''	
#main function	
def main():

	print ("****** Four Square Cipher *******\n")
	
	#print ("Enter Key 1: ", end=' ')	
	key1 = sys.argv[1]
	

	#print ("\nEnter Key 2: ", end=' ')
	key2 = sys.argv[2]

	#print ("\nEnter the message to encrypt (only A-Z):", end=' ')
	message = sys.argv[3]
	
	enCr = encrypt ( message, key1 , key2)

	print ("\nEncrypted message: ")
	print (enCr)

	print ("\n\nDecrypted message: ")
	deCr = decrypt ( enCr, key1 , key2)
	print (deCr)
'''