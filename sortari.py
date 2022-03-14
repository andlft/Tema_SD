import random
import time
import sys
sys.setrecursionlimit(2000) # modificare facuta pentru quicksort

def quicksort(nr_random, n):
    try:
        def quick(numere, st, dr):
            if dr <= st:
                return
            pivot_index = random.randint(st, dr) #alegem un pivot random
            numere[st], numere[pivot_index] = numere[pivot_index], numere[st] #punem pivotul ca primul element din lista
            i = st  #punem valoarea pointerului din stanga in variabila i
            for j in range(st+1, dr+1):
                if numere[j] < numere[st]: #comparam elementele cu pivotul, care se afla pe prima pozitie
                    i += 1 #marim valoarea pointrului care indica locul in care sunt separate valorile mai mari decat pivotul de cele mai mici
                    numere[i], numere[j] = numere[j], numere[i]

            numere[i], numere[st] = numere[st], numere[i] #mutam pivotul de pe prima pozitie in locul in care indica i

            quick(numere, st, i-1) #se sorteaza ce e in stanga pivotului
            quick(numere, i+1, dr)   #se sorteaza ce e in dreapta pivotului

        if nr_random is None or n < 2:
            return

        quick(nr_random, 0, n - 1)
    except:
        print("Prea multe numere egale pentru quicksort!", end = " - ")

