from qrcode import QRCode


def make_qr():
    data = input("Enter the text or URL for the QR code: ")

    qr = QRCode()
    qr.add_data(data)

    return qr


def change_color(qr, main, background):
    """
    *main = the main color of the QR Code, that will be applied to the Squares.\n
    *background = the color given to the QR background.
    """
    img = qr.make_image(
        fill_color=main,
        back_color=background
    )
    return img


def make_img(qr):

    color = input("Do you have any color preference (Y/N): ").upper()
    if color == "Y":
        print("You can input either color name or RGB value")

        main_color = input("QR code (Default- black): ")
        bg_color = input("Background (Default- white): ")

        img = change_color(qr, main_color, bg_color)

    else:
        img = qr.make_image()

    return img


def save(img):
    file_name = input("Enter the filename: ")

    img.save(f"{file_name}.png")

    print(f"QR code saved as {file_name}.png")


def main():
    qr = make_qr()

    img = make_img(qr)

    save(img)


if __name__ == "__main__":
    main()
