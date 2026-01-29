# Conversion Logic SOP

## Mapping Strategy
We will use a specialized "Find & Replace" strategy with context awareness (Line-by-line + Block parsing).

## Key Mappings

### 1. Test Structure (TestNG -> Playwright)
| Java | Playwright TS |
|------|---------------|
| `public class LoginTest {` | `test.describe('LoginTest', () => {` |
| `@Test` | `test('testName', async ({ page }) => {` |
| `@BeforeMethod` | `test.beforeEach(async ({ page }) => {` |
| `@AfterMethod` | `test.afterEach(async ({ page }) => {` |

### 2. Locators (Selenium -> Playwright)
| Java | Playwright TS |
|------|---------------|
| `driver.findElement(By.id("user"))` | `page.locator('#user')` |
| `driver.findElement(By.cssSelector(".btn"))` | `page.locator('.btn')` |
| `By.xpath("//div")` | `page.locator('xpath=//div')` |

### 3. Actions
| Java | Playwright TS |
|------|---------------|
| `.click()` | `.click()` (await) |
| `.sendKeys("text")` | `.fill("text")` (await) |
| `.getText()` | `.innerText()` (await) |

### 4. Assertions
| Java | Playwright TS |
|------|---------------|
| `Assert.assertEquals(actual, expected)` | `await expect(actual).toBe(expected)` |
| `Assert.assertTrue(condition)` | `expect(condition).toBeTruthy()` |
| `driver.getTitle()` | `await page.title()` |

## Edge Case Handling
- **Waits:** Remove `Thread.sleep` and `WebDriverWait` where possible; rely on Auto-wait.
- **Variable Types:** Convert `String` -> `const` or `let`. `int` -> `const`.
