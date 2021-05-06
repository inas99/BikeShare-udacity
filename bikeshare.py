"""
Description: In Bikeshare.py we are using python to understand and analyze US.bikesaare data.
Author: Inas Talhi
"""
import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns',200)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to ha

    city = input("Wich city are you exploring? chicago, new york city or washington? Please enter the name of the city: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("This city name is inavalid, please input a name from these (chicago,new york city, washington) : ").lower()
    # get user input for month (all, january, february, ... , june)
    months= ['january','february', 'march', 'april', 'may', 'june']
    month = input("Wich month are you exploring?Please enter the name of a month from these (January, February, March, April, May, June): ").lower()
    while month not in months:
        month = input("This month name is inavalid, please input a name from these (January, February, March, April, May, June) : ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Wich day are you exploring?  Please enter the day from these (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday): ").lower()
    days= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while day not in days:
        day = input("This day name is inavalid, please input a name from these (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) : ").lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    print("The most frequent start station is: {} ".format(df['Start Station'].mode().values[0]))

    #  display most commonly used end station
    print("The most frequent end station is: {} ".format(df['End Station'].mode().values[0]))


    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['Start Station'] 
    print("The most frequent combination of start and end station is: {} ".format(df['routes'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df["User Type"].value_counts
        print("The counts of various user types are : ",user_types)
        
    except Execption as e:
        print('The type of users couldn\'t be calculated: {}'.format(e))


    # Display counts of gender
    if city != 'washington':
        try:
            gender_types = df["Gender"].value_counts()
            print("Gender Types:", gender_types)
            
        except Execption as e:
            print('The gender  of users couldn\'t befound: {}'.format(e))
            
               
    # Display earliest, most recent, and most common year of birth
    Most_recent_Year = df["Birth Year"].min()
    print("Earliest Year:", Most_recent_Year)
    
    Most_common_Year = df["Birth Year"].max()
    print("Earliest Year:", Most_common_Year)
    
    Earliest_Year = df["Birth Year"].mode()
    print("Earliest Year:", Earliest_Year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        start_loc = 0
        end_loc = 5
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            input("Would you like to keep going?: ").lower()
            if end_display == 'no':
                break
               

        restarting = input('\nWould you like to restart? (use y or n )\n')
        if restarting.lower() != 'y':
            break


if __name__ == "__main__":
	main()