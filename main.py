import streamlit as st
import pandas as pd
from pyproj import Transformer

st.title("Vakkenzoeker")

st.markdown(
    """
### Over Vakkenzoeker
**Vakkenzoeker** is een samenwerkingsproject van **Bafren al Jaff, Job Stelling en Bart ter Mull** gemaakt tijdens de Python cursus.

### Gebruiksaanwijzing
Vul de x- en y-coordinaat in en wij bepalen het vaknummer voor je!
"""
)


def get_waternet_vak(x, y):
    return "onbekend"


x = st.number_input("X coordinaat", value=123456)
y = st.number_input("Y coordinaat", value=456789)
vaknaam = get_waternet_vak(x, y)

st.text(f"Coordinaten x={x} en y={y} liggen in vak '{vaknaam}'")

transformer = Transformer.from_crs(28992, 4326)
lat, lon = transformer.transform(x, y)
df = pd.DataFrame({"lat": [lat], "lon": [lon]})
st.map(df)
