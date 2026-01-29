import requests
import json

class AIEngine:
    def __init__(self, model="codellama", url="http://localhost:11434/api/generate"):
        self.model = model
        self.url = url

    def generate_playwright_code(self, java_code):
        prompt = self._construct_prompt(java_code)
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2, # Low temperature for deterministic mapping
                "stop": ["```java", "User:", "Java Code:"] 
            }
        }

        try:
            response = requests.post(self.url, json=payload, timeout=300)
            response.raise_for_status()
            result = response.json()
            return self._clean_output(result.get("response", ""))
        except Exception as e:
            return f"// Error generating code: {str(e)}"

    def _construct_prompt(self, code):
        return f"""
You are an expert Test Automation Engineer specializing in migrating Selenium Java (TestNG) assertions to Playwright TypeScript.

### Task
Convert the following Selenium Java code to Playwright TypeScript.

### Rules
1. **Structure:**
   - `public class X` -> `test.describe('X', ...)`
   - `@Test` -> `test('name', ...)`
   - `@BeforeMethod` -> `test.beforeEach(...)`
2. **Selectors:**
   - `By.id("foo")` -> `page.locator('#foo')`
   - `By.xpath("//div")` -> `page.locator('xpath=//div')`
   - `By.cssSelector(".bar")` -> `page.locator('.bar')`
3. **Actions:**
   - `.click()` -> `await locator.click()`
   - `.sendKeys("txt")` -> `await locator.fill("txt")`
   - `.getText()` -> `await locator.innerText()`
4. **Assertions:**
   - `Assert.assertEquals(actual, expected)` -> `await expect(actual).toBe(expected)`
   - `Assert.assertTrue(condition)` -> `expect(condition).toBeTruthy()`
5. **Output:** Only output the TypeScript code. Do not explain. Wrap in markdown code block.

### Input (Java)
```java
{code}
```

### Output (Playwright TypeScript)
"""

    def _clean_output(self, text):
        # Remove Markdown wrappers if present
        text = text.replace("```typescript", "").replace("```javascript", "").replace("```", "")
        return text.strip()
