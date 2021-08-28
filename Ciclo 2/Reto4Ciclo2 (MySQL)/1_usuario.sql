CREATE TABLE usuario(
    usr_alias		varchar(20) PRIMARY KEY NOT NULL,
    usr_nombres		varchar(20) NOT NULL,
    usr_apellidos	varchar(20) NOT NULL,
    usr_email		varchar(40) DEFAULT '',
    usr_celular		varchar(15) NOT NULL,
    usr_clave		varchar(15) NOT NULL,
    usr_fecha_nto	varchar(10) DEFAULT ''
);

INSERT INTO usuario VALUES ("diva","Ana", "Diaz", "adiaz@gmail.com", "3124578905", "76$3&gg", "20/09/1978");
INSERT INTO usuario VALUES ("dreamer","Luis", "Rojas", "lrojas@gmail.com", "3185241967", "nsbdnbs", "11/10/1995");
INSERT INTO usuario VALUES ("green","Jorge", "Rodriguez", "jorgeGreen@gmail.com", "3208956726", "1234%$#", "20/12/2000");
INSERT INTO usuario VALUES ("lucky","Pedro", "Perez", "pp@gmail.com", "3221589161", "x1y2z3", "25/10/2000");
INSERT INTO usuario VALUES ("malopez","Maria", "Lopez", "malopez@gmail.com", "3501531561", "98774n", "4/03/1980");
INSERT INTO usuario VALUES ("neon","Nelson", "Ruiz", "nelson2@gmail.com", "3201643458", "45&$%", "25/08/1992");
INSERT INTO usuario VALUES ("ninja","Andres", "Cruz", "acninja@gmail.com", "3181513313", "pass123", "30/10/1990");
INSERT INTO usuario VALUES ("rose","Claudia", "Mendez", "florm@gmail.com", "3108972635", "flor121", "25/01/1990");