# /streamlit-app/app.py
import streamlit as st
import requests
from typing import List

API_URL = "http://127.0.0.1:8000"

if "token" not in st.session_state:
    st.session_state.token = None

def login():
    st.title("Login to Golf App")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        resp = requests.post(f"{API_URL}/login", json={"email": email, "password": password})
        if resp.status_code == 200:
            st.session_state.token = resp.json()["access_token"]
            st.success("Logged in!")
            st.experimental_rerun()
        else:
            st.error("Login failed")

def get_headers():
    return {"Authorization": f"Bearer {st.session_state.token}"}

def dashboard():
    st.title("🏌️ Golf Dashboard")
    me = requests.get(f"{API_URL}/me", headers=get_headers()).json()
    st.subheader(f"Welcome {me['name']} ({me['email']})")

    # My rounds & WHS handicap
    rounds = requests.get(f"{API_URL}/my-rounds", headers=get_headers()).json()
    if rounds:
        diffs = sorted([r["differential"] for r in rounds if r.get("differential")])
        st.write(f"Latest differentials: {diffs}")
    else:
        st.info("No rounds yet.")

    sg = requests.get(f"{API_URL}/strokes-gained", headers=get_headers()).json()
    st.metric("Strokes Gained Tee", sg["tee"])
<<<<<<< HEAD
    st.metric("Strokes Gained Approach", sg["approach"])
    st.metric("Strokes Gained Putting", sg["putting"])

    # Videos
    st.subheader("📹 Swing Videos")
    for r in rounds:
        if r.get("video_url"):
            st.video(r["video_url"])

    # Map sample
    st.subheader("Map (placeholder for Google/Mapbox)")
    st.map()

def main():
    if not st.session_state.token:
        login()
    else:
        page = st.sidebar.selectbox("Navigate", ["Dashboard", "Logout"])
        if page == "Dashboard":
            dashboard()
        elif page == "Logout":
            st.session_state.token = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()
=======
st.metric("Strokes Gained Approach", sg["approach"])
st.metric("Strokes Gained Putting", sg["putting"])

>>>>>>> 7dc98ebfc0c2d4646f8660a018a198e646b48bcf
