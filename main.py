from main_ui import Ui_MainWindow  # Import the generated UI class
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout,
    QGridLayout, QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem,
    QLabel, QPushButton, QMessageBox, QWidget, QHeaderView
)

class LicensePlate(QMainWindow, Ui_MainWindow):
    def __init__(self, login_screen=None, db_manager=None, user=None):
        super(LicensePlate, self).__init__()
        self.setupUi(self)  # Initialize UI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlate()
    window.show()
    sys.exit(app.exec_())
