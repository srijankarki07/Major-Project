import tkinter as tk
from tkinter import filedialog
from hemorrhage_detection import load_trained_model, predict_hemorrhage
from PIL import ImageTk, Image

# Function to handle the "Browse" button click event
def browse_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display the selected image
        show_selected_image(file_path)
        # Predict whether the image represents hemorrhage or not
        prediction = predict_hemorrhage(model, file_path)
        prediction_label.config(text="Prediction: " + prediction)

# Function to display the selected image
def show_selected_image(file_path):
    img = Image.open(file_path)
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

# Create Tkinter window with specified size and banner background
window = tk.Tk()
window.title("Hemorrhage Detection")
window.geometry("700x700")

# Create header
header_label = tk.Label(window, text="Brain Hemorrhage Detection Using CT Images", font=('Arial Bold', 16))
header_label.pack(padx=10, pady=10, ipadx=10)

# Path to the trained model
model_path = 'C:\Major project\Code\model.hdf5'
# Load the trained model
model = load_trained_model(model_path)


# Create label to display prediction
prediction_label = tk.Label(window, text="", font=('Arial', 14))  # Adjust font size as needed
prediction_label.place(x=180, y=60)  

# Create panel to display the selected image
panel = tk.Label(window)
panel.place(x=150, y=100)

# Create "Browse" button
browse_button = tk.Button(window, text="Insert Your CT Images", command=browse_image)
browse_button.place(x=270, y=550)

# Run the Tkinter event loop
window.mainloop()
