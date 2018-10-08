import unittest

import dry
from dry.container import Container

class TestContainer(unittest.TestCase):
  def setUp(self):
    self.container = Container()

  def test_resolve_known(self):
    self.container.register('test', 1)

    result = self.container.resolve('test')
    self.assertEqual(result, 1)

  def test_fails_with_key_error_when_resolving_unknown(self):
    self.container.register('test', 1)

    try:
      self.container.resolve('should fail')
      self.assertFail()
    except Exception as err:
      self.assertIsInstance(err, KeyError)
