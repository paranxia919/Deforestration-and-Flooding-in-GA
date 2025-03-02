import os
import pandas as pd
import glob

def load_county():
    
    pattern = os.path.join(".", "*.csv")
    csv_files = glob.glob(pattern)

    county_data ={}

    for file in csv_files:
        name = os.path.splitext(os.path.basename(file))[0]
        df = pd.read_csv(file)
        county_data[name] = df

    return county_data

def calculate_rate(county_data):
   
   rate_change_dict = {}
   

   for county, df in county_data.items():
    
    df_data = df.iloc[1:]

    types = df_data.iloc[:,0].astype(str).str.strip().str.lower()
    y1985 = pd.to_numeric(df_data.iloc[:,1],errors = 'raise')
    y2023 = pd.to_numeric(df_data.iloc[:,-2],errors = 'raise')
    
    rate_change = (y2023-y1985)/y1985.replace(0,pd.NA)

    # print(f"County: {county}")
    # print("y1985 head:", y1985.head())
    # print("y2023 head:", y2023.head())
    # print("Rate change head:", rate_change.head())
    # print("-" * 40)
    
    df['rate_change'] = rate_change
    
    rate_series = pd.Series(rate_change.values, index=types)
    rate_change_dict[county]=rate_series

   rate_change_NLCD = pd.DataFrame(rate_change_dict) 
   rate_change_NLCD.to_csv(os.path.join(".", "rate_change_NLCD.csv"))

   return rate_change_NLCD

if __name__ == "__main__":
   
   county_data = load_county()

   rate_change_NLCD = calculate_rate(county_data)

   print("processed")


