import telebot
from telebot import types
from datetime import timedelta,datetime
bot = telebot.TeleBot('6775254343:AAFQQBiTu5KpDwKWQuvKx6qvVzGw23lkScg')
@bot.message_handler(commands=['start'],func=lambda message: message.text)
def handledstart(message) :
    cname="cname"
    username="username"
    password="password"
    port="port"
    Server_Name=["asd","aef"]
    UsernameC="unamec"
    cardnames="cardnames"
    cardnum="cardnum"
    encodedup="encodedup"
    # line_of_dots = '.' * 10
    
    # formatted_string = f"""\nHostname: `{cname}` \nUsername: `{username}` \nPassword: `{password}` \nPort: `  {port}` \nServer: {Server_Name[0]} \nConfig Name:{UsernameC}\n{line_of_dots.center(50)} \nNetmod Desktop/ Android:\n `ssh://{username}:{password}@{cname}:{port}/#{username}`\n{line_of_dots.center(50)} \nv2Box   IPhone:\n`ssh://{username}:{password}@{cname}:{port}#{username}``\n{line_of_dots.center(50)}\nv2Box   Android:\n`ssh://{encodedup}=@{cname}:{port}#{username}`\n{line_of_dots.center(50)}\nبه کارت زیر واریز    شود:\nCardnumber: `{cardnum}`\nCARDNAME:{cardnames}\n{line_of_dots.center(50)}\nCname not created!"""
    line_length = 70
    line_of_dots = '`' * line_length
    def formatter(textmid):
        
        centered_text = f"{textmid}"
        return centered_text
    formatted_string = f"""
            {"```نپستر-نت```"}\nHostname: `{cname}` \nUsername: `{username}` \nPassword: `{password}` \nPort:`{port}        ` \nServer: {Server_Name[0]} \nConfig Name:{UsernameC}\n
            {"```NetMod-اندروید/ویندوز```"}\n`ssh://{username}:{password}@{cname}:{port}/#{username}`\n
            {"```V2box-آیفون```"}\n`ssh://{username}:{password}@{cname}:{port}#{username}`\n
            {"```V2box-اندروید```"}\n `ssh://{encodedup}=@{cname}:{port}#{username}`\n
            {"```اطلاعات-پرداخت```"}\nبه کارت زیر واریز شود:\nCardnumber: `{cardnum}`\nCARDNAME:{cardnames}\n
            {"```Alert! Cname not created!```"}
            """
    
    bot.send_message(message.chat.id, f"{formatted_string}",parse_mode='MarkdownV2')
bot.polling()



