import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': './chicago.csv',
             'new york city': './new_york_city.csv',
             'washington': './washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by, or 0 to apply no month filter
        (int) day - number of the day of week to filter by
        Note that if day filtering is selected, the returned day will be -1 from the
        original user input, to be prepared for the dayofweek method in next function
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # day & month are initialized to return all data - only modified if user chooses to do so
    city = 'nocity'
    day = 8
    month = 0
    while city not in ['chicago', 'new york city', 'washington']:
        print('You may choose to examine data from Chicago, New York City, or Washington.')
        city = input(
            'Which city would you like to get data from? ').lower().strip()
    filter = 'x'
    print('Would you like to filter the data by month (M) or day (D) or not at all (A)?')
    while filter.lower().strip() not in ['m', 'd', 'a']:
        filter = input('Choose a filter: ')
    # get user input for month (Jan - Jun), if desired
    if filter.lower().strip() == 'm':
        while month not in [1, 2, 3, 4, 5, 6]:
            print(
                'Data is available for Jan (1), Feb (2), Mar (3), Apr (4), May (5), or Jun (6).')
            try:
                # take data in string form and convert to integer
                month = int(
                    input('Please enter what # month you want data from: '))
            except:
                print("Please enter the month in numeric form (1 - 6).")
                continue
    # get user input for day of week (Mon - Sun), if desired
    elif filter.lower().strip() == 'd':
        while day not in [0, 1, 2, 3, 4, 5, 6]:
            print('Data is available for each day of the week, Mon (1) through Sun (7).')
            try:
                # day must be converted to 0 - 6 integer format from string
                day = int(
                    input('Please enter what # day you want data from: ')) - 1
            except:
                print("Please enter the day in numeric form (1 - 7).")
                continue
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by, or 0 to apply no month filter
        (int) day - number of the day of week to filter by, or 8 to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert date column from strings to datetime, and rename to avoid spaces
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df = df.rename(columns={'Start Time': 'start_time'})
    # convert date column from strings to datetime, and rename to avoid spaces
    df['End Time'] = pd.to_datetime(df['End Time'])
    df = df.rename(columns={'End Time': 'end_time'})
    # apply filtering if user changed month/day values from "all" presets
    if month != 0:
        df = df[df['start_time'].dt.month == month]
    elif day != 8:
        df = df[df['start_time'].dt.dayofweek == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # add new columns to dataframe isolating different datetime fields
    # POTENTIAL IMPROVEMENT: If SQL could be used here to access DATE_TRUNC
    #   function, that would be ideal.  pandasql works in SQLite, and SQLite
    #   does not appear to have the DATE_TRUNC function, only workarounds.
    df['month'] = df['start_time'].dt.month
    df['day_of_week'] = df['start_time'].dt.dayofweek
    df['hour'] = df['start_time'].dt.hour
    # establish count dataframes for each field to pull index and value from
    month_df = df['month'].value_counts()
    dow_df = df['day_of_week'].value_counts()
    hour_df = df['hour'].value_counts()
    # display the most common month and associated value
    # dictionary maps numerical month to month name
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June"
    }
    print("The most common month for trips was: ",
          month_dict[month_df.index[0]])
    print("{} trips occurred during this month".format(month_df.iloc[0]))
    print("\n")
    # display the most common day of week and associated value
    # dictionary maps numerical day to day name
    day_dict = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    print("The most common day of the week for trips was: ",
          day_dict[dow_df.index[0]])
    print("{} trips occurred on this day of the week".format(dow_df.iloc[0]))
    print("\n")
    # display the most common start hour and associated value
    print("The most common hour for trips was: ", hour_df.index[0])
    print("{} trips occurred during this hour".format(hour_df.iloc[0]))
    # Clean up my original df from the month/dow/hour columns
    df.drop(columns=['month', 'day_of_week', 'hour'], axis=1, inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # temporary dataframes of value counts to take index and count from
    start_df = df['Start Station'].value_counts()
    end_df = df['End Station'].value_counts()
    # combine start & end station fields into a single long string, which
    # can then be counted itself, instead of trying to count across two columns
    trip_df = (df['Start Station'] + " to " + df['End Station']).value_counts()
    # display most commonly used start station and associated value
    print("Most common start station: ", start_df.index[0])
    print("This station was the start of {} trips.".format(start_df.iloc[0]))
    print("\n")
    # display most commonly used end station and associated value
    print("Most common end station: ", end_df.index[0])
    print("This station was the end of {} trips.".format(end_df.iloc[0]))
    print("\n")
    # display most frequent combination of start station and end station trip
    print("The most frequent trip was: ", trip_df.index[0])
    print("This trip was taken {} times".format(trip_df.iloc[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time (in seconds (raw) and in days)
    print("Total travel time (in seconds): ", df['Trip Duration'].sum())
    print("Total travel time (in days): ", df['Trip Duration'].sum() / 86400)
    print("\n")
    # display mean travel time (in seconds (raw) and in minutes)
    print("Average travel time (in seconds): ", df['Trip Duration'].mean())
    print("Average travel time (in minutes): ",
          df['Trip Duration'].mean() / 60)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    users_df = df['User Type'].value_counts()
    print("Here is the breakdown of customer types:\n")
    print("Subscribers: ", users_df.loc['Subscriber'])
    print("Customers: ", users_df.loc['Customer'])
    # Chicago had 1 instance of "Dependent" to be handled, NYC/Wash did not
    if 'Dependent' in users_df.index:
        print("Dependents: ", users_df.loc['Dependent'])
    # Display counts of customer genders:
    print("\n")
    if 'Gender' in df.columns:
        print("Gender data is available for this city!")
        print("Here is a breakdown of customers by gender:\n")
        gender_df = df[['Gender']]
        gender_df = df.dropna(axis=0)
        gender_df = df['Gender'].value_counts()
        print("Male: ", gender_df.loc['Male'])
        print("Female: ", gender_df.loc['Female'])
        print("\n")
    # Display earliest, most recent, and most common year of birth
        print("Birth year data is available for this city!")
        print("Here are some stats on customers' birth years:\n")
        # converting Birth Year value to int for readability
        print("The earliest birth year is: ", int(df['Birth Year'].min()))
        print("The latest birth year is: ", int(df['Birth Year'].max()))
        print("The most common birth year is: ", int(df['Birth Year'].mode()))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def data_scrolling(df):
    '''Allows user to view raw dataframe information, 5 lines at a time
    and advancing through the dataframe as directed by the user.'''
    print("\n\nWould you like to see the raw data, 5 lines at a time?")
    go = "x"
    # Loop prompting user to read raw data or skip
    while go not in ["n", "y"]:
        go = input("Please enter Y/N: ")
        try:
            go = go.lower().strip()
        except:
            print("You must enter Y or N.")
            continue
    # If user decides to read raw data, next loop is executed with an iterator
    if go == "y":
        start = 0
        prompt = "y"
        while prompt == 'y':
            # iterator mechanic is used to maintain position and provide
            # 5-line slices of raw data to the user
            print(df.iloc[start:start+5])
            start += 5
            prompt = input("Enter Y to continue ")
            try:
                prompt = prompt.lower().strip()
            except:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # My function to allow for scrolling the dataframe
        data_scrolling(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
