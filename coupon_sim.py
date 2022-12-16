import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Set up the Streamlit app
st.title("Coupon Collectors Problem Simulator")

# Initialise session state
if 'results' not in st.session_state:
    st.session_state.results = []

# Get input from the user
in_coupons = st.sidebar.number_input("Number of coupons", min_value=1, max_value=1000, value=670)
in_pack = st.sidebar.number_input("Number of coupons per pack", min_value=1, max_value=in_coupons, value=5)

# Function to simulate coupon collectors problem
def simulate_coupon_collectors(n_coupons, n_pack):
    coupons = set()
    packs = 0
    while len(coupons) < n_coupons:
        packs += 1
        coupons.update(np.random.choice(n_coupons, size=n_pack, replace=False))
    return packs

button_row = st.empty()
k = 0
state = button_row.radio(
    "State",
    ('Pause', 'Run', 'Reset'),
    0,
    horizontal=True,
    key=k
)

fig, ax = plt.subplots()

pl = st.empty()
with pl.container():
    if state == 'Run':
        for i in range(100):
            # Run the simulation
            result = simulate_coupon_collectors(n_coupons, n_packs)
            st.session_state.results.append(result)
    elif state == 'Reset':
        # Reset the histogram data
        st.session_state.results = []
        st.experimental_rerun()
    # Draw the histogram
    sns.histplot(np.asarray(st.session_state.results), ax=ax)
    try:
        st.pyplot(fig) # st.write(fig)
    except Exception as e:
        st.exception(e)
