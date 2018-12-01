from demo.app import Inject

@Inject('download_feed', 'parse_products')
class ImportProducts:
  def __call__(self):
    feed = self._download_feed()
    return self._parse_products(feed)
