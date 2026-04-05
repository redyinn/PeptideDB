# PeptideDB Design System

## Core Identity

PeptideDB is a **scientific research database** for peptide therapeutics. The design philosophy bridges **clinical precision** with **premium dark-mode aesthetics** — the interface should feel like a high-end medical research platform, not a consumer health app.

Design principle: *"Every element earns its place. Data is the hero."*

---

## Color Palette

### Dark Mode (Default)

| Token | HSL | Hex (approx) | Usage |
|-------|-----|--------------|-------|
| `--background` | `222 47% 6%` | `#090d17` | Page background |
| `--card` | `222 47% 6%` | `#090d17` | Card surfaces |
| `--popover` | `222 47% 9%` | `#0e1420` | Dropdowns, tooltips |
| `--secondary` | `222 30% 14%` | `#1a2035` | Elevated surfaces |
| `--border` | `222 20% 18%` | `#242c3d` | Subtle dividers |
| `--muted` | `222 30% 14%` | `#1a2035` | Disabled backgrounds |
| `--muted-foreground` | `215 16% 57%` | `#808ea8` | Secondary text, captions |
| `--foreground` | `210 40% 96%` | `#eef2f9` | Primary text |
| `--primary` | `173 58% 39%` | `#28a08a` | Teal — primary actions, links, focus |
| `--primary-foreground` | `0 0% 100%` | `#ffffff` | Text on primary |
| `--accent` | `173 40% 14%` | `#112926` | Teal tint backgrounds |
| `--accent-foreground` | `173 58% 70%` | `#72d4c4` | Teal text on dark |
| `--destructive` | `0 62% 50%` | `#d43a3a` | Errors, warnings |
| `--ring` | `173 58% 39%` | `#28a08a` | Focus rings |

### Light Mode

| Token | HSL | Usage |
|-------|-----|-------|
| `--background` | `210 40% 98%` | Near-white canvas |
| `--foreground` | `222 47% 11%` | Deep navy text |
| `--primary` | `173 78% 26%` | Deeper teal |
| `--accent` | `173 55% 92%` | Pale teal tint |

### Semantic Colors (Extend as needed)

```css
--color-success: hsl(142 70% 45%);   /* green — FDA approved, safe */
--color-warning: hsl(38 92% 50%);    /* amber — caution, Phase 2 */
--color-info: hsl(210 80% 56%);      /* blue — informational */
--color-research: hsl(270 60% 60%);  /* purple — research/experimental */
```

---

## Typography

### Font Stack

| Role | Font | Fallback |
|------|------|---------|
| **Headings** | Space Grotesk | ui-sans-serif, system-ui |
| **Body / UI** | IBM Plex Sans | ui-sans-serif |
| **Code / Sequences** | IBM Plex Mono | ui-monospace, SFMono-Regular |

### Scale

| Step | Size | Weight | Usage |
|------|------|--------|-------|
| Display | 48–64px | 700 | Hero headlines |
| H1 | 36px | 700 | Page titles |
| H2 | 28px | 600 | Section headings |
| H3 | 22px | 600 | Card titles, tab labels |
| H4 | 18px | 600 | Sub-sections |
| Body | 16px | 400 | Default text |
| Small | 14px | 400 | Metadata, captions |
| Micro | 12px | 500 | Badges, labels, tags |
| Mono | 13px | 400 | Amino acid sequences, code |

### Rules
- Headings use Space Grotesk exclusively
- Never use font-weight 300 for body text on dark backgrounds — contrast suffers
- Amino acid sequences always render in IBM Plex Mono with letter-spacing: 0.05em
- Line height: 1.6 for body, 1.2 for headings, 1.0 for data-dense tables

---

## Spacing

Base unit: **4px**

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 4px | Icon gaps, tight inline spacing |
| `sm` | 8px | Component internal padding |
| `md` | 16px | Default padding, card internals |
| `lg` | 24px | Section internal spacing |
| `xl` | 32px | Between components |
| `2xl` | 48px | Section separation |
| `3xl` | 64px | Major section breaks |
| `4xl` | 96px | Hero padding |

