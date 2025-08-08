# seo_tool.py

import streamlit as st
import pandas as pd

def run_seo_tool():
    st.subheader("🔍 SEO Analyzer – Keyword CTR Checker")
    st.markdown("Upload your SEO data to analyze keywords, clicks, and impressions.")

    uploaded_file = st.file_uploader("Upload SEO CSV File", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.write("🔢 Uploaded Data Preview:")
        st.dataframe(df.head())

        try:
            df['CTR (%)'] = (df['Clicks'] / df['Impressions']) * 100
            st.success("✅ CTR calculated successfully!")

            st.write("📊 Keyword CTR Breakdown:")
            st.dataframe(df[['Keyword', 'Clicks', 'Impressions', 'CTR (%)']].sort_values(by='CTR (%)', ascending=False))
        except:
            st.error("⚠️ Make sure your CSV has columns: `Keyword`, `Clicks`, `Impressions`")

