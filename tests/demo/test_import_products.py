import unittest

from demo.importer import ImportProducts

class TestImportProducts(unittest.TestCase):
  def setUp(self):
    self.subject = ImportProducts()

  def test_uses_defaults_when_constructed_without_deps(self):
    import_products = ImportProducts()

    self.assertEqual(import_products(), ["Product 1", "Product 2", "Product 3"])

  def test_accepts_deps_via_constructor(self):
    import_products = ImportProducts(
      download_feed = lambda : [1,2],
      parse_products = lambda feed : ["Item {}".format(item) for item in feed]
    )

    self.assertEqual(import_products(), ["Item 1", "Item 2"])
