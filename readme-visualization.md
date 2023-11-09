# How Does the Visualization/Dashboard Work?

The visualization process is implemented such as to visualize the data achieved from analysis of the html pages acquired through web crawling. It reads through the analysis.json file which contain aggregate data as the result of keyword analysis and it produces bar and pie charts utilizing the streamlit and matplotlib library. To achieve the purpose of ease of understanding, categories with less than 9 values will be visualized in the form of pie charts. Categories with 9 or more values will be visualized by bar charts, only taking the 9 highest values and the rest categorically grouped as others. This visualization process is done to let the reader have a better understanding of the data and to help improve the clarity of the report.  

To run the dashboard.py, you might need to configure the path of analysis.json and/or sample.json accordingly.

The following is the official documentation to get started on streamlit: https://docs.streamlit.io/library/get-started

To run Dashboard.py, please follow the instructions here or online and you might need to install the necessary libraries.