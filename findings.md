# Findings

## Research
- [ ] Search for existing conversion tools/libraries from Selenium Java to Playwright TS/JS.
- [ ] Identify key mapping differences between Selenium Java API and Playwright API.

## Discoveries
- **Async Nature:** Playwright is async. All interactions must be prefixed with `await`.
- **Selectors:** Playwright locators are more robust. `By.id` -> `#id`, `By.xpath` -> `xpath=...`.
- **Assertions:** TestNG `Assert` is synchronous. Playwright `expect` is web-aware and async (e.g. `await expect(locator).toBeVisible()`).
- **Environment:** System Python is missing from PATH. Use `C:\Users\Adqura\AppData\Local\Programs\Python\Launcher\py.exe` to run scripts.

## Constraints
- **Complexity:** Complex logic (Variables passed between methods, inheritance) is hard to convert with Regex. We will focus on "In-File" conversion first.
- **Language:** Target is TypeScript (strict mode preferred).

