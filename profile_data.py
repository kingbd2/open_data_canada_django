import sys
import pandas as pd
import pandas_profiling

csv_data = sys.argv[1]
html = sys.argv[2]

def profile(csv_data):
    df=pd.read_csv(csv_data, parse_dates=True, encoding='UTF-8')
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(outputfile=html)

if __name__ == "__main__":
    profile(csv_data)
