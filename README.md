# Taxi Trip Duration Prediction
This project predicts the duration of taxi trips in New York City using a pre-trained machine learning model. The data is processed from Parquet files and predictions are saved to a Parquet file.

## Table of Contents
Project Overview
Setup Instructions
Usage
Files
Contributing
License
Project Overview
The main objective of this project is to predict the duration of taxi trips using a machine learning model. The project processes trip data, makes predictions using a pre-trained model, and saves the results for further analysis.

## Setup Instructions
Prerequisites
Docker
Python 3.10 or later
Pip
Installation
Clone the repository:

###  sh
Copy code
git clone https://github.com/yourusername/taxi-trip-duration-prediction.git
cd taxi-trip-duration-prediction
Build the Docker image:

### sh

docker build -t taxi-trip-duration-prediction .
Run the Docker container:

###  sh

docker run taxi-trip-duration-prediction
Local Setup (without Docker)
Install dependencies:

### sh

pip install pandas pyarrow
Run the script:

###  sh

python mean_predicted_duration.py 2023 5
Usage
Command-Line Arguments
The main script mean_predicted_duration.py requires two arguments: year and month.

### sh
 
python mean_predicted_duration.py <year> <month>
For example, to calculate the mean predicted duration for May 2023:

### sh

python mean_predicted_duration.py 2023 5
Predicting Trip Duration
Prepare your data:

### Ensure you have the Parquet file with taxi trip data, e.g., yellow_tripdata_2023-05.parquet.

Run the prediction script:

### sh

python predict_duration.py
This will load the data, make predictions, and save the results to predictions.parquet.

### Example
An example of how to run the prediction script:

#### sh

### python predict_duration.py
This will load the data from yellow_tripdata_2023-03 (1).parquet, process it, make predictions, and save the results to predictions.parquet.###

### Files
Dockerfile: Configuration for Docker.
mean_predicted_duration.py: Script to calculate the mean predicted duration for a given month.
predict_duration.py: Script to predict trip durations using a pre-trained model.
model.pkl: Pre-trained machine learning model.
yellow_tripdata_2023-05.parquet: Sample data file (not included in the repository).
Contributing
Contributions are welcome! Please create an issue or submit a pull request for any feature requests or bug fixes.



