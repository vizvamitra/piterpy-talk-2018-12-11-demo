class ParseProducts:
  def __call__(self, feed):
    return ['Product {}'.format(item) for item in feed]
