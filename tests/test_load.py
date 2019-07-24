from environment import Environment


def test_load():
    env = Environment()

    print(f"Loaded threshold {env.threshold}")
    assert type(env.threshold) is float


def test_render():
    env = Environment()
    env.render()

    assert type(env.stream) is list
