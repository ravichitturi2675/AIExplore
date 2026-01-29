import { test, expect } from '@playwright/test';
import { chromium } from 'playwright';

test.describe('GoogleTest', () => {
  let driver: any;

  test.beforeEach(async ({ page }) => {
    driver = await chromium.launch();
    await page.goto('https://www.google.com');
  });

  test('verifyGoogleTitle', async ({ page }) => {
    const title = await page.title();
    console.log(`Page title: ${title}`);
    expect(title).toContain('Google');
  });

  test('searchInGoogle', async ({ page }) => {
    await page.fill('#q', 'Selenium TestNG');
    await page.click('#q');
    expect(await page.title()).toContain('Selenium');
  });

  test.afterEach(async () => {
    await driver.close();
  });
});