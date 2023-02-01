def templatematriks():
    matriks = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'],
    ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b'],
    ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c'],
    ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],
    ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e'],
    ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f'],
    ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g'],
    ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h'],
    ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i'],
    ['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j'],
    ['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k'],
    ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l'],
    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m'],
    ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n'],
    ['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'],
    ['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'],
    ['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'],
    ['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'],
    ['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],
    ['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'],
    ['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],
    ['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'],
    ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'],
    ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'],
    ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']]
    return matriks

def vigenereencrypttanpaspasi(kalimat, key):
    selectkalimat = []
    selectkey = []
    for i in range (len(key)):
        selectkey.append(key[i])

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range (len(kalimat)):
        kalimat = kalimat.lower()
        if (kalimat[i]) in alphabet:
            selectkalimat.append(kalimat[i])
      
    for i in range (len(key)):
        selectkey.append(key[i])
    if (len(selectkey)<len(selectkalimat)):
        for i in range(len(selectkey)+1, len(selectkalimat)+1):
            selectkey.append(selectkey[i-len(key)-1])
    else:
        selectkey = selectkey[:len(selectkalimat)]    

    matriks = templatematriks()
    hasil = []

    for i in range(len(selectkey)):
        selectkey[i] = selectkey[i].lower()

    for i in range (len(selectkalimat)):
        indeks1 = ord(selectkalimat[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        indeks2 = ord(selectkey[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        hasil.append(matriks[indeks1][indeks2])

    strhasil = ''.join(str(x) for x in hasil)

    return strhasil

def vigenereencryptperlima(kalimat, key):
    selectkalimat = []
    selectkey = []
    for i in range (len(key)):
        selectkey.append(key[i])

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range (len(kalimat)):
        kalimat = kalimat.lower()
        if (kalimat[i]) in alphabet:
            selectkalimat.append(kalimat[i])
      
    for i in range (len(key)):
        selectkey.append(key[i])

    if (len(selectkey)<len(selectkalimat)):
        for i in range(len(selectkey)+1, len(selectkalimat)+1):
            selectkey.append(selectkey[i-len(key)-1])
    else:
        selectkey = selectkey[:len(selectkalimat)]        

    matriks = templatematriks()
    hasil = []

    for i in range(len(selectkey)):
        selectkey[i] = selectkey[i].lower()

    for i in range (len(selectkalimat)):
        indeks1 = ord(selectkalimat[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        indeks2 = ord(selectkey[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        hasil.append(matriks[indeks1][indeks2])

    strhasil5 = ''.join(str(x) for x in hasil)
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5

def vigeneredecrypttanpaspasi(kalimat, key):
    selectkalimat = []
    selectkey = []

    for i in range (len(key)):
        selectkey.append(key[i])

    for i in range(len(selectkey)):
        selectkey[i] = selectkey[i].lower()    

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range (len(kalimat)):
        kalimat = kalimat.lower()
        if (kalimat[i]) in alphabet:
            selectkalimat.append(kalimat[i])
      
    if (len(selectkey)<len(selectkalimat)):
        for i in range(len(selectkey)+1, len(selectkalimat)+1):
            selectkey.append(selectkey[i-len(key)-1])
    else:
        selectkey = selectkey[:len(selectkalimat)]    

    matriks = templatematriks()
    hasil = []

    for i in range (len(selectkalimat)):
        indeks2 = ord(selectkey[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        for j in range (26):
            if (selectkalimat[i]==matriks[j][indeks2]):
                indeks1 = j
        hasil.append(matriks[indeks1][0])

    strhasil = ''.join(str(x) for x in hasil)
  
    return strhasil

def vigeneredecryptperlima(kalimat, key):
    selectkalimat = []
    selectkey = []
    
    for i in range (len(key)):
        selectkey.append(key[i])

    for i in range(len(selectkey)):
        selectkey[i] = selectkey[i].lower()    

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range (len(kalimat)):
        kalimat = kalimat.lower()
        if (kalimat[i]) in alphabet:
            selectkalimat.append(kalimat[i])

    if (len(selectkey)<len(selectkalimat)):
        for i in range(len(selectkey)+1, len(selectkalimat)+1):
            selectkey.append(selectkey[i-len(key)-1])
    else:
        selectkey = selectkey[:len(selectkalimat)]    

    matriks = templatematriks()
    hasil = []

    for i in range (len(selectkalimat)):
        indeks2 = ord(selectkey[i]) - 96 - 1 #indeks matriks mulai dari 0 makanya -1
        for j in range (26):
            if (selectkalimat[i]==matriks[j][indeks2]):
                indeks1 = j
        hasil.append(matriks[indeks1][0])

    strhasil5 = ''.join(str(x) for x in hasil)
    # strhasil5 = [strhasil[i:i+5] for i in range(0, len(strhasil), 5)]
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5

# tes1 = vigenereencryptperlima("testkal01imat","abc")
# tes2 = vigeneredecryptperlima(tes1,"abc")

# print(tes1)
# print(tes2)


