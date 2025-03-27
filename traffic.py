import os
import time
import json
import herepy
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk, BOTH, X, Toplevel
import tkinter.ttk as ttk
from tkinter.ttk import Frame, Label, Style, Progressbar

# Constants
WIDTH = 400
HEIGHT = 250

# HERE API Key
API_KEY = "5d0cTCrzeeLQCjcr1lb13znwcWdKxYxMSybGoDRsNEE"

# Function to Get Location Coordinates
def location(place):
    """Fetches latitude and longitude for a given place using HERE API."""
    geocoderApi = herepy.GeocoderApi(API_KEY)

    try:
        response = geocoderApi.free_form(place)
        s = json.loads(str(response))  # Convert response to JSON

        # Debugging: Print API response
        print(f"API Response for {place}: {json.dumps(s, indent=2)}")

        # Check if expected keys exist
        if "Response" in s and "View" in s["Response"]:
            view = s["Response"]["View"]
            if view and "Result" in view[0] and view[0]["Result"]:
                location_data = view[0]["Result"][0]["Location"]["DisplayPosition"]
                lat, lng = location_data["Latitude"], location_data["Longitude"]
                return f'{{{lat:.2f},{lng:.2f}}}'

        print(f"Warning: API response structure is incorrect for {place}.")
        return "{0.00,0.00}"  # Return default if API response fails

    except Exception as e:
        print(f"Error fetching location for '{place}': {e}")
        return "{0.00,0.00}"

# Dictionary to Store Locations
d = {
    1: "Big Ben  " + location("Big Ben"),
    2: "Gariahat  " + location("Gariahat"),
    3: "Jadavpur  " + location("Jadavpur"),
    4: "Times Square  " + location("Times Square"),
    5: "Rasbehari  " + location("Rasbehari"),
    6: "Garia  " + location("Garia"),
    7: "Tollygunge  " + location("Tollygunge"),
    8: "Chingrihata  " + location("Chingrihata"),
    9: "Saltlake  " + location("Salt Lake")
}

class Traffic(Toplevel):
    """Traffic Management System GUI"""

    def __init__(self):
        Toplevel.__init__(self)
        self.title("TRAFFIC MANAGEMENT SYSTEM")
        self.configure(background="white")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # Initialize UI for each road
        for i in range(1, 3):
            for j in range(1, 10):
                self.initUI(i, j, (j - 1) % 3 + 1, (j - 1) // 3 + 1)
            time.sleep(5)

    def initUI(self, path, pic, xi, yi):
        """Initializes UI components and updates traffic information."""
        
        # Construct the correct image file path
        image_path = os.path.join(str((path - 1) * 5), f"{pic}.jpg")

        # Check if the image exists
        if os.path.exists(image_path):
            try:
                stgImg = Image.open(image_path)
                stgImg = stgImg.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
                stgImg2 = ImageTk.PhotoImage(stgImg)
            except Exception as e:
                print(f"Error loading image '{image_path}': {e}")
                return
        else:
            print(f"Warning: Image '{image_path}' not found.")
            return

        # Read Traffic Data from CSV
        data_file = f"output{(path - 1) * 5}.csv"
        if os.path.exists(data_file):
            data = pd.read_csv(data_file, header=None)
            var = data.to_numpy()
        else:
            print(f"Error: CSV file '{data_file}' not found.")
            var = [[0, 0]] * 10  # Provide a default value

        # Create Label for Image
        label = Label(self, image=stgImg2)
        label.image = stgImg2
        label.place(x=543 * xi - 543 + 20, y=280 * yi - 300 + 10)

        # Progress Bar for Traffic
        label1 = Label(self)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

        progress = Progressbar(label1, style="red.Horizontal.TProgressbar", length=100, mode='determinate')
        progress['value'] = int(var[pic - 1][1] * 20)  # Convert CSV value to percentage

        # Time Label
        fn = f"{var[pic - 1][1]} mins"
        fn1 = d[pic]

        # Labels for time and location
        label2 = Label(self, text=fn, font="arial 12 bold", background="#f0d630")
        label2.place(x=543 * xi - 317 - 90, y=280 * yi - 50 + 17)

        label3 = Label(self, text=fn1, font="arial 12 bold", background="white")
        label3.place(x=543 * xi - 235.5 - 90, y=280 * yi - 50 + 18)

        progress.pack()
        label1.place(x=543 * xi - 540 + 20, y=280 * yi - 50 + 18)
        self.update_idletasks()


# Run Application
if __name__ == "__main__":
    root = Tk()
    root.title("Traffic Management System")
    root.configure(background="#f0eec5")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    
    # Start Traffic Management System
    app = Traffic()
    
    root.mainloop()
