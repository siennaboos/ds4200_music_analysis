import pandas as pd
import altair as alt

# Load dataset
df = pd.read_csv("dataset.csv")

# Melt the dataframe to plot Danceability and Energy together
df_melted = df.melt(
    id_vars=["popularity"],
    value_vars=["danceability", "energy"],
    var_name="Feature",
    value_name="Value"
)

# Create Altair scatter plot
chart = (
    alt.Chart(df_melted)
    .mark_circle(size=70, opacity=0.6)
    .encode(
        x=alt.X("Value", title="Feature Value (Danceability / Energy)"),
        y=alt.Y("popularity", title="Popularity"),
        color=alt.Color("Feature", legend=alt.Legend(title="Feature")),
        tooltip=["Feature", "Value", "popularity"]
    )
    .properties(
        title="Relationship Between Danceability + Energy vs Popularity",
        width=700,
        height=500
    )
    .interactive()
)

chart.show()

