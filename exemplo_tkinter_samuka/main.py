import requests, json
import tkinter as tk
from tkinter import messagebox

def toggle_editable(var, entry):
    if var.get():
        entry.config(state=tk.NORMAL)
    else:
        entry.config(state=tk.DISABLED)

def submit_data():
    if get_create_station() == 200:
        station_id = get_stationID()
        if station_id:
            data = {
                "host": host_entry.get(),
                "station_name": name_entry.get(),
                "station_id": station_id,
                "url_db": url_db_entry.get(),
                "url_station": url_station_entry.get(),
                "sleep": sleep_entry.get(),
                "log": log_entry.get(),
                "delay_log": log_time_entry.get()
            }
            write_to_env(data)
            messagebox.showinfo("Success", "Data updated successfully")
        else:
            messagebox.showinfo("Error", "Incorrect station name, try again")

def write_to_env(data):
    try:
        with open(".env", "w") as f:
            for key, value in data.items():
                f.write(f"{key}={value}\n")
    except IOError as e:
        messagebox.showinfo("Error", f"Failed to write to .env: {e}")

def get_create_station():
    session = requests.Session()
    station_name = name_entry.get()

    if check_station_exists(station_name):
        messagebox.showinfo("Info", "Station already exists.")
        return 200

    data = {
        "name": station_name,
        "status": True
    }
    
    try:
        response = session.post(url_station_create.get(), json=data)
        response.raise_for_status()
        return response.status_code
    except requests.RequestException as e:
        messagebox.showinfo("Error", f"Request failed: {e}")
        return None

def check_station_exists(station_name):
    session = requests.Session()
    try:
        response = session.get(f'{url_station_entry.get()}/{station_name}')
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
    except requests.RequestException as e:
        messagebox.showinfo("Error", f"Request failed: {e}")
    
    return False

def get_stationID():
    session = requests.Session()
    try:
        response = session.get(f'{url_station_entry.get()}/{name_entry.get()}', timeout=1)
        response.raise_for_status()
        return json.loads(response.text)['data'].get('stationId', 0)
    except requests.RequestException as e:
        messagebox.showinfo("Error", f"Request failed: {e}")
        return None

window = tk.Tk()
window.title("Config APP")

label_width = 10
write_width = 40

host         = "10.110.40.2"
url_db       = 'http://mercuryhub-dev.sao.flextronics.com/mercury/api/stationmetrics'
url_station  = 'http://mercuryhub-dev.sao.flextronics.com/mercury/api/station/byname'
url_create   = 'http://mercuryhub-dev.sao.flextronics.com/mercury/api/station'
sleep        = 5
log          = 'True'
time_log     = 1800

# Name
tk.Label(window, text="Station Name:", width=label_width, anchor=tk.W).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(window, width=write_width)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Host
tk.Label(window, text="Host:", width=label_width, anchor=tk.W).grid(row=1, column=0, padx=10, pady=5)
host_var = tk.BooleanVar()
host_entry = tk.Entry(window, width=write_width)
host_entry.insert(0, host)
host_entry.config(state=tk.DISABLED)
host_entry.grid(row=1, column=1, padx=10, pady=5)

host_checkbox = tk.Checkbutton(window, text="Edit", variable=host_var,
                                command=lambda: toggle_editable(host_var, host_entry))
host_checkbox.grid(row=1, column=2)

# URL DB
tk.Label(window, text="URL DB:", width=label_width, anchor=tk.W).grid(row=2, column=0, padx=10, pady=5)
url_db_var = tk.BooleanVar() 
url_db_entry = tk.Entry(window, width=write_width)
url_db_entry.insert(0, url_db)
url_db_entry.config(state=tk.DISABLED)
url_db_entry.grid(row=2, column=1, padx=10, pady=5)

url_db_checkbox = tk.Checkbutton(window, text="Edit", variable=url_db_var,
                                  command=lambda: toggle_editable(url_db_var, url_db_entry))
url_db_checkbox.grid(row=2, column=2)

# URL Station
tk.Label(window, text="URL Station:", width=label_width, anchor=tk.W).grid(row=3, column=0, padx=10, pady=5)
url_station_var = tk.BooleanVar() 
url_station_entry = tk.Entry(window, width=write_width)
url_station_entry.insert(0, url_station)
url_station_entry.config(state=tk.DISABLED)
url_station_entry.grid(row=3, column=1, padx=10, pady=5)

url_station_checkbox = tk.Checkbutton(window, text="Edit", variable=url_station_var,
                                       command=lambda: toggle_editable(url_station_var, url_station_entry))
url_station_checkbox.grid(row=3, column=2)

# Sleep
tk.Label(window, text="Sleep:", width=label_width, anchor=tk.W).grid(row=4, column=0, padx=10, pady=5)
sleep_var = tk.BooleanVar() 
sleep_entry = tk.Entry(window, width=write_width)
sleep_entry.insert(0, sleep)
sleep_entry.config(state=tk.DISABLED)
sleep_entry.grid(row=4, column=1, padx=10, pady=5)

sleep_checkbox = tk.Checkbutton(window, text="Edit", variable=sleep_var,
                                 command=lambda: toggle_editable(sleep_var, sleep_entry))
sleep_checkbox.grid(row=4, column=2)

# URL Create Station
tk.Label(window, text="URL Create:", width=label_width, anchor=tk.W).grid(row=5, column=0, padx=10, pady=5)
url_create_var = tk.BooleanVar() 
url_station_create = tk.Entry(window, width=write_width)
url_station_create.insert(0, url_create)
url_station_create.config(state=tk.DISABLED)
url_station_create.grid(row=5, column=1, padx=10, pady=5)

url_station_checkbox = tk.Checkbutton(window, text="Edit", variable=url_create_var,
                                       command=lambda: toggle_editable(url_create_var, url_station_create))
url_station_checkbox.grid(row=5, column=2)

# LOG State
tk.Label(window, text="LOG State:", width=label_width, anchor=tk.W).grid(row=6, column=0, padx=10, pady=5)
log_var = tk.BooleanVar() 
log_entry = tk.Entry(window, width=write_width)
log_entry.insert(0, log)
log_entry.config(state=tk.DISABLED)
log_entry.grid(row=6, column=1, padx=10, pady=5)

log_checkbox = tk.Checkbutton(window, text="Edit", variable=log_var,
                                       command=lambda: toggle_editable(log_var, log_entry))
log_checkbox.grid(row=6, column=2)

# Time Log
tk.Label(window, text="LOG Time:", width=label_width, anchor=tk.W).grid(row=7, column=0, padx=10, pady=5)
log_time_var = tk.BooleanVar() 
log_time_entry = tk.Entry(window, width=write_width)
log_time_entry.insert(0, time_log)
log_time_entry.config(state=tk.DISABLED)
log_time_entry.grid(row=7, column=1, padx=10, pady=5)

log_time_checkbox = tk.Checkbutton(window, text="Edit", variable=log_time_var,
                                       command=lambda: toggle_editable(log_time_var, log_time_entry))
log_time_checkbox.grid(row=7, column=2)


submit_button = tk.Button(window, text="Send", command=submit_data)
submit_button.grid(row=8, column=0, columnspan=3, pady=10)

window.mainloop()