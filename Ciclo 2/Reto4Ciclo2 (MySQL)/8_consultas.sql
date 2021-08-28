select 'Consulta 1';
select cmp_descripcion from campania order by cmp_descripcion;
select 'Consulta 2';
select cmp_descripcion, csm_cuotas, csm_tasa_interes from consumo join campania where consumo.csm_id=campania.cmp_id order by csm_tasa_interes;
select 'Consulta 3';
select campania.cmp_descripcion  
from consumo 
join campania on consumo.csm_id=campania.cmp_id
where consumo.csm_asesor =102 order by cmp_descripcion;
select 'Consulta 4';
select campania.cmp_descripcion
from campania_aplicada
join campania on campania_aplicada.cpa_campania=campania.cmp_id
where campania_aplicada.cpa_usuario='lucky' order by cmp_descripcion;
select 'Consulta 5';
select distinct usuario.usr_alias, usuario.usr_nombres, usuario.usr_apellidos 
from usuario 
join campania_aplicada on campania_aplicada.cpa_usuario = usuario.usr_alias 
where campania_aplicada.cpa_campania >= 6
order by usuario.usr_alias ;
select 'Consulta 6';
select count(csm_cuotas) from consumo where csm_cuotas=60;