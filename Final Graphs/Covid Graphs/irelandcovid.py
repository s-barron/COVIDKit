import pandas as pd
import pygal

df = pd.read_csv("irelandcovid.csv")
total_cases = (df["total_cases"]).max(skipna = True)
total_deaths = (df["total_deaths"]).max(skipna= True)
total_vaccinations = (df["total_vaccinations"]).max(skipna= True)


line_chart = pygal.HorizontalBar()
line_chart.title = 'Ireland Covid Data'
line_chart.add('Total Cases', total_cases)
line_chart.add('Total Deaths', total_deaths)
line_chart.add('Total Vaccinations', total_vaccinations)

#line_chart.add('Most New', most_new)
line_chart.render_to_file("Ireland COVID-19 Data.svg")