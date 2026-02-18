---
title: Polymorphic Components with the as Prop
impact: MEDIUM
impactDescription: enables a single component to render as different HTML elements or other components
tags: composition, polymorphic, as-prop, design-system, reusability
---

## Polymorphic Components with the `as` Prop

Allow a component to change its rendered element via an `as` prop. This avoids
duplicating styling and behavior logic across `ButtonLink`, `ButtonDiv`, etc.
Widely used in Chakra UI, styled-components, and other design systems.

**Incorrect (duplicate components for different elements):**

```tsx
function Button({ children, ...props }: ButtonProps) {
  return <button className="btn" {...props}>{children}</button>
}

function ButtonLink({ children, href, ...props }: ButtonLinkProps) {
  return <a className="btn" href={href} {...props}>{children}</a>
}

function ButtonDiv({ children, ...props }: ButtonDivProps) {
  return <div className="btn" role="button" tabIndex={0} {...props}>{children}</div>
}
```

Three components with identical styling. Every style change must be applied
three times.

**Correct (polymorphic component with `as` prop):**

```tsx
type PolymorphicProps<E extends React.ElementType> = {
  as?: E
  children: React.ReactNode
} & Omit<React.ComponentPropsWithoutRef<E>, 'as' | 'children'>

function Button<E extends React.ElementType = 'button'>({
  as,
  children,
  ...props
}: PolymorphicProps<E>) {
  const Component = as || 'button'
  return (
    <Component className="btn" {...props}>
      {children}
    </Component>
  )
}
```

**Usage:**

```tsx
// Renders <button>
<Button onClick={handleClick}>Click me</Button>

// Renders <a> with href type-checked
<Button as="a" href="/about">About</Button>

// Renders a Next.js Link
<Button as={Link} href="/dashboard">Dashboard</Button>
```

TypeScript infers the correct props for the chosen element. `href` is available
when `as="a"` but not when `as="button"`.

**When to use:**

- Design system primitives (Box, Text, Heading, Button)
- Components that may render as different semantic elements
- Wrapping third-party link components (Next.js Link, React Router Link)

**When NOT to use:**

- When variants have significantly different behavior (use explicit variants
  instead — see `patterns-explicit-variants.md`)
- When the component only ever renders as one element type
