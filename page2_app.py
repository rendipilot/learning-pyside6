import sys
from deep_translator import GoogleTranslator
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
        
        self.ui.btnTranslate.clicked.connect(self.handle_translate)
        
    def handle_translate(self):
        # Ambil teks dari QTextEdit Bahasa Indonesia
        teks_indo = self.ui.txtIndo.toPlainText().strip()

        # Cek apakah kosong
        if not teks_indo:
            # Kosong → kosongkan output & keluar dari fungsi
            self.ui.txtEng.clear()
            return

        # Translate pakai Deep Translator
        try:
            hasil = GoogleTranslator(source='id', target='en').translate(teks_indo)
            self.ui.txtEng.setPlainText(hasil)
        except Exception as e:
            self.ui.txtEng.setPlainText(f"Terjadi kesalahan:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())