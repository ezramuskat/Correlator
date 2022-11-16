
#this is going to be updated to be a db model later
#likely going to change datapoints to reflect a graph
class Pattern():
	def __init__(self, name:str, patterns:list[str], datapoints:list[str]):
		self.name = name
		self.patterns = patterns
		self.datapoints = datapoints