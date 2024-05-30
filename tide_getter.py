import pandas as pd
import numpy as np

months_ref = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep",
              10: "Oct", 11: "Nov", 12: "Dec"}

# retrive vessel arrival data from csv file
# change usecols parameter if required. retrieved data should be in DD:MM:YYYY:"HH:MM" format
file = pd.read_csv("vessel_arrival.csv", header=None, usecols=[2,3,4,5])
vessel_arrival = file.to_numpy()

# retrive 2022 tide data from csv file
# change usecols parameter if required. retrieved data should be in DD:"HH:MM":{"H", "L"} format
file = pd.read_csv("tidal_data/2022_tidal_data.csv", header=None, na_filter=False)
tide_2022 = file.to_numpy()
# print(tide_2022)

# retrive 2023 tide data from csv file
# change usecols parameter if required. retrieved data should be in DD:"HH:MM":{"H", "L"} format
file = pd.read_csv("tidal_data/2023_tidal_data.csv", header=None, na_filter=False)
tide_2023 = file.to_numpy()
# print(tide_2023)

# retrive 2024 tide data from csv file
# change usecols parameter if required. retrieved data should be in DD:"HH:MM":{"H", "L"} format
file = pd.read_csv("tidal_data/2024_tidal_data.csv", header=None, na_filter=False)
tide_2024 = file.to_numpy()
# print(tide_2024)

tide_data = []
# days - 0, months - 1, years - 2, time - 3
for i in range(10):
  day = str(vessel_arrival[i, 0])
  month = months_ref[vessel_arrival[i, 1]]
  year = vessel_arrival[i, 2]
  time = str(vessel_arrival[i, 3])
  if year == 2022:
    month_idx = np.argwhere(tide_2022[:, 0] == month)[0][0]
    truncated = tide_2022[month_idx:]
    
  elif year == 2023:
    month_idx = np.argwhere(tide_2023[:, 0] == month)[0][0]
    truncated = tide_2023[month_idx:]

  elif year == 2024:
    month_idx = np.argwhere(tide_2024[:, 0] == month)[0][0]
    truncated = tide_2024[month_idx:]
  
  day_idx = np.argwhere(truncated == str(day))[0][0]
  prev_time = ""
  while(day_idx < len(truncated) and time > truncated[day_idx, 2] and prev_time < truncated[day_idx, 2]):
    print(day, truncated[day_idx, 2])
    prev_time = truncated[day_idx, 2]
    day_idx += 1

  if (day_idx == len(truncated)):
    tide = truncated[day_idx - 1, 4]
  else:
    tide = "H" if truncated[day_idx, 4] == "L" else "L"
  
  tide_data.append(tide)

df = pd.DataFrame(data=tide_data)
df.to_csv("out.csv", header=False, index=False)