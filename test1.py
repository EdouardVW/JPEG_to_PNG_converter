from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(img.filenameÒ)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blurred_pikachu','png')

smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.save('smooth_pikachu','png')

sharpen_img = img.filter(ImageFilter.SHARPEN)
sharpen_img.save('sharpen_pikachu','png')

grey = filtered_img.convert('L')
grey.save('grey_pikachu','png')

#grey.show()

#grey.rotate(90).show()

#grey.resize((300,300)).show()

box = (100, 100, 400, 400)
#img.crop(box).show()





img2 = Image.open('./astro.jpg')
print(img2.size)

img2.thumbnail((400, 400)) #to keep aspect ratio of image -> use thumbnail 
img2.save('thumbnail.jpg')
img2.show()


