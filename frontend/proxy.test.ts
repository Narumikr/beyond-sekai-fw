import type { NextRequest } from 'next/server';
import { describe, expect, it } from 'vitest';
import { getLocale } from './proxy';

/**
 * テスト用に最小限の NextRequest モックを生成するヘルパー。
 * as unknown as NextRequest を使い、型チェックをバイパスする。
 * 実際のテスト対象（Accept-Language ヘッダーの読み取り）に必要なプロパティだけ実装する。
 */
function mockRequest(acceptLanguage: string): NextRequest {
  return {
    headers: {
      get: (name: string) => (name === 'accept-language' ? acceptLanguage : null),
    },
  } as unknown as NextRequest;
}

describe('getLocale', () => {
  it('日本語のAccept-Languageに対してjaを返す', () => {
    expect(getLocale(mockRequest('ja'))).toBe('ja');
  });

  it('英語のAccept-Languageに対してenを返す', () => {
    expect(getLocale(mockRequest('en-US,en;q=0.9'))).toBe('en');
  });

  it('q値の高い言語を優先する', () => {
    expect(getLocale(mockRequest('en;q=0.8,ja;q=0.9'))).toBe('ja');
  });

  it('未対応言語の場合はデフォルトのjaを返す', () => {
    expect(getLocale(mockRequest('zh-hant'))).toBe('ja');
  });

  it('空のAccept-Languageの場合はデフォルトのjaを返す', () => {
    expect(getLocale(mockRequest(''))).toBe('ja');
  });
});
