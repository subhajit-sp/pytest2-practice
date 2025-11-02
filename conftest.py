import pytest

@pytest.fixture(scope="session")
def setup():
    print("Setup staring")
    yield
    print("setup closing")

@pytest.fixture(scope="session")
def value_provider(request):
    value = ["value1", "value2", "value3", "value4"]
    return value
