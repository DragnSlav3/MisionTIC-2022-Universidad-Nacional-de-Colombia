import random

salutacion = ["Queridos", "Apreciados", "Distinguidos", "Honorables", "Estimados", "Respetados"]  #se definen listas
marranos = ["compatiotas:", "conciudadanos:", "amigos:", "coterráneos:", "copartidarios:", "electores:"]
condicion = ["En mi gobierno", "Con su apoyo", "Siendo elegido", "Con su ayuda", "Si me siguen", "Durante mi mandato"]
compromiso = ["voy a derrotar", "venceré", "eliminaré", "acabaré", "lucharé contra", "combatiré"]
ilusion = ["la violencia y", "la delincuencia y", "la corrupción y", "la inflación y", "la pobreza y", "el desplazamiento y"]
promesa = ["trabajaré por", "garantizaré", "protegeré", "velaré por", "promoveré", "defenderé"]
beneficio = ["la educación", "el empleo", "la seguridad", "la paz", "la igualdad", "la salud"]
entorno = ["del país.", "de la ciudad.", "de la comunidad.", "de la población.", "para toda la gente.", "de cada colombiano."]

sel_salutacion = random.choice(salutacion)
sel_marranos = random.choice(marranos)
sel_condicion = random.choice(condicion)
sel_compromiso = random.choice(compromiso)
sel_ilusion = random.choice(ilusion)
sel_promesa = random.choice(promesa)
sel_beneficio = random.choice(beneficio)
sel_entorno = random.choice(entorno)

print(sel_salutacion + " " + sel_marranos + " " + sel_condicion + " " 
      + sel_compromiso + " " + sel_ilusion + " " + sel_promesa + " " + sel_beneficio + " " + sel_entorno)