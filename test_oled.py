import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


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


#----------------------------------------------------MY TEST AREA----------------------------------------------------
self.clear_image()

text = "My name is Brendon and I am a big boy that really needs a happy break"

text_list = text.split()

self.draw.multiline_text((self.x, self.top + 20), text, font=self.font_norm, fill=255)
self.disp()

