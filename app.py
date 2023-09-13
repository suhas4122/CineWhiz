import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from streamlit_chat import message
from application.search.search_engine_llm import build_search_engine

st.subheader("CineWhiz: Your Personal Movie Recommender")

def format_response(response):
    lines = response.split('\n')  # Split input text into lines
    formatted_lines = [f'<p style="font-family: Lato; font-size: 18px; color: white;">{line}</p>' for line in lines]  # Wrap each line with paragraph tags
    return '\n'.join(formatted_lines)  # Join formatted lines with line breaks

if 'responses' not in st.session_state:
    st.session_state['responses'] = None

if 'agent' not in st.session_state:
    se = build_search_engine()
    st.session_state["agent"] = se

def get_response(query):
    agent = st.session_state['agent']
    response = agent.search(prompt = query)
    return response

textcontainer = st.container()
response_container = st.container()

def funcy():
    st.session_state["query"] = st.session_state.input
    st.session_state.input = ""
    
with textcontainer:
    st.text("")
    test_box = st.text_input("Type the prompt and press ENTER", key="input", on_change= funcy)
    query = st.session_state.get("query")
    if query:
        with st.spinner("searching..."):
            st.session_state['responses'] = get_response(query)
            
with response_container:
    if st.session_state['responses']:
        col1, col2 = st.columns([1, 1])
        responses = [dict(t) for t in {tuple(d.items()) for d in st.session_state['responses']}]
        odd_index = [i for i in range(len(responses)) if i % 2 == 0]
        even_index = [i for i in range(len(responses)) if i % 2 == 1]
        with col1:
            if len(odd_index) > 0:
                for i in odd_index:
                    response = responses[i]
                    image = response["poster"]
                    name = response["name"]
                    url = response["url"]
                    imdb_rating = response["rating"]
                    title_container = st.container()
                    col3, col4 = st.columns([15, 20])
                    with title_container:
                        with col3:
                            st.image(image, width = 120)
                        with col4:
                            st.markdown(f"**{name}**")
                            st.markdown(f"[IMDB Link]({url})")
                            st.markdown(f"***IMDB Rating: {imdb_rating}***")
                    st.divider()
        with col2:
            if len(even_index) > 0:
                for i in even_index:
                    response = responses[i]
                    image = response["poster"]
                    name = response["name"]
                    url = response["url"]
                    imdb_rating = response["rating"]
                    title_container = st.container()
                    col3, col4 = st.columns([15, 20])
                    with title_container:
                        with col3:
                            st.image(image, width = 120)
                        with col4:
                            st.markdown(f"**{name}**")
                            st.markdown(f"***IMDB Rating: {imdb_rating}***")
                            st.markdown(f"[IMDB Link]({url})")
                    st.divider()