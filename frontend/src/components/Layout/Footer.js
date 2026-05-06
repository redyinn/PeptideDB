import React from 'react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

function FooterCol({ heading, items }) {
  return (
    <div>
      <div className="pdb-overline" style={{ marginBottom: 12 }}>{heading}</div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: 8 }}>
        {items.map(({ label, to, href }) => (
          <li key={label}>
            {to ? (
              <Link to={to} style={{ fontSize: 13, color: 'var(--pdb-ink-2)', textDecoration: 'none' }}>{label}</Link>
            ) : (
              <a href={href || '#'} style={{ fontSize: 13, color: 'var(--pdb-ink-2)', textDecoration: 'none' }}>{label}</a>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default function Footer() {
  const { t } = useTranslation();

  return (
    <footer style={{ borderTop: '1px solid oklch(92% 0.005 145)', marginTop: 64, padding: '40px 24px 56px', background: 'var(--pdb-page-warm)' }}>
      <div style={{ maxWidth: 1280, margin: '0 auto', display: 'flex', justifyContent: 'space-between', gap: 32, flexWrap: 'wrap' }}>

        <div style={{ maxWidth: 340 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 12 }}>
            <img src="/logo-mark.svg" width="22" height="22" alt="" />
            <span style={{ fontFamily: 'var(--pdb-font-display)', fontSize: 17, fontWeight: 500, color: 'var(--pdb-ink)' }}>PeptideDB</span>
          </div>
          <p style={{ fontSize: 13, color: 'var(--pdb-ink-3)', margin: 0, lineHeight: 1.65 }}>
            {t('footer.disclaimer')} {t('footer.data_sources')}: ClinicalTrials.gov, PubMed.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 48, flexWrap: 'wrap' }}>
          <FooterCol heading="Product" items={[
            { label: t('nav.encyclopedia'), to: '/encyclopedia' },
            { label: t('nav.studies'),      to: '/studies' },
            { label: t('nav.papers'),       to: '/papers' },
            { label: 'Calculator',          to: '/calculator' },
          ]} />
          <FooterCol heading="Resources" items={[
            { label: t('nav.glossary'), to: '/glossary' },
            { label: t('nav.news'),     to: '/news' },
          ]} />
        </div>
      </div>
    </footer>
  );
}
