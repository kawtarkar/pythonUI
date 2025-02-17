
from PyQt5 import QtCore, QtGui, QtWidgets

from view2 import Ui_MainWindow
from view3 import Ui_MainWindow2
import db




class Ui_afficher(object):
    def open_window(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def open_window2(self):
        selected_item = self.listWidget.currentItem()
        if selected_item is not None:
            selected_text = selected_item.text()
            medicament_id = int(selected_text.split(" - ")[0])
            medicament_data = self.db.get_medicament_data(medicament_id)
            
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi2(self.window, medicament_data)  # Pass medicament_data to view2
           
            self.window.show()
            
        
    def __init__(self):
        self.db = db.DatabaseHandler()  
        
        
        
        
    def setupUi(self, afficher):
        afficher.setObjectName("afficher")
        afficher.resize(618, 368)
        self.centralwidget = QtWidgets.QWidget(afficher)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(180, 30, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ajouter = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.open_window())
        self.ajouter.setGeometry(QtCore.QRect(80, 100, 101, 31))
        self.ajouter.setObjectName("ajouter")
        self.modifier = QtWidgets.QPushButton(self.centralwidget ,clicked=lambda:self.open_window2())
        self.modifier.setGeometry(QtCore.QRect(340, 100, 101, 31))
        self.modifier.setObjectName("modifier")
        self.supprimer = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_medicament())
        self.supprimer.setGeometry(QtCore.QRect(470, 100, 101, 31))
        self.supprimer.setObjectName("supprimer")
        self.afficher_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.show_medicaments())
        self.afficher_2.setGeometry(QtCore.QRect(210, 100, 101, 31))
        self.afficher_2.setObjectName("afficher_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(180, 160, 256, 121))
        self.listWidget.setObjectName("listWidget")
        afficher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(afficher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        afficher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(afficher)
        self.statusbar.setObjectName("statusbar")
        afficher.setStatusBar(self.statusbar)

        self.retranslateUi(afficher)
        QtCore.QMetaObject.connectSlotsByName(afficher)

    def retranslateUi(self, afficher):
        _translate = QtCore.QCoreApplication.translate
        afficher.setWindowTitle(_translate("afficher", "MainWindow"))
        self.label.setText(_translate("afficher", "gestion des medicaments"))
        self.ajouter.setText(_translate("afficher", "ajouter"))
        self.modifier.setText(_translate("afficher", "modifier "))
        self.supprimer.setText(_translate("afficher", "supprimer"))
        self.afficher_2.setText(_translate("afficher", "afficher"))
    def delete_medicament(self):
        selected_item = self.listWidget.currentItem()
    
        if selected_item is not None:
            selected_text = selected_item.text()
            medicament_id = int(selected_text.split(" - ")[0])
    
            confirm = QtWidgets.QMessageBox.question(
                self.centralwidget, "Confirm Deletion",
                f"Are you sure you want to delete Medicament?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
    
            if confirm == QtWidgets.QMessageBox.Yes:
                self.db.delete_medicament(medicament_id)  # Call the new delete_medicament method
                self.show_medicaments()
        else:
            QtWidgets.QMessageBox.warning(
                self.centralwidget, "No Selection",
                "Please select a medicament to delete.",
                QtWidgets.QMessageBox.Ok
            )

    def show_medicaments(self):
        # Implement code to retrieve and display medicaments in the listWidget
        medicaments = self.db.get_medicaments()
        self.listWidget.clear()
        for medicament in medicaments:
            self.listWidget.addItem(f"{medicament[0]} - {medicament[1]}")
    def update_medicament_list(self):
    # Update the list of medicaments in the second view (Ui_afficher)
        self.ui.show_medicaments()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    afficher = QtWidgets.QMainWindow()
    ui = Ui_afficher()
    ui.setupUi(afficher)
    afficher.show()
    sys.exit(app.exec_())
