SELECT * from autor

SELECT * from itensvenda

insert into itensvenda

alter table itensvenda add FOREIGN key (id_produtos) REFERENCES produtos (id)

alter table itensvenda add column ID_produtos serial not null

alter table itensvenda add constraint fk_id_produtos FOREIGN key (id_produtos) REFERENCES produtos (id)

select * from produtos join itensvenda itensvenda2 ON itensvenda2.id_produtos = produtos.id

select * from produtos left join itensvenda itensvenda3 ON itensvenda3.id_produtos = produtos.id

select * from produtos right join itensvenda itensvenda4 ON itensvenda4.id_produtos = produtos.id

select * from produtos INNER join itensvenda itensvenda5 ON itensvenda5.id_produtos = produtos.id

