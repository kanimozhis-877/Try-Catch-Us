import qrcode


def make_qr(
    token: str
):

    qr = qrcode.QRCode(
        version=1,

        box_size=10,

        border=4
    )


    qr.add_data(token)

    qr.make(
        fit=True
    )


    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )


    from io import BytesIO

    buffer = BytesIO()

    image.save(
        buffer,
        format="PNG"
    )


    return buffer.getvalue()