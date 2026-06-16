# -*- coding: utf-8 -*-
from Types import DataType


class DebtCounter:
    """Подсчёт студентов с академическими задолженностями."""

    def __init__(self, data: DataType, threshold: int = 61) -> None:
        self.data: DataType = data
        self.threshold: int = threshold

    def debtors(self) -> list[str]:
        result: list[str] = []
        for name, subjects in self.data.items():
            if any(score < self.threshold for _, score in subjects):
                result.append(name)
        return result

    def count(self) -> int:
        return len(self.debtors())
