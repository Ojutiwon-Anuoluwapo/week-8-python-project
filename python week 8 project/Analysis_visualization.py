#BASIC ANATYSIS

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Load the metadata.csv file
df = pd.read_csv(r'C:\Users\User\Documents\python week 8 project\metadata.csv')

# 📆 Count the number of papers published each year
# This helps analyze research trends over time
year_counts = df['publish_year'].value_counts().sort_index()
print("Publication count by year:\n", year_counts)

# 🏛️ Identify the top 10 journals publishing COVID-19 research
# Useful for understanding which journals are most active
top_journals = df['journal'].value_counts().head(10)
print("\nTop publishing journals:\n", top_journals)

# 📝 Find the most frequent words in paper titles
# This gives insight into common research themes
titles = df['title'].dropna().str.lower().str.split()
all_words = [word for title in titles for word in title]
word_freq = Counter(all_words)
common_words = word_freq.most_common(20)
print("\nMost frequent words in titles:\n", common_words)

# VISUALIZATION

# 📈 Plot the number of publications over time
plt.figure(figsize=(10, 5))
year_counts.plot(kind='line', marker='o')
plt.title('Publications Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 Create a bar chart of the top publishing journals
plt.figure(figsize=(10, 5))
top_journals.plot(kind='bar', color='skyblue')
plt.title('Top Journals Publishing COVID-19 Research')
plt.xlabel('Journal')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ☁️ Generate a word cloud of paper titles
# This visually highlights the most frequent words
text = ' '.join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.tight_layout()
plt.show()

# 🧭 Plot distribution of paper counts by source
# Helps identify which sources contributed the most papers
source_counts = df['source_x'].value_counts()
plt.figure(figsize=(10, 5))
source_counts.plot(kind='bar', color='lightgreen')
plt.title('Distribution of Paper Counts by Source')
plt.xlabel('Source')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
