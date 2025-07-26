import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_page2 import Ui_MainWindow  # <-- ini hasil dari pyside6-uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sambungkan tombol ke fungsi ganti tampilan
        self.ui.btnMenu1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btnMenu2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())