import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


oled = Adafruit_SSD1306.SSD1306_128_64(rst=None)

oled.begin()    #Initialize library
oled.clear()    #Clear display
oled.display()  #Update display

#Create blank image for drawing (mode '1' for 1-bit color)
width = oled.width
height = oled.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)                           #Get drawing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0)  #Draw a black filled box to clear the image

#Define some constants to allow easy resizing of shapes
padding = -2
top = padding
bottom = height - padding
x = 0  #Move left to right keeping track of the current x position for drawing shapes

#self.font = ImageFont.load_default()
font_small = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 10)
font_norm = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 15)
font_large = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 30)
font_huge = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 40)


#----------------------------------------------------MY TEST AREA----------------------------------------------------
text1 = "My name is Brendon and I am a big boy that really needs a happy break"
text2 = "aaaaa"

text_list = text1.split()
text_to_print = ""
line_limit = 3
line = 1

while text_list and line <= line_limit:

    fit = True
    while fit and text_list:
        x_pos, y_pos = draw.textsize(text_to_print + text_list[0], font=font_norm)
        if x_pos <= 128:
            text_to_print += (text_list.pop(0) + " ")
        else:
            text_to_print += "\n"
            fit = False
    line += 1

draw.multiline_text((x, top + 15), text_to_print, font=font_norm, spacing=3, fill=255)
oled.image(image)
oled.display()

