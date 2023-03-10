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
if 'params' not in st.session_state:
    st.session_state.params = '670-5'

# Get input from the user
in_coupons = st.sidebar.number_input("Number of coupons", min_value=1, max_value=1000, value=670)
in_pack = st.sidebar.number_input("Number of coupons per pack", min_value=1, max_value=in_coupons, value=5)
if '{}-{}'.format(in_coupons,in_pack) != st.session_state.params:
    st.session_state.results = []
    st.session_state.params = '{}-{}'.format(in_coupons,in_pack)

# Function to simulate coupon collectors problem
def simulate_coupon_collectors(n_coupons, n_pack):
    coupons = set()
    packs = 0
    while len(coupons) < n_coupons:
        packs += 1
        coupons.update(np.random.choice(n_coupons, size=n_pack, replace=False))
    return packs

col1, col2 = st.columns([1,1])

with col1:
    btn_run = st.button('Run')

with col2:
    if st.button('Reset'):
        # Reset the histogram data
        st.session_state.results = []

pl = st.empty()
with pl.container():
    fig, ax = plt.subplots()
    
    if btn_run or len(st.session_state.results)==0:
        # Run the simulation 100 times
        bar = st.progress(0)
        for i in range(100):
            bar.progress(i)
            result = simulate_coupon_collectors(in_coupons, in_pack)
            st.session_state.results.append(result)
        bar.progress(100)
    
    # Write total and draw the histogram
    st.write('Total: {} runs'.format(len(st.session_state.results)))
    sns.histplot(np.asarray(st.session_state.results), ax=ax)
    try:
        st.pyplot(fig) # st.write(fig)
    except Exception as e:
        st.exception(e)
