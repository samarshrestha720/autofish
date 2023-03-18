from PyQt6.QtWidgets import (QApplication, QSpacerItem, QSpacerItem, QLineEdit,
                             QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton)
from PyQt6.QtCore import QSize, Qt
#from PyQt6.QtMultimedia import QSoundEffect
from sys import argv
from main import fishy


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(600, 500))
        self.fishyObj = fishy()
        self.init_window()

    def init_window(self):
        # Create a QWidget to hold the QHBoxLayout
        widget1 = QWidget(self)
        # set the height to half of the window height
        widget1.setFixedHeight(self.height() // 3)

        # created layout for getting coordinates
        layout1 = QHBoxLayout(widget1)

        self.my_label = QLabel("Appear here")  # prints the coordinates
        self.my_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse)
        font = self.my_label.font()
        font.setPointSize(15)
        self.my_label.setFont(font)
        layout1.addWidget(self.my_label)

        self.cordButton = QPushButton("Get Coordinates", self)
        self.cordButton.clicked.connect(self.call_get_cords)
        layout1.addWidget(self.cordButton)

        # Create a second QWidget to hold the second QHBoxLayout
        widget2 = QWidget(self)

        # Create a QHBoxLayout for the second QWidget
        layout2 = QVBoxLayout(widget2)
        layout2.setSpacing(10)

        # add first text field to second layout
        self.text_field1 = QLineEdit()
        self.text_field1.setFixedWidth(200)
        layout2.addWidget(self.text_field1)

        # add second text field to second layout
        self.text_field2 = QLineEdit()
        self.text_field2.setFixedWidth(200)
        layout2.addWidget(self.text_field2)

        # add button and label
        self.runButton = QPushButton("Start")
        self.runButton.setFixedSize(100, 50)
        self.output = QLabel("Status: ")
        layout2.addWidget(self.runButton)
        layout2.addWidget(self.output)

        # Use a QVBoxLayout to stack the two widgets vertically
        layout = QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)

        # Set the QVBoxLayout as the central widget of the QMainWindow
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def call_get_cords(self):
        self.cordButton.setEnabled(False)
        self.my_label.setText(self.fishyObj.get_cords())
        self.cordButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
