import os

from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,  # Import for creating message boxes
    QComboBox,    # Import for creating combo boxes
)

from PyQt5.QtGui import (
    QValidator,   # Import for input validation
)

from PyQt5.QtGui import (
    QPixmap,     # Import for loading images
)

import pandas as pd

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

    def export_excel(self, shape):
        """
        Exports shape calculation data and plot to an Excel file.

        This function retrieves data from the user interface, creates Pandas DataFrames,
        and writes them to a new Excel file with formatting. It also saves the shape plot
        (assuming it's a Matplotlib figure) as an image and inserts it into the Excel sheet.

        Raises:
            Exception: If an error occurs during the export process.
        """
        file_name, _ = QFileDialog.getSaveFileName(
        self, 'Export to Excel', os.path.join(os.getcwd(), 'Results', f"{shape}.xlsx"), 'Excel (*.xlsx)')

        if not file_name:
            return  # User canceled the file selection dialog

        # Prepare data for the Excel sheet
        try:
            if shape == 'Circle':
                # Create dictionaries containing circle property data and calculation results
                data = {
                'Property': [self.label_radius.text(),
                            self.label_centerX.text(),
                            self.label_centerY.text()],
                'Value': [float(self.edit_radius.text()), 
                        float(self.edit_centerX.text()),
                        float(self.edit_centerY.text())],
                'Unit': ['cm', 
                        'cm',
                        'cm']
                }

                results = {
                'Result': [self.label_perimeter.text(),
                            self.label_area.text()],
                'Value': [float(self.label_res_perimeter.text()), 
                        float(self.label_res_area.text())],
                'Unit': ['cm', 
                        'cm²']
                }

            elif shape == 'Ellipse':
                # Create dictionaries containing ellipse property data and calculation results
                data = {
                'Property': [self.label_axis_a.text(),
                            self.label_axis_b.text(),
                            self.label_centerX.text(),
                            self.label_centerY.text()],
                'Value': [float(self.edit_axis_a.text()),
                        float(self.edit_axis_b.text()), 
                        float(self.edit_centerX.text()),
                        float(self.edit_centerY.text())],
                'Unit': ['cm', 
                        'cm',
                        'cm',
                        'cm']
                }

                results = {
                'Result': [self.label_perimeter.text(),
                            self.label_area.text()],
                'Value': [float(self.label_res_perimeter.text()), 
                        float(self.label_res_area.text())],
                'Unit': ['cm', 
                        'cm²']
                }

            elif shape == 'Square':
                # Create dictionaries containing square property data and calculation results
                data = {
                'Property': [self.label_side.text(),
                            self.label_centerX.text(),
                            self.label_centerY.text()],
                'Value': [float(self.edit_side.text()), 
                        float(self.edit_centerX.text()),
                        float(self.edit_centerY.text())],
                'Unit': ['cm', 
                        'cm',
                        'cm']
                }

                results = {
                'Result': [self.label_perimeter.text(),
                            self.label_area.text()],
                'Value': [float(self.label_res_perimeter.text()), 
                        float(self.label_res_area.text())],
                'Unit': ['cm', 
                        'cm²']
                }

            elif shape == 'Sphere':
                # Create dictionaries containing square property data and calculation results
                data = {
                'Property': [self.label_radius.text(),
                            self.label_centerX.text(),
                            self.label_centerY.text(),
                            self.label_centerZ.text()],
                'Value': [float(self.edit_radius.text()), 
                        float(self.edit_centerX.text()),
                        float(self.edit_centerY.text()),
                        float(self.edit_centerZ.text())],
                'Unit': ['cm',
                        'cm',
                        'cm',
                        'cm']
                }

                results = {
                'Result': [self.label_surface.text(),
                            self.label_volume.text()],
                'Value': [float(self.label_res_surface.text()), 
                        float(self.label_res_volume.text())],
                'Unit': ['cm²', 
                        'cm³']
                }

            elif shape == 'Ellipsoid':
                # Create dictionaries containing square property data and calculation results
                data = {
                'Property': [self.label_axis_a.text(),
                            self.label_axis_b.text(),
                            self.label_axis_c.text(),
                            self.label_centerX.text(),
                            self.label_centerY.text(),
                            self.label_centerZ.text()],
                'Value': [float(self.edit_axis_a.text()),
                        float(self.edit_axis_b.text()),
                        float(self.edit_axis_c.text()),
                        float(self.edit_centerX.text()),
                        float(self.edit_centerY.text()),
                        float(self.edit_centerZ.text())],
                'Unit': ['cm',
                        'cm',
                        'cm',
                        'cm',
                        'cm',
                        'cm']
                }

                results = {
                'Result': [self.label_surface.text(),
                            self.label_volume.text()],
                'Value': [float(self.label_res_surface.text()), 
                        float(self.label_res_volume.text())],
                'Unit': ['cm²', 
                        'cm³']
                }

            # Create Pandas DataFrames from the dictionaries
            df = pd.DataFrame(data)
            df_res = pd.DataFrame(results)

            # Create an Excel writer object with the specified filename
            writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

            # Create a workbook and worksheet within the Excel writer
            workbook = writer.book
            worksheet = workbook.add_worksheet(f"{shape} Calculation")

            # Define a header format with background color and styling
            header_format = workbook.add_format({
                'bg_color': '#EAF1FF',
                'bold': True,
                'align': 'center',
                'valign': 'vcenter',
                'border': 1
            })

            # Determine starting rows for property and result data
            property_start_row = 0
            result_start_row = 8

            # Write the circle property data to the Excel sheet
            df.to_excel(writer, sheet_name=f"{shape} Calculation", startrow=property_start_row, startcol=0, index=False)

            # Write the calculation results data to the Excel sheet with a starting row offset
            df_res.to_excel(writer, sheet_name=f"{shape} Calculation", startrow=result_start_row, startcol=0, index=False)


            # Write the column headers for both dataframes using the defined format
            for col_idx, col in enumerate(df.columns):
                worksheet.write(0, col_idx, col, header_format)
            for col_idx, col in enumerate(df_res.columns):
                worksheet.write(8, col_idx, col, header_format)

            image_file = f".\\Results\\{shape}_plot.png"
            image_cell = 'E2'  # Adjust default image cell if needed

            # Save the Matplotlib figure (assuming self.fig is a valid figure) as an image
            self.fig.savefig(image_file)

            # Insert the saved image into the worksheet at the specified cell
            worksheet.insert_image(image_cell, image_file)
            
            writer.close()

            QMessageBox.information(self, 'Success', 'Data exported to Excel successfully.')

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'An error occurred while exporting the data: {e}')