import unittest

import dry
from dry.auto_inject import Constructor
from dry.container import Container

class TestConstructor(unittest.TestCase):
  def setUp(self):
    container = Container()
    container.register('test', 1)

    self.constructor = Constructor(container, ['test'])

    class Dummy: pass
    self.object = Dummy()

  def test_resolves_when_none(self):
    self.constructor(self.object, test=None)
    self.assertEqual(self.object.test, 1)

  def test_resolves_when_not_given(self):
    self.constructor(self.object)
    self.assertEqual(self.object.test, 1)

  def test_takes_from_kwargs_when_present(self):
    self.constructor(self.object, test=2)
    self.assertEqual(self.object.test, 2)

  def test_fails_with_key_error_when_unknown_key_given(self):
    try:
      self.constructor(self.object, fail=True)
      self.assertFail()
    except Exception as err:
      self.assertIsInstance(err, KeyError)
