import { expect, test } from '@playwright/test';

const reference = new URL(
  '../initiatives/textile-interface/reference/thread-button/index.html',
  import.meta.url,
);

test.beforeEach(async ({ page }) => {
  await page.goto(reference.href);
});

test('commit and undo keep the live announcement and visual state in sync', async ({ page }) => {
  const button = page.getByRole('button', { name: 'Stitch commitment', exact: true });
  const status = page.locator('#button-status');

  await expect(status).toHaveAttribute('aria-live', 'polite');
  await expect(status).toHaveText('Not committed.');
  await expect(button).toHaveAttribute('data-state', 'loose');
  await expect(button).toHaveAttribute('aria-pressed', 'false');

  for (const [pressed, state, announcement] of [
    ['true', 'committed', 'Commitment stitched.'],
    ['false', 'loose', 'Commitment removed.'],
    ['true', 'committed', 'Commitment stitched.'],
  ]) {
    await button.click();
    await expect(button).toHaveAttribute('aria-pressed', pressed);
    await expect(button).toHaveAttribute('data-state', state);
    await expect(status).toHaveText(announcement);
  }
});

test('reduced motion suppresses active displacement without suppressing activation', async ({ page }) => {
  // Use a mouse for the held :active state; mobile tap is covered by the visual verifier.
  const button = page.getByRole('button', { name: 'Stitch commitment', exact: true });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await button.hover();
  await page.mouse.down();
  try {
    await expect(page.locator('.thread-button:active')).toHaveCount(1);
    await expect(button).toHaveCSS('transform', 'none');
    await expect(button).toHaveCSS('transition-duration', '0s');
    await expect(button).toHaveAttribute('aria-pressed', 'false');
  } finally {
    await page.mouse.up();
  }
  await expect(button).toHaveAttribute('aria-pressed', 'true');
});
