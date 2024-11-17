from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd

# Initialize Google Trends API with specified language and timezone
pytrends = TrendReq(hl='en-US', tz=360)

# Get user input for the keyword and capitalize the first letter
keyword = input("Enter a keyword to analyze: ").capitalize()

# Build payload for the keyword over the past year
pytrends.build_payload([keyword], timeframe="today 12-m")

# Get interest over time
trends_data = pytrends.interest_over_time()

# Analyze interest over time and find the peak
if not trends_data.empty:
    # Reset index to turn the date index into a column
    trends_data = trends_data.reset_index()

    # Remove partial data if present
    if 'isPartial' in trends_data.columns:
        trends_data = trends_data[trends_data['isPartial'] == False]

    # Find the date and value of the peak interest
    peak_value = trends_data[keyword].max()
    peak_date = trends_data.loc[trends_data[keyword].idxmax(), 'date']

    print(f"The peak search interest for '{keyword}' was {peak_value} on {peak_date.date()}.")

    # Find the closest data point 30 days after the peak
    date_30_days_later = peak_date + pd.Timedelta(days=30)
    data_after_30_days = trends_data[trends_data['date'] >= date_30_days_later]

    if not data_after_30_days.empty:
        # Get the value closest to 30 days later
        closest_date_30_days = data_after_30_days.iloc[0]['date']
        closest_value_30_days = data_after_30_days.iloc[0][keyword]

        # Calculate the numerical and percentage fall-off
        numerical_fall_off = peak_value - closest_value_30_days
        percentage_fall_off = (numerical_fall_off / peak_value) * 100

        print(f"Search interest 30 days later (on {closest_date_30_days.date()}) was {closest_value_30_days}.")
        print(f"The search interest has fallen off by {numerical_fall_off} points ({percentage_fall_off:.2f}%) in 30 days.")
    else:
        print("No data available for the period 30 days after the peak.")

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(trends_data['date'], trends_data[keyword], marker='o', label=keyword)
    plt.axvline(x=peak_date, color='red', linestyle='--', label='Peak')
    if not data_after_30_days.empty:
        plt.axvline(x=closest_date_30_days, color='blue', linestyle='--', label='30 Days Later')
    plt.title(f"Interest Over Time for '{keyword}' (Last 12 Months)")
    plt.xlabel("Date")
    plt.ylabel("Search Interest (Normalized 1 to 100)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("No data available for the specified keyword.")
