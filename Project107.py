import plotly.express as px
import csv
import pandas as pd

df = pd.read_csv("data107.csv")

student_df = df.loc[df['student_id'] == "TRL_987"]

print (df.groupby("level")["attempt"].mean())

fig = px.Figure(px.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y=['Level 1','Level 2','Level 3','Level 4']
))

fig.show()