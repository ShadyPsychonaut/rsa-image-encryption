
# Created by sarthak on 11/13/21.

from typing import List
from PIL import Image
import random
import math

from numpy import array


class RSA_Encryption:

    def hcf(a, b):
        if(b == 0):
            return a
        else:
            return RSA_Encryption.hcf(b, a % b)

    def extendedEuclid(a, b):
        if(b == 0):
            return a, 1, 0

        gcd, x1, y1 = RSA_Encryption.extendedEuclid(b, a % b)
        x = y1
        y = x1 - (a//b) * y1

        return gcd, x, y

    def fetchImage():
        try:

            # input path to the image from user
            path = input(r'Enter path of image : ')

            # opening the file for reading purpose
            fileInput = open(path, 'rb')

            image = fileInput.read()
            fileInput.close()

            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            return path, image

        except IOError:
            print('Path not found : ', Exception.__name__)

    def pub_keygen():
        prime_nos = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

        p = prime_nos[random.randint(0, len(prime_nos)-1)]
        q = prime_nos[random.randint(0, len(prime_nos)-1)]

        if(p == q):
            q = prime_nos[random.randint(0, len(prime_nos)-1)]

        # First part of public key
        n = p * q

        # Other part of the public key (Public exponent)
        # calcualting Euler's totient function
        phi_n = (p - 1) * (q - 1)

        # print(phi_n)

        e = 2

        while(e < phi_n):
            # e must be co-prime to phi and
            # smaller than phi
            if(RSA_Encryption.hcf(e, phi_n) == 1):
                break
            else:
                e = e + 1

        return n, e, phi_n

    def pvt_keygen(phi_n, e):

        d = 1

        # Hit and Trial method for finding d
        for d in range(phi_n):
            if(math.fmod(e*d, phi_n) == 1):
                return d

        # # Extended Euclid algorithm to find k
        # gcd, x, y = RSA_Encryption.extendedEuclid(phi_n, e)

        # if(x > y):
        #     k = x
        # else:
        #     k = y

        # print("Value of k is", k)
        # print(gcd)

        # while (True):
        #     d = (1 + (k * phi_n))/e
        #     if(d.is_integer() == True):
        #         return d
        #     else:
        #         k = k + 1

    def encrypt(n, e):

        path, image = RSA_Encryption.fetchImage()

        n_u = int(input("Input public key value n : "))
        e_u = int(input("Input public key exp e : "))

        if(n != 0):
            if(n_u != n or e_u != e):
                print("Invalid key values.")
                return
        else:
            n = n_u
            e = e_u

        in_c = []

        for index, values in enumerate(image):
            if(values > 1):
                c = pow(values, e, mod=n)
                if(c < 256):
                    image[index] = c
                    in_c.append(index)
                    # print('Encrypted data :', image[index])
                    if(len(in_c) > 1000):
                        break

        print('\nFinal list of encrypted indices :')
        i = 0
        for i in range(0, len(in_c)-1):
            print('', in_c[i], end='')
        print("\nTotal indices encrypted :", len(in_c))

        # Opening file for writing
        fileInput = open(path, 'wb')

        # writing encryted data in image
        fileInput.write(image)
        fileInput.close()

        print('Image encrypted!')

        return in_c

    def decrypt(in_c, n, d):

        path, image = RSA_Encryption.fetchImage()

        n_u = int(input("Enter private key n : "))
        d_u = int(input("Enter private key exponent d : "))

        if(d != 0):
            if(n_u != n or d_u != d):
                print('Invalid key entered. Try again!')
                return
        else:
            n = n_u
            d = d_u

        for index, values in enumerate(in_c):
            # print("List index :", index)
            p = pow(image[values], d, mod=n)
            image[values] = p

        fileInput = open(path, 'wb')
        fileInput.write(image)
        fileInput.close()

        print('Image decrypted!')

        img = Image.open(path)
        img.show()


n = 0
e = 0
phi_n = 0
d = 0
in_c = []

while True:
    print('\nImage Encryption Application')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Generate public key')
    print('4. Generate private key')
    print('5. View Image')
    print('6. Exit')

    opt = int(input('Select option : '))

    if (opt == 1):
        in_c = RSA_Encryption.encrypt(n, e)
    elif(opt == 2):
        RSA_Encryption.decrypt(in_c, n, d)
    elif(opt == 3):
        n, e, phi_n = RSA_Encryption.pub_keygen()
        print(f'\nThe public key is [n : {n}], [e : {e}]')
    elif(opt == 4):
        d = RSA_Encryption.pvt_keygen(phi_n, e)
        print(f'\nThe Private Exponent is [n : {n}] [d : {d}]')
    elif(opt == 5):
        path = RSA_Encryption.fetchImage()[0]
        try:
            img = Image.open(path)
            img.show()
        except Exception:
            print('\nImage data encrypted', Exception.__name__)
    elif(opt > 5):
        break
