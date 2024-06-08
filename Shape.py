from PyQt5.QtWidgets import (
    QMessageBox,
)

from PyQt5.QtGui import (
    QValidator,
)

from PyQt5.QtGui import (
    QPixmap,
)

class ShapeFunctionality:

    def custom_messagebox(self, text="Error!"):
        messagebox = QMessageBox(QMessageBox.Warning, "Error", text, buttons = QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap('stop_writing.png'))
        messagebox.exec_()

    def check_state_and_set_color(self, sender):
        """
        This function checks the validation state of a QLineEdit sender and sets its background color accordingly.

        Args:
            sender (QtWidgets.QLineEdit): The QLineEdit widget whose state and color need to be updated.
        """
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        color = '#f6989d'  # Default color (red)

        if sender.text() == "":
            color = '#f6989d'  # Empty field remains red
        elif state == QValidator.Acceptable or sender.text() == "0":
            color = '#c4df9b'  # Valid input turns green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # Intermediate state turns yellow

        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
    
    def check_state_rad_and_set_color(self, sender):
        """
        This function checks the validation state of a QLineEdit sender and sets its background color accordingly.

        Args:
            sender (QtWidgets.QLineEdit): The QLineEdit widget whose state and color need to be updated.
        """
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]

        if sender.text() == "0" or sender.text() == "":
            color = '#f6989d' # Empty or "0" field remains red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # Valid input turns green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # Intermediate state turns yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)