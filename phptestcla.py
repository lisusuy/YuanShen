import os
import re
import json
import subprocess
import yaml

class PHPCodeScanner:
    def __init__(self, rule_file,):
        self.rules = self.load_rules(rule_file)
        self.json_file_name = "results.json"
        self.match_count = 1

    def load_rules(self, rule_file):
        with open(rule_file, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            rules = data.get('rules')
        return rules

    def apply_rules(self, node):
        matched_data = []
        for rule in self.rules:
            if rule['type'] == 'regex':
                for pattern in rule['kind']:
                    if re.search(pattern, node):
                        matched_item = {
                            "ID": str(self.match_count),
                            "文件路径": "文件路径信息",  # 你需要提供文件路径信息
                            "漏洞描述": rule['name'],
                            "漏洞详细": rule['description']
                        }
                        matched_data.append(matched_item)
                        self.match_count += 1
                        print(matched_item)
        return matched_data

    def save_matched_data(self, matched_data):
        try:
            with open(self.json_file_name, "r", encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.extend(matched_data)

        with open(self.json_file_name, "w", encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)



    def scan_folder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.php'):
                    file_path = os.path.join(root, file)
                    result = subprocess.run(['node', './php.js'], stdout=subprocess.PIPE, text=True, input=file_path)
                    ast_test = result.stdout
                    ast_tree = json.loads(ast_test)
                    for child in ast_tree:
                        matched_data = self.apply_rules(str(child))
                        self.save_matched_data(matched_data)

# 使用示例
# 使用示例

