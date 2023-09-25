import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    # Get the text from the input field
    data = entry.get()
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create a PIL image from the QR code data
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert PIL image to PhotoImage for tkinter
    tk_img = ImageTk.PhotoImage(qr_img)
    
    # Display the QR code
    qr_label.config(image=tk_img)
    qr_label.photo = tk_img

# Create a tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Create an input field
entry_label = tk.Label(window, text="Enter data:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

# Start the tkinter main loop
window.mainloop()
