import pytest

@pytest.fixture(scope="session", autouse=True)
def setup():
    print("Setup staring")
    yield
    print("setup closing")

@pytest.fixture(scope="session")
def value_provider(request):
    print("I am in value provider")
    value = ["value1", "value2", "value3", "value4"]
    return value
