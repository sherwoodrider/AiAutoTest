import json

import requests
from pathlib import Path


def load_mmlu_dataset(subset="biology", cache_dir="benchmarks/deepseek/datasets/mmlu"):
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    file_path = f"{cache_dir}/{subset}.json"

    if not Path(file_path).exists():
        url = f"https://huggingface.co/datasets/mmlu/resolve/main/{subset}.json"
        data = requests.get(url).json()
        with open(file_path, 'w') as f:
            json.dump(data, f)

    with open(file_path) as f:
        return [(q["question"], q["answer"]) for q in json.load(f)]