class Constructor:
  def __init__(self, container, names):
    self._container = container
    self._names = names

  def __call__(self, obj, **kwargs):
    self._check_unexpected_kwargs(kwargs)

    for name in self._names:
      val = kwargs.get(name) or self._container.resolve(name)
      obj.__setattr__('_'+name, val)

  def _check_unexpected_kwargs(self, kwargs):
    unexpected_kwargs = kwargs.keys() - self._names

    if len(unexpected_kwargs) > 0:
      msg = "__init__() got an unexpected keyword argument '{}'".format(unexpected_kwargs.pop())
      raise KeyError(msg)
