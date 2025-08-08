# insta_tracker.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# URL of Instagram profile or hashtag page
url = input("Enter Instagram URL (e.g. https://www.instagram.com/nike/): ")

# Start browser
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# Scroll down to load more posts
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find post captions
posts = driver.find_elements(By.XPATH, "//div[@class='_a9zs']/span")
captions = [post.text for post in posts if post.text.strip() != ""]

# Close browser
driver.quit()

# Combine captions into one big text
all_text = " ".join(captions)

# Create WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Show WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("🌀 Trending Words from Instagram Captions")
plt.show()

# Print top 10 common hashtags
hashtags = [word for word in all_text.split() if word.startswith("#")]
hashtag_counts = {}
for tag in hashtags:
    hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1

print("\n🔥 Top Hashtags:")
for tag, count in sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{tag}: {count}")
