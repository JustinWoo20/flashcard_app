from flashcard_ui import UserInterface
from flashcard_engine import MakeFlashcards
from word_list import WordList

ui = UserInterface()
word_data = WordList()
logic = MakeFlashcards(ui, word_data.words_dict, word_data.known_words)

ui.right_button.config(command=logic.mark_correct)
ui.wrong_button.config(command=logic.generate_word)

ui.window.mainloop()






