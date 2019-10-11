# -*- coding: utf-8 -*-

from lxml import etree
xmlfile = "../exo-parser/valery_ame-et-danse_1921.xml"
tree = etree.parse(xmlfile)
root = tree.getroot()

TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE
# print(TEI) : {http://www.tei-c.org/ns/1.0}

print("Le nom de l'éditeur <edition> :")
for elt in root.iter(TEI + 'edition'):
    print(elt.text)

print("\nL'url de la licence <licence> :")
for elt in root.iter(TEI + 'licence'):
    #print(elt.attrib) # {'target': 'http://creativecommons.org/licenses/by-nc-nd/3.0/fr/'}
    print(elt.get('target'))

print("\nLe personnage avec le plus de réplique (@speaker), et le nombre de répliques :")
speaker={}
for elt in root.iter(TEI + 'label'):
    speaker[elt.text] = speaker.get(elt.text, 0) +1

max_speaker = max(speaker, key = speaker.get)
personnage = max_speaker
nombre = speaker[max_speaker]
print('{} : {}'.format(personnage, nombre))
# sorted(speaker.items(), key=lambda s: s[1], reverse=True)[0]
# (clé, valeur), on trie par la valeur donc s[1]
"""
# Une autre manière à faire :
speaker={}
for elt in root.iter(TEI + 'label'):
    if speaker.get(elt.text)==None :
        speaker[elt.text]=1
    else :
        speaker[elt.text]+=1
"""

# 4.Ajouter un autre <respStmt> avec deux enfants name et resp contenant du texte
for elt in root.iter(TEI + 'editionStmt'):
    ch = etree.SubElement(elt, 'respStmt')
    sub1 = etree.SubElement(ch, 'name')
    sub1.text = "something"
    sub2 = etree.SubElement(ch, 'resp')
    sub2.text = "anything"

print("\nModifier la valeur de la signature <signature> pour afficher le texte existant en majuscule :")
for elt in root.iter(TEI + 'signed'):
    for ch in elt:
        print(ch.text + " --> " + ch.text.upper())