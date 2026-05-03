from encrypter import encrypt as enc
import sys

filefrom = sys.argv[1]
fileto = sys.argv[2]

if not filefrom:
    print(SyntaxError("No File Given to extract text"))

try:
    file = open(filefrom, "r")
    filecontent = file.read()
    encrypt = enc(filecontent, 3).encrypt()
    file.close()
    file = open(fileto, "w")
    file.write(encrypt)
    file.close()
    print("New encrypted file created at: {}".format(fileto))
except FileNotFoundError, OSError:
    print("There was an error getting into your file.")
    raise SyntaxWarning()

