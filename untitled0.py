# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 11:46:44 2023

@author: bryso
"""

import tkinter as tk
from tkinter import messagebox
import random

class PokemonCard:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class PokemonGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.cards = [
            PokemonCard("Pikachu", 30),
            PokemonCard("Charizard", 50),
            PokemonCard("Bulbasaur", 20),
            # Add more Pokémon cards as needed
        ]
        self.current_card = None
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Endless Pokemon Card Game")

        self.player_score_label = tk.Label(self.root, text="Your Score: 0")
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0")
        self.computer_score_label.pack()

        self.draw_button = tk.Button(self.root, text="Draw Card", command=self.draw_card)
        self.draw_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

    def draw_card(self):
        self.current_card = random.choice(self.cards)
        self.show_card_dialog()

    def show_card_dialog(self):
        result = messagebox.askyesno("Pokemon Card", f"You drew {self.current_card.name}. Do you want to battle?")
        if result:
            self.battle()

    def battle(self):
        computer_card = random.choice(self.cards)
        result = self.compare_cards(self.current_card, computer_card)

        if result == "win":
            self.player_score += 1
        elif result == "lose":
            self.computer_score += 1

        self.update_scores()

    def compare_cards(self, player_card, computer_card):
        if player_card.damage > computer_card.damage:
            return "win"
        elif player_card.damage < computer_card.damage:
            return "lose"
        else:
            return "draw"

    def update_scores(self):
        self.player_score_label.config(text=f"Your Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

if __name__ == "__main__":
    game = PokemonGame()
    game.root.mainloop()
