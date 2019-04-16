import time
import pandas as pd
import numpy as np

from gather_input import get_input_from_user
pd.set_option('display.max_columns',None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday']

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
        city = input('Which city do you want to explore Chicago, New York city or Washington?\n').lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_input_from_user('Which month do you want to choose (e.g. all, january, february, march, april, may, june)?\n',months)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input_from_user('Which day do you want to choose (e.g. all,sunday,monday,tuesday,wednesday,thursday,friday,saturday)?\n',days)

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
    print("                exploring the bikshare data for '{}'               \n".format(city).upper())
    df = pd.read_csv(CITY_DATA[city],nrows=5000)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day'].value_counts().idxmax()
    print("The most common day of week is :",most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hr = df['hour'].value_counts().idxmax()
    print("The most common start hour :",most_common_start_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_station,most_common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = dict(df['User Type'].value_counts())
    print('Each user type counts from the given bikeshare data:\n')
    for usertype,count in counts_of_user_types.items():
        print(usertype,count)
    print()

    # TO DO: Display counts of gender
    print('Gender counts from the given bikeshare data:\n')
    if 'Gender' in df.columns:
        counts_of_gender = dict(df['Gender'].value_counts())
        for name,count in counts_of_gender.items():
            print(name,count)
    else:
        print("There is no 'Gender' column from the given city\'s bikeshare data")
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        print("The most earliest birth year :", int(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print("The most recent birth year   :", int(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("The most common birth year   :", int(most_common_year_of_birth))
    else:
        print("There is no 'Birth Year' column from the given city\'s bikeshare data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    This Function is used to display the Raw data upon request by the user.
    This Function prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes',
    and continue these prompts and displays until the user says 'no'.

    args:
        Passing the dataframe as an arugment in this function
    return:
        None
    """
    #Dropping the created columns (month,day,hour) used for previous analysis
    df=df.drop(['month','day','hour'],axis=1)

    row_count = 0

    #getting the user input 'yes' or 'no' and also using the while loop to handle the invalid inputs.
    while True:
        ReadData = input("Do you want to see the actual 'RAW DATA\'? Please input 'yes' or 'no' \n").lower()
        if ReadData in ['yes','no']:
            break

    while True:
        if ReadData == 'no':
            break
        if ReadData == 'yes':
            #Here using iloc for numerical indexing not the labeled index
            print(df.iloc[row_count: row_count + 5])
            row_count = row_count + 5
        ReadData = input("\n Do you want to see 'five more records\' of the 'RAW DATA\'? Please input 'yes' or 'no' \n").lower()

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
