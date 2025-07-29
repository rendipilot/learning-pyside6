import sys
from dotenv import load_dotenv
import os
from openai import OpenAI
from deep_translator import GoogleTranslator
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollBar, QHBoxLayout, QWidget
from PySide6.QtCore import QFile, Qt
from ui_page2 import Ui_MainWindow  # <-- ini hasil dari pyside6-uic

load_dotenv()

client = OpenAI(
    api_key=os.getenv("KEY_OPEN"),
    base_url="https://ai.sumopod.com/v1"
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sambungkan tombol ke fungsi ganti tampilan
        self.ui.btnMenu1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btnMenu2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btnMenu3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        
        self.ui.btnTranslate.clicked.connect(self.handle_translate)
        self.ui.btnSend.clicked.connect(self.send_message)
        
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

    def send_message(self):
        teks_input_ai = self.ui.txtAi.toPlainText().strip()
        
        if not teks_input_ai:
            self.ui.txtAi.clear()
            
        self.add_bubble(teks_input_ai, sender="user")
        
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": teks_input_ai}
        ],
        max_tokens=450,
        temperature=0.7
)
        
        self.add_bubble(response.choices[0].message.content, sender="ai")
        
        self.ui.txtAi.clear()
        
        self.scroll_to_bottom()
            
        
    def add_bubble(self, text, sender="user"):
        label = QLabel(text)
        label.setWordWrap(True)
        label.setMaximumWidth(400)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        if sender == "user":
            label.setStyleSheet("background-color: lightblue; padding: 10px; border-radius: 10px;")
            alignment = Qt.AlignRight
        else:
            label.setStyleSheet("background-color: #dddddd; padding: 10px; border-radius: 10px;")
            alignment = Qt.AlignLeft
        
        bubble_layout = QHBoxLayout()
        bubble_layout.addWidget(label)
        bubble_layout.setAlignment(alignment)
        
        bubble_widget = QWidget()
        bubble_widget.setLayout(bubble_layout)

        self.ui.chatLayout.addWidget(bubble_widget)
        
    def scroll_to_bottom(self):
        scrollbar: QScrollBar = self.ui.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())