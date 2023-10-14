import tkinter as tk
import sub_main

def search_wikipedia():
    query = entry.get()
    summary = sub_main.search_wikipedia(query)
    show_results_window(summary)

def show_results_window(result_text):
    results_window = tk.Toplevel(app)
    results_window.title("Search Results")

    result_label = tk.Label(results_window, text=result_text, wraplength=400)
    result_label.pack()

# Create the main application window
app = tk.Tk()
app.title("Wikipedia Summar")

# Create and configure GUI elements
label = tk.Label(app, text="Enter a word to search on Wikipedia:")
entry = tk.Entry(app)
search_button = tk.Button(app, text="Search", command=search_wikipedia)

# Arrange GUI elements in the main window
label.pack()
entry.pack()
search_button.pack()

# Start the GUI application
app.mainloop()
