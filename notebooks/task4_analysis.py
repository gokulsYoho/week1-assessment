import pandas as pd

%timeit [x * 2 for x in range(1000)]

df = pd.read_csv("../data/employees.csv")
print(df.groupby("department")["salary"].agg(["count", "mean", "max"]))
