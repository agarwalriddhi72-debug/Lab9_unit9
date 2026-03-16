"""
Program Name: Player Class
Name: Riddhi Agarwal
Purpose: This program defines the player class.
         This class represents a player that has a name, waller of coins, and has a coin to toss.
Starter Code: None
Date: March 15, 2026
"""

from coin import Coin

class Player:
    """Initializes the player with name, wallet and coin."""
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Tells player to toss"""
        self.__coin.toss()
    
    def get_coin_side(self):
        """Return the side of the player's coin"""
        return self.__coin.get_sideup()
    
    def win_coin(self):
        """Adds 1 to the __wallet attribute"""
        self.__wallet += 1

    def lose_coin(self):
        """Subtracts 1 from the __wallet attribute"""
        self.__wallet -= 1
    
    def get_wallet(self):
        """Returns the value of the __wallet attribute"""
        return self.__wallet

    def get_name(self):
        """Returns the value of the __name name attribute"""
        return self.__name

