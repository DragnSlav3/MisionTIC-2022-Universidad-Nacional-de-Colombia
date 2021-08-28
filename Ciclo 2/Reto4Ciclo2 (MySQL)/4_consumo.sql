create table consumo(
csm_id int not null primary key,
csm_asesor int not null,
csm_cuotas int not null,
csm_tasa_interes varchar(5) not null,
foreign key (csm_id) references campania (cmp_id),
foreign key (csm_asesor) references asesor_comercial(asr_id)
);

insert into consumo values (1, 102, 60, 0.72);
insert into consumo values (2, 103, 72, 1.0);
insert into consumo values (3, 101, 48, 2.50);
insert into consumo values (4, 104, 60, 0.90);
insert into consumo values (5, 105, 60, 0.70);