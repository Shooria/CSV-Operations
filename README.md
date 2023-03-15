# CSV-Operations
Internship Assignment

**CSV Tool:**
CSV Tool is a command-line tool for working with CSV files. It provides several commands for loading, filtering, and analyzing data in CSV format.

**Installation:**

To use CSV Tool, we will need to have Python 3 installed on our computer.

Once we have Python installed, we can download the CSV Tool program files from the GitHub repository. Save the files to a directory of our choice.

**Usage:**

To use CSV Tool, open a command prompt or terminal and navigate to the directory where the program files are saved. Then run the program using the following command:
**python my_csv_tool.py [filename]**

Replace [filename] with the name of the CSV file you want to load. If you don't specify a filename, you can load a file from within the program using the load command, which i've done in my assignment.

Once the program is running, you can enter commands one at a time and press enter to execute them. The available commands are:

                load <file>: Load a CSV file into memory.
                count: Count the number of rows in the currently loaded CSV file.
                mean <column>: Calculate the mean of a numeric column in the currently loaded CSV file.
                filter <column> <value>: Filter the currently loaded CSV file to include only rows where the specified column matches the specified value.
                sort <column>: Sort the currently loaded CSV file by the specified column.
                std <column>: Calculate the standard deviation of a numeric column in the currently loaded CSV file.
                exit: Exit the program.
Here is an example of how to use the program:

                > load filename.csv
                > count
                 6
                > mean salary
                 67500.0
                > filter department HR
                > count
                 2
                > exit

**Tests:**

The CSV Tool program includes a set of unit tests to ensure that it is functioning correctly. To run the tests, navigate to the directory where the program files are saved and run the following command:

>>> python -m unittest test_my_csv_tool.py
This will run the test suite and output the results.

**Dependencies:**
CSV Tool requires Python 3 and the following third-party libraries:
argparse
csv
If you don't already have these libraries installed, you can install them using the following command:

**pip install argparse csv**
Alternatively, you can install them manually from their respective websites:
argparse
csv
