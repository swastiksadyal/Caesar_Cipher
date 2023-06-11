# Caesar_Cipher
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabets

how it worksThe transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Cipher	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W
When encrypting, a person looks up each letter of the message in the "plain" line and writes down the corresponding letter in the "cipher" line.

Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
Deciphering is done in reverse, with a right shift of 3.

The replacement remains the same throughout the message, so the cipher is classed as a type of monoalphabetic substitution, as opposed to polyalphabetic substitution.

how to work with:
use encrypt.py to encrpt any message file and decrypt to decrypt it.
the key is stored in the code but can be stored in the form of a file and moved around as well.

for example:
to encrypt message.txt you will do: `python3 encrypt.py message.txt` you can use any file name there (the original file will be deleted after encryption)
to decrypt you can do `python3 decrypt.py encrypted_message.txt` and you will get your original message back.
