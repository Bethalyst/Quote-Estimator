

# 🧩 Project Break-Down
### *FinalProject.py – BSH Cleaning Quote Estimator & Job Scheduler*

This README explains the main parts of the program — why each code block exists and what purpose it serves.  
It’s written in a simple, beginner-friendly way to show my thought process while building the project.

## 1️⃣ Import Section
```python
import os
import tkinter as tk
from breezypythongui import EasyFrame

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = ImageTk = None 
```
Why I started with these statements:
- os: For file path management.
- tkinter: GUI (graphical user interface) foundation.
- breezypythongui: Simplifies Tkinter UI creation with EasyFrame class.
- PIL (Pillow): Handles image loading/resizing.
- try/except makes sure the app still runs even if Pillow isn’t installed.

## 2 Main Window setup
```python
class MainMenu(EasyFrame):
    def __init__(self):
        super().__init__(title="BSH Cleaning", background="lightgreen")
```
*Purpose*

The defines the main window (MainMenu) the first screen users see.
It inherits from EasyFrame, which means I can easily add labels, buttons, and other widgets.
The *super().__init__()* line sets the title bar and background color for the app.
"BSH Cleaning" is the app name and matches my cleaning business idea 

## 3️⃣ Banner Image Setup
```python
baseDir = os.path.dirname(os.path.abspath(__file__))
bannerPath = os.path.join(baseDir, "istockphoto-1318525310-612x612.jpg")
```
*Purpose*

I wanted the app to find the banner image even if someone moves the folder.
os.path.dirname *(os.path.abspath(__file__)*) gives the script’s folder location.
Then I join that path with the image name so the image always loads correctly.

## 4 Load and Display Banner Image
```python
if Image and ImageTk:
    try:
        banner = Image.open(bannerPath)
        banner = banner.resize((580, 120), resample=Image.LANCZOS)
        self.bannerPhoto = ImageTk.PhotoImage(banner)
        tk.Label(self, image=self.bannerPhoto, bg="lightgreen").grid(row=0, column=0, columnspan=4, sticky="nsew")
```
*Purpose*
It checks if Pillow is installed (if Image and ImageTk).
Opens and resizes the banner to fit nicely at the top of the app.
Converts it into a format Tkinter can display (PhotoImage).
Uses a Tkinter Label to show the banner image at the top row of my layout grid.

## 5️⃣Banner Fallback Options
```python
except FileNotFoundError:
    self.addLabel(text="[Banner not found]", row=0, column=0, columnspan=4, background="lightgreen", foreground="white")
else:
    self.addLabel(text="[Pillow not installed]", row=0, column=0, columnspan=4, background="lightgreen", foreground="white")
```
*Purpose*
If the banner file is missing, it still shows a text label instead of crashing.
If Pillow isn’t installed at all, it shows a message letting me know.
This helps debug problems easily and keeps the UI clean even if something fails.

## 6 Welcome Text & Main Buttons
``` python
self.addLabel(
    text="Welcome to BSH Cleaning",
    row=1, column=0, columnspan=4,
    background="lightgreen",
    foreground="white",
    font=("Arial", 18, "bold")
)

self.addButton(text="Quote Estimator", row=2, column=0, command=self.openQuote)
self.addButton(text="Job Scheduler",   row=2, column=1, command=self.openScheduler)
self.addButton(text="Exit",            row=2, column=3, command=self.exitProgram)
```
*Purpose*
Adds a welcome label to greet the user.
Creates three main navigation buttons:
Quote Estimator – opens the quote calculator.
Job Scheduler – opens the scheduling form.
Exit – closes the app.
These buttons make it easy to move between different tools.

## 7️⃣ Navigation Functions
``` python
def openQuote(self):
    self.destroy()
    QuoteEstimator().mainloop()

def openScheduler(self):
    self.destroy()
    JobScheduler().mainloop()

def exitProgram(self):
    self.quit()
```
*Purpose*
Each function handles moving between windows.
- *destroy()* closes the current screen, then opens a new one.
- *mainloop()* starts the new window loop so it stays visible.
- *exitProgram()* cleanly exits the entire program.

## 8 Quote Estimator Buttons
``` python
self.addButton(text="Calculate", row=2, column=0, command=self.calculateQuote)
self.addButton(text="Clear", row=2, column=1, command=self.clearFields)
self.addButton(text="Back", row=2, column=2, command=self.goBack)
self.addButton(text="Exit", row=2, column=3, command=self.exitProgram)
```
*Purpose*
These Buttons give users control:
**Calculate**: runs the quote formula.
**Clear**: resets the input boxes.
**Back**: returns to the main menu.
**Exit**: quits the app.

## :fax: Quote Calculation Logic
```python
def calculateQuote(self):
    sqft = self.sqftEntry.getNumber()
    rate = self.rateEntry.getNumber()
    if sqft < 0 or rate < 0:
        self.messageBox(title="Error", message="Values must be non-negative.")
        return
    total = sqft * rate
    self.messageBox(title="Quote", message=f"Estimated Cost: ${total:.2f}")
```
*Purpose*
Reads the values the user typed in, Checks that both numbers are positive.
Multiplies square footage × rate to get the total.
Shows the result in a pop-up message box.

## :lock_with_ink_pen: Quote Utility Functions
```python
def clearFields(self):
    self.sqftEntry.setNumber(0.0)
    self.rateEntry.setNumber(0.0)

def goBack(self):
    self.destroy()
    MainMenu().mainloop()

def exitProgram(self):
    self.quit()
```
*Purpose*
**clearFields:** resets the inputs for a new calculation.
**goBack:** closes the quote window and reopens the main menu.
**exitProgram:** exits the program completely.

## 🗓️Job Scheduler Window
```python
class JobScheduler(EasyFrame):
    def __init__(self):
        super().__init__(title="Job Scheduler", background="lightgreen")
```
*Purpose*
Adds another tool inside the app — the Job Scheduler.
Lets the user plan cleaning jobs by date and time.

## ⏰ Job Scheduler Fields & Buttons
```python 
self.addLabel(text="Job Date (YYYY-MM-DD):", row=0, column=0, background="lightgreen", foreground="white")
self.dateEntry = self.addTextField(text="", row=0, column=1)

self.addLabel(text="Time (HH:MM):", row=1, column=0, background="lightgreen", foreground="white")
self.timeEntry = self.addTextField(text="", row=1, column=1)

self.addButton(text="Schedule", row=2, column=0, command=self.scheduleJob)
self.addButton(text="Clear", row=2, column=1, command=self.clearFields)
self.addButton(text="Back", row=2, column=2, command=self.goBack)
self.addButton(text="Exit", row=2, column=3, command=self.exitProgram)
```
*Purpose*
Two text boxes collect date and time for a cleaning job.
Buttons let users schedule, clear, go back, or exit.
Uses the same consistent color and layout for design unity.

# ✅ Job Scheduling Logic
``` python
def scheduleJob(self):
    dateStr = self.dateEntry.getText()
    timeStr = self.timeEntry.getText()
    self.messageBox(title="Scheduled", message=f"Job set for {dateStr} at {timeStr}.")
```
*Purpose*
Displays a message confirming that the job has been set.
For now it’s a basic confirmation, but it could be expanded later to save data or connect to a calendar.

## 🔚 Program Entry Point
```python
if __name__ == "__main__":
    MainMenu().mainloop()
```
*Purpose*
This tells Python what to run first.
When the file is opened directly, it launches the Main Menu window.
*mainloop()* keeps the GUI active until the user closes it.






