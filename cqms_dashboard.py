# app.py
import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("QLayer Style Dashboard")
st.markdown("""
This is a simple dashboard with a layout inspired by QLayer panels. It uses **Streamlit** to create interactive elements and display dynamic content.
""")

# Sidebar with controls
st.sidebar.header("Control Panel")

# Create sidebar sliders to control values
temperature = st.sidebar.slider("Temperature (K)", 200, 400, 300)
voltage = st.sidebar.slider("Voltage (V)", 1.0, 5.0, 3.5)
current = st.sidebar.slider("Current (A)", 0.5, 5.0, 1.0)

# Calculate power based on voltage and current
power = voltage * current

# Display results in the main panel
st.write(f"### Temperature: {temperature} K")
st.write(f"### Voltage: {voltage} V")
st.write(f"### Current: {current} A")
st.write(f"### Power: {power:.2f} W")

# Generate a random data table and display it
st.write("### Random Sensor Data")
data = pd.DataFrame({
    'Time': pd.date_range(start='2023-01-01', periods=10, freq='H'),
    'Temperature (K)': np.random.uniform(200, 400, 10),
    'Voltage (V)': np.random.uniform(1.0, 5.0, 10),
    'Current (A)': np.random.uniform(0.5, 5.0, 10),
    'Power (W)': lambda x: x['Voltage (V)'] * x['Current (A)']
})
st.dataframe(data)

# Create a line chart for temperature over time
st.write("### Temperature Over Time")
st.line_chart(data['Temperature (K)'])

# Footer
st.markdown("---")
st.markdown("**QLayer Dashboard Example** | Created using [Streamlit](https://streamlit.io)")
