import tkinter as tk
import math

# Constants
WIDTH, HEIGHT = 800, 800  # Canvas size
RE = 50  # Earth's radius (scaled down)
RQ = 200  # Initial asteroid distance from Earth (scaled down)
v0 = 5  # Initial velocity of the asteroid (scaled down)
G = 1  # Gravitational constant (scaled down)
ME = 1000  # Mass of Earth
mQ = 1  # Mass of asteroid

class AsteroidSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Asteroid Near Earth Simulation")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Draw Earth
        self.earth_x, self.earth_y = WIDTH // 2, HEIGHT // 2
        self.canvas.create_oval(
            self.earth_x - RE, self.earth_y - RE,
            self.earth_x + RE, self.earth_y + RE,
            fill="blue", outline="white"
        )

        # Initialize asteroid
        self.asteroid_x = self.earth_x + RQ
        self.asteroid_y = self.earth_y - 4 * RQ
        self.vx, self.vy = 0, v0

        # Label to display asteroid coordinates
        self.coord_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="white")
        self.coord_label.pack()

        # Start the simulation
        self.update_asteroid()

    def update_asteroid(self):
        # Calculate gravitational force
        dx = self.earth_x - self.asteroid_x
        dy = self.earth_y - self.asteroid_y
        r = math.sqrt(dx**2 + dy**2)
        force = G * ME * mQ / r**2
        ax = force * dx / r / mQ
        ay = force * dy / r / mQ

        # Update velocity and position
        self.vx += ax
        self.vy += ay
        self.asteroid_x += self.vx
        self.asteroid_y += self.vy

        # Draw asteroid
        self.canvas.delete("asteroid")
        self.canvas.create_oval(
            self.asteroid_x - 5, self.asteroid_y - 5,
            self.asteroid_x + 5, self.asteroid_y + 5,
            fill="yellow", tags="asteroid"
        )

        # Update coordinates label
        self.coord_label.config(
            text=f"Asteroid Coordinates: ({self.asteroid_x:.2f}, {self.asteroid_y:.2f})"
        )

        # Schedule the next update
        self.root.after(50, self.update_asteroid)

if __name__ == "__main__":
    root = tk.Tk()
    simulation = AsteroidSimulation(root)
    root.mainloop()f
