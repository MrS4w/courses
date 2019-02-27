INSERT INTO cidades
    (nome, area, estado_id)
VALUES
    ('Campinas', 795, 26);

INSERT INTO cidades
    (nome, area, estado_id)
VALUES
    ('Niterói', 133.9, 20);

INSERT INTO cidades
    (nome, area, estado_id)
VALUES('Caruaru', 920.6, (SELECT id
        from estados
        WHERE sigla = 'PE'))

INSERT INTO cidades
    (nome, area, estado_id)
VALUES('Juazeiro do Norte', 248.2, (SELECT id
        FROM estados
        WHERE sigla = 'CE'))

SELECT *
FROM cidades;