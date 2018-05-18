def get_pressure():
	"""Returns the pressure in the system."""
	return sys_press

def calc_press_diff(in, out):
	"""Calculates the pressure drop across a valve.

	:param in: Input pressure
	:param out: Output pressure
	:return The valve pressure drop
	"""
	deltaP = out - in
	return deltaP
