import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class OLED:
    def __init__(self):
        self.oled = Adafruit_SSD1306.SSD1306_128_64(rst=None)

        self.oled.begin()    #Initialize library
        self.oled.clear()    #Clear display
        self.oled.display()  #Update display

        #Create blank image for drawing (mode '1' for 1-bit color)
        self.width = self.oled.width
        self.height = self.oled.height
        self.image = Image.new('1', (width, height))

        self.draw = ImageDraw.Draw(image)                           #Get drawing object to draw on image
        self.draw.rectangle((0,0,width,height), outline=0, fill=0)  #Draw a black filled box to clear the image

        #Define some constants to allow easy resizing of shapes
        self.padding = -2
        self.top = padding
        self.bottom = height - padding
        self.x = 0  #Move left to right keeping track of the current x position for drawing shapes

        self.font = ImageFont.load_default()    #try:     arial_large = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 70)
                                                #https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
    
    def disp(self):
        self.oled.image(image)
        self.oled.display()

    def clear_image(self):
        self.draw.rectangle((0,0,width,height), outline=0, fill=0)
        self.disp()

    def num_with_exercise(self, num, unit, exercise):
        self.clear_image()
        self.draw.text((self.x, self.top), num + ' ' + unit, font=font, fill=255)
        self.draw.text((self.x, self.top+8), exercise, font=font, fill=255)
        self.disp()
    
    def text_block(self, text):
        self.clear_image()
        self.draw.multiline_text((self.x, self.top), num + ' ' + unit, font=font, fill=255)

        
        #TODO: break string up by num characters fit on one line (limit lines and print error if over, don't exit script)
        #insert newlines to do multiline text (could split text on spaces and word wrap)
        #TODO: create 2 logs: regular operation and errors
        #https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

    def show_num(self, num):
        self.clear_image()
        self.draw.text((self.x, self.top), num, font=font, fill=255)
        self.disp()
    
    def show_time(self, recorded_time):
        self.clear_image()
        self.draw.text((self.x, self.top), recorded_time + ' sec', font=font, fill=255)
        self.disp()