from flask import request, json
from flask_restx import Namespace, Resource, reqparse
import telegram
import time

namespace = Namespace('bot', 'Bot use to send image to UI')

my_token = "5684369853:AAE1TFTYUavxqoxPjNy7GPhyfDPCYA2kLyE"
bot = telegram.Bot(token=my_token)

@namespace.route('/camera-new', methods=['GET'])
class GetImage(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(400, 'Not Found')
    @namespace.response(200, 'Success')
    def get(self):
        time.sleep(13)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/10_1/0.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!")
        time.sleep(1)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/10_1/1.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!")
        time.sleep(1)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/10_1/2.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!")
        
        return 'success'

@namespace.route('/camera-exist', methods=['GET'])
class GetImage(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(400, 'Not Found')
    @namespace.response(200, 'Success')
    def get(self):
        time.sleep(15)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/1/105.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!\nThời điểm vi phạm: 08:15 19/12/2022\nĐịa điểm: Phố Hàng Bông, Quận Hoàn Kiếm, Hà Nội")
        time.sleep(4)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/1/129.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!\nThời điểm vi phạm: 10:23 19/12/2022\nĐịa điểm: Phố Hàng Bông, Quận Hoàn Kiếm, Hà Nội")
        time.sleep(6)
        bot.sendPhoto(chat_id="5638388061", photo=open('./img/1/220.jpg', "rb"), caption="Phát hiện phương tiện vi phạm!!!\nThời điểm vi phạm: 16:45 19/12/2022\nĐịa điểm: Phố Hàng Bông, Quận Hoàn Kiếm, Hà Nội")
        
        return 'success'