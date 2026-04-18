# ============================================
# PRODUCTION DATA ANALYSIS PIPELINE
# End-to-end: Load → Clean → Analyze → Export → SQL
# ============================================

# ============================
# 1. IMPORT LIBRARY
# ============================

import pandas as pd
import numpy as np
import sqlite3

# ============================
# 2. LOAD DATA
# ============================

# Ganti dengan nama file kamu
file_path = r"C:\Users\ASUS\OneDrive\Desktop\phyton\portofolio\PTF_PECGI\production_data.csv"

df = pd.read_csv(file_path)

print("=== DATA AWAL ===")
print(df.head())

# ============================
# 3. DATA UNDERSTANDING
# ============================

print("\n=== INFO DATA ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# ============================
# 4. DATA CLEANING
# ============================

# --- Standarisasi nama kolom ---
df.columns = df.columns.str.lower().str.replace(" ", "_")

# --- Convert tanggal ---
if 'production_date' in df.columns:
    df['production_date'] = pd.to_datetime(df['production_date'], errors='coerce')

# --- Handle missing values ---
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# --- Drop duplicate ---
df = df.drop_duplicates()

# ============================
# 5. FEATURE ENGINEERING
# ============================

# --- Feature tambahan ---
if 'mixing_time' in df.columns and 'product_quality_score' in df.columns:
    df['efficiency_score'] = df['product_quality_score'] / df['mixing_time']

# kategori kualitas
def categorize_quality(score):
    if score >= 8:
        return "High"
    elif score >= 6:
        return "Medium"
    else:
        return "Low"

df['quality_category'] = df['product_quality_score'].apply(categorize_quality)

# ============================
# 6. ANALISIS DATA
# ============================

print("\n=== ANALISIS ===")

# rata-rata kualitas
print("\nRata-rata kualitas:")
print(df['product_quality_score'].mean())

# kualitas per supplier
print("\nKualitas per supplier:")
print(df.groupby('raw_material_supplier')['product_quality_score'].mean())

# kualitas per pigment
print("\nKualitas per pigment:")
print(df.groupby('pigment_type')['product_quality_score'].mean())

# rata-rata waktu mixing
print("\nRata-rata mixing time:")
print(df['mixing_time'].mean())

# ============================
# 7. SORT DATA
# ============================

if 'production_date' in df.columns:
    df = df.sort_values(by='production_date')

# ============================
# 8. EXPORT CLEAN DATA
# ============================

clean_file = "Clean_Production_Data.csv"
df.to_csv(clean_file, index=False)

print(f"\nData bersih disimpan: {clean_file}")

# ============================
# 9. SAVE TO SQL DATABASE
# ============================

conn = sqlite3.connect("production.db")

df.to_sql("production", conn, if_exists="replace", index=False)

print("Data berhasil dimasukkan ke database SQLite!")

# ============================
# 10. SAMPLE SQL QUERY VIA PYTHON
# ============================

query = """
SELECT pigment_type, AVG(product_quality_score) as avg_quality
FROM production
GROUP BY pigment_type
ORDER BY avg_quality DESC;
"""

result = pd.read_sql(query, conn)

print("\n=== HASIL QUERY SQL (QUALITY PER PIGMENT) ===")
print(result)

# ============================
# 11. CLOSE CONNECTION
# ============================

conn.close()

print("\nPIPELINE SELESAI 🚀")