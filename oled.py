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
        self.oled.clear()
        self.oled.display()

    def num_with_exercise(self, num, unit, exercise):
        self.clear_image()
        self.draw.text((self.x, self.top), exercise, font=self.font_norm, fill=255)
        self.draw.text((self.x, self.top+25), str(num) + ' ' + unit, font=self.font_large, fill=255)
        self.disp()
    
    def challenge_block(self, text):

        self.clear_image()

        text_list = text.split()
        text_to_print = ""
        line_limit = 3
        line = 1

        while text_list and line <= line_limit:

            fit = True
            while fit and text_list:
                x_pos, y_pos = self.draw.textsize(text_to_print + text_list[0], font=self.font_norm)
                if x_pos <= 127:
                    text_to_print += (text_list.pop(0) + " ")
                else:
                    text_to_print += "\n"
                    fit = False
            line += 1

        self.draw.text((25, self.top), "Challenge", font=self.font_norm, fill=255)
        self.draw.multiline_text((self.x, self.top + 15), text_to_print, font=self.font_norm, spacing=3, fill=255)
        self.disp()

        #https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

    def challenge_records(self, records_list, unit, new_record):       #TODO: while waiting for button press, blink new record (if there is one)
        self.clear_image()
        if new_record:
            self.draw.text((self.x, self.top), "NEW RECORD!", font=self.font_norm, fill=255)

        text_to_print = ""
        for record in records_list:
            text_to_print += (record.rstrip('\n') + ' ' + unit + '\n')

        self.draw.multiline_text((self.x, self.top + 15), text_to_print, font=self.font_norm, spacing=3, fill=255)
        self.disp()

    def show_num(self, num, text):
        self.clear_image()
        self.draw.text((self.x, self.top), text, font=self.font_norm, fill=255)
        self.draw.text((self.x, self.top+20), str(num), font=self.font_huge, fill=255)
        self.disp()
    
    def show_time(self, recorded_time):
        self.clear_image()
        self.draw.text((self.x, self.top), str(recorded_time) + ' sec', font=self.font_large, fill=255)
        self.disp()