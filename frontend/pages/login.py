import streamlit as st

from api.client import (
    login_user,
    register_user,
    get_current_user
)

from utils.auth import (
    login_session
)


def show_login_page():

    st.title("🤖 AI Lead Qualification System")

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    # -----------------------------------
    # Login
    # -----------------------------------

    with tab1:

        st.subheader("Login")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            if not username or not password:

                st.warning(
                    "Please enter username and password."
                )

                return

            try:

                response = login_user(
                    username=username,
                    password=password
                )

                if response.status_code == 200:

                    data = response.json()

                    token = data.get(
                        "access_token"
                    )

                    if not token:

                        st.error(
                            "Access token not received."
                        )

                        return

                    # --------------------------
                    # Fetch Current User
                    # --------------------------

                    user_response = get_current_user(
                        token=token
                    )

                    if user_response.status_code == 200:

                        user_data = (
                            user_response.json()
                        )

                        # Debug (optional)
                        # st.write(user_data)

                        user_name = (

                            user_data.get(
                                "username"
                            )

                            or

                            user_data.get(
                                "sub"
                            )

                            or

                            username
                        )

                        role = (
                            user_data.get(
                                "role",
                                "USER"
                            )
                        )

                        login_session(
                            token=token,
                            username=user_name,
                            role=role
                        )

                        st.success(
                            "Login successful."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Unable to fetch user details."
                        )

                else:

                    try:

                        error = (
                            response.json()
                            .get(
                                "detail",
                                "Invalid credentials."
                            )
                        )

                    except:

                        error = (
                            "Invalid credentials."
                        )

                    st.error(error)

            except Exception as e:

                st.error(
                    f"Login failed: {str(e)}"
                )

    # -----------------------------------
    # Register
    # -----------------------------------

    with tab2:

        st.subheader("Register")

        new_username = st.text_input(
            "New Username",
            key="register_username"
        )

        new_password = st.text_input(
            "New Password",
            type="password",
            key="register_password"
        )

        if st.button("Register"):

            if (

                not new_username

                or

                not new_password

            ):

                st.warning(
                    "Please enter username and password."
                )

                return

            try:

                response = register_user(
                    username=new_username,
                    password=new_password
                )

                if response.status_code == 200:

                    st.success(
                        "User registered successfully. Please login."
                    )

                else:

                    try:

                        error = (
                            response.json()
                            .get(
                                "detail",
                                "Registration failed."
                            )
                        )

                    except:

                        error = (
                            "Registration failed."
                        )

                    st.error(error)

            except Exception as e:

                st.error(
                    f"Registration failed: {str(e)}"
                )