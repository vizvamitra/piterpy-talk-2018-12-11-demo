class Container:
  def __init__(self):
    self._deps = {}

  def register(self, name, dep):
    self._deps[name] = dep

  def resolve(self, name):
    return self._deps[name]
