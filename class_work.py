import tkinter as tk
from tkinter import messagebox


the_german_dictionary={
    'hallo': "hello",
    'danke': "thank you",
    'schwester': "sister",
    'bruda': "brother",
    'musik': "music",
    'hund': "dog",
    'blume': "flower",
    'telefon': "telephone",
    'schokolade': "chocolate",
    'brot': "bread",
    'sonne': "sun",
    'mond': "moon",
    'strand': "beach",
    'glucklich': "happy",
    'essen': "food",
    'tschuss': "goodbye",
    'liebe': "love",
    'haus': "house",
    'wasser': "water",
    'kleidung': "clothes"
}
the_hausa_dictionary = {
    'ruwa': "water",
    'Abinchi': "food",
    'Rago': "Sheep",
    'tarkada': "book",
    'Kare': "dog",
    'mota': "car",
    'Nama': "meat",
    'talakami': "shoe",
    'riga': "clothe",
    'Gashi': "hair",
    'kujera': "chair",
    'makaranta': "school",
    'shayi': "tea",
    'baba': "father",
    'mama': "mother",
    'yaro': "boy",
    'likita': "doctor",
    'akwuiya': "goat",
    'wakar': "music",
    'keke': "bike"
}
the_igbo_dictionary= {
    'ewu': "goat",
    'mmiri': "water",
    'niri': "food",
    'nkita': "dog",
    'azu': "fish",
    'nne': "mother",
    'nna': "father",
    'kedu': "hello",
    'ari': "food",
    'nwanne': "brother",
    'akpu': "cassava",
    'okpu': "basket",
    'ugbo': "car",
    'anu': "meat",
    'ogwu': "medicine",
    'umu': "children",
    'osiso': "quickly",
    'ulo': "house",
    'akwukwo': "book",
    'okwo': "salt"
}
the_yoruba_dictionary={
    'omi': "water",
    'onuje': "food",
    'iya': "mother",
   'moto': "car",
    'aja': "dog",
    'egbong': "brother",
    'baba': "father",
    'egbeyan': "sister",
    'lle': "house",
    'bawo': "hello",
    'omo': "child",
    'aso': "cloth",
    'oni': "today",
    'oko': "husband",
    'aya': "wife",
    'ola': "tomorrow",
    'ese': "leg",
    'akoko': "time",
    'owo': "money",
    'eja': "fish"
}
the_spanish_dictionary={
    'musica': "music",
    'perro': "dog",
    'casa': "house",
    'comida': "food",
    'hola': "hi",
    'universidad': "university",
    'montana': "mountain",
    'pescado': "fish",
    'flor': "flower",
    'sol': "sun",
    'amor': "love",
    'amigo': "friend",
    'familia': "family",
    'gato': "cat",
    'feliz': "happy",
    'luna': "moon",
    'playa': "beach",
    'terria': "earth",
    'agua': "water",
    'trabajo': "work",

}
the_french_dictionary={
    'maison': "house",
    'ecole': "school",
    'chien': "dog",
    'nourriture': "food",
    'plage': "beach",
    'fleur': "flower",
    'ville': "city",
    'reve': "dream",
    'bonjour': "hello",
    'patisserie': "bakery",
    'chat': "cat",
    'ami': "friend",
    'livre': "book",
    'musique': "music",
    'terre': "earth",
    'lune': "moon",
    'soleil': "sun",
    'au revoir': "bye",
    'heureux': "happy",
    'eau': "water"
}

dictionaries ={
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
        meaning = dictionariees[dictionary_name][word]
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
