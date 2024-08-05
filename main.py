import streamlit as st
import myChain

st.title("Restaurant Dish Recommendation")

cuisine = st.selectbox("Select a cuisine", ("Indian", "Italian", "Mexican", "Chinese", "Japanese", "Thai", "Korean", "Vietnamese", "French", "Spanish", "Greek", "Lebanese", "Turkish", "Moroccan", "Ethiopian", "Peruvian", "Brazilian", "Argentine", "Caribbean", "African"))

if cuisine:
    response = myChain.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)



