class Prefix:
	def __init__(self):
		self.public = 10
		self._private = 12
test = Prefix()

print(test.public)

print(test._private)
# print(test.private) returns: "AttributeError: 'Prefix' object has no attribute 'private'"

amount = 100_000_000.0
print(amount)
