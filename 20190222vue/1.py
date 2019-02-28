import pandas as pd
csv_data=pd.read_csv("data.csv")
json_data=csv_data.to_dict()