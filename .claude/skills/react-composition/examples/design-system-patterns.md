---
title: Design System Composition Examples
tags: examples, design-system, polymorphic, slot, controlled-uncontrolled
---

## Design System Composition Examples

Practical examples of composition patterns applied to design system components.

---

### Example 1: Polymorphic Text Component

A single Text component that renders as any heading or paragraph element.

```tsx
type TextProps<E extends React.ElementType = 'p'> = {
  as?: E
  size?: 'sm' | 'md' | 'lg' | 'xl'
  weight?: 'normal' | 'medium' | 'bold'
  children: React.ReactNode
} & Omit<React.ComponentPropsWithoutRef<E>, 'as' | 'size' | 'children'>

function Text<E extends React.ElementType = 'p'>({
  as,
  size = 'md',
  weight = 'normal',
  children,
  className,
  ...props
}: TextProps<E>) {
  const Component = as || 'p'
  return (
    <Component
      className={cn(
        styles.text,
        styles[`size-${size}`],
        styles[`weight-${weight}`],
        className,
      )}
      {...props}
    >
      {children}
    </Component>
  )
}
```

**Usage:**

```tsx
<Text>Default paragraph</Text>
<Text as="h1" size="xl" weight="bold">Page Title</Text>
<Text as="span" size="sm">Inline text</Text>
<Text as="label" htmlFor="email" size="sm" weight="medium">Email</Text>
```

TypeScript correctly infers `htmlFor` is available for `as="label"` but not
for `as="h1"`.

---

### Example 2: Dialog with Slot Trigger

A Dialog component where the trigger can be any element.

```tsx
import { Slot } from '@radix-ui/react-slot'

interface DialogTriggerProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  asChild?: boolean
}

function DialogTrigger({ asChild, ...props }: DialogTriggerProps) {
  const { open } = use(DialogContext)
  const Component = asChild ? Slot : 'button'
  return <Component onClick={open} {...props} />
}
```

**Usage:**

```tsx
// Default — renders a <button>
<Dialog>
  <Dialog.Trigger>Open Settings</Dialog.Trigger>
  <Dialog.Content>...</Dialog.Content>
</Dialog>

// asChild — renders the child element directly with Dialog behavior
<Dialog>
  <Dialog.Trigger asChild>
    <a href="#settings">Open Settings</a>
  </Dialog.Trigger>
  <Dialog.Content>...</Dialog.Content>
</Dialog>

// asChild with a custom component
<Dialog>
  <Dialog.Trigger asChild>
    <IconButton icon={<SettingsIcon />} label="Settings" />
  </Dialog.Trigger>
  <Dialog.Content>...</Dialog.Content>
</Dialog>
```

No wrapper elements. The trigger behavior is merged onto whatever child is
provided.

---

### Example 3: Controlled/Uncontrolled Tabs

Tabs that work out of the box but can also be controlled externally.

```tsx
interface TabsProps {
  value?: string
  onValueChange?: (value: string) => void
  defaultValue?: string
  children: React.ReactNode
}

function Tabs({ value, onValueChange, defaultValue, children }: TabsProps) {
  const [activeTab, setActiveTab] = useControllableState({
    value,
    defaultValue: defaultValue ?? '',
    onChange: onValueChange,
  })

  return (
    <TabsContext value={{ activeTab, setActiveTab }}>
      <div role="tablist">{children}</div>
    </TabsContext>
  )
}

function TabsTrigger({ value, children }: { value: string; children: React.ReactNode }) {
  const { activeTab, setActiveTab } = use(TabsContext)
  return (
    <button
      role="tab"
      aria-selected={activeTab === value}
      onClick={() => setActiveTab(value)}
    >
      {children}
    </button>
  )
}

function TabsContent({ value, children }: { value: string; children: React.ReactNode }) {
  const { activeTab } = use(TabsContext)
  if (activeTab !== value) return null
  return <div role="tabpanel">{children}</div>
}

const TabsCompound = {
  Root: Tabs,
  Trigger: TabsTrigger,
  Content: TabsContent,
}
```

