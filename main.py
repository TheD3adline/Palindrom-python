#   Author:     Michael Fessler
#   Data:       2022/09/28
#   Version:    0.1
#               Description placeholder
#
import palindrom

zahlen_liste = list()

while len(zahlen_liste) < 5:
    num = input("Bitte geben sie eine Zahl ein: ")
    if num.isdigit():
        zahlen_liste.append(num)
    elif not num.isdigit():
        print("Falsche Eingabe!")