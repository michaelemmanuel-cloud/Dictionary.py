import tkinter as tk
from tkinter import messagebox

the_italian_dictionary = {
    'hello': 'ciao',
    'thank you': 'grazie',
    'friend': 'amico',
    'good morning': 'buongiorno ',
    'school': 'scuola',
    'book': 'libro',
    'cat': 'gatto',
    'dog': 'cane',
    'car': 'macchina',
    'eat': 'macchina',
    'drink': 'bere',
    'house': 'casa',
    'moon': 'luna',
    'sun': 'sole',
    'tree': 'albero',
    'flower': 'fiore',
    'sea': 'mare',
    'mountain': 'montagna',
    'city': 'città',
    'love': 'amore'
}
the_hausa_dictionary = {
    'water': 'ruwa',
    'food': 'Abinchi',
    'sheep': 'Rago',
    'dog': 'kare',
    'book': 'tarkada',
    'car': 'mota',
    'meat': 'nama',
    'shoe': 'talakami',
    'cloth': 'riga',
    'hair': 'Gashi',
    'chair': 'kujera',
    'school': "makaranta",
    'tea': "shayi",
    'father': "baba",
    'mother': "mama",
    'boy': "yaro",
    'doctor': "likita",
    'goat': "akwuiya",
    'music': "wakar",
    'bike': "keke"
}

the_igbo_dictionary = {
    'goat': 'ewu',
    'water': 'mmiri',
    'food': 'niri',
    'dog': 'nkita',
    'fish': 'azu',
    'mother': 'nne',
    'father': 'nna',
    'hello': 'kedu',
    'ogwu': 'medicine',
    'brother': 'nwanne',
    'cassava': "akpu",
    'basket': "okpu",
    'car': "ugbo",
    'meat': "anu",
    'medicine': "ogwu",
    'children': "umu",
    'quickly': "osiso",
    'house': "ulo",
    'book': "akwukwo",
    'salt': "okwo"
}
the_yoruba_dictionary = {
    'water': 'omi',
    'food': 'onuje',
    'mother': 'iya',
    'car': 'moto',
    'dog': 'aja',
    'brother': 'egbong',
    'father': 'baba',
    'sister': 'egbeyan',
    'house': 'lle',
    'hello': 'bawo',
    'child': 'omo',
    'cloth': "aso",
    'today': "oni",
    'husband': "oko",
    'wife': "aya",
    'tomorrow': "ola",
    'leg': "ese",
    'time': "akoko",
    'money': "owo",
    'fish': "eja"
}
the_spanish_dictionary = {
    'music': 'musica',
    'dog': 'perro',
    'house': 'casa',
    'food': 'comida',
    'hi': 'hola',
    'university': 'universidad',
    'mountain': 'montana',
    'fish': 'pescado',
    'flower': 'flor',
    'sun': 'sol',
    'love': 'amor',
    'friend': "amigo",
    'family': "familia",
    'cat': "gato",
    'happy': "feliz",
    'moon': "luna",
    'beach': "playa",
    'earth': "terria",
    'water': "",
    'work': "trabajo",
}
the_french_dictionary = {
    'house': 'maison',
    'school': 'ecole',
    'dog': 'chein',
    'food': 'nourriture',
    'beach': 'plage',
    'flower': 'fleur',
    'city': 'ville',
    'dream': 'reve',
    'hello': 'bonjour',
    'bakery': 'patisserie',
    'cat': 'chat',
    'friend': "ami",
    'book': "livre",
    'music': "musique",
    'earth': "terre",
    'moon': "lune",
    'son': "soleil",
    'bye': "au revoir",
    'happy': "heureux",
    'water': "eau"
}
the_german_dictionary = {
    'hello': 'hallo',
    'thank you': 'danke',
    'sister': 'schwester',
    'brother': 'bruda',
    'music': 'musik',
    'dog': 'hund',
    'flower': 'blume',
    'telephone': 'telefon',
    'chocolate': 'schokolade',
    'bread': 'brot',
    'sun': 'sonne',
    'moon': "mond",
    'beach': "strand",
    'happy': "glucklich",
    'food': "essen",
    'goodbye': "tschuss",
    'love': "liebe",
    'house': "haus",
    'water': "wasser",
    'clothes': "kleidung"
}
dictionaries = {
    "Italian dictionary": the_italian_dictionary,
    "Igbo dictionary": the_igbo_dictionary,
    "German dictionary": the_german_dictionary,
    "Yoruba dictionary": the_yoruba_dictionary,
    "French dictionary": the_french_dictionary,
    "Spanish dictionary": the_spanish_dictionary,
    "Hausa dictionary": the_hausa_dictionary,
}
root = tk.Tk()
root.title("Dictionary App")
root.geometry("500x400")

selected_dict = tk.StringVar()
word_input = tk.StringVar()

def get_meaning():
    word = word_input.get().strip().lower()
    dictionary_name = selected_dict.get()

    if dictionary_name in dictionaries and word in dictionaries[dictionary_name]:
        meaning = dictionaries[dictionary_name][word]
        result_label.config(text=f"Meaning of '{word}':\n{meaning}")

    else:
         result_label.config(text=f"sorry, the word '{word}'was not found in the selected dictionary.")

label = tk.Label(root, text="Choose a Dictionary:", font=("Arial", 18))
label.pack(pady=10)

dict_menu = tk.OptionMenu(root, selected_dict, *dictionaries.keys())
dict_menu.pack(pady=10)

word_label = tk.Label(root, text="Enter a word:", font=("Arial", 14))
word_label.pack(pady=10)

word_entry = tk.Entry(root, textvariable=word_input, font=("Arial", 16))
word_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Interpretation", font=("Arial", 14), command=get_meaning)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()