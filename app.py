from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import ExtractRARFiles as exZip


#interface

class Ui_Dialog(object):
    
    def __init__(self):
        self.directory = ""
        
    def select_folder(self):
        file = QFileDialog.getExistingDirectory()
        self.showFolderNameTextEdit.setText(file)
        self.directory = self.directory.replace(" ", "\\")

    def extract_files(self):
        directory = self.showFolderNameTextEdit.toPlainText()
        files = exZip.ZIPfilesName(directory)
        directory = directory +"/"
        message = exZip.extractZIPFiles(files, directory)
        #show alert message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec_()
                 
         
    def setupUi(self, Dialog):
        #Choose Folder Button
        self.chooseFolderBtn = QtWidgets.QPushButton(Dialog)
        self.chooseFolderBtn.setGeometry(QtCore.QRect(130, 80, 75, 23))
        self.chooseFolderBtn.setObjectName("chooseFolder")
        self.chooseFolderBtn.clicked.connect(self.select_folder)
        
        #Text Field to show folder name
        self.showFolderNameTextEdit = QtWidgets.QTextEdit(Dialog)
        self.showFolderNameTextEdit.setGeometry(QtCore.QRect(240, 80, 171, 31))
        self.showFolderNameTextEdit.setObjectName("showFolderNameTextEdit")
           
        # extract files button
        self.extractFilesBtn = QtWidgets.QPushButton(Dialog)
        self.extractFilesBtn.setGeometry(QtCore.QRect(335, 170, 75, 23))
        self.extractFilesBtn.setObjectName("chooseFramesFolder")
        self.extractFilesBtn.clicked.connect(self.extract_files)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
      
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.chooseFolderBtn.setText(_translate("Dialog", "Choose"))
        self.extractFilesBtn.setText(_translate("Dialog", "Extract files"))

#Main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

