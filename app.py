# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:17:11 2023

@author: lEO
"""

import time
import pandas as pd
import random
import matplotlib.pyplot as plt
import streamlit as st
import streamlit_card as sc
import streamlit_vertical_slider as svs
import streamlit_option_menu as sto
import streamlit_extras as se
import streamlit_lottie as slo
import base64

class Game:
    def __init__(self):
        pass
    
    def generated_num(self):
        self.generated_number = random.randint(1000, 9999)
        return self.generated_number
    

class Action:
    def __init__(self):
        self.__points = 0
        self.generated_number_rounds = {}
        self.store = []
        self.point_from_round = []
        self.total_points_gotten = []
        self.number = 0
        
    def counting_bulls(self):
        self.y = 0
        self.number_bulls = 0
        while self.y < 4:
            self.number = str(self.number)
            self.generated_number = str(self.generated_number)
            
            if self.number[self.y] == self.generated_number[self.y]:
                self.number_bulls += 1
            self.y += 1
        return self.number_bulls
            
    def counting_cows(self):
        self.x = 0
        self.number_cows = 0
        while self.x < 4:
            self.number = str(self.number)
            self.generated_number = str(self.generated_number)
            
            if self.number[self.x] == self.generated_number[0]:
                if self.x == 0:
                    pass
                else:
                    self.number_cows += 1 
            if self.number[self.x] == self.generated_number[1]:
                if self.x == 1:
                    pass
                else:
                    self.number_cows += 1       
            if self.number[self.x] == self.generated_number[2]:
                if self.x == 2:
                    pass
                else:
                    self.number_cows += 1     
            if self.number[self.x] == self.generated_number[3]:
                if self.x == 3:
                    pass
                else:
                    self.number_cows += 1
            self.x += 1
            if self.x == 4:
                return self.number_cows
                break
        
    
    def calculating_bulls_cows(self):
        self.bulls_points = 2
        self.cows_points = 1
        self.round_points = (self.number_bulls * self.bulls_points) + (self.number_cows * self.cows_points)
        self.point_from_round.append(self.round_points)
        self.__points += self.round_points
        self.total_points_gotten.append(self.__points)
        return self.round_points
        
    def store_data(self, x):
        self.x = x
        if self.x in self.store:
            self.x += 1
            self.store.append(self.x)
            self.generated_number_rounds[self.x] = {}
            self.generated_number_rounds[self.x]['Bulls'] = self.number_bulls
            self.generated_number_rounds[self.x]['Cows'] = self.number_cows
            self.generated_number_rounds[self.x]['Points_For_Round'] = self.round_points
            self.generated_number_rounds[self.x]['Total_Points_Accumulated'] = self.__points
            self.generated_number_rounds[self.x]['Guessed'] = self.number
            self.generated_number_rounds[self.x]['Game_Generated'] = self.generated_number
        else:
            self.store.append(self.x)
            self.generated_number_rounds[self.x] = {}
            self.generated_number_rounds[self.x]['Bulls'] = self.number_bulls
            self.generated_number_rounds[self.x]['Cows'] = self.number_cows
            self.generated_number_rounds[self.x]['Points_For_Round'] = self.round_points
            self.generated_number_rounds[self.x]['Total_Points_Accumulated'] = self.__points
            self.generated_number_rounds[self.x]['Guessed'] = self.number
            self.generated_number_rounds[self.x]['Game_Generated'] = self.generated_number
        return self.generated_number_rounds
    
    def get_data(self):
        self.generated_number_rounds = pd.DataFrame(self.generated_number_rounds)
        return self.generated_number_rounds
    
    def get_points_rounds(self):
        return self.round_points
    
    def total_points_from_rounds(self):
        return self.__points
    
    def graph_round_points(self, list_of_rounds):
        self.round_game = list_of_rounds
        plt.figure(figsize = (10, 5))
        plt.bar(self.round_game, self.point_from_round,  color = 'maroon', width = 0.4)
        plt.xlabel('Number of Rounds')
        plt.ylabel('Points per Round')
        plt.title(f'{self.name} graphs of points from each round')
        plt.show()
    
    def graph_for_totalpoints(self, list_of_rounds):
        self.round_game = list_of_rounds
        plt.figure(figsize = (10, 5))
        plt.bar(self.round_game, self.total_points_gotten,  color = 'maroon', width = 0.4)
        plt.xlabel('Number of Rounds')
        plt.ylabel('Total Points in Game')
        plt.title(f'{self.name} graphs of total points accumulated')
        plt.show()
        

class Player(Action):
    def __init__(self, name):
        self.name = name
        self.__database = {'name': self.name}
        super().__init__()
        
    def guess_number(self, number):
        if number > 9999 and number < 1000 :
            print('Invalid Response. Insert a 4 digit number')
        else:
            self.number = int(number)
            return self.number
    
    def get_generated_number(self, num):
        self.generated_number = num
    
class AI(Action):
    def __init__(self):
        self.name = 'Enoch'
        super().__init__()
    
    def ai_guess(self):
        self.number = random.randint(1000, 9999)
        return self.number
        
    def get_generated_number(self, num):
        self.generated_number = num
    
    
# # Program Begins 
# print('GAME-TIME: ' + time.ctime())
# while True:
#     try:
#         print('\nWelcome to BULLS & COWS.\n    C R E A T O R: Onyiriuba Leonard\nThe rules of the game are simple\n\nRULE 1: You are to guess a 4 digit number\nRULE 2: Bulls are gotten when you match the exact location of your guessed number with the location of the numbers the game generates\nRULE 3: Cows are gotten if the number we guess exists in the number that is generated.\nRULE 4: ZERO(0) should not start your guess e.g Guessing a 4 digit number as 0786 or 0234. These are 3 digits represented as 786 and 234\n\n')
#         proceed = int(input('Press 1: Proceed\nPress 2: Exit\nRESPONSE: ')) 
#         if proceed == 1:
#             while True:
#                 try:
#                     question = int(input('\nPress 1: One Player\nPress 2: Two Player\nPress 3: Specify the number of players\nPress 4: Exit\nRESPONSE: '))
#                     if question == 4:
#                         while True:
#                             try:
#                                 flag = False
#                                 switch = False
#                                 main_menu = int(input('Press 0: Previous Menu\nPress 1: Main Menu\nPress 2: Exit\nRESPONSE: '))
#                                 if main_menu == 0:
#                                     break
#                                 elif main_menu == 1:
#                                     flag = True
#                                     switch = False
#                                     break
#                                 elif main_menu == 2:
#                                     switch = True
#                                     flag = False
#                                     break                        
#                             except ValueError:
#                                 print('\nInvalid Response. Insert 1 or 2\n')
#                                 continue                        
#                     elif question == 3:
#                         x = 1
#                         num_of_rounds = []
#                         number = int(input('INDICATE THE NUMBER OF PLAYERS: '))
#                         if number == 1:
#                             x = 1
#                             game = Game()
#                             human = Player(input('Name: '))
#                             ai = AI()
#                             while True:
#                                 gen_num = game.generated_num()
                                
#                                 get_gen_human = human.get_generated_number(gen_num)
#                                 get_gen_ai = ai.get_generated_number(gen_num)
                                             
#                                 print(f'\n\nBEAT THE AI\n    R O U N D   {x}') 
#                                 my_guess = human.guess_number(int(input('PLAYERS MOVE: \nGuess a 4 digit number: ')))
#                                 ai_guess = ai.ai_guess()
                                
#                                 my_bulls = human.counting_bulls()
#                                 ai_bulls = ai.counting_bulls()
#                                 my_cows = human.counting_cows()
#                                 ai_cows = ai.counting_cows()
                                
#                                 my_calc = human.calculating_bulls_cows()
#                                 ai_calc = ai.calculating_bulls_cows()
                                
#                                 my_store = human.store_data(x)
#                                 ai_store = ai.store_data(x)
#                                 print(f'\n    ** GENERATED NUMBER: {gen_num}\n\n    ** Your Guess: {my_guess}\n    ** AI Guess: {ai_guess}\n')
                                
#                                 n = zip(my_store[x].values(), ai_store[x].values())
#                                 player1 = human.name
#                                 player2 = ai.name
#                                 bulls, cows, round_points, points, guess, game_guess = n
#                                 if round_points[0] > round_points[1]:
#                                     print(f'- The winner of this round is {player1} -')
#                                     print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                     print('')
#                                     print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                     print('')
#                                     print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                                 elif round_points[0] < round_points[1]:
#                                     print('- AI wins this round -')
#                                     print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                     print('')
#                                     print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                     print('')
#                                     print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                                 elif round_points[0] == round_points[1]:
#                                     print('- This round is a draw -')
#                                     print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                     print('')
#                                     print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                     print('')
#                                     print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                                 else:
#                                     raise ValueError
                                
#                                 x = x + 1                            
#                                 try:
#                                     flag = False
#                                     switch = False
#                                     main_menu = int(input('Press 0: Previous Menu\nPress 1: Main Menu\nPress 2: Exit\nPress 3: Play Another Round\nRESPONSE: '))
#                                     if main_menu == 0:
#                                         if points[0] > points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print(f'- OUR GUESS CHAMPION is {player1} -')
                                            
#                                         elif points[0] < points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- OUR GUESS CHAMPION is AI Enoch-')
                                            
#                                         elif points[0] == points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                         break
#                                     elif main_menu == 1:
#                                         flag = True
#                                         if points[0] > points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print(f'- OUR GUESS CHAMPION is {player1} -')
                                            
#                                         elif points[0] < points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- OUR GUESS CHAMPION is AI Enoch-')
                                            
#                                         elif points[0] == points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                         else:
#                                             raise ValueError
#                                         break
#                                     elif main_menu == 2:
#                                         switch = True
#                                         if points[0] > points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print(f'- OUR GUESS CHAMPION is {player1} -')
                                            
#                                         elif points[0] < points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- OUR GUESS CHAMPION is AI Enoch-')
                                            
#                                         elif points[0] == points[1]:
#                                             print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                             print("\n\n- S T A T S -")
#                                             print(f'{player1} STATS:\n{human.get_data()}')
#                                             print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                             print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                         break
#                                     elif main_menu == 3:
#                                         continue
                            
#                                 except ValueError:
#                                     print('\nInvalid Response. Insert 1 or 2\n')
#                                     continue  
#                         elif number <= 0:
#                             continue
#                         else:
#                             game = Game()
#                             # Creating the players in the game
#                             generate = []
#                             num = 1
#                             z = 0
#                             while num <= number:
#                                 generate.append(Player(input(f'PLAYER {num} Name: ')))
#                                 num += 1
                            
#                             while True:
#                                 y = 0
#                                 points_store = []
#                                 total_store = []
#                                 name_store = []
                                
#                                 store_name = []
#                                 store_points = []
#                                 store_win = []
#                                 store_total = []
                                
#                                 winners = ', '
#                                 winner = ', '
                                
#                                 num_of_rounds.append(x)
#                                 gen_num = game.generated_num()
#                                 print(f'\n\nGET READY FOR AN ALL-ROUND BATTLE AGAINST OUR {number} PLAYERS\n    R O U N D   {x}')
#                                 for action in generate:
#                                     action.guess_number(int(input(f'{generate[y].name} MOVE: \nGuess a 4 digit number: ')))
#                                     action.get_generated_number(gen_num)
#                                     action.counting_bulls()
#                                     action.counting_cows()
#                                     action.calculating_bulls_cows()
#                                     action.store_data(x)
#                                     points_store.append(action.get_points_rounds())
#                                     name_store.append(action.name)
#                                     total_store.append(action.total_points_from_rounds())
#                                     if y > number:
#                                         break
#                                     else:
#                                         y = y + 1

#                                 print(f'\n    ** GENERATED NUMBER: {gen_num}\n\n')
#                                 for z in range(0, number):
#                                     print(f'        ** {generate[z].name} Guess: {generate[z].number}\n')
#                                 for z in range(0, number):
#                                     print(f'\n{generate[z].name}: \n     BULLS: {generate[z].number_bulls}     COWS: {generate[z].number_cows}')
                                    
#                                 print('\n\n\n- P O I N T S   T H I S   R O U N D -')
#                                 for z in range(0, number):
#                                     print(f'{generate[z].name}: \n     POINTS: {generate[z].get_points_rounds()}')
                                
#                                 for z in range(0, len(name_store)):
#                                     if points_store[z] == max(points_store):
#                                         if max(points_store) == 0:
#                                             pass
#                                         else:
#                                             store_points.append(points_store[z])
#                                             store_name.append(name_store[z])
                                
#                                 plt.figure(figsize = (7, 5))
#                                 plt.bar(name_store, points_store, color = 'grey', width = 0.4)
#                                 plt.ylabel('Number of Rounds')
#                                 plt.xlabel('Players')
#                                 plt.title(f'GRAPH OF POINTS IN ROUND {x}')
#                                 plt.show()
                                
#                                 if len(store_name) > 0:    
#                                     store_points = set(store_points)
#                                     winners = winners.join(store_name)      
#                                     print(f'THIS ROUND IS WON BY {winners}.')
#                                 else:
#                                     print('THIS ROUND HAS NO WINNERS')
        
#                                 try:
#                                     flag = False
#                                     switch = False
#                                     main_menu = int(input('Press 0: Previous Menu\nPress 1: Main Menu\nPress 2: Exit\nPress 3: Play Another Round\nRESPONSE: '))
#                                     if main_menu == 0:
#                                         print('\n\n\n- T O T A L   P O I N T S / W I N N E R -')
#                                         for z in range(0, number):
#                                             print(f'{generate[z].name}: \n     POINTS: {generate[z].total_points_from_rounds()}')
                                        
#                                         print("\n\n- G R A P H S -")
#                                         for z in range(0, number):
#                                             print('Graphs Plotted')
#                                             generate[z].graph_round_points(num_of_rounds)
#                                             generate[z].graph_for_totalpoints(num_of_rounds)
                                            
#                                         plt.figure(figsize = (10, 5))
#                                         plt.bar(name_store, total_store, color = 'blue', width = 0.4)
#                                         plt.ylabel('Number of Rounds')
#                                         plt.xlabel('Players')
#                                         plt.title('GRAPH OF PLAYER with the HIGHEST TOTAL POINTS accumulated')
#                                         plt.show()
                                            
#                                         for z in range(0, number):
#                                             print("\n\n- S T A T S -")
#                                             print(f'{generate[z].name} STATS:\n{generate[z].get_data()}')
                                        
#                                         for z in range(0, len(name_store)):
#                                             if max(total_store) == 0:
#                                                 pass
#                                             elif total_store[z] == max(total_store):
#                                                 store_total.append(total_store[z])
#                                                 store_win.append(name_store[z])
                                        
#                                         if len(store_name) > 0:    
#                                             store_total = set(store_total)
#                                             winner = winner.join(store_win)      
#                                             print(f'\nTHIS GAME IS WON BY {winner}.\nWell done in securing victory. You are our GUESS CHAMPION. BRAVO!!!')
#                                         else:
#                                             print('THIS GAME HAS NO WINNERS')
#                                         break
#                                     elif main_menu == 1:
#                                         flag = True
#                                         print('\n\n\n- T O T A L   P O I N T S / W I N N E R -')
#                                         for z in range(0, number):
#                                             print(f'{generate[z].name}: \n     POINTS: {generate[z].total_points_from_rounds()}')
                                        
#                                         print("\n\n- G R A P H S -")
#                                         for z in range(0, number):
#                                             print('Graphs Plotted')
#                                             generate[z].graph_round_points(num_of_rounds)
#                                             generate[z].graph_for_totalpoints(num_of_rounds)
                                            
#                                         plt.figure(figsize = (10, 5))
#                                         plt.bar(name_store, total_store, color = 'blue', width = 0.4)
#                                         plt.ylabel('Number of Rounds')
#                                         plt.xlabel('Players')
#                                         plt.title('GRAPH OF PLAYER with the HIGHEST TOTAL POINTS accumulated')
#                                         plt.show()
                                            
#                                         for z in range(0, number):
#                                             print("\n\n- S T A T S -")
#                                             print(f'{generate[z].name} STATS:\n{generate[z].get_data()}')
                                        
#                                         for z in range(0, len(name_store)):
#                                             if max(total_store) == 0:
#                                                 pass
#                                             elif total_store[z] == max(total_store):
#                                                 store_total.append(total_store[z])
#                                                 store_win.append(name_store[z])
                                        
#                                         if len(store_name) > 0:    
#                                             store_total = set(store_total)
#                                             winner = winner.join(store_win)      
#                                             print(f'\nTHIS GAME IS WON BY {winner}.\nWell done in securing victory. You are our GUESS CHAMPION. BRAVO!!!')
#                                         else:
#                                             print('THIS GAME HAS NO WINNERS')
#                                         break
#                                     elif main_menu == 2:
#                                         switch = True
#                                         print('\n\n\n- T O T A L   P O I N T S / W I N N E R -')
#                                         for z in range(0, number):
#                                             print(f'{generate[z].name}: \n     POINTS: {generate[z].total_points_from_rounds()}')
                                        
#                                         print("\n\n- G R A P H S -")
#                                         for z in range(0, number):
#                                             print('Graphs Plotted')
#                                             generate[z].graph_round_points(num_of_rounds)
#                                             generate[z].graph_for_totalpoints(num_of_rounds)
                                        
#                                         plt.figure(figsize = (10, 5))
#                                         plt.bar(name_store, total_store, color = 'blue', width = 0.4)
#                                         plt.ylabel('Number of Rounds')
#                                         plt.xlabel('Players')
#                                         plt.title('GRAPH OF PLAYER with the HIGHEST TOTAL POINTS accumulated')
#                                         plt.show()
                                            
#                                         for z in range(0, number):
#                                             print("\n\n- S T A T S -")
#                                             print(f'{generate[z].name} STATS:\n{generate[z].get_data()}')
                                        
#                                         for z in range(0, len(name_store)):
#                                             if max(total_store) == 0:
#                                                 pass
#                                             elif total_store[z] == max(total_store):
#                                                 store_total.append(total_store[z])
#                                                 store_win.append(name_store[z])
                                        
#                                         if len(store_name) > 0:    
#                                             store_total = set(store_total)
#                                             winner = winner.join(store_win)      
#                                             print(f'\nTHIS GAME IS WON BY {winner}.\nWell done in securing victory. You are our GUESS CHAMPION. BRAVO!!!')
#                                         else:
#                                             print('THIS GAME HAS NO WINNERS')
#                                         break
#                                     elif main_menu == 3:
#                                         x = x + 1
#                                         continue                                        
                            
#                                 except ValueError:
#                                     print('\nInvalid Response. Insert 1 or 2\n')
#                                     continue
                            
#                     elif question == 2:
#                         x = 1
#                         game = Game()
#                         human = Player(input('PLAYER 1 Name: '))
#                         human1 = Player(input('PLAYER 2 Name: '))
#                         generate = [human, human1]
#                         while True:
#                             y = 0
#                             gen_num = game.generated_num()
#                             print(f'\n\n{human.name} Vs {human1.name}\n    R O U N D   {x}') 
                            
#                             for action in generate:
#                                 action.guess_number(int(input(f'{generate[y].name} MOVE: \nGuess a 4 digit number: ')))
#                                 action.get_generated_number(gen_num)
#                                 action.counting_bulls()
#                                 action.counting_cows()
#                                 action.calculating_bulls_cows()
#                                 action.store_data(x)
#                                 y = 1
                            
#                             print(f'\n    ** GENERATED NUMBER: {gen_num}\n\n    ** {human.name} Guess: {human.number}\n    ** {human1.name}: {human1.number}\n')
#                             human_store = human.get_data()
#                             human1_store = human1.get_data()
                            
#                             n = zip(human_store[x].values(), human1_store[x].values())                           
#                             player1 = human.name
#                             player2 = human1.name
#                             bulls, cows, points, total_points, guess, game_guess = n
#                             if points[0] > points[1]:
#                                 print(f'- The winner of this round is {player1} -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'- POINTS -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                             elif points[0] < points[1]:
#                                 print('- AI wins this round -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'- POINTS -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                             elif points[0] == points[1]:
#                                 print('- This round is a draw -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'- POINTS -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                             else:
#                                 raise ValueError
#                             x = x + 1
                        
#                             try:
#                                 flag = False
#                                 switch = False
#                                 main_menu = int(input('Press 0: Previous Menu\nPress 1: Main Menu\nPress 2: Exit\nPress 3: Play Another Round\nRESPONSE: '))
#                                 if main_menu == 0:
#                                     break
#                                 elif main_menu == 1:
#                                     flag = True
#                                     break
#                                 elif main_menu == 2:
#                                     switch = True
#                                     break
#                                 elif main_menu == 3:
#                                     continue
                        
#                             except ValueError:
#                                 print('\nInvalid Response. Insert 1 or 2\n')
#                                 continue 
                        
#                     elif question == 1:
#                         x = 1
#                         game = Game()
#                         human = Player(input('Name: '))
#                         ai = AI()
#                         while True:
#                             gen_num = game.generated_num()
                            
#                             get_gen_human = human.get_generated_number(gen_num)
#                             get_gen_ai = ai.get_generated_number(gen_num)
                                         
#                             print(f'\n\nBEAT THE AI\n    R O U N D   {x}') 
#                             my_guess = human.guess_number(int(input('PLAYERS MOVE: \nGuess a 4 digit number: ')))
#                             ai_guess = ai.ai_guess()
                            
#                             my_bulls = human.counting_bulls()
#                             ai_bulls = ai.counting_bulls()
#                             my_cows = human.counting_cows()
#                             ai_cows = ai.counting_cows()
                            
#                             my_calc = human.calculating_bulls_cows()
#                             ai_calc = ai.calculating_bulls_cows()
                            
#                             my_store = human.store_data(x)
#                             ai_store = ai.store_data(x)
#                             print(f'\n    ** GENERATED NUMBER: {gen_num}\n\n    ** Your Guess: {my_guess}\n    ** AI Guess: {ai_guess}\n')
                            
#                             n = zip(my_store[x].values(), ai_store[x].values())
#                             player1 = human.name
#                             player2 = ai.name
#                             bulls, cows, round_points, points, guess, game_guess = n
#                             if round_points[0] > round_points[1]:
#                                 print(f'- The winner of this round is {player1} -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                             elif round_points[0] < round_points[1]:
#                                 print('- AI wins this round -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                             elif round_points[0] == round_points[1]:
#                                 print('- This round is a draw -')
#                                 print(f'{player1} BULLS: {bulls[0]}\nAI.{player2} BULLS: {bulls[1]}')
#                                 print('')
#                                 print(f'{player1} COWS: {cows[0]}\nAI.{player2} COWS: {cows[1]}')
#                                 print('')
#                                 print(f'\n- P O I N T S -\nPLAYER 1({player1}): {round_points[0]}\nPLAYER 2(AI.{player2}): {round_points[1]}')
#                             else:
#                                 raise ValueError
                            
#                             x = x + 1                            
#                             try:
#                                 flag = False
#                                 switch = False
#                                 main_menu = int(input('Press 0: Previous Menu\nPress 1: Main Menu\nPress 2: Exit\nPress 3: Play Another Round\nRESPONSE: '))
#                                 if main_menu == 0:
#                                     if points[0] > points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print(f'- OUR GUESS CHAMPION is {player1} -')
                                        
#                                     elif points[0] < points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- OUR GUESS CHAMPION is AI Enoch-')
                                        
#                                     elif points[0] == points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                     break
#                                 elif main_menu == 1:
#                                     flag = True
#                                     if points[0] > points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print(f'- OUR GUESS CHAMPION is {player1} -')
                                        
#                                     elif points[0] < points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- OUR GUESS CHAMPION is AI Enoch-')
                                        
#                                     elif points[0] == points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                     else:
#                                         raise ValueError
#                                     break
#                                 elif main_menu == 2:
#                                     switch = True
#                                     if points[0] > points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print(f'- OUR GUESS CHAMPION is {player1} -')
                                        
#                                     elif points[0] < points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- OUR GUESS CHAMPION is AI Enoch-')
                                        
#                                     elif points[0] == points[1]:
#                                         print(f'\n- P O I N T S -\nPLAYER 1({player1}): {points[0]}\nPLAYER 2(AI.{player2}): {points[1]}')
#                                         print("\n\n- S T A T S -")
#                                         print(f'{player1} STATS:\n{human.get_data()}')
#                                         print(f'\n\nAI Enoch STATS:\n{ai.get_data()}')
#                                         print('- THE GAME IS A DRAW BETWEEN {player1} AND AI Enoch -')
#                                     break
#                                 elif main_menu == 3:
#                                     continue
                        
#                             except ValueError:
#                                 print('\nInvalid Response. Insert 1 or 2\n')
#                                 continue     
                    
#                     if switch == True:
#                         switch = False
#                         break
#                     elif flag == True:
#                         flag = False
#                         break
#                 except ValueError:
#                     print('Invalid Command')
#                     pass
                
#         elif proceed == 2:
#             print('Goodbye!')
#             break
        
#         if switch == False:
#             break
#         if flag == False:
#             print('- M A I N   M E N U -')
#     except ValueError:
#         print('\nInvalid Response. Insert 1 or 2\n')
#         pass








# my_bulls = human.counting_bulls()
# ai_bulls = ai.counting_bulls()
# my_cows = human.counting_cows()
# ai_cows = ai.counting_cows()

# my_calc = human.calculating_bulls_cows()
# ai_calc = ai.calculating_bulls_cows()

# my_store = human.store_data(x)
# ai_store = ai.store_data(x)
