# EncryEngChar function used to encrypt English words
def EncryEngChar():
    result = ""
    key = input("Please Enter Size Of Encryption Key: ")
    EngChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    while not key.isnumeric():
        print("Please Enter Numbers Only.")
        encryption()
    if 0 < int(key) < 27:
        plaintxt = list(input("Please Enter The Text To Encrypt: ").upper())
        print(plaintxt)
        print(EngChar)
        for i in range(0, len(plaintxt)):
            for j in range(0, len(EngChar)):
                if plaintxt[i] == EngChar[j]:
                    x = j + int(key)
                    if x <= 25:
                        result += EngChar[(j + int(key))]
                    else:
                        result += EngChar[(x - 26)]
        print("Your Cipher Text is:- " + result)
        main()
    else:
        print("Your Key Must Be Between 1-26")
        EncryEngChar()


# DecryEngChar function used to decrypt English words
def DecryEngChar():
    result = ""
    key = input("Please Enter Size Of Decryption Key: ")
    EngChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    while not key.isnumeric():
        print("Please Enter Numbers Only.")
        decryption()
    if 0 < int(key) < 27:
        plaintxt = list(input("Please Enter The Text To Decrypt: ").upper())
        print(plaintxt)
        print(EngChar)
        for i in range(0, len(plaintxt)):
            for j in range(0, len(EngChar)):
                if plaintxt[i] == EngChar[j]:
                    res = j - int(key)
                    if res < 0:
                        result += EngChar[j - int(key)]
                    else:
                        result += EngChar[j - int(key)]
        print("Your Plain Text is:- " + result)
        main()
    else:
        print("Your Key Must Be Between 1-26")
        DecryEngChar()


# EncryTurkChar function used to encrypt Turkish words
def EncryTurkChar():
    result = ""
    key = input("Lütfen Şifreleme Anahtarını Giriniz: ")
    TurkChar = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J',
                'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü',
                'V', 'Y', 'Z']
    while not key.isnumeric():
        print("Lütfen Sadece Numara Giriniz.")
        encryption()
    if 0 < int(key) < 30:
        plaintxt = list(input("Lütfen Şifreleme Metnini Girin: ").upper())
        print(plaintxt)
        print(TurkChar)
        for i in range(0, len(plaintxt)):
            for j in range(0, len(TurkChar)):
                if plaintxt[i] == TurkChar[j]:
                    x = j + int(key)
                    if x <= 28:
                        result += TurkChar[(j + int(key))]
                    else:
                        result += TurkChar[(x - 29)]
        print("Şifrelenmiş Metniniz:- " + result)
        main()
    else:
        print("Anahtarınız 1-29 Arasında Olmalıdır")
        EncryTurkChar()


# DecryTurkChar function used to decrypt Turkish words
def DecryTurkChar():
    result = ""
    key = input("Lütfen Şifre Çözme Anahtarını Giriniz: ")
    TurkChar = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J',
                'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü',
                'V', 'Y', 'Z']
    while not key.isnumeric():
        print("Lütfen Sadece Numara Giriniz.")
        encryption()
    if 0 < int(key) < 30:
        plaintxt = list(input("Lütfen Şifre Çözme Metnini Giriniz: ").upper())
        print(plaintxt)
        print(TurkChar)
        for i in range(0, len(plaintxt)):
            for j in range(0, len(TurkChar)):
                if plaintxt[i] == TurkChar[j]:
                    x = j + int(key)
                    if x <= 28:
                        result += TurkChar[j - int(key)]
                    else:
                        result += TurkChar[j - int(key)]
        print("Çözülmüş Metniniz:- " + result)
        main()
    else:
        print("Anahtarınız 1-29 Arasında Olmalıdır")
        DecryTurkChar()


# in Encryption function the program will ask user in which language wants to Encrypt(English , Turkish)
def encryption():

    print("you choose Encryption")
    langChose = int(input("Chose a Language Please. English:0 Turkish:1 "))
    if langChose == 0:
        EncryEngChar()
    elif langChose == 1:
        EncryTurkChar()
    else:
        print("You Must Chose Language First?")
        encryption()


# in Decryption function the program will ask user in which language wants to Decrypt(English , Turkish)
def decryption():
    print("you choose Decryption")
    langChose = int(input("Chose a Language Please. 0:English 1:Turkish "))
    if langChose == 0:
        DecryEngChar()
    elif langChose == 1:
        DecryTurkChar()
    else:
        print("You Must Chose Language First?")
        decryption()


# in res function program check the input value must be number
# and must be in range that program asked otherwise the program will be back to main function
# if input is 0 the program will close
# if input is 1 that mean go to Encryption
# if input is 2 that mean go to Decryption
def res(cipherValue):
    while not cipherValue.isnumeric():
        print("Please Enter Numbers Only.")
        main()
    if int(cipherValue) == 0:
        exit()
    elif int(cipherValue) == 1:
        encryption()
    elif int(cipherValue) == 2:
        decryption()
    elif cipherValue != range(0, 2):
        print("you must choose Encryption or Decryption or Exit first")
        main()


# after user decide whats he/she wants program call res function
def main():
    cipherType = input("please choose Exit:0 or Encryption:1 or Decryption:2 ? select : ")
    res(cipherType)


# first program call main function to ask user he/she wants to encrypt or decrypt or Exit
main()