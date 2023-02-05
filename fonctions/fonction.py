import csv

test_E = "data_test/PV/E/2020_installations_sportives.csv"
test_S = "data_test/PV/S/2020_installations_sportives_test.csv"

test_E1 = "data_test/V/E/2021-parcoursup-toulouse.csv"
test_S1 = "data_test/V/S/2021-parcoursup-toulouse_test.csv"

test_E2 = "data_test/V/E/2012-London-Ind.csv"
test_S2 = "data_test/V/S/2012-London-Ind_test.csv"

test_E3 = "data_test/V/E/2022-premiertour-toulouse.csv"
test_S3 = "data_test/V/S/2022-premiertour-toulouse_test.csv"

test_E4 = "data_test/V/E/yelp-delaware.csv"
test_S4 = "data_test/V/S/yelp-delaware_test.csv"

test_E5 = "data_test/PV/E/2018-associations-et-clubs-sportifs.csv"
test_S5 = "data_test/PV/S/2018-associations-et-clubs-sportifs_test.csv"

test_E6 = "data_test/PV/E/2020_installations_sportives.csv"
test_S6 = "data_test/PV/S/2020_installations_sportives_test.csv"

test_E7 = "data_test/PV/E/2018-licencies-sportifs-yvelines.csv"
test_S7 = "data_test/PV/S/2018-licencies-sportifs-yvelines_test.csv"

test_E8 = "data_test/PV/E/2015-sportifs-haut-niveau.csv"
test_S8 = "data_test/PV/S/2015-sportifs-haut-niveau_test.csv"

test_E9 = "data_test/V/E/films_hk.csv"
test_S9 = "data_test/V/S/films_hk_test.csv"

test_E10 = "data_test/V/E/star_trek.csv"
test_S10 = "data_test/V/S/star_trek_test.csv"

test_E11 = "data_test/V/E/series_latines.csv"
test_S11 = "data_test/V/S/series_latines_test.csv"

test_E12 = "data_test/V/E/parodies_simpson.csv"
test_S12 = "data_test/V/S/parodies_simpson_test.csv"



"""
# ------ chemin des fichier.csv  ------
data_csv = "C:/Users/Andrew/PycharmProjects/ProjetData/Test/data_test/2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
admissions_par_formation_detaillee_csv = "C:/Users/Andrew/PycharmProjects/ProjetData/Test/data_test/AdmissionParFormationDetaillee.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "C:/Users/Andrew/PycharmProjects/ProjetData/Test/data_test/CommunesUniques.csv"

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
installations_uniques_csv = "C:/Users/Andrew/PycharmProjects/ProjetData/Test/data_test/IntallationsUniques.csv"
"""

# ------ Fonction -------

# ----- Fonction esthétique / grap -----

def space_graph(valeur):
    for i in range(valeur):
        print("")


# ------ Fonction Lecture du fichier.csv ------

# fonction lecture de fichier CSV avec en paramètres le nom du fichier.csv
def lecture_csv(nom_fichier_csv):
    # Ouverture d'un fichier csv avec en paramètres un mode "r" read = lecture
    with open(nom_fichier_csv, errors="ignore") as csv_file:
        # Lecture du fichier csv
        csv_reader = csv.reader(csv_file)
        # Boucle pour lire le fichier csv
        for line in csv_reader:
            # Affichage de la ligne lu
            print(line)


# ------   Fontion Écriture du fichier.csv   -------

# fonction écriture de fichier CSV avec en paramètre le nom du fichier.cvs et l'en tête

def ecriture_csv(nom_fichier_csv, header, data):
    # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
    with open(nom_fichier_csv, "w", newline="") as csv_file:
        # Écriture du fichier csv avec un paramètre un delimitation par le ";"
        writer = csv.writer(csv_file, delimiter=";")
        # Écriture de l'en tête du fichier csv
        writer.writerow(header)
        # Écriture du fichier.csv
        writer.writerow(data)  # test ecriture dans le fichier csv


# ----   fichier.csv en liste  --------

def csv_en_liste_v2(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)

    return (lignes[valeur_ligne][valeur_valeur])


def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer):
    donnees = []
    with open(nom_fichier_entree, 'r', errors="ignore") as fichier_entree:
        reader = csv.reader(fichier_entree)
        for ligne in reader:
            donnees.append(ligne)

    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie)
        for ligne in donnees:
            colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
            writer.writerow(colonnes_selectionnees)

