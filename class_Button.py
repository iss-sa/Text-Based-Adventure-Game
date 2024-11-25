class Button():
	""" class for the buttons on end_screen:
		it can update the button image and text, check for input from user (boolian value) 
		and change color if user places mouse over button"""
		
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image  #"background" image of button
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color # if you hover over button it can change color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None: # if no image given
			self.image = self.text 
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) 
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):  # update screen
		if self.image is not None:
			screen.blit(self.image, self.rect) # blit image if image was given
		screen.blit(self.text, self.text_rect) # blit also text (after the image, so that text is visible)

	def checkForInput(self, position):  # check if your position in range of button rect 
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True 
		return False

	def changeColor(self, position):  # change color if you hover over button rect
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)