#!/usr/bin/env python
# coding: utf-8

# # Case Study

# Introduction: 
# 
# Wind turbines are essential to maintaining our population's growing energy consumption and noble desire for cleaner & renewable energy resources. While turbines present environmentally responsible alternatives to other energy sources, they do come with downsides such as impacts on nearby populations from their output noise pollution. This study aims to test the noise level impact of a theoretical wind turbine placed on Horsebarn Hill, UConn campus using a monte carlo simulation.  

# Methodologies 
# 
# Monte Carlo simulations will be used due to its large number of iterations to better estimate the variability of wind energy output. Important variables to consider are wind speed and turbine sound pressure output. Historical wind speed values on UConn campus were found using data recorded by the UConn Connecticut State Climate Center [1].  Using this data, we can extract the recorded windspeed every day since 1962 and calculate the mean, standard deviation, min, and max wind speed using python code (shown in appendix figure 1). Using the calculated values for windspeed, the optimal likely wind turbine was selected and the sound pressure for that turbine was found. Using the known sound pressure at a recorded distance, the sound pressure at other distances can be found using equation 1 below, where 𝑝 is the sound pressure, 𝑝1 is the sound pressure at a distance of 1, and 
# 𝑑 is the distance. 
# 
# (1)          𝑝 = 𝑝1−20log(𝑑)			
# 
# Using this formula in python, the sound pressure for distances along the hill’s pedestrian path was calculated. Finally, utilizing Monte Carlo simulation in python 100 UConn students were simulated sitting randomly on the hill from 1-200 meters from the turbine for a random amount of time between 10-90 minutes, 1000 times. 
# 
# Knowing the sound pressure over time values for hearing damage [2], we can determine how many students are at risk for hearing loss and the level of their risk after they sit on the hill.  

# References:
# 
# [1] https://cscc.nre.uconn.edu/climate-data/ 
# 
# [2] https://www.mdhearingaid.com/blog/decibel-chart/ 
# 
# [3] https://cdn.prod.website-files.com/64c38ca9b1a2e59bd5b7d64a/656a178801f71b16b0045a38_ENERCON%20E-82%20EP2%20E4%20en.pdf
# 
# 

# #### WIND SPEED CALCULATION

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

url = "https://raw.githubusercontent.com/ColeScottUconn/data-driven-decisions/main/STORRS_WindSpeed_Post1962_Converted.csv"

response = requests.get(url)
open('STORRS_WindSpeed_Post1962_Converted.csv', 'wb').write(response.content)

file_path = 'STORRS_WindSpeed_Post1962_Converted.csv'
wind_speed_data = pd.read_csv(file_path)

wind_speed_statistics = wind_speed_data['WindSpeed_mps'].describe()

plt.figure(figsize=(10, 6))
plt.hist(wind_speed_data['WindSpeed_mps'], bins=50, edgecolor='black')
plt.title('Distribution of Wind Speed (Post-1962, Converted to m/s)')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print(wind_speed_statistics)



# #### TURBINE DECIBEL CALCULATION

# In[25]:


import numpy as np
import matplotlib.pyplot as plt

# Define the sound power level range in dB(A) from reference 3
L_w_min = 87.4
L_w_max = 104.0

# Distances in Meters
distances = np.array([1, 5, 10, 25, 50, 100, 150, 200, 250, 300])  # starting at 1 meter instead of 0 to avoid log(0)

# Calculate the sound pressure levels at each distance
L_p_min = L_w_min - 20 * np.log10(distances)
L_p_max = L_w_max - 20 * np.log10(distances)

plt.figure(figsize=(10, 6))
plt.plot(distances, L_p_min, label=f'Sound Pressure Level (Min {L_w_min} dB(A))')
plt.plot(distances, L_p_max, label=f'Sound Pressure Level (Max {L_w_max} dB(A))')
plt.xlabel('Distance from Source (meters)')
plt.ylabel('Sound Pressure Level (dB(A))')
plt.title('Sound Pressure Level vs. Distance from Wind Turbine')
plt.legend()
plt.grid(True)
plt.show()

for d, l_min, l_max in zip(distances, L_p_min, L_p_max):
    print(f"Distance: {d} m, Sound Pressure Level (Min): {l_min:.2f} dB(A), Sound Pressure Level (Max): {l_max:.2f} dB(A)")


# In[ ]:




