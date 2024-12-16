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
word = input('Enter a hausa word')
 if word in the_hausa_dictionary:
   print('it translates to',the_hausa_dictionary[word])
else:
     print('this word is not yet in the hausa dictionary')

       

