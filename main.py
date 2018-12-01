import dry
import demo
from demo.importer import ImportProducts

products = ImportProducts()()

print('\n'.join(products))
