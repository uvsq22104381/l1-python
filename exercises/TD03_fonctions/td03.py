#Td03

#création d'une fonction donnant le temps, saisi par l'utilisateur, en seconde
#le temps prendra comme forme : temps[0] : jours, temps[1]: heures, temps[2]: minutes, 
#temps[3]: secondes

date = [10,5,56,45]

def tempsEnSeconde(temps) :
    seconde = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return seconde



print(tempsEnSeconde(date), "secondes")



#création d'une fonction donnant les secondes, saisis par l'utilisateur, en temps

secondes = 4500

def secondeEnTemps(seconde) :
    minute = seconde // 60
    seconde %= 60
    heure = minute // 60
    minute %= 60
    jour = heure // 24
    heure %= 24
    return (jour, heure, minute, seconde)

print(secondeEnTemps(secondes))
