# da-test

## Get tidal level based on vessel arrival time

Tidal data obtained from [here](http://www.weather.gov.sg/weather-astronomical-and-tidal-information-monthly-data/).

2024 tidal data only taken up till Mar 24.

To use, drag and drop the `vessel_arrival` dataset into the root directory. Information on the format of the csv file is written in `tide_getter.py`. A sample dataset for reference is given in this repository.

`out.csv` contains the tide level at the vessel's time of arrival.