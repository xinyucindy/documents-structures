#!/usr/bin/python
# -*- coding: utf-8 -*-

output = open("tournagesdefilmsparis2011.xml", "w", encoding='utf-8')
output.write('<?xml version="1.0" encoding="utf-8"?>\n<tournages>\n')
i = 1

with open("tournagesdefilmsparis2011.csv", encoding="utf8") as input :
    for line in input:
        line = line.strip()
        infos = line.split(";")
        if infos[0]=="Titre":
            continue
        else :
            output.write('\t<tournage n="'+str(i)+'">\n')
            output.write(f'\t\t<Titre>{infos[0]}</Titre>\n\t\t<Réalisateur>{infos[1]}</Réalisateur>\n\t\t<Adresse>{infos[2]}</Adresse>\n\t\t<OrganismeDemandeur>{infos[3]}</OrganismeDemandeur>\n\t\t<TypeDeTournage>{infos[4]}</TypeDeTournage>\n\t\t<Arrondissement>{infos[5]}</Arrondissement>\n\t\t<DateDebut>{infos[6]}</DateDebut>\n\t\t<DateFin>{infos[7]}</DateFin>\n\t\t<xy>{infos[8]}</xy>')
            output.write('\n\t</tournage>\n')
            i= i+1

output.write('</tournages>')
output.close()