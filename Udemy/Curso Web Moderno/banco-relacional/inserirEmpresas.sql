ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

INSERT INTO empresas
    (nome,cnpj)
VALUES
    ('Bradesco', 92564186000132),
    ('Vale', 27887148000146),
    ('Cielo', 64321213213254);

DESC empresas;

DESC prefeitos;

SELECT *
FROM empresas;

SELECT *
FROM cidades;

INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);