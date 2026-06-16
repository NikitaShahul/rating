# -*- coding: utf-8 -*-
import pytest

from src.DebtCounter import DebtCounter
from src.Types import DataType


class TestDebtCounter:
    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("физика", 100),
                ("информатика", 91),
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("физика", 87),
                ("информатика", 61),
            ],
            "Сидоров Семён Семёнович": [
                ("математика", 55),
                ("физика", 40),
                ("информатика", 88),
            ],
        }

    def test_count_default_threshold(self, input_data: DataType) -> None:
        counter = DebtCounter(input_data)
        assert counter.count() == 1

    def test_debtors_default_threshold(self, input_data: DataType) -> None:
        counter = DebtCounter(input_data)
        assert counter.debtors() == ["Сидоров Семён Семёнович"]

    def test_count_custom_threshold(self, input_data: DataType) -> None:
        counter = DebtCounter(input_data, threshold=70)
        assert counter.count() == 3
