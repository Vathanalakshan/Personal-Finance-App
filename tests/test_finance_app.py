"""Test file to test the Finance app """
from datetime import datetime

import pytest
from finance_app import Expense
from finance_app import FinanceApp
from finance_app import Income


@pytest.fixture
def init__finance_app():
    return FinanceApp()


def test_finance_app_init(init__finance_app) -> None:
    assert len(init__finance_app.transactions_history) == 0
    assert init__finance_app.funds == 0


def test_finance_app_income(init__finance_app) -> None:
    init__finance_app.add_event(Income(1000, "Test Income 1", datetime.now))
    assert len(init__finance_app.transactions_history) == 1
    assert init__finance_app.funds == 1000
    init__finance_app.add_event(Income(1000, "Test Income 2", datetime.now))
    assert len(init__finance_app.transactions_history) == 2
    assert init__finance_app.funds == 2000


def test_finance_app_expense(init__finance_app, capsys) -> None:
    init__finance_app.add_event(Expense(1000, "Test Expense 1", datetime.now))
    captured = capsys.readouterr()
    assert captured.out.split("\n")[0] == "You are missing 1000 euros"
    assert captured.out.split("\n")[1] == "Action Aborted"
    init__finance_app.add_event(Income(1000, "Test Income 1", datetime.now))
    init__finance_app.add_event(Expense(950, "Test Expense 1", datetime.now))
    assert len(init__finance_app.transactions_history) == 2
    assert init__finance_app.funds == 50


def test_finance_app_negative_value(init__finance_app) -> None:
    with pytest.raises(ValueError, match="Negative Value Error"):
        init__finance_app.add_event(Income(-1000, "Test Income 1", datetime.now))
        assert len(init__finance_app.transactions_history) == 0
        assert init__finance_app.funds == 0
    with pytest.raises(ValueError, match="Negative Value Error"):
        init__finance_app.add_event(Expense(-1000, "Test Income 1", datetime.now))
        assert len(init__finance_app.transactions_history) == 0
        assert init__finance_app.funds == 0
