from dry.auto_inject import Constructor

class AutoInject:
  def __init__(self, container):
    self._container = container

  def __call__(self, *names):
    constructor = Constructor(self._container, names)
    func = lambda obj, **kwargs: constructor(obj, **kwargs)
    return lambda cls: [setattr(cls, '__init__', func), cls][1]
