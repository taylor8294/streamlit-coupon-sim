import streamlit as st
import random
import matplotlib.pyplot as plt

st.title('Coupon Collectors Problem Simulator')

# Get input variables
num_coupons_per_pack = st.sidebar.number_input('Number of coupons per pack:', min_value=1)
total_num_coupons = st.sidebar.number_input('Total number of coupons:', min_value=1)

# Initialize variables for simulation
coupons = set()
num_packs = 0

# Function to simulate getting a pack of coupons
def get_pack():
    global num_packs
    num_packs += 1
    for i in range(num_coupons_per_pack):
        coupons.add(random.randint(1, total_num_coupons))

# Start button
if st.button('Start'):
    while len(coupons) < total_num_coupons:
        get_pack()

# Pause button
if st.button('Pause'):
    pass

# Reset button
if st.button('Reset'):
    coupons.clear()
    num_packs = 0

# Show histogram
plt.hist(num_packs)
st.pyplot()
