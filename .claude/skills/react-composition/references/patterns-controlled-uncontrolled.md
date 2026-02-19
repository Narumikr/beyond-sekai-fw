---
title: Controlled and Uncontrolled Component Pattern
impact: MEDIUM
impactDescription: enables components to work both as controlled and uncontrolled for maximum reusability
tags: composition, controlled, uncontrolled, state, reusability
---

## Controlled and Uncontrolled Component Pattern

Build components that work in both controlled mode (parent owns state) and
uncontrolled mode (component owns state). This maximizes reusability — simple
use-cases work out of the box, while complex use-cases can take full control.

Used extensively in Radix UI, Headless UI, and React Aria.

**Incorrect (controlled only — forces all consumers to manage state):**

```tsx
function Accordion({
  openItems,
  onOpenItemsChange,
  children,
}: {
  openItems: string[]
  onOpenItemsChange: (items: string[]) => void
  children: React.ReactNode
}) {
  // Every consumer MUST provide state, even for simple use-cases
  return (...)
}

// Simple use-case still requires full state management
function FAQ() {
  const [openItems, setOpenItems] = useState<string[]>([])
  return (
    <Accordion openItems={openItems} onOpenItemsChange={setOpenItems}>
      <Accordion.Item id="q1">...</Accordion.Item>
    </Accordion>
  )
}
```

**Correct (supports both controlled and uncontrolled):**

```tsx
function useControllableState<T>({
  value,
  defaultValue,
  onChange,
}: {
  value?: T
  defaultValue: T
  onChange?: (value: T) => void
}) {
  const [internalValue, setInternalValue] = useState(defaultValue)
  const isControlled = value !== undefined
  const currentValue = isControlled ? value : internalValue

  const setValue = useCallback(
    (next: T | ((prev: T) => T)) => {
      const nextValue = typeof next === 'function'
        ? (next as (prev: T) => T)(currentValue)
        : next

      if (!isControlled) {
        setInternalValue(nextValue)
      }
      onChange?.(nextValue)
    },
    [isControlled, currentValue, onChange],
  )

  return [currentValue, setValue] as const
}
```

**Usage in a component:**

```tsx
interface AccordionProps {
  // Controlled mode
  value?: string[]
  onValueChange?: (value: string[]) => void
  // Uncontrolled mode
  defaultValue?: string[]
  children: React.ReactNode
}

function Accordion({
  value,
  onValueChange,
  defaultValue = [],
  children,
}: AccordionProps) {
  const [openItems, setOpenItems] = useControllableState({
    value,
    defaultValue,
    onChange: onValueChange,
  })

  return (
    <AccordionContext value={{ openItems, setOpenItems }}>
      {children}
    </AccordionContext>
  )
}
```

**Consumer usage:**

```tsx
// Uncontrolled — works out of the box, no state management needed
<Accordion defaultValue={['q1']}>
  <Accordion.Item id="q1">...</Accordion.Item>
  <Accordion.Item id="q2">...</Accordion.Item>
</Accordion>

// Controlled — parent owns state for complex use-cases
function FilterableAccordion() {
  const [openItems, setOpenItems] = useState<string[]>([])

  return (
    <>
      <button onClick={() => setOpenItems([])}>Collapse All</button>
      <Accordion value={openItems} onValueChange={setOpenItems}>
        <Accordion.Item id="q1">...</Accordion.Item>
        <Accordion.Item id="q2">...</Accordion.Item>
      </Accordion>
    </>
  )
}
```

**API convention:**

| Mode         | Props                           |
| ------------ | ------------------------------- |
| Uncontrolled | `defaultValue`, callbacks       |
| Controlled   | `value` + `onValueChange`       |

When `value` is provided, the component is controlled. When only `defaultValue`
is provided (or neither), the component manages its own state.

**When to use:**

- Reusable UI components that may be used in both simple and complex contexts
- Design system components (Accordion, Tabs, Select, Dialog open state)
- Any component where some consumers need state control and others don't

**When NOT to use:**

- Application-specific components where the state ownership is always clear
- Components that always require external state (e.g., form inputs bound to
  form libraries)
