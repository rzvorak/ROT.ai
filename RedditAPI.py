import matplotlib.pyplot as plt
import datetime
import pandas as pd
import praw
import time
import os

# Path to your ChromeDriver (change if needed)
driver_path = '/Users/alexlu/Desktop/chromedriver-mac-x64/chromedriver'

class Useless:
    def testRedditAPI(self):


        # Initialize reddit api
        reddit = praw.Reddit(client_id='H5092zuImQyMCKARxvK8QQ',
                     client_secret='HSMR_yOGA2vGc7yLv-oPt4xV4Ibv_A',
                     user_agent='Mint_Swirls')
        # Set the slang word you want to track
        slang_word = input("Please enter the slang word you want to track: ")
       
        # Initialize a dictionary to track mentions by week (keyed by 'year-week')
        mentions_per_week = {}

        # Set the time range for posts (e.g., past year)
        end_date = datetime.datetime.utcnow()
        start_date = end_date - datetime.timedelta(days=365)  # Look back one year

        # Search for the slang word in posts across all subreddits (adjust the limit as needed)
        for submission in reddit.subreddit('all').search(slang_word, sort='controversial', time_filter='year', limit=500):
            # Get the submission's date and convert to datetime
            submission_date = datetime.datetime.utcfromtimestamp(submission.created_utc)

            # Only count posts within the last year
            if start_date <= submission_date <= end_date:
                # Extract the year and week number from the submission's date
                year, week, _ = submission_date.isocalendar()

                # Create a key for the week (e.g., "2023-W01", "2023-W02")
                week_key = f"{year}-W{week:02d}"

                # Increment the count for the corresponding week
                if week_key not in mentions_per_week:
                    mentions_per_week[week_key] = 0
                mentions_per_week[week_key] += 1

        # Now, aggregate mentions by month
        mentions_per_month = {}

        # Loop over each week and sum the mentions into the appropriate month
        for week_key, count in mentions_per_week.items():
            # Extract year and week from the key
            year, week = week_key.split('-')
            year = int(year)
            week = int(week[1:])  # Remove the 'W' character

            # Get the first day of the week to determine the month
            first_day_of_week = datetime.datetime(year, 1, 1) + datetime.timedelta(weeks=week - 1)
            month = first_day_of_week.strftime('%Y-%m')  # Format as 'YYYY-MM'

            # Aggregate weekly mentions into the respective month
            if month not in mentions_per_month:
                mentions_per_month[month] = 0
            mentions_per_month[month] += count

        # Convert the mentions per month into a sorted DataFrame
        df = pd.DataFrame(list(mentions_per_month.items()), columns=['Month', 'Mentions'])
        df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')  # Convert 'YYYY-MM' to datetime format
        df = df.sort_values(by='Month')

        # Plot the trend of mentions per month
        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df['Mentions'], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

        plt.xlabel('Month')
        plt.ylabel('Number of Mentions')
        plt.title(f"Trend of the word '{slang_word}' (Mentions per Month, Aggregated from Weekly Data)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Show the plot
        plt.show()
        
# Run this shit
browser = Useless()
browser.testRedditAPI()


