from PyQt5.QtWidgets import (
    QComboBox,
)

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