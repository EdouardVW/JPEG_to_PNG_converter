from PIL import Image, ImageFilter
import sys
import glob
import os
import re

folderName = sys.argv[1]
newFolderName = sys.argv[2]

def createFolder(filename):
    if not os.path.exists(f'./{filename}'):
        os.makedirs(f'./{filename}')

createFolder(newFolderName)

files = glob.glob("./Pokedex/*.jpg")

filesDestination = glob.glob("f'./{newFolderName}'")

for file in files:
    if file not in filesDestination:
        img = Image.open(f'{file}')

        fileName = re.sub('.jpg', '.png', re.sub(f"{folderName}", f"{newFolderName}", img.filename))

        img.save(fileName)

