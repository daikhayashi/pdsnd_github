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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter a city name: chicago, new york city, or washington in lower case:")
    while city not in CITY_DATA:
        city = input("Please input the city name in lower case correctly from: chicago, new yourk city, or washington:")
    print('I believe you would like to know about {}! If not please abort this program and restart it').format(city)
    


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("In what month would you like to know? If all, please input 'all':").lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("In which day of week would like to know?:").lower()


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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month: ", df['month'].mode()[0])


    # TO DO: display the most common day of week
    print("The most common day of week: ", df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)
    
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station: ", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Most commonly used end station: ", df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    print("Most frequent combination of start station and end station trip: ", df['Start_End'].mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum()," sec")


    # TO DO: display mean travel time
    print("Mean travel time: ", df['Trip Duration'].mean()," sec")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_type = df['Gender'].value_counts()
        print(gender_type)
    else:
        print("Gender data does not exist!")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest year of birth: ", int(df['Birth Year'].min()))
        print("Most recent year of birth: ", int(df['Birth Year'].max()))
        print("Earliest year of birth: ", int(df['Birth Year'].mode()[0]))
    else:
        print("Year of birth data does not exit!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print('Please see the top five lines of data below:\n ', df[1:6])
        raw_data_count = input("Would you like to see 5 more lines of data? Please answer with yes or no: ")
        while_count = 1
        while raw_data_count == 'yes':
            print('Please see the next five lines of data below:\n ', df[while_count*5+1:(while_count+1)*5+1])
            while_count = while_count +1
            raw_data_count = input("Would you like to see 5 more lines of data? Please answer with yes or no: ")
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
