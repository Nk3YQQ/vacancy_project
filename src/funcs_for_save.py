import csv
import json
from pathlib import Path
from typing import Any


def open_json_file(filepath: Path) -> Any:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError("Указанный файл не найден.")


def write_to_json_file(filepath: Path, data: Any) -> Any:
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        raise FileNotFoundError("Указанный файл не найден.")


def open_csv_file(filepath: Path) -> Any:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        raise FileNotFoundError("Указанный файл не найден.")


def write_to_csv_file(filepath: Path, data: Any) -> Any:
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            fieldnames = ["vacancy", "url", "salary", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    except FileNotFoundError:
        raise FileNotFoundError("Указанный файл не найден.")
