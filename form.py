#Основная форма
#Методы формы:
#--------------------
#-Прозрачность[готово]
#--Закрепление[готово]
#---
#Изменить Иконки при старте - ПУТИ (C:/)
#Создать установку с иконками
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import formAlt
import os.path
import array
import pyperclip
import time

lst_bufer = list()
temp = list()
filesname = []
ico_style = ''
opacity_val = float(1)
WindowsStyle = 'standart_style'
#Цвета
ColorStyleForm = []
#----------------

class Ui_MainWindow(object):
    #Переменные
    
    
    #Паблики
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(MainWindow.width(), MainWindow.height())
        print(MainWindow.width(), MainWindow.height())#Проверка экрана
        self.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/favicon.ico'))
        MainWindow.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/favicon.ico'))
        #----------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.plainTextEdit.setObjectName("plainTextEdit")#self.plainTextEdit.font()).horizontalAdvance(' ') * 8
        self.plainTextEdit.setTabStopDistance(QtGui.QFontMetricsF(self.plainTextEdit.font()).horizontalAdvance(' ') * 8)
        #Буфер обмена
        QApplication.clipboard().dataChanged.connect(self.clipboards)
        #-----------------------------------------------
        self.setWindowTitle('WorkBook')
        #--------------------------------ListView
        self.listView = QtWidgets.QListView()
        self.listView.setGeometry(QtCore.QRect(55, 30, 501, 151))
        self.listView.setObjectName("listView")
        self.listView.setWindowTitle('Буфер обмена')
        self.listView.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Delete.png'))
        self.listView.setVisible(False)
        
        #lock
        self.grid = QGridLayout(self.centralwidget)
        self.grid.addWidget(self.plainTextEdit)
        self.centralwidget.setStyleSheet("border-radius: 0px;" "background: white")
        #
        self.listView.clicked.connect(self.on_cliceds)
        #------------
        
    
        
        #-----------------------------------------Vertica
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setEnabled(True)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 10, 20, 10))
        self.verticalSlider.setTabletTracking(False)
        self.verticalSlider.setAcceptDrops(False)
        self.verticalSlider.setVisible(0)
        self.verticalSlider.setToolTipDuration(0)
        self.verticalSlider.setMinimum(10)
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setProperty("value", 99)
        self.verticalSlider.setSliderPosition(99)
        self.verticalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.valueChanged.connect(self.changeValue)
        #-------------------------ToolBar
        self.TextsEdit = QSpinBox(value=100)
        self.TextsEdit.valueChanged.connect(self.changeValue)
        self.fileToolBar = self.addToolBar('')
       # self.fileToolBar.addAction('Прозрачность:')
        #self.fileToolBar.setVisible(0)
       # self.fileToolBar.addWidget(self.TextsEdit)
        self.fileToolBar.setMovable(True)#Изменить  перемещается или нет
        self.fileToolBar.setFloatable(False)
        #Значки ToolBar-------------------------------------------------
        self.exitAction = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Add.png'),'Создать', self)#Новый документ
        self.fileToolBar.addAction(self.exitAction)
        
        self.exitAction = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Open.png'),'Открыть', self)#Открыть
        self.fileToolBar.addAction(self.exitAction)
        self.exitAction.triggered.connect(self.OpenMyFile)#Открытие файла Комманда
        
        self.exitAction_1 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Save.png'),'Сохранить', self)#Сохранить
        self.fileToolBar.addAction(self.exitAction_1)
        self.exitAction_1.triggered.connect(self.SaveMyFiled)
        
        
        self.exitAction_2 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Saves.png'),'Сохранить как', self)#Сохранить как
        self.fileToolBar.addAction(self.exitAction_2)
        self.exitAction_2.triggered.connect(self.SaveMyFile)
        
        
        self.exitAction_3 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Delete.png'),'Очистить', self)#Очистить
        self.fileToolBar.addAction(self.exitAction_3)
        self.exitAction_3.triggered.connect(self.ListViewVisible)
        
        self.exitAction_4 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/open_delete.png'),'Открыть корзину', self)#Открыть корзину
        self.fileToolBar.addAction(self.exitAction_4)
        self.exitAction_4.triggered.connect(self.ClearListView)

        self.exitAction_5 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Zakrep.png'),'Открыть корзину', self)#Закреп
        self.fileToolBar.addAction(self.exitAction_5)
        self.exitAction_5.triggered.connect(self.on_zk_o)

        self.exitAction_6 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/w_str.png'),'+ Прозрачность', self)#Вверх
        self.fileToolBar.addAction(self.exitAction_6)
        self.exitAction_6.triggered.connect(self.changeValue)

        self.exitAction_7 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/s_str.png'),'- Прозрачность', self)#Вниз
        self.fileToolBar.addAction(self.exitAction_7)
        self.exitAction_7.triggered.connect(self.MinValue)

        self.exitAction_8 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/standart_style.png'),'Стандартный стиль', self)#Style
        self.fileToolBar.addAction(self.exitAction_8)
        self.exitAction_8.triggered.connect(self.SetStandartStyle)

        self.exitAction_9 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/dark_style.png'),'Темный стиль', self)#DarkStyle
        self.fileToolBar.addAction(self.exitAction_9)
        self.exitAction_9.triggered.connect(self.SetBlackStyle)

        self.exitAction_10 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/light_style.png'),'Светлый стиль',self)#LightStyle
        self.fileToolBar.addAction(self.exitAction_10)
        self.exitAction_10.triggered.connect(self.SetWhiteStyle)

        self.exitAction_11 = QAction(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/settings_ico.png'),'Настройки', self)#Настройки
        self.fileToolBar.addAction(self.exitAction_11)
        self.exitAction_11.triggered.connect(self.SettingsWorkBook)
        
        #----------------------------------------------------------------
        #QtCore.Qt.LeftToolBarArea Style
        self.fileToolBar.setStyleSheet('background-color: white; border-bottom:0px; right:0px; top:0; z-index:99; font-family:sans-serif; box-shadow:0 0 0px #000, 0 0 0px black;')
        #--------------------Открытие файла если он существует-------------------------
        if not sys.argv:
            return
        try:
            global filesname
            file = open(sys.argv[1])
            file_read = file.read()
            filesname = sys.argv
            filesname[0] = sys.argv[1]
            print(file_read)
            self.plainTextEdit.setPlainText(file_read)
            file.close()
        except:
            print("Открывается новая форма")
        #---------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #SettingsWorkBook------------------------------------------------------------------------------------------------
    def SettingsWorkBook(self):
        #----------------------------Box----------------------------------------------------------
        self.SettingBox = QtWidgets.QWidget()
        self.SettingBox.setGeometry(QtCore.QRect(55, 30, 400, 400))
        self.SettingBox.setObjectName("SettingBox")
        self.SettingBox.setWindowTitle('Настройки')
        self.SettingBox.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/settings_ico.png'))
        self.SettingBox.setVisible(True)
        self.SettingBox.setFixedSize(400, 400)
        #-----------------------------------------------------------------------------------------
        #-------------------------List--------------------------------------------------------
        name_setting = ['Стиль', 'Значки панели','Сохранение','Доп.функции', 'Справка']
        self.listSetting = QtWidgets.QListView(self.SettingBox)
        self.listSetting.setGeometry(QtCore.QRect(0, 0, 120, 399))
        self.listSetting.setObjectName("listView")
        self.listSetting.setVisible(True)
        self.listSetting.setStyleSheet('border: 1px solid black; background-color: #fff0f5; color: #a2a2d0; font-weight:BOLD')
        self.listSetting_add = QtGui.QStandardItemModel(parent=self.centralwidget)
        elements = len(name_setting)
        for row in range(0, elements):
            if row == 2:
                print('1')
            else:
                print('2')
            item = QtGui.QStandardItem(QtGui.QIcon(), name_setting[row])
            self.listSetting_add.appendRow(item)
        self.listSetting.setModel(self.listSetting_add)

        self.listSetting.clicked.connect(self.SettingClicked)
        
        #---------------------------------------------------------------------------------------
        #-----------------------------Box_2--------------------------------------------------
        self.PanelBox = QtWidgets.QWidget(self.SettingBox)
        self.PanelBox.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBox.setObjectName("PanelBox")
        self.PanelBox.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBox.setVisible(True)
        #StyleBoxPanel------------------------------------------------------------------------------------------
        self.PanelBoxAlt = QtWidgets.QWidget(self.SettingBox)
        self.PanelBoxAlt.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBoxAlt.setObjectName("PanelAltBox")
        self.PanelBoxAlt.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBoxAlt.setVisible(False)

        self.Label = QLabel(self.PanelBoxAlt)
        self.Label.setText('Стиль')
        self.Label.adjustSize()
        self.Label.move(0, 0)
        self.Label.setVisible(False)

        #Выбор стиля
        self.Label = QLabel(self.PanelBoxAlt)
        self.Label.setText('Настройка стиля текстового редактора')
        self.Label.adjustSize()
        self.Label.move(10, 10)
        self.Label.setVisible(False)
        self.Label.setStyleSheet('border: 0px')
        
        self.test_Plain = QPlainTextEdit(self.PanelBoxAlt)
        self.test_Plain.setGeometry(QtCore.QRect(30, 50, 200, 200))
        self.test_Plain.setPlainText('Пример использования шрифтов\nHello world')
        self.test_Plain.setVisible(True)
        
        
        self.button_cl = QPushButton('Выбрать цвет',self.PanelBoxAlt)
        self.button_cl.setToolTip('Выбрать цвет')
        self.button_cl.setVisible(True)
        self.button_cl.setGeometry(QtCore.QRect(10, 350, 120, 20))
        self.button_cl.clicked.connect(self.ActionClickMenu)
        self.button_cl.setStyleSheet('border: 1px solid black; background-color: #9c9598; color: white')

        self.button_sh = QPushButton('Выбрать шрифт',self.PanelBoxAlt)#Шрифт
        self.button_sh.setToolTip('Выбрать шрифт')
        self.button_sh.setVisible(True)
        self.button_sh.setGeometry(QtCore.QRect(145, 350, 120, 20))
        #self.button.clicked.connect(self.ActionClickMenu)
        self.button_sh.setStyleSheet('border: 1px solid black; background-color: #9c9598; color: white')

        self.button_save_style = QPushButton('Сохранить',self.PanelBoxAlt)#Шрифт
        self.button_save_style.setToolTip('Сохранить')
        self.button_save_style.setVisible(True)
        self.button_save_style.setGeometry(QtCore.QRect(72, 325, 120, 20))
        self.button_save_style.clicked.connect(self.ActionTrueStyleForm)
        self.button_save_style.setStyleSheet('border: 1px solid black; background-color: #9c9598; color: white')

        

        #self.BlackStyleSheet = QWidget(self.PanelBoxAlt)
        #self.BlackStyleSheet.setGeometry(QtCore.QRect(10, 100, 120, 20))
        #self.BlackStyleSheet.setVisible(True)
        #self.BlackStyleSheet.mouseReleaseEvent=lambda event:self.ActionClickMenu()
        #self.BlackStyleSheet.setStyleSheet('background-color: black')

        
            
        #IcoBoxPanel---------------------------------------------------------------------------------------------
        self.PanelBox3 = QtWidgets.QWidget(self.SettingBox)
        self.PanelBox3.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBox3.setObjectName("PanelAltBox")
        self.PanelBox3.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBox3.setVisible(False)

        self.LabelAlt = QLabel(self.PanelBox3)
        self.LabelAlt.setText('Иконки')
        self.LabelAlt.adjustSize()
        self.LabelAlt.setStyleSheet('border: 0px;')
        self.LabelAlt.move(10, 2)
        self.LabelAlt.setVisible(False)
        #SaveBoxPanel------------------------------------------------------------------------------------------
        self.PanelBox4 = QtWidgets.QWidget(self.SettingBox)
        self.PanelBox4.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBox4.setObjectName("PanelAltBox")
        self.PanelBox4.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBox4.setVisible(False)

        self.Label3 = QLabel(self.PanelBox4)
        self.Label3.setText('Сохранение')
        self.Label3.adjustSize()
        self.Label3.move(0, 0)
        self.Label3.setVisible(False)
        #------------------------------------------------------------------------------------------
        #AddBoxPanel------------------------------------------------------------------------------------
        self.PanelBox5 = QtWidgets.QWidget(self.SettingBox)
        self.PanelBox5.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBox5.setObjectName("PanelAltBox")
        self.PanelBox5.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBox5.setVisible(False)

        self.Label4 = QLabel(self.PanelBox5)
        self.Label4.setText('Дополнительные функции')
        self.Label4.adjustSize()
        self.Label4.move(0, 0)
        self.Label4.setVisible(False)
        #-------------------------------------------------------------------------------------------------------
        #HelpMainForm----------------------------------------------------------------------------------
        self.PanelBox6 = QtWidgets.QWidget(self.SettingBox)
        self.PanelBox6.setGeometry(QtCore.QRect(120, 0, 280, 399))
        self.PanelBox6.setObjectName("PanelAltBox")
        self.PanelBox6.setStyleSheet('background-color:white;border: 1px solid black;')
        self.PanelBox6.setVisible(False)

        self.Label5 = QLabel(self.PanelBox6)
        self.Label5.setText('Справка')
        self.Label5.adjustSize()
        self.Label5.move(0, 0)
        self.Label5.setVisible(False)
        #--------------------------------------------------------------------------------------------------------
        print('Тестовое')
    #------------------------------------------------------------------------------------------------------------------------------
    def ActionTrueStyleForm(self):
        self.plainTextEdit.setStyleSheet('background-color: rgba({},{},{},{});'.format(ColorStyleForm[0], ColorStyleForm[1], ColorStyleForm[2], ColorStyleForm[3]))
        print('Good')
    def ActionClickMenu(self):#Изменение цвета фона QPlainText
        global ColorStyleForm
        ColorDialog = QColorDialog.getColor(initial=QtGui.QColor("#ff0000"), parent=self, title="Заголовок окна", options=QtWidgets.QColorDialog.ShowAlphaChannel)
        if ColorDialog.isValid():
            print(ColorDialog.red(), ColorDialog.green(), ColorDialog.blue(), ColorDialog.alpha())
            ColorStyleForm = [ColorDialog.red(), ColorDialog.green(), ColorDialog.blue(), ColorDialog.alpha()]
            print(ColorStyleForm)
            self.test_Plain.setStyleSheet('background-color: rgba({},{},{},{});'.format(ColorDialog.red(), ColorDialog.green(), ColorDialog.blue(), ColorDialog.alpha()))
            print('Good')
    def StyleMainWidgets(self):
        self.PanelBox.setVisible(False)#Основная панель - Пустая
        self.PanelBox3.setVisible(False)
        self.PanelBox4.setVisible(False)
        self.PanelBox5.setVisible(False)
        self.PanelBox6.setVisible(False)
        
        
        self.LabelAlt.setVisible(False)
        self.Label3.setVisible(False)
        self.Label4.setVisible(False)
        self.Label5.setVisible(False)
        
        self.PanelBoxAlt.setVisible(True)
        self.Label.setVisible(True)
    def IconMainWidgets(self):
        self.PanelBoxAlt.setVisible(False)
        self.PanelBox.setVisible(False)
        self.PanelBox4.setVisible(False)
        self.PanelBox5.setVisible(False)
        self.PanelBox6.setVisible(False)

        self.Label.setVisible(False)
        self.Label3.setVisible(False)
        self.Label4.setVisible(False)
        self.Label5.setVisible(False)
        
        self.PanelBox3.setVisible(True)
        self.LabelAlt.setVisible(True)
    def SaveMainForm(self):
        self.PanelBox.setVisible(False)
        self.PanelBoxAlt.setVisible(False)
        self.PanelBox3.setVisible(False)
        self.PanelBox5.setVisible(False)
        self.PanelBox6.setVisible(False)

        self.Label.setVisible(False)
        self.LabelAlt.setVisible(False)
        self.Label4.setVisible(False)
        self.Label5.setVisible(False)
          
        self.PanelBox4.setVisible(True)
        self.Label3.setVisible(True)
    def AddFunctionForm(self):
        self.PanelBox.setVisible(False)
        self.PanelBoxAlt.setVisible(False)
        self.PanelBox3.setVisible(False)
        self.PanelBox4.setVisible(False)
        self.PanelBox6.setVisible(False)

        self.Label.setVisible(False)
        self.LabelAlt.setVisible(False)
        self.Label3.setVisible(False)
        self.Label5.setVisible(False)
        
        self.PanelBox5.setVisible(True)
        self.Label4.setVisible(True)
    def HelpMainForm(self):
        self.PanelBox.setVisible(False)
        self.PanelBoxAlt.setVisible(False)
        self.PanelBox3.setVisible(False)
        self.PanelBox4.setVisible(False)
        self.PanelBox5.setVisible(False)
        
        self.Label.setVisible(False)
        self.LabelAlt.setVisible(False)
        self.Label3.setVisible(False)
        self.Label4.setVisible(False)
        
        self.PanelBox6.setVisible(True)
        self.Label5.setVisible(True)
    def SettingClicked(self):#Элементы списка Setting
            text = self.listSetting.currentIndex().data()
            if text == 'Стиль':
                self.StyleMainWidgets()
            elif text == 'Значки панели':
                self.IconMainWidgets()
            elif text == 'Сохранение':
                self.SaveMainForm()
            elif text == 'Доп.функции':
                self.AddFunctionForm()
            elif text == 'Справка':
                self.HelpMainForm()
    
    #Закреп
    def on_zk_o(self):
        global ico_style
        if ico_style == '':
            ico_style = 'C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Zakrep Off.png'
            self.exitAction_5.setIcon(QIcon(ico_style))#Закреп
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)#Или "ДА"
            self.show()
        elif ico_style == 'C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Zakrep Off.png':
            ico_style = ''
            self.exitAction_5.setIcon(QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/ico/Style_1/Zakrep.png'))#Закреп
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)#Или "НЕТ"
            self.show()
    #Изменение видимости
    def on_clicked_op(self):
        self.verticalSlider.setVisible(1)
        
    def off_clicked_op(self):
        self.verticalSlider.setVisible(0)
    def changeValue(self):#------------------------------------------------------------Opacity +
        global opacity_val
        opacity_val += 0.1
        if opacity_val > 1:
            opacity_val = 1
            print('Максимальное установлено')
        else:
            self.setWindowOpacity(opacity_val)
        print(opacity_val)
    def MinValue(self):#------------------------------------------------------------Opacity -
        global opacity_val
        opacity_val -= 0.1
        if opacity_val < 0.20:
            opacity_val = 0.20
            print('Минимальное установлено')
        else:
            self.setWindowOpacity(opacity_val)
        print(opacity_val)
    #Стили для блокнота
    def SetStandartStyle(self):#Стандартный
        global WindowsStyle
        WindowsStyle = 'dark_style'
        
        self.plainTextEdit.setStyleSheet('')
        self.setStyleSheet("")
        self.verticalSlider.setStyleSheet("background-color: rgba(255,250,250,0);")
        self.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/favicon.ico'))
        self.centralwidget.setStyleSheet("border-radius: 0px;" "background-color: white;")
        self.fileToolBar.setStyleSheet('background-color: white;' "border-bottom:5px; right:20px; top:0; z-index:99; font-family:sans-serif; box-shadow:0 0 5px #000, 0 0 5px #000;")
    def SetWhiteStyle(self):#Светлый
        global WindowsStyle
        WindowsStyle = 'standart_style'
        
        print('Светлый фон')
        #Style
        #-TextArea
        self.plainTextEdit.setStyleSheet("background-color: rgba(255,250,250,1);"
                                        "color: #a2a2d0;" "resize:none;" "border: 0;"
                                        "font-weight: bold;")
        #--MainForm
        self.setStyleSheet("")
        #---Scroll
        self.verticalSlider.setStyleSheet("background-color: rgba(255,250,250,0);")
        #----ICO
        self.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/favicon_1.ico'))
        #-----CentralWidget
        self.centralwidget.setStyleSheet("border-radius: 0px;" "background: rgba(255,250,250,1);")
        #------ListView
        self.listView.setStyleSheet("background-color: rgba(255,250,250,1);" "color:#828282;" "font-weight:bold;")
        #-------ToolBar
        self.fileToolBar.setStyleSheet('background-color: rgba(255,250,250,1);' "border-bottom:5px; right:20px; top:0; z-index:99; font-family:sans-serif; box-shadow:0 0 5px #000, 0 0 5px #000;")
    def SetBlackStyle(self):#Темный
        print('Темный фон')
        #Style
        #-TextArea
        self.plainTextEdit.setStyleSheet(
                                        "color: #dbd7d2;" "resize:none;" "border: 0;"
                                        "font-weight: bold;"
                                        "background-color: rgba(83,75,79,1);"                            
                                        )
        #--MainForm
        self.setStyleSheet("selection-background-color: #828282;")
        #---Scroll
        self.verticalSlider.setStyleSheet("background-color: rgba(83,75,79,0);")
        #----ICO
        self.setWindowIcon(QtGui.QIcon('C:/Users/grigorev.vladimir/Desktop/PyQt5/favicon_2.ico'))
        #-----ListView
        self.listView.setStyleSheet("background-color: rgba(83,75,79,1);" "color:#828282;" "font-weight:bold;")
        #------CentralWidget
        self.centralwidget.setStyleSheet("border-radius: 0px;" "background: rgba(83,75,79,1);")
        #-------ToolBar
        self.fileToolBar.setStyleSheet('background-color: rgba(83,75,79,1); border-bottom:5px; right:20px; top:0; z-index:99; font-family:sans-serif; box-shadow:0 0 5px #000, 0 0 5px #000;')
    #Открытие файла
    def OpenMyFile(self):
        global filesname
        filesname = QFileDialog.getOpenFileName(self, "Открытие файла", '', '*.txt') 
        if not filesname:
            return
        try:
            file = open(filesname[0])
            file_read = file.read()
            print(file_read)
            self.plainTextEdit.setPlainText(file_read)
            file.close()
        except:
            print("Close File")
        
    #Сохранение файла
    def SaveMyFile(self):
      global filesname
      filesname = QFileDialog.getSaveFileName(self, "Сохранение",'name.txt','*.txt')
      print(filesname[0])
      if not filesname:
          return
      try:
          print(filesname)
          print(filesname[0])
          file = open(filesname[0], 'w')
          text = self.plainTextEdit.toPlainText()
          file.write(text)
          file.close()
          
      except:
          print('Отмена действий')
    def SaveMyFiled(self):
        print(filesname)   
        if not filesname:
          return
        try:
          print(filesname)
          print(filesname[0])
          file = open(filesname[0], 'w')
          text = self.plainTextEdit.toPlainText()
          file.write(text)
          file.close()
        except:
          print('Отмена действий')
#-----------------------------------Буфер обмена---------------------------------
    def clipboards(self):
        text = QApplication.clipboard().text()
        print(text+'\n')
        lst_bufer.append(text)
        print(lst_bufer)
#================================ListView - Буфер обмена-------------------------
    def ListViewOffVisible(self):
        self.listView.setVisible(False)
    def ListViewVisible(self):
        self.listView.setVisible(True)
        self.listView_add = QtGui.QStandardItemModel(parent=self.centralwidget)
        
        #
        lst_bufer1 = list(set(lst_bufer))
        print(lst_bufer1)
        elements = len(lst_bufer1)
        #
        print('Колличество элементов в массиве:',elements)
        for row in range(0, elements):
            if row == 2:
                print('1')
            else:
                print('2')
            item = QtGui.QStandardItem(QtGui.QIcon(), lst_bufer1[row])
            self.listView_add.appendRow(item)
        self.listView.setModel(self.listView_add)
    def ClearListView(self):
        lst_bufer.clear()
    def on_cliceds(self, index):#По нажатию буфер обмена
        print(self.listView.currentIndex().data())
        text = self.listView.currentIndex().data()
        pyperclip.copy(text)
    
        
       
        
    
        

        
        

        

    
        
        
        
