import sys
from PyQt5 import QtWidgets
import form


class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    print(sys.argv[0])
    window = ExampleApp()
    window.show()
    
    app.exec_() 

if __name__ == '__main__':  
    main()
#--------------------------------------------------------------------

