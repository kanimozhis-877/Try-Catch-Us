import io, qrcode
def make_qr(data):
    qr=qrcode.QRCode(box_size=8,border=2); qr.add_data(data); qr.make(fit=True)
    image=qr.make_image(); out=io.BytesIO(); image.save(out, format="PNG"); return out.getvalue()
