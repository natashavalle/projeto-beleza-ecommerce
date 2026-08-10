import pandas as pd
import numpy as np

# Carregar o CVS bruto - B2W-Reviews01
df = pd.read_csv(
    'B2W-Reviews01.csv',
    sep=',',
    quotechar='"',
    encoding='utf-8',
    on_bad_lines='warn'   # avisa quais linhas teve que pular, sem quebrar tudo
)
print(df.shape)

print(df.columns.tolist())
print(df.head(2))

print(df.shape)

print(df.columns.tolist())
print(df.head(2))

# --- ADICIONE ESSA LINHA AQUI ---
df['product_id'] = df['product_id'].astype(str).str.strip()

# Filtrar por categoria - beleza e perfumaria
beauty_categories = ['Beleza e Perfumaria', 'Beleza', 'Perfumaria']
df = df[df['site_category_lv1'].isin(beauty_categories)]

# Filtrar por categoria - beleza e perfumaria
beauty_categories = ['Beleza e Perfumaria', 'Beleza', 'Perfumaria']
df = df[df['site_category_lv1'].isin(beauty_categories)]

# Tratar tipos e remover duplicados e nulos essenciais
df['submission_date'] = pd.to_datetime(df['submission_date'], errors='coerce')
df['overall_rating'] = pd.to_numeric(df['overall_rating'], errors='coerce')
df['reviewer_birth_year'] = pd.to_numeric(df['reviewer_birth_year'], errors='coerce')

df = df.drop_duplicates()
df = df.dropna(subset=['overall_rating', 'reviewer_id', 'product_id'])

# Padronizar gênero e Estado
df['reviewer_gender'] = df['reviewer_gender'].fillna('Not informed').str.upper()
df['reviewer_state'] = df['reviewer_state'].fillna('Not informed').str.upper()

# Criar coluna de sentimento baseada na nota
def classify_sentiment(rating):
    if rating >= 4: return 'Positive'
    elif rating <= 2: return 'Negative'
    return 'Neutral'

df['sentiment'] = df['overall_rating'].apply(classify_sentiment)

# Normalizar em 3 tabelas
customers = (
    df[['reviewer_id', 'reviewer_birth_year', 'reviewer_gender', 'reviewer_state']]
    .drop_duplicates(subset='reviewer_id')
    .rename(columns={
        'reviewer_id': 'customer_id',
        'reviewer_birth_year': 'birth_year',
        'reviewer_gender': 'gender',
        'reviewer_state': 'state'
    })
)

products = (
    df[['product_id', 'product_name', 'product_brand',
        'site_category_lv1', 'site_category_lv2']]
    .drop_duplicates(subset='product_id')
    .rename(columns={
        'product_brand': 'brand',
        'site_category_lv1': 'category_lvl1',
        'site_category_lv2': 'category_lvl2'
    })
)

products = products.drop_duplicates(subset='product_id', keep='first')

reviews = (
    df[[
        'submission_date', 'reviewer_id', 'product_id', 'overall_rating',
        'recommend_to_a_friend', 'review_title', 'review_text', 'sentiment'
    ]]
    .rename(columns={
        'submission_date': 'review_date',
        'reviewer_id': 'customer_id',
        'overall_rating': 'rating',
        'recommend_to_a_friend': 'recommend_to_friend'
    })
)

# Exportar para CSV
customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
reviews.to_csv('reviews.csv', index=False)

print('Rows after cleaning:', len(reviews))
print('Unique customers:', len(customers))
print('Unique products:', len(products))

