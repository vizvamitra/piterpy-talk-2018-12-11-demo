import dry

container = dry.Container()
container.register('test', 1)
container.resolve('test') # => 1

Inject = dry.AutoInject(container)

@Inject('test')
class MyClass:
  pass

print(MyClass().test)
