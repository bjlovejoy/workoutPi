sudo apt update
sudo apt upgrade

#enable i2c interface using
#sudo raspi-config

#The following libraries may already be installed but run these commands anyway to make sure :
sudo apt install -y python3-dev
sudo apt install -y python-smbus i2c-tools
sudo apt install -y python3-pil
sudo apt install -y python3-pip
sudo apt install -y python3-setuptools
sudo apt install -y python3-rpi.gpio

#With the I2C libraries installed I used the i2cdetect command to find the module on the I2C bus
echo -e "\n\n"
i2cdetect -y 1     #or i2cdetect -y 0
echo -e "\n\n"

#clone and install adafruit's library
cd /home/pi
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
sudo python3 Adafruit_Python_SSD1306/setup.py install

#install python moudles
sudo pip3 install gpiozero
sudo pip3 install colorzero
