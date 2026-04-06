import qrcode
qr=qrcode.make("https://www.instagram.com/soumyajit__bhowmik?igsh=djR4NnVyaGl6c2Zk")
qr.save("My_Insta_qr.png")
print("QR code generated sucessfully")