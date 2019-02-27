SELECT *
FROM cidades AS c INNER JOIN prefeitos AS p ON c.id = p.cidade_id;

SELECT *
FROM cidades AS c LEFT JOIN prefeitos AS p ON c.id = p.cidade_id;

SELECT *
FROM cidades AS c RIGHT JOIN prefeitos AS p ON c.id = p.cidade_id;

-- FULL JOIN
    SELECT *
    FROM cidades AS c LEFT JOIN prefeitos AS p ON c.id = p.cidade_id
UNION
    SELECT *
    FROM cidades AS c RIGHT JOIN prefeitos AS p ON c.id = p.cidade_id;