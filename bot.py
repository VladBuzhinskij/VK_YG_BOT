from datetime import datetime
import telebot
import conf,vk_bt,text,fil,model
from telebot import types
import time
from random import randint


now = int( time.time() )

# ch_wom_choes='-1001571931302'

bot = telebot.TeleBot(conf.tok_tg)

while True:
    tttt = time.localtime()
    current_time = time.strftime("%H%M", tttt)
    tii: int = int(time.strftime("%H%M", tttt))
    if tii>=1200 and tii<1201:
        for i in range(0,len(text.data_ch)):
            
            fil.read_file()
            ch_vk=text.data_ch[i][0]
            ch_tg=text.data_ch[i][1]
            ch_tg_tz=text.data_tiz
            updt_tg=text.data_ch[i][2]
            base_vk=list(vk_bt.vk_pars (ch_vk,updt_tg))
            now = int( time.time() )
            text.data_ch[i][2]=int(now)
            fil.write_file()
            st=model.category (i+1)
            st2=model.category_ch (i+1)
            if len(base_vk)!=0:
                for j in base_vk:
                    photo_url=j[2]
                    rez_photo_url=j[3]
                    caption=j[1]
                    try:
                        bot.send_photo(ch_tg, photo=photo_url, caption=caption)
                    except Exception as er:
                        
                        time.sleep(60)
                        try:
                            bot.send_photo(ch_tg, photo=rez_photo_url, caption=caption)
                        except Exception as er:
                             
                             time.sleep(60)
                    time.sleep(5)
                
                tz_base=list()
                if len(base_vk)>5:
                    for ii in range(0,3):
                        tz_base.append(base_vk[randint(0,len(base_vk)-1)])
                else:
                    tz_base.append(base_vk[0])
                for iii in tz_base:
                    
                    try:
                        
                        bot.send_photo(ch_tg_tz, photo=iii[2], caption=iii[1])
                        
                    except Exception as er:


                        time.sleep(60)
                bot.send_message(ch_tg_tz, text=f'{st}')

                    
                
            
            time.sleep(20)
        
    time.sleep(40)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Обновить все")
#     markup.add(btn1)
#     ms=bot.send_message(message.chat.id, text="Меню",reply_markup=markup)

    
# # bot.send_message(414254071,text='hello')
# @bot.message_handler(regexp='Обновить все')
# def func(message):
        
            
#         for i in range(0,len(text.data_ch)):
            
#             fil.read_file()
#             ch_vk=text.data_ch[i][0]
#             ch_tg=text.data_ch[i][1]
#             ch_tg_tz=text.data_tiz
#             updt_tg=text.data_ch[i][2]
#             base_vk=list(vk_bt.vk_pars (ch_vk,updt_tg))
#             now = int( time.time() )
#             text.data_ch[i][2]=int(now)
#             fil.write_file()
#             st=model.category (i+1)
#             st2=model.category_ch (i+1)
#             if len(base_vk)!=0:
#                 for j in base_vk:
#                     photo_url=j[2]
#                     rez_photo_url=j[3]
#                     caption=j[1]
#                     try:
#                         bot.send_photo(ch_tg, photo=photo_url, caption=caption)
#                     except Exception as er:
                        
#                         time.sleep(60)
#                         try:
#                             bot.send_photo(ch_tg, photo=rez_photo_url, caption=caption)
#                         except Exception as er:
#                              bot.send_message(message.chat.id, text=f'Ошибка:   {er}')
#                              bot.send_message(message.chat.id, text=f'не удалось отправить фотов канал{st2}:  {caption}')
#                              time.sleep(60)
#                     time.sleep(5)
                
#                 tz_base=list()
#                 if len(base_vk)>5:
#                     for ii in range(0,3):
#                         tz_base.append(base_vk[randint(0,len(base_vk)-1)])
#                 else:
#                     tz_base.append(base_vk[0])
#                 for iii in tz_base:
                    
#                     try:
                        
#                         bot.send_photo(ch_tg_tz, photo=iii[2], caption=iii[1])
                        
#                     except Exception as er:
#                         bot.send_message(message.chat.id, text=f'не удалось отправить фото в общий канал:  {caption}')
#                         bot.send_message(message.chat.id, text=f'Ошибка:   {er}')

#                         time.sleep(60)
#                 bot.send_message(ch_tg_tz, text=f'{st}')

                    
#                 bot.send_message(message.chat.id, text=f'обновилcя канал {st2}')
#             else: bot.send_message(message.chat.id, text=f'обновление канала {st2} не требуется')
#             time.sleep(20)
            


# @bot.message_handler(content_types=['text'])
# def messages_handler(message):
#     print('1')
#     if message.forward_from_chat:
#         chat_id = message.forward_from_chat.id
#         print(chat_id)
        
         

             
            
            
        
        
        
        
        
        


# bot.polling(none_stop=True)
# bot.infinity_polling()

