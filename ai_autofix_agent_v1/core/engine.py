import subprocess
from openai import OpenAI
from .prompts import FIXER_SYSTEM_PROMPT, FIXER_USER_TEMPLATE, REVIEWER_SYSTEM_PROMPT, REVIEWER_USER_TEMPLATE

class AutoFixEngine:
    def __init__(self, api_key, model):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run_tests(self, file_path):
        """执行目标文件并捕获报错"""
        result = subprocess.run(["python3", file_path], capture_output=True, text=True)
        return result.returncode == 0, result.stderr + result.stdout

    def fix_code(self, code, error_log):
        """调用 Fixer Agent"""
        prompt = FIXER_USER_TEMPLATE.format(code=code, error_log=error_log)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": FIXER_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    def review_code(self, code):
        """调用 Reviewer Agent"""
        prompt = REVIEWER_USER_TEMPLATE.format(code=code)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": REVIEWER_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content.strip()
        return code if "PASS" in result.upper() else result
