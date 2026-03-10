from PySide6 import QtCore, QtWidgets  # , QtGui
import random
import sys
"""A GUI for FFMPEG
"""

__authors__ = "Benjamin Arent", "Christain Tuttle"
__data__ = "3/10/2026"


class FfmpegGui(QtWidgets.QWidget):
    """The GUI for ffmpeg

    Args:
            QtWidgets (_type_): ???
    """
    _instance: "FfmpegGui | None" = None  # Singleton

    def show(self) -> None:
        """Something
            """
        self.resize(800, 600)
        self.show()

    def __new__(cls) -> "FfmpegGui":
        """Create a new GUI
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialization of the GUI
        """
        super().__init__()
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            "Hello World", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lt = QtWidgets.QVBoxLayout(self)
        self.lt.addWidget(self.text)
        self.lt.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self) -> None:
        self.text.setText(random.choice(self.hello))

    @staticmethod
    def main() -> None:
        """The main function for the GUI
        """
        app = QtWidgets.QApplication([])
        gui = FfmpegGui()
        gui.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    FfmpegGui.main()
