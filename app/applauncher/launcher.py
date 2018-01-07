"""This is the launcher class"""

from app.basemodels.Comments import Comments
if __name__ == '__main__':
    print("Starting the launcher class")
    MAIN_OBJ = Comments()
    MAIN_OBJ.getcomment()
    MAIN_OBJ.printcomment()
