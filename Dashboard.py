import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

sample = {'JOB_TYPE': {'Full Time': 1, 'Part Time': 0}, 'JOB_LEVEL': {'Intern': 1, 'Junior': 0, 'Senior': 0, 'Executive': 0}, 'JOB_ROLE': {'Software Engineer': 0, 'Quality Assurance': 0, 'Data Scientist': 0, 'Web Developer': 0, 'Frontend Developer': 1, 'Backend Developer': 1, 'Full Stack Developer': 1, 'Researcher': 0, 'Networking Engineer': 0, 'Test Engineer': 1, 'Machine Learning Engineer': 0, 'AI Engineer': 0, 'DevOps Engineer': 0, 'System Administrator': 0, 'Cloud Architect': 0, 'Database Administrator': 0, 'Security Analyst': 0, 'Mobile App Developer': 0, 'Game Developer': 0, 'UI/UX Designer': 0, 'Technical Support': 0, 'Product Manager': 0, 'IT Manager': 0}, 'REQUIRED_DEGREE': {'None': 0, 'Bachelor': 0, 'Graduate': 0, 'MASTER': 0, 'PHD': 0}, 'PROGRAMMING_LANGUAGE': {'Java': 0, 'JavaScript': 1, 'C++': 0, 'Python': 0, 'SQL': 0, 'Ruby': 0, 'PHP': 0, 'C#': 0, 'Swift': 0, 'Go': 0, 'Perl': 0, 'Kotlin': 0, 'TypeScript': 1, 'HTML': 0, 'Dart': 0, 'COBOL': 0, 'Fortran': 0, 'Scala': 0, 'VHDL': 0, 'Lua': 0, 'Elixir': 0, 'MATLAB': 0, 'Haskell': 0, 'Objective-C': 0, 'Groovy': 0, 'Crystal': 0, 'CoffeeScript': 0, 'Erlang': 0, 'Coq': 0, 'Racket': 0, 'F#': 0, 'Perl 6': 0, 'Cool': 0, 'Scheme': 0, 'Prolog': 0, 'Ada': 0}, 'FRAMEWORK': {'React': 0, 'Django': 0, 'Laravel': 0, 'Spring Boot': 0, 'Vue.js': 0, 'Express.js': 0, 'Next.js': 1, 'Nuxt.js': 0, 'ASP.NET Core': 0, 'Ruby on Rails': 0, 'Svelte': 0, 'Angular': 0, 'Nest.js': 1, 'Koa.js': 0, 'Flutter': 0, 'React Native': 0, 'TensorFlow': 0, 'PyTorch': 0, 'PySpark': 0, 'Scikit-learn': 0, 'Keras': 0, 'Flask': 0, 'FastAPI': 0, 'Pyramid': 0, 'Catalyst': 0, 'CakePHP': 0, 'Yii': 0, 'CodeIgniter': 0, 'Symfony': 0, 'Zend Framework': 0, 'Laravel Mix': 0, 'Webpack': 0, 'Parcel': 0, 'Jest': 0, 'Cypress': 0, 'Mocha': 0, 'Enzyme': 0, 'Jasmine': 0, 'JUnit': 0, 'RSpec': 0, 'Capybara': 0, 'Cucumber': 0, 'Selenium': 0, 'Appium': 0, 'Docker': 0, 'Kubernetes': 0, 'Terraform': 0, 'Ansible': 0, 'Chef': 0, 'Puppet': 0}}

st.write("HELLO")

df = pd.DataFrame(sample)
#streamlit run c:\Users\Lenovo\OneDrive\Documents\CS3103\Dashboard.py

# Streamlit app
st.title('Data Visualization')

# Show the data as a DataFrame
st.write('Sample Data:')
st.write(df)

# Create a bar chart for JOB_TYPE
st.bar_chart(df['JOB_TYPE'])

# Create a bar chart for JOB_LEVEL
st.bar_chart(df['JOB_LEVEL'])

# Create a bar chart for PROGRAMMING_LANGUAGE
st.bar_chart(df['PROGRAMMING_LANGUAGE'])

# Create a bar chart for FRAMEWORK
st.bar_chart(df['FRAMEWORK'])

st.title('Data Visualization')

# Show the data as a DataFrame
st.write('Sample Data:')
st.write(df)

# Create a bar chart for JOB_TYPE
st.subheader('JOB_TYPE')
st.bar_chart(df['JOB_TYPE'])

# Create a horizontal bar chart for PROGRAMMING_LANGUAGE
st.subheader('PROGRAMMING_LANGUAGE')
st.bar_chart(df['PROGRAMMING_LANGUAGE'], use_container_width=True)

for item_name, item_data in sample.items():
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