# fungsi filter alfabet + lowercase + ganti j ke i
def removej(key):
    key = "".join(char for char in key if char.isalpha())
    key = key.lower()
    key = key.replace("j","i")
    return key

#fungsi key jadi matrix 5x5
def matrix(key):
    key = key + "abcdefghiklmnopqrstuvwxyz"
    key = "".join(dict.fromkeys(key).keys())   
    matrix = []
    for i in range (5):
        rowList = []
        for j in range (5):
            if key[j] not in matrix:
                rowList.append(key[i*5+j])
        matrix.append(rowList)
    return matrix 

#fungsi yang mengembalikan text yang telah diformat (ditambahkan x dan di partisi per 2 huruf )
def tobigram(text):
    bigramtext = ""
    i = 1
    while i <= len(text):
        if i < len(text):
            fisrtletter = text[i-1]
            secondletter = text[i]
            if fisrtletter == secondletter:
                bigramtext+=(fisrtletter+"x")
                i+=1
            else:
                bigramtext+=(fisrtletter+secondletter)
                i+=2
        else:
            bigramtext += text[i-1]
            i+=1
        if len(bigramtext) % 2 != 0:
            bigramtext += 'x'
    bigramtext = [bigramtext[i:i+2] for i in range(0, len(bigramtext), 2)]
    return(bigramtext)

#fungsi yang membantu untuk mencari lokasi huruf pada matrix
def search(huruf,matrix):
    for i in range(5):
        for j in range(5):
            if(matrix[i][j] == huruf):
                return i, j

#fungsi enkripsi playfair
def playfairenk(text1,key1):
    key = removej(key1) #formating key
    text = removej(text1) #fromating plain text
    bigram = tobigram(text) #plain text ke bigram
    mat = (matrix(key)) #key jadi marix 5x5
    textenkrip = ""
    for i in range (0,len(bigram)):
        pos1 = search((bigram[i])[0],mat)
        pos2 = search((bigram[i])[1],mat)
        result1 = ""
        result2 = ""
        if pos1[0]==pos2[0]:
            result1 = [pos1[0],(pos1[1]+1)%5] 
            result2 = [pos2[0],(pos2[1]+1)%5] 
        elif pos1[1] == pos2[1]:
            result1 = [(pos1[0]+1)%5,pos1[1]] 
            result2 = [(pos2[0]+1)%5,pos2[1]]
        else:
            result1 = [pos1[0],pos2[1]] 
            result2 = [pos2[0],pos1[1]] 
        textenkrip += mat[result1[0]][result1[1]]
        textenkrip += mat[result2[0]][result2[1]]
    return textenkrip

#fungsi dekripsi playfair per lima
def playfairenkperlima(text1,key1):
    key = removej(key1) #formating key
    text = removej(text1) #fromating plain text
    bigram = tobigram(text) #plain text ke bigram
    mat = (matrix(key)) #key jadi marix 5x5
    textenkrip = ""
    for i in range (0,len(bigram)):
        pos1 = search((bigram[i])[0],mat)
        pos2 = search((bigram[i])[1],mat)
        result1 = ""
        result2 = ""
        if pos1[0]==pos2[0]:
            result1 = [pos1[0],(pos1[1]+1)%5] 
            result2 = [pos2[0],(pos2[1]+1)%5] 
        elif pos1[1] == pos2[1]:
            result1 = [(pos1[0]+1)%5,pos1[1]] 
            result2 = [(pos2[0]+1)%5,pos2[1]]
        else:
            result1 = [pos1[0],pos2[1]] 
            result2 = [pos2[0],pos1[1]] 
        textenkrip += mat[result1[0]][result1[1]]
        textenkrip += mat[result2[0]][result2[1]]

    strhasil5 = ''.join(str(x) for x in textenkrip)
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5        

#fungi dekripsi playfair
def playfairdek(text1,key1):
    key = removej(key1) #formating key
    text = removej(text1) #fromating plain text
    bigram = tobigram(text) #plain text ke bigram
    mat = (matrix(key)) #key jadi marix 5x5
    textdekrip = ""
    for i in range (0,len(bigram)):
        pos1 = search((bigram[i])[0],mat)
        pos2 = search((bigram[i])[1],mat)
        result1 = ""
        result2 = ""
        if pos1[0]==pos2[0]:
            result1 = [pos1[0],(pos1[1]+4)%5] 
            result2 = [pos2[0],(pos2[1]+4)%5] 
        elif pos1[1] == pos2[1]:
            result1 = [(pos1[0]+4)%5,pos1[1]] 
            result2 = [(pos2[0]+4)%5,pos2[1]]
        else:
            result1 = [pos1[0],pos2[1]] 
            result2 = [pos2[0],pos1[1]] 
        textdekrip += mat[result1[0]][result1[1]]
        textdekrip += mat[result2[0]][result2[1]]
    return textdekrip

#fungi dekripsi playfair perlima
def playfairdekperlima(text1,key1):
    key = removej(key1) #formating key
    text = removej(text1) #fromating plain text
    bigram = tobigram(text) #plain text ke bigram
    mat = (matrix(key)) #key jadi marix 5x5
    textdekrip = ""
    for i in range (0,len(bigram)):
        pos1 = search((bigram[i])[0],mat)
        pos2 = search((bigram[i])[1],mat)
        result1 = ""
        result2 = ""
        if pos1[0]==pos2[0]:
            result1 = [pos1[0],(pos1[1]+4)%5] 
            result2 = [pos2[0],(pos2[1]+4)%5] 
        elif pos1[1] == pos2[1]:
            result1 = [(pos1[0]+4)%5,pos1[1]] 
            result2 = [(pos2[0]+4)%5,pos2[1]]
        else:
            result1 = [pos1[0],pos2[1]] 
            result2 = [pos2[0],pos1[1]] 
        textdekrip += mat[result1[0]][result1[1]]
        textdekrip += mat[result2[0]][result2[1]]

    strhasil5 = ''.join(str(x) for x in textdekrip)
    for i in range (len(strhasil5)//5+1):
        strhasil5 = strhasil5[:i*6] + " " + strhasil5[i*6:]
    strhasil5 = strhasil5[1:]    
    return strhasil5     

# #----main------- enkripsi
# key = input("Enter Your Key : ") # input key
# text = input("Enter Your Text : ")
# textenkrip = playfairenk(text,key) #enkripsi
# textenkripf5 = playfairenkperlima(text,key)
# # print()
# # print("------ Playfair Square -------")
# # for i in range(5):
# #     print(mat[i]) # print matrix
# # print("------------------------------")
# # print()
# # print("Hasil pemisahan per 2 huruf : ",bigram) # print text per 2 huruf
# print("Hasil enkripsi : ",textenkrip) #print hasil enkripsi
# print("Hasil enkripsi per 5 huruf : ",textenkripf5) #print hasil enkripsi

# # #----main------- dekripsi
# key = input("Enter Your Key : ") # input key
# text = input("Enter Your Text : ")
# textdekrip = playfairdek(text,key) #enkripsi
# textdekripf5 = playfairdekperlima(text,key)
# # print()
# # print("------ Playfair Square -------")
# # for i in range(5):
# #     print(mat[i]) # print matrix
# # print("------------------------------")
# # print()
# # print("Hasil pemisahan per 2 huruf : ",bigram) # print text per 2 huruf
# print("Hasil dekripsi : ",textdekrip) #print hasil enkripsi
# print("Hasil dekripsi per 5 huruf : ",textdekripf5) #print hasil enkripsi
