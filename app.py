import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Configure page settings
st.set_page_config(
    page_title="Quantum Physics — Engineering Physics",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Seamless full-screen styling to display pw.html cleanly
st.markdown(
    """
    <style>
    /* Hide Streamlit header and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    /* Fill entire viewport */
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 99999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load and render pw.html
html_path = Path(__file__).parent / "pw.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
