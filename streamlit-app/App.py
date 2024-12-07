import streamlit as st

# Set the title of the app
st.title('Streamlit Text Input Example')

# Create a text input field
user_input = st.text_input('Enter something:', '')

# Handle and display the input
if user_input:
    st.write(f'You entered: {user_input}')
else:
    st.write('Please enter something in the text field.')
