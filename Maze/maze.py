# handle the FileNotFoundError exception

# note that:
# >> "\\".join(sys.argv[0].split('\\')[:-1]) # returns --> 'C:\\Python_Rust_Removal\\AI_CS50_Harvard\\Maze'

from pathlib import Path
script_path = Path(__file__).parent


import sys
import warnings
# import os


# to have user configured exception (more clearly defined); e.g. "fileInputException: maze must have exactly one start point"
class fileInputException(Exception):  
	...


class Node:
	"""docstring for None"""
	def __init__(self, state, parent, action):
		# super(None, self).__init__()
		self.state = state  # (i, j) tuple - for (row, col)
		self.parent = parent # the node from which we progressed (starts from None at the beginning)
		self.action = action  # "up", "down", "left", "right"


class StackFrontier(): # remind that a Stack is last-in first-out 'data-structure' ('depth for search' DFS algorithm)
	"""docstring for StackFrontier"""
	def __init__(self):
		self.frontier = [] # to be list of nodes to examine one by one (either via the 'Stack' or the 'Queue' algorithm)
		
	def add(self, node):
		self.frontier.append(node)


	def contains_state(self, state):
		# when adding neighbors to the frontier, we want to ensure that it's state is not among the current listed frontier nodes states
		return any(node.state == state for node in self.frontier)

	def empty(self):  # used with:  if empty()
		return len(self.frontier) == 0


	def remove(self): # removing the last added noded for the Stack DS implementation
		if self.empty():
			raise Exception("empty frontier")
		else:
			# node = self.frontier[-1]
			# self.frontier = self.frontier[:-1]
			node = self.frontier.pop() # replacing the above 2 lines in a single line
			return node # I guess we shall pass it to the set (since we've been visiting here)


# inheriting from above class, in case we decide to implement the shallow scan Algorithm
class QueueFrontier(StackFrontier):
	"""docstring for QueueFrontier"""

	def remove(self): # removing the first  added noded for the Queue DS implementation
		if self.empty():
			raise Exception("empty frontier")
		else:
			node = self.frontier[0]
			self.frontier = self.frontier[1:]
			return node # I guess we shall pass it to the set (since we've been visiting here)

	

class Maze(): # getting a text file to represent a maze language by symbols
	"""Maze solver class. Use Maze.create(filename) instead of direct instantiation."""
	_factory_creation = False  # Class-level flag - > to trigger the warning only upon direct instantiation and not upon using the create() method

	@classmethod
	def create(cls, filename):
		"""Preferred creation method with error handling."""
		cls._factory_creation = True # set flag before instantiation to avoid unnecessary warning
		try:
			return cls(filename)
		except Exception as e:
			print(f"{type(e).__name__}: {e}")
			return None
		finally: cls._factory_creation = False  # Reset flag afterward


	def __init__(self, filename):
		"""Warning: Avoid direct instantiation. Use Maze.create() instead!"""
		if not self.__class__._factory_creation:
			warnings.warn("Direct instantiation may raise exceptions. Use Maze.create() instead.", UserWarning,stacklevel=2)



		#Read file and set height and width of maze
		# note that the build-in exception is raised anyhow by the create(cls, filename) class method
		with open(filename) as f:
			contents = f.read()


		# validate start and goal
		if contents.count("A") != 1:
			raise fileInputException("maze must have exactly one start point")
		if contents.count("B") != 1:
			raise fileInputException("maze must have exactly one end point")


		# Determines height and width of maze
		contents = contents.splitlines() # getting an array of lines?
		self.height = len(contents)
		self.width = max(len(line) for line in contents) # the length of the lengthiest line


		#Keep track of walls
		self.walls = []
		for i in range(self.height):
			row = []
			for j in range(self.width):
				try:
					if contents[i][j] == "A":
						self.start = (i, j)
						row.append(False)
					elif contents[i][j] == "B":
						self.goal = (i, j)
						row.append(False)
					elif contents[i][j] == " ":
						row.append(False)
					else:
						row.append(True)
				except:
					pass
			self.walls.append(row)

		self.solution = None


	def print(self):
		solution = self.solution[1] if self.solution is not None else None # self.solution[1] since later the self.solution arg becomes a tuple (actions, cells)
		print()
		for i , row in enumerate(self.walls):
			for j, col in enumerate(row):
				if col: # if there's a wall
					print("█", end="")
				elif (i,j)==self.start:
					print("A", end="")
				elif (i,j)==self.goal:
					print("B", end="")
				elif solution is not None and (i,j) in solution:
					print("*", end="")
				else:
					print(" ", end="")
			print()
		print()

				
	def neighbors(self, state):
		row, col = state

		# All possible actions
		candidates = [
			("up", (row - 1, col)),
			("down", (row + 1, col)),
			("left", (row, col - 1)),
			("right", (row, col + 1)),
		]

		#Ensure actions are valid (getting all possible action from a certain coord)
		results = []
		for action, (r,c) in candidates:
			try:
				if not self.walls[r][c]:
					results.append((action, (r, c)))
			except IndexError:
				continue
		return results


	def solve(self): #another Maze class method
		"""Finds a solution to maze, if one exists."""

		# Keep track of number of states explored
		self.num_explored = 0

		# Initialize frontier to just the starting position
		start = Node(state=self.start, parent=None, action=None) # getting the initial state, (i, j) Tuple, from class member instantiation
		frontier = StackFrontier()
		frontier.add(node = start)

		# Initialize an empty explored set
		self.explored = set()

		#Keep looping until solution found
		while True:

			# If nothing left in frontier, then no path
			if frontier.empty():
				raise Exception("no solution")

			# Choose a node from the frontier
			node = frontier.remove() # like .pop()
			self.num_explored+=1

			# If node is the goal, then we have a solution
			if node.state == self.goal:
				actions = []
				cells = []

				# Follow parent nodes to find solution
				while node.parent is not None:  # maybe revese engineering here?
					actions.append(node.action)  # "Up" | "Down"| "Left"| "Right" 
					cells.append(node.state)
					node = node.parent # working here like connected list a --> b --> c --> d ...
				actions.reverse() # so the actions list starts from left to right
				cells.reverse() # so the actions list starts from left to right
				self.solution = (actions, cells)
				return # getting out of the loop


			# Mark node as explored
			self.explored.add(node.state) # state is (i, j) coords per the state

			# Add neightbors to frontier
			for action, state in self.neighbors(node.state): # adding potential nodes to investigate into the frontier
				if not frontier.contains_state(state) and state not in self.explored:
					child = Node(state=state, parent=node, action=action)
					frontier.add(child)


def main():
	my_maze = Maze.create(script_path / "maze3.txt") # makes it more robust (earlier it failed when using the new build system with inner directory instead of the prior root)
	# my_maze = Maze.create(".Maze/maze2.txt")
	# my_maze = Maze("./maze2.txt") # this shall result with the warning: "UserWarning: Direct instantiation may raise exceptions. Use Maze.create() instead."

	if my_maze != None:
		my_maze.solve()
		my_maze.print()


if __name__ == "__main__":
	main()




# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(arr.pop())

# print(arr)
# 9
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 9
