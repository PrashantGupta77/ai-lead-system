import streamlit as st


def init_session_state():
    if "token" not in st.session_state:
        st.session_state.token = None

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = None

    if "role" not in st.session_state:
        st.session_state.role = None


def login_session(token, username, role):
    st.session_state.token = token
    st.session_state.username = username
    st.session_state.role = role
    st.session_state.logged_in = True


def logout_session():
    st.session_state.token = None
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.logged_in = False


def is_logged_in():
    return st.session_state.logged_in


def is_admin():
    return st.session_state.role == "ADMIN"