# Quiz Flashcard Program
Quiz Flashcard Program

This software is designed for the use of flashcard games. It has four different fuctions. Practice games without time, where you can practice your questions without pressure. It has a game setting where you play against a clock and attempt to get a high score. You can add cards, and you can also view and delete cards within your deck. Decks should be saved as they do not automatically store. This program was made entirely in Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Libraries needed to run this software

```bash

apt-get install python3-tk

```
additional libraries used JSON and random

## Deployment

### Beginning interface

![sample1](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample1.png)

The initial interface will prompt you to load a deck from a file. Default files will be JSON format. New decks can be created as well and saved in JSON format.

After one has loaded a deck. The full options become available to be used. 

![sample2](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample2.png)

After one has loaded a deck. The full options become available to be used. This menu will remain until the program is restarted or the current deck is removed, via the "New deck" option in the 'File' menu.

### Practice

![sample3](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample3.png)

In the practice activity, your deck is shuffled and you are presented with a card from your deck. You may try as many times as you like to get it right. If you select 'hint', the answer will be shown and the text field will be disabled. You will be informed each time an answer you entered was correct. The 'Enter' key is the means of submitting your answer. Practicing cannot be done when there are no cards in the deck.

### Game Play

![sample4](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample4.png)

The quiz portion of this game is to enter the solution as fast as you can. Each time there answer is entered and submitted with the 'Enter' key, it will be evaluated and move to the next card. Correct answers will yield points and time on the clock. The deck will continuously be shuffled and the game will continue until the clock has run out. The game cannot be played when there are no cards in the deck.

### Adding Cards

![sample5](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample5.png)

Cards are added using this interface. Each card is added individually, unless loaded from a JSON file. The card consists of one 'question key' and an 'answer value'. The fields may be cleared with the clear button, and saved with the save button. The 'Enter' key may also be used to submit cards. All fields must be filled before a card can be saved. 

### Viewing Cards

![sample6](https://raw.githubusercontent.com/delanyk/flashcard_software/master/img/sample6.png)


## Built With

*[tkinter](https://wiki.python.org/moin/TkInter) Python's GUI (Graphical User Interface) package


## Versioning
Current version is 1.6

## Authors

* **Delany** - *Initial work* - 

## Acknowledgments

sample_words.json were a subset taken from an online [wordlist](https://www.trueterm.com/wordlist.html)
