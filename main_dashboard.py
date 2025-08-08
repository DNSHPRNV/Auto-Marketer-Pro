# dashboard.py

import streamlit as st
from seo_tool import run_seo_tool
from email_tool import run_email_tool
from ads_optimizer import run_ads_tool
from insta_trends import run_insta_tool

# App Title
st.set_page_config(page_title="AutoMarketer Pro", layout="wide")
st.title("🤖 AutoMarketer Pro Dashboard")
st.markdown("Supercharge your digital marketing with Python-powered intelligence ⚡")

# Sidebar Navigation
tool = st.sidebar.radio("Select a Tool", ["SEO Analyzer", "Email Campaign Analyzer", "Google Ads Optimizer", "Instagram Trend Tracker"])

# Load Tool
if tool == "SEO Analyzer":
    run_seo_tool()

elif tool == "Email Campaign Analyzer":
    run_email_tool()

elif tool == "Google Ads Optimizer":
    run_ads_tool()

elif tool == "Instagram Trend Tracker":
    run_insta_tool()
