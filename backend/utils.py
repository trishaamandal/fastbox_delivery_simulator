import json
import math
from typing import Dict, Any, Tuple


def load_json(filepath: str) -> Dict[str, Any]:
    """
    Load and return JSON data from a file.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"JSON file not found: {filepath}")
    except json.JSONDecodeError:
        raise Exception(f"Invalid JSON format in file: {filepath}")


def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """
    Calculate Euclidean distance between two 2D points.
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """
    Save dictionary data to a JSON file.
    """
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