---

## Border Radius

```css
--radius: 0.75rem;  /* 12px — default */

sm:  calc(var(--radius) - 4px)  /* 8px  — inputs, tags */
md:  calc(var(--radius) - 2px)  /* 10px — buttons */
lg:  var(--radius)              /* 12px — cards, modals */
xl:  1.5rem                     /* 24px — feature cards */
full: 9999px                    /* pills, badges */
```

---

## Components

### Cards

```css
background: hsl(var(--card));
border: 1px solid hsl(var(--border));
border-radius: var(--radius);
padding: 24px;
/* Hover state */
border-color: hsl(var(--primary) / 0.4);
box-shadow: 0 0 0 1px hsl(var(--primary) / 0.15);
transition: all 0.2s ease;
```

Cards never use heavy box-shadows. Depth is communicated through border brightness, not elevation.

### Peptide Cards (Encyclopedia)

- Status badge (top-right): pill shape, semantic color per phase
  - `Phase 3+` → green
  - `Phase 1-2` → amber  
  - `Preclinical / Research` → purple
  - `FDA Approved` → teal (primary)
- Category badge: bottom of card, muted background
- Hover: primary border tint + subtle teal glow `box-shadow: 0 0 16px hsl(173 58% 39% / 0.12)`

### Buttons

**Primary:**
```css
background: hsl(var(--primary));
color: hsl(var(--primary-foreground));
border-radius: calc(var(--radius) - 2px);
padding: 10px 20px;
font-weight: 500;
font-size: 14px;
/* Hover: */
background: hsl(var(--primary) / 0.9);
box-shadow: 0 0 12px hsl(var(--primary) / 0.3);
```

**Secondary:**
```css
background: hsl(var(--secondary));
border: 1px solid hsl(var(--border));
color: hsl(var(--foreground));
```

**Ghost:** No background, no border. Text color = primary on hover.

**Destructive:** Use sparingly. Only for irreversible actions.

### Badges / Phase Labels

```
FDA Approved  → bg: accent, text: accent-foreground (teal)
Phase 3       → bg: green/10, text: green-400, border: green/20
Phase 2       → bg: amber/10, text: amber-400, border: amber/20
Phase 1       → bg: orange/10, text: orange-400
Preclinical   → bg: purple/10, text: purple-400
Research      → bg: muted, text: muted-foreground
```

Font: IBM Plex Mono, 11px, font-weight 500, letter-spacing 0.05em

### Tabs (Peptide Detail)

- Active tab: `border-bottom: 2px solid hsl(var(--primary))`, text = primary color
- Inactive: text = muted-foreground
- No background fills on tabs — underline only
- Tab strip: `border-bottom: 1px solid hsl(var(--border))`

### Search Input

```css
background: hsl(var(--secondary));
border: 1px solid hsl(var(--border));
border-radius: var(--radius);
padding: 12px 16px 12px 44px; /* left padding for icon */
font-family: IBM Plex Sans;
font-size: 16px;
/* Focus: */
border-color: hsl(var(--primary));
box-shadow: 0 0 0 3px hsl(var(--primary) / 0.15);
outline: none;
```

### Medical Disclaimer Banner

```css
background: hsl(38 92% 50% / 0.08);
border: 1px solid hsl(38 92% 50% / 0.25);
border-radius: var(--radius);
padding: 12px 16px;
/* Icon: ⚠️ or info circle in amber */
font-size: 13px;
color: hsl(38 92% 65%);
```

Required on: PeptideDetailPage (dosage tab), ComparePage (dosage section), any page showing administration info.

### Evidence Level Badges

For clinical studies and papers:

```
Level A (RCT, Meta-analysis)  → solid green badge
Level B (Cohort, Case-control) → outlined blue badge  
Level C (Case reports, Expert) → outlined gray badge
In Vitro / Animal             → outlined purple badge
```

