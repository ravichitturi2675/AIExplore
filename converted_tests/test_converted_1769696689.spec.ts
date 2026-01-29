import { test, expect } from '@playwright/test';
import { chromium } from 'playwright';

test.describe('Web', () => {
  let browser: Browser;
  let page: Page;

  beforeEach(async () => {
    browser = await chromium.launch();
    page = await browser.newPage();
  });

  afterEach(() => {
    browser.close();
  });

  test('should navigate to the desired website', async () => {
    await page.goto('https://www.geeksforgeeks.org/');
    const pageTitle = await page.title();
    console.log(`Page Title: ${pageTitle}`);
  });
});