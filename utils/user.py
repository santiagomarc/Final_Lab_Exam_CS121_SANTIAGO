class User:
	def __init__(self, username=None, password=None, points=0, stages_won=0):
		self.username = username
		self.password = password
		self.points = points
		self.stages_won = stages_won