import random

from tableaux.hiragana import hiragana
from tableaux.katakana import katakana
from tableaux.kanji_N5 import kanji

def parcourirTableau(tableau):
    kana_choisi = random.choice(list(tableau.keys()))

    return kana_choisi

def poserQuestion(score, kana_choisi, tableau):

    sens_question = random.choice(["caractère japonais", "romaji"])
    nb_indices = 3
    indices = []

    if sens_question == "romaji":
        # Demander le romaji
        
        print(f"Quel le romaji de {kana_choisi} ? ")
          
        indices = random.sample(list(tableau.values()), nb_indices - 1)
        indices.append(tableau[kana_choisi])
        bonne_reponse = tableau[kana_choisi]
        
    else:
        # Demander le caractère japonais

        print(f"Quel le caractère japonais de {tableau[kana_choisi]} ? ")
                  
        indices = random.sample(list(tableau), nb_indices - 1)
        indices.append(kana_choisi)
        bonne_reponse = kana_choisi

    random.shuffle(indices)
    print(indices)

    reponse = input("Votre réponse : ")

    print()
    if reponse.strip().lower() == bonne_reponse.lower():
        print(f"Bravo, la réponse était bien {bonne_reponse}")
        score += 1
    else:
        print(f"Dommage, la réponse était {bonne_reponse}")
    print()

    return score

# Mettre ** permet de copier des dictionnaires et de les fusionner entre eux
kana = {**hiragana, **katakana}

# print(hiragana, katakana, kana)

# pays_restants = pays.copy()

tableau = {}

print("Que voulez-vous travailler aujourd'hui ?")
print("A : Hiragana")
print("B : Katakana")
print("c : Kana (les deux à la fois)")
reponse = input("Votre réponse : ")

if reponse.strip().lower() == "a":
    reponse = "hiragana"
    tableau = hiragana

elif reponse.strip().lower() == "b":
    reponse = "katakana"
    tableau = katakana

elif reponse.strip().lower() == "c":
    tableau = kana

elif reponse.strip().lower() == "d":
    tableau = kanji

else:
    reponse = input("Veuillez marquer une nouvelle réponse")

print()
print("Combien de questions voulez-vous faire ? ")
nb_questions = int(input("Votre réponse : "))

if nb_questions > len(tableau):
    nb_questions = len(tableau)

question = 1
score = 0
tableau_restant = tableau.copy()

while question <= nb_questions and len(tableau_restant) > 0:

    print()
    print(f"Question {question} :")

    kana_choisi = parcourirTableau(tableau_restant)

    score = poserQuestion(score, kana_choisi, tableau)

    del tableau_restant[kana_choisi]

    question += 1

print(f"Vous avez fait un score de {score}/{nb_questions}")