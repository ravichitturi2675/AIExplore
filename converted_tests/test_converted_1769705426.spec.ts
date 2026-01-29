import { test, expect } from '@playwright/test';
import { chromium } from 'playwright';

test.describe('VwoLoginTest', () => {
  let driver: any;
  let wait: any;

  beforeEach(async () => {
    const options = new ChromeOptions();
    options.addArguments('--start-maximized');

    driver = await chromium.launch(options);
    wait = new WebDriverWait(driver, Duration.ofSeconds(20));

    await driver.get('https://app.vwo.com');
  });

  test('loginToVwo', async () => {
    // Email field
    const email = await wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@type='email' or @placeholder='Enter email ID']")));
    await email.fill('test@example.com');

    // Password field
    const password = await driver.findElement(By.xpath("//input[@type='password' or @placeholder='Enter password']"));
    await password.fill('Password@123');

    // Remember Me checkbox
    const rememberMe = await driver.findElement(By.xpath("//input[@type='checkbox']"));
    if (!await rememberMe.isSelected()) {
      await rememberMe.click();
    }

    // Sign In button
    const signInButton = await driver.findElement(By.xpath("//button[.//text()[contains(.,'Sign in')]]"));
    await signInButton.click();
  });

  afterEach(() => {
    driver.quit();
  });
});