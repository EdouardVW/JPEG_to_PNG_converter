import glob

files = glob.glob("./Pokedex/*.jpg")



#print('./Pokedex/bulbasaur.jpg' in files)

import re
print(re.sub("Pokedex", "newFolder", './Pokedex/bulbasaur.jpg'))
