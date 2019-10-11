# -*- coding: utf-8 -*-
"""
Auteur : YU Xin
Date : 11/10/2019
"""

from lxml import etree
xmlfile = '../exo-parser/Duchn-etiquetage.txt.xml'
tree = etree.parse(xmlfile)

determinants = []
for elt in tree.xpath('//element/data'):
    if elt.get('type') == 'type' and "DET:" in elt.text:
        #print(elt.getnext().getnext().xpath('text()'))
        i = elt.getnext().getnext().xpath('text()')
        determinants += i

output = "exo5_determinants.txt"
with open(output,"w") as out:
    out.write(str(determinants))
print("Vous trouverez tous les déterminants dans le fichier {}".format(output))

print("\nAfficher les patrons DET - NOM :")
for elt in tree.xpath('//element'):
    if "DET:" in str(elt.xpath('./data[1]/text()')) and "NOM" in str(elt.getnext().xpath('./data[1]/text()')): 
        #print(str(elt.xpath('./data[3]/text()')) +' ' + str(elt.getnext().xpath('./data[3]/text()')))
        print("{} {}".format(elt.xpath('./data[3]/text()'), elt.getnext().xpath('./data[3]/text()')))

print("\nReconstruire les phrases (méthode 1):")
phrases = ""
for elt in tree.xpath('//element/data[3]'):
    # print(elt.text.encode('utf-8'))
    phrases += elt.text.encode('utf-8') + ' '
print(phrases)

print("\nReconstruire les phrases (méthode 2):")
phrase = ''
for elt in tree.xpath('//element'):
    for ch in elt:
        if ch.get('type') == 'string' :
            phrase += ch.text.encode('utf-8')+ ' '
        elif ch.text == "SENT":
            phrase += str(ch.getnext().getnext().text)+'\n'
            break
print(phrase)

print("\nTransformer l'affichage en : token/lemme/pos")
for elt in tree.xpath('//element/data[1]'):
    pos = elt.text
    lemme = elt.getnext().text.encode('utf-8')
    token = elt.getnext().getnext().text.encode('utf-8')
    print("{}/{}/{}".format(token,lemme,pos))