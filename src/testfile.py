import sys
from PySide6 import QtWidgets


class Installer(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        notin = QtWidgets.QMessageBox()
        notin.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        notin.setText("Error")
        notin.setInformativeText("Please install FFmpeg to continue.")
        notin.setWindowTitle("FFmpeg Not Found")

        install_button = notin.addButton(
            "Install FFmpeg",
            QtWidgets.QMessageBox.ButtonRole.AcceptRole
        )
        close_button = notin.addButton(
            QtWidgets.QMessageBox.StandardButton.Close
        )

        notin.exec()

        if notin.clickedButton() == install_button:
            print("install clicked")
        elif notin.clickedButton() == close_button:
            print("close clicked")


app = QtWidgets.QApplication(sys.argv)
print("before installer")
Installer()
print("after installer")
sys.exit(app.exec())