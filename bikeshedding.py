import datetime
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = CITY_DATA.keys()
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in cities:
        city = input(f'Pick from the list of cities \"{", ".join(cities)}\": ').lower().strip()
    month = ''

    while month not in months:
        month = input(f'Pick from the list of months \"{", ".join(months)}\": ').lower().strip()

    day = ''
    while day not in days:
        day = input(f'Pick from the list of days \"{", ".join(days)}\": ').lower().strip()

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
    # input already validates existence of key; file existence assumed
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # index already correct due to 'all' as 0th
    month_num = months.index(month)
    # monday = 0, sunday = 6 => all == -1 after adjustment
    day_num = days.index(day) - 1
    if month_num != 0:
        df = df[df['month'] == month_num]
    if day_num != -1:
        df = df[df['day_of_week'] == day_num]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month_num = df['month'].mode()[0]
    popular_dow_num = df['day_of_week'].mode()[0]
    popular_hour = (df['Start Time'].dt.hour).mode()[0]
    print(f"Most popular month: {months[popular_month_num]}")
    print(f"Most popular day of week: {days[popular_dow_num + 1]}")
    print(f"Most popular start hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start = df['Start Station'].mode()[0]
    print(f"Most common start: {popular_start}")
    popular_end = df['End Station'].mode()[0]
    print(f"Most common end: {popular_end}")
    popular_start_end = df[['Start Station', 'End Station']].mode()
    print(f"Most common start-end combination:\n{popular_start_end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = int(df['Trip Duration'].sum())
    print(f"Total travel time: {str(datetime.timedelta(seconds=total_travel_time))}")
    mean_travel_time = int(df['Trip Duration'].mean())
    print(f"Mean travel time: {str(datetime.timedelta(seconds=mean_travel_time))}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(f"Counts of users:\n{user_types}")
    genders = df['Gender'].value_counts()
    print(f"Counts of genders:\n{genders}")
    earliest_birth_year = df['Birth Year'].min()
    latest_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]
    print(f"Earliest birth year: {earliest_birth_year}")
    print(f"Latest birth year: {latest_birth_year}")
    print(f"Most common birth year: {common_birth_year}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_show_data(more = False):
    """
    Ask the user if data is to be shown.
    
    Returns:
        bool - true if the user would like to know more
    """
    question = '\nWould you like to see data? Enter yes or no.\n'
    if more:
        question = '\nWould you like to see more data? Enter yes or no.\n'
    display_data = input(question)
    if display_data.lower().strip() != 'yes':
        return False
    return True

def chunk_data(df, n):
    """
    Chunk input
    
    Attribution: Part of the training, but originally from Ned Batchelder on stackoverflow
    
    Args:
        (slicable) df: slicable to get chunks from
        int n: size of slice
    
    Returns:
        (generator) with n items
    """
    for i in range(0, len(df), n):
        yield df[i:i + n]

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_data = ask_show_data()
        gen = chunk_data(df, 5)
        while show_data:
            chunk = next(gen)
            print(chunk)
            show_data = ask_show_data(more = True)
            if not show_data:
                exit()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break


if __name__ == "__main__":
	main()
