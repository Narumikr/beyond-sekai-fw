import { describe, expect, it } from 'vitest';
import { getDictionary } from './get-dictionary';

describe('getDictionary', () => {
  it('jaロケールで日本語辞書を返す', async () => {
    const dict = await getDictionary('ja');
    expect(dict.page.greeting).toBe('ハローセカイ');
  });

  it('enロケールで英語辞書を返す', async () => {
    const dict = await getDictionary('en');
    expect(dict.page.greeting).toBe('Hello SEKAI');
  });
});
