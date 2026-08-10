SELECT
  (SELECT COUNT(*) FROM customers) AS total_customers,
  (SELECT COUNT(*) FROM products)  AS total_products,
  (SELECT COUNT(*) FROM reviews)   AS total_reviews;