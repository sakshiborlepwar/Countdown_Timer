import tkinter as tk
from tkinter import messagebox


def countdown():
    global time_left
    if time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_string.set(f"{minutes:02}:{seconds:02}")
        time_left -= 1
        
        root.after(1000, countdown)
    else:
        messagebox.showinfo("Time's Up!", "The countdown has finished!")
        start_button.config(state=tk.NORMAL)


def start_timer():
    global time_left
    try:
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        time_left = minutes * 60 + seconds
        start_button.config(state=tk.DISABLED)
        countdown()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for minutes and seconds.")


def reset_timer():
    global time_left
    time_left = 0
    time_string.set("00:00")
    entry_minutes.delete(0, tk.END)
    entry_seconds.delete(0, tk.END)
    start_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Countdown Timer")


time_left = 0
time_string = tk.StringVar()
time_string.set("00:00")


label = tk.Label(root, text="Enter time (minutes and seconds):", font=("Helvetica", 14))
label.pack(pady=10)

entry_minutes = tk.Entry(root, font=("Helvetica", 14), width=3)
entry_minutes.pack(side=tk.LEFT, padx=5)
entry_seconds = tk.Entry(root, font=("Helvetica", 14), width=3)
entry_seconds.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 14), command=start_timer)
start_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Timer", font=("Helvetica", 14), command=reset_timer)
reset_button.pack(pady=10)


timer_display = tk.Label(root, textvariable=time_string, font=("Helvetica", 30), fg="red")
timer_display.pack(pady=20)


root.mainloop()
