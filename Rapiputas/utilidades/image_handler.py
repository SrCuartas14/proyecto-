from PIL import Image, ImageTk

def resize_image(image_path, size=(150, 150)):
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)