import streamlit as st 

# Title of the web app
st.title("TULA'S Hackathon ")

# create a form 
with st.form(key='my_form'):
    # create a selectbox
    option = st.selectbox(
    'Enter a keyword : ',
    ('data science', 'web development', 'python'))
    st.write('You selected:', option)
    # create a submit button
    submit_button = st.form_submit_button(label='Submit')

# check if the submit button is clicked
if submit_button:
    # if the submit button is clicked, then print the selected option
    st.write(option)

# create a css file
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    
