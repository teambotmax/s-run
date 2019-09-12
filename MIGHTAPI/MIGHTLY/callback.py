# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("[ ล็อกอินด้วยอีเมล ] กรุณาใส่รหัส '" + pin + "' บนอุปกรณ์มือถือ")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='หรือสแกนคิวอาร์โค้ด '
        else:
            notice=''
        self.callback('กดลิ้งค์นี้ใน 2 นาที \n' + url + '\nBy HuuMeaw')
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
