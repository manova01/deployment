FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY mean_predicted_duration.py .

# Copy the Parquet file into the container
COPY yellow_tripdata_2023-05.parquet yellow_tripdata.parquet

# Install any necessary dependencies (if not already installed in the base image)
RUN pip install pandas pyarrow

# Define the entry point
CMD ["python", "mean_predicted_duration.py", "2023", "5"]
