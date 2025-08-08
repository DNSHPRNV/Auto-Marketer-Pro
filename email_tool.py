# email_tool.py

import streamlit as st
import pandas as pd

def run_email_tool():
    st.subheader("📨 Email Campaign Analyzer – Open Rate & Click Rate Tracker")
    st.markdown("Upload your email campaign CSV file to analyze performance.")

    uploaded_file = st.file_uploader("Upload Email Campaign CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.write("📋 Uploaded Campaign Preview:")
        st.dataframe(df.head())

        try:
            df['Open Rate (%)'] = (df['Opens'] / df['Delivered']) * 100
            df['Click Rate (%)'] = (df['Clicks'] / df['Delivered']) * 100
            st.success("✅ Open and Click Rates calculated successfully!")

            st.write("📊 Email Campaign Analysis:")
            st.dataframe(df[['Campaign Name', 'Delivered', 'Opens', 'Clicks', 'Open Rate (%)', 'Click Rate (%)']]
                         .sort_values(by='Open Rate (%)', ascending=False))
        except:
            st.error("⚠️ Make sure your CSV has columns: `Campaign Name`, `Delivered`, `Opens`, `Clicks`")
