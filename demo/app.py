from dry.container import Container
from dry.auto_inject import AutoInject

container = Container()
Inject = AutoInject(container)

from demo import importer

container.register('download_feed', importer.DownloadFeed())
container.register('parse_products', importer.ParseProducts())
