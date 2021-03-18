create database gui
use database gui
create table produto(
    id_prod int not null identity,
    nome varchar(20) not null,
    preco int not null,
    estoque int not null,
    disponibilidade bit not null
)
#INSERT INTO produto(nome,preco,estoque,disponibilidade) VALUES ('Batata',30.0,4,1)
