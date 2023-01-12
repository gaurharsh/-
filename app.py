import tkinter as tk
import pyqrcode
from PIL import Image,ImageTk


# Create a tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Create a label and text entry for the URL
url_label = tk.Label(root, text="Enter URL:")
url_entry = tk.Entry(root)

# Create a function to generate the QR code
def generate_qr():
       # Get the URL from the text entry
        # Get the URL from the text entry
    url = url_entry.get()
    # Create a QR code object from the UR  L
    qr = pyqrcode.create(url)
    qr.png("BABA/qr.png",scale=6)
    qr_image =tk.PhotoImage(file="BABA/qr.png")
    qr_label = tk.Label(root, image=qr_image)
    qr_label.image = qr_image
    qr_label.pack()

generate_button = tk.Button(root,text="Generate QR Code",command=generate_qr)
url_label.pack()
url_entry.pack()
generate_button.pack()

root.mainloop()
