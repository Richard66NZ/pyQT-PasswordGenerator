# -*- coding: utf-8 -*-
"""
Python code to generate pseudorandom passwords, display in pyQT window and allow copying to clipboard.
This is a python conversion of code originally written in XOJO.

@author: Richard John Smith

@date: 13 January 2021

This source code is provided by Richard J Smith 'as is' and 'with all faults'. The provider makes no 
representations or warranties of any kind concerning the safety, suitability, inaccuracies, 
typographical errors, or other harmful components of this software.
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import random
import pyperclip

#load Designer window definition file
qtcreator_file = "passwordGen.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

#setup global variable
ButtonSelected = 3

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #connect buuttons to code
        self.quit_button.clicked.connect(self.on_Quitclick)
        self.gen_button.clicked.connect(self.on_click_genb)
        self.copy_button.clicked.connect(self.on_click_copg)  
        self.radioButton1.toggled.connect(self.radioclicked1)
        self.radioButton2.toggled.connect(self.radioclicked2)
        self.radioButton3.toggled.connect(self.radioclicked3)        
        self.radioButton4.toggled.connect(self.radioclicked4)
        self.radioButton5.toggled.connect(self.radioclicked5)
        self.radioButton6.toggled.connect(self.radioclicked6)
        
        #setup controls
        self.password_text.setAlignment(Qt.AlignCenter)
        self.length_slider.setRange(4, 20)
        self.length_slider.setSingleStep(1)
        self.length_slider.setPageStep(4)
        self.length_slider.setSliderPosition(10)
        self.slider_display.setText(str(10))   
        self.length_slider.valueChanged.connect(self.value_changed)
        self.radioButton3.setChecked(True) 
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.setFocus()
        self.password_text.repaint()  
        
    def radioclicked1(self):
        global ButtonSelected
        ButtonSelected = 1
        print("Selection is %s" % (ButtonSelected))
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
    def radioclicked2(self):
        global ButtonSelected
        ButtonSelected = 2
        print("Selection is %s" % (ButtonSelected))
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
    def radioclicked3(self):
        global ButtonSelected
        ButtonSelected = 3
        print("Selection is %s" % (ButtonSelected))
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
    def radioclicked4(self):
        global ButtonSelected
        ButtonSelected = 4
        print("Selection is %s" % (ButtonSelected))
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
    def radioclicked5(self):
        global ButtonSelected
        ButtonSelected = 5
        print("Selection is %s" % (ButtonSelected))
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
    def radioclicked6(self):
        global ButtonSelected
        ButtonSelected = 6
        print("Selection is %s" % (ButtonSelected))        
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
            
    def on_Quitclick(self): #Quit button has been pressed         
        self.close()

    def on_click_genb(self): #Generate new password button has been pressed        
        print('Generate new password')
        print(ButtonSelected)
        print(self.password_text.text())
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
         
    def on_click_copg(self): #Copy to clipboard button has been pressed
        print('Copy password to clipboard')       
        textboxValue = self.password_text.text()
        pyperclip.copy(textboxValue)   
        
    def value_changed(self, i): #Slider position has changed
        print("Password length is %s" % (i))  
        self.slider_display.setText(str(i))        
        self.password_text.setText(get_random_string(int(self.slider_display.text()), ButtonSelected))
        self.password_text.repaint()  
        
def get_random_string(length, type): #function to construct password
    if type == 1:
        sample_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'        
    elif type == 3:
        sample_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
    elif type == 5:
        sample_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'         
    elif type == 6:
        sample_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'         
    elif type == 2:
        sample_letters = 'abcdefghijklmnopqrstuvwxyz'  
    elif type == 4:
        sample_letters = '1234567890'  
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    print("Random string is:", result_str)
    return result_str            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())