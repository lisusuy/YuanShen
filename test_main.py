from test_cla import CodeScannerpy
from cla_java import CodeScannerjava
def main():
    rule_file = 'python_rules.yml'  # 请替换为实际的规则文件路径
    folder_path = 'Z:/p1nk/BUPT/A_scan/YIBAN/new/folder/'

    code_scanner = CodeScannerpy(rule_file)
    code_scanner.scan_folder(folder_path)

if __name__ == "__main__":
    main()