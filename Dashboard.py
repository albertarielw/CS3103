import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

 
# Opening JSON file analysis.JSON which contains the aggregate info from key word analysis of html page from web crawling
f = None
try :
  f = open(r'./analysis.json')
except Exception:
  print("analysis.json file is not found. This is because your webcrawler process had not been run yet. Data will be loaded from sample.json.")
  f = open(r'./sample.json')


 
# returns JSON object as a dictionary
data = json.load(f)

# Closing file
f.close()

# Create a new dictionary to separate visualization for bar chart and pie chart
bar_chart_category = {}
pie_chart_category = {}

# Category for pie chart and bar chart respectively

pie_category = ("JOB_TYPE", "JOB_LEVEL", "REQUIRED_DEGREE", "JOB_MODE")
bar_category = ("JOB_ROLE", "COMMUNICATION", "PROGRAMMING_LANGUAGE", "FRAMEWORK")

# Assign the related values in the data to a new dictionary specifically for pie chart
for key in pie_category:
  pie_chart_category.update({key: data[key]})

# Do similarly for bar chart 
for key in bar_category:
  bar_chart_category.update({key: data[key]})

for key in bar_chart_category:
  bar_chart_category[key] = dict(sorted(bar_chart_category[key].items(), key=lambda x:x[1], reverse=True)[:9])

#referenced from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py
def func(pct, allvals):
  absolute = int(np.round(pct/100.*np.sum(allvals)))
  return f"{pct:.1f}%\n({absolute:d})"

# Visualizing a pie chart for each category in bar_category
for item_name, item_data in pie_chart_category.items():
  # Extract labels and sizes for the pie chart
  filtered_data = {label: value for label, value in item_data.items() if value > 0}
  labels = list(filtered_data.keys())
  sizes = list(filtered_data.values())

  # Create a pie chart
  fig, ax = plt.subplots()
  ax.pie(sizes, labels=labels, autopct=lambda pct: func(pct,sizes), shadow=True, startangle=90)
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

  # Display the pie chart in Streamlit
  st.subheader(item_name)
  st.pyplot(fig)

# Create a DataFrame for the data
df = pd.DataFrame(bar_chart_category)

# Display the bar chart in streamlit
for item in bar_chart_category:
  st.subheader(item)
  st.bar_chart(df[item])
