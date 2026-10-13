import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['january', 'february', 'march', 'april', 'may','june','july','all']
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
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
        city = input('Hello please specify the name of the city for which you want the data from the group {chicago, new york city, washington} : ')
        city=city.lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('specified city is not in the allowed group or wrong format')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('please specify the month you are intrested in :')
        month=month.lower()
        if month in months:
            break
        else:
            print('specified month is not allowed or wrong format')        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please specify the day you are intrested in :  ')
        day=day.lower()
        if day in days:
            break
        else:
            print('specified day is not allowed or wrong format') 
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


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month.lower()) + 1

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
    popular_month = months[df['month'].mode()[0]-1].title()
    print('Most Popular month is :  {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular weekday is :  {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Popular Start Hour is : {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('most commonly used end station is : {}'.format(
        df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    common_combo=df.groupby(['Start Station','End Station']).size(
    ).sort_values(ascending=False).index[0]
    print('most frequent combination of start station and end station trip is : {} and {}'.format(
        common_combo[0],common_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print('total travel time is : {} [s]'.format(
        df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('average travel time is : {} [s]'.format(
        df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('counts of user types are :\n {}'.format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns: 
        print('counts of gender are :  \n {}'.format(
            df['Gender'].value_counts()))
    else:
        print('current dataset has no Gender statistic') 

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest year of birth is : {}'.format(
            int(df['Birth Year'].min())))
        print('most recent year of birth is : {}'.format(
            int(df['Birth Year'].max())))
        print('most common year of birth is : {}'.format(
            int(df['Birth Year'].value_counts().index[0]))) 
    else:
        print('current dataset has no Birth Year statistic') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_raw(df,id_start=0,id_range=5):
    if id_start<df.index.size-id_range:
        print(df.iloc[id_start:id_start+id_range])
    elif id_start<df.index.size:
        print(df.iloc[id_start:df.index.size])
    else:
        print('There is no more data show')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        #prompt for raw lines 
        id_start=0
        id_range=5
        while True:
            if id_start>0:
                init_prompt='\n Would you like to see another 5 raw lines from the dataset? Enter y or n \n'
                raw_prompt=input(init_prompt)
            else:
                continue_prompt='\n Would you like to see 5 raw lines from the dataset? Enter y or n \n'
                raw_prompt=input(continue_prompt)
            if raw_prompt.lower()!='y':
                    break
            show_raw(df,id_start)
            id_start+=id_range
            
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
