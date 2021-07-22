### JOE'S BIKESHARE DATA ANALYSIS PROGRAM

### Date created
This bikeshare project was initially created & submitted for grading on 17 Jul 2021 for the Introduction to Python course in Udacity's Programming for Data Science with Python Nanodegree.  The bikeshare project was moved to gitHub on 21 Jul 2021 as part of my project for the Introduction to Version Control project for the same nanodegree program.  

### Description
This program was built in Python using VSCode and GitBash to analyze a provided collection of data on bikesharing programs in three US cities: Chicago, New York City, and Washington D.C.  The goal was to build an interactive program which would allow the user to select a city of their choice, a filter of their choice (filter by a given month, day, or not at all), and to then return a series of automatically generated statistics about the dataset that the user defined.   After presenting these automated statistics, the program then offered the user an opportunity to page through the raw data, 5 lines at a time, if desired.  Finally, the program would prompt the user to either restart with a new query, or exit the program entirely.  

### Files used
This project uses the following files:
* bikeshare.py (included)
  * requires Python (built on 3.8.8)
  * requires NumPy package 
  * requires PanDas package
* .csv files from Udacity containing bikesharing data for analysis (not included)

In order to run this program, the user will need to place the .csv files in the same directory as the bikesharing.py file.  

### Credits
This project was built using Python 3.8.8, NumPy, and PanDas (all via Anaconda), VSCode 1.58.2, and git version 2.31.1.windows.1.  The projects were assignments from Udacity's Programming for Data Science with Python Nanodegree, where I gained a lot of the knowledge to be able to complete them.  
Credit must be given to the following, as well, for specific help in writing the bikeshare.py program:
* [GeeksForGeeks](https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/)
  * This post helped me figure out how to convert the dates from a string into a datetime object
* [StackOverflow](https://stackoverflow.com/questions/25873772/how-to-filter-a-dataframe-of-dates-by-a-particular-month-day)
  * This post helped me filter my dataframe by month or day of the week
* [StackOverflow](https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column)
  * This post helped me figure out how to count the frequency of a value
* [StackOverflow](https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe)
  * This post helped me pull a specific cell from a dataframe to present neatly
* [TowardsDataScience](https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587)
  * This post helped me get month/dayofweek/hour data, when I couldn't make it work with SQL.