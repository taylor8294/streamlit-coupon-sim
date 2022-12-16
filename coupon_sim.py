import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

state = button_row.radio(
    "State",
    ('Pause', 'Run', 'Reset'),
    0,
    horizontal=True
)

# Create a histogram to display the results of the simulations
pl = st.empty()
results = []
fig, ax = plt.subplots()
ax.hist(np.asarray(results))
pl.pyplot(fig)

while True:
    if state == 'Running':
        # Run the simulation and update the histogram
        result = simulate_coupon_collectors(n_coupons, n_packs)
        results.append(result)
        fig, ax = plt.subplots()
        ax.hist(np.asarray(results))
        pl.pyplot(fig)
    elif state == 'Reset':
        # Reset the histogram data and display an empty histogram
        results = []
        fig, ax = plt.subplots()
        ax.hist(np.asarray(results))
        pl.pyplot(fig)
        # Change state back to Pause
        state = button_row.radio(
            "State",
            ('Pause', 'Run', 'Reset'),
            0,
            horizontal=True
        )
