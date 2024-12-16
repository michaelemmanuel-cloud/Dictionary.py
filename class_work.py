 import tkinter as tk
from tkinter import ttk


the_hausa_dictionary = {
    'ruwa': 'water',
    'Abinchi':'food',
    'Rago':'Sheep',
    'Kare':'dog',
    'tarkada':'book',
    'mota': 'car',
    'Nama': 'meat',
    'talakami':'shoe',
    'riga':'clothe',
    'Gashi':'hair',
    'kujera':'chair',
    'makaranta':'school',
    'shayi':'tea',
    'baba':'father',
    'mama':'mother',
    'yaro':'boy',
    'likita':'doctor',
    'akwuiya':'goat',
    'wakar':'music',
    'keke':'bike'
}
the_igbo_dictionary= 
    'ewu': 'goat',
    'mmiri': 'water',
    'niri': 'food',
    'nkita':'dog',
    'azu':'fish',
    'nne':'mother',
    'nna':'father',
    'kedu':'hello',
    'ari':'food',
    'nwanne':'brother',
    'akpu':'cassava',
    'okpu':'basket',
    'ugbo':'car',
    'anu':'meat',
    'ogwu':'medicine',
    'umu':'children',
    'osiso':'quickly',
    'ulo':'house',
    'akwukwo':'book',
    'okwo':'salt'
}
the_yoruba_dictionary={
    'omi':'water',
    'onuje':'food',
    'iya':'mother',
   'moto':'car',
    'aja':'dog',
    'egbong':'brother',
    'baba':'father',
    'egbeyan':'sister',
    'lle':'house',
    'bawo':'hello',
    'omo':'child',
    'aso':'cloth',
    'oni':'today',
    'oko':'husband',
    'aya':'wife',
    'ola':'tomorrow',
    'ese':'leg',
    'akoko':'time',
    'owo':'money',
    'eja':'fish'
}
 the_spanish_dictionary={
    'musica':'music',
    'perro':'dog',
    'casa':'house',
    'comida':'food',
    'hola':'hi',
    'universidad':'university',
    'montana':'mountain',
    'pescado':'fish',
    'flor': 'flower',
    'sol':'sun',
    'amor':'love',
    'amigo':'friend',
    'familia':'family',
    'gato':'cat',
    'feliz':'happy',
    'luna':'moon',
    'playa':'beach',
    'terria':'earth',
    'agua':'water',
    'trabajo':'work',

}
 the_french_dictionary={
    'maison':'house',
    'ecole':'school',
    'chien':'dog',
    'nourriture':'food',
    'plage':'beach',
    'fleur':'flower',
    'ville':'city',
    'reve':'dream',
    'bonjour':'hello',
    'patisserie':'bakery',
    'chat':'cat',
    'ami':'friend',
    'livre':'book',
    'musique':'music',
    'terre':'earth',
    'lune':'moon',
    'soleil':'sun',
    'heureux':'happy',
    'au revoir':'bye',
    'eau':'water'

}
 the_german_dictionary={
    'hallo':'hello',
    'danke':'thank you',
    'schwester':'sister',
    'bruda':'brother',
    'musik':'music',
    'hund':'dog',
    'blume':'flower',
    'telefon':'telephone',
    'schokolade':'chocolate',
    'brot':'bread',
    'sonne':'sun',
    'mond':'moon',
    'strand':'beach',
    'glucklich':'happy',
    'essen':'food',
    'tschuss':'goodbye',
    'liebe':'love',
    'haus':'house',
    'wasser':'water',
    'kleidung':'clothes'
}
def search_word(dictionary):
    word = entry.get().lower()
    if word in dictionary:
        result_label.config(text=dictionary[word])
    else:
        result_label.config(text='word not found')

root = tk.tk()
root.title('The Sigma dictionary')

entry = ttk.entry(root,width=40)
entry.grid(row=0, column=0, padx=10, pady=0)

ttk.Button(root, text='search hausa', command=lambda: search_word(the_hausa_dictionary)).grid(row=0, column=1, pady=10, padx=10)
ttk.Button(root, text='search igbo',command=lambda: search_word(the_igbo_dictionary)).grid(row=0, column=2, pady=10, padx=10)
ttk.Button(root, text='search yoruba', command=lambda : search_word(the_yoruba_dictionary)).grid(row=0, column=3, pady=10, padx=10)
ttk.Button(root, text='search french',command=lambda :search_word(the_french_dictionary)).grid(row=0, column=4, pady=10, padx=10)
ttk.Button(root, text='search spanish', command=lambda: search_word(the_spanish_dictionary)).grid(row=0, column=5, pady=10, padx=10)

       

