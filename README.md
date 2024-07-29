# da-test

## Get tidal level based on vessel arrival time

Tidal data obtained from [here](http://www.weather.gov.sg/weather-astronomical-and-tidal-information-monthly-data/).

2024 tidal data only taken up till Mar 24.

To use, drag and drop the `vessel_arrival` dataset into the root directory. Information on the format of the csv file is written in `tide_getter.py`.

`out.csv` contains the tide level at the vessel's time of arrival.

## Use KNN (with Damerau-Levenshtein distance) for feature extraction

Use KNN on the `cargo_description` dataset with free text input to perform feature extraction.

To use, create the training and testing text files, `TRAIN.txt` and `TEST.txt` and drop them into the root directory. Format of data is written in the comments under the KNN Classifier section.

To use K-Fold Cross Validation, pass the entire dataset into the `DATA.txt` file, then run the code in the section.

See sample data in `SAMPLE_CARGO.txt` for a sample of what the text files should look like.