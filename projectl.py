import plotly.express as px
import csv
import pandas as pd
df = pd.read_csv("projectl.csv")
m = df.groupby("level")["attempt"].mean()

with open("projectl.csv") as f:
    df = csv.DictReader(f)
    fig = px.line(df,x=("level"),y=("attempt"))
    fig.show()

