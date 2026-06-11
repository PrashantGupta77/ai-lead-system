import streamlit as st

from utils.auth import (
    init_session_state,
    is_logged_in,
    logout_session
)

from pages.login import show_login_page
from pages.lead_processing import show_lead_processing_page
from pages.admin_dashboard import show_admin_dashboard


st.set_page_config(
    page_title="AI Lead Qualification System",
    page_icon="🤖",
    layout="wide"
)


def main():

    init_session_state()

    if not is_logged_in():
        show_login_page()
        return

    with st.sidebar:
        st.title("🤖 AI Lead System")

        st.write(f"**User:** {st.session_state.username}")
        st.write(f"**Role:** {st.session_state.role}")

        pages = [
            "Lead Processing"
        ]

        if st.session_state.role == "ADMIN":
            pages.append("Admin Dashboard")

        page = st.radio(
            "Navigation",
            pages
        )

        st.divider()

        if st.button("Logout"):
            logout_session()
            st.rerun()

    if page == "Lead Processing":
        show_lead_processing_page()

    elif page == "Admin Dashboard":
        show_admin_dashboard()


if __name__ == "__main__":
    main()