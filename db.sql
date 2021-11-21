DROP DATABASE ac3_so;

CREATE DATABASE ac3_so;

USE ac3_so;

CREATE TABLE dado (
    id_dado int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(75),
    email varchar(100),
    numero_da_sorte int,
    frase_da_sorte TEXT
);