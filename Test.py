from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtWidgets import QVBoxLayout,QRadioButton

count = 1
true_count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vMainLay = QVBoxLayout()
        self.start()
        self.setWindowTitle('TEST')
    def start(self):

        self.savol1 = QLabel("Manchester City vs Arsenal?\t\t\n\n")
        self.v1 = QRadioButton("2-1")
        self.v2 = QRadioButton('2-2')
        self.v3 = QRadioButton('3-2')
        self.v4 = QRadioButton('3-1') # True answer

        self.vMainLay.addWidget(self.savol1)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)


        self.savol2 = QLabel("Dasturlshni bilasizmi?")
        self.v5 = QRadioButton("Ha") # True answer
        self.v6 = QRadioButton('Yo\'q')
        self.v7 = QRadioButton('Kim u?')
        self.v8 = QRadioButton('Eshitganman ammo ma\'lumotim yo\'q')
        

        self.savol3 = QLabel("Kelajakda nima rejalaringiz bor?")
        self.v9 = QRadioButton("Nima ishing bor!")
        self.v10 = QRadioButton('Senior dasturchi bo\'lish') # True answer
        self.v11 = QRadioButton('Har sohadagi fundamental bilimlarni egallsh')
        self.v12 = QRadioButton('Yaxshi inson bo\'lish')


        self.savol4 = QLabel("1-(8*7)*2 = ?")
        self.v13 = QRadioButton("112")
        self.v14 = QRadioButton('110')
        self.v15 = QRadioButton('111') # True answer
        self.v16 = QRadioButton('113')


        self.savol5 = QLabel("5 * 5 == 24?")
        self.v17 = QRadioButton("True")
        self.v18 = QRadioButton('I don\'t know')
        self.v19 = QRadioButton('Maybe')
        self.v20 = QRadioButton('there is no correct answer') # True answer

        self.setLayout(self.vMainLay)

        self.Next1 = QPushButton("Next")
        self.Next1.clicked.connect(self.dalshe)
        self.vMainLay.addWidget(self.Next1)


    def dalshe(self):
        global true_count
        global count
        if count==1:
            if self.v4.isChecked():
                true_count+=1
                count+=1
                self.savol1.setText(self.savol2.text())

                self.v1.hide()
                self.v2.hide()
                self.v3.hide()
                self.v4.hide()

                self.vMainLay.addWidget(self.v5)
                self.vMainLay.addWidget(self.v6)
                self.vMainLay.addWidget(self.v7)
                self.vMainLay.addWidget(self.v8)
                
                self.vMainLay.addWidget(self.Next1)
            else:
                self.savol1.setText(self.savol2.text())

                self.v1.hide()
                self.v2.hide()
                self.v3.hide()
                self.v4.hide()
                count+=1
                self.vMainLay.addWidget(self.v5)
                self.vMainLay.addWidget(self.v6)
                self.vMainLay.addWidget(self.v7)
                self.vMainLay.addWidget(self.v8)
                
                self.vMainLay.addWidget(self.Next1)

        elif count==2:
            if self.v5.isChecked():
                true_count+=1
                count+=1
                self.savol1.setText(self.savol3.text())

                self.v5.hide()
                self.v6.hide()
                self.v7.hide()
                self.v8.hide()

                self.vMainLay.addWidget(self.v9)
                self.vMainLay.addWidget(self.v10)
                self.vMainLay.addWidget(self.v11)
                self.vMainLay.addWidget(self.v12)
                
                self.vMainLay.addWidget(self.Next1)
            else:
                self.savol1.setText(self.savol3.text())

                self.v5.hide()
                self.v6.hide()
                self.v7.hide()
                self.v8.hide()
                count+=1
                self.vMainLay.addWidget(self.v9)
                self.vMainLay.addWidget(self.v10)
                self.vMainLay.addWidget(self.v11)
                self.vMainLay.addWidget(self.v12)
                
                self.vMainLay.addWidget(self.Next1)

        elif count==3:
            if self.v10.isChecked():
                true_count+=1
                count+=1
                self.savol1.setText(self.savol4.text())

                self.v9.hide()
                self.v10.hide()
                self.v11.hide()
                self.v12.hide()

                self.vMainLay.addWidget(self.v13)
                self.vMainLay.addWidget(self.v14)
                self.vMainLay.addWidget(self.v15)
                self.vMainLay.addWidget(self.v16)
                
                self.vMainLay.addWidget(self.Next1)
            else:
                self.savol1.setText(self.savol4.text())

                self.v9.hide()
                self.v10.hide()
                self.v11.hide()
                self.v12.hide()
                count+=1
                self.vMainLay.addWidget(self.v13)
                self.vMainLay.addWidget(self.v14)
                self.vMainLay.addWidget(self.v15)
                self.vMainLay.addWidget(self.v16)
                
                self.vMainLay.addWidget(self.Next1)

        elif count==4:

            self.finish = QPushButton("Finish")
            if self.v15.isChecked():
                true_count+=1
                count+=1
                self.savol1.setText(self.savol5.text())

                self.v13.hide()
                self.v14.hide()
                self.v15.hide()
                self.v16.hide()

                self.vMainLay.addWidget(self.v17)
                self.vMainLay.addWidget(self.v18)
                self.vMainLay.addWidget(self.v19)
                self.vMainLay.addWidget(self.v20)
                
                self.vMainLay.addWidget(self.Next1)
            else:
                self.v13.hide()
                self.v14.hide()
                self.v15.hide()
                self.v16.hide()

                self.vMainLay.addWidget(self.v17)
                self.vMainLay.addWidget(self.v18)
                self.vMainLay.addWidget(self.v19)
                self.vMainLay.addWidget(self.v20)

                count+=1
                self.vMainLay.addWidget(self.Next1)
        else:
            if self.v20.isChecked():true_count+=1
            
            self.vMainLay.addWidget(self.finish)
            self.finish.clicked.connect(self.info)
            self.Next1.setText(self.finish.text())
            self.Next1.hide()
            self.savol1.hide()
            self.v17.hide()
            self.v18.hide()
            self.v19.hide()
            self.v20.hide()

    def info(self):
        global true_count
        self.finish.hide()
        self.rezult = QLabel(f'Rezult: {true_count} ball')
        self.vMainLay.addWidget(self.rezult)
                
app = QApplication([])
obj = Window()
obj.show()
app.exec_()