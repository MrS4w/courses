-- População por região
SELECT regiao AS 'Região', SUM(populacao) as Total
FROM estados
GROUP BY regiao
ORDER BY Total DESC;

-- População total
SELECT SUM(populacao) as Total
FROM estados;

-- Média por estado
SELECT AVG(populacao) as 'Média por estado'
FROM estados;