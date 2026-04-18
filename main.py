import streamlit as st


def show_login():
    st.write("You are not logged in")

    if st.button("Log in with Microsoft"):
        st.login(provider="microsoft")


def show_authenticated():
    st.write(f"Welcome {st.user.name}")

    if st.button("Log out"):
        st.logout()


def show_debug_info():
    with st.expander("🔍 Debug: user info"):
        st.json(st.user.to_dict())


def main():
    st.title("Authentication demo")

    if not st.user.is_logged_in:
        show_login()
    else:
        show_authenticated()

    show_debug_info()


if __name__ == "__main__":
    main()