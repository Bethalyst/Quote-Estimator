

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

    def _build_widgets(self):
        ttk.Label(self, text="Square Footage:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.sqft_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.sqft_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Service Type:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.service_var = tk.StringVar(value=list(SERVICE_RATES.keys())[0])
        ttk.OptionMenu(self, self.service_var, self.service_var.get(), *SERVICE_RATES.keys()).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Service Frequency:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.freq_var = tk.StringVar(value=list(FREQUENCY_MULTIPLIERS.keys())[0])
        ttk.OptionMenu(self, self.freq_var, self.freq_var.get(), *FREQUENCY_MULTIPLIERS.keys()).grid(row=2, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(self, text="Calculate Quote", command=self.calculate_quote)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Result d
        self.result_label = ttk.Label(self, text="Your estimated quote will appear here.")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def calculate_quote(self):
        try:
            sqft = float(self.sqft_var.get())
            rate = SERVICE_RATES[self.service_var.get()]
            freq_mult = FREQUENCY_MULTIPLIERS[self.freq_var.get()]
            quote = sqft * rate * freq_mult
            self.result_label.config(text=f"Estimated Quote: ${quote:,.2f}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number for square footage.")


if __name__ == "__main__":
    app = QuoteEstimator()
    app.mainloop()
