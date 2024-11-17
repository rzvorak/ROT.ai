from pytrends.request import TrendReq
import pandas as pd

def max(word):
    # Initialize Google Trends API with specified language and timezone
    pytrends = TrendReq(hl='en-US', tz=360)

    # Get user input for the keyword and capitalize the first letter
    keyword = word

    # Build payload for the keyword over the past year
    pytrends.build_payload([keyword], timeframe="today 12-m")

    # Get interest over time
    trends_data = pytrends.interest_over_time()

    # Analyze interest over time and calculate the decrease
    if not trends_data.empty:
        # Reset index to turn the date index into a column
        trends_data = trends_data.reset_index()

        # Remove partial data if present
        if 'isPartial' in trends_data.columns:
            trends_data = trends_data[trends_data['isPartial'] == False]

        # Find the date and value of the peak interest
        peak_value = trends_data[keyword].max()
        peak_date = trends_data.loc[trends_data[keyword].idxmax(), 'date']

        # Find the closest data point 30 days after the peak
        date_30_days_later = peak_date + pd.Timedelta(days=30)
        data_after_30_days = trends_data[trends_data['date'] >= date_30_days_later]

        if not data_after_30_days.empty:
            # Get the value closest to 30 days later
            closest_value_30_days = data_after_30_days.iloc[0][keyword]

            # Calculate the decrease as a raw numerical double
            decrease = (closest_value_30_days - peak_value) / peak_value
            
            # Print decrease as a double
            return f"{decrease:.6f}"  # Output the decrease as a double with six decimal places
        else:
            return "0.000000"  # Output zero if no data is available
    else:
        return "0.000000"  # Output zero if no data is available
