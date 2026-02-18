---
title: Before/After Composition Examples
tags: examples, composition, refactoring
---

## Before/After Composition Examples

Practical examples of refactoring components from anti-patterns to composition patterns.

---

### Example 1: Monolithic Component to Compound Components

**Before** -- A single component with boolean props and conditional rendering:

```tsx
function NotificationCard({
  type,
  isRead,
  isDismissible,
  showAvatar,
  showTimestamp,
  showActions,
  onDismiss,
  onMarkRead,
  notification,
}: Props) {
  return (
    <div className={cn('card', { unread: !isRead })}>
      {showAvatar && <Avatar user={notification.sender} />}
      <div>
        <p>{notification.message}</p>
        {showTimestamp && <time>{notification.createdAt}</time>}
      </div>
      {showActions && (
        <div>
          {!isRead && <button onClick={onMarkRead}>Mark read</button>}
          {isDismissible && <button onClick={onDismiss}>Dismiss</button>}
        </div>
      )}
    </div>
  )
}
```

**After** -- Compound components with explicit composition:

```tsx
const NotificationContext = createContext<NotificationContextValue | null>(null)

function NotificationProvider({ notification, children }: ProviderProps) {
  const { markRead, dismiss } = useNotificationActions(notification.id)

  return (
    <NotificationContext value={{
      state: { notification, isRead: notification.isRead },
      actions: { markRead, dismiss },
    }}>
      {children}
    </NotificationContext>
  )
}

function NotificationCard({ children }: { children: React.ReactNode }) {
  const { state } = use(NotificationContext)
  return <div className={cn('card', { unread: !state.isRead })}>{children}</div>
}

function NotificationAvatar() {
  const { state } = use(NotificationContext)
  return <Avatar user={state.notification.sender} />
}

function NotificationMessage() {
  const { state } = use(NotificationContext)
  return <p>{state.notification.message}</p>
}

function NotificationTimestamp() {
  const { state } = use(NotificationContext)
  return <time>{state.notification.createdAt}</time>
}

function NotificationMarkRead() {
  const { state, actions } = use(NotificationContext)
  if (state.isRead) return null
  return <button onClick={actions.markRead}>Mark read</button>
}

function NotificationDismiss() {
  const { actions } = use(NotificationContext)
  return <button onClick={actions.dismiss}>Dismiss</button>
}

const Notification = {
  Provider: NotificationProvider,
  Card: NotificationCard,
  Avatar: NotificationAvatar,
  Message: NotificationMessage,
  Timestamp: NotificationTimestamp,
  MarkRead: NotificationMarkRead,
  Dismiss: NotificationDismiss,
}
```

**Usage -- each variant composes exactly what it needs:**

```tsx
// Full notification with all features
function DetailedNotification({ notification }) {
  return (
    <Notification.Provider notification={notification}>
      <Notification.Card>
        <Notification.Avatar />
        <div>
          <Notification.Message />
          <Notification.Timestamp />
        </div>
        <div>
          <Notification.MarkRead />
          <Notification.Dismiss />
        </div>
      </Notification.Card>
    </Notification.Provider>
  )
}

// Minimal notification -- no avatar, no actions
function MinimalNotification({ notification }) {
  return (
    <Notification.Provider notification={notification}>
      <Notification.Card>
        <Notification.Message />
      </Notification.Card>
    </Notification.Provider>
  )
}
```

---

### Example 2: Prop Drilling to Provider-Based State

**Before** -- Props passed through multiple levels:

```tsx
function SearchPage({ query, results, filters, onSearch, onFilter, onSort }) {
  return (
    <div>
      <SearchBar query={query} onSearch={onSearch} />
      <FilterPanel filters={filters} onFilter={onFilter} />
      <ResultsList results={results} query={query} onSort={onSort} />
      <ResultsCount results={results} filters={filters} />
    </div>
  )
}
```

**After** -- State lifted to provider:

```tsx
interface SearchState {
  query: string
  results: Result[]
  filters: Filter[]
}

interface SearchActions {
  search: (query: string) => void
  filter: (filters: Filter[]) => void
  sort: (field: string, direction: 'asc' | 'desc') => void
}

const SearchContext = createContext<{
  state: SearchState
  actions: SearchActions
} | null>(null)

function SearchProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(searchReducer, initialState)
  const actions = useMemo(() => ({
    search: (query: string) => dispatch({ type: 'SEARCH', query }),
    filter: (filters: Filter[]) => dispatch({ type: 'FILTER', filters }),
    sort: (field: string, direction: 'asc' | 'desc') =>
      dispatch({ type: 'SORT', field, direction }),
  }), [])

  return (
    <SearchContext value={{ state, actions }}>
      {children}
    </SearchContext>
  )
}

// Each component reads only what it needs from context
function SearchBar() {
  const { state, actions } = use(SearchContext)
  return <input value={state.query} onChange={(e) => actions.search(e.target.value)} />
}

function ResultsCount() {
  const { state } = use(SearchContext)
  return <span>{state.results.length} results for "{state.query}"</span>
}

// Usage
function SearchPage() {
  return (
    <SearchProvider>
      <SearchBar />
      <FilterPanel />
      <ResultsList />
      <ResultsCount />
    </SearchProvider>
  )
}
```

---

### Example 3: Render Props to Children Composition

**Before** -- Render props create awkward nesting:

```tsx
<Card
  renderHeader={() => <h2>Title</h2>}
  renderBody={() => (
    <div>
      <p>Content</p>
      <img src="image.png" />
    </div>
  )}
  renderFooter={() => (
    <div>
      <Button>Cancel</Button>
      <Button variant="primary">Save</Button>
    </div>
  )}
/>
```

**After** -- Children composition is natural and flexible:

```tsx
<Card>
  <Card.Header>
    <h2>Title</h2>
  </Card.Header>
  <Card.Body>
    <p>Content</p>
    <img src="image.png" />
  </Card.Body>
  <Card.Footer>
    <Button>Cancel</Button>
    <Button variant="primary">Save</Button>
  </Card.Footer>
</Card>
```

---

### Example 4: Swappable Providers (Dependency Injection)

**Same UI, different state sources:**

```tsx
// Provider A: REST API backend
function RestSearchProvider({ children }) {
  const { data, search } = useRestSearch()
  return (
    <SearchContext value={{ state: data, actions: { search } }}>
      {children}
    </SearchContext>
  )
}

// Provider B: GraphQL backend
function GraphQLSearchProvider({ children }) {
  const { data, search } = useGraphQLSearch()
  return (
    <SearchContext value={{ state: data, actions: { search } }}>
      {children}
    </SearchContext>
  )
}

// Provider C: Mock data for tests/storybook
function MockSearchProvider({ children, mockData }) {
  const [state, setState] = useState(mockData)
  return (
    <SearchContext value={{
      state,
      actions: { search: (q) => setState({ ...state, query: q }) },
    }}>
      {children}
    </SearchContext>
  )
}

// Same UI works with all three
function SearchPage() {
  return (
    <>
      <SearchBar />
      <ResultsList />
    </>
  )
}

// Production
<RestSearchProvider><SearchPage /></RestSearchProvider>

// Storybook
<MockSearchProvider mockData={fixtures}><SearchPage /></MockSearchProvider>
```
