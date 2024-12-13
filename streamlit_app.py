import streamlit as st
from istatapi import discovery, retrieval

def pop_dropdown(result):
    return st.selectbox('Choose a Dimension', result.dimensions)

def search_by_id(df_Id):
    st.write(f"Searching by Dataset ID: {df_Id}")
    try:
        result = discovery.DataSet(dataflow_identifier=df_Id)
        st.write(result)
        ##pop_dropdown(result)
    except Exception as e:
        st.error(f"Error: {e}")

def search_by_keyword(keyword):
    st.write(f"Searching by Keyword: {keyword}")
    try:
        result = discovery.search_dataset(keyword)
        st.write(result)
    except Exception as e:
        st.error(f"Error: {e}")

def search_all():
    result = discovery.all_available()
    st.write(result)

options = ["Dataset ID", "Keyword","View All"]

pick_search_option = st.sidebar.selectbox("Search Dataset By", options)

search_query = ""
if pick_search_option == "Dataset ID":
    search_query = st.text_input("Search by Dataset ID")
elif pick_search_option == "Keyword":
    search_query = st.text_input("Search by Keyword")
elif pick_search_option == "View All":
    search_query = 'ALL'



if st.button("Search"):
    if search_query.strip():
        if pick_search_option == "Dataset ID":
            search_by_id(search_query)
        elif pick_search_option == "Keyword":
            search_by_keyword(search_query)
        else:
            search_all()
    else:
        st.warning("Please enter a search query before clicking the search button.")
