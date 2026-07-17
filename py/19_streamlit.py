import streamlit as st
import datetime

st.title("👤 Personal Dashboard")

#Sidebar for input
st.sidebar.header("personal Information")

name = st.sidebar.text_input("Your Name")
age = st.side.number_input("Your Age", min_value=1, max_value=120, value=25)
favorite_color = st.sidebar.color_picker("Favorite Color", "#FF6B6B") 
hobbies = st.sidebar.multiselect(
    "Your Hobbies",
    ["Reading", "Gaming", "Sports", "Music", "Cooking", "Travel"],
    defult=["Reading"]
)

#Main content
if name:
    st.header(f"Welcome, {name}! 👋")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Age", f"{age} years")

    with col2:
        st.metric("Hobbies, len(hobbies)")
    
    with col3:
        birth_year = datetime.datetime.now().year - age
        st.metric("Birth Year", birth_year)
    
    #Display favourite color
    st.subheader("Your Favourite Color")
    st.color_picker("", favourite_color, disabled=True)

    #Display hobbies
    if hobbies:
        st.subheader("Your Hobbies")
        for hobby in hobbies:
            st.write(f"{hobby}")

    #Fun fact
    st.subheader("Fun Fact")
    days_lived = age * 365
    st.info(f"You've lived approximately {days_lived:,} days!")

else:
    st.info("Please enter your name in the sidebar to get started!")