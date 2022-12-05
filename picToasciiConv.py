from PIL import Image


def get_ascii_image():
    picture_path = input("Введите путь к файлу с картинкой: ")
    #picture_path = "./emoji.jpg"
   # ascii_picture_file = input("Введите путь к файлу, в котором вы хотите сохранить ASCII аналог картинки: ")

    with Image.open(picture_path) as picture:

        # resizing picture
        width, height = picture.size
        aspect_ratio = height / width
        width_new = 150
        height_new = int(aspect_ratio * width_new * 0.4)
        picture = picture.resize((width_new, height_new))

        picture = picture.convert("L")
        pixels = picture.getdata()

        chars = ".,-~:;=!*#$@"[::-1]
        print(chars)
        new_pixels = [chars[pixel // 22] for pixel in pixels]
        new_pixels = ''.join(new_pixels).replace(".", " ")

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + width_new] for index in range(0, new_pixels_count, width_new)]
        ascii_image = "\n".join(ascii_image)

        print(ascii_image)




get_ascii_image()





