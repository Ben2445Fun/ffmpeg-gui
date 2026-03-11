"""A GUI for FFMPEG
"""

__authors__ = "Benjamin Arent", "Christain Tuttle"
__data__ = "3/10/2026"

from PySide6 import QtCore, QtWidgets  # , QtGui
import sys
import subprocess


class FfmpegGui(QtWidgets.QWidget):
    """The GUI for ffmpeg

    Args:
            QtWidgets (_type_): Parent class to create a GUI
    """
    _instance: "FfmpegGui | None" = None  # Singleton

    def __new__(cls) -> "FfmpegGui":
        """Create a new GUI
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialization of the GUI
        """
        # Get ffmpeg
        ffmpeg = subprocess.run(
            ['ffmpeg', '-formats'], capture_output=True, text=True)
        if ffmpeg.returncode == 127 or True:  # or True to test
            # If ffmpeg not installed, pop-up requesting its installation
            self.notin = QtWidgets.QMessageBox()
            self.notin.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            self.notin.setText("Error")
            self.notin.setInformativeText(
                'FFMPEG was not found! Please install FFMPEG to continue')
            self.notin.setWindowTitle("FFMPEG Not Found")
            self.notin.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Close)
            self.notin.addButton(
                QtWidgets.QMessageBox.StandardButton.Help)
            self.notin.resize(600, 200)
            self.notin.exec()
            exit()
        super().__init__()
        self.input = QtWidgets.QLineEdit()
        self.input_file = QtWidgets.QPushButton("Find File")
        self.convert = QtWidgets.QPushButton("Convert")
        self.lt = QtWidgets.QVBoxLayout(self)
        self.lt.addWidget(self.input)
        self.lt.addWidget(self.input_file)
        self.lt.addWidget(self.convert)
        self.input_file.clicked.connect(self.promptinputfile)
        self.convert.clicked.connect(self.beginconversion)

    def enable(self) -> None:
        """Shows the GUI
        """
        self.resize(800, 600)
        self.show()

    @QtCore.Slot()
    def beginconversion(self) -> None:
        """Attempts the conversion
        """

    @QtCore.Slot()
    def promptinputfile(self) -> None:
        """Let's the user find a file via the file explorer
        """
        self.fileprompt = QtWidgets.QFileDialog()
        print(self.fileprompt.getOpenFileName())

    @staticmethod
    def main() -> None:
        """The main function for the GUI
        """
        app = QtWidgets.QApplication([])
        gui = FfmpegGui()
        gui.enable()
        sys.exit(app.exec())


if __name__ == "__main__":
    FfmpegGui.main()
