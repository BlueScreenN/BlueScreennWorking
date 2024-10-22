import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem

class StockTrackingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pvc = 0.0
        self.pp = 0.0
        self.pe = 0.0
        self.pvc_label = QLabel('Please enter the amount of PVC:', self)
        self.pp_label = QLabel('Please enter the amount of PP:', self)
        self.pe_label = QLabel('Please enter the amount of PE:', self)
        self.pvc_input = QLineEdit(self)
        self.pp_input = QLineEdit(self)
        self.pe_input = QLineEdit(self)
        self.set_button = QPushButton('Set Stocks', self)
        self.set_button.clicked.connect(self.set_initial_stocks)
        self.update_button = QPushButton('Update Stock', self)
        self.update_button.clicked.connect(self.update_stocks)
        self.table = QTableWidget(self)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['PVC Amount', 'PP Amount', 'PE Amount'])

        vbox = QVBoxLayout()

        vbox.addWidget(self.pvc_label)
        vbox.addWidget(self.pvc_input)
        vbox.addWidget(self.pp_label)
        vbox.addWidget(self.pp_input)
        vbox.addWidget(self.pe_label)
        vbox.addWidget(self.pe_input)
        hbox = QHBoxLayout()
        hbox.addWidget(self.set_button)
        hbox.addWidget(self.update_button)
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)

        self.setLayout(vbox)
        self.setWindowTitle('Stock Tracking Application')

    def set_initial_stocks(self):
        try:
            self.pvc = float(self.pvc_input.text())
            self.pp = float(self.pp_input.text())
            self.pe = float(self.pe_input.text())
            self.update_table()
            QMessageBox.information(self, 'Information', 'Stocks successfully set!')
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid number!')

    def update_stocks(self):
        try:

            pvc_used, ok = QInputDialog.getDouble(self, "PVC Update", "Enter the amount of PVC to be used/added:")
            if ok:
                self.pvc += pvc_used
            pp_used, ok = QInputDialog.getDouble(self, "PP Update", "Enter the amount of PP to be used/added:")
            if ok:
                self.pp += pp_used
            pe_used, ok = QInputDialog.getDouble(self, "PE Update", "Enter the amount of PE to be used/added:")
            if ok:
                self.pe += pe_used
            self.update_table()

        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid number!')

    def update_table(self):

        self.table.setItem(0, 0, QTableWidgetItem(str(self.pvc)))
        self.table.setItem(0, 1, QTableWidgetItem(str(self.pp)))
        self.table.setItem(0, 2, QTableWidgetItem(str(self.pe)))


        self.check_stocks()

    def check_stocks(self):
        message = ""

        if self.pvc <= 200:
            message += "PVC stock is below the safety threshold! Remaining PVC: {}\n".format(self.pvc)
        else:
            message += "Remaining PVC stock: {}\n".format(self.pvc)

        if self.pp <= 250:
            message += "PP stock is below the safety threshold! Remaining PP: {}\n".format(self.pp)
        else:
            message += "Remaining PP stock: {}\n".format(self.pp)

        if self.pe <= 100:
            message += "PE stock is below the safety threshold! Remaining PE: {}\n".format(self.pe)
        else:
            message += "Remaining PE stock: {}\n".format(self.pe)

        QMessageBox.information(self, 'Stock Status', message)

app = QApplication(sys.argv)
window = StockTrackingApp()
window.show()
sys.exit(app.exec_())