def quicksort2(nr_random, n):
    try:
        def quick(numere, st, dr):
            if dr <= st:
                return
            aux_lis=[(numere[st], st),(numere[(st+dr)//2], (st+dr)//2),(numere[dr],dr)]
            aux_lis.remove(max(aux_lis))
            if aux_lis[0][0]>aux_lis[1][0]:
                pivot_index = aux_lis [0][1]
            else:
                pivot_index = aux_lis [1][1]
            numere[st], numere[pivot_index] = numere[pivot_index], numere[st] #punem pivotul ca primul element din lista
            i = st  #punem valoarea pointerului din stanga in variabila i
            for j in range(st+1, dr+1):
                if numere[j] < numere[st]: #comparam elementele cu pivotul, care se afla pe prima pozitie
                    i += 1 #marim valoarea pointrului care indica locul in care sunt separate valorile mai mari decat pivotul de cele mai mici
                    numere[i], numere[j] = numere[j], numere[i]

            numere[i], numere[st] = numere[st], numere[i] #mutam pivotul de pe prima pozitie in locul in care indica i

            quick(numere, st, i-1) #se sorteaza ce e in stanga pivotului
            quick(numere, i+1, dr)   #se sorteaza ce e in dreapta pivotului

        if nr_random is None or n < 2:
            return

        quick(nr_random, 0, n - 1)
    except:
        print("Prea multe numere egale pentru quicksort!", end = " - ")




def counting_sort_no_dict(nr_random, maxim):
    v_aux = [0] * (maxim + 2)
    for nr in nr_random:
        v_aux[nr] += 1
    rezultat = []
    for i in range(max(nr_random)+1):
        if v_aux[i] != 0:
            for j in range(v_aux[i]):
                rezultat.append(i)
    return rezultat




def shellsort(nr_random, n):

    intervals = [1, 10, 23, 57, 132, 301, 701]
    i = 701
    while i < maxim:
        i = int((i*2.2)//1)
        intervals.append(i)

    for interval in intervals[::-1]:

        for i in range(interval, n):
            aux_1 = nr_random[i]
            aux_2 = i


            while nr_random[aux_2 - interval] > aux_1 and aux_2 >= interval :
                nr_random[aux_2] = nr_random[aux_2 - interval]
                aux_2 -= interval


            nr_random[aux_2] = aux_1

def mergesort(nr_random, n):
    if n > 1:

        # gasim mijlocul vectorului si il impartim in doua
        mid = n // 2
        vector_stanga = nr_random[:mid]
        vector_dreapta = nr_random[mid:]

        mergesort(vector_stanga, len(vector_stanga))  # aplicam recursiv mergesort pentru jumatatea din stanga
        mergesort(vector_dreapta, len(vector_dreapta))  # aplicam recursiv mergesort pentru jumatatea din dreapta

        i = 0
        j = 0
        k = 0

        while i < len(vector_stanga) and j < len(vector_dreapta):
            if vector_stanga[i] < vector_dreapta[j]:
                nr_random[k] = vector_stanga[i]
                i += 1
                k += 1
            if i <len(vector_stanga) and vector_dreapta[j] <= vector_stanga[i]:
                nr_random[k] = vector_dreapta[j]
                j += 1
                k += 1

        # copiem restul elementelor in vector
        while i < len(vector_stanga):
            nr_random[k] = vector_stanga[i]
            i += 1
            k += 1

        while j < len(vector_dreapta):
            nr_random[k] = vector_dreapta[j]
            j += 1
            k += 1

def nr_generate (n, maxim):
    nr_random = []
    for i in range(n):
        aux = random.randint(0, maxim+1)
        nr_random.append(aux)
    return nr_random

def counting_sort_radix (nr_random, exponent, n): #
    rezultat = [0] * n #vector auxiliar in care pastram ce rezulta dupa fiecare etapa
    aux = [0] * 10 # cele 10 "bucketuri"

    for i in range(n):
        cifra = (nr_random[i] // exponent) % 10
        aux[cifra] += 1

    for i in range(1, 10):
        aux[i] += aux[i-1]

    i = n - 1
    while i >= 0:
        cifra = (nr_random[i] // exponent) % 10
        rezultat[aux[cifra]-1] = nr_random[i]
        aux[cifra] -= 1
        i -= 1

    i = 0
    for i in range(0, n):
        nr_random[i] = rezultat[i]



def radix(nr_random, n, maxim):
    max_vector = maxim + 1

    # facem counting sort pentru fiecare cifra de la dreapta la stanga pentru toate numerele
    exponent = 1
    while max_vector // exponent != 0:  # la fiecare etapa inmultim exponentul cu 10 pentru a trece la cifra urmatoare
        counting_sort_radix(nr_random, exponent, n)
        exponent *= 10

def counting_sort_radix_16 (nr_random, exponent, n):

    rezultat = [0] * n #vector auxiliar in care pastram ce rezulta dupa fiecare etapa
    aux = [0] * 16 # cele 16 "bucketuri"

    for i in range(n):
        cifra = (nr_random[i] // exponent) % 16
        aux[cifra] += 1
    for i in range(1, 16):
        aux[i] += aux[i-1]

    i = n - 1
    while i >= 0:
        cifra = (nr_random[i] // exponent) % 16
        rezultat[aux[cifra]-1] = nr_random[i]
        aux[cifra] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        nr_random[i] = rezultat[i]



def radix_16(nr_random, n, maxim):
    max_vector = maxim + 1


    exponent = 1
    while maxim // exponent != 0:
        counting_sort_radix_16(nr_random, exponent, n)
        exponent *= 16

def counting_sort_radix_256 (nr_random, exponent, n):

    rezultat = [0] * n
    aux = [0] * 256

    for i in range(n):
        cifra = (nr_random[i] >> exponent) & 0xff
        aux[cifra] += 1
    for i in range(1, 256):
        aux[i] += aux[i-1]

    i = n - 1
    while i >= 0:
        cifra = (nr_random[i] >> exponent) & 0xff
        rezultat[aux[cifra]-1] = nr_random[i]
        aux[cifra] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        nr_random[i] = rezultat[i]



def radix_256(nr_random, n, maxim):
    max_vector = maxim + 1


    exponent = 0
    while max_vector >> exponent != 0:
        counting_sort_radix_256(nr_random, exponent, n)
        exponent += 8

def counting_sort_radix_1024 (nr_random, exponent, n):

    rezultat = [0] * n
    aux = [0] * 1024

    for i in range(n):
        cifra = (nr_random[i] >> exponent) & 0x3ff
        aux[cifra] += 1
    for i in range(1, 1024):
        aux[i] += aux[i-1]

    i = n - 1
    while i >= 0:
        cifra = (nr_random[i] >> exponent) & 0x3ff
        rezultat[aux[cifra]-1] = nr_random[i]
        aux[cifra] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        nr_random[i] = rezultat[i]



def radix_1024(nr_random, n, maxim):
    max_vector = maxim + 1


    exponent = 0
    while max_vector >> exponent != 0:
        counting_sort_radix_1024(nr_random, exponent, n)
        exponent += 10

def counting_sort_radix_2_16 (nr_random, exponent, n):

    rezultat = [0] * n
    aux = [0] * 65536

    for i in range(n):
        cifra = (nr_random[i] >> exponent) & 0xffff
        aux[cifra] += 1
    for i in range(1, 65536):
        aux[i] += aux[i-1]

    i = n - 1
    while i >= 0:
        cifra = (nr_random[i] >> exponent) & 0xffff
        rezultat[aux[cifra]-1] = nr_random[i]
        aux[cifra] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        nr_random[i] = rezultat[i]



def radix_2_16(nr_random, n, maxim):
    max_vector = maxim + 1


    exponent = 0
    while max_vector >> exponent != 0:
        counting_sort_radix_2_16(nr_random, exponent, n)
        exponent += 16


def verificare_sortare(vector, vector_initial):
    if vector == sorted(vector_initial):
        return True
    else:
        return False



fin = open("teste.txt")
nr_teste = int(fin.readline())
for i in range(nr_teste):
    linie = fin.readline()
    aux = linie.split()
    n = int(aux[0])
    maxim = int(aux[1])
    print(f"N = {n} Max = {maxim}")

    if n>100000001:
        print("Prea multe numere de sortat pentru toti algoritmii!")
        print("-"*100)
        continue

    nr_random = nr_generate(n, maxim)
    nr_random_copie = nr_random.copy()

    start = time.time()
    nr_random_copie.sort()
    stop = time.time()
    if verificare_sortare(nr_random_copie, nr_random) == True:
        print(f"Time executare timsort nativ: {stop-start}")
    else:
        print("Algoritmul nu a sortat corect.")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        radix(nr_random_copie, n, maxim)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare radixsort_baza 10: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Radixsort_baza 10 este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        radix_16(nr_random_copie, n, maxim)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare radixsort_baza 16: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Radixsort_baza 16 este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        radix_256(nr_random_copie, n, maxim)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare radixsort_baza 256: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Radixsort_ baza 256 este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 100000001:
        start = time.time()
        radix_1024(nr_random_copie, n, maxim)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare radixsort_baza 1024: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Radixsort_baza 1024 este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        radix_2_16(nr_random_copie, n, maxim)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare radixsort_baza 2^16: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Radixsort_baza 2^16 este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        mergesort(nr_random_copie, n)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare mergesort: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Mergesort este prea incet!")

    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        quicksort(nr_random_copie, n)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare quicksort (pivot random): {stop-start}")
        else:
            print("Algoritmul nu a putut sorta (trece peste limita de recursie).")
    else:
        print("Quicksort este prea incet!")
    nr_random_copie = nr_random.copy()

    if n < 10000001:
        start = time.time()
        quicksort2(nr_random_copie, n)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare quicksort cu (pivot din 3): {stop-start}")
        else:
            print("Algoritmul nu a putut sorta (trece peste limita de recursie).")
    else:
        print("Quicksort este prea incet!")
    nr_random_copie = nr_random.copy()

    if n < 10000001 and ((n > 99999 and n<=500000 and maxim > 999) or (n > 500000 and maxim > 99999) or n <= 99999):
        start = time.time()
        shellsort(nr_random_copie, n)
        stop = time.time()
        if verificare_sortare(nr_random_copie, nr_random) == True:
            print(f"Timp executare shellsort: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Shellsort este prea incet!")
    nr_random_copie = nr_random.copy()


    if maxim < 100000001:
        start = time.time()
        nr_sortate = counting_sort_no_dict(nr_random_copie, maxim)
        stop = time.time()
        if verificare_sortare(nr_sortate, nr_random) == True:
            print(f"Timp executare counting sort: {stop-start}")
        else:
            print("Algoritmul nu a sortat corect.")
    else:
        print("Nu exista suficienta memorie pentru counting sort")
    print("-"*100)

