

import tkinter as tk

from tkinter import ttk

SERVICE_RATES = {
    'Deep Clean': 0.15,
    'Move-Out Clean': 0.20,
    'Eco-Boost Clean': 0.18,}

FREQUENCY_MULTIPLIERS = {
    'One-Time': 1.0,
    'Weekly': 0.90,     
    'Biweekly': 0.92,  
    'Monthly': 0.95,    
}

class QuoteEstimator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BSH Cleaning Quote Estimator")
        self._build_widgets()

if __name__ == "__main__":
    app = QuoteEstimator()
    app.mainloop()
