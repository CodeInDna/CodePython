# Unit Testing
from random import choice
def eat(food, ishealthy):
	if not isinstance(ishealthy, bool):
		raise ValueError("ishealthy must be a boolean")
	ending = "because YOLO."
	if ishealthy:
		ending = "because my body is a Temple."
	return f"I'm eating broccoli, {ending}"

def nap(num_hours):
	if num_hours >= 2:
		return f"Ugh I overslept. I didn't mean to nap for such long hours!"
	return "I'm feeling refreshed after my 1 hour nap"

def is_funny(name):
	if name is "tim": return False
	return True

def laugh():
	return choice(('lol','haha','hehe'))