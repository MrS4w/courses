SELECT e.nome AS Empresa, c.nome AS Cidade
FROM empresas AS e, empresas_unidades AS eu, cidades AS c
WHERE e.id = eu.empresa_id AND c.id = eu.cidade_id AND sede;