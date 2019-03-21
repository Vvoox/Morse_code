#NOT FINISH YET 1.0

print("Welcome to Morse code app , this app build to encrypt and decrypt any morse code , and facilitate your task . Enjoy")
biblo={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
biblo=['A','.-', 'B','-...',
                    'C','-.-.', 'D','-..', 'E','.',
                    'F','..-.', 'G','--.', 'H','....',
                    'I','..', 'J','.---', 'K','-.-',
                    'L','.-..', 'M','--', 'N','-.',
                    'O','---', 'P','.--.', 'Q','--.-',
                    'R','.-.', 'S','...', 'T','-',
                    'U','..-', 'V','...-', 'W','.--',
                    'X','-..-', 'Y','-.--', 'Z','--..',
                    '1','.----', '2','..---', '3','...--',
                    '4','....-', '5','.....', '6','-....',
                    '7','--...', '8','---..', '9','----.',
                    '0','-----', ', ','--..--', '.','.-.-.-',
                    '?','..--..', '/','-..-.', '-','-....-',
                    '(','-.--.', ')','-.--.-']
A=input('enter 1 for encryption and 2 for decryption : ')
Message=input('Enter your message : ')
print(biblo('A'))
def encryption(message):
    cipher=''
    if A==1 :
        for lettle in message :
            if lettle != '' :
                cipher += biblo[lettle]
            else :
                print("you didn't enter any morse code , exist and retry")
        print(cipher)


def decryption(message):
    decipher=''
    if A==2:
        for lettle in message:
            if lettle != '':
                decipher += biblo[lettle]
            else :
                print("something is wrong")
        return decipher




