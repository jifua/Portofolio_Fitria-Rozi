import os
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# PATH SETUP
# ===============================
BASE_DIR = r'C:\Users\ASUS\OneDrive\Desktop\phyton\portofolio\PTF_DATA_ANALYSIS'
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'Ecommerce.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv(DATA_PATH)
df = df.dropna().drop_duplicates()

print("✅ Data Loaded")

# ===============================
# FEATURE ENGINEERING
# ===============================
df['Price Category'] = pd.cut(
    df['Price of the product'],
    bins=[0, 1000, 3000, 10000],
    labels=['Low', 'Medium', 'High']
)

df['Product Score'] = (
    0.4 * df['Rating of the product'] +
    0.3 * df['Customer review sentiment score (overall)'] +
    0.3 * df['Probability for the product to be recommended to the person']
)

def clean_plot(xlabel, ylabel, caption, filename):
    ax = plt.gca()

    # Remove border (spines)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    # Grid tipis
    plt.grid(alpha=0.3)

    # Label axis
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)

    # Caption (judul di bawah)
    plt.figtext(0.5, -0.05, caption, ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

# ===============================
# 📊 1. DISTRIBUSI HARGA (Histogram)
# ===============================
plt.figure(figsize=(8,5))

plt.hist(
    df['Price of the product'],
    bins=30,
    edgecolor='black',
    linewidth=1.2
)

clean_plot(
    'Price',
    'Frequency',
    'Gambar 1. Distribusi Harga Produk',
    os.path.join(OUTPUT_DIR, 'price_distribution.png')
)

# ===============================
# 📊 2. RATING vs REKOMENDASI (Scatter)
# ===============================
plt.figure(figsize=(8,5))

plt.scatter(
    df['Rating of the product'],
    df['Probability for the product to be recommended to the person'],
    alpha=0.6,
    linewidths=0.8
)

clean_plot(
    'Product Rating',
    'Recommendation Probability',
    'Gambar 2. Hubungan Rating dan Probabilitas Rekomendasi',
    os.path.join(OUTPUT_DIR, 'rating_vs_recommendation.png')
)

# ===============================
# 📊 3. SENTIMENT vs REKOMENDASI
# ===============================
plt.figure(figsize=(8,5))

plt.scatter(
    df['Customer review sentiment score (overall)'],
    df['Probability for the product to be recommended to the person'],
    alpha=0.6,
    linewidths=0.8
)

clean_plot(
    'Sentiment Score',
    'Recommendation Probability',
    'Gambar 3. Pengaruh Sentiment terhadap Rekomendasi',
    os.path.join(OUTPUT_DIR, 'sentiment_analysis.png')
)

# ===============================
# 📊 4. BRAND ANALYSIS (Bar Horizontal)
# ===============================
brand = df.groupby('Brand of the product')['Rating of the product'].mean().sort_values().tail(10)

plt.figure(figsize=(10,6))

brand.plot(
    kind='barh',
    linewidth=2
)

plt.legend(['Average Rating'], loc='center left', bbox_to_anchor=(1, 0.5))

clean_plot(
    'Rating',
    'Brand',
    'Gambar 4. Top 10 Brand berdasarkan Rating',
    os.path.join(OUTPUT_DIR, 'brand_analysis.png')
)

# ===============================
# 📊 5. SEASON ANALYSIS (Bar)
# ===============================
season = df.groupby('Season')['Probability for the product to be recommended to the person'].mean()

plt.figure(figsize=(8,5))

season.plot(
    kind='bar',
    linewidth=2
)

plt.legend(['Recommendation Probability'], loc='upper left', bbox_to_anchor=(1, 1))

clean_plot(
    'Season',
    'Probability',
    'Gambar 5. Pengaruh Musim terhadap Rekomendasi Produk',
    os.path.join(OUTPUT_DIR, 'season_analysis.png')
)

# ===============================
# 📊 6. PRICE SEGMENT (Bar)
# ===============================
segment = df.groupby('Price Category', observed=True)[
    'Probability for the product to be recommended to the person'
].mean()

plt.figure(figsize=(8,5))

segment.plot(
    kind='bar',
    linewidth=2
)

plt.legend(['Recommendation'], loc='upper left', bbox_to_anchor=(1, 1))

clean_plot(
    'Price Category',
    'Probability',
    'Gambar 6. Rekomendasi berdasarkan Kategori Harga',
    os.path.join(OUTPUT_DIR, 'price_segment.png')
)

# ===============================
# 📊 7. TOP PRODUCTS (Bar)
# ===============================
top_products = df.sort_values(by='Product Score', ascending=False).head(10)

plt.figure(figsize=(10,6))

top_products.set_index('Brand of the product')['Product Score'].plot(
    kind='barh',
    linewidth=2
)

plt.legend(['Product Score'], loc='center left', bbox_to_anchor=(1, 0.5))

clean_plot(
    'Score',
    'Brand',
    'Gambar 7. Produk Terbaik Berdasarkan Skor',
    os.path.join(OUTPUT_DIR, 'top_products.png')
)

# ===============================
# 📊 8. CORRELATION MATRIX
# ===============================
corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,8))

im = plt.imshow(corr)

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90, fontsize=7)
plt.yticks(range(len(corr.columns)), corr.columns, fontsize=7)

plt.colorbar(im)

clean_plot(
    '',
    '',
    'Gambar 8. Korelasi antar Variabel',
    os.path.join(OUTPUT_DIR, 'correlation.png')
)

# ===============================
# 📌 FINAL INSIGHT
# ===============================
print("""
📌 BUSINESS INSIGHT:

1. Rating produk memiliki pengaruh terbesar terhadap kemungkinan direkomendasikan
2. Sentiment pelanggan memperkuat keputusan pembelian
3. Harga bukan faktor utama → kualitas lebih penting
4. Brand dengan rating tinggi memiliki kepercayaan pelanggan lebih baik
5. Segment harga medium-high paling optimal untuk bisnis

📊 STRATEGI:
- Fokus pada peningkatan kualitas produk
- Gunakan sentiment analysis untuk monitoring
- Prioritaskan produk dengan skor tinggi untuk campaign
""")

print("\n✅ ANALYSIS COMPLETED")