"""
Program Name: Coin Class
Name: Riddhi Agarwal
Purpose: This program defines the coin class and represents a coin that can be Heads or Tails.
Starter Code: None
Date: March 15, 2026

"""

import random

class coin:
    def __init__(self):
        """Initializes the coin and sets up the __sideup attribute"""
        if random.randinit(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        """Generates a random number 0 or 1 and sets __sideup to heads or tails"""
        if random.randinit(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
        
    def get_sideup(self):
        """Returns the value of __sideup (Heads or Tails)"""
        return self.__sideup