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
        self.geometry("400x520")  # Adjusted for vertical stacking and centering
        self.ce_entries = []  # Entry widgets for CE values
        self.pe_entries = []  # Entry widgets for PE values
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange all widgets in the GUI using grid layout, centered.
        """
        # Configure grid columns for centering and spacing
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

        # Labels for columns (centered)
        ttk.Label(self, text="CE", font=(None, 12, "bold"), anchor="center", justify="center").grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        ttk.Label(self, text="PE", font=(None, 12, "bold"), anchor="center", justify="center").grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Entry boxes for CE and PE (centered)
        for i in range(10):
            ce_entry = ttk.Entry(self, width=10, justify="center")
            ce_entry.grid(row=i+1, column=1, padx=5, pady=2, sticky="ew")
            self.ce_entries.append(ce_entry)
            pe_entry = ttk.Entry(self, width=10, justify="center")
            pe_entry.grid(row=i+1, column=2, padx=5, pady=2, sticky="ew")
            self.pe_entries.append(pe_entry)

        # Totals as Entry boxes directly below CE and PE columns
        self.ce_total_var = tk.StringVar()
        self.pe_total_var = tk.StringVar()
        ttk.Label(self, text="CE Total:", anchor="center", justify="center").grid(row=11, column=1, sticky="ew", padx=5)
        self.ce_total_entry = ttk.Entry(self, textvariable=self.ce_total_var, width=12, justify="center", state="normal")
        self.ce_total_entry.grid(row=12, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(self, text="PE Total:", anchor="center", justify="center").grid(row=11, column=2, sticky="ew", padx=5)
        self.pe_total_entry = ttk.Entry(self, textvariable=self.pe_total_var, width=12, justify="center", state="normal")
        self.pe_total_entry.grid(row=12, column=2, padx=5, pady=2, sticky="ew")

        # Initial Balance (centered, own row)
        self.net_pnl_var = tk.StringVar()
        ttk.Label(self, text="Initial Balance:", anchor="center", justify="center").grid(row=13, column=1, columnspan=2, sticky="ew", pady=10)
        self.initial_balance_entry = ttk.Entry(self, width=15, justify="center")
        self.initial_balance_entry.grid(row=14, column=1, columnspan=2, padx=5, pady=2, sticky="ew")

        # Net P&L (centered, own row)
        ttk.Label(self, text="Net P&L:", anchor="center", justify="center").grid(row=15, column=1, columnspan=2, sticky="ew", padx=5)
        self.net_pnl_entry = ttk.Entry(self, textvariable=self.net_pnl_var, width=12, justify="center", state="normal")
        self.net_pnl_entry.grid(row=16, column=1, columnspan=2, padx=5, pady=2, sticky="ew")

        # Net Balance (centered, own row)
        self.net_balance_var = tk.StringVar()
        ttk.Label(self, text="Net Balance:", anchor="center", justify="center").grid(row=17, column=1, columnspan=2, sticky="ew", padx=5)
        self.net_balance_entry = ttk.Entry(self, textvariable=self.net_balance_var, width=12, justify="center", state="normal")
        self.net_balance_entry.grid(row=18, column=1, columnspan=2, padx=5, pady=2, sticky="ew")

        # Calculate button (centered below all)
        calc_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calc_btn.grid(row=19, column=1, columnspan=2, pady=15, sticky="ew")

    def calculate(self):
        """
        Calculate CE total, PE total, Net P&L, and Net Balance. Update the display variables and Entry boxes.
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

