import os
import time
from ai_engine import AIEngine

class JavaToPlaywrightConverter:
    def __init__(self):
        self.ai = AIEngine()
        self.output_dir = os.path.join(os.getcwd(), "converted_tests")
        os.makedirs(self.output_dir, exist_ok=True)

    def convert(self, java_code):
        # 1. Generate Code using AI
        ts_code = self.ai.generate_playwright_code(java_code)
        
        # 2. Add boilerplate imports if missing
        if "import { test, expect } from '@playwright/test';" not in ts_code:
            ts_code = "import { test, expect } from '@playwright/test';\n\n" + ts_code

        # 3. Save to file
        timestamp = int(time.time())
        filename = f"test_converted_{timestamp}.spec.ts"
        file_path = os.path.join(self.output_dir, filename)
        
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(ts_code)
            
        return {
            "converted_code": ts_code,
            "file_path": file_path,
            "status": "success"
        }
