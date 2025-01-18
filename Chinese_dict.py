import tkinter as tk
from tkinter import messagebox


class ChineseDictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Chinese  Dictionary")


        self.chinese_dict = {
            "please": "qing",
            "hello": "ni hao",
            "thank you": "xie xie",
            "goodbye": "zai jian",
            "friend": "peng you",
            "love": "ai",
            "family": "jia ting",
            "happy": "kuai le",
            "beautiful": "mei li",
            "teacher": "lao shi",
        }


        tk.Label(root, text="Enter English Word:").grid(row=0, column=0, padx=10, pady=5)
        self.input_entry = tk.Entry(root, width=30)
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)


        tk.Button(root, text="Translate", command=self.translate_word).grid(row=1, column=0, columnspan=2, pady=5)


        tk.Label(root, text="Chinese Translation:").grid(row=2, column=0, padx=10, pady=5)
        self.result = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result, font=("Arial", 14), fg="blue")
        self.result_label.grid(row=2, column=1, padx=10, pady=5)

    def translate_word(self):
        """
        
        """
        english_word = self.input_entry.get().strip().lower()  # Convert to lowercase for case-insensitive search

        if not english_word:
            messagebox.showwarning("Input Error", "Please enter an English word to translate.")
            return

        if english_word in self.chinese_dict:
            self.result.set(self.chinese_dict[english_word])
        else:
            self.result.set("Translation not found.")  # Handle unknown words



if __name__ == "__main__":
    root = tk.Tk()
    app = ChineseDictionaryApp(root)
    root.mainloop()
