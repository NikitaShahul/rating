# -*- coding: utf-8 -*-
import json

import pytest

from src.JsonDataReader import JsonDataReader
from src.Types import DataType


class TestJsonDataReader:
    @pytest.fixture()
    def reader(self) -> JsonDataReader:
        return JsonDataReader()

    def test_read_returns_dict(
            self, reader: JsonDataReader, tmp_path) -> None:
        content = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "физика": 100,
                "информатика": 91,
            }
        }
        path = tmp_path / "data.json"
        path.write_text(json.dumps(content, ensure_ascii=False),
                        encoding='utf-8')
        result: DataType = reader.read(str(path))
        assert "Иванов Иван Иванович" in result
        assert ("физика", 100) in \
            result["Иванов Иван Иванович"]

    def test_read_scores_are_int(
            self, reader: JsonDataReader, tmp_path) -> None:
        content = {"Сидоров Семён": {"математика": 55}}
        path = tmp_path / "data.json"
        path.write_text(json.dumps(content, ensure_ascii=False),
                        encoding='utf-8')
        result: DataType = reader.read(str(path))
        for _, score in result["Сидоров Семён"]:
            assert isinstance(score, int)
