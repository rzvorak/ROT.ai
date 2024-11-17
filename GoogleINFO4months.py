from pytrends.request import TrendReq
import pandas as pd

def fourMonths(word):
    try:
        # Initialize Google Trends API with specified language and timezone
        pytrends = TrendReq(hl='en-US', tz=360)

        # Get user input for the keyword
        keyword = word

        # Build payload for the keyword over the past year
        pytrends.build_payload([keyword], timeframe="today 12-m")

        # Get interest over time
        trends_data = pytrends.interest_over_time()

        # Calculate the percentage change from 4 months ago to the present
        if not trends_data.empty:
            # Reset index to turn the date index into a column
            trends_data = trends_data.reset_index()

            # Remove partial data if present
            if 'isPartial' in trends_data.columns:
                trends_data = trends_data[trends_data['isPartial'] == False]

            # Get the most recent date and 4 months ago
            current_date = trends_data['date'].max()
            date_4_months_ago = current_date - pd.DateOffset(months=4)

            # Get the most recent value
            present_value = trends_data.iloc[-1][keyword]

            # Get the value from 4 months ago (last available before the date)
            past_data = trends_data[trends_data['date'] <= date_4_months_ago]
            if not past_data.empty:
                past_value = past_data.iloc[-1][keyword]

                # Calculate the percentage change
                percentage_change_decimal = (present_value - past_value) / past_value if past_value > 0 else 0.0

                return float(percentage_change_decimal)
            else:
                return 0.0  # Return zero if no data is available
        else:
            return 0.0  # Return zero if no data is available

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0.0  # Return zero in case of any error
