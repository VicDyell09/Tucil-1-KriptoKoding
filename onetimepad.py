import random

# fungsi filter alfabet + lowercase
def filter(text):
    text = "".join(char for char in text if char.isalpha())
    text = text.lower()
    return text

#fungsi generate key dalam bentuk list angka 0-25
def generatekey(text):
    key = []
    for char in text:
        n = random.randint(0,25)
        key.append(n)
    return key

#fungsi mengubah list angka menjadi string alfabet
def toalfa(text):
    textstr = ""
    for i in range (len(text)):
        textstr+=(chr(text[i]+97))
    return textstr

#fungsi mengubah string alfabet menjadi list angka 0-25
def tonumb(text):
    num = []
    for char in text:
        n = (ord(char)-97)
        num.append(n)
    return num

#fungsi enkripsi otp
def enkripotp(text):
    text = filter(text)
    textnum = tonumb(text)
    keynum = tonumb(key)
    enkripsinum = []
    for i in range (len(textnum)):
        enkripsinum.append((textnum[i]+keynum[i])%26)
    enkripsi = toalfa(enkripsinum)
    return enkripsi

#fungsi enkripsi otp perlima
def enkripotpperlima(text):
    text = filter(text)
    textnum = tonumb(text)
    keynum = tonumb(key)
    enkripsinum = []
    for i in range (len(textnum)):
        enkripsinum.append((textnum[i]+keynum[i])%26)
    enkripsi = toalfa(enkripsinum)
    strhasil5 = ''.join(str(x) for x in enkripsi)
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5

#fungsi dekripsi otp
def dekripsiotp(text):
    text = filter(text)
    keynum = tonumb(key)
    textnum = tonumb(text)
    dekripsinum = []
    for i in range (len(textnum)):
        dekripsinum.append((26+textnum[i]-keynum[i])%26)
    dekripsi = toalfa(dekripsinum)
    return dekripsi

#fungsi dekripsi otp perlima
def dekripsiotpperlima(text):
    text = filter(text)
    keynum = tonumb(key)
    textnum = tonumb(text)
    dekripsinum = []
    for i in range (len(textnum)):
        dekripsinum.append((26+textnum[i]-keynum[i])%26)
    dekripsi = toalfa(dekripsinum)
    strhasil5 = ''.join(str(x) for x in dekripsi)
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5

# #-----main------ enkripsi dekripsi
# text = input("Masukkan Plain Text : ")
# keynum = generatekey(text)
# key = toalfa(keynum)
# print("KeyOTP : "+key)
# enkripsi = enkripotp(text,key)
# print("Hasil Enkripsi : "+enkripsi)
# dekripsi = dekripsiotp(enkripsi,key)
# print("Hasil Dekripsi : "+dekripsi)