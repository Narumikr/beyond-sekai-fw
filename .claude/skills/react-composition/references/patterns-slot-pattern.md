---
title: Slot Pattern for Flexible Content Injection
impact: MEDIUM
impactDescription: enables type-safe content injection without render props or boolean flags
tags: composition, slot, design-system, reusability, radix
---

## Slot Pattern for Flexible Content Injection

The Slot pattern lets a component merge its props onto whatever child is passed
to it, instead of rendering a fixed wrapper element. The consumer controls the
rendered element while the component provides behavior and styling. Popularized
by Radix UI's `Slot` / `asChild` pattern.

**Incorrect (wrapper div forces extra DOM nesting):**

```tsx
function Tooltip({ children, content }: TooltipProps) {
  return (
    <div className="tooltip-trigger" onMouseEnter={show} onMouseLeave={hide}>
      {children}
      {isOpen && <div className="tooltip">{content}</div>}
    </div>
  )
}

// Consumer — unwanted wrapper div in the DOM
<Tooltip content="Settings">
  <button>⚙️</button>
</Tooltip>
// Renders: <div class="tooltip-trigger"><button>⚙️</button></div>
```

**Correct (Slot merges props onto the child):**

```tsx
import { Slot } from '@radix-ui/react-slot'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  asChild?: boolean
}

function Button({ asChild, ...props }: ButtonProps) {
  const Component = asChild ? Slot : 'button'
  return <Component className="btn" {...props} />
}
```

**Usage:**

```tsx
// Renders a <button>
<Button onClick={handleClick}>Save</Button>

// Renders a <a> — Slot merges Button's props onto the anchor
<Button asChild>
  <a href="/home">Home</a>
</Button>
// Renders: <a class="btn" href="/home">Home</a>

// Renders a Next.js Link with Button styling
<Button asChild>
  <Link href="/dashboard">Dashboard</Link>
</Button>
```

No extra wrapper element. The child receives the component's className, event
handlers, and other props via merging.

**Implementing a minimal Slot without Radix:**

```tsx
import { cloneElement, isValidElement, Children } from 'react'

function Slot({
  children,
  ...props
}: React.HTMLAttributes<HTMLElement> & { children: React.ReactNode }) {
  if (isValidElement(children)) {
    return cloneElement(children, {
      ...props,
      ...children.props,
      className: cn(props.className, children.props.className),
    })
  }
  return null
}
```

**When to use:**

- Design system components that should not enforce a DOM element
- Trigger components (tooltip triggers, popover triggers, dialog triggers)
- When avoiding extra wrapper elements matters for styling or accessibility

**When NOT to use:**

- When the component must control its own element for accessibility
  (e.g., dialog panels that require specific ARIA roles)
- When multiple children need to be wrapped — Slot works with a single child
