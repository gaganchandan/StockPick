import config
from tkinter import *
from PIL import ImageTk, Image
import os
import datetime
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Run get.py to ensure that the latest data is available
os.system("python3 " + os.path.join(config.root, "data", "get.py"))
# Generate calls using scan.py
process = subprocess.Popen(
    ["python3", os.path.join(config.root, "stockpick", "scan.py")])
(calls, err) = process.communicate()
exit_code = process.wait()


# Function to plot price chart
def plot_price_chart():
    symbol = stock.get()
    if symbol not in config.symbols:
        print("Invalid symbol")
        return
    end = datetime.date(2023, 2, 1)
    start = end - datetime.timedelta(days=90)
    file = os.path.join(config.root, "data", (symbol + '.csv'))
    data = pd.read_csv(file, index_col=False)
    data = data[['Date', 'Close']]
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    data = data.loc[start:end]
    data.plot(figsize=(16, 9))
    plt.show()


# GUI
window = Tk()
window.title("STONKS PICKER")
window.config(padx=10, pady=10, bg="#7a3530")
canvas = Canvas(width=1080, height=676, bg="#7a3530", highlightthickness=0)
img = ImageTk.PhotoImage(Image.open(os.path.join(
    config.root, "images", "stonks_image.jpeg")))


canvas.create_image(540, 338, image=img)
stock_compute = Button(text="COMPUTE", font=(
    "Arial", 15, "bold"), bg="#7a3530", fg="white", command=plot_price_chart)
stock = Entry(width=20)
Display = Label(text="THIS IS A TEST", font=("Arial", 30, "bold"),
                bg="white", fg="white", width=15, height=15)

canvas.grid(row=0, column=0, columnspan=6)


stock.grid(row=1, column=3)
stock_compute.grid(row=2, column=3)
Display.grid(row=3, column=3)

window.mainloop()


# Button2 = Button(text="Butto", font=("Arial", 20, "bold"), bg="#7a3530", fg="white")
# Button2.grid(row=1,column=4)
# canvas.create_text(540,338,text="STOCKS PICKER",font=("Arial",30,"bold"),fill="white")
# title_label=Label(text="STOCK PICKER",font=("Arial",30,"bold"),bg="#7a3530",fg="white")
