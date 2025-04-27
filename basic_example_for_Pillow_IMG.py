# def output_image(self, filename, show_solution=True, show_explored=False):

from PIL import Image, ImageDraw
BRICK_EDGE = 50
cell_border = 2

# Create a blank canvas (blue colored)
img = Image.new(
    "RGBA",
    (10 * BRICK_EDGE, 10 * BRICK_EDGE), # 10 is the number of bricks per dimension
    "blue"
)
draw = ImageDraw.Draw(img)


solution = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
# for i, row in enumerate(self.walls):
#     for j, col in enumerate(row):

for i in range(BRICK_EDGE):
    for j in range(BRICK_EDGE):
        if (i, j) in solution:
            fill = (255, 0, 0) # 'R' the fill of the diagonaled colors ("solutions")
        elif (i < j):
            fill = (0, 171, 28) # upper right rectangle in ngreen



        # # Walls
        # if col:
        #     fill = (40, 40, 40)

        # # Start
        # elif (i, j) == self.start:
        #     fill = (255, 0, 0)

        # # Goal
        # elif (i, j) == self.goal:
        #     fill = (0, 171, 28)

        # Solution
        # elif solution is not None and show_solution and (i, j) in solution:
        #     fill = (220, 235, 113)

        # # Explored
        # elif solution is not None and show_explored and (i, j) in self.explored:
        #     fill = (212, 97, 85)

        # # Empty cell
        else:
            fill = (237, 240, 252) # white color fill(for the rest which are no in solution)

        # Draw cell
        draw.rectangle(
            ([(j * BRICK_EDGE + cell_border, i * BRICK_EDGE + cell_border),
              ((j + 1) * BRICK_EDGE - cell_border, (i + 1) * BRICK_EDGE - cell_border)]),
            fill=fill
        )

img.save("maze.png")