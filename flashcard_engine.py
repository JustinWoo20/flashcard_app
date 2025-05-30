import random
import pandas
from word_list import language

class MakeFlashcards:
    def __init__(self, ui, words_dict, known_words):
        self.ui=ui
        self.words_dict = words_dict
        self.known_words = known_words
        self.correct_words = []
        self.current_word = {}
        self.timer = None
        self.generate_word()

    def generate_word(self):
        if self.timer:
            self.ui.window.after_cancel(self.timer)
        self.ui.canvas.itemconfig(self.ui.current_side, image=self.ui.flashcard_front)
        random_set = random.choice(self.words_dict)
        self.current_word = random_set
        self.ui.canvas.itemconfig(self.ui.card_title, text=language, fill="black")
        self.ui.canvas.itemconfig(self.ui.card_word, text=random_set[language], fill="black")
        self.timer = self.ui.window.after(3000, self.flip_card)

    def flip_card(self):
        self.ui.canvas.itemconfig(self.ui.card_title, text="English", fill="white")
        self.ui.canvas.itemconfig(self.ui.card_word, text=self.current_word["English"], fill="white")
        self.ui.canvas.itemconfig(self.ui.current_side, image=self.ui.flashcard_back)

    def mark_correct(self):
        self.correct_words.append(self.current_word)
        total_known_words = self.known_words + self.correct_words
        pandas.DataFrame(total_known_words).drop_duplicates().to_csv(f"flashcard_data_{language}/{language} Known Words.csv", index=False)
        self.generate_word()