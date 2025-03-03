from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("flr.jpg") 
        
        #Angle given
        img = img.rotate(180) 
        
         #Saved in the same relative location
        img.save("rotated_flr.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("flr.jpg")
        width, height = img.size
        
        area = (0, 0, width/2, height/2)
        img = img.crop(area)
        
        #Saved in the same relative location
        img.save("cropped_flr.jpg") 
        
    except IOError:
        pass

if __name__ == "__main__":
    main()
from PIL import Image

def main():
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open("flr.jpg") 
        
        #Relative Path
        #Image which we want to paste
        img2 = Image.open("flr1.jpg") 
        img.paste(img2, (50, 50))
        
        #Saved in the same relative location
        img.save("pasted_flr.jpg")
        
    except IOError:
        pass

if __name__ == "__main__":
    main()

##An additional argument for an optional image mask image is also available.
    from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("flr.jpg") 
        
        #transposing image 
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        #Save transposed image
        transposed_img.save("transposed.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
def main():
    try:
        #Relative Path
        img = Image.open("flr.jpg") 
        print img.mode
        
        #converting image to bitmap
        print img.tobitmap()
        
        print type(img.tobitmap())
    except IOError:
        pass

if __name__ == "__main__":
    main()
