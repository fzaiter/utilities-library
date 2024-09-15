from PIL import Image
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer


def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_code = qr.make_image(image_factory=StyledPilImage,
                            module_drawer=CircleModuleDrawer())
    qr_code.save('Generated-QR.png')
    print("QR saved as: Generated-QR.png")


def main():
    link = input("Enter text to convert to QR code: ")
    generate_qr_code(link)


if __name__ == "__main__":
    main()
