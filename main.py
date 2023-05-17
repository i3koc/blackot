from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options # Import the Options class for Firefox
import time
import telebot

# Replace this with your API token from @BotFather
TOKEN = "5990384804:AAHOHAm7CYumhgGaaiYIzWXfr2xiDYMQdo8"

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TOKEN)

# Define a message handler for the /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, """

ياهلا والله ,
تــقدر ترســـل رابط المـــــحاضرة للبوت بأي وقت
وهو يعطيك الرابط المصدري. للتواصل @i3koc

    """)

# Define a message handler for any text message
@bot.message_handler(func=lambda m: True)
def get_video_source(message):
    # Get the URL from the message text
    url = message.text

    # Create a webdriver instance and open the URL
    firefox_options = Options() # Create an Options object for Firefox
    firefox_options.add_argument("--headless") # Add the --headless argument to run Firefox in headless mode
    driver = webdriver.Firefox(options=firefox_options) # Pass the options to the driver
    driver.get(url)

    # Wait for 10 seconds for the page to load
    time.sleep(10)

    # Find all elements with the class name "vjs-tech"
    elements = driver.find_elements(By.CLASS_NAME, "vjs-tech")

    # Loop through the elements and get their src attribute
    for element in elements:
        src = element.get_attribute("src")

        # Send the src as a reply to the message
        bot.reply_to(message, src)

    # Close the driver
    driver.close()

# Start polling for incoming messages
bot.polling()