import csv

# -----------Choixpeau ai--------------
def open_csv(path):
    """retourne une nouvelle instance de 
    la base de donnée des élèves"""
    list_csv = []
    with open(path, 'r') as file:
        lec = csv.DictReader(file)
        for l in lec:
            list_csv.append(dict(l))
    return list_csv

def nbr_par_maisons(list_eleves):
    """retourne le nom des maisons et le nombre d'élèves par maison"""
    dic = {}
    for k in list_eleves:
        if k["Maison"] not in dic:
            dic[k["Maison"]] = 1
        else:
            dic[k["Maison"]] += 1
    return dic

def maison_majoritaire(list_eleves):
    """retourne le nom de la maison majoritaire"""
    a = nbr_par_maisons(list_eleves)
    maxi = 0
    rep = None
    for k in a:
        if a[k] > maxi:
            maxi = a[k]
            rep = k
    return rep

def distance_eleves(e1, e2):
    """retourne la distance de manhattan de 2 élèves"""
    return (abs(int(e2["Courage"])-int(e1["Courage"]))
    + abs(int(e2["Loyaute"])-int(e1["Loyaute"]))
    + abs(int(e2["Sagesse"])-int(e1["Sagesse"]))
    + abs(int(e2["Malice"])-int(e1["Malice"])))

def plus_proche_voisin(eleve, db, k = 7):
    """retourne une liste contenant les k plus proches
      élèves de la base de donnée d'un autres élèves donné
      selon l'algorithme de la distance de manhattan"""
    eleve_proche = None
    l = []
    for _ in range(k):
        dist = 999999
        for i in range(len(db)):
        # on boucle sur tous les élèves de la base
            dist2 = distance_eleves(eleve, db[i])
            if dist2 < dist and db[i] not in l:
            # on compare les distance à tous les élèves
            # on choisit le plus proche qui n'est pas déjà dans la liste
                dist = dist2
                eleve_proche = db[i]
        l.append(eleve_proche)
    return l

def attribution_maison(eleve, list_eleves):
    """retourne une maison pour un élève donné en paramètre"""
    voisin = plus_proche_voisin(eleve, list_eleves)
    maison = maison_majoritaire(voisin)
    return maison

# -------------test---------------
if __name__ == "__main__":
    db_path = "choixpeauMagique.csv"
    list_csv = open_csv(db_path)
    eleve = {'Nom': 'Elliot', 'Courage': '7', 'Loyaute': '9', 'Sagesse': '10', 'Malice': '4'}
    attribution_maison(eleve, list_csv)
