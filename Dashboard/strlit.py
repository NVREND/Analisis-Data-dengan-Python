import streamlit as st 
 
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.title("Belajar Analisis Data") # title
st.header('Pengembangan Dashboard') #header
st.subheader('Pengembangan Dashboard')#subheader
st.caption("Copyrigt (c) 2023")#caption

#code
code = """ def hello():
    print("Hello Streamlit")"""

st.code(code, language='python')

st.text("Halo, calon orang sukses")

#latex
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

## DISPLAY DATA

# data frame
import pandas as pd

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
})

st.dataframe(data=df, width=600, height=200)

#table
st.table(data=df)

#metric
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")


#json
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
})

###           CHART                  #####
# Digunakan untuk menampilkan grafik visualisasi data ke dalam streamlit app.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)


####           INPUT WIDGET            ####

## Text Input
name = st.text_input(label='Nama Lengkap', value='')
st.write("Nama: ", name)


## Text-Area
text = st.text_area("Feedback")
st.write('Feedback: ', text)


## Number Input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')


## Date Input
import datetime 

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir: ', date)


## File Uploader 
uploaded_file = st.file_uploader('choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)


## Camera Input 
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


## Button
if st.button('Say hello'):
    st.write('Hello there')


## Check Box
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp')


## Radio Button 
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)


## Select Box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
)


## Multi select
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)






######       BASIC LAYOUT       ######


## Slidebar
 
st.title('Belajar Analisis Data')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)



## Columns
st.title('Belajar Analisis Data')
col1, col2, col3 = st.columns(3)
# col1, col2, col3 = st.columns[(3,1,1)]
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")



## Tabs 
st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")



## Container
with st.container():
    st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
 
st.write("Outside the container")



## Expander
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) 
 
with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )