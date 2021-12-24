import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    a1 = None
    while a1 == None:
        city = input('\nPlease indicate city (Chicago, New York City, Washington): \n').lower()
        a1 = CITY_DATA.get(city)
        if a1 == None:
            print('\nThe city provided is not valid. Please try again.\n')


    # get user input for month (all, january, february, ... , june)
    a2 = False
    while a2 != True:
        month = input('\nPlease indicate month or all (january, february, ... , june): \n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            a2 = True
        else:
            print('\nThe input is not valid. Please try again.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    a3 = False
    while a3 != True:
        day = input('\nPlease indicate day of week or all (monday, tuesday, ... sunday): \n').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday ', 'friday', 'saturday', 'sunday', 'all']:
            a3 = True
        else:
            print('\nThe input is not valid. Please try again.\n')

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        index = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = months[index - 1]
        print('Most Frequent Month:', popular_month)
    else:
        print('Month filtered: ', month)

    # display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Frequent Day of Week:', popular_day)
    else:
        print('Day filtered: ', day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station)

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, ' minutes')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time, ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The types of users are the following: \n')
    print(user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nThe gender of the users are the following: \n')
        print(gender)
    except:
        print("\nThere isn't data available regarding the gender of the users\n")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth is: ', earliest)
        print('\nThe most recent year of birth is: ', most_recent)
        print('\nThe most common year of birth is: ', most_common)
    except:
        print("\nThere isn't data available regarding the birth of the users\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays five rows of raw data on demand by the user."""
    view_bool = True
    row = 0
    while view_bool == True:
        view_data = input("\nWould you like to see the raw data? Type 'Yes' or 'No'.\n").lower()
        if view_data == 'yes':
            print(df.iloc[row : row + 5, :])
            row += 5
        elif view_data != 'no':
            print('\nThe input is not valid. Please try again.\n')
        else:
            view_bool = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
