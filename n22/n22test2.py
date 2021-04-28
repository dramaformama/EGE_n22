import sys
# Импортируем наш интерфейс из файла
from n22ui2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.buttonotvet.clicked.connect(self.MyFunction)

    def MyFunction(self):

        def nuli(chislo, k=1):
            if len(str(chislo)) != 1:
                for i in range(1, len(str(chislo))):
                    k *= 10
            return k

        def deystvie(chislo, spinchislo, i, j, findex):
            if chislo !=0:
                if (spinchislo == 0) or (spinchislo == 1):
                    if vse[findex+j]+chislo == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 2:
                    if vse[findex+j]*chislo == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 3:
                    if vse[findex+j]**2 == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 4:
                    if nuli(vse[findex+j]) != 1:
                        if vse[findex+j] + nuli(vse[findex+j]) == vse[findex+i]:
                            puti[i] += puti[j]
                elif spinchislo == 5:
                    if vse[findex+j]*2 == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 6:
                    if vse[findex+j]*2+1 == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 7:
                    if vse[findex+j]+vse[findex+j]-1 == vse[findex+i]:
                        puti[i] += puti[j]
                elif spinchislo == 8:
                    if vse[findex+j]+vse[findex+j]+1 == vse[findex+i]:
                        puti[i] += puti[j]

        def obichnoe(first, last):
            puti.append(1)
            findex = vse.index(first)
            for i in range(1,last-first+1):
                puti.append(0)
                for j in range(i):
                    deystvie(chislo1, spinchislo1, i, j, findex)
                    deystvie(chislo2, spinchislo2, i, j, findex)
                    deystvie(chislo3, spinchislo3, i, j, findex)
                    deystvie(chislo4, spinchislo4, i, j, findex)
            x = puti[len(puti)-1]
            puti.clear()
            return x
        
        a = int(self.ui.a.text())
        b = int(self.ui.b.text())
        chislo1 = int(self.ui.chislo1.text())
        chislo2 = int(self.ui.chislo2.text())
        chislo3 = int(self.ui.chislo3.text())
        chislo4 = int(self.ui.chislo4.text())
        sod = self.ui.sod.text()
        nesod = self.ui.nesod.text()
        spinchislo1 = self.ui.spinchislo1.currentIndex()
        spinchislo2 = self.ui.spinchislo2.currentIndex()
        spinchislo3 = self.ui.spinchislo3.currentIndex()
        spinchislo4 = self.ui.spinchislo4.currentIndex()
        vse = []
        puti = []
        x = 0
        otvet = 0

        if a > b:
            a, b = b, a
        for i in range(b-a+1):
            vse.append(a+i)

        if not ' ' in list(sod):
            if not ' ' in list(nesod):
                sod = int(self.ui.sod.text())
                nesod = int(self.ui.nesod.text())
                if (sod != 0) and (nesod != 0):
                    if sod <= nesod:
                        otvet = obichnoe(a, sod)*(obichnoe(sod, b) - obichnoe(sod, nesod)*obichnoe(nesod, b))
                    else:
                        otvet = obichnoe(sod, b)*(obichnoe(a, sod) - obichnoe(a, nesod)*obichnoe(nesod, sod))
                elif nesod != 0:
                    otvet = obichnoe(a, b) - obichnoe(a, nesod)*obichnoe(nesod, b)
                elif sod != 0:
                    otvet = obichnoe(a, sod) * obichnoe(sod, b)
                elif (sod == 0) and (nesod == 0):
                    otvet = obichnoe(a, b)
        elif ' ' in list(sod):
            sodindex = list(sod).index(' ')
            sod1 = int(sod[:sodindex])
            sod2 = int(sod[sodindex+1:])
            if sod1 < sod2:
                otvet = obichnoe(a, sod1)*obichnoe(sod1, sod2)*obichnoe(sod2, b)
            else:
                otvet = obichnoe(a, sod2)*obichnoe(sod2, sod1)*obichnoe(sod1, b)
        elif ' ' in list(nesod):
            nesodindex = list(nesod).index(' ')
            nesod1 = int(nesod[:nesodindex])
            nesod2 = int(nesod[nesodindex+1:])
            if nesod1 < nesod2:
                otvet = obichnoe(a, b) - obichnoe(a, nesod1)*obichnoe(nesod1, nesod2)*obichnoe(nesod2, b)
            else:
                otvet = obichnoe(a, b) - obichnoe(a, nesod2)*obichnoe(nesod2, nesod1)*obichnoe(nesod1, b)

        self.ui.otvet.setText('Ответ: '+str(otvet))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

