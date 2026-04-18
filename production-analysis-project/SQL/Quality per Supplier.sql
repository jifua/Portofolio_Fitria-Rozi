SELECT raw_material_supplier, AVG(product_quality_score)
FROM production
GROUP BY raw_material_supplier;