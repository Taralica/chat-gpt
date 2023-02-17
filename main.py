import sys

from PyQt6.QtWidgets import QMainWindow, \
    QTextEdit, QPushButton, QLineEdit, QApplication

from backend import Chatbot
import threading

class Chatbotwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(615, 400)

        # add chat area widget

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)

        # add the input field widget

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,40)

        # add the button

        self.button = QPushButton("send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style'color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        tread = threading.Thread(target=self.get_bot_responce, args=(user_input, ))
        tread.start()


    def get_bot_responce(self, user_input):
        responce = self.chatbot.get_responce(user_input)
        self.chat_area.append(f"<p style'color:#333333;background-color:E9E9E9'>Bot: {responce}</p>")

app = QApplication(sys.argv)
main_window = Chatbotwindow()
sys.exit(app.exec())