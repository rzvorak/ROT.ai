from pytrends.request import TrendReq
import pandas as pd

# Initialize Google Trends API with specified language and timezone
pytrends = TrendReq(hl='en-US', tz=360)

# Get user input for the keyword and capitalize the first letter
keyword = input("Enter a keyword to analyze: ").capitalize()

# Build payload for the keyword over the past year
pytrends.build_payload([keyword], timeframe="today 12-m")

# Get interest over time
trends_data = pytrends.interest_over_time()

# Analyze interest over time and calculate the percentage change after the minimum
if not trends_data.empty:
    # Reset index to turn the date index into a column
    trends_data = trends_data.reset_index()

    # Remove partial data if present
    if 'isPartial' in trends_data.columns:
        trends_data = trends_data[trends_data['isPartial'] == False]

    # Find the date and value of the minimum interest
    min_value = trends_data[keyword].min()
    min_date = trends_data.loc[trends_data[keyword].idxmin(), 'date']

    # Find the closest data point 30 days after the minimum
    date_30_days_later = min_date + pd.Timedelta(days=30)
    data_after_30_days = trends_data[trends_data['date'] >= date_30_days_later]

    if not data_after_30_days.empty:
        # Get the value closest to 30 days later
        closest_value_30_days = data_after_30_days.iloc[0][keyword]

        # Calculate the percentage increase as a decimal
        percentage_increase_decimal = (closest_value_30_days - min_value) / min_value if min_value > 0 else 0

        # Print percentage increase as a decimal
        print(f"{percentage_increase_decimal:.6f}")
    else:
        print("0.000000")  # Output zero if no data is available
else:
    print("0.000000")  # Output zero if no data is available
