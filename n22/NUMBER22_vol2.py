
# coding: utf-8

# In[3]:


def nuli(chislo, k=1):
    if len(list(chislo)) != 2:
        for i in range(1, len(list(chislo))):
            k *= 10
    return k

def deystvie(chislo, i, j, findex):
    if chislo != '0':
        if list(chislo)[0] == '*':
            if len(chislo) == 2: 
                if vse[findex+j]*int(list(chislo)[1]) == vse[findex+i]:
                    puti[i] += puti[j]
            elif len(chislo) == 3:
                if vse[findex+j]*int(chislo[1]+chislo[2]) == vse[findex+i]:
                    puti[i] += puti[j]
        elif chislo == 'увеличь старшую цифру числа на 1':
            if nuli(chislo) != 1:
                if vse[findex+j] + nuli(chislo) == vse[findex+i]:
                    puti[i] += puti[j]
        elif list(chislo)[0] == '+':
            if vse[findex+j]+int(list(chislo)[1]) == vse[findex+i]:
                puti[i] += puti[j]
        elif chislo == 'сделай четное':
            if vse[findex+j]*2 == vse[findex+i]:
                puti[i] += puti[j]
        elif chislo == 'сделай нечетное':
            if vse[findex+j]*2+1 == vse[findex+i]:
                puti[i] += puti[j]
        elif chislo == 'прибавь предыдущее':
            if vse[findex+j]+vse[findex+j]-1 == vse[findex+i]:
                puti[i] += puti[j]
        elif chislo == 'возведи в квадрат':
            if vse[findex+j]**2 == vse[findex+i]:
                puti[i] += puti[j]
            
def obichnoe(first, last):
    puti.append(1)
    findex = vse.index(first)
    for i in range(1,last-first+1):
        puti.append(0)
        for j in range(i):
            deystvie(chislo1, i, j, findex)
            deystvie(chislo2, i, j, findex)
            deystvie(chislo3, i, j, findex)
            deystvie(chislo4, i, j, findex)   
    x = puti[len(puti)-1]
    puti.clear()
    return x

a, b = map(int, input('Введите два числа ').split())
chislo1 = input('Введите первую операцию ')
chislo2 = input('Введите вторую операцию ')
chislo3 = input('Введите третью операцию (если ее нет, напишите 0) ')
chislo4 = input('Введите четвертую операцию (если ее нет, напишите 0) ')
sod = int(input('Введите число, через которое должна проходить траектория (если его нет, напишите 0) '))
nesod = int(input('Введите число, через которое НЕ должна проходить траектория (если ее нет, напишите 0) '))
vse = []
puti = []
x = 0
otvet = 0

for i in range(b-a+1):
    vse.append(a+i)

if (sod != 0) and (nesod != 0):
    if sod <= nesod:
        otvet = obichnoe(a, sod)*(obichnoe(sod, b) - obichnoe(sod, nesod)*obichnoe(nesod, b))
    else:
        otvet = obichnoe(sod, b)*(obichnoe(a, sod) - obichnoe(a, nesod)*obichnoe(nesod, sod))
elif nesod != 0:
    otvet = obichnoe(a, b) - obichnoe(a, nesod)*obichnoe(nesod, b)
elif sod != 0:
        otvet = obichnoe(a, sod) * obichnoe(sod, b)
elif (sod == 0) and (nesod ==0):
    otvet = obichnoe(a, b)

print ('Ответ: ', otvet)

