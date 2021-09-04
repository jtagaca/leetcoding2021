def sunsetViews(buildings, direction):
    # Write your code here.
	sIDX = 0 if direction == "EAST" else len(buildings)-1
	step = 1 if direction == "EAST" else -1
	stack = []
	while sIDX >= 0 and sIDX < len(buildings):
		currentBuilding = buildings[sIDX]
		# we keep popping til we find a building that is not bigger than use
		# since if we are bigger then we should not return that since we are blocking it
		# the order is important as well.
		while len(stack) > 0 and currentBuilding >= buildings[stack[-1]]:
			stack.pop()
		stack.append(sIDX)
		sIDX += step
	return stack if direction == "EAST" else stack[::-1]
