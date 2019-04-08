#!/usr/bin/env python3
from tkinter import *
import json
from tkinter.filedialog import *
from tkinter.messagebox import *
import random


class WordQuiz:
		instructions = {
				"intro"   : "Make a selection", 
				"practice": "Type the answer and press 'Enter' or\n Click 'Hint' to show the answer",
				"game"    : "Type the answer as fast as you can\n Each correct answer will yeild time and points",
				"cards"   : "Enter a Question and a corresponding Answer below\nThen click 'Save' to save the card or press 'Enter'",
				"view"    : "List of cards below."
									  }
		current_frame = ''

		def __init__(self, frame): 
				# master frame
				self.__master = frame
				self.__master.title("Word Quiz")
				
				# hotkey bindings
				self.__master.bind('<Control-q>', self.__exitApp)
				self.__master.bind('<Control-n>', self.__load_new_deck)
				self.__master.bind('<Control-o>', self.__load_file)
				self.__master.bind('<Control-s>', self.__save)

				# window measurements
				self.height = 450
				self.width  = 650
				# Center the window 
				screenWidth  = self.__master.winfo_screenwidth() 
				screenHeight = self.__master.winfo_screenheight() 
				# For left-alling 
				left = (screenWidth / 2) - (self.width / 2) 
		
				# For right-allign 
				top = (screenHeight / 2) - (self.height /2) 
		
				# For top and bottom 
				self.__master.geometry('%dx%d+%d+%d' % (self.width, 
											self.height, 
											left, top)) 
				self.__master.config(bg='#8EBCCB') 

				self.__master.grid_rowconfigure(0, weight=1) 
				self.__master.grid_columnconfigure(0, weight=1) 

				# menu variables
				self.__menu       = Menu(self.__master)
				self.__fileMenu   = Menu(self.__menu, tearoff=0) 
				self.__optionMenu = Menu(self.__menu, tearoff=0) 
				self.__helpMenu   = Menu(self.__menu, tearoff=0) 

				# self.__data = {"big": "small", "toast": "butter"}
				self.__data = {}

				# Menu
				self.__fileMenu.add_command(label="New Deck", command=self.__load_new_deck)
				self.__fileMenu.add_command(label="Load Deck", command= self.__load_file)
				self.__fileMenu.add_command(label="Save as ...", command= self.__save)
				self.__fileMenu.add_separator()
				self.__fileMenu.add_command(label="Quit", command=self.__exitApp)

				# add card option
				self.__optionMenu.add_command(label="Add Cards", command=self.__load_card_ui)
				self.__optionMenu.add_command(label="View Cards", command=self.__card_view_ui)
				
				# about
				self.__helpMenu.add_command(label="About", command=self.__showAbout)

				self.__menu.add_cascade(label="File", menu=self.__fileMenu)
				self.__menu.add_cascade(label="Options", menu=self.__optionMenu)
				self.__menu.add_cascade(label="Help", menu=self.__helpMenu)

				self.__master.config(menu=self.__menu)

				# load main menu
				self.__load_main()

		# load main user interface
		def __load_main(self):
				# destroy other frames
				self.__destroy_frame()
				
				#active frame
				self.current_frame = 'main'

				#main user interface
				self.__main_frame = Frame(self.__master,bg="#8EBCCB")
				self.__main_frame.place(relx=0.5, rely=0.25, relwidth= 0.8, 
																							relheight=0.7, anchor='n')

				# create deck or load cards
				if self.__data:
						# load instuctions
						self.instruct = Label(self.__master, text = self.instructions['intro'],
																	font =('Helvetica', 40), bg="#8EBCCB", fg='black')
						self.instruct.place(relx= 0.5, rely=0.05, anchor='n')
						
						# button for practice without time
						self.practice_btn = Button(self.__main_frame,text = "Practice",
							font=('Helvetica', 20), fg='blue', command=self.__load_practice_ui)
						self.practice_btn.place(relx=0.5, rely=0.05,relheight=0.2, 
																										relwidth=0.8,anchor='n')
						
						# quiz for quiz with time limit
						self.play_btn = Button(self.__main_frame,text = "Play a Game", 
									font=('Helvetica', 20), fg='green', command=self.__load_game_ui)
						self.play_btn.place(relx=0.5, rely=0.25, relheight=0.2, 
																									relwidth=0.8,anchor='n')

						# load new cards
						self.new_cards = Button(self.__main_frame,text = "Add Cards",
									font=('Helvetica', 20), fg='orange', command=self.__load_card_ui)
						self.new_cards.place(relx=0.5, rely=0.45, 
																relheight=0.2, relwidth=0.8,anchor='n')

						# view cards
						self.view_cards = Button(self.__main_frame,text = "View Cards",
									font=('Helvetica', 20), fg='purple', command=self.__card_view_ui)
						self.view_cards.place(relx=0.5, rely=0.65, 
																relheight=0.2, relwidth=0.8,anchor='n')
				
				else:

						self.load_cards = Button(self.__main_frame,text = "Load a Deck",
							font=('Helvetica', 30), fg='blue', command=self.__load_file)
						self.load_cards.place(relx=0.5, rely=0.05 ,relheight=0.3,
																							 relwidth=0.8, anchor='n')

						self.new_cards = Button(self.__main_frame,text = "Create a Deck",
							font=('Helvetica', 30), fg='orange', command=self.__load_card_ui)
						self.new_cards.place(relx=0.5, rely=0.45,relheight=0.3,
																							 relwidth=0.8, anchor='n')

		def __destory_main(self):
				try:
						self.instruct.destroy()
				except:
						pass
				self.__main_frame.destroy()

		def __destroy_practice(self):
				self.navbar.destroy()
				self.instruct.destroy()
				try:
						self.practice_frame.destroy()
				except:
						pass

		def __destroy_game(self):
				self.navbar.destroy()
				self.instruct.destroy()
				self.game_frame.destroy()

		def __destory_cards(self):
				self.navbar.destroy()
				self.instruct.destroy()
				self.card_frame.destroy()
		
		def __destory_view(self):
				self.navbar.destroy()
				self.instruct.destroy()
				self.view_frame.destroy()
				self.scrollbar.destroy()
		
		# determin frame to be destoryed
		def __destroy_frame(self):
				curr = self.current_frame
				if curr == 'main':
						self.__destory_main()
				elif curr == 'practice':
						self.__destroy_practice()
				elif curr == 'game':
						self.__destroy_game()
				elif curr == 'cards':
						self.__destory_cards()
				elif curr == 'view':
						self.__destory_view()

		def __load_new_deck(self,*args):
				self.__data = {}
				self.__load_card_ui()

		def __load_nav(self, act):
				current_act = act

				# Build Navbar
				self.navbar = Frame(self.__master)
				self.navbar.place(relwidth=1, relheight=0.06, anchor='nw')
				self.main_nav = Button(self.navbar, text='Main',
																				fg='blue', command=self.__load_main)
				self.main_nav.place(relheight=1, relwidth=0.2)
				self.practice_nav = Button(self.navbar, text='Practice', 
																	fg='blue', command=self.__load_practice_ui)
				self.practice_nav.place(relx=0.2, relheight=1, relwidth=0.2)
				self.play_nav = Button(self.navbar, text='Play Game',
																	 		fg='blue', command=self.__load_game_ui)
				self.play_nav.place(relx=0.4, relheight=1, relwidth=0.2)
				self.cards_nav = Button(self.navbar, text='Add Cards',
																			fg='blue', command=self.__load_card_ui)
				self.cards_nav.place(relx=0.6, relheight=1, relwidth=0.2)
				self.view_nav = Button(self.navbar, text='View Cards', fg='blue',
																								 command=self.__card_view_ui)
				self.view_nav.place(relx=0.8, relheight=1, relwidth=0.2)

				nav_btns = [self.practice_nav, self.play_nav, self.cards_nav, self.view_nav]
				for btn in nav_btns:
						if current_act == btn['text']:
								btn.config(state='disabled')
						else:
								btn.config(state='normal')

		def __load_practice_ui(self):
				# destroy old frame
				self.__destroy_frame()

				# current frame
				self.current_frame = 'practice'

				def reveal_hint():
						key = self.key['text']
						answer = self.__data[key]
						self.ans_hint = Label(self.practice_frame, text= answer,
														 bg="white", fg="brown", font=('Helvetica', 16))
						self.ans_hint.place(relx=0.5, rely=0.4, anchor='n')
						self.answer_entry.config(state='disabled')

				def evaluation(event):
						solution = self.__check_answer()

						if solution:
								self.eval['text'] = 'Correct'
								self.eval['fg'] = 'green'
						else:
								self.eval['text'] = 'Try again'
								self.eval['fg'] = 'red'

				self.__load_nav('Practice')

				self.instruct = Label(self.__master, text = self.instructions['practice'],
															font =('Helvetica', 14), bg="#8EBCCB",fg='black')
				self.instruct.place(relx= 0.5, rely=0.1, anchor='n')


				if self.__data:

						#current point in array
						self.curr = 0

						# shuffle the cards
						self.cards = self.__shuffle(self.__data)

						# card display
						self.practice_frame = Frame(self.__master, bg="white", bd=5)
						self.practice_frame.place(relx=0.5, rely=0.3, 
														relwidth=0.8, relheight=0.5, anchor='n')
						
						# loading key
						self.key = Label(self.practice_frame, bg="white",
																 	fg="green", font=('Helvetica', 30))
						self.key.place(relx=0.5, rely=0.1, anchor='n')

						# answer entry
						self.answer_entry = Entry(self.practice_frame, font=('Helvetica', 20))
						self.answer_entry.place(relx=0.5, rely=0.6, relheight=0.2, 
																								relwidth=0.6, anchor='n')

						# Correctness
						self.eval = Label(self.practice_frame, bg="white", 
																						font=('Helvetica', 20))
						self.eval.place(relx=0.5, rely=0.8, anchor='n')

						# Bind answer with enter
						self.answer_entry.bind('<Return>', evaluation)

						# hint answer
						self.hint = Button(self.practice_frame, text='Hint',
																		 fg='red', command=reveal_hint)
						self.hint.place(rely=1, anchor='sw')

						# button to next card
						self.next_btn = Button(self.practice_frame, text='Next Card',
														fg='green', command=self.__next_card_practice)
						self.next_btn.place(relx=1, rely=1, anchor='se')

						self.__next_card_practice()
				else:
						self.instruct['text'] = 'There are no cards yet to practice with'

		def __load_game_ui(self):
				# destroy old frame
				self.__destroy_frame()

				# current frame
				self.current_frame = 'game'

				self.__load_nav('Play Game')

				self.instruct = Label(self.__master, text = self.instructions['game'],
															font =('Helvetica', 14), bg="#8EBCCB",fg='black')
				self.instruct.place(relx= 0.5, rely=0.1, anchor='n')

				# initiate score
				self.score = 0

				# starting time
				self.time_left = 20

				# card display
				self.game_frame = Frame(self.__master, bg="#8EBCCB", bd=5)
				self.game_frame.place(relx=0.5, rely=0.25, 
												relwidth=0.8, relheight=0.65, anchor='n')

				# if no data
				if self.__data:

						# button to start game
						self.start_btn = Button(self.game_frame, text='Start Game',
											fg='green', command=self.__play, font =('Helvetica', 25))
						self.start_btn.place(relx=0.5, rely=0.2, relwidth=0.5, 
																								relheight=0.5, anchor='n')

				else:
						self.instruct['text'] = 'There are no cards yet to play with'


		# view cards in list
		def __card_view_ui(self):
				# destroy old frame
				self.__destroy_frame()

				# current frame
				self.current_frame = 'view'

				self.__load_nav('View Cards')

				# card display
				self.view_frame = Frame(self.__master, bg='#8EBCCB',)
				self.view_frame.place(relx=0.5, rely=0.15, 
												relwidth=0.8, relheight=0.83, anchor='n')
				self.card_frame=Canvas(self.view_frame,bg='#8EBCCB', highlightthickness=0)
				self.card_frame.pack(side='top',fill='both', expand=True)

				self.instruct = Label(self.__master, text = self.instructions['view'],
															font =('Helvetica', 12), bg="#8EBCCB",fg='black')
				self.instruct.place(relx= 0.5, rely=0.07, anchor='n') 


				self.scrollbar = Scrollbar(self.__master, orient='vertical', command=self.card_frame.yview)
				self.scrollbar.place(relx=1, rely=0.06, relheight=0.94, anchor='ne')	
				self.card_frame.config(yscrollcommand=self.scrollbar.set)
	
	
				# pull in cards
				cards =  [(key, val) for key, val in self.__data.items()]

				#default directions for sorting
				self.key_direction = 'asc'
				self.ans_direction = 'asc'

				# display cards in viewing Frame
				def display_cards(cards):
						def delete_card(key):
								answer = askquestion('Delete Card', 'Are you sure you wish to delete this card')
								if answer == 'yes':
										del self.__data[key]
										self.__card_view_ui()
								else:
										pass

						def populate_cards(frame):
								#load title cards
								card_tag = Frame(card_display, bg='black', height=50, width=(self.__master.winfo_width()*0.63))
								card_tag.pack(anchor='nw')
								key_label = Button(card_tag, text='Question', fg='blue', 
																		bd=2, font =('Helvetica', 25),command=key_sort)
								key_label.place(relx=0.005, rely=0.025, relwidth=0.49, relheight=0.95)
								val_label = Button(card_tag, text='Answers', fg='orange',
																		bd=2, font =('Helve,tica', 25), command=ans_sort)
								val_label.place(relx=0.505, rely=0.025, relwidth=0.49, relheight=0.95)

								#load cards
								for key, val in cards:
									card_tag = Frame(card_display, bg='black', height=50, width=(self.__master.winfo_width()*0.79))
									card_tag.pack()

									# key, val labels and delete button
									key_label = Label(card_tag, text=key, bd=2, font =('Helvetica', 20))
									key_label.place(relx=0.005, rely=0.025, relwidth=0.39, relheight=0.95)
									val_label = Label(card_tag, text=val, bd=2, font =('Helvetica', 20))
									val_label.place(relx=0.40, rely=0.025, relwidth=0.39, relheight=0.95)
									del_btn   = Button(card_tag, text='Delete', bg='red', fg='white', 
																					highlightthickness=0,  font=('Helvetica', 12),
																					command= lambda x=key: delete_card(x))
									del_btn.place(relx=0.80, rely=0.025, relwidth=0.195, relheight=0.95)
						
						# Reset the scroll region
						def onFrameConfigure(canvas):
								canvas.configure(scrollregion=canvas.bbox("all"))

						try:
								card_display.distroy()
						except:
								pass

						card_display = Frame(self.card_frame, bg='#8EBCCB')

						self.card_frame.create_window((4,4), window=card_display, anchor="nw")
						card_display.bind("<Configure>", 
										lambda event, canvas=self.card_frame: onFrameConfigure(self.card_frame))

						populate_cards(card_display)


				#sort cards by question
				def key_sort():
						if self.key_direction =='asc':
								sorted_keys = sorted(cards)
								display_cards(sorted_keys)
								self.key_direction = 'desc'
						else:
								sorted_keys = sorted(cards, reverse=True)
								display_cards(sorted_keys)
								self.key_direction = 'asc'

				#sort cards by answers
				def ans_sort():
						if self.ans_direction =='asc':
								sorted_ans = sorted(cards, key=lambda x: x[1])
								display_cards(sorted_ans)
								self.ans_direction = 'desc'
						else:
								sorted_ans = sorted(cards, key=lambda x: x[1], reverse=True)
								display_cards(sorted_ans)
								self.ans_direction = 'asc'
				if self.__data:
						display_cards(cards)
				else:
						self.instruct['text'] = 'Currently there are no cards'

		# load UI for creating cards
		def __load_card_ui(self):
				# destroy old frame
				self.__destroy_frame()

				# current frame
				self.current_frame = 'cards'

				self.__load_nav('Add Cards')

				self.instruct = Label(self.__master, text = self.instructions['cards'],
															font =('Helvetica', 14), bg="#8EBCCB",fg='black')
				self.instruct.place(relx= 0.5, rely=0.1, anchor='n')

				# save the card to dictionary
				def save_card(*args):
						key = self.key_entry.get()
						val = self.answer_entry.get()
						if key and val:
							self.__data[key.lower()] = val.lower()
							success(True)
							clear_card()
						else:
							success(False)

				# clear the card fields
				def clear_card():
						self.key_entry.delete(0, END)
						self.answer_entry.delete(0, END)

				def success(Bool):
						if Bool:
								self.eval['text'] = 'Card was saved'
								self.eval['fg'] = 'green'
						else:
								self.eval['text'] = 'Fields cannot be empty'
								self.eval['fg'] = 'red'

				# card display
				self.card_frame = Frame(self.__master, bg="white", bd=5)
				self.card_frame.place(relx=0.5, rely=0.3, 
												relwidth=0.8, relheight=0.5, anchor='n')

				# key label
				self.key_label = Label(self.card_frame, text='Question',bg='white', 
																						font=('Helvetica', 20),justify='right')
				self.key_label.place( rely=0.2, relheight=0.25, relwidth=0.35)
				
				# key entry
				self.key_entry = Entry(self.card_frame, font=('Helvetica', 25))
				self.key_entry.place(relx=0.6, rely=0.2, relheight=0.25, 
																						relwidth=0.6, anchor='n')

				# answer label
				self.key_label = Label(self.card_frame, text='Answer',bg='white', 
																						font=('Helvetica', 20),justify='right')
				self.key_label.place( rely=0.5, relheight=0.25, relwidth=0.35)

				# answer entry
				self.answer_entry = Entry(self.card_frame, font=('Helvetica', 25))
				self.answer_entry.place(relx=0.6, rely=0.5, relheight=0.25, 
																						relwidth=0.6, anchor='n')

				# Correctness
				self.eval = Label(self.card_frame, bg="white", 
																				font=('Helvetica', 20))
				self.eval.place(relx=0.5, rely=0.8, anchor='n')


				# hint answer
				self.clear_btn = Button(self.card_frame, text='Clear',
																 fg='orange', command=clear_card)
				self.clear_btn.place(rely=1, anchor='sw')

				# button to next card
				self.save_btn = Button(self.card_frame, text='Save Card',
												fg='green', command=save_card)
				self.save_btn.place(relx=1, rely=1, anchor='se')
				
				#bind return for submission
				self.answer_entry.bind('<Return>', save_card)
				self.key_entry.bind('<Return>', save_card)

		def __next_card_practice(self):
				self.answer_entry.config(state='normal')
				try:
						self.ans_hint.destroy()
				except:
						pass
				
				# clear evaluation
				try:
						self.eval['text'] =''
						self.eval['fg'] =''
				except:
						pass

				# clear answer
				self.answer_entry.delete(0, END)

				# establish new key
				try:
					key = self.cards[self.curr][0]
				except:
					key = ''

				self.key['text'] = key
				self.curr += 1

				if self.curr >= len(self.cards):
						self.next_btn.config(state='disabled')
		
		# return shuffled deck
		def __shuffle(self, *args):

				cards = [(key, ans) for key,ans in self.__data.items()]

				random.shuffle(cards)
				return cards

		# check if answer is correct
		def __check_answer(self):
				answer = self.answer_entry.get()
				key = self.key['text']
				return answer == self.__data[key]

		def __play(self):

				# clear the Fame Frame
				self.start_btn.destroy()

				# change background
				self.game_frame['bg'] = 'white'

				#score board
				self.score_label = Label(self.game_frame, background='white',
																								 font =('Helvetica', 14))
				self.score_label.place(relx=0.5, anchor="n")

				#timer
				self.time_label = Label(self.game_frame, background='white', 
																							font =('Helvetica', 14))
				self.time_label.place(anchor="nw")

				# get card
				def get_card():
						card = self.__shuffle()[0]

						return card[0], card[1]

				# loading key
				def load_card(key):
						self.key['text'] = key

				# game countdown clock
				def count_down():

						#if the game is running
						if self.time_left > 0:

								# decrease counter
								self.time_left -= 1

								#update time clock
								self.time_label['text'] = "Time Left: "+str(self.time_left)

								# run clock after 1 second
								self.time_label.after(1000, count_down)
						else:
								self.key['text'] = 'Game Over'
								self.key['fg'] = 'red'
								self.answer_entry.destroy()

				# selects new card and continues game
				def next_card(Event):
						if self.time_left > 0:

								# get new card
								key, answer = get_card()

								# load card
								load_card(key)

								# # make text box
								# self.answer_entry.focus_set()

								# check if solution is correct
								if self.answer_entry.get() ==  answer.lower():

									self.score += 1
									self.time_left +=5

								# clear the text box
								self.answer_entry.delete(0, END)

								# update score
								self.score_label['text'] = "Score: " + str(self.score)

				# key/question field
				self.key = Label(self.game_frame, bg="white",
														 	fg="green", font=('Helvetica', 30))
				self.key.place(relx=0.5, rely=0.1, anchor='n')

				# answer entry
				self.answer_entry = Entry(self.game_frame, font=('Helvetica', 20))
				self.answer_entry.place(relx=0.5, rely=0.6, relheight=0.2, 
																						relwidth=0.6, anchor='n')

				# Bind answer with enter
				self.answer_entry.bind('<Return>', next_card)
				
				count_down()
				# Game Loop
				next_card('start')


		# loading user cards from file	
		def __load_file(self, *args):
				self.__file = askopenfilename(defaultextension=".json", 
											filetypes=[("JSON Documents","*.json"),
											("All Files","*.*")]) 

				if self.__file == "": 
						# no file to open 
						self.__file = None

				else: 
					# Try to open the file 
					with open(self.__file, "r") as f:
							self.__data = json.load(f)

				#load main menu
				self.__load_main()

		# saving user cards to file
		def __save(self, *args):
				self.__file = asksaveasfilename(defaultextension=".json", 
											filetypes=[("JSON Documents","*.json"),
											("All Files","*.*")]) 

				if self.__file == "": 
						# no file to open 
						self.__file = None

				else: 
					# Try to open the file 
					with open(self.__file, "w") as f:
							json.dump(self.__data, f)

		# show about
		def __showAbout(self): 
				showinfo("Word Quiz Game","Word Quiz Game\n\n\nCopyright © 2019\nK. De Lany\nversion 1.6") 

		# exit application
		def __exitApp(self,*args):
				exit()

		# run program
		def run(self):
				self.__master.mainloop()

root=Tk()
game = WordQuiz(root)
game.run()