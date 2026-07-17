import streamlit as st
import pandas as pd
from optimizer import optimize

if "calculated" not in st.session_state:
    st.session_state.calculated = False

st.title("Food Distribution Optimizer")

families = st.number_input("Families", value=205)
singles = st.number_input("Singles", value=136)

units_availible = st.number_input("Units of food available", value=1000)
quant = optimize(units_availible, families, singles)

def calculate():
    st.session_state.calculated = True

st.button("Calculate", on_click = calculate) 

if st.session_state.calculated:
    if len(quant) >= 3:
        df = pd.DataFrame(
            [
                {"Units per family": quant[0][0], "Units per single": quant[0][1], "Extra units": quant[0][2]},
                {"Units per family": quant[1][0], "Units per single": quant[1][1], "Extra units": quant[1][2]},
                {"Units per family": quant[2][0], "Units per single": quant[2][1], "Extra units": quant[2][2]},
            ]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.write("There are less than 3 valid options. The options we have found are:")
        for i in quant:
            st.write(f"({i[0]}, {i[1]}, {i[2]})")



if st.button("See more"):
    for i in quant:
        st.write(f"({i[0]}, {i[1]}, {i[2]})")



st.write("Custom ratio:")

col1, col2 = st.columns(2)

with col1:
    x = st.number_input("Units per family", min_value=0, value=4)

with col2:
    y = st.number_input("Units per single", min_value=0, value=2)

used = families*x + singles*y
leftover = units_availible - used

st.write("Extra units:", leftover)
