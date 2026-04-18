SELECT pigment_type, AVG(product_quality_score) AS avg_quality
FROM production
GROUP BY pigment_type;