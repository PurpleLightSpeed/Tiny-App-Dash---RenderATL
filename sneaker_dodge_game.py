import tkinter as tk
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 20
SNEAKER_SIZE = 30
SPEED = 10
SNEAKER_FALL_SPEED = 8

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
        self.canvas.pack()
        self.player = self.canvas.create_rectangle(
            WINDOW_WIDTH//2 - PLAYER_WIDTH//2, WINDOW_HEIGHT-PLAYER_HEIGHT-10,
            WINDOW_WIDTH//2 + PLAYER_WIDTH//2, WINDOW_HEIGHT-10,
            fill="blue"
        )
        self.sneakers = []
        self.score = 0
        self.game_over = False
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", text="Score: 0", font=("Arial", 14))
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.spawn_sneaker()
        self.update()

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.player, -SPEED, 0)
            self.keep_player_in_bounds()

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.player, SPEED, 0)
            self.keep_player_in_bounds()

    def keep_player_in_bounds(self):
        coords = self.canvas.coords(self.player)
        if coords[0] < 0:
            self.canvas.move(self.player, -coords[0], 0)
        if coords[2] > WINDOW_WIDTH:
            self.canvas.move(self.player, WINDOW_WIDTH - coords[2], 0)

    def spawn_sneaker(self):
        x = random.randint(0, WINDOW_WIDTH - SNEAKER_SIZE)
        sneaker = self.canvas.create_text(x + SNEAKER_SIZE//2, 0, text="👟", font=("Arial", SNEAKER_SIZE))
        self.sneakers.append(sneaker)
        if not self.game_over:
            self.root.after(random.randint(800, 1500), self.spawn_sneaker)

    def update(self):
        if self.game_over:
            return
        for sneaker in self.sneakers[:]:
            self.canvas.move(sneaker, 0, SNEAKER_FALL_SPEED)
            sneaker_coords = self.canvas.bbox(sneaker)
            player_coords = self.canvas.coords(self.player)
            # Check for collision
            if sneaker_coords and player_coords:
                if (sneaker_coords[2] > player_coords[0] and
                    sneaker_coords[0] < player_coords[2] and
                    sneaker_coords[3] > player_coords[1] and
                    sneaker_coords[1] < player_coords[3]):
                    self.game_over = True
                    self.canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="Game Over!", font=("Arial", 32), fill="red")
                    return
            # Remove sneaker if it falls off screen
            if sneaker_coords and sneaker_coords[1] > WINDOW_HEIGHT:
                self.canvas.delete(sneaker)
                self.sneakers.remove(sneaker)
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        self.root.after(30, self.update)

root = tk.Tk()
root.title("Sneaker Dodge Game")
game = Game(root)
root.mainloop()