import streamlit as st

def calculate_percentage_yield(mass_of_extract, initial_mass_of_plant):
    """Calculate the percentage yield of plant extracts."""
    try:
        percentage_yield = (mass_of_extract / initial_mass_of_plant) * 100
        return percentage_yield
    except ZeroDivisionError:
        return 0

# Streamlit app title
st.title('Plant Extracts Percentage Yield Calculator')

# Input fields for the initial mass of the plant and the mass of the extract obtained
initial_mass_of_plant = st.number_input('Enter the initial mass of the plant material (g):', min_value=0.0, format='%f')
mass_of_extract = st.number_input('Enter the mass of the extract obtained (g):', min_value=0.0, format='%f')

# Button to calculate the percentage yield
if st.button('Calculate Percentage Yield'):
    # Calculate the percentage yield
    percentage_yield = calculate_percentage_yield(mass_of_extract, initial_mass_of_plant)
    
    # Display the result
    st.write(f'The percentage yield of the plant extracts is: {percentage_yield:.2f}%')

