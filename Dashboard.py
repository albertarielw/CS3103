import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

 
# Opening JSON file analysis.JSON which contains the aggregate info from key word analysis of html page from web crawling
f = open(r'./analysis.json')
 
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

# For the bar chart categories which have lot of values, we take only the top 9 and collectively group the rest as 'others'
for key in bar_chart_category:
  temp = dict(sorted(bar_chart_category[key].items(), key=lambda x:x[1], reverse=True)[9:])
  bar_chart_category[key] = dict(sorted(bar_chart_category[key].items(), key=lambda x:x[1], reverse=True)[:9])
  bar_chart_category[key].update({"others":sum(list(temp.values()))})


# Change the values into percentage for ease of looking for both bar and pie categories
bar_percentage = {}
for key in bar_chart_category:
  total = sum(bar_chart_category[key].values())
  bar_percentage[key] = {k: v / total * 100 for k, v in bar_chart_category[key].items()}


pie_percentage = {}
for key in pie_chart_category:
  total = sum(pie_chart_category[key].values())
  pie_percentage[key] = {k: v / total * 100 for k, v in pie_chart_category[key].items()}

# Visualizing a pie chart for each category in bar_category
for item_name, item_data in pie_percentage.items():
    # Extract labels and sizes for the pie chart
    filtered_data = {label: value for label, value in item_data.items() if value > 0}
    labels = list(filtered_data.keys())
    sizes = list(filtered_data.values())

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart in Streamlit
    st.subheader(item_name)
    st.pyplot(fig)

# Create a DataFrame for the data
df = pd.DataFrame(bar_percentage)

# Display the bar chart in streamlit
for item in bar_percentage:
  st.subheader(item)
  st.bar_chart(df[item])
