# -*- coding: utf-8 -*-
import pytest

from src.JsonDataReader import JsonDataReader
from src.TextDataReader import TextDataReader
from src.main import get_path_from_arguments, get_reader


class TestMain:
    def test_get_path_from_arguments(self) -> None:
        path = get_path_from_arguments(["-p", "data/data.json"])
        assert path == "data/data.json"

    def test_get_path_missing_raises(self) -> None:
        with pytest.raises(SystemExit):
            get_path_from_arguments([])

    def test_get_reader_json(self) -> None:
        assert isinstance(get_reader("data/data.json"), JsonDataReader)

    def test_get_reader_text(self) -> None:
        assert isinstance(get_reader("data/data.txt"), TextDataReader)
