num1 = float(input("Entrez la première valeur : "))
opérateur1 = input ("Entrez un opérateur : ")
num2 = float(input ("Entrez une seconde valeur : "))
vérification = input ("Souhaitez-vous ajoutez d'autres valeur ? (oui/non): ")

def calcule():
    if opérateur1 == "+":
       résultat = num1 + num2
       print (résultat)
    elif opérateur1 == "-":
       résultat = num1 - num2
       print (résultat)
    elif opérateur1 == "*":
       résultat = num1 * num2
       print (résultat)
    elif opérateur1 == "%":
       résultat = num1 % num2
       print (résultat)
    elif opérateur1 == "/":
       if num2 != 0:
         résultat = num1 / num2
         print (résultat)
    else:
       print ("ERREUR , division par zéro")
       
if vérification == "non":
   calcule()
elif vérification == "oui":
   def calcule2 ():
      opérateur2 = input ("Entrez un opérateur : ")
      num3 = float(input("Entrez une troisième valeur : "))
      if opérateur1 == "+" and opérateur2 == "+":
       résultat = num1 + num2 + num3
       print (résultat)
      if opérateur1 == "+" and opérateur2 == "-":
       résultat = num1 + num2 - num3
       print (résultat)
      if opérateur1 == "+" and opérateur2 == "*":
       résultat = num1 + num2 * num3
       print (résultat)
      if opérateur1 == "+" and opérateur2 == "/":
       résultat = num1 + num2 / num3
       print (résultat)
      elif opérateur1 == "-" and opérateur2 == "-":
       résultat = num1 - num2 - num3
       print (résultat)
      elif opérateur1 == "-" and opérateur2 == "+":
       résultat = num1 - num2 + num3
       print (résultat)
      elif opérateur1 == "-" and opérateur2 == "*":
       résultat = num1 - num2 * num3
       print (résultat)
      elif opérateur1 == "-" and opérateur2 == "/":
       résultat = num1 - num2 / num3
       print (résultat)
      elif opérateur1 == "*" and opérateur2 == "*":
       résultat = num1 * num2 * num3
       print (résultat)
      elif opérateur1 == "*" and opérateur2 == "+":
       résultat = num1 * num2 + num3
       print (résultat)
      elif opérateur1 == "*" and opérateur2 == "-":
       résultat = num1 * num2 - num3
       print (résultat)
      elif opérateur1 == "*" and opérateur2 == "/":
       résultat = num1 * num2 / num3
       print (résultat)
      elif opérateur1 == "/" and opérateur2 == "*":
       résultat = num1 / num2 * num3
       print (résultat)
      elif opérateur1 == "%" and opérateur2 == "%":
       résultat = num1 % num2 % num3
       print (résultat)
      elif opérateur1 == "/" and opérateur2 == "/":
        if num2 != 0:
         résultat = num1 / num2 / num3
         print (résultat)
        else:
         print ("ERREUR , division par zéro")
      elif opérateur1 == "/" and opérateur2 == "+":
        if num2 != 0:
         résultat = num1 / num2 + num3
         print (résultat)
        else:
         print ("ERREUR , division par zéro")
      elif opérateur1 == "/" and opérateur2 == "-":
        if num2 != 0:
         résultat = num1 / num2 - num3
         print (résultat)
        else:
         print ("ERREUR , division par zéro")

      calcule2 ()