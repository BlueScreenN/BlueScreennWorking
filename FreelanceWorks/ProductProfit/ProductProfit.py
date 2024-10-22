import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDoubleSpinBox, QTableWidget, QTableWidgetItem, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.products = []

        self.initUI()

    def initUI(self):

        self.promptLabel = QLabel('Please enter the following information:', self)

        self.productNameLabel = QLabel('Product Name:', self)
        self.productNameInput = QLineEdit(self)

        self.productCategoryLabel = QLabel('Product Category:', self)
        self.productCategoryInput = QLineEdit(self)

        self.quantityLabel = QLabel('Quantity:', self)
        self.quantityInput = QLineEdit(self)

        self.avgCostLabel = QLabel('Average Cost (Unit Price):', self)
        self.avgCostInput = QDoubleSpinBox(self)
        self.avgCostInput.setMaximum(1000000)

        self.scrapCostLabel = QLabel('Scrap Cost (Unit Price):', self)
        self.scrapCostInput = QDoubleSpinBox(self)
        self.scrapCostInput.setMaximum(1000000)

        self.unitWeightLabel = QLabel('Unit Weight (kg):', self)
        self.unitWeightInput = QDoubleSpinBox(self)
        self.unitWeightInput.setMaximum(100000)

        self.submitButton = QPushButton('Add Product', self)
        self.submitButton.clicked.connect(self.process_data)

        self.finishButton = QPushButton('Finished Adding Products', self)
        self.finishButton.clicked.connect(self.show_products)


        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "Product Name", "Quantity", "Avg Cost (Unit Price)", "Semi-Finished Total Cost",
            "Scrap Cost (Unit Price)", "Scrap Total Cost", "Loss (%)", "Product Category", "Unit Weight (kg)"
        ])


        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(8, 150)


        vbox = QVBoxLayout()

        vbox.addWidget(self.promptLabel)

        vbox.addWidget(self.productNameLabel)
        vbox.addWidget(self.productNameInput)

        vbox.addWidget(self.productCategoryLabel)
        vbox.addWidget(self.productCategoryInput)

        vbox.addWidget(self.quantityLabel)
        vbox.addWidget(self.quantityInput)

        vbox.addWidget(self.avgCostLabel)
        vbox.addWidget(self.avgCostInput)

        vbox.addWidget(self.scrapCostLabel)
        vbox.addWidget(self.scrapCostInput)

        vbox.addWidget(self.unitWeightLabel)
        vbox.addWidget(self.unitWeightInput)

        vbox.addWidget(self.submitButton)
        vbox.addWidget(self.finishButton)

        vbox.addWidget(self.tableWidget)

        self.setLayout(vbox)

        self.setWindowTitle('Product Information Entry')
        self.setGeometry(300, 300, 1200, 500)
        self.show()

    def process_data(self):

        productName = self.productNameInput.text()
        productCategory = self.productCategoryInput.text()
        try:
            quantity = int(self.quantityInput.text())
            avgCost = float(self.avgCostInput.value())
            scrapCost = float(self.scrapCostInput.value())
            unitWeight = float(self.unitWeightInput.value())

            semiFinishedTotalCost = quantity * avgCost
            scrapTotalCost = quantity * scrapCost
            loss = semiFinishedTotalCost - scrapTotalCost
            lossPercentage = (loss / semiFinishedTotalCost) * 100

            rowIndex = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowIndex)

            self.tableWidget.setItem(rowIndex, 0, QTableWidgetItem(productName))
            self.tableWidget.setItem(rowIndex, 1, QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(rowIndex, 2, QTableWidgetItem(str(avgCost)))
            self.tableWidget.setItem(rowIndex, 3, QTableWidgetItem(str(semiFinishedTotalCost)))
            self.tableWidget.setItem(rowIndex, 4, QTableWidgetItem(str(scrapCost)))
            self.tableWidget.setItem(rowIndex, 5, QTableWidgetItem(str(scrapTotalCost)))
            self.tableWidget.setItem(rowIndex, 6, QTableWidgetItem(f"%{lossPercentage:.2f}"))
            self.tableWidget.setItem(rowIndex, 7, QTableWidgetItem(productCategory))
            self.tableWidget.setItem(rowIndex, 8, QTableWidgetItem(str(unitWeight)))

            QMessageBox.information(self, 'Success', f"Product '{productName}' added. You can add another product.")

            self.productNameInput.clear()
            self.productCategoryInput.clear()
            self.quantityInput.clear()
            self.avgCostInput.setValue(0)
            self.scrapCostInput.setValue(0)
            self.unitWeightInput.setValue(0)

        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid numerical values!')

    def show_products(self):
        QMessageBox.information(self, 'Completed', 'Product entry is complete. All products are shown in the table.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
