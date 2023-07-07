import random

mots_liste= "sangle zombi croix rouge catastrophe gym chatouiller lucifer ardent librairie"
tableau_mots = mots_liste.split(" ")

index_mots = random.randint(0,len(tableau_mots)-1)
mot_choisi = tableau_mots[index_mots]

jeu_information = {
    'mot_choisi':mot_choisi,
    'mot_a_trouver':"_"*len(mot_choisi),
    'vie':10
}

print(f"Mot à trouver : {jeu_information['mot_a_trouver']}  Nombre d'essais : {jeu_information['vie']}")

while True:
    lettre = input('Entrer une lettre : ')
    if lettre in jeu_information['mot_choisi'] and lettre not in jeu_information['mot_a_trouver']:
        lettre_mot_a_trouver=list(jeu_information['mot_a_trouver'])
        for index, lettre_test in enumerate(jeu_information['mot_choisi']):
            if lettre_test == lettre:
                lettre_mot_a_trouver[index] = lettre
        jeu_information['mot_a_trouver'] = ''.join(lettre_mot_a_trouver)        
        print(f"Mot à trouver : {jeu_information['mot_a_trouver']} ")    
    elif lettre not in jeu_information['mot_choisi']:
        jeu_information['vie']-=1
        if jeu_information['vie'] > 1:
            print(f"Il vous reste {jeu_information['vie']} essais")
        elif jeu_information['vie'] == 1:
            print("Plus qu'un essai")
        else:
            print("Allez je vous accorde un dernier essai")
    
    print(f"Mot à trouver : {jeu_information['mot_a_trouver']} ")

    if jeu_information['vie'] < 0:
        print(f"Perdu le mot etait : {jeu_information['mot_choisi']}")
        break

    if "_" not in jeu_information['mot_a_trouver']:
        print("Bravo !! Vous avez trouver le mot secret !!!")
        break