import tkinter as tk
import time

time_object = None
running = False
def start_timer():
    global time_object
    global running
    if not running:
        time_object = time.time()
        running = True
        update_time()

def stop_timer():
    global time_object
    global running
    if running:
        elapsed_time = round(time.time() - time_object, 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, str(elapsed_time) + " seconds")
        running = False

def reset_window():
    global time_object
    global running
    main_window.delete(1.0, "end")
    main_window.insert(1.0, "0.00 seconds")
    time_object = None
    running = False

def update_time():
    global time_object
    global running
    if running:
        elapsed_time = round(time.time() - time_object, 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, elapsed_time)
        main_window.after(55, update_time)
        
root = tk.Tk()
root.title("Stopwatch")
root.geometry("400x400")
root.resizable(False, False)

main_window = tk.Text(root, width = 10, height = 1)
main_window.grid(row = 0, column = 0, columnspan = 4, padx = 10)
main_window.config(font=('Helvatical bold',60))
main_window.insert(1.0, "0.00 seconds")

start_button = tk.Button(root, text = "Start", command = start_timer)
start_button.grid(row = 1, column = 1, columnspan = 1)

stop_button = tk.Button(root, text = "Stop", command = stop_timer)
stop_button.grid(row = 1, column = 3, columnspan = 1)

reset_button = tk.Button(root, text = "Reset", command = reset_window)
reset_button.grid(row = 2, column = 2, columnspan = 1)


root.mainloop()