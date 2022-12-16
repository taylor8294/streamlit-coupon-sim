import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Set up the Streamlit app
st.title("Coupon Collectors Problem Simulator")

# Get input from the user
n_coupons = st.sidebar.number_input("Number of coupons", min_value=1, max_value=1000, value=670)
n_packs = st.sidebar.number_input("Number of coupons per pack", min_value=1, max_value=n_coupons, value=5)

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

# Create a histogram to display the results of the simulations
pl = st.empty()
results = []
while True:
    with pl.container():
        if state == 'Running':
            # Run the simulation and update the histogram
            result = simulate_coupon_collectors(n_coupons, n_packs)
            results.append(result)
            fig, ax = plt.subplots()
            sns.histplot(np.asarray(results), ax=ax)
            try:
                st.pyplot(fig) # st.write(fig)
            except Exception as e:
                st.exception(e)
        elif state == 'Reset':
            # Change state back to Pause
            k += 1
            state = button_row.radio(
                "State",
                ('Pause', 'Run', 'Reset'),
                0,
                horizontal=True,
                key=k
            )
            # Reset the histogram data and display an empty histogram
            results = []
            fig, ax = plt.subplots()
            sns.histplot(np.asarray(results),ax=ax)
            try:
                st.pyplot(fig) # st.write(fig)
            except Exception as e:
                st.exception(e)
    time.sleep(1)
