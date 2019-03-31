# Screening Task 2: Create an Application using PyQt/Kivy
### Technologies/Libraries to use:

- Python
- PyQt/Kivy

### Instructions:

1. Create a Github Account or Use your existing one.
2. Create a new Repository in your Github Account for this task called fsf_2019_screening_task2
3. Commit your code at regular intervals by doing small incremental changes to your code (committing huge blobs of code all at once is not recommended).
4. The steps in “Description” below are general, minimum and mandatory guidelines. You are free to add well-documented features to your application.

### Description:

##### Following functionalities should be present in the application.

User should be able to:

1. Load a csv file using ‘Load’ option available under “File” menu
2. Display the complete data from the loaded csv as a table
3. Edit the existing data in the table using the ‘Edit data’ option under the “Edit” menu.
4. Add new data to the table using ‘Add data’ option under “File” menu.
5. Select any number of columns from the displayed table
6. Plot the data from any two selected columns should be available as buttons as mentioned below:

Plot scatter points
- Plot scatter points with smooth lines
- Plot lines
- Click on any of the plot button. Plot should be generated accordingly in a new tab.
- Label x-axis and y-axis accordingly.
- Add a title to the graph.
- Save the plot as .png file using ‘Save as png’ option under “File” menu.

## Install PyQt4
Installing PyQt4 on a Ubuntu Machine
```sh
$ apt-cache search pyqt
$ sudo apt-get install python-qt4
```

### Running The App
As Python3 is used to build the app, it can be run by: 
```sh
$ python3 app.py
```
### Bugs

- Closing the Scatter Plots and creating again will show a blank page
- After Creating the Plots, only by clicking the other buttons will change the plot
- Only a Single Column can be selected for plotting the graph

License
----

MIT
