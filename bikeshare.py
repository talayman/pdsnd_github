import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=["new york city", "chicago", "washington"]
days=["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
months=["january", "february", "march", "april", "may", "june", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("May you please choose one of these cities? \nChicago \nNew York City \nWashington\n").lower()
        if city in cities:
            break
        else:
            print("Please choose one of the following cities: \nChicago, \nNew York, \nWashington\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Please choose one of the following months: \nJanuary, \nFebruary, \nMarch, \nApril, \nMay, \nJune, \nALL\n").lower()
        if month in months:
            break
        else:
            print ("Please choose one of the following months: \nJanuary, \nFebruary, \nMarch, \nApril, \nMay, \nJune, \nALL\n")
         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Could you please choose one of the weekdays: \nMonday, \nTuesday, \nWednesday, \nThursday, \nFriday, \nSaturday, \nSunday\n").lower()
        if day in days:
            break
        else:
            print("Please choose one of the weekdays: \nMonday, \nTuesday, \nWednesday, \nThursday, \nFriday, \nSaturday, \nSunday")

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
    print("The data for the city which you have chosen is loading. Please wait a sec")
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name

    if month != 'all':
        month=months.index(month)+1

        df=df [ df ['month'] == month ]
    
    if day != 'all':
        df = df [df ['day'] == day.title()]  
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    common_month = df ['month'].mode()[0]
    print('Most common month=', common_month)
    # TO DO: display the most common day of week
    common_week = df ['day'].mode()[0]
    print('Most common day of week=', common_week)
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour= df ['hour'].mode()[0]
    print('Most common hour=', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station= df['Start Station'].value_counts().idxmax()
    print('The starting station is most commonly used: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station= df['End Station'].value_counts().idxmax()
    print('The ending station is most commonly used: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    stations= df ['Start Station'] + "-" + df ['End Station']
    counts_of_trips =stations.value_counts()
    most_common_trip=counts_of_trips.idxmax()
    combination_start_station=most_common_trip.split('_')[0]
    #combination_end_station=most_common_trip.split('_')[1]
    print('Most frequent combination of start station and end station trip:', combination_start_station)
    #combination_end_station

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration for entered destinations."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df ['Trip Duration'].sum()
    m, s = divmod(total_travel_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("Total travel time: %d days, %d hours, %d min, %d sec" % (d, h, m, s))
    

    # TO DO: display mean travel time
    average_travel_time= df ['Trip Duration'].mean()
    m, s = divmod(average_travel_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("Average travel time: %d hours, %d min, %d sec" % (h, m, s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df ['User Type'].value_counts()
    print('Count of user types: \n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender= df['Gender'].value_counts()
        print('Counts of gender: \n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year= df ['Birth Year'].min()
        print('The earliest year of birth:', earliest_year)
    
        most_recent_year= df ['Birth Year'].max()
        print('The most recent year of birth:', most_recent_year)
        
        common_birth = df['Birth Year'].mode()[0]
        print('The common year of birth:', common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    i = 0
    answer = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if answer != 'no':
            print(df[i:i+5])
            raw = input('\nWould you like to see next rows of raw data?\n type: yes or nı \n').lower()
            i += 5       
        else:
            break
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
