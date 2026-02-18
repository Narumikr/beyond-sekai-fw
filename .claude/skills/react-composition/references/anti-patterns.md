---
title: Composition Anti-Patterns
impact: HIGH
impactDescription: common mistakes that undermine component extensibility and reusability
tags: anti-patterns, composition, architecture
---

## Composition Anti-Patterns

Common patterns that seem convenient but undermine extensibility and reusability.

### 1. Boolean Prop Accumulation

**Problem**: Adding a boolean prop for every new feature or variant.

```tsx
// Each new feature adds another boolean
<Modal
  isFullScreen
  isClosable
  isDraggable
  hasOverlay
  isAnimated
  isNested
/>
```

**Solution**: Use compound components or explicit variants.

```tsx
<FullScreenModal>
  <Modal.Overlay />
  <Modal.Content draggable>
    <Modal.CloseButton />
    {children}
  </Modal.Content>
</FullScreenModal>
```

### 2. Prop Drilling Through Multiple Layers

**Problem**: Passing props through components that don't use them.

```tsx
function App() {
  return <Layout user={user} theme={theme} locale={locale}>
    <Sidebar user={user} theme={theme}>
      <Navigation user={user} theme={theme} locale={locale}>
        <NavItem user={user} />
      </Navigation>
    </Sidebar>
  </Layout>
}
```

**Solution**: Use context providers at the appropriate level.

```tsx
function App() {
  return (
    <UserProvider user={user}>
      <ThemeProvider theme={theme}>
        <Layout>
          <Sidebar>
            <Navigation>
              <NavItem />
            </Navigation>
          </Sidebar>
        </Layout>
      </ThemeProvider>
    </UserProvider>
  )
}
```

### 3. useEffect for State Syncing

**Problem**: Using useEffect to sync child state to parent.

```tsx
function Parent() {
  const [childValue, setChildValue] = useState('')
  return (
    <>
      <ChildInput onValueChange={setChildValue} />
      <Preview value={childValue} />
    </>
  )
}

function ChildInput({ onValueChange }) {
  const [value, setValue] = useState('')
  useEffect(() => {
    onValueChange(value) // Double render, potential infinite loops
  }, [value])
  return <input value={value} onChange={(e) => setValue(e.target.value)} />
}
```

**Solution**: Lift state to a provider so both components read from the same source.

```tsx
function InputProvider({ children }) {
  const [value, setValue] = useState('')
  return (
    <InputContext value={{ value, setValue }}>
      {children}
    </InputContext>
  )
}

function Parent() {
  return (
    <InputProvider>
      <ChildInput />
      <Preview />
    </InputProvider>
  )
}
```

### 4. God Components

**Problem**: One component that does everything, with hundreds of lines and
dozens of conditional branches.

```tsx
function Dashboard({ user, settings, data, filters, ... }) {
  // 500+ lines of hooks, state, effects, and conditional rendering
}
```

**Solution**: Break into compound components, each with a focused responsibility.

### 5. Tight Coupling to State Libraries

**Problem**: UI components directly import and depend on specific state
management hooks (Zustand, Redux, etc.).

```tsx
function TodoList() {
  const todos = useTodoStore((state) => state.todos)  // Coupled to Zustand
  const addTodo = useTodoStore((state) => state.addTodo)
  // ...
}
```

**Solution**: Define a context interface and inject state through providers.
The UI only knows about `{ state, actions, meta }`.

### 6. Excessive Nesting of Render Props

**Problem**: Multiple render props create "callback hell" in JSX.

```tsx
<DataProvider render={(data) => (
  <ThemeConsumer render={(theme) => (
    <LocaleConsumer render={(locale) => (
      <Component data={data} theme={theme} locale={locale} />
    )} />
  )} />
)} />
```

**Solution**: Use compound components with context, or compose with children.

```tsx
<DataProvider>
  <ThemeProvider>
    <LocaleProvider>
      <Component />
    </LocaleProvider>
  </ThemeProvider>
</DataProvider>
```
