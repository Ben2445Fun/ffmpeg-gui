"""An error output for when ffmpeg does not run correctly
"""

__author__ = "Benjamin Arent"
__created__ = "4/15/2026"
__updated__ = "4/16/2026"

from PySide6 import QtWidgets


class ErrorOut(QtWidgets.QWidget):
    """A popup that specifies an error has occured

    Args:
        QtWidgets (_type_): Parent class to create a widget
    """

    def __init__(self, error: 'str | Exception' = 'No information given') -> None:
        """Initialize an error box
        """
        super().__init__()
        self.box = QtWidgets.QMessageBox(self)
        self.box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        self.box.setWindowTitle('Error During Conversion')
        self.box.setInformativeText(str(error))
        self.box.exec()
