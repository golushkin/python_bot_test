import sys

def show_err(msg, bot):
    cls_name, msg, stack = sys.exc_info()
    print('-'*50)
    print("{}: {}".format(cls_name, msg))
    print(stack)
    print('-'*50)
    bot.send_message(msg.chat.id, "Something bad has happend")
     
def log(msg):
    print('-'*50)
    print("Bot gets message from {}({}) \nchat - {}".format(msg.from_user.first_name, msg.from_user.username,msg.chat.id))
    print('-'*50)