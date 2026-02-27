import sys
import pandas as pd

print("Hello, World!",sys.argv)

month = int(sys.argv[1])
print(f"The month is: {month}")

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_day_{month}.parquet") 