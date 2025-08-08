# google_ads_optimizer.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_google_ads_optimizer():
    st.subheader("💸 Google Ads Optimizer")
    st.markdown("Upload your exported Google Ads report to find optimization insights.")

    uploaded_file = st.file_uploader("Upload Google Ads CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.write("📋 Preview of Uploaded Data:")
        st.dataframe(df.head())

        try:
            df['CTR (%)'] = (df['Clicks'] / df['Impressions']) * 100
            df['CPC (₹)'] = df['Cost'] / df['Clicks']
            df['Conversion Rate (%)'] = (df['Conversions'] / df['Clicks']) * 100

            top_ads = df.sort_values(by='CTR (%)', ascending=False).head(10)

            st.write("🚀 Top 10 Ad Sets by CTR:")
            st.dataframe(top_ads[['Ad Group', 'CTR (%)', 'CPC (₹)', 'Conversion Rate (%)']])

            st.write("📊 CPC vs CTR")
            fig, ax = plt.subplots()
            ax.scatter(df['CPC (₹)'], df['CTR (%)'], alpha=0.7)
            ax.set_xlabel("CPC (₹)")
            ax.set_ylabel("CTR (%)")
            st.pyplot(fig)

            st.markdown("### 🧠 Suggestions:")
            st.write("- 🚨 High CPC but low CTR → Consider improving ad copy.")
            st.write("- 🎯 Low conversions → Refine targeting or landing page.")
            st.write("- 📉 High impressions but low clicks → Weak headlines or irrelevant keywords.")

        except:
            st.error("⚠️ Make sure CSV has: `Impressions`, `Clicks`, `Cost`, `Conversions`, `Ad Group`")
