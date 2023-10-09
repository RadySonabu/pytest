from apps.main import main
from dotenv import load_dotenv

load_dotenv()
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_main():
    value = main()

    assert value == '123'