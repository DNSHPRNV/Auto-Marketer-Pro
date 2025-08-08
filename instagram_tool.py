# instagram_tool.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_instagram_tool():
    st.subheader("📱 Instagram Trend Tracker")
    st.markdown("Upload your Instagram hashtag dataset to see trending topics and engagement rates.")

    uploaded_file = st.file_uploader("Upload Instagram CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.write("📝 Preview of Uploaded Data:")
        st.dataframe(df.head())

        # Try basic analysis
        try:
            df['Engagement Rate (%)'] = ((df['Likes'] + df['Comments']) / df['Followers']) * 100

            top_tags = df.groupby('Hashtag').agg({
                'Likes': 'mean',
                'Comments': 'mean',
                'Engagement Rate (%)': 'mean'
            }).sort_values(by='Engagement Rate (%)', ascending=False).head(10)

            st.write("🔥 Top 10 Hashtags by Engagement Rate:")
            st.dataframe(top_tags)

            # Chart
            st.write("📊 Engagement Rate by Hashtag")
            fig, ax = plt.subplots()
            top_tags['Engagement Rate (%)'].plot(kind='barh', ax=ax)
            st.pyplot(fig)

        except:
            st.error("⚠️ Make sure CSV has columns: `Hashtag`, `Likes`, `Comments`, `Followers`")
