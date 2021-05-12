import random

lista=["lisica","auto","avion","brod","ruža","drvo","medved","autobus","fakultet","škola"]

def hangman():
    print("Dobrodošli u igru vešala! Imate 10 pokušaja da pogodite rec")
    rec=random.choice(lista)
    x=10
    #lista sa slovima reci koja se pogadja
    word_list=list(rec)
    #lista za pracenje pogodaka
    tajna_rec= list(len(rec[:])*"*")
    print("Moja rec ima", len(rec[:]), " slova")
    print(tajna_rec)

    while x!=0:
        if word_list==tajna_rec:
            print("Pogodili ste moju rec!")
            start()
        print("Imate", x, "pokušaja")
        #upis slova ili reci
        slovo=input("Upisite slovo ili celu rec: ")

        #ukoliko slovo
        if len(slovo)==1 and slovo in word_list:
            for i in range(len(word_list)):
                if slovo == word_list[i]:
                    index=i
                    tajna_rec[index]=slovo
            print(tajna_rec)
        
        elif len(slovo)==1 and slovo not in word_list:
            print("Tog slova nema. Probajte ponovo")
        x-=1
        
        #za celu rec
        if len(slovo)>1:
            if slovo==rec:
                print("Pogodili ste moju rec!")
                start()
                

        #nedostatak šansi
        if x==0:
            print("Nemate više pogodaka.")
            break
    
def start():
    odgovor=(input("Za start kliknite 1, za izlaz bilo šta: "))
    print(odgovor)
    if odgovor=="1":
        hangman()
    else:
        print("Hvala što ste igrali")
start()

