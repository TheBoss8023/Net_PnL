# Project: Net P&L Calculator
# Description:
# 1. Create a Tkinter GUI with the title "Net P&L"
# 2. GUI should have two main columns: CE and PE
# 3. Each column should allow user to input 10 float/int values (Entry boxes)
# 4. Below each column, show total of CE and total of PE separately
# 5. Add an input box for "Initial Balance" to accept float/int
# 6. Display "Net P&L" = CE Total + PE Total
# 7. Display "Net Balance" = Initial Balance + Net P&L
# 8. Add "Calculate" button to trigger all calculations
# 9. Design layout neatly using grid()
# 10. Create a folder structure with:
#    - main.py
#    - requirements.txt (mention tkinter if needed)
#    - .gitignore (ignore __pycache__, .vscode, etc.)
#    - README.md with usage instructions
# 11. Initialize Git and create a GitHub repo if possible (use subprocess/git commands if required)

import tkinter as tk
from tkinter import ttk

class NetPnLCalculator(tk.Tk):
    """
    Tkinter GUI application for calculating Net P&L and Net Balance.
    Allows user to input CE and PE values, initial balance, and calculates totals.
    """
    def __init__(self):
        """
        Initialize the NetPnLCalculator window and widgets.
        """
        super().__init__()
        self.title("Net P&L")
        self.geometry("600x400")
        self.ce_entries = []  # Entry widgets for CE values
        self.pe_entries = []  # Entry widgets for PE values
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange all widgets in the GUI using grid layout.
        """
        # Labels for columns
        ttk.Label(self, text="CE", font=(None, 12, "bold")).grid(row=0, column=0, padx=10)
        ttk.Label(self, text="PE", font=(None, 12, "bold")).grid(row=0, column=2, padx=10)

        # Entry boxes for CE and PE
        for i in range(10):
            ce_entry = ttk.Entry(self, width=10)
            ce_entry.grid(row=i+1, column=0, padx=5, pady=2)
            self.ce_entries.append(ce_entry)
            pe_entry = ttk.Entry(self, width=10)
            pe_entry.grid(row=i+1, column=2, padx=5, pady=2)
            self.pe_entries.append(pe_entry)

        # Totals
        self.ce_total_var = tk.StringVar()
        self.pe_total_var = tk.StringVar()
        ttk.Label(self, text="CE Total:").grid(row=11, column=0, sticky="e")
        ttk.Label(self, textvariable=self.ce_total_var).grid(row=11, column=1, sticky="w")
        ttk.Label(self, text="PE Total:").grid(row=11, column=2, sticky="e")
        ttk.Label(self, textvariable=self.pe_total_var).grid(row=11, column=3, sticky="w")

        # Initial Balance
        ttk.Label(self, text="Initial Balance:").grid(row=12, column=0, sticky="e", pady=10)
        self.initial_balance_entry = ttk.Entry(self, width=15)
        self.initial_balance_entry.grid(row=12, column=1, padx=5, pady=10)

        # Net P&L and Net Balance
        self.net_pnl_var = tk.StringVar()
        self.net_balance_var = tk.StringVar()
        ttk.Label(self, text="Net P&L:").grid(row=13, column=0, sticky="e")
        ttk.Label(self, textvariable=self.net_pnl_var).grid(row=13, column=1, sticky="w")
        ttk.Label(self, text="Net Balance:").grid(row=13, column=2, sticky="e")
        ttk.Label(self, textvariable=self.net_balance_var).grid(row=13, column=3, sticky="w")

        # Calculate button
        calc_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calc_btn.grid(row=14, column=0, columnspan=4, pady=15)

    def calculate(self):
        """
        Calculate CE total, PE total, Net P&L, and Net Balance. Update the display variables.
        """
        ce_total = sum(self._get_entry_value(e) for e in self.ce_entries)
        pe_total = sum(self._get_entry_value(e) for e in self.pe_entries)
        self.ce_total_var.set(f"{ce_total:.2f}")
        self.pe_total_var.set(f"{pe_total:.2f}")
        net_pnl = ce_total + pe_total
        self.net_pnl_var.set(f"{net_pnl:.2f}")
        try:
            initial_balance = float(self.initial_balance_entry.get())
        except ValueError:
            initial_balance = 0.0
        net_balance = initial_balance + net_pnl
        self.net_balance_var.set(f"{net_balance:.2f}")

    def _get_entry_value(self, entry):
        """
        Safely get float value from an Entry widget. Returns 0.0 if invalid.
        """
        try:
            return float(entry.get())
        except ValueError:
            return 0.0

if __name__ == "__main__":
    # Start the NetPnLCalculator application
    app = NetPnLCalculator()
    app.mainloop()

