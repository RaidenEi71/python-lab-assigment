import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("student.csv")

# Fill missing values with subject average
df.fillna(df.mean(numeric_only=True), inplace=True)

# Subjects list
subjects = ['Math', 'Science', 'English', 'History', 'Computer']

# Calculate Percentage
df['Percentage'] = df[subjects].mean(axis=1)

# Calculate GPA (out of 10)
df['GPA'] = df['Percentage'] / 10

# Identify at-risk students (<40%)
at_risk = df[df['Percentage'] < 40]

print("\n=== At-Risk Students (Below 40%) ===")
print(at_risk[['Name', 'Department', 'Percentage']])

# ----------- PLOTS -----------

# Histogram: Grade Distribution
plt.figure()
plt.hist(df['Percentage'], bins=10)
plt.title("Grade Distribution")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")

# Bar Chart: Department-wise Average
dept_avg = df.groupby('Department')['Percentage'].mean()

plt.figure()
dept_avg.plot(kind='bar')
plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Percentage")

plt.tight_layout()
plt.show()