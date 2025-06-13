import tkinter as tk
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
SNEAKER_SIZE = 40
GRAVITY = 3
JUMP_STRENGTH = -18
OBSTACLE_WIDTH = 50
OBSTACLE_GAP = 150
OBSTACLE_SPEED_START = 3  # Slower speed at start

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="skyblue")
        self.canvas.pack()
        self.restart_btn = None
        self.reset_game()
        self.root.bind("<space>", self.jump)

    def reset_game(self):
        self.canvas.delete("all")
        self.sneaker = self.canvas.create_text(80, WINDOW_HEIGHT//2, text="👟", font=("Arial", SNEAKER_SIZE))
        self.sneaker_y = WINDOW_HEIGHT//2
        self.velocity = 0
        self.obstacles = []
        self.score = 0
        self.obstacle_speed = OBSTACLE_SPEED_START
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", text="Score: 0", font=("Arial", 16))
        self.game_over = False
        if self.restart_btn:
            self.restart_btn.destroy()
            self.restart_btn = None
        self.spawn_obstacle()
        self.update()

    def jump(self, event):
        if not self.game_over:
            self.velocity = JUMP_STRENGTH

    def spawn_obstacle(self):
        gap_y = random.randint(100, WINDOW_HEIGHT - 100 - OBSTACLE_GAP)
        top = self.canvas.create_rectangle(
            WINDOW_WIDTH, 0, WINDOW_WIDTH + OBSTACLE_WIDTH, gap_y, fill="green"
        )
        bottom = self.canvas.create_rectangle(
            WINDOW_WIDTH, gap_y + OBSTACLE_GAP, WINDOW_WIDTH + OBSTACLE_WIDTH, WINDOW_HEIGHT, fill="green"
        )
        self.obstacles.append((top, bottom))
        if not self.game_over:
            self.root.after(1500, self.spawn_obstacle)

    def update(self):
        if self.game_over:
            return

        # Gradually increase speed for challenge
        if self.obstacle_speed < OBSTACLE_SPEED_START + 3 + self.score // 5:
            self.obstacle_speed += 0.005

        # Move sneaker
        self.velocity += GRAVITY
        self.sneaker_y += self.velocity
        self.canvas.coords(self.sneaker, 80, self.sneaker_y)

        # Check for collision with ground/ceiling
        if self.sneaker_y > WINDOW_HEIGHT or self.sneaker_y < 0:
            self.end_game()
            return

        # Move obstacles
        for top, bottom in self.obstacles:
            self.canvas.move(top, -self.obstacle_speed, 0)
            self.canvas.move(bottom, -self.obstacle_speed, 0)

        # Check for collision with obstacles
        sneaker_bbox = self.canvas.bbox(self.sneaker)
        for top, bottom in self.obstacles:
            if self.check_collision(sneaker_bbox, self.canvas.bbox(top)) or \
               self.check_collision(sneaker_bbox, self.canvas.bbox(bottom)):
                self.end_game()
                return

        # Remove passed obstacles and update score
        for top, bottom in self.obstacles[:]:
            if self.canvas.coords(top)[2] < 0:
                self.canvas.delete(top)
                self.canvas.delete(bottom)
                self.obstacles.remove((top, bottom))
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        self.root.after(30, self.update)

    def check_collision(self, bbox1, bbox2):
        if not bbox1 or not bbox2:
            return False
        x1, y1, x2, y2 = bbox1
        a1, b1, a2, b2 = bbox2
        return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="Game Over!", font=("Arial", 32), fill="red")
        self.restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 16), command=self.reset_game)
        self.restart_btn.place(x=WINDOW_WIDTH//2-50, y=WINDOW_HEIGHT//2+40, width=100)

root = tk.Tk()
root.title("Jumping Sneaker Game")
game = Game(root)
root.mainloop()