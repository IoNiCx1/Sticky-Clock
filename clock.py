# import tkinter as tk
# import time
# import math
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Sticky Clock with Countdown")

# # ✅ Always on top and pinned to top-left corner
# root.attributes("-topmost", True)
# root.geometry("250x350+0+0")  # Width x Height + X + Y (top-left corner)

# # Optional: uncomment to remove window borders (like a widget)
# # root.overrideredirect(True)

# canvas = tk.Canvas(root, width=250, height=250, bg="white", highlightthickness=0)
# canvas.pack()

# center_x = 125
# center_y = 125
# radius = 100

# def draw_clock_face():
#     canvas.create_oval(center_x - radius, center_y - radius,
#                        center_x + radius, center_y + radius)
    
#     for hour in range(12):
#         angle = math.radians(hour * 30)
#         x = center_x + (radius - 15) * math.sin(angle)
#         y = center_y - (radius - 15) * math.cos(angle)
#         canvas.create_text(x, y, text=str(hour if hour != 0 else 12), font=("Helvetica", 10))
    
#     canvas.create_text(center_x, 230, text="Time is Precious", font=("Helvetica", 10), fill="darkred")

# # FIX: Track the scheduled after-ID so we can cancel any existing one
# # before scheduling a new one — prevents double-scheduling (which caused 2x speed)
# _clock_job = None

# def update_clock():
#     global _clock_job

#     canvas.delete("hands")
#     now = time.localtime()
#     sec = now.tm_sec
#     minute = now.tm_min
#     hour = now.tm_hour % 12 + minute / 60

#     # Second hand
#     sec_angle = math.radians(sec * 6)
#     sec_x = center_x + radius * 0.9 * math.sin(sec_angle)
#     sec_y = center_y - radius * 0.9 * math.cos(sec_angle)
#     canvas.create_line(center_x, center_y, sec_x, sec_y, fill="red", width=1, tags="hands")

#     # Minute hand
#     min_angle = math.radians(minute * 6)
#     min_x = center_x + radius * 0.75 * math.sin(min_angle)
#     min_y = center_y - radius * 0.75 * math.cos(min_angle)
#     canvas.create_line(center_x, center_y, min_x, min_y, fill="blue", width=2, tags="hands")

#     # Hour hand
#     hour_angle = math.radians(hour * 30)
#     hour_x = center_x + radius * 0.5 * math.sin(hour_angle)
#     hour_y = center_y - radius * 0.5 * math.cos(hour_angle)
#     canvas.create_line(center_x, center_y, hour_x, hour_y, fill="black", width=4, tags="hands")

#     # FIX: Cancel any pending call before scheduling the next one
#     # This guarantees exactly one callback is ever in flight at a time
#     if _clock_job is not None:
#         root.after_cancel(_clock_job)
#     _clock_job = root.after(1000, update_clock)


# # Countdown timer logic
# timer_running = False
# timer_paused = False
# time_left = 0
# _timer_job = None  # FIX: same guard for the timer

# def format_time(seconds):
#     mins = seconds // 60
#     secs = seconds % 60
#     return f"{mins:02}:{secs:02}"

# def update_timer():
#     global time_left, timer_running, timer_paused, _timer_job

#     if timer_running and not timer_paused and time_left > 0:
#         time_left -= 1
#         timer_label.config(text=format_time(time_left))
#         _timer_job = root.after(1000, update_timer)
#     elif timer_running and not timer_paused and time_left == 0:
#         timer_running = False
#         timer_paused = False
#         timer_label.config(text="00:00")
#         pause_btn.config(text="Pause", state=tk.DISABLED)
#         root.bell()
#         messagebox.showinfo("Time's Up", "Your countdown has finished!")
#     elif timer_running and timer_paused:
#         _timer_job = root.after(100, update_timer)

# def start_countdown():
#     global time_left, timer_running, timer_paused, _timer_job

#     # FIX: cancel any running timer job before starting a new one
#     if _timer_job is not None:
#         root.after_cancel(_timer_job)

#     try:
#         minutes = int(entry.get())
#         if minutes <= 0:
#             raise ValueError

#         time_left = minutes * 60
#         timer_label.config(text=format_time(time_left))
#         timer_running = True
#         timer_paused = False
#         pause_btn.config(text="Pause", state=tk.NORMAL)
#         update_timer()
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

# def pause_resume_timer():
#     global timer_paused

#     if timer_running:
#         timer_paused = not timer_paused
#         if timer_paused:
#             pause_btn.config(text="Resume")
#         else:
#             pause_btn.config(text="Pause")

# def reset_timer():
#     global time_left, timer_running, timer_paused, _timer_job

#     # FIX: cancel any pending timer callback on reset
#     if _timer_job is not None:
#         root.after_cancel(_timer_job)
#         _timer_job = None

#     timer_running = False
#     timer_paused = False
#     time_left = 0
#     timer_label.config(text="00:00")
#     pause_btn.config(text="Pause", state=tk.DISABLED)

# # Timer UI
# timer_label = tk.Label(root, text="00:00", font=("Helvetica", 12))
# timer_label.pack(pady=5)

# entry_frame = tk.Frame(root, bg="white")
# entry_frame.pack()

# tk.Label(entry_frame, text="Set (min):", bg="white").pack(side=tk.LEFT)
# entry = tk.Entry(entry_frame, width=5)
# entry.pack(side=tk.LEFT)

# btn_frame = tk.Frame(root, bg="white")
# btn_frame.pack(pady=5)

# tk.Button(btn_frame, text="Start", command=start_countdown).pack(side=tk.LEFT, padx=2)
# pause_btn = tk.Button(btn_frame, text="Pause", command=pause_resume_timer, state=tk.DISABLED)
# pause_btn.pack(side=tk.LEFT, padx=2)
# tk.Button(btn_frame, text="Reset", command=reset_timer).pack(side=tk.LEFT, padx=2)

# draw_clock_face()
# update_clock()
# root.mainloop()