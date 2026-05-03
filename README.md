#  Simple Python Encrypter

A lightweight Python tool for encrypting and decrypting text using
character shifting.

------------------------------------------------------------------------

##  Description

This project implements a basic encryption system similar to a Caesar
cipher.\
It transforms readable text into an unreadable format by shifting each
character's ASCII value.

------------------------------------------------------------------------

##  Features

-   Encrypt any string\
-   Decrypt back to original text\
-   Simple and easy-to-understand code\
-   No external libraries required

------------------------------------------------------------------------

##  Files

```python
encrypter.py \# Contains encryption class\
main.py \# Example usage
```

------------------------------------------------------------------------

##  Usage

### Import the class

```python
from encrypter import encrypt as enc
```

------------------------------------------------------------------------

### Encrypt text

```python
encrypted = enc("THIS FILE USES ENCRYPTION FILE", 3).encrypt()\
print(encrypted)
```

Output:

```txt
WKLV#ILOH#XVHV#HQFU`\SWLRQ`{=tex}#ILOH
```

------------------------------------------------------------------------

### Decrypt text

```python
decrypted = enc(encrypted, 3).decrypt()\
print(decrypted)
```

Output:
```txt
THIS FILE USES ENCRYPTION FILE
```

------------------------------------------------------------------------

##  How It Works

-   Each character is converted to ASCII using ord()\
-   A shift value is added (encryption) or subtracted (decryption)\
-   Converted back using chr()

------------------------------------------------------------------------

##  Warning

This is a basic encryption method and NOT secure for real-world
sensitive data.\
Use it for learning or simple obfuscation only.

------------------------------------------------------------------------

##  Author

Dev-KYM Derick

------------------------------------------------------------------------

##  License

Free to use and modify.
