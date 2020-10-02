from config import token
import telebot
import pdb
from utils import log, show_err

bot = telebot.TeleBot(token)

        

@bot.message_handler(commands=['photo'])
def send_video(msg):
    log(msg)
    try:
        bot.send_photo(msg.chat.id, 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F39110%2Fpexels-photo-39110.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26fit%3Dcrop%26h%3D627%26w%3D1200&f=1&nofb=1', timeout=5)
    except:
        show_err(msg, bot)
        
@bot.message_handler(commands=['location'])
def send_video(msg):
    log(msg)
    try:
        bot.send_location(msg.chat.id, latitude=50, longitude=50)
    except:
        show_err(msg, bot)
        
@bot.message_handler(commands=['music'])
def send_audio(msg):
    log(msg)
    try:
        f = open('files/Lorn_-_Acid_Rain_60240932.mp3', 'rb')
        bot.send_audio(msg.chat.id, f)
    except:
        show_err(msg, bot)
    
   

@bot.message_handler(content_types=['text'])
def repeat_all_messages(msg):
    log(msg)
    try: 
        bot.send_message(msg.chat.id, msg.text)
    except:
        show_err(msg, bot)
    
@bot.message_handler(content_types=['sticker'])
def repeat_all_stickers(msg):
    log(msg)
    try:
        bot.send_sticker(msg.chat.id, msg.sticker.file_id)
    except:
        show_err(msg, bot)


if __name__ == '__main__':
    print("Bot awaits messages")
    bot.infinity_polling()