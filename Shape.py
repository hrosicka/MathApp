from PyQt5.QtWidgets import (
    QMessageBox,  # Import for creating message boxes
    QComboBox,    # Import for creating combo boxes
)

from PyQt5.QtGui import (
    QValidator,   # Import for input validation
)

from PyQt5.QtGui import (
    QPixmap,     # Import for loading images
)

class ShapeFunctionality:

    def custom_messagebox(self, text="Error!"):
        """
        Displays a custom message box with an error icon.

        Args:
            text (str, optional): The message to display. Defaults to "Error!".
        """
        messagebox = QMessageBox(QMessageBox.Warning, "Error", text, buttons = QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap('stop_writing.png'))
        messagebox.exec_()

    def custom_combo(self):
        """
        Creates a custom QComboBox widget with a predefined list of colors.

        Args:
            self: The parent widget.

        Returns:
            QComboBox: A QComboBox widget populated with color options.
        """

        # Create a new QComboBox instance and set its parent widget
        custom_combo = QComboBox(self)

        # Define a list of color names to populate the combo box
        colors = ["black", "blue", "gray", "green", "magenta",
                "orange", "pink", "red", "violet", "yellow"]
        
        # Add all color names to the combo box's item list
        custom_combo.addItems(colors)

        # Set a fixed width and height for the combo box to ensure consistent appearance
        custom_combo.setFixedWidth(150)
        custom_combo.setFixedHeight(28)

        # Return the created QComboBox instance
        return custom_combo

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