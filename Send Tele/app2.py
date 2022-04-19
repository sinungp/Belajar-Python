import telepot


token = 'YOUR TOKEN' # telegram token
receiver_id = YOUR ID # https://api.telegram.org/bot<TOKEN>/getUpdates


bot = telepot.Bot(token)

bot.sendMessage(receiver_id, 'TEST PESAN DARI PYTHON KE TELEGRAM.') # send a activation message to telegram receiver id

# bot.sendPhoto(receiver_id, photo=open('ip.txt', 'rb')) # send message to telegram
