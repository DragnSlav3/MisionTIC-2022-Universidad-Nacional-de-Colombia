create table libranza (
lbr_id int not null primary key,
lbr_empresa varchar(50) not null,
lbr_meses_plazo int not null,
lbr_tasa_interes varchar(5) not null,
foreign key (lbr_id) references campania (cmp_id)
);

insert into libranza values (6, "La Cuncia S.A", 60, 1.00);
insert into libranza values (7, "Colsubsidio", 48, 0.50);
insert into libranza values (8, "Los Recuerdos Ltda.", 36, 0.50);
insert into libranza values (9, "Conductores S.A", 60, 0.75);
insert into libranza values (10, "Pardo Rojo Ltda.", 60, 0.50);
insert into libranza values (11, "Manaure S.A.S", 36, 0.75);
insert into libranza values (12, "Rio Frío Ltda.", 24, 0.90);
insert into libranza values (13, "Río Bravo S.A.S", 48, 0.85);