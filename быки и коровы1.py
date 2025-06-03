import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QApplication,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Быки и коровы")
        self.setGeometry(100, 100, 800, 500)
        self.setFixedSize(800, 500)

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 800, 500)

        self.start_background = QPixmap(
            "C:/Users/User/Desktop/bulls_cows.py/background.jpg"
        )
        self.start_background = self.start_background.scaled(
            800, 500, Qt.AspectRatioMode.IgnoreAspectRatio
        )
        self.background.setPixmap(self.start_background)

        # Помещаем фон на задний план
        self.background.lower()

        self.welcome_label = QLabel("Добро пожаловать в игру!", self)
        self.welcome_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.welcome_label.setStyleSheet(
            """
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 0.98);
                padding: 10px;
                border-radius: 15px;
            }
        """
        )
    
        self.welcome_label.adjustSize()
    
        welcome_x = (800 - self.welcome_label.width()) // 2
        welcome_y = (500 - 100) // 2 - 60  
        self.welcome_label.move(welcome_x, welcome_y)

        # Создаем кнопку "НАЧАТЬ ИГРУ"
        self.start_button = QPushButton("НАЧАТЬ ИГРУ", self)
      
        button_width = 300
        button_height = 100
        self.start_button.setGeometry(
            (800 - button_width) // 2,  
            (500 - button_height) // 2,  
            button_width,
            button_height,
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
