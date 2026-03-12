import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import { TestButton } from './TestButton';

describe('TestButton', () => {
  it('テキストが正しく表示される', () => {
    render(<TestButton>クリック</TestButton>);
    expect(screen.getByRole('button', { name: 'クリック' })).toBeInTheDocument();
  });

  it('クリック時にonClickが呼ばれる', async () => {
    const onClick = vi.fn();
    render(<TestButton onClick={onClick}>クリック</TestButton>);

    await userEvent.click(screen.getByRole('button'));

    expect(onClick).toHaveBeenCalledOnce();
  });

  it('disabled のときクリックしてもonClickが呼ばれない', async () => {
    const onClick = vi.fn();
    render(
      <TestButton onClick={onClick} disabled>
        クリック
      </TestButton>,
    );

    await userEvent.click(screen.getByRole('button'));

    expect(onClick).not.toHaveBeenCalled();
  });
});
