from PyQt6.QtWidgets import (QApplication, QSpacerItem, QLineEdit,
                             QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton)
from PyQt6.QtCore import QSize, Qt, QObject, QThread, pyqtSignal, Q_ARG, QMetaObject
#from PyQt6.QtMultimedia import QSoundEffect
from sys import argv
from macha import fishy


class FishyWorker(QObject):
    finished_signal = pyqtSignal(str)
    op_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.fishyObjS = fishy()
        self.op_signal = self.fishyObjS.operation_signal

    def get_cords(self):
        return self.fishyObjS.get_cords()

    def set_cords(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def run(self):
        self.fishyObjS.run(self.cord1, self.cord2)

    def stop(self):
        self.fishyObjS.stop()
        self.finished_signal.emit("Stopped!")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Macchi Marana hau")
        self.setFixedSize(QSize(600, 500))
        self.fishy_worker = FishyWorker()
        self.fishy_thread = QThread(self)
        self.fishy_worker.moveToThread(self.fishy_thread)
        self.fishy_worker.finished_signal.connect(self.thread_finished)
        self.fishy_thread.started.connect(self.fishy_worker.run)
        # self.fishy_thread.started.connect(
        #     lambda: self.fishy_worker.run(self.c1, self.c2))

        self.init_window()  # initialize window

    def init_window(self):
        # Create a QWidget to hold the QHBoxLayout
        widget1 = QWidget(self)
        # set the height to half of the window height
        widget1.setFixedHeight(self.height() // 3)

        # created layout for getting coordinates
        layout1 = QHBoxLayout(widget1)

        # prints the coordinates
        self.my_label = QLabel("Coordinates Appear Here")
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
        self.runButton.clicked.connect(self.buttonOp)

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
        self.fishy_worker.op_signal.connect(self.update_output)

    def buttonOp(self):
        if (self.runButton.text() == "Start"):
            self.c1 = self.text_field1.text()
            self.c2 = self.text_field2.text()
            self.fishy_worker.set_cords(self.c1, self.c2)
            self.runButton.setText("Stop")
            self.fishy_thread.start()
        else:
            self.runButton.setText("Start")
            self.fishy_worker.stop()

    def thread_finished(self, message):
        self.output.setText(f"{message}")
        self.runButton.setText("Start")

    def call_get_cords(self):
        self.cordButton.setEnabled(False)
        self.my_label.setText(self.fishy_worker.get_cords())
        self.cordButton.setEnabled(True)

    def update_output(self, message):
        self.output.setText(f"{message}")  # displays output on the gui


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
