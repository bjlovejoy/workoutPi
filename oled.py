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
        self.image = Image.new('1', (self.width, self.height))

        self.draw = ImageDraw.Draw(self.image)                           #Get drawing object to draw on image
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)  #Draw a black filled box to clear the image

        #Define some constants to allow easy resizing of shapes
        padding = -2
        self.top = padding
        self.bottom = self.height - padding
        self.x = 0  #Move left to right keeping track of the current x position for drawing shapes

        #self.font = ImageFont.load_default()
        self.font_small = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 10)
        self.font_norm = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 15)
        self.font_large = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 30)
        self.font_huge = ImageFont.truetype("/home/pi/workoutPi/arial.ttf", 40)
                                                #https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
    
    def disp(self):
        self.oled.image(self.image)
        self.oled.display()

    def clear_image(self):
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        self.disp()

    def num_with_exercise(self, num, unit, exercise):
        self.clear_image()
        self.draw.text((self.x, self.top), exercise, font=self.font_norm, fill=255)
        self.draw.text((self.x, self.top+25), str(num) + ' ' + unit, font=self.font_large, fill=255)
        self.disp()
    
    def text_block(self, text):                             #TODO: fix this, not working
        self.clear_image()
        self.draw.multiline_text((self.x, self.top), text, font=self.font_norm, fill=255)

        
        #TODO: break string up by num characters fit on one line (limit lines and print error if over, don't exit script)
        #insert newlines to do multiline text (could split text on spaces and word wrap)
        #TODO: create 2 logs: regular operation and errors
        #https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

    def show_num(self, num, text):
        self.clear_image()
        self.draw.text((self.x, self.top), text, font=self.font_norm, fill=255)
        self.draw.text((self.x, self.top+20), str(num), font=self.font_huge, fill=255)
        self.disp()
    
    def show_time(self, recorded_time):
        self.clear_image()
        self.draw.text((self.x, self.top), str(recorded_time) + ' sec', font=self.font_large, fill=255)
        self.disp()