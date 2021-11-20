# Image encryption by RSA algorithm

An application that encrypts an image file using RSA encryption algorithm, which is an assymetrical block cipher encryption method.

## How to use this program?

### Encryption

Step 1: Generate a pair of public and private key.\
Step 2: Input the path to the image you want to encrypt.\
Step 3: Next enter the public key (n and e). This will encrypt the image.

### Decryption

Step 1: Input the path of the encrypted image.\
Step 2: Next, input your private key (n and d). At this step, you need to ensure the entered private key is the one generated alongwith the public key used for encryption. Else the image might be lost forever.\
Step 3: Image gets decrypted and can be displayed.
