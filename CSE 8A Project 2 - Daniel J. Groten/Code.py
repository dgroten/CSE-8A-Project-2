#The image "Spider-Man (Original).jpg" is an image I took myself and "Spider-Man (Resized).jpg"
#is the same image resized to a smaller form.

#The image "New York City.jpg" is an image I took myself using the photo mode in the video game
#"Marvel's Spider-Man" by Insomniac Games.

#The image "Web.jpg" is an official piece of promo art for the movie "Spider-Man: Homecoming".

#The image "My Result Image.jpg" is the final resulting image when the code is finished running.

from PIL import Image

def crop_and_copy(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    for x in range(44,47):
        for y in range(0,300):
            r, g, b = image1.getpixel((x,y))
            image2.putpixel((x + 920, y), (r,g,b))
    image2.save("york1.jpg")

crop_and_copy("Web.jpg", "New York City.jpg")

def flip(img):
    image = Image.open(img)
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x,y))
            new_image.putpixel((width - x - 1, height - y - 1), (r,g,b))
    new_image.save("spider1.jpg")

flip("Spider-Man (Resized).jpg")

def remove_green_and_copy(img1, img2):
    image1 = Image.open(img1)
    width, height = image1.size
    image2 = Image.open(img2)
    for x in range(width):
        for y in range(height):
            r, g, b = image1.getpixel((x,y))
            if x in range(119,191) and y in range(452,486):
                image2.putpixel((x + 810, y + 200), (r,g,b))
            elif r <= g and b <= g:
                continue
            else:
                image2.putpixel((x + 810, y + 200), (r,g,b))
    image2.save("york2.jpg")

remove_green_and_copy("spider1.jpg", "york1.jpg")

def filter(img):
    image = Image.open(img)
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x,y))
            r = int(r * 1.1)
            image.putpixel((x,y), (r, g, b))
    image.save("result.jpg")

filter("york2.jpg")

result = Image.open("result.jpg")
result.show()