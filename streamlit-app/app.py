
import streamlit as st
import requests
from streamlit.components.v1 import html

API_URL = "https://golf-platform.onrender.com"

st.set_page_config(page_title="Golf Platform", page_icon="🏌️", layout="centered")

# --- Sidebar Navigation ---
st.sidebar.title("🏌️ Golf Platform")
page = st.sidebar.radio("Go to", ["Login", "Dashboard"])

# --- Login / Register Page ---
if page == "Login":
    st.title("🔐 Login or Register")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            f"{API_URL}/token",
            data={"username": email, "password": password}
        )
        if response.status_code == 200:
            token = response.json()["access_token"]
            st.session_state["token"] = token
            st.success("✅ Logged in successfully.")
        else:
            st.error("❌ Login failed")

    if st.button("Register"):
        r = requests.post(f"{API_URL}/register", json={"email": email, "password": password})
        if r.status_code == 200:
            st.success("✅ Account created! You can now log in.")
        else:
            st.error(f"❌ Registration failed: {r.text}")

    # Optional: Google Sign-In
    st.markdown("Or login with Google:")
    html("""
    <script src="https://accounts.google.com/gsi/client" async defer></script>
    <div id="g_id_onload"
         data-client_id="88785808917-5r4crdq3kjgv7t7tga8ln9j4sg3286ea.apps.googleusercontent.com"
         data-callback="handleCredentialResponse"
         data-auto_prompt="true">
    </div>
    <div class="g_id_signin" data-type="standard"></div>
    <script>
    function handleCredentialResponse(response) {
      window.parent.postMessage(response.credential, "*");
    }
    </script>
    """, height=300)

    html("""
    <script>
    window.addEventListener("message", (event) => {
      const token = event.data;
      const el = window.parent.document.querySelector("iframe + div");
      el.innerText = "✅ Google Token: " + token;
    });
    </script>
    """)

# --- Dashboard Page ---
elif page == "Dashboard":
    if "token" not in st.session_state:
        st.warning("🔒 Please log in to access your dashboard.")
        st.stop()

    st.title("📊 My Golf Dashboard")
    st.success("✅ Logged in as secure user.")
    # Add dashboard charts, metrics, etc. here
