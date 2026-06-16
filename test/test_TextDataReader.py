# -*- coding: utf-8 -*-
import pytest

from src.TextDataReader import TextDataReader
from src.Types import DataType


class TestTextDataReader:
    @pytest.fixture()
    def reader(self) -> TextDataReader:
        return TextDataReader()

    def test_read_returns_dict(
            self, reader: TextDataReader, tmp_path) -> None:
        content = (
            "Иванов Иван Иванович\n"
            "    математика: 67\n"
            "    физика: 100\n"
            "    информатика: 91\n"
        )
        path = tmp_path / "data.txt"
        path.write_text(content, encoding='utf-8')
        result: DataType = reader.read(str(path))
        assert "Иванов Иван Иванович" in result
        assert ("математика", 67) in \
            result["Иванов Иван Иванович"]

    def test_read_multiple_students(
            self, reader: TextDataReader, tmp_path) -> None:
        content = (
            "Иванов Иван Иванович\n"
            "    математика: 67\n"
            "Петров Петр Петрович\n"
            "    физика: 55\n"
        )
        path = tmp_path / "data.txt"
        path.write_text(content, encoding='utf-8')
        result: DataType = reader.read(str(path))
        assert len(result) == 2
