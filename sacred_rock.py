#import libraries for hc-sr04
import time
import board
import adafruit_hcsr04

#import libraries for memory display
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_sharpmemorydisplay

import textwrap
import random

#seting up paramaters for sonar
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D26)

# Colors
BLACK = 0
WHITE = 255

# Parameters to Change
FONTSIZE = 36
LEADING = 5
MAXCHARS = 23

FIELD = 60

EXIT = 80

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
scs = digitalio.DigitalInOut(board.D6)  # inverted chip select

display = adafruit_sharpmemorydisplay.SharpMemoryDisplay(spi, scs, 400, 240)

# Clear display.
display.fill(1)
display.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (display.width, display.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black background
draw.rectangle((0, 0, display.width, display.height), outline=BLACK, fill=BLACK)

# Load a TTF font.
font = ImageFont.truetype("/home/arthur/library/type/lapture_italic_1.ttf", FONTSIZE)

text = "The gods even envy those who are small and tender, who are free from pride, and free from attachment."

broke_last_cycle = False

while True:
    try:
        if(round(sonar.distance, 1)) <= FIELD:
            broke_last_cycle = False
            (font_width, font_height) = font.getsize(text)

            lines = textwrap.wrap(text, width=MAXCHARS)

            text_height = (len(lines) * (font_height + LEADING))
            max_line_width = 0

            for line in lines:
                (line_width, line_height) = font.getsize(line)
                if line_width > max_line_width:
                    max_line_width = line_width
                
            line_y = display.height // 2 - text_height // 2
            line_x = display.width // 2 - max_line_width // 2
            for line in lines:
                draw.text(
                    (line_x, line_y),
                    line,
                    font=font,
                    fill=WHITE,
                )
                line_y += (line_height + LEADING)
        if(round(sonar.distance, 1)) >= EXIT:
            broke_last_cycle = True
        if((round(sonar.distance, 1)) >= EXIT) and (broke_last_cycle):
            random_number = random.randint(1,27)
            if random_number == 1:
                text = "Through a slit in the belly a creature will be born with two heads and four arms: it will survive for some few years."
            elif random_number == 2:
                text = "They say the heavens look strange and foreign; and that the earth seems to have changed."
            elif random_number == 3:
                text = "The gods even envy those who are small and tender, who are free from pride, and free from attachment."
            elif random_number == 4:
                text = "Death carries off a man who is gathering flowers and whose mind is distracted, as a flood carries off a sleeping village."
            elif random_number == 5:
                text = "Death subdues a man who is gathering flowers, and whose mind is distracted, before he is satiated in his pleasures."
            elif random_number == 6:
                text = "Two chiefs elected, the first one will cause to death."
            elif random_number == 7:
                text = "Death will be held in the temple of Saint-Solonne, sacrificing he will consecrate festival smoke."
            elif random_number == 8:
                text = "The white corn will want to mix dew in the mineral: pasteur will follow the severe, the cross will pursue to death."
            elif random_number == 9:
                text = "They will be driven out put to death chased nude, into red and black will they convert their green."
            elif random_number == 10:
                text = "The Sun and the Eagle will appear to the victor. An empty answer assured to the defeated."
            elif random_number == 11:
                text = "At night the last one will be strangled in his bed."
            elif random_number == 12:
                text = "The shaven heads of the sects will be cut up."
            elif random_number == 13:
                text = "There will appear a shining ornate temple, lamp and the candle at Borne and Breteuil."
            elif random_number == 14:
                text = "When the light of mars will fall, seven months great war, people dead."
            elif random_number == 15:
                text = "He will come to convert them. The holy laws will be made in the Sun and Moon."
            elif random_number == 16:
                text = "Be thou blessed with the touch of the Lord of Mountains."
            elif random_number == 17:
                text = "Like a swan sitting in the floods he pants wisest in mind mid men he wakes at morn."
            elif random_number == 18:
                text = "A sage like Soma, sprung from Law, he grew like some young creature, mighty shining far."
            elif random_number == 19:
                text = "From the bottom of the hill a voice heard, be gone, be gone all of you on both sides."
            elif random_number == 20:
                text = "Great cow, everyone would be of it. One will be titled Kshetra."
            elif random_number == 21:
                text = "Liberty will not be recovered. A proud, vilanous wicked black one will occupy it."
            elif random_number == 22:
                text = "The city will be in great grief, vain and lightning"
            elif random_number == 23:
                text = "Two little feather falls down out of the sky, then he will bleed a great pain."
            elif random_number == 24:
                text = "In the places and times of flesh giving way to fish, the younger stone, the nectar will be divided."
            elif random_number == 25:
                text = "The Earth seems to have changed. The sun is hidden in the clouds, and the moon is obscured in the haze."
            elif random_number == 26:
                text = "A while after he will act very rudely, and he will at very warlike against the flower."
            else:
                text = "Evil ruin will fall upon the great one from the roof: they will accuse an innocent one of the deed."
            draw.rectangle((0, 0, display.width, display.height), outline=BLACK, fill=BLACK)
        print(round(sonar.distance, 1))      
    except RuntimeError:
        print("Retrying!")

    # Display image
    display.image(image)
    display.show()
    #draw.rectangle((0, 0, display.width, display.height), outline=BLACK, fill=BLACK)
