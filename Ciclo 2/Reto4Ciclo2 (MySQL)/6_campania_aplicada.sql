create table campania_aplicada(
cpa_app_id  int not null primary key,
cpa_usuario varchar(20) not null,
cpa_campania int not null,
cpa_app_fecha varchar(20),
foreign key (cpa_usuario) references usuario (usr_alias),
foreign key (cpa_campania) references campania (cmp_id)
);

insert into campania_aplicada values (1, "lucky", 1, "2017-10-25 20:00:00");
insert into campania_aplicada values (2, "malopez", 1, "2018-05-20 20:30:00");
insert into campania_aplicada values (3, "diva", 2, "2019-05-20 20:30:00");
insert into campania_aplicada values (4, "green", 2, "2020-01-10 17:30:20");
insert into campania_aplicada values (5, "diva", 3, "2018-06-22 21:30:00");
insert into campania_aplicada values (6, "lucky", 4, "2019-03-15 18:30:00");
insert into campania_aplicada values (7, "green", 4, "2020-02-15 20:30:20");
insert into campania_aplicada values (8, "green", 5, "2020-03-17 18:30:20");
insert into campania_aplicada values (9, "diva", 6, "2020-03-17 15:30:20");
insert into campania_aplicada values (10, "dreamer", 6, "2020-03-17 15:30:20");
insert into campania_aplicada values (11, "dreamer", 7, "2020-04-10 18:30:20");
insert into campania_aplicada values (12, "ninja", 8, "2020-02-17 20:30:20");
insert into campania_aplicada values (13, "lucky", 9, "2019-05-20 20:30:00");
insert into campania_aplicada values (14, "malopez", 9, "2020-01-20 20:30:00");
insert into campania_aplicada values (15, "ninja", 9, "2020-02-20 16:30:20");
insert into campania_aplicada values (16, "rose", 10, "2020-03-20 21:30:20");
insert into campania_aplicada values (17, "ninja", 11, "2020-03-27 18:30:20");