import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Helmet } from 'react-helmet-async';
import { Link, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { Search, ArrowRight, Dna, BookOpen, TestTube, ExternalLink, TrendingUp, FlaskConical } from 'lucide-react';
import { Skeleton } from '../components/ui/skeleton';
import { getPeptides, getTrials, getPapers, getStats, seedPeptides, getSeedStatus } from '../lib/api';

/* ── shared inline styles ──────────────────────────────────────────────── */
const ink  = 'var(--pdb-ink)';
const ink2 = 'var(--pdb-ink-2)';
const ink3 = 'var(--pdb-ink-3)';
const acc  = 'var(--pdb-accent)';
const acc2 = 'var(--pdb-accent-2)';
const accT = 'var(--pdb-accent-tint)';
const accT2= 'var(--pdb-accent-tint-2)';
const mono = 'var(--pdb-font-mono)';
const disp = 'var(--pdb-font-display)';
const body = 'var(--pdb-font-body)';

/* ── StatPill ──────────────────────────────────────────────────────────── */
function StatPill({ n, label, useMono = true, delay = '0ms' }) {
  return (
    <div className="pdb-stat" style={{ animationDelay: delay }}>
      <div style={{ fontFamily: useMono ? mono : disp, fontSize: 22, fontWeight: 500, color: ink, lineHeight: 1 }}>{n}</div>
      <div style={{ fontFamily: body, fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.10em', color: ink3, marginTop: 5 }}>{label}</div>
    </div>
  );
}

/* ── PeptideCard ───────────────────────────────────────────────────────── */
function PeptideCard({ peptide, index, lang }) {
  return (
    <Link to={`/encyclopedia/${peptide.slug}`} style={{ textDecoration: 'none' }}>
      <article
        className="card-hover pdb-card-in"
        style={{
          animationDelay: `${index * 60}ms`,
          border: '1px solid oklch(92% 0.005 145)',
          borderRadius: 8, padding: 22, background: '#fff',
          display: 'flex', flexDirection: 'column', gap: 10, height: '100%',
        }}
        data-testid={`peptide-card-${peptide.slug}`}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 12 }}>
          <div>
            <h3 style={{ fontFamily: disp, fontSize: 20, fontWeight: 500, color: ink, margin: 0, letterSpacing: '-0.01em' }}>{peptide.name}</h3>
            <div style={{ fontFamily: body, fontSize: 12, color: ink3, marginTop: 3 }}>{peptide.category || 'Peptide'}</div>
          </div>
          {peptide.research_status?.phase && (
            <span style={{ fontFamily: mono, fontSize: 11, color: acc2, background: accT, padding: '4px 8px', borderRadius: 4, whiteSpace: 'nowrap', flexShrink: 0 }}>
              {peptide.research_status.phase}
            </span>
          )}
        </div>
        <p style={{ fontFamily: body, fontSize: 14, lineHeight: 1.6, color: ink2, margin: 0, flex: 1 }}>
          {(peptide.description?.[lang] || peptide.description?.en || '').slice(0, 160)}…
        </p>
        <div style={{ display: 'flex', gap: 16, fontFamily: mono, fontSize: 12, color: ink3, borderTop: '1px solid oklch(96% 0.003 145)', paddingTop: 10, marginTop: 'auto' }}>
          {peptide.trials_count > 0 && <span><b style={{ color: ink, fontWeight: 500 }}>{peptide.trials_count}</b> trials</span>}
          {peptide.papers_count > 0 && <span><b style={{ color: ink, fontWeight: 500 }}>{peptide.papers_count}</b> papers</span>}
          {peptide.half_life && <span>t½&nbsp;<b style={{ color: ink, fontWeight: 500 }}>{peptide.half_life}</b></span>}
        </div>
      </article>
    </Link>
  );
}

/* ── TrialRow ──────────────────────────────────────────────────────────── */
function TrialRow({ trial, index }) {
  const statusCls = (() => {
    const s = (trial.status || '').toLowerCase();
    if (s.includes('recruit')) return 'status-recruiting';
    if (s.includes('complet')) return 'status-completed';
    if (s.includes('active'))  return 'status-active';
    return 'status-default';
  })();
  return (
    <a
      href={trial.url}
      target="_blank"
      rel="noopener noreferrer"
      className="pdb-card-in"
      style={{
        animationDelay: `${index * 50}ms`,
        display: 'flex', alignItems: 'flex-start', gap: 16, padding: '14px 16px',
        borderRadius: 8, border: '1px solid oklch(92% 0.005 145)', background: '#fff',
        textDecoration: 'none', transition: 'border-color 200ms var(--pdb-ease)',
      }}
      data-testid={`trial-item-${index}`}
      onMouseEnter={(e) => { e.currentTarget.style.borderColor = 'oklch(80% 0.008 145)'; }}
      onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'oklch(92% 0.005 145)'; }}
    >
      <div style={{ flex: 1, minWidth: 0 }}>
        <p style={{ fontFamily: body, fontSize: 14, fontWeight: 500, color: ink, margin: 0, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
          {trial.title}
        </p>
        <div style={{ marginTop: 6, display: 'flex', flexWrap: 'wrap', gap: 8, alignItems: 'center', fontFamily: mono, fontSize: 12, color: ink3 }}>
          <span>{trial.nct_id}</span>
          {trial.sponsor && <><span>·</span><span style={{ fontFamily: body }}>{trial.sponsor}</span></>}
          <span className={statusCls} style={{ padding: '2px 7px', borderRadius: 4, fontSize: 11, fontWeight: 500 }}>
            {trial.status?.replace(/_/g, ' ')}
          </span>
        </div>
      </div>
      <ExternalLink style={{ width: 14, height: 14, color: ink3, flexShrink: 0, marginTop: 3 }} />
    </a>
  );
}

/* ── HomePage ──────────────────────────────────────────────────────────── */
export default function HomePage() {
  const { t, i18n } = useTranslation();
  const navigate = useNavigate();
  const lang = i18n.language;

  const [searchQuery, setSearchQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [suggestLoading, setSuggestLoading] = useState(false);
  const searchRef = useRef(null);
  const debounceRef = useRef(null);

  const [peptides, setPeptides] = useState([]);
  const [trials,   setTrials]   = useState([]);
  const [stats,    setStats]    = useState(null);
  const [loading,  setLoading]  = useState(true);
  const [seeding,  setSeeding]  = useState(false);

  const loadData = useCallback(async () => {
    setLoading(true);
    try {
      const [pepRes, trialRes, statsRes] = await Promise.allSettled([
        getPeptides({ limit: 6 }),
        getTrials({ query: 'peptide', page_size: 5 }),
        getStats(),
      ]);
      if (pepRes.status   === 'fulfilled') setPeptides(pepRes.value.data.peptides || []);
      if (trialRes.status === 'fulfilled') setTrials(trialRes.value.data.trials || []);
      if (statsRes.status === 'fulfilled') setStats(statsRes.value.data);

      if (pepRes.status === 'fulfilled' && (pepRes.value.data.peptides || []).length === 0) {
        setSeeding(true);
        try {
          await seedPeptides();
          const poll = setInterval(async () => {
            try {
              const s = await getSeedStatus();
              if (s.data.seeded > 0) {
                const fp = await getPeptides({ limit: 6 });
                setPeptides(fp.data.peptides || []);
                const fs = await getStats();
                setStats(fs.data);
              }
              if (s.data.seeded >= 5) { clearInterval(poll); setSeeding(false); }
            } catch { /* ignore */ }
          }, 8000);
          setTimeout(() => { clearInterval(poll); setSeeding(false); }, 180000);
        } catch { setSeeding(false); }
      }
    } catch (e) { console.error(e); }
    setLoading(false);
  }, []);

  useEffect(() => { loadData(); }, [loadData]);

  const handleSearch = (e) => {
    e.preventDefault();
    setShowSuggestions(false);
    if (searchQuery.trim()) navigate(`/encyclopedia?q=${encodeURIComponent(searchQuery.trim())}`);
  };

  const handleSearchChange = (e) => {
    const val = e.target.value;
    setSearchQuery(val);
    clearTimeout(debounceRef.current);
    if (!val.trim()) { setSuggestions([]); setShowSuggestions(false); return; }
    debounceRef.current = setTimeout(async () => {
      setSuggestLoading(true);
      try {
        const res = await getPeptides({ query: val.trim(), limit: 6 });
        setSuggestions(res.data.peptides || []);
        setShowSuggestions(true);
      } catch { setSuggestions([]); }
      setSuggestLoading(false);
    }, 280);
  };

  useEffect(() => {
    const h = (e) => { if (searchRef.current && !searchRef.current.contains(e.target)) setShowSuggestions(false); };
    document.addEventListener('mousedown', h);
    return () => document.removeEventListener('mousedown', h);
  }, []);

  return (
    <div>
      <Helmet>
        <title>PeptideDB — Peptide Research Database</title>
        <meta name="description" content="Explore 48+ peptide therapeutics with clinical trial data, PubMed research papers, dosage information, and mechanisms of action." />
      </Helmet>

      {/* ── Hero ─────────────────────────────────────────────────────── */}
      <section style={{ position: 'relative', overflow: 'hidden', background: 'var(--pdb-page)' }}>
        <div style={{
          maxWidth: 1280, margin: '0 auto', padding: '88px 24px 64px',
          display: 'grid', gridTemplateColumns: '1.25fr 1fr', gap: 48, alignItems: 'center',
        }}>
          {/* Left column */}
          <div>
            <div className="pdb-overline pdb-rise" style={{ marginBottom: 20 }}>The peptide research database</div>
            <h1
              className="pdb-rise"
              style={{
                animationDelay: '80ms',
                fontFamily: disp,
                fontSize: 'clamp(42px, 5.2vw, 68px)',
                fontWeight: 500, lineHeight: 1.04,
                letterSpacing: '-0.025em',
                margin: '0 0 18px', color: ink,
                textWrap: 'balance',
                fontVariationSettings: '"opsz" 144',
              }}
            >
              Peptide therapeutics,<br />evidenced.
            </h1>
            <p
              className="pdb-rise"
              style={{
                animationDelay: '160ms',
                fontFamily: body, fontSize: 18, lineHeight: 1.6,
                color: ink2, maxWidth: '52ch', margin: '0 0 28px',
              }}
            >
              {t('home.hero_subtitle') || 'Browse mechanisms of action, clinical trials, and the papers behind every claim — across 48 compounds. Updated weekly from PubMed and ClinicalTrials.gov.'}
            </p>

            {/* CTA buttons */}
            <div className="pdb-rise" style={{ animationDelay: '240ms', display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'center' }}>
              <Link to="/encyclopedia" style={{
                fontFamily: body, fontSize: 15, fontWeight: 500, textDecoration: 'none',
                padding: '11px 22px', borderRadius: 8, border: 0,
                background: acc, color: '#fff', display: 'inline-flex', alignItems: 'center', gap: 7,
                transition: 'background 200ms, transform 200ms',
              }}
                onMouseEnter={(e) => { e.currentTarget.style.background = acc2; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                onMouseLeave={(e) => { e.currentTarget.style.background = acc;  e.currentTarget.style.transform = 'translateY(0)'; }}
              >
                {t('home.explore_encyclopedia') || 'Browse the database'}
                <ArrowRight style={{ width: 15, height: 15 }} />
              </Link>
              <Link to="/studies" style={{
                fontFamily: body, fontSize: 15, fontWeight: 500, textDecoration: 'none',
                padding: '11px 16px', color: ink,
                transition: 'color 120ms',
              }}
                onMouseEnter={(e) => { e.currentTarget.style.color = acc; }}
                onMouseLeave={(e) => { e.currentTarget.style.color = ink; }}
              >
                {t('home.track_studies') || 'Methodology →'}
              </Link>
            </div>

            {/* Search */}
            <div
              ref={searchRef}
              className="pdb-rise"
              style={{ animationDelay: '320ms', position: 'relative', maxWidth: 480, marginTop: 28 }}
            >
              <form onSubmit={handleSearch} style={{ display: 'flex', gap: 8 }}>
                <div style={{ position: 'relative', flex: 1 }}>
                  <Search style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', width: 14, height: 14, color: ink3 }} />
                  {suggestLoading && (
                    <div style={{ position: 'absolute', right: 12, top: '50%', transform: 'translateY(-50%)', width: 13, height: 13, border: `1.5px solid ${acc}`, borderTopColor: 'transparent', borderRadius: '50%', animation: 'spin 0.6s linear infinite' }} />
                  )}
                  <input
                    data-testid="hero-search-input"
                    type="text"
                    value={searchQuery}
                    onChange={handleSearchChange}
                    onFocus={() => suggestions.length > 0 && setShowSuggestions(true)}
                    placeholder={t('home.search_placeholder') || 'Search peptides…'}
                    autoComplete="off"
                    style={{
                      width: '100%', paddingLeft: 36, paddingRight: 14, paddingTop: 9, paddingBottom: 9,
                      fontFamily: body, fontSize: 14, border: '1px solid oklch(85% 0.008 145)',
                      borderRadius: 6, background: '#fff', color: ink, outline: 'none',
                      boxSizing: 'border-box',
                      transition: 'border-color 120ms',
                    }}
                    onFocusCapture={(e) => { e.target.style.borderColor = acc; }}
                    onBlurCapture={(e) => { e.target.style.borderColor = 'oklch(85% 0.008 145)'; }}
                  />
                </div>
                <button
                  type="submit"
                  data-testid="hero-search-submit"
                  style={{
                    padding: '9px 16px', borderRadius: 6, border: 0, cursor: 'pointer',
                    background: acc, color: '#fff', fontFamily: body, fontSize: 14, fontWeight: 500,
                    display: 'flex', alignItems: 'center', gap: 6,
                    transition: 'background 200ms',
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.background = acc2; }}
                  onMouseLeave={(e) => { e.currentTarget.style.background = acc; }}
                >
                  <Search style={{ width: 14, height: 14 }} />
                </button>
              </form>

              {/* Autocomplete dropdown */}
              {showSuggestions && suggestions.length > 0 && (
                <div style={{
                  position: 'absolute', top: '100%', left: 0, right: 48, marginTop: 6,
                  background: '#fff', border: '1px solid oklch(88% 0.006 145)',
                  borderRadius: 8, boxShadow: 'var(--pdb-shadow-2)', zIndex: 50, overflow: 'hidden',
                }}>
                  {suggestions.map((p) => (
                    <button
                      key={p.slug}
                      onMouseDown={() => { setShowSuggestions(false); navigate(`/encyclopedia/${p.slug}`); }}
                      style={{
                        width: '100%', display: 'flex', alignItems: 'center', gap: 12,
                        padding: '10px 14px', background: 'transparent', border: 0, cursor: 'pointer',
                        textAlign: 'left', transition: 'background 80ms',
                      }}
                      onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--pdb-page-warm)'; }}
                      onMouseLeave={(e) => { e.currentTarget.style.background = 'transparent'; }}
                    >
                      <Dna style={{ width: 14, height: 14, color: acc, flexShrink: 0 }} />
                      <div style={{ flex: 1, minWidth: 0 }}>
                        <p style={{ fontFamily: body, fontSize: 14, fontWeight: 500, color: ink, margin: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{p.name}</p>
                        <p style={{ fontFamily: body, fontSize: 12, color: ink3, margin: 0 }}>{p.category}</p>
                      </div>
                      <ArrowRight style={{ width: 12, height: 12, color: ink3, flexShrink: 0 }} />
                    </button>
                  ))}
                  <button
                    onMouseDown={handleSearch}
                    style={{
                      width: '100%', padding: '9px 14px', borderTop: '1px solid oklch(95% 0.004 145)',
                      background: 'transparent', border: 0, borderTop: '1px solid oklch(95% 0.004 145)',
                      display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer',
                      fontFamily: mono, fontSize: 12, color: acc,
                    }}
                  >
                    <Search style={{ width: 12, height: 12 }} />
                    {lang === 'de' ? `Alle Ergebnisse für „${searchQuery}"` : `All results for "${searchQuery}"`}
                  </button>
                </div>
              )}
            </div>

            {/* Stats bar */}
            <div
              className="pdb-rise"
              style={{
                animationDelay: '400ms',
                display: 'flex', gap: 28, marginTop: 44, paddingTop: 20,
                borderTop: '1px solid oklch(92% 0.005 145)', flexWrap: 'wrap',
              }}
            >
              <StatPill n={stats?.peptides_in_db || '48+'} label="Peptides" delay="480ms" />
              <StatPill n="4,200+"  label="Papers"       delay="540ms" />
              <StatPill n={trials.length || '318'} label="Trials" delay="600ms" />
              <StatPill n="Weekly"  label="Updates" useMono={false} delay="660ms" />
            </div>
          </div>

          {/* Right column — animated molecule */}
          <div className="pdb-fade" style={{ position: 'relative', justifySelf: 'end', animationDelay: '200ms', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <div className="pdb-glow" style={{
              position: 'absolute', inset: '-40px', borderRadius: '50%',
              background: 'radial-gradient(circle, rgba(47,125,107,0.12), transparent 65%)',
              pointerEvents: 'none',
            }} />
            <img
              className="pdb-mol"
              src="/molecule-animated.svg"
              width="360" height="360"
              alt=""
              style={{ position: 'relative', zIndex: 1, display: 'block', maxWidth: '100%' }}
            />
          </div>
        </div>

        {/* Mobile: hide right column */}
        <style>{`@media (max-width: 768px) { .pdb-hero-grid { grid-template-columns: 1fr !important; } .pdb-hero-mol { display: none !important; } }`}</style>
      </section>

      {/* ── Featured Peptides ─────────────────────────────────────────── */}
      <section style={{ maxWidth: 1280, margin: '0 auto', padding: '64px 24px' }}>
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', marginBottom: 28, flexWrap: 'wrap', gap: 16 }}>
          <div>
            <h2 style={{ fontFamily: disp, fontSize: 28, fontWeight: 500, margin: 0, letterSpacing: '-0.015em', color: ink }}>
              {t('home.featured_peptides') || 'Featured peptides'}
            </h2>
            {!loading && (
              <p style={{ fontFamily: body, fontSize: 14, color: ink3, margin: '5px 0 0' }}>{peptides.length} compounds shown</p>
            )}
          </div>
          <Link to="/encyclopedia" style={{ fontFamily: body, fontSize: 14, fontWeight: 500, color: acc, textDecoration: 'none', display: 'flex', alignItems: 'center', gap: 4 }}>
            {t('home.view_all') || 'View all'} <ArrowRight style={{ width: 14, height: 14 }} />
          </Link>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: 14 }}>
          {loading ? (
            Array.from({ length: 6 }).map((_, i) => (
              <div key={i} style={{ border: '1px solid oklch(92% 0.005 145)', borderRadius: 8, padding: 22, background: '#fff' }}>
                <Skeleton className="h-5 w-32 mb-2" />
                <Skeleton className="h-4 w-24 mb-4" />
                <Skeleton className="h-16 w-full" />
              </div>
            ))
          ) : peptides.length > 0 ? (
            peptides.map((p, i) => <PeptideCard key={p.slug || i} peptide={p} index={i} lang={lang} />)
          ) : (
            <div style={{ gridColumn: '1 / -1', padding: '48px 0', textAlign: 'center' }}>
              <Dna style={{ width: 36, height: 36, color: ink3, margin: '0 auto 12px' }} />
              <p style={{ fontFamily: body, fontSize: 14, color: ink3 }}>{t('encyclopedia.no_results')}</p>
            </div>
          )}
        </div>

        {seeding && (
          <div style={{ marginTop: 16, padding: '12px 16px', borderRadius: 8, background: accT, border: `1px solid ${accT2}`, display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{ width: 16, height: 16, border: `2px solid ${acc}`, borderTopColor: 'transparent', borderRadius: '50%', animation: 'spin 0.6s linear infinite', flexShrink: 0 }} />
            <span style={{ fontFamily: body, fontSize: 14, color: acc, fontWeight: 500 }}>{t('home.generating')}</span>
          </div>
        )}
      </section>

      {/* ── Latest Trials ─────────────────────────────────────────────── */}
      <section style={{ borderTop: '1px solid oklch(92% 0.005 145)', background: 'var(--pdb-page-warm)' }}>
        <div style={{ maxWidth: 1280, margin: '0 auto', padding: '56px 24px 64px' }}>
          <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', marginBottom: 24, flexWrap: 'wrap', gap: 16 }}>
            <h2 style={{ fontFamily: disp, fontSize: 28, fontWeight: 500, margin: 0, letterSpacing: '-0.015em', color: ink }}>
              {t('home.latest_studies') || 'Active clinical trials'}
            </h2>
            <Link to="/studies" style={{ fontFamily: body, fontSize: 14, fontWeight: 500, color: acc, textDecoration: 'none', display: 'flex', alignItems: 'center', gap: 4 }}>
              {t('home.view_all') || 'View all'} <ArrowRight style={{ width: 14, height: 14 }} />
            </Link>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {loading ? (
              Array.from({ length: 4 }).map((_, i) => (
                <div key={i} style={{ border: '1px solid oklch(92% 0.005 145)', borderRadius: 8, padding: '14px 16px', background: '#fff' }}>
                  <Skeleton className="h-4 w-full mb-2" />
                  <Skeleton className="h-3 w-48" />
                </div>
              ))
            ) : trials.length > 0 ? (
              trials.slice(0, 5).map((trial, i) => <TrialRow key={trial.nct_id || i} trial={trial} index={i} />)
            ) : (
              <p style={{ fontFamily: body, fontSize: 14, color: ink3, textAlign: 'center', padding: '32px 0' }}>{t('studies.no_results')}</p>
            )}
          </div>
        </div>
      </section>

      <style>{`
        @keyframes spin { to { transform: rotate(360deg); } }
        @media (max-width: 768px) {
          section:first-of-type > div:first-child {
            grid-template-columns: 1fr !important;
          }
          section:first-of-type > div:first-child > div:last-child {
            display: none;
          }
        }
      `}</style>
    </div>
  );
}
