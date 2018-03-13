import sys
import pandas as pd
import pandas_profiling
from get_links import getCSV
from convert_date import convert_date

data_url = sys.argv[1]
html = sys.argv[2]

def profile(data_url):
    df = getCSV(data_url)
    df = convert_date(df)
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(outputfile=html)

    export_csv(df)

if __name__ == "__main__":
    profile(data_url)
