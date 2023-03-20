#program izpise skupno stevilo skatel
n = int(input())

#st korakov (max 2020)
korak = 0
#ali smo nasli hrosca
zadetek = False

#poseben primer n = 2 ves cas uzburamo 0
if n == 2:
    while True:
        print(0)
        odgovor = input()
        if odgovor == 'Bingo!':
            break

else:

    #za splosen n
    while korak < 2019:
        #najprej se zapeljemo od leve proti desni
        for i in range(0, n - 1):
            print(i)
            #odgovor racunalnika
            odgovor = input()
            if odgovor == 'Bingo!':
                zadetek = True
                break #ven iz notranje zanke
            korak += 1
    
        #ven iz zunanje zanke
        if zadetek:
            break
    
        for i in range(n - 2, 0, -1):
            print(i)
            odgovor = input()
            if odgovor == 'Bingo!':
                zadetek = True
                break #ven iz notranje zanke
            korak += 1
    
        #ven iz zunanje zanke
        if zadetek:
            break

        
            