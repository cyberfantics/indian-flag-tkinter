import tkinter as tk
import math

def draw_flag():
    # Create a tkinter window
    root = tk.Tk()
    root.title("Indian Flag Design")

    # Create a Canvas widget
    canvas = tk.Canvas(root, width=800, height=500, bg='white')
    canvas.pack()

    # Draw the Orange Rectangle
    canvas.create_rectangle(0, 0, 800, 167, fill="orange", outline="orange")

    # Draw the Green Rectangle
    canvas.create_rectangle(0, 167, 800, 334, fill="green", outline="green")

    # Center coordinates
    center_x, center_y = 420, 250

    # Draw the Big Blue Circle
    blue_radius = 70
    canvas.create_oval(
        center_x - blue_radius, center_y - blue_radius,
        center_x + blue_radius, center_y + blue_radius,
        fill="navy", outline="navy"
    )

    # Draw the Big White Circle
    white_radius = 60
    canvas.create_oval(
        center_x - white_radius, center_y - white_radius,
        center_x + white_radius, center_y + white_radius,
        fill="white", outline="white"
    )

    # Draw Mini Blue Circles
    mini_radius = 3
    for i in range(24):
        angle = math.radians(i * 15)
        x = center_x + 60 * math.cos(angle)
        y = center_y - 60 * math.sin(angle)
        canvas.create_oval(
            x - mini_radius, y - mini_radius,
            x + mini_radius, y + mini_radius,
            fill="navy", outline="navy"
        )

    # Draw the Small Blue Circle
    small_circle_radius = 20
    canvas.create_oval(
        center_x - small_circle_radius, center_y - small_circle_radius,
        center_x + small_circle_radius, center_y + small_circle_radius,
        fill="navy", outline="navy"
    )

    # Draw the Spokes
    for i in range(24):
        angle = math.radians(i * 15)
        x1 = center_x + 60 * math.cos(angle)
        y1 = center_y - 60 * math.sin(angle)
        x2 = center_x - 60 * math.cos(angle)
        y2 = center_y + 60 * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, fill="navy", width=2)

    # Draw the Text
    canvas.create_text(
        center_x, center_y - 145,  # Position the text a bit below the center
        text="Created By",
        fill="white",
        font=("Arial", 20, "bold")
    ) # Draw the Text
    canvas.create_text(
        center_x, center_y + 140,  # Position the text a bit below the center
        text="Salfi Hacker",
        fill="green",
        font=("Arial", 20, "bold")
    )

    # Run the tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    draw_flag()
