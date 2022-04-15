import telepot


token = '5371063625:AAGuxLU8Cw2V2v09n9PUGXqC-nnNdWWO-DA' # telegram token
receiver_id = 450126196 # https://api.telegram.org/bot<TOKEN>/getUpdates


bot = telepot.Bot(token)

bot.sendMessage(receiver_id, 'TEST PESAN DARI PYTHON KE TELEGRAM.') # send a activation message to telegram receiver id

# bot.sendPhoto(receiver_id, photo=open('ip.txt', 'rb')) # send message to telegram
