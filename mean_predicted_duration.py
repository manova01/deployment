import pandas as pd
import argparse

def calculate_mean_predicted_duration(year, month):
    # Load Parquet file
    df = pd.read_parquet('yellow_tripdata.parquet')
    
    # Print columns to debug
    print("Columns in the DataFrame:", df.columns)
    
    # Ensure the date columns are datetime type
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    
    # Calculate trip duration in minutes
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60.0
    
    # Filter data for the given year and month
    filtered_df = df[(df['tpep_pickup_datetime'].dt.year == year) & (df['tpep_pickup_datetime'].dt.month == month)]
    
    # Debug: print the number of records found for the month
    record_count = len(filtered_df)
    print(f"Number of records for {year}-{month:02d}: {record_count}")
    
    if record_count == 0:
        return None
    
    # Calculate mean predicted duration
    mean_predicted_duration = filtered_df['trip_duration'].mean()
    
    return mean_predicted_duration

def main():
    parser = argparse.ArgumentParser(description="Calculate the mean predicted duration for a given year and month.")
    parser.add_argument('year', type=int, help="The year for which to calculate the mean predicted duration")
    parser.add_argument('month', type=int, help="The month for which to calculate the mean predicted duration")
    
    args = parser.parse_args()
    
    year = args.year
    month = args.month
    
    mean_duration = calculate_mean_predicted_duration(year, month)
    
    if mean_duration is not None:
        print(f"The mean predicted duration for {year}-{month:02d} is {mean_duration:.2f} minutes")
    else:
        print(f"No records found for {year}-{month:02d}")

if __name__ == "__main__":
    main()
