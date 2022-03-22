use categoriasobjetos;

create table categoria(
	categoria_id int auto_increment,
    nome varchar(100),
    primary key (categoria_id)
);

create table objeto(
	objeto_id int auto_increment,
    categoria_id int,
    nome varchar(100),
    primary key(objeto_id),
    foreign key (categoria_id) references categoria(categoria_id) on delete cascade on update cascade
);