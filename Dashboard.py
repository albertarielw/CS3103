import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {'JOB_TYPE': {'Full Time': 51, 'Part Time': 88}, 'JOB_LEVEL': {'Intern': 9, 'Junior': 41, 'Senior': 99, 'Executive': 69}, 'REQUIRED_DEGREE': {'None': 40, 'Bachelor': 4, 'Graduate': 24, 'MASTER': 64, 'PHD': 31}, 'JOB_MODE': {'On-Site': 49, 'Remote': 27, 'Hybrid': 37}, 'JOB_ROLE': {'Software Engineer': 89, 'Quality Assurance': 56, 'Data Scientist': 17, 'Web Developer': 13, 'Frontend Developer': 33, 'Backend Developer': 24, 'Full Stack Developer': 29, 'Researcher': 79, 'Networking Engineer': 41, 'Test Engineer': 80, 'Machine Learning Engineer': 86, 'AI Engineer': 84, 'DevOps Engineer': 93, 'System Administrator': 11, 'Cloud Architect': 78, 'Database Administrator': 93, 'Security Analyst': 48, 'Mobile App Developer': 75, 'Game Developer': 71, 'UI/UX Designer': 16, 'Technical Support': 64, 'Product Manager': 66, 'IT Manager': 76}, 'COMMUNICATION': {'Collaboration': 7, 'Presentation': 86, 'Competitive': 63, 'Teamwork': 77, 'Leadership': 31, 'Creativity': 75, 'Conflict Resolution': 13, 'Ambitious': 67, 'Critical Thinking': 85, 'Time Management': 69, 'Problem Solving': 87, 'Enthusiasm': 29, 'Feedback Receptivity': 7, 'Attentiveness': 0}, 'PROGRAMMING_LANGUAGE': {'Java': 38, 'JavaScript': 14, 'C++': 49, 'Python': 3, 'SQL': 70, 'Ruby': 2, 'PHP': 92, 'C#': 61, 'Swift': 61, 'Go': 94, 'Perl': 23, 'Kotlin': 70, 'TypeScript': 5, 'HTML': 35, 'Dart': 46, 'COBOL': 94, 'Fortran': 95, 'Scala': 76, 'VHDL': 86, 'Lua': 3, 'Elixir': 57, 'MATLAB': 59, 'Haskell': 21, 'Objective-C': 37, 'Groovy': 95, 'Crystal': 69, 'CoffeeScript': 72, 'Erlang': 54, 'Coq': 0, 'Racket': 55, 'F#': 18, 'Perl 6': 3, 'Cool': 51, 'Scheme': 31, 'Prolog': 58, 'Ada': 100}, 'FRAMEWORK': {'React': 100, 'Django': 60, 'Laravel': 79, 'Spring Boot': 4, 'Vue.js': 13, 'Express.js': 96, 'Next.js': 21, 'Nuxt.js': 78, 'ASP.NET Core': 32, 'Ruby on Rails': 55, 'Svelte': 8, 'Angular': 25, 'Nest.js': 77, 'Koa.js': 61, 'Flutter': 82, 'React Native': 25, 'TensorFlow': 83, 'PyTorch': 26, 'PySpark': 5, 'Scikit-learn': 86, 'Keras': 12, 'Flask': 13, 'FastAPI': 12, 'Pyramid': 34, 'Catalyst': 97, 'CakePHP': 71, 'Yii': 50, 'CodeIgniter': 38, 'Symfony': 43, 'Zend Framework': 63, 'Laravel Mix': 10, 'Webpack': 38, 'Parcel': 77, 'Jest': 98, 'Cypress': 96, 'Mocha': 95, 'Enzyme': 41, 'Jasmine': 98, 'JUnit': 22, 'RSpec': 15, 'Capybara': 72, 'Cucumber': 41, 'Selenium': 5, 'Appium': 96, 'Docker': 10, 'Kubernetes': 36, 'Terraform': 3, 'Ansible': 34, 'Chef': 35, 'Puppet': 1}}

bar_chart_category = {}
pie_chart_category = {}

pie_chart_category.update({"JOB_TYPE": data["JOB_TYPE"]})
pie_chart_category.update({"JOB_LEVEL": data["JOB_LEVEL"]})
pie_chart_category.update({"REQUIRED_DEGREE": data["REQUIRED_DEGREE"]})
pie_chart_category.update({"JOB_MODE": data["JOB_MODE"]})


bar_chart_category.update({"JOB_ROLE": data["JOB_ROLE"]})
bar_chart_category.update({"COMMUNICATION": data["COMMUNICATION"]})
bar_chart_category.update({"PROGRAMMING_LANGUAGE": data["PROGRAMMING_LANGUAGE"]})
bar_chart_category.update({"FRAMEWORK": data["FRAMEWORK"]})

for key in bar_chart_category:
  temp = dict(sorted(bar_chart_category[key].items(), key=lambda x:x[1], reverse=True)[9:])
  bar_chart_category[key] = dict(sorted(bar_chart_category[key].items(), key=lambda x:x[1], reverse=True)[:9])
  bar_chart_category[key].update({"others":sum(list(temp.values()))})


bar_percentage = {}
for key in bar_chart_category:
  total = sum(bar_chart_category[key].values())
  bar_percentage[key] = {k: v / total * 100 for k, v in bar_chart_category[key].items()}


pie_percentage = {}
for key in pie_chart_category:
  total = sum(pie_chart_category[key].values())
  pie_percentage[key] = {k: v / total * 100 for k, v in pie_chart_category[key].items()}

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

# # Create a DataFrame for the data
df = pd.DataFrame(bar_percentage)

for item in bar_percentage:
  st.subheader(item)
  st.bar_chart(df[item])
