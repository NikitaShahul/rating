# -*- coding: utf-8 -*-
import json

from DataReader import DataReader
from Types import DataType


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            raw = json.load(file)
        self.students = {}
        for name, subjects in raw.items():
            self.students[name] = [
                (subject, int(score))
                for subject, score in subjects.items()
            ]
        return self.students
