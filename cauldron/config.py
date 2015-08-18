import inspect


RULES = {
    'walk': [
        lambda x: x.endswith('.py'),
        # lambda x: not x.startswith('__'),
        lambda x: not x.startswith('.'),
        lambda x: not x.startswith('00'),
        lambda x: not x.startswith('test'),
        lambda x: not x.startswith('wsgi'),
    ],
    'inspect': [
        lambda x: not x[0].startswith('__'),
        lambda x: inspect.isclass(x[1]),
    ]
}
