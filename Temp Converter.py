from tkinter import *
from tkinter import messagebox


class TemperatureLogic:

    def fahrenheit_to_celsius(self, f):
        if f < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
        return (f - 32) * 5 / 9

    def celsius_to_fahrenheit(self, c):
        if c < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        return (c * 9 / 5) + 32


class TemperatureConverter:

    def __init__(self, root):
        self.root = root
        self.logic = TemperatureLogic()

        # Set up the main window
        self.root.title("Temperature Converter")
        self.root.geometry("500x300")
        self.root.minsize(400, 250)

        # Container that holds all pages/screens
        self.container = Frame(root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Create the three screens used in the program
        self.main_screen = Frame(self.container)
        self.f_to_c_screen = Frame(self.container)
        self.c_to_f_screen = Frame(self.container)

        # Stack all frames in the same position
        for frame in (self.main_screen, self.f_to_c_screen, self.c_to_f_screen): frame.grid(row=0, column=0, sticky="nsew")

        # Build each page
        self.main_menu()
        self.fahrenheit_page()
        self.celsius_page()

        # Start on the main menu
        self.show_main()

    def main_menu(self):
        # Main heading
        Label(self.main_screen, text="Temperature Converter", font=("Arial", 18, "bold")).pack(pady=30)

        button_frame = Frame(self.main_screen)
        button_frame.pack(pady=20)

        # Navigation buttons
        Button(button_frame, text="To Centigrade", command=self.show_f_to_c, width=15, height=2, bg="yellow", font=("Arial", 12)).pack(side=LEFT, padx=10)

        Button(button_frame, text="To Fahrenheit", command=self.show_c_to_f, width=15, height=2, bg="pink", font=("Arial", 12)).pack(side=LEFT, padx=10)

        # Exit the application
        Button(self.main_screen, text="Quit", command=self.root.quit, width=20).pack(pady=20)

    def fahrenheit_page(self):
        # Screen for Fahrenheit to Celsius conversion
        Label(self.f_to_c_screen, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=15)

        Label(self.f_to_c_screen, text="Enter the temperature in Fahrenheit", font=("Arial", 11)).pack(pady=10)

        self.f_input = Entry(self.f_to_c_screen, font=("Arial", 12), justify="center")
        self.f_input.pack(fill="x", padx=50, pady=5)

        button_frame = Frame(self.f_to_c_screen)
        button_frame.pack(pady=15)

        # Convert, go back, or clear everything
        Button(button_frame, text="Calculate", command=self.convert_f_to_c, width=10, bg="lightgreen").pack(side=LEFT, padx=5)

        Button(button_frame, text="Back", command=self.show_main, width=10).pack(side=LEFT, padx=5)

        Button(button_frame, text="Reset", command=self.reset_f, width=10, bg="orange").pack(side=LEFT, padx=5)

        # Result will appear here after conversion
        self.f_result = Label(self.f_to_c_screen, text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"), wraplength=400)
        self.f_result.pack(pady=15)

    def celsius_page(self):
        # Screen for Celsius to Fahrenheit conversion
        Label(self.c_to_f_screen, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=15)

        Label(self.c_to_f_screen, text="Enter the temperature in Centigrade", font=("Arial", 11)).pack(pady=10)

        self.c_input = Entry(self.c_to_f_screen, font=("Arial", 12), justify="center")
        self.c_input.pack(fill="x", padx=50, pady=5)

        button_frame = Frame(self.c_to_f_screen)
        button_frame.pack(pady=15)

        Button(button_frame, text="Calculate", command=self.convert_c_to_f, width=10, bg="lightgreen").pack(side=LEFT, padx=5)

        Button(button_frame, text="Back", command=self.show_main, width=10).pack(side=LEFT, padx=5)

        Button(button_frame, text="Reset", command=self.reset_c, width=10, bg="orange").pack(side=LEFT, padx=5)

        self.c_result = Label(self.c_to_f_screen, text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"), wraplength=400)
        self.c_result.pack(pady=15)

    def show_main(self):
        # Bring the main menu to the front
        self.main_screen.tkraise()

    def show_f_to_c(self):
        # Clear old data before opening this screen
        self.f_input.delete(0, END)
        self.f_result.config(text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"))
        self.f_to_c_screen.tkraise()

    def show_c_to_f(self):
        # Clear old data before opening this screen
        self.c_input.delete(0, END)
        self.c_result.config(text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"))
        self.c_to_f_screen.tkraise()

    def convert_f_to_c(self):
        try:
            # Get the user's input
            f = float(self.f_input.get())

            # Fahrenheit to Celsius formula
            c = self.logic.fahrenheit_to_celsius(f)

            self.f_result.config(text=f"{f:.2f}°F = {c:.2f}°C", fg="green", font=("Arial", 11, "bold"))

        except ValueError as e:
            # Handle non-numeric input
            messagebox.showerror("Invalid Input", str(e))
            self.f_input.delete(0, END)

    def convert_c_to_f(self):
        try:
            # Get the user's input
            c = float(self.c_input.get())

            # Celsius to Fahrenheit formula
            f = self.logic.celsius_to_fahrenheit(c)

            self.c_result.config(text=f"{c:.2f}°C = {f:.2f}°F", fg="green", font=("Arial", 11, "bold"))

        except ValueError as e:
            # Handle non-numeric input
            messagebox.showerror("Invalid Input", str(e))
            self.c_input.delete(0, END)

    def reset_f(self):
        # Clear the input box and reset the result label
        self.f_input.delete(0, END)
        self.f_result.config(text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"))

    def reset_c(self):
        # Clear the input box and reset the result label
        self.c_input.delete(0, END)
        self.c_result.config(text="Converted temperature goes here", fg="blue", font=("Arial", 10, "italic"))


# Create and run the application
root = Tk()
app = TemperatureConverter(root)
root.mainloop()