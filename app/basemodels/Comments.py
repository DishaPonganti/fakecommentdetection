""" A POJO like class for comments """

class Comments(object):
    """class comments"""
    comm = ''
    def __init__(self):
        self.data = []
        print("Comments object created")

    def getcomment(self):
        """function to get the input comment """
        print("Please enter the comment: ")
        self.comm = input()

    def printcomment(self):
        """function to print the input comment """
        print(self.comm)
