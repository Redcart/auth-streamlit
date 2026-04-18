import streamlit as st

st.title("Authentication demo")

if not st.user.is_logged_in:
    st.write("You are not logged in")

    if st.button("Log in with Microsoft"):
        st.login(provider="microsoft") #okta
else:
    st.write(f"Welcome {st.user.name}")

    if st.button("Log out"):
        st.logout()

# Debugging: show user info
st.write("User info:")
st.json(st.user.to_dict())