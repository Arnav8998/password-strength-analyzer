from password_analyzer import analyze_password

class PasswordAnalyzerGUI:
def init(self, root):
self.root = root
self.root.title("Password Strength Analyzer")
self.root.geometry("580x650")
self.root.minsize(500, 550)
self.root.configure(bg="#f4f6f9")

    # Main container
    main = tk.Frame(root, bg="#f4f6f9", padx=25, pady=20)
    main.pack(fill="both", expand=True)

    # Application heading
    tk.Label(
        main,
        text="Password Strength Analyzer",
        font=("Arial", 20, "bold"),
        bg="#f4f6f9",
        fg="#172554"
    ).pack(pady=(0, 8))

    tk.Label(
        main,
        text="Evaluate password strength and identify weaknesses",
        font=("Arial", 10),
        bg="#f4f6f9",
        fg="#475569"
    ).pack(pady=(0, 20))

    # Password input
    tk.Label(
        main,
        text="Enter a test password:",
        font=("Arial", 11, "bold"),
        bg="#f4f6f9"
    ).pack(anchor="w")

    self.password_entry = ttk.Entry(
        main,
        show="*",
        font=("Arial", 12)
    )
    self.password_entry.pack(fill="x", pady=10)

    # Show/hide password
    self.show_password = tk.BooleanVar(value=False)

    ttk.Checkbutton(
        main,
        text="Show password",
        variable=self.show_password,
        command=self.toggle_password
    ).pack(anchor="w", pady=5)

    # Analyze button
    tk.Button(
        main,
        text="Analyze Password",
        command=self.analyze,
        bg="#2563eb",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        pady=10,
        cursor="hand2"
    ).pack(fill="x", pady=15)

    # Strength result
    self.strength_label = tk.Label(
        main,
        text="Strength: Not evaluated",
        font=("Arial", 14, "bold"),
        bg="#f4f6f9",
        fg="#334155"
    )
    self.strength_label.pack(pady=8)

    # Progress bar
    self.progress = ttk.Progressbar(
        main,
        orient="horizontal",
        length=450,
        mode="determinate",
        maximum=5
    )
    self.progress.pack(fill="x", pady=10)

    # Results section
    tk.Label(
        main,
        text="Security Checks and Recommendations",
        font=("Arial", 12, "bold"),
        bg="#f4f6f9",
        fg="#172554"
    ).pack(anchor="w", pady=(20, 10))

    # Results text area
    self.results = tk.Text(
        main,
        height=14,
        font=("Consolas", 10),
        wrap="word",
        bg="white",
        fg="#1e293b",
        padx=12,
        pady=12,
        state="disabled"
    )
    self.results.pack(fill="both", expand=True)

    # Footer
    tk.Label(
        main,
        text="Educational password analysis tool",
        font=("Arial", 9),
        bg="#f4f6f9",
        fg="#64748b"
    ).pack(pady=(10, 0))

def toggle_password(self):
    if self.show_password.get():
        self.password_entry.config(show="")
    else:
        self.password_entry.config(show="*")

def analyze(self):
    password = self.password_entry.get()

    if not password:
        self.strength_label.config(
            text="Please enter a test password",
            fg="#dc2626"
        )
        self.progress["value"] = 0
        self.display_results("")
        return

    # Call the existing analysis function
    strength, score, checks, suggestions = (
        analyze_password(password)
    )

    # Update strength label
    colors = {
        "Weak": "#dc2626",
        "Moderate": "#d97706",
        "Strong": "#16a34a"
    }

    self.strength_label.config(
        text=f"Strength: {strength} ({score}/5)",
        fg=colors[strength]
    )

    # Update progress bar
    self.progress["value"] = score

    # Build results
    output = "SECURITY CHECKS\n"
    output += "-" * 35 + "\n\n"

    for check, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        output += f"[{status}] {check}\n"

    output += "\nRECOMMENDATIONS\n"
    output += "-" * 35 + "\n\n"

    if suggestions:
        for suggestion in suggestions:
            output += f"- {suggestion}\n"
    else:
        output += "No basic weaknesses identified.\n"

    output += (
        "\nNote: This educational score does not "
        "guarantee password security."
    )

    self.display_results(output)

    # Avoid retaining the test password in the input
    self.password_entry.delete(0, tk.END)

def display_results(self, text):
    self.results.config(state="normal")
    self.results.delete("1.0", tk.END)
    self.results.insert(tk.END, text)
    self.results.config(state="disabled")
if name == "main":
root = tk.Tk()
app = PasswordAnalyzerGUI(root)
root.mainloop()
