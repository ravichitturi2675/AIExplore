import { test, expect } from '@playwright/test';

test('Web', async () => {
  // Set the system property for ChromeDriver (path to chromedriver executable)
  const driver = await new ChromeDriver();

  try {
    // Navigate to the desired website (GeeksforGeeks in this example)
    await driver.get('https://www.geeksforgeeks.org/');

    // Get and print the page title
    const pageTitle = await driver.getTitle();
    console.log(`Page Title: ${pageTitle}`);

    // Wait for a few seconds (for demonstration purposes only)
    await new Promise(resolve => setTimeout(resolve, 3000));
  } catch (e) {
    console.error(e);
  } finally {
    // Close the browser
    await driver.quit();
  }
});