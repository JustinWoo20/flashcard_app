import pandas
from tkinter import messagebox

language = "Japanese"

class WordList:
    def __init__(self, word_list_path=f"flashcard_data_{language}/{language} Word List.csv",
                 known_words_path=f"flashcard_data_{language}/{language} Known Words.csv"):
        self.word_list_path = word_list_path
        self.known_words_path = known_words_path
        # Load word list
        self.words_to_learn = pandas.read_csv(self.word_list_path)
        self.words_dict = self.words_to_learn.to_dict("records")
        # Load known words if studied before
        try:
            known_words_df = pandas.read_csv(self.known_words_path)
            self.known_words = known_words_df.to_dict("records")
        except FileNotFoundError:
            self.known_words = []
        # Filter out known words
        self.words_dict = [word for word in self.words_dict if word not in self.known_words]

        if not self.words_dict:
            messagebox.showinfo("Congratulations", "You've learned all the words!")
