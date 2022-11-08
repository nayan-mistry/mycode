#!/usr/bin/python3
"""Driving a simple game framework with a dictionary
object"""

def showInstructions():
    """Show the instructions when called"""
    print(""".git/
    RPG Game
    =============
        Commands:
            go [direction]
            get [item]
    """)

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it