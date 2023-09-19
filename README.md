[![Python application test with Github Actions](https://github.com/nogibjj/DataScienceCI_YCLiu/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/DataScienceCI_YCLiu/actions/workflows/main.yml)

## Generating Descriptive Stats with A Homebrew Pandas-Based Library

This repo demonstrates how to use a homebrew library (lib.py, pandas-based) to generate descriptive statistics for pandas DataFrame. The dataset used for demo is extracted from [European Health for All database (HFA-DB)](https://gateway.euro.who.int/en/datasets/european-health-for-all-database/), which contains suicide rate and GDP per capita data for France and Albania from the 1960's to the 2010's.

The repository contains the following scripts:
<br>a. **lib.py** is a homebrew python library for generating descriptive statistics for pandas DataFrame.
<br>a. **main.ipynb**: a Jupyter Notebook containing demonstration of how to use the package and some example output.
<br>b. **main.py**: a python script containing all the python code used in main.ipynb.
<br><br>All functions were **<em>linted</em>**, **<em>tested</em>**, and **<em>formatted</em>** when pushed to the repository and passed all the steps.
<br> c. **test_lib.py**: test code for lib.py. **testCase1.csv** is used for test_lib.py.
<br> d. **test_main.py**: test code for main.py
<br>
<br> e. **.github/workflows/main.yml**: GitHUb actions for **<em>linting</em>**, **<em>testing</em>**, and **<em>formatting</em>** all the **.py** and **.ipynb** files, the executed commands of each action is specified in **MAKEFILE**.

<br>Below is a brief **documentation of the homebrew library** (**lib.py**) for generating descriptive stats:

1. **calMean**: returns the **mean** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **mean** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

2. **calMedian**: returns the **median** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **median** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

3. **calSD**: returns the **standard deviation** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **standard deviation** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

4. **countItemOcc**: returns the **count of occurrences** of the input item in the input column.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and outputs the **number of occurrences of the item** in the column.
  <br> If the input column is **not in the DataFrame**, the function **raise errors**.

5. **calItemRate**: returns the **count of occurrences over count of all non-NA rows** of the input item in the input column.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and outputs the **number of occurrences of the string over total number of non-None rows** in the column.
  <br> If the input column is **not in the DataFrame**, the function **raise errors**.

6. **printNumStats**: a simple visualization tool to print the **mean and median** of a column in a clear format.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and it **returns the mean and median** of the numerical column in the following format (string):
  <br> In *Input* column, the mean is *MeanRoundedTo2Digits* and the median is *MedianRoundedTo2Digits*.          

7. **printOccStats**: a simple visualization tool to **print the count and rate of occurrence of an item** of a column in a clear format.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and it **returns the count and rate of occurrences of an item** of the input item in the input column in the following format (string):
  <br> In *Input* column, the number of occurrences is *CountItemOccurrence*, or *RateOfItemOccurrenceRoundedTo2Digits* of total samples.        
