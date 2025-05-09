

"""
Quote Estimator app quickly calculates cleaning job costs so you can give customers fast, accurate prices.
Helps you estimate how much to charge a customer based on the size of the space and your set price per square foot. 
{You can update your rate anytime}
Job Scheduler app keep track of when and where your jobs are happening, so you never miss an appointment.
Lets you schedule jobs by date and time, so you can track when you need to show up. Once they approve, 
you pop over to the Job Scheduler and lock in the date/time.
"""



"""

IMPORTANT: Before running FinalProject.py, make sure to extract the zip file! 
Running directly from inside the zip will cause a FileNotFoundError.
 PS. You must have PIP already installed

"""



import os
import tkinter as tk
from breezypythongui import EasyFrame

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = ImageTk = None

class MainMenu(EasyFrame):
    def __init__(self):
        super().__init__(title="BSH Cleaning", background="lightgreen")

        # 1) Build the absolute path to the banner JPG
        baseDir = os.path.dirname(os.path.abspath(__file__))
        bannerPath = os.path.join(
            baseDir,
            "istockphoto-1318525310-612x612.jpg"
        )

        # 2) Try loading & resizing it with Pillow (LANCZOS replaces ANTIALIAS)
        if Image and ImageTk:
            try:
                banner = Image.open(bannerPath)
                banner = banner.resize((580, 120), resample=Image.LANCZOS)
                self.bannerPhoto = ImageTk.PhotoImage(banner)
                # <-- HERE: use tk.Label instead of addLabel(image=...)
                tk.Label(self, image=self.bannerPhoto, bg="lightgreen") \
                  .grid(row=0, column=0, columnspan=4, sticky="nsew")
            except FileNotFoundError:
                # fallback to text-only Breezy label
                self.addLabel(
                    text="[Banner not found]",
                    row=0, column=0, columnspan=4,
                    background="lightgreen", foreground="white"
                )
        else:
            self.addLabel(
                text="[Pillow not installed]",
                row=0, column=0, columnspan=4,
                background="lightgreen", foreground="white"
            )

        # Rest of your widgets…
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

   
def openQuote(self):
    self.destroy()
    QuoteEstimator().mainloop()

def openScheduler(self):
    self.destroy()
    JobScheduler().mainloop()

def exitProgram(self):
    self.quit()


class QuoteEstimator(EasyFrame):
    def __init__(self):
        super().__init__(title="Quote Estimator", background="lightgreen")
        # Inputs
        self.addLabel(
            text="Square Footage:",
            row=0, column=0,
            background="lightgreen", foreground="white"
        )
        self.sqftEntry = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(
            text="Rate per Sqft:",
            row=1, column=0,
            background="lightgreen", foreground="white"
        )
        self.rateEntry = self.addFloatField(value=0.0, row=1, column=1)

        # Buttons
        self.addButton(
            text="Calculate",
            row=2, column=0,
            command=self.calculateQuote
        )
        self.addButton(
            text="Clear",
            row=2, column=1,
            command=self.clearFields
        )
        self.addButton(
            text="Back",
            row=2, column=2,
            command=self.goBack
        )
        self.addButton(
            text="Exit",
            row=2, column=3,
            command=self.exitProgram
        )

    def calculateQuote(self):
        sqft = self.sqftEntry.getNumber()
        rate = self.rateEntry.getNumber()
        if sqft < 0 or rate < 0:
            self.messageBox(title="Error", message="Values must be non‑negative.")
            return
        total = sqft * rate
        self.messageBox(
            title="Quote",
            message=f"Estimated Cost: ${total:.2f}"
        )

    def clearFields(self):
        self.sqftEntry.setNumber(0.0)
        self.rateEntry.setNumber(0.0)

    def goBack(self):
        self.destroy()
        MainMenu().mainloop()

    def exitProgram(self):
        self.quit()


class JobScheduler(EasyFrame):

    def __init__(self):
        super().__init__(title="Job Scheduler", background="lightgreen")
        # Inputs
        self.addLabel(
            text="Job Date (YYYY‑MM‑DD):",
            row=0, column=0,
            background="lightgreen", foreground="white"
        )
        self.dateEntry = self.addTextField(text="", row=0, column=1)

        self.addLabel(
            text="Time (HH:MM):",
            row=1, column=0,
            background="lightgreen", foreground="white"
        )
        self.timeEntry = self.addTextField(text="", row=1, column=1)

        # Buttons
        self.addButton(
            text="Schedule",
            row=2, column=0,
            command=self.scheduleJob
        )
        self.addButton(
            text="Clear",
            row=2, column=1,
            command=self.clearFields
        )
        self.addButton(
            text="Back",
            row=2, column=2,
            command=self.goBack
        )
        self.addButton(
            text="Exit",
            row=2, column=3,
            command=self.exitProgram
        )

    def scheduleJob(self):
        dateStr = self.dateEntry.getText()
        timeStr = self.timeEntry.getText()
        # (You can add stricter date/time validation here)
        self.messageBox(
            title="Scheduled",
            message=f"Job set for {dateStr} at {timeStr}."
        )

    def clearFields(self):
        self.dateEntry.setText("")
        self.timeEntry.setText("")

    def goBack(self):
        self.destroy()
        MainMenu().mainloop()

    def exitProgram(self):
        self.quit()


if __name__ == "__main__":
    MainMenu().mainloop()
