from encrypter import encrypt as enc

encrypt = enc("THIS FILE USES ENCRYPTION FILE", 3).encrypt()

# Returns WKLV#ILOH#XVHV#HQFU\SWLRQ#ILOH

print(encrypt)

decrypt = enc(encrypt,3).decrypt()

# Returns THIS FILE USES ENCRYPTION FILE

print(decrypt)
