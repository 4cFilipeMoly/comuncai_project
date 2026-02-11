import os

pasta = "pasta"

def crate_folder():
    if pasta not in os.listdir():
        os.mkdir(pasta)

crate_folder()