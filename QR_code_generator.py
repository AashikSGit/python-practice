from qrcode import QRCode

data = input("Enter the text or URL for the QR code: ")
file_name = input("Enter the filename: ")

qr = QRCode()
qr.add_data(data)

img = qr.make_image()

img.save(f"{file_name}.png")

print(f"QR code saved as {file_name}.png")
