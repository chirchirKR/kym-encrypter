# encrypter
# Use to encrypt a text by changing characters to different characters
# In other words it hides text to be human unreadable

print("-----------------------\nENCRYPTER FILE BY DEV-KYM DERICK\nV1.0.0\n----------------------\n")
class encrypt:
	def __init__(self,text="", to=0):
		self.readable_text = text
		self.changeto = to
		self.newtext = ""
		
	def encrypt(self):
		""" Encrypt given text by adding {__init__(..., to)} indexing
		with no given paramaters string type returned """
		
		
		
		#self.newtext = ""
		for character in self.readable_text:
			indexnumber = ord(character)
			indexnumber = indexnumber + self.changeto
			self.newtext += chr(indexnumber)

		return self.newtext

	def decrypt(self):
		""" Decrypt given text by subtracting {__init__(..., to)} indexing
		with no given paramaters string type returned """
		#print(self.readable_text)
		self.newtext = ""
		for character in self.readable_text:
			indexnumber = ord(character)
			indexnumber = indexnumber - self.changeto
			self.newtext += chr(indexnumber)

		return self.newtext
