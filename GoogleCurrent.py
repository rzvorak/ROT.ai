from pytrends.request import TrendReq
import pandas as pd

def cur(word):
    if not word.strip():
        return "0.000000"  # Return zero for empty or invalid word

    try:
        # Initialize Google Trends API with specified language and timezone
        pytrends = TrendReq(hl='en-US', tz=360)

        # Build payload for the keyword with a very short timeframe (e.g., last 24 hours)
        pytrends.build_payload([word], timeframe="now 1-d")  # 'now 1-d' for 24 hours

        # Get interest over time
        trends_data = pytrends.interest_over_time()

        # Check if the trends data is not empty
        if not trends_data.empty:
            # Reset index to turn the date index into a column
            trends_data = trends_data.reset_index()

            # Remove partial data if present
            if 'isPartial' in trends_data.columns:
                trends_data = trends_data[trends_data['isPartial'] == False]

            # Check if data remains after removing partial rows
            if not trends_data.empty:
                # Get the most recent data point
                most_recent_point = trends_data.iloc[-1][word]
                return f"{most_recent_point:.6f}"  # Output the most recent value as a double with six decimal places
            else:
                return "0.000000"  # Output zero if no valid data is available
        else:
            return "0.000000"  # Output zero if no data is available

    except Exception as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return "0.000000"
