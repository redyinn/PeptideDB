import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { AnimatePresence, motion } from 'framer-motion';
import { Menu, X, Moon, Sun, Globe, Calculator } from 'lucide-react';

const navItems = [
  { key: 'encyclopedia', path: '/encyclopedia' },
  { key: 'studies',      path: '/studies' },
  { key: 'papers',       path: '/papers' },
  { key: 'news',         path: '/news' },
  { key: 'glossary',     path: '/glossary' },
];

export default function Navbar() {
  const { t, i18n } = useTranslation();
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [dark, setDark] = useState(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('peptide-theme');
      if (saved) return saved === 'dark';
      return window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    return false;
  });

  React.useEffect(() => {
    const root = document.documentElement;
    dark ? root.classList.add('dark') : root.classList.remove('dark');
    localStorage.setItem('peptide-theme', dark ? 'dark' : 'light');
  }, [dark]);

  const isActive = (path) =>
    path === '/' ? location.pathname === '/' : location.pathname.startsWith(path);

  const iconBtn = {
    display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
    width: 32, height: 32, borderRadius: 6, cursor: 'pointer',
    border: '1px solid oklch(88% 0.006 145)',
    background: 'transparent', color: 'var(--pdb-ink)',
    transition: 'background 120ms, border-color 120ms',
  };

  return (
    <header style={{ position: 'sticky', top: 0, zIndex: 50, width: '100%' }}>
      <div className="glass-surface">
        <div style={{ maxWidth: 1280, margin: '0 auto', padding: '0 24px', display: 'flex', alignItems: 'center', gap: 8, height: 58 }}>

          {/* Wordmark */}
          <Link to="/" data-testid="nav-logo" style={{ display: 'flex', alignItems: 'center', gap: 10, textDecoration: 'none', marginRight: 16 }}>
            <img src="/logo-mark.svg" width="26" height="26" alt="" />
            <span style={{ fontFamily: 'var(--pdb-font-display)', fontSize: 19, fontWeight: 500, letterSpacing: '-0.01em', color: 'var(--pdb-ink)' }}>
              PeptideDB
            </span>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden md:flex" style={{ gap: 2 }}>
            {navItems.map(item => (
              <Link
                key={item.key}
                to={item.path}
                data-testid={`nav-${item.key}`}
                style={{
                  padding: '6px 12px', borderRadius: 6, fontSize: 14, fontWeight: 500,
                  fontFamily: 'var(--pdb-font-body)', textDecoration: 'none',
                  color: isActive(item.path) ? 'var(--pdb-ink)' : 'var(--pdb-ink-3)',
                  background: isActive(item.path) ? 'oklch(92% 0.005 145 / 0.6)' : 'transparent',
                  transition: 'color 120ms, background 120ms',
                }}
              >
                {t(`nav.${item.key}`)}
              </Link>
            ))}
          </nav>

          <div style={{ flex: 1 }} />

          {/* Actions */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <Link to="/calculator" title="Dosage Calculator" style={{ ...iconBtn, textDecoration: 'none' }}>
              <Calculator style={{ width: 15, height: 15 }} />
            </Link>
            <button
              onClick={() => setDark(p => !p)}
              data-testid="theme-toggle"
              title={dark ? t('nav.light_mode') : t('nav.dark_mode')}
              style={iconBtn}
            >
              {dark
                ? <Sun  style={{ width: 15, height: 15 }} />
                : <Moon style={{ width: 15, height: 15 }} />
              }
            </button>
            <button
              onClick={() => i18n.changeLanguage(i18n.language === 'en' ? 'de' : 'en')}
              data-testid="language-toggle"
              style={{ ...iconBtn, gap: 4, width: 'auto', padding: '0 10px', fontSize: 13, fontWeight: 600 }}
            >
              <Globe style={{ width: 13, height: 13 }} />
              {i18n.language === 'en' ? 'DE' : 'EN'}
            </button>

            {/* Mobile hamburger */}
            <button
              className="md:hidden"
              onClick={() => setMobileOpen(!mobileOpen)}
              data-testid="mobile-nav-open"
              style={iconBtn}
            >
              {mobileOpen ? <X style={{ width: 17, height: 17 }} /> : <Menu style={{ width: 17, height: 17 }} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile nav */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.18 }}
            className="md:hidden"
            style={{ background: 'var(--pdb-page)', borderBottom: '1px solid oklch(92% 0.005 145)' }}
          >
            <div style={{ maxWidth: 1280, margin: '0 auto', padding: '10px 24px 14px', display: 'flex', flexDirection: 'column', gap: 2 }}>
              <Link to="/" onClick={() => setMobileOpen(false)} style={{ padding: '8px 12px', borderRadius: 6, fontSize: 14, fontWeight: 500, color: isActive('/') ? 'var(--pdb-accent)' : 'var(--pdb-ink-2)', textDecoration: 'none' }}>{t('nav.home')}</Link>
              {navItems.map(item => (
                <Link key={item.key} to={item.path} onClick={() => setMobileOpen(false)} style={{ padding: '8px 12px', borderRadius: 6, fontSize: 14, fontWeight: 500, color: isActive(item.path) ? 'var(--pdb-accent)' : 'var(--pdb-ink-2)', textDecoration: 'none' }}>
                  {t(`nav.${item.key}`)}
                </Link>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
