import subprocess
import sys
import os


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


def start_vm():
   rt = subprocess.run('/home/tswisse/Documents/UI_Virtualisation/code/Start_VM.sh')
   print(rt.returncode)
   if int(rt.returncode) == 0:
        print("pass")
   else:
        print("fail")



def Ui():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("UI Virtualization")

    label = QLabel(win)
    label.setText("Migration d'une machine virtuelle")
    label.move(75, 50)
    label.resize(200, 20)

    b1 = QPushButton(win)
    b1.setText("Start VM")
    b1.move(40, 120)
    b1.clicked.connect(start_vm)

    b2 = QPushButton(win)
    b2.setText("Select Features")
    b2.move(150, 120)

    b3 = QPushButton(win)
    b3.setText("Deploy App")
    b3.move(40, 180)

    b4 = QPushButton(win)
    b4.setText("Save Features")
    b4.move(150, 180)

    win.show()
    sys.exit(app.exec_())


Ui()
