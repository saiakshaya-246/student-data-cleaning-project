import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# create folder for charts
os.makedirs("charts", exist_ok=True)

# load dataset
df = pd.read_csv("students.csv")

# basic info
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# save cleaned file
df.drop_duplicates(inplace=True)
df.to_csv("cleaned_students.csv", index=False)

# Chart 1
df["Department"].value_counts().plot(kind="bar")
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/department.png")
plt.close()

# Chart 2
sns.histplot(df["GPA"], bins=10)
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.tight_layout()
plt.savefig("charts/gpa_distribution.png")
plt.close()

# Chart 3
plt.scatter(df["Age"], df["GPA"])
plt.title("Age vs GPA")
plt.xlabel("Age")
plt.ylabel("GPA")
plt.tight_layout()
plt.savefig("charts/age_vs_gpa.png")
plt.close()

# Chart 4
sns.boxplot(x="Department", y="GPA", data=df)
plt.title("Department-wise GPA")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("charts/department_gpa.png")
plt.close()

print("\nProject Completed Successfully")