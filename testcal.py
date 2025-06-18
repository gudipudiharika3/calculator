from main import add, subtract, multiply, divide, calculator


def test_add():
    assert add(6 ,7) == 13


def test_sub():
    assert subtract(7,8) == -1


def test_multiply():
    assert multiply(4, 6) == 24


def test_divide():
    assert divide(6,3) == 2


def test_divide_by_zero():
    assert divide(5,0) == "Error: Division By zero"


def test_invalid_choice(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '9')
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out

    
def test_input(monkeypatch, capsys):
    inputs = iter(['1', '5', 'add'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only" in captured.out

