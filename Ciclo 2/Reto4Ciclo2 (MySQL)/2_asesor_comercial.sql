CREATE TABLE asesor_comercial(
    asr_id INT NOT NULL PRIMARY KEY,
    asr_nombres  VARCHAR(20) NOT NULL,
    asr_apellidos VARCHAR(20) NOT NULL,
    asr_sucursal_bancaria VARCHAR(40) NOT NULL
);

INSERT INTO asesor_comercial VALUES (101, "Juanquini","Takebuchi", "Centro Mayor");
INSERT INTO asesor_comercial VALUES (102, "Mariana", "Blandón", "Ensueño");
INSERT INTO asesor_comercial VALUES (103, "Farceliza", "De la Hoz", "Unicentro");
INSERT INTO asesor_comercial VALUES (104, "Cupertino", "Lions", "Gran Estación");
INSERT INTO asesor_comercial VALUES (105, "Mariano", "Cívico", "Américas");