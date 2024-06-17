#!/usr/bin/env python
# coding: utf-8

# In[3]:


# conda list | findstr scikit-learn


# In[4]:


# get_ipython().system('python -V')


# In[42]:


import pickle
import pandas as pd
import pyarrow
import os


# In[9]:



with open('model.pkl', 'rb') as f_in:
    dv, lr = pickle.load(f_in)


# In[10]:


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[12]:


# Load the data
df = pd.read_parquet('yellow_tripdata_2023-03 (1).parquet')


# In[14]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = lr.predict(X_val)


# In[15]:


y_pred


# In[16]:


# Calculate the standard deviation of the predicted durations
std_pred = y_pred.std()


# In[17]:


std_pred


# In[20]:


# Assuming you have the year and month variables defined
year = 2023
month = 3


# In[30]:


df.head()


# In[21]:


df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')


# In[25]:


# Example preprocessing (to be adjusted based on the actual data and initial notebook)
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df['duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60


# In[26]:


# Filter out any potential outliers or invalid data as done in the initial notebook
df = df[(df['duration'] >= 1) & (df['duration'] <= 60)]


# In[31]:


# Select the relevant categorical columns for transformation
categorical = ['PULocationID', 'DOLocationID']


# In[32]:


# Convert the categorical columns to a list of dictionaries
dicts = df[categorical].fillna(-1).astype(int).to_dict(orient='records')


# In[33]:


# Transform the data
X_val = dv.transform(dicts)


# In[35]:


# Make predictions
y_pred = lr.predict(X_val)


# In[36]:


# Create a results DataFrame
df_result = pd.DataFrame({
    'ride_id': df['ride_id'],
    'predicted_duration': y_pred
})


# In[37]:


# Define the output file name
output_file = 'predictions.parquet'


# In[38]:


df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# In[43]:


# Check the size of the output file
output_file_size = os.path.getsize(output_file)

print(f'Size of the output file: {output_file_size} bytes')


# In[ ]:




