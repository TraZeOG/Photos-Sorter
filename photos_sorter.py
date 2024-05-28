import os
import collections

domaines = [["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"],
            ["Photos 2016", "Photos 2017", "Photos 2018", "Photos 2019", "Photos 2020", "Photos 2021", "Photos 2022", "Photos 2023", "Photos 2024"]]


# - - - Création des différents dossiers - - - - - - - - - - - - - - - -
root_path = os.path.expanduser("~")
images_path = os.path.join(root_path, "Pictures\Photos triees")
for name in domaines[1]:
    dir_path = os.path.join(images_path, name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Create the "Autres" directory
autres_dir = os.path.join(images_path, "Autres")
if not os.path.isdir(autres_dir):
    os.mkdir(autres_dir)

# - - - tri des fichiers par extension - - - - - - - - - - - - - - - - -
file_mapping = collections.defaultdict(list)
file_list = os.listdir(images_path)
for name in file_list:
    if name[0] != ".":
        file_ext = name.split(".")[0]
        file_mapping[file_ext].append(name)


# - - - rangement dans les dossiers correspondant aux extensions - - - -
for ext, file_list in file_mapping.items():
    found_yet = False
    for index, domaine in enumerate(domaines[0]):
        if domaine in ext:
            found_yet = True
            for file in file_list:
                try:
                    os.rename(os.path.join(images_path, file), os.path.join(images_path, domaines[1][index], file))
                except:
                    print("Fin du tri par année")
    if not found_yet:
        for file in file_list:
            try:
                os.rename(os.path.join(images_path, file), os.path.join(autres_dir, file))
            except:
                print("Fin du tri par année")


annees = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

for annee in annees:

    domaines_bis = [[f"{annee}01", f"{annee}02", f"{annee}03", f"{annee}04", f"{annee}05", f"{annee}06", f"{annee}07", f"{annee}08", f"{annee}09", f"{annee}10", f"{annee}11", f"{annee}12"],
                [f"Janvier {annee}", f"Février {annee}", f"Mars {annee}", f"Avril {annee}", f"Mai {annee}", f"Juin {annee}", f"Juillet {annee}", f"Août {annee}", f"Septembre {annee}", f"Octobre {annee}", f"Novembre {annee}", f"Décembre {annee}"]]


    # - - - Création des différents dossiers - - - - - - - - - - - - - - - -
    root_path_bis = os.path.expanduser("~")
    images_path_bis = os.path.join(root_path, f"Pictures\Photos triees\Photos {annee}")
    for name in domaines_bis[1]:
        dir_path_bis = os.path.join(images_path_bis, name)
        if not os.path.isdir(dir_path_bis):
            os.mkdir(dir_path_bis)

    # Create the "Autres" directory
    autres_dir_bis = os.path.join(images_path_bis, "Autres")
    if not os.path.isdir(autres_dir):
        os.mkdir(autres_dir_bis)

    # - - - tri des fichiers par extension - - - - - - - - - - - - - - - - -
    file_mapping_bis = collections.defaultdict(list)
    file_list_bis = os.listdir(images_path_bis)
    for name in file_list_bis:
        if name[0] != ".":
            file_ext_bis = name.split(".")[0]
            file_mapping_bis[file_ext_bis].append(name)


    # - - - rangement dans les dossiers correspondant aux extensions - - - -
    for ext, file_list_bis in file_mapping_bis.items():
        found_yet_bis = False
        for index, domaine in enumerate(domaines_bis[0]):
            if domaine in ext:
                found_yet_bis = True
                for file in file_list_bis:
                    try:
                        os.rename(os.path.join(images_path_bis, file), os.path.join(images_path_bis, domaines_bis[1][index], file))
                    except:
                        print(f"Fin du tri par mois de l'année {annee}")
        if not found_yet_bis:
            for file in file_list:
                try:
                    os.rename(os.path.join(images_path_bis, file), os.path.join(autres_dir_bis, file))
                except:
                    print(f"Fin du tri par mois de l'année {annee}")