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
    
        #I just set it to true for testing now, but can change it to try/except later
        if True:
            notin = QtWidgets.QMessageBox()
            notin.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            notin.setText("Error")
            notin.setInformativeText(
                "FFMPEG was not found! Please install FFMPEG to continue"
            )
            notin.setWindowTitle("FFMPEG Not Found")
            install_button = notin.addButton("Install FFMPEG", QtWidgets.QMessageBox.ButtonRole.AcceptRole)
            close_button = notin.addButton(QtWidgets.QMessageBox.StandardButton.Close)
            notin.resize(600, 200)
            notin.exec()
            if notin.clickedButton() == install_button:
                self.installffmpeg()
            elif notin.clickButton() == close_button: 
                exit()
                
            ffmpeg = subprocess.run(
            ['ffmpeg', '-formats'], capture_output=True, text=True)
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
        
    def installffmpeg(self) -> None: 
        platform_identifier = sys.platform
        #probably some repetitive code in this function but will fix later

        #Install ffmpeg based on platform(cant on windows rn)
        if platform_identifier.startswith("win"):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Installing")
            msg.setText("You're using Windows, install online before continuing")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.exec()
        elif platform_identifier == "linux":
            msg = QtWidgets.QProgressDialog("Installing FFmpeg...", None, 0, 0)
            msg.setWindowTitle("Installing")
            msg.setLabelText("Installing FFmpeg...")
            msg.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            msg.show()
            QtWidgets.QApplication.processEvents()
            subprocess.run(["sudo", "apt", "install", "ffmpeg", "-y"])
            msg.close()
        elif platform_identifier == "darwin":
            msg = QtWidgets.QProgressDialog("Installing FFmpeg...", None, 0, 0)
            msg.setWindowTitle("Installing")
            msg.setLabelText("Installing FFmpeg...")
            msg.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            subprocess.run(["brew", "install", "ffmpeg"])
            msg.close()
        

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
