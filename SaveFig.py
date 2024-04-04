import os
import CheckCreateDirectory

from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
)


def save_fig(self, fig, name):
        """
        Saves the current figure as a PNG image.

        This method prompts the user to select a file name and location to save the
        figure as a PNG image.
        """
        path = ".\\Results"
        CheckCreateDirectory.check_create_dir(path)

        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Figure', os.path.join(os.getcwd(), 'Results', name), 'PNG (*.png)')

        if file_name:
            try:
                fig.savefig(file_name)
                QMessageBox.information(self, 'Success', 'Figure saved successfully.')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'An error occurred while saving the figure: {e}')