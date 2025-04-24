import streamlit as st
import pandas as pd
import random

# Page configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("🎓 Student CSV File Generator")

# List of student names
names = [
    "Kulsoom", "Farrukh", "Amna", "Sufyan", "Urwa", "Rameen", "Jveriya",
    "Babar", "Annie", "Dua", "Kiran", "Imran", "Kashif", "Rahim", "Rahman",
    "Fatima", "Zainab"
]

# Generate student data
students = []
for i in range(1, 18):  # 17 students
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

# Convert to DataFrame
df = pd.DataFrame(students)

# Display data
st.subheader("📊 Generated Students Data")
st.dataframe(df, use_container_width=True)

# Download CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download CSV File",
    data=csv,
    file_name='students.csv',
    mime='text/csv'
)

# Success message
st.success("✅ Students Record Generated Successfully!")
