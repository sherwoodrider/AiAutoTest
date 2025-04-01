import os
import json
import yaml
from datetime import datetime
from .evaluators.accuracy import calculate_accuracy
from .datasets.mmlu import load_mmlu_dataset


class DeepSeekBenchmark:
    def __init__(self, config_path="config/deepseek_benchmark.json"):
        self.config = self._load_config(config_path)
        self.log_dir = "logs/benchmark_deepseek"
        os.makedirs(self.log_dir, exist_ok=True)

    def _load_config(self, path):
        with open(path) as f:
            return json.load(f)

    def run(self):
        results = {}
        for benchmark in self.config["benchmarks"]:
            if benchmark == "mmlu":
                results["mmlu"] = self._run_mmlu()
            # 扩展其他测试...

        self._save_results(results)
        return results

    def _run_mmlu(self):
        dataset = load_mmlu_dataset(subset="biology")  # 示例：生物学子集
        correct = 0
        total = len(dataset)

        for question, answer in dataset:
            response = self._query_model(question)
            if self._check_answer(response, answer):
                correct += 1

        return {
            "accuracy": calculate_accuracy(correct, total),
            "details": f"{correct}/{total}"
        }

    def _query_model(self, prompt):
        # 实现API或本地模型调用
        if self.config["model_type"] == "api":
            return self._call_api(prompt)
        else:
            return self._call_local_model(prompt)

    def _save_results(self, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = f"{self.log_dir}/result_{timestamp}.json"
        with open(log_path, 'w') as f:
            json.dump(results, f, indent=2)