---

## Iconography

Library: **Lucide React** (already in use via shadcn/ui)

Rules:
- Default icon size: 16px for inline, 20px for standalone
- Stroke width: 1.5px default, 2px for emphasis
- Never use filled icons except for active/selected states
- Icon color follows text color context — never hard-code colors

---

## Layout & Grid

### Container

```css
max-width: 1280px;
margin: 0 auto;
padding: 0 24px; /* mobile */
padding: 0 48px; /* tablet+ */
```

### Page Structure

```
<Navbar>           — fixed, 64px height, backdrop-blur
<main>
  <Hero>           — 680px min-height
  <Section>        — 64–96px vertical padding
  ...
</main>
<Footer>
```

### Grid Patterns

- **Cards grid**: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` with `gap-6`
- **Stats row**: `grid-cols-2 sm:grid-cols-4` with `gap-4`
- **Compare**: `grid-cols-1 md:grid-cols-3` with sticky first column on mobile
- **Detail tabs**: full-width content area, max-width 860px centered

---

## Animation

Library: **Framer Motion**

| Interaction | Duration | Easing |
|------------|----------|--------|
| Page enter | 400ms | `easeOut` |
| Card hover | 150ms | `ease` |
| Dropdown open | 200ms | `easeOut` |
| Spotlight | 2000ms | `ease` delay 750ms |
| Lamp glow | 600ms | spring |
| Toast/notification | 300ms | `easeInOut` |

Rules:
- Never animate layout properties (width, height) — use transform/opacity
- `will-change: transform` only on elements that animate every frame (shader background)
- Reduced-motion: all animations → instant at `prefers-reduced-motion: reduce`

---

## Hero Section

Three-layer stack (bottom to top):

1. **WebGL Aurora shader** — `z-index: 0`, fills container, `alpha: true` renderer
2. **Dark overlay** — `bg-black/50 z-10` — ensures text readability
3. **Lamp component** — `z-20 bg-transparent` — cyan conic gradient glow from top
4. **Content** — `z-30` — title, search, CTAs

Lamp glow color: `hsl(173 58% 39%)` (primary teal) not cyan — keeps consistency with brand.

---

## Data Visualization

For dosage ranges, molecular weights, and research timelines:

- Use horizontal bar indicators (not pie charts)
- Research phase progress: linear stepped indicator (Phase 1 → 2 → 3 → Approved)
- Severity indicators (side effects): dot scale 1–5, color: green → yellow → red
- Half-life comparison: horizontal bar, teal fill

---

## Voice & Tone (Content)

| Context | Tone |
|---------|------|
| Page headings | Precise, clinical ("Mechanism of Action") |
| Descriptions | Informative, neutral — no hype language |
| Dosage notes | Always include "research purposes only" qualifier |
| Error states | Direct and actionable ("No peptides found. Try a broader search.") |
| Empty states | Helpful, not apologetic |
| Badges/labels | Abbreviated, uppercase caps for phase labels (e.g. "PHASE 3") |

---

## Accessibility

- Color contrast: minimum 4.5:1 for body text, 3:1 for large text
- Focus rings: `box-shadow: 0 0 0 3px hsl(var(--ring) / 0.5)` — never remove outline
- All icons that convey meaning need `aria-label`
- Amino acid sequences: wrap in `<code>` with `aria-label="Amino acid sequence"`
- Medical disclaimers: `role="note"` or `role="alert"` where appropriate

---

## Medical Disclaimer (Required)

This text must appear on all peptide detail pages:

> *"The information on this page is intended for research and educational purposes only. It does not constitute medical advice and should not be used as a basis for clinical decisions. Consult a qualified healthcare professional before using any peptide therapeutics."*

---

## What This Design System Is Not

- Not a consumer wellness app — no gamification, no streak counters, no achievement badges
- Not a pharma marketing site — no promotional language, no "revolutionary breakthrough" copy
- Not a social platform — no user-generated content patterns, no feed UX
