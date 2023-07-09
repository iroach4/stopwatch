import tkinter as tk
import time

elapsed_time = None
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
    global elapsed_time
    if running and elapsed_time == None:
        elapsed_time = round(time.time() - time_object, 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, str(elapsed_time) + " seconds")
        running = False
    if running and elapsed_time != None:
        time_elapsed = round(elapsed_time + (time.time() - time_object), 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, str(time_elapsed) + " seconds")
        running = False
        elapsed_time = time_elapsed

def reset_window():
    global time_object
    global running
    global elapsed_time
    main_window.delete(1.0, "end")
    main_window.insert(1.0, "0.00 seconds")
    time_object = None
    running = False
    elapsed_time = None

def update_time():
    global time_object
    global running
    global elapsed_time
    if running and elapsed_time == None:
        time_elapsed = round(time.time() - time_object, 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, time_elapsed)
        main_window.after(55, update_time)
    if running and elapsed_time != None:
        time_elapsed = round(elapsed_time + (time.time() - time_object), 2)
        main_window.delete(1.0, "end")
        main_window.insert(tk.END, time_elapsed)
        main_window.after(55, update_time)
        
root = tk.Tk()
root.title("Stopwatch")
root.geometry("435x400")
root.resizable(False, False)

main_window = tk.Text(root, width = 11, height = 1)
main_window.grid(row = 0, column = 0, columnspan = 3, padx = 10)
main_window.config(font=('Helvatical bold',60))
main_window.insert(1.0, "0.00 seconds")

start_button = tk.Button(root, text = "Start", command = start_timer, width = 8)
start_button.grid(row = 1, column = 0)

stop_button = tk.Button(root, text = "Stop", command = stop_timer, width = 8)
stop_button.grid(row = 1, column = 2)

reset_button = tk.Button(root, text = "Reset", command = reset_window, width = 8)
reset_button.grid(row = 2, column = 1)

root.mainloop()