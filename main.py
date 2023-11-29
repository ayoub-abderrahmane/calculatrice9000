historique = []

while True:
    

    num1 = float(input("Entrez la première valeur : "))
    operateur1 = input("Entrez un opérateur : ")
    num2 = float(input("Entrez une seconde valeur : "))
    verification = input("Souhaitez-vous ajouter d'autres valeurs ? (oui/non): ")

    def calculer(operateur, num1, num2):
        if operateur == "+":
            return num1 + num2
        elif operateur == "-":
            return num1 - num2
        elif operateur == "*":
            return num1 * num2
        elif operateur == "%":
            return num1 % num2
        elif operateur == "/":
            if num2 != 0:
                return num1 / num2
            else:
                print("ERREUR, division par zéro")
                return None

    def calculer2(operateur1, num1, num2):
        operateur2 = input("Entrez un opérateur : ")
        num3 = float(input("Entrez une troisième valeur : "))

        resultat1 = calculer(operateur1, num1, num2)

        if resultat1 is not None:
            resultat_final = calculer(operateur2, resultat1, num3)
            if resultat_final is not None:
                historique.append(resultat_final)
                print(resultat_final)

    if verification == "non":
        resultat = calculer(operateur1, num1, num2)
        if resultat is not None:
            historique.append(resultat)
            print(resultat)
    elif verification == "oui":
        calculer2(operateur1, num1, num2)

    to_continue = input("Souhaitez vous continuez à faire des calculs ? (oui/non) : ")

    question = input("Souhaitez-vous afficher l'historique des résultats ? (oui/non) : ")

    if question == "oui":
        print(historique)

    if to_continue == "non":
        break
    


