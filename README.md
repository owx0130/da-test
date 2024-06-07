# da-test

## Get tidal level based on vessel arrival time

Tidal data obtained from [here](http://www.weather.gov.sg/weather-astronomical-and-tidal-information-monthly-data/).

2024 tidal data only taken up till Mar 24.

To use, drag and drop the `vessel_arrival` dataset into the root directory. Information on the format of the csv file is written in `tide_getter.py`.

`out.csv` contains the tide level at the vessel's time of arrival.

## Use KNN (with Damerau-Levenshtein distance) for feature extraction

Use KNN on the dataset with free text input to perform feature extraction.

To use, create the training and testing text files, `TRAIN.txt` and `TEST.txt` and drop them into the root directory.

## Use K-Medoids clustering to identify trends

After getting the tides for the `vessel_arrival` dataset, it is then possible to do clustering with K-Medoids to identify trends within the dataset.