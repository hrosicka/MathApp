# MathApp - Explore 2D and 3D Shapes
This interactive application allows you to visualize and learn about various geometric shapes. Still in progress...

## Key Features:

- **Multiple Shapes:** Explore circles, spheres, ellipses, ellipsoids, squares, and cubes.
- **Interactive Windows:** Each shape has a dedicated window for detailed exploration.
- **Graphical Representation:** Visualize the shapes using appropriate graphical elements.
- **User-friendly Interface:** A clear layout with buttons and a central image for easy navigation.
- **Menu Bar:** Access options for closing the application and selecting specific shapes.

## Main window

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/MainWindow.PNG)

### Menu

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/Menu.png)

### Shortcuts:
Using keyboard shortcuts in this menu allows for quick and efficient shape drawing. Instead of navigating through the menu and finding the desired option, you can instantly select the desired shape by pressing a few keys. This can be particularly beneficial when drawing shapes repeatedly.
- **Close (Ctrl+W):** Close the application window.
- **Circle (Ctrl+1):** Open Circle. Press "1" while holding Ctrl for a quick circle!
- **Sphere (Ctrl+2):** Open Sphere. Feeling spherical? Hit Ctrl+2!
- **Ellipse (Ctrl+3):** Open Ellipse. Need an oval shape? Ctrl+3 is your friend.
- **Ellipsoid (Ctrl+4):** Open Ellipsoid. Feeling 3D? Ellipsoid it is with Ctrl+4.
- **Square (Ctrl+5):** Draw a square. Feeling boxy? Create a square with Ctrl+5.
- **Cube (Ctrl+6):** Draw a cube. Feeling cubic? Ctrl+6 to the rescue!


## Circle

### The application allows you to:
- Calculate the circumference and area of a circle.
- Visually represent the circle on a graph.
- Export the results and graph to an Excel file.
- Save the graph as an image.

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculation.PNG)

### User Interface
The application window is divided into three main sections:

- **Input Parameters:** This section contains labeled fields for entering the circle's radius, center coordinates (X and Y), and selecting a color for the graph.
- **Results:** This section displays the calculated circumference and area of the circle.
- **Graph:** This section displays a visual representation of the circle based on the entered parameters.
- **Menu Bar:** This bar located at the top of the window provides quick access to actions like solving, exporting, clearing, and closing the application.

### Menu bar
- **Solve and plot** Click this button to calculate the circle's circumference and area and plot the circle on the graph.
  
  ![](https://github.com/hrosicka/PyQtMathApp/blob/master/CalculateIcon.svg)

- **Graph Export:** Click this button to save the plotted circle as an image file (enabled after solving).

  ![](https://github.com/hrosicka/PyQtMathApp/blob/master/SavePictureIcon.svg) 

- **Excel Export:** Click this button to export the input parameters, results, and graph to an Excel file (enabled after solving).

  ![](https://github.com/hrosicka/PyQtMathApp/blob/master/ExportXLSIcon.svg)

- **Clear:** Click this button to clear all input fields, results, and the graph (disabled when results are unavailable).
  
  ![](https://github.com/hrosicka/PyQtMathApp/blob/master/ClearResultsIcon.svg)

- **Close:** Click this button to close the window.
  
  ![](https://github.com/hrosicka/PyQtMathApp/blob/master/CloseAppIcon.svg) -

### Using the Application
1. **Enter the circle's radius:** In the "Radius (r)" field, enter a positive numerical value for the circle's radius. The background color of the field will change depending on the validity of your input (red for invalid, green for valid).
   
![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculationValidation.PNG)

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculationRadiusValidation.PNG)

2. **Enter the center coordinates:** Enter the X and Y coordinates of the circle's center in the respective fields. Similar to the radius field, the background changes based on the input validity.

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculationCenterXValidation.PNG)

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculationCenterYValidation.PNG)

3. **Select a circle color:** Choose a desired color for the circle from the "Circle Color" dropdown menu.
   
![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleColorCombo.PNG)

4. **Click "Solve and Plot" button:** Click this button to trigger the calculation and visualization. The application will calculate the circle's circumference and area and plot the circle on the graph using your chosen color. The calculated values for circumference and area will be displayed in the "Results" section.

5. **Export options (after solving):** Once you have a result, the "Graph Export" and "Excel Export" buttons become enabled. Click "Graph Export" to save the plotted circle as an image file. Click "Excel Export" to save the input parameters, results, and graph to an Excel spreadsheet.
   
![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/CircleCalculationXlsxResults.PNG)

6. **Clear all (optional):** If you want to start over, click the "Clear" button. This will clear all input fields, results, and the graph. The button is disabled when there are no results to clear.

7. **Close:** Click the "Close" button (or the "X" button in the top right corner) to exit the window.

## Sphere
Calculation and plotting sphere

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/SphereCalculation.PNG)

## Ellipse
Calculation and plotting ellipse

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/EllipseCalculation.PNG)

## Square
Calculation and plotting square

![](https://github.com/hrosicka/PyQtMathApp/blob/master/doc/SquareCalculation.PNG)

## Unit Tests
### Circle
 Tests cover various aspects of the class, including:

#### Initialization Validation:
- Verifies successful object creation with valid positive radii.
- Raises errors for invalid inputs like zero, negative, or non-numeric radii.

#### Method Functionality:
- Validates the circumference method for various radii using the formula 2 * pi * radius.
- Confirms the accuracy of the area method for different circle sizes using pi * radius**2.

#### get_description Method Evaluation:
- Asserts that get_description generates clear and informative descriptions of circumference and area.
- Verifies that the returned descriptions accurately reflect the calculated values.

### Ellipse
Tests cover various aspects of the ellipse's behavior:

#### Initialization Validation:
- Confirms successful object creation with valid positive values for both semi-major and semi-minor axes.
- Raises ValueError exceptions for invalid inputs:
  - Zero or negative values for either axis length.
  - Non-numeric values (e.g., strings) for axis lengths.
    
#### Edge Case Testing:
- Handles very small positive values for the major axis (approaching zero).
- Tests initialization with very large major axis values.
  
#### Method Functionality:
- Validates the circumference method for various ellipse dimensions using the formula: circumference = pi * sqrt(2 * (a^2 + b^2)), where a is the semi-major axis and b is the semi-minor axis.
- Verifies the accuracy of the area method for different ellipses using the formula: area = pi * a * b.
#### get_description Method Evaluation:
- Asserts that get_description generates clear and informative descriptions of the ellipse's properties, including its circumference and area, formatted using the actual axis lengths.
- Confirms that the returned descriptions accurately reflect the calculated values obtained from the circumference and area methods.

[MIT LICENSE](https://github.com/hrosicka/MathApp?tab=MIT-1-ov-file#readme)


