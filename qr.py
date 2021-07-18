import pyqrcode

def qrcode():
    q=pyqrcode.create(input("Text to qr code converter: "))
    q.png('qrcode.png',scale=6)
    print('QR generated')

if __name__=='__main__':
    qrcode()    