**Uncontrolled — simple use case:**

```tsx
<TabsCompound.Root defaultValue="tab1">
  <TabsCompound.Trigger value="tab1">General</TabsCompound.Trigger>
  <TabsCompound.Trigger value="tab2">Security</TabsCompound.Trigger>

  <TabsCompound.Content value="tab1">
    <GeneralSettings />
  </TabsCompound.Content>
  <TabsCompound.Content value="tab2">
    <SecuritySettings />
  </TabsCompound.Content>
</TabsCompound.Root>
```

**Controlled — URL-synced tabs:**

```tsx
function SettingsPage() {
  const [searchParams, setSearchParams] = useSearchParams()
  const activeTab = searchParams.get('tab') ?? 'general'

  return (
    <TabsCompound.Root
      value={activeTab}
      onValueChange={(tab) => setSearchParams({ tab })}
    >
      <TabsCompound.Trigger value="general">General</TabsCompound.Trigger>
      <TabsCompound.Trigger value="security">Security</TabsCompound.Trigger>

      <TabsCompound.Content value="general">
        <GeneralSettings />
      </TabsCompound.Content>
      <TabsCompound.Content value="security">
        <SecuritySettings />
      </TabsCompound.Content>
    </TabsCompound.Root>
  )
}
```

Same component, but now the active tab is synced with the URL. No changes to
the Tabs implementation needed.

---

### Example 4: Combining All Patterns — Compound + Slot + Controlled

A complete Select component using compound components, slot pattern, and
controlled/uncontrolled state.

```tsx
interface SelectProps {
  value?: string
  onValueChange?: (value: string) => void
  defaultValue?: string
  children: React.ReactNode
}

function Select({ value, onValueChange, defaultValue, children }: SelectProps) {
  const [selected, setSelected] = useControllableState({
    value,
    defaultValue: defaultValue ?? '',
    onChange: onValueChange,
  })
  const [isOpen, setIsOpen] = useState(false)

  return (
    <SelectContext value={{ selected, setSelected, isOpen, setIsOpen }}>
      {children}
    </SelectContext>
  )
}

function SelectTrigger({ asChild, children, ...props }: TriggerProps) {
  const { isOpen, setIsOpen, selected } = use(SelectContext)
  const Component = asChild ? Slot : 'button'

  return (
    <Component
      aria-expanded={isOpen}
      onClick={() => setIsOpen(!isOpen)}
      {...props}
    >
      {children ?? selected}
    </Component>
  )
}

function SelectOption({ value, children }: OptionProps) {
  const { selected, setSelected, setIsOpen } = use(SelectContext)

  return (
    <div
      role="option"
      aria-selected={selected === value}
      onClick={() => {
        setSelected(value)
        setIsOpen(false)
      }}
    >
      {children}
    </div>
  )
}

const SelectCompound = {
  Root: Select,
  Trigger: SelectTrigger,
  Content: SelectContent,
  Option: SelectOption,
}
```

**Usage:**

```tsx
// Uncontrolled with default trigger
<SelectCompound.Root defaultValue="apple">
  <SelectCompound.Trigger />
  <SelectCompound.Content>
    <SelectCompound.Option value="apple">Apple</SelectCompound.Option>
    <SelectCompound.Option value="banana">Banana</SelectCompound.Option>
  </SelectCompound.Content>
</SelectCompound.Root>

// Controlled with custom trigger element
<SelectCompound.Root value={fruit} onValueChange={setFruit}>
  <SelectCompound.Trigger asChild>
    <Chip>{fruit}</Chip>
  </SelectCompound.Trigger>
  <SelectCompound.Content>
    <SelectCompound.Option value="apple">Apple</SelectCompound.Option>
    <SelectCompound.Option value="banana">Banana</SelectCompound.Option>
  </SelectCompound.Content>
</SelectCompound.Root>
```
