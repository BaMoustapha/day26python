import pandas

# Lire le fichier CSV contenant l'alphabet phonétique
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Convertir le DataFrame en dictionnaire
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Demander à l'utilisateur d'entrer un mot
word = input("Enter a word: ").upper()

# Générer la liste phonétique tout en gérant les erreurs si une lettre n'est pas dans le dictionnaire
try:
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
except KeyError as e:
    print(f"Le caractère '{e.args[0]}' n'est pas valide.")
