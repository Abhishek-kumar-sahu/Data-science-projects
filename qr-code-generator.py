from PIL import Image
import segno
qrcode=segno.make("https://www.youtube.com/watch?v=bDCMXR8yRVg")
qrcode.save("qrcode.png",scale=10,light="red", dark="darkblue")
print("OK DONE")


image = Image.open("qrcode.png")
image.show()