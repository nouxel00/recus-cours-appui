import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root/'src'/'index.src.html').read_text(encoding='utf-8')
qr = (root/'src'/'qrcode.min.js').read_text(encoding='utf-8')
out = src.replace('/*QR_LIB*/', qr)
assert out != src
(root/'index.html').write_text(out, encoding='utf-8')
print('index.html', len(out))
