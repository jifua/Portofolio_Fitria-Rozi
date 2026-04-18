SELECT pigment_type, AVG(efficiency_score) AS efficiency
FROM production
GROUP BY pigment_type
ORDER BY efficiency DESC;

UPDATE production
SET pigment_type = LOWER(pigment_type);