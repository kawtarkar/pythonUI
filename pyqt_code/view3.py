
from PyQt5 import QtCore, QtGui, QtWidgets

import db

class Ui_MainWindow2(object):
    def setupUi2(self, MainWindow, medicament_data=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 253)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 40, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 70, 191, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 100, 191, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 130, 191, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 160, 191, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.db = db.DatabaseHandler()
        
        
        self.medicament_data = medicament_data  # Store the medicament data for later use
        self.pushButton.clicked.connect(self.update_medicament)
        
        if medicament_data is not None:
            self.lineEdit.setText(str(medicament_data[1]))  # Access elements by their positions
            self.lineEdit_2.setText(medicament_data[2])
            self.lineEdit_3.setText(medicament_data[3])
            self.lineEdit_4.setText(str(medicament_data[4]))
            self.lineEdit_5.setText(str(medicament_data[5]))
            self.lineEdit_6.setText(medicament_data[6])

    def update_medicament(self):
    # Get data from the input fields
        nom_m = self.lineEdit.text()
        description = self.lineEdit_2.text()
        fournisseur = self.lineEdit_3.text()
        prix = float(self.lineEdit_4.text())
        quantite = int(self.lineEdit_5.text())
        date_peremption = self.lineEdit_6.text()
        
        if self.medicament_data is not None:
            id_m = self.medicament_data[0]  # Access the first element for id_m
            # Call the update_medicament method from DatabaseHandler
            self.db.update_record(id_m, nom_m, description, fournisseur, prix, quantite, date_peremption, self)
        
            # Optionally, display a message to confirm that the medicament was updated
            QtWidgets.QMessageBox.information(self.centralwidget, "Medicament Updated", "Medicament has been updated successfully.")
        active_window = QtWidgets.QApplication.instance().activeWindow()
        if active_window:
            active_window.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "nom"))
        self.label_2.setText(_translate("MainWindow", "description"))
        self.label_3.setText(_translate("MainWindow", "fournisseur"))
        self.label_4.setText(_translate("MainWindow", "prix"))
        self.label_5.setText(_translate("MainWindow", "quantite"))
        self.label_6.setText(_translate("MainWindow", "date de peremption"))
        self.pushButton.setText(_translate("MainWindow", "envoyer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

