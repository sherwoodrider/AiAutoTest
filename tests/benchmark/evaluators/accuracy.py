def calculate_accuracy(correct: int, total: int) -> float:
    return round(correct / total * 100, 2) if total > 0 else 0.0