import { test, expect } from '@playwright/test';
import { chromium } from 'playwright';

test.describe('GoogleTest', () => {
  let driver: any;

  test.beforeEach(async () => {
    driver = await chromium.launch();
    await driver.manage().window().maximize();
  });

  test('verifyGoogleTitle', async () => {
    await driver.get('https://www.google.com');

    const title = await driver.getTitle();
    console.log(`Page title: ${title}`);

    expect(title).toContain('Google');
  });

  test('searchInGoogle', async () => {
    await driver.get('https://www.google.com');

    const searchInput = await driver.locator('#lst-ib');
    await searchInput.fill('Selenium TestNG');
    await searchInput.press('Enter');

    expect(await driver.title()).toContain('Selenium');
  });

  test.afterEach(async () => {
    await driver.close();
  });
});