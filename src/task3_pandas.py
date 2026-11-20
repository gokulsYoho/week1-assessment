import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/employees.csv")
print(df.info())
print(df.describe())
print("Row 0:\n", df.loc)
print("First 2 rows:\n", df.iloc[:2])
print("IT Dept:\n", df[df["department"] == "IT"])

dept_text = """department,head,budget
Sales,Vikram,500000
HR,Lakshmi,300000
IT,Ramesh,900000
Finance,Sita,600000
Marketing,Kiran,400000"""

with open("data/departments.csv", "w") as f:
    f.write(dept_text)

dirty_df = df.copy()
dirty_df.loc[1, "salary"] = np.nan
dirty_df.loc[5, "salary"] = np.nan
dirty_df = pd.concat([dirty_df, dirty_df.iloc[0:1]], ignore_index=True)

dirty_df = dirty_df.drop_duplicates().copy()
med_sal = dirty_df["salary"].median()
dirty_df["salary"] = dirty_df["salary"].fillna(med_sal).astype(int)

stats = df.groupby("department").agg(
    headcount=("id", "count"),
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max")
).round(2)

ordered = stats.reindex(["Sales", "HR", "IT", "Finance"])
hc_str = " | ".join([f"{k} {v}" for k, v in ordered["headcount"].items()])
print(f"Headcount: {hc_str}")

depts = pd.read_csv("data/departments.csv")
inner_m = pd.merge(df, depts, on="department", how="inner")
left_m = pd.merge(df, depts, on="department", how="left")
outer_m = pd.merge(df, depts, on="department", how="outer")

no_emp = outer_m[outer_m["id"].isna()]["department"].tolist()
print(f"Outer join: {no_emp}")

plt.figure(figsize=(6, 4))
plt.bar(ordered.index, ordered["avg_salary"], color="steelblue", label="Avg Salary")
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/1_bar_chart.png")
plt.close()
print("Bar chart insight: Finance has the highest average salary.")

plt.figure(figsize=(6, 4))
plt.hist(df["salary"], bins=4, color="teal", edgecolor="black", label="Employees")
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Employee Count")
plt.legend()
plt.tight_layout()
plt.savefig("reports/2_histogram.png")
plt.close()
print("Histogram insight: Most employees earn between 45000 and 75000.")

plt.figure(figsize=(6, 4))
for d in df["department"].unique():
    sub = df[df["department"] == d]
    plt.scatter(sub["id"], sub["salary"], label=d, s=60)
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig("reports/3_scatter_plot.png")
plt.close()
print("Scatter plot insight: IT employees sit in the higher salary range.")

sorted_df = df.sort_values("salary")
plt.figure(figsize=(6, 4))
plt.plot(sorted_df["name"], sorted_df["salary"], marker="o", color="orange", label="Salary")
plt.title("Employee Salaries (Low to High)")
plt.xlabel("Employee Name")
plt.ylabel("Salary (INR)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("reports/4_line_chart.png")
plt.close()
print("Line chart insight: Salaries rise steadily from 30000 to 90000.")