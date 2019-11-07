from pyrobot import BOT
from pyrogram import Filters, Message
from clarifai.rest import Image as celeb
from clarifai.rest import ClarifaiApp
capp = ClarifaiApp(api_key='687797d9ad5144cbb55b3ef806f569ee')
from clarifai.rest import ClarifaiApp
model2 = capp.models.get('celeb-v1.3')


@BOT.on_message(Filters.user(['me']) & Filters.reply & Filters.command('guess', '!'))
def img(bot: BOT, message: Message):
    if message.reply_to_message.photo:
        BOT.download_media(message.reply_to_message.photo.sizes[-1].file_id, '/home/UB/tmp/img.jpg')
        image = celeb(file_obj=open('/home/UB/tmp/img.jpg', 'rb'))
        cons = ''
        response = model2.predict([image])
        concept = response['outputs'][0]['data']['regions'][0]['data']['face']['identity']['concepts'][0]
        message.reply(concept['name'].title(), quote=True)
