{
  "brand": {
    "name": "Peptide Research (DE/EN)",
    "attributes": [
      "premium",
      "clinical-trustworthy",
      "scientific-but-approachable",
      "light-clean",
      "data-dense-yet-calm"
    ],
    "visual_metaphor": "Glass lab instruments + calm ocean-teal accents + precise editorial typography + subtle molecule field animation"
  },
  "design_personality": {
    "north_star": "Feels like a €10k+ biotech product: quiet confidence, immaculate spacing, crisp tables, and subtle motion that suggests ‘live research’.",
    "style_fusion": [
      "Swiss/International Typographic Style (grid, hierarchy, whitespace)",
      "Soft glassmorphism (frosted surfaces for filters/nav)",
      "Bento grid (home highlights + quick stats)",
      "Scientific motion layer (molecule/particle field behind hero only)"
    ],
    "anti_patterns": [
      "No purple.",
      "No loud gradients or gradient-heavy pages.",
      "No centered-everything landing page.",
      "No ‘AI-looking’ generic blobs; use restrained geometry + grain.",
      "Avoid dense paragraphs; use sections, bullets, and definition lists."
    ]
  },
  "typography": {
    "font_pairing": {
      "headings": {
        "family": "Space Grotesk",
        "fallback": "ui-sans-serif, system-ui",
        "usage": "H1/H2, navigation, KPI numbers",
        "weights": ["500", "600"]
      },
      "body": {
        "family": "IBM Plex Sans",
        "fallback": "ui-sans-serif, system-ui",
        "usage": "paragraphs, tables, metadata",
        "weights": ["400", "500"]
      },
      "mono": {
        "family": "IBM Plex Mono",
        "fallback": "ui-monospace, SFMono-Regular",
        "usage": "peptide sequences, IDs (NCT numbers), dosage units",
        "weights": ["400", "500"]
      },
      "implementation_note": "Load via Google Fonts in public/index.html (CRA) or in CSS @import. Keep to 2–3 weights total for performance."
    },
    "scale": {
      "h1": "text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight",
      "h2": "text-base md:text-lg font-medium text-muted-foreground",
      "section_title": "text-xl md:text-2xl font-semibold tracking-tight",
      "card_title": "text-base font-semibold",
      "body": "text-sm md:text-base leading-7",
      "small": "text-xs text-muted-foreground"
    },
    "content_rules": {
      "max_line_length": "~72ch for reading blocks",
      "numbers": "Use tabular-nums for tables/KPIs (Tailwind: tabular-nums)",
      "bilingual": "All user-facing strings must be sourced from i18n dictionary; never hardcode English-only labels."
    }
  },
  "color_system": {
    "notes": [
      "Light theme base; dark mode optional later.",
      "No purple anywhere.",
      "Use teal/sage as accents; keep most surfaces neutral for premium feel.",
      "Gradients only as subtle hero background overlays (<=20% viewport)."
    ],
    "palette": {
      "ink": "#0B1220",
      "ink_muted": "#334155",
      "bg": "#F7FAFC",
      "surface": "#FFFFFF",
      "surface_2": "#F1F5F9",
      "border": "#E2E8F0",
      "primary_teal": "#0F766E",
      "primary_teal_soft": "#99F6E4",
      "sage": "#86A789",
      "sand": "#F3EFE7",
      "info": "#2563EB",
      "success": "#16A34A",
      "warning": "#D97706",
      "danger": "#DC2626"
    },
    "design_tokens_css": {
      "file": "/app/frontend/src/index.css",
      "instructions": [
        "Replace current :root tokens with the HSL equivalents below (keep shadcn token names).",
        "Keep --radius slightly larger for premium feel (0.75rem).",
        "Add custom tokens for glass + noise."
      ],
      "tokens": {
        "--background": "210 40% 98%",
        "--foreground": "222 47% 11%",
        "--card": "0 0% 100%",
        "--card-foreground": "222 47% 11%",
        "--popover": "0 0% 100%",
        "--popover-foreground": "222 47% 11%",
        "--primary": "173 78% 26%",
        "--primary-foreground": "0 0% 100%",
        "--secondary": "210 40% 96%",
        "--secondary-foreground": "222 47% 11%",
        "--muted": "210 40% 96%",
        "--muted-foreground": "215 16% 35%",
        "--accent": "173 55% 92%",
        "--accent-foreground": "173 78% 18%",
        "--destructive": "0 72% 51%",
        "--destructive-foreground": "0 0% 100%",
        "--border": "214 32% 91%",
        "--input": "214 32% 91%",
        "--ring": "173 78% 26%",
        "--radius": "0.75rem",
        "--glass-bg": "rgba(255,255,255,0.72)",
        "--glass-border": "rgba(15,118,110,0.14)",
        "--shadow-elev-1": "0 1px 2px rgba(2,6,23,0.06)",
        "--shadow-elev-2": "0 12px 30px rgba(2,6,23,0.10)",
        "--noise-opacity": "0.06"
      }
    },
    "allowed_gradients": {
      "hero_overlay_only": [
        "radial-gradient(900px circle at 20% 10%, rgba(153,246,228,0.55), transparent 55%)",
        "radial-gradient(700px circle at 80% 0%, rgba(37,99,235,0.10), transparent 60%)",
        "linear-gradient(180deg, rgba(247,250,252,0.0), rgba(247,250,252,1))"
      ],
      "restriction": "Must not exceed 20% viewport; never on cards/tables; never on small UI elements (<100px)."
    }
  },
  "layout_and_grid": {
    "container": "max-w-6xl xl:max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
    "page_structure": [
      "Sticky top navigation (glass)",
      "Hero (search + quick stats) with subtle animated background",
      "Content sections on solid surfaces",
      "Footer with regulatory/disclaimer links"
    ],
    "grid_rules": {
      "home_bento": "grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-6",
      "cards": "Use 16–24px padding; avoid cramped layouts; prefer gap-6 on desktop.",
      "reading_blocks": "Use max-w-[72ch] and left alignment."
    },
    "responsive": {
      "mobile_first": "All pages must work at 360px width; filters collapse into Drawer/Sheet.",
      "tables": "On mobile, switch to stacked cards or horizontal ScrollArea with sticky first column."
    }
  },
  "components": {
    "component_path": {
      "shadcn_primary": "/app/frontend/src/components/ui/",
      "use_only_note": "Use these shadcn components instead of raw HTML for dropdowns, dialogs, calendars, etc."
    },
    "navigation": {
      "use": ["navigation-menu.jsx", "sheet.jsx", "dropdown-menu.jsx", "button.jsx"],
      "spec": {
        "desktop": "NavigationMenu with 5 items: Encyclopedia, Studies, Papers, News, About. Right side: Language toggle + Search icon.",
        "mobile": "Hamburger opens Sheet with same nav + language toggle.",
        "style": "Glass bar: bg-[var(--glass-bg)] backdrop-blur-md border border-[var(--glass-border)] shadow-[var(--shadow-elev-1)] rounded-xl"
      },
      "testids": {
        "lang_toggle": "data-testid=\"language-toggle\"",
        "global_search_open": "data-testid=\"global-search-open\"",
        "mobile_nav_open": "data-testid=\"mobile-nav-open\""
      }
    },
    "search": {
      "use": ["command.jsx", "input.jsx", "dialog.jsx", "badge.jsx"],
      "spec": {
        "hero_search": "Large Input with left icon + hint text; on Enter navigates to encyclopedia results.",
        "global_search": "Command palette in Dialog: search peptides, studies, papers. Grouped results with badges (Peptide/Study/Paper)."
      },
      "testids": {
        "hero_search_input": "data-testid=\"hero-search-input\"",
        "hero_search_submit": "data-testid=\"hero-search-submit\"",
        "command_search_input": "data-testid=\"command-search-input\""
      }
    },
    "filters": {
      "use": ["select.jsx", "popover.jsx", "calendar.jsx", "checkbox.jsx", "slider.jsx", "badge.jsx", "separator.jsx"],
      "spec": {
        "desktop": "Filters in left column Card (sticky within viewport).",
        "mobile": "Filters open in Sheet/Drawer; apply/reset buttons pinned at bottom.",
        "chips": "Active filters shown as removable Badges."
      },
      "testids": {
        "filters-open": "data-testid=\"filters-open\"",
        "filters-apply": "data-testid=\"filters-apply\"",
        "filters-reset": "data-testid=\"filters-reset\""
      }
    },
    "data_display": {
      "use": ["card.jsx", "table.jsx", "tabs.jsx", "accordion.jsx", "collapsible.jsx", "scroll-area.jsx", "skeleton.jsx", "tooltip.jsx", "hover-card.jsx", "pagination.jsx"],
      "spec": {
        "tables": "Use Table for studies/papers with sticky header, row hover, and right-aligned actions.",
        "detail_page": "Tabs: Overview, Mechanism, Dosage, Safety, Studies, Papers, News. Use Accordion for long sections.",
        "loading": "Skeleton blocks matching final layout (avoid spinners-only)."
      },
      "testids": {
        "studies-table": "data-testid=\"studies-table\"",
        "papers-table": "data-testid=\"papers-table\"",
        "peptide-tabs": "data-testid=\"peptide-detail-tabs\""
      }
    },
    "feedback": {
      "use": ["sonner.jsx", "alert.jsx", "progress.jsx"],
      "spec": {
        "toasts": "Use Sonner for saved filters, copied citations, API errors.",
        "empty_states": "Use Alert with icon + action button (e.g., ‘Clear filters’)."
      },
      "testids": {
        "toast-region": "data-testid=\"toast-region\"",
        "empty-state": "data-testid=\"empty-state\""
      }
    },
    "buttons": {
      "variants": {
        "primary": "Button variant=default with teal primary; hover darken; active scale.",
        "secondary": "Button variant=secondary on neutral surface.",
        "ghost": "Button variant=ghost for table row actions.",
        "pill_rule": "Avoid fully pill buttons; use premium rounded (radius 10–12px)."
      },
      "motion": {
        "hover": "transition-colors duration-200; shadow on hover for primary only",
        "press": "active:scale-[0.98] transition-transform duration-150"
      }
    }
  },
  "page_blueprints": {
    "home": {
      "hero": {
        "layout": "Two-column on desktop: left copy + search; right: ‘Live signals’ cards (Eli Lilly trials, new PubMed papers, news).",
        "background": "Molecule/particle canvas behind hero only (opacity 0.35) + subtle radial gradients.",
        "cta": "Primary: Explore Encyclopedia; Secondary: Track Eli Lilly Trials"
      },
      "sections": [
        "Featured peptides (Carousel or grid)",
        "Clinical trials snapshot (mini table)",
        "Latest papers (3–5 items)",
        "News feed (cards)"
      ]
    },
    "encyclopedia": {
      "layout": "Left filters (Card) + right results grid/list toggle.",
      "results": "Card list with peptide name, primary indication tags, safety badge, last updated."
    },
    "peptide_detail": {
      "layout": "Header with breadcrumb + title + key badges; below: Tabs.",
      "content": "Use definition-list style blocks for dosage/mechanism; mono for sequences; citations as compact list with copy button."
    },
    "studies": {
      "layout": "Filters + Table; include company filter with Eli Lilly quick chip.",
      "row": "Study title, phase, status, sponsor, updated date, link out."
    },
    "papers": {
      "layout": "Search + sort (date/relevance) + Table; each row has journal, year, authors, abstract preview HoverCard."
    },
    "news": {
      "layout": "Magazine-like list: featured story large card + smaller cards; filters by topic/peptide.",
      "detail": "Reading view max-w-[72ch], citations, related peptides sidebar."
    }
  },
  "motion_and_microinteractions": {
    "libraries": {
      "framer_motion": {
        "install": "npm i framer-motion",
        "use_cases": [
          "Hero entrance (fade+slide)",
          "Card hover lift",
          "Filter drawer transitions",
          "Tab underline motion"
        ]
      },
      "particle_background": {
        "recommended": "tsparticles (lightweight, configurable)",
        "install": "npm i tsparticles react-tsparticles",
        "behavior": "Use only in hero; pause when tab not visible; respect prefers-reduced-motion."
      }
    },
    "principles": [
      "Entrance: opacity 0 -> 1 + y: 8 -> 0 over 450ms, stagger 60ms.",
      "Hover: cards lift 2px + shadow-elev-2; no transform transitions globally.",
      "Scroll: subtle parallax on hero background only (translateY 0..18px).",
      "Reduced motion: disable particles + parallax; keep simple fades."
    ],
    "css_scaffolds": {
      "noise_overlay": ".noise::before { content: \"\"; position: absolute; inset: 0; background-image: url('data:image/svg+xml;utf8,<svg xmlns=\\\"http://www.w3.org/2000/svg\\\" width=\\\"120\\\" height=\\\"120\\\"><filter id=\\\"n\\\"><feTurbulence type=\\\"fractalNoise\\\" baseFrequency=\\\"0.9\\\" numOctaves=\\\"3\\\" stitchTiles=\\\"stitch\\\"/></filter><rect width=\\\"120\\\" height=\\\"120\\\" filter=\\\"url(%23n)\\\" opacity=\\\"0.35\\\"/></svg>'); opacity: var(--noise-opacity); pointer-events: none; mix-blend-mode: multiply; }",
      "glass_surface": "bg-[var(--glass-bg)] backdrop-blur-md border border-[var(--glass-border)] shadow-[var(--shadow-elev-1)]"
    }
  },
  "data_viz": {
    "library": {
      "recommended": "recharts",
      "install": "npm i recharts",
      "use_cases": [
        "Home quick stats (sparkline for new trials/papers)",
        "Studies page: phase distribution bar chart",
        "Peptide detail: research activity over time"
      ]
    },
    "chart_style": {
      "colors": {
        "primary": "hsl(var(--primary))",
        "muted_grid": "hsl(var(--border))",
        "tooltip_bg": "hsl(var(--popover))"
      },
      "rules": [
        "No gradients in charts; use solid fills with 70–90% opacity.",
        "Always include empty state + skeleton state.",
        "Tooltips must be readable and keyboard accessible."
      ]
    }
  },
  "accessibility": {
    "requirements": [
      "WCAG AA contrast for text and interactive elements.",
      "Visible focus ring: ring-2 ring-[hsl(var(--ring))] ring-offset-2.",
      "Keyboard navigation for menus, dialogs, command palette.",
      "prefers-reduced-motion respected (disable particles/parallax).",
      "Language toggle must set lang attribute on html/body where feasible."
    ]
  },
  "i18n_bilingual": {
    "approach": {
      "recommended": "react-i18next",
      "install": "npm i i18next react-i18next",
      "structure": "src/i18n/{en,de}.json with nested keys (nav.*, home.*, peptide.*)",
      "toggle": "Switch component; persist in localStorage; default based on browser language."
    },
    "testids": {
      "language_toggle": "data-testid=\"language-toggle\""
    }
  },
  "image_urls": {
    "hero_background_optional": [
      {
        "url": "https://images.unsplash.com/photo-1719163534402-ba86dcb55228?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwxfHxhYnN0cmFjdCUyMG1vbGVjdWxlJTIwcGFydGljbGVzJTIwbGlnaHQlMjBiYWNrZ3JvdW5kfGVufDB8fHx0ZWFsfDE3NzQ5OTM2NTR8MA&ixlib=rb-4.1.0&q=85",
        "category": "hero",
        "description": "Soft bubble/molecule texture; use as very low-opacity overlay behind particles (optional)."
      }
    ],
    "editorial_lab_photos": [
      {
        "url": "https://images.unsplash.com/photo-1554475901-4538ddfbccc2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwyfHxzY2llbnRpc3QlMjBsYWIlMjBjbG9zZSUyMHVwJTIwaGFuZHMlMjByZXNlYXJjaHxlbnwwfHx8d2hpdGV8MTc3NDk5MzY1N3ww&ixlib=rb-4.1.0&q=85",
        "category": "about/credibility",
        "description": "Hands with lab flasks; use in About section or credibility strip (not as full-bleed)."
      },
      {
        "url": "https://images.unsplash.com/photo-1579165466991-467135ad3110?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjA1OTN8MHwxfHNlYXJjaHwxfHxjbGVhbiUyMG1lZGljYWwlMjBsYWJvcmF0b3J5JTIwcmVzZWFyY2glMjBsaWdodHxlbnwwfHx8Ymx1ZXwxNzc0OTkzNjUzfDA&ixlib=rb-4.1.0&q=85",
        "category": "home",
        "description": "Clean lab scene; use as small card image or subtle header illustration."
      }
    ]
  },
  "instructions_to_main_agent": [
    "Update /app/frontend/src/App.css: remove CRA demo styles (dark header, spinning logo). Keep file minimal or delete unused classes.",
    "Update /app/frontend/src/index.css tokens to the provided HSL system; set --radius to 0.75rem.",
    "Implement a reusable <GlassPanel> wrapper (div with glass classes) for nav + filter panels.",
    "Hero background animation: use react-tsparticles OR a lightweight canvas; mount only on Home; opacity <= 0.35; disable on prefers-reduced-motion.",
    "Use shadcn Command in Dialog for global search; hero search is a normal Input.",
    "All interactive elements and key info blocks must include data-testid in kebab-case.",
    "Use Recharts for small, tasteful data viz; no gradients in charts.",
    "Implement i18n with react-i18next; every label must have DE/EN keys; add language toggle in nav and persist choice."
  ],
  "general_ui_ux_design_guidelines_appendix": "<General UI UX Design Guidelines>\n    - You must **not** apply universal transition. Eg: `transition: all`. This results in breaking transforms. Always add transitions for specific interactive elements like button, input excluding transforms\n    - You must **not** center align the app container, ie do not add `.App { text-align: center; }` in the css file. This disrupts the human natural reading flow of text\n   - NEVER: use AI assistant Emoji characters like`🤖🧠💭💡🔮🎯📚🎭🎬🎪🎉🎊🎁🎀🎂🍰🎈🎨🎰💰💵💳🏦💎🪙💸🤑📊📈📉💹🔢🏆🥇 etc for icons. Always use **FontAwesome cdn** or **lucid-react** library already installed in the package.json\n\n **GRADIENT RESTRICTION RULE**\nNEVER use dark/saturated gradient combos (e.g., purple/pink) on any UI element.  Prohibited gradients: blue-500 to purple 600, purple 500 to pink-500, green-500 to blue-500, red to pink etc\nNEVER use dark gradients for logo, testimonial, footer etc\nNEVER let gradients cover more than 20% of the viewport.\nNEVER apply gradients to text-heavy content or reading areas.\nNEVER use gradients on small UI elements (<100px width).\nNEVER stack multiple gradient layers in the same viewport.\n\n**ENFORCEMENT RULE:**\n    • Id gradient area exceeds 20% of viewport OR affects readability, **THEN** use solid colors\n\n**How and where to use:**\n   • Section backgrounds (not content backgrounds)\n   • Hero section header content. Eg: dark to light to dark color\n   • Decorative overlays and accent elements only\n   • Hero section with 2-3 mild color\n   • Gradients creation can be done for any angle say horizontal, vertical or diagonal\n\n- For AI chat, voice application, **do not use purple color. Use color like light green, ocean blue, peach orange etc**\n\n</Font Guidelines>\n\n- Every interaction needs micro-animations - hover states, transitions, parallax effects, and entrance animations. Static = dead. \n   \n- Use 2-3x more spacing than feels comfortable. Cramped designs look cheap.\n\n- Subtle grain textures, noise overlays, custom cursors, selection states, and loading animations: separates good from extraordinary.\n   \n- Before generating UI, infer the visual style from the problem statement (palette, contrast, mood, motion) and immediately instantiate it by setting global design tokens (primary, secondary/accent, background, foreground, ring, state colors), rather than relying on any library defaults. Don't make the background dark as a default step, always understand problem first and define colors accordingly\n    Eg: - if it implies playful/energetic, choose a colorful scheme\n           - if it implies monochrome/minimal, choose a black–white/neutral scheme\n\n**Component Reuse:**\n\t- Prioritize using pre-existing components from src/components/ui when applicable\n\t- Create new components that match the style and conventions of existing components when needed\n\t- Examine existing components to understand the project's component patterns before creating new ones\n\n**IMPORTANT**: Do not use HTML based component like dropdown, calendar, toast etc. You **MUST** always use `/app/frontend/src/components/ui/ ` only as a primary components as these are modern and stylish component\n\n**Best Practices:**\n\t- Use Shadcn/UI as the primary component library for consistency and accessibility\n\t- Import path: ./components/[component-name]\n\n**Export Conventions:**\n\t- Components MUST use named exports (export const ComponentName = ...)\n\t- Pages MUST use default exports (export default function PageName() {...})\n\n**Toasts:**\n  - Use `sonner` for toasts\"\n  - Sonner component are located in `/app/src/components/ui/sonner.tsx`\n\nUse 2–4 color gradients, subtle textures/noise overlays, or CSS-based noise to avoid flat visuals.\n</General UI UX Design Guidelines>"
}
