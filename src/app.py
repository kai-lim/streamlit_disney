import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV file
df = pd.read_csv("/Users/kai/Library/CloudStorage/OneDrive-Personal/03_Career/Github/streamlit_disney/data/princesses.csv")
df.head()
# post 1990 movies
post_1990 = df[df['FirstMovieYear'] > 1990]

st.title("👑 Princess Popularity Explorer")

years = ["All"] + sorted(post_1990["FirstMovieYear"].dropna().unique().tolist())
year_choice = st.selectbox("Filter by first movie year:", years, index=0)

if year_choice != "All":
    data = post_1990[post_1990["FirstMovieYear"] == year_choice].copy()
else:
    data = post_1990.copy()

if data.empty:
    st.info("No data for the selected year. Try a different filter.")
    st.stop()

# Sort by PopularityScore descending
data = data.sort_values("PopularityScore", ascending=False)

# Altair bar chart (x ordered by -y so it follows PopularityScore desc)
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("PrincessName:N", sort="-y", title="Princess"),
        y=alt.Y("PopularityScore:Q", title="Popularity Score"),
        tooltip=["PrincessName", "FirstMovieYear", "PopularityScore"]
    )
    .properties(height=420)
)

st.altair_chart(chart, use_container_width=True)