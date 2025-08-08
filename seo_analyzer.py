# seo_analyzer.py

import requests
from bs4 import BeautifulSoup
from collections import Counter

# Ask user for a website
url = input("Enter the website URL (with https://): ")

# Fetch the website content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("\n🔍 Analyzing:", url)
print("-" * 40)

# 1. Title Tag Check
title = soup.title.string if soup.title else "No Title Found"
print("Title Tag:", title)
print("Title Length:", len(title))

# 2. Meta Description Check
description = soup.find("meta", attrs={"name": "description"})
if description:
    print("\nMeta Description:", description["content"])
    print("Meta Description Length:", len(description["content"]))
else:
    print("\nNo Meta Description Found")

# 3. H1 Tag Check
h1 = soup.find("h1")
print("\nH1 Tag:", h1.text.strip() if h1 else "No H1 Tag Found")

# 4. Word Frequency (basic keyword analysis)
print("\nTop 10 Most Common Words:")
text = soup.get_text().lower()
words = text.split()
filtered_words = [word for word in words if len(word) > 3]
word_counts = Counter(filtered_words)
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")

print("\n✅ SEO Report Done!")