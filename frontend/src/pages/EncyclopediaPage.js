import React, { useState, useEffect, useCallback } from 'react';
import { Helmet } from 'react-helmet-async';
import { Link, useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, FlaskConical, Sparkles, Loader2, Target, GitCompareArrows } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { getPeptides, getCategories, generatePeptide } from '../lib/api';
import { toast } from 'sonner';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

function getPhaseBadge(researchStatus) {
  if (!researchStatus) return null;
  const { fda_approved, ema_approved, phase } = researchStatus;
  const ph = (phase || '').toLowerCase();
  const approved = { background: 'var(--pdb-accent-tint)', color: 'var(--pdb-accent-2)', border: '1px solid var(--pdb-accent-tint-2)' };
  const ph3 = { background: 'var(--pdb-accent-tint)', color: 'var(--pdb-accent)', border: '1px solid var(--pdb-accent-tint-2)' };
  const ph2 = { background: 'var(--pdb-citation-tint)', color: 'var(--pdb-citation)', border: '1px solid #C5D2E8' };
  const ph1 = { background: 'var(--pdb-clay-tint)', color: 'var(--pdb-clay)', border: '1px solid #E8C4B5' };
  const other = { background: 'var(--pdb-page-warm)', color: 'var(--pdb-ink-3)', border: '1px solid var(--pdb-line-2)' };
  if (fda_approved) return { label: 'FDA Approved', style: approved };
  if (ema_approved) return { label: 'EMA Approved', style: approved };
  if (ph.includes('phase 3') || ph.includes('phase iii') || ph.includes('phase 4') || ph.includes('phase iv'))
    return { label: phase, style: ph3 };
  if (ph.includes('phase 2') || ph.includes('phase ii'))
    return { label: phase, style: ph2 };
  if (ph.includes('phase 1') || ph.includes('phase i'))
    return { label: phase, style: ph1 };
  if (ph.includes('preclinical'))
    return { label: phase, style: other };
  return { label: phase || 'Research', style: other };
}

function getFreshness(dateStr) {
  if (!dateStr) return null;
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return null;
  const days = Math.floor((Date.now() - d.getTime()) / 86400000);
  if (days < 7) return { color: 'bg-green-500', label: 'Fresh' };
  if (days < 30) return { color: 'bg-yellow-500', label: 'Recent' };
  if (days < 90) return { color: 'bg-orange-400', label: 'Aging' };
  return { color: 'bg-muted-foreground/50', label: 'Stale' };
}

function formatDate(dateStr, lang) {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return '';
  return d.toLocaleDateString(lang === 'de' ? 'de-DE' : 'en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

export default function EncyclopediaPage() {
  const { t, i18n } = useTranslation();
  const lang = i18n.language;
  const [searchParams, setSearchParams] = useSearchParams();
  const [peptides, setPeptides] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [generating, setGenerating] = useState(false);
  const [compareList, setCompareList] = useState([]);
  const [query, setQuery] = useState(searchParams.get('q') || '');
  const [category, setCategory] = useState('');
  const [goal, setGoal] = useState('');
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const loadPeptides = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getPeptides({ query, category, goal, page, limit: 20 });
      setPeptides(res.data.peptides || []);
      setTotalPages(res.data.pages || 1);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [query, category, goal, page]);

  const loadCategories = useCallback(async () => {
    try {
      const res = await getCategories();
      setCategories(res.data.categories || []);
    } catch (e) { /* ignore */ }
  }, []);

  useEffect(() => { loadPeptides(); }, [loadPeptides]);
  useEffect(() => { loadCategories(); }, [loadCategories]);

  const handleSearch = (e) => {
    e.preventDefault();
    setPage(1);
    setSearchParams(query ? { q: query } : {});
    loadPeptides();
  };

  const handleGenerate = async () => {
    if (!query.trim()) return;
    setGenerating(true);
    try {
      await generatePeptide(query.trim());
      toast.success(lang === 'de' ? `Profil f\u00fcr "${query}" wurde generiert!` : `Profile for "${query}" generated!`);
      await loadPeptides();
    } catch (e) {
      toast.error(lang === 'de' ? 'Fehler beim Generieren' : 'Generation failed');
    }
    setGenerating(false);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <Helmet>
        <title>Peptide Encyclopedia — PeptideDB</title>
        <meta name="description" content="Browse and search 48+ peptide therapeutics. Filter by category, goal, and research phase. Compare peptides side by side." />
      </Helmet>
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'var(--pdb-font-display)', letterSpacing: '-0.02em' }}>
          {t('encyclopedia.title')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground max-w-[64ch]">
          {t('encyclopedia.subtitle')}
        </p>
      </motion.div>

      {/* Filters */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="flex flex-col sm:flex-row gap-3 mb-8">
        <form onSubmit={handleSearch} className="flex gap-2 flex-1 max-w-lg">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <input
              data-testid="encyclopedia-search"
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={t('encyclopedia.search_placeholder')}
              className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-card text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
            />
          </div>
          <Button type="submit" size="sm" className="btn-press rounded-xl">
            <Search className="w-4 h-4" />
          </Button>
        </form>

        <Select value={category} onValueChange={(val) => { setCategory(val === 'all' ? '' : val); setPage(1); }}>
          <SelectTrigger className="w-full sm:w-[200px] rounded-xl" data-testid="category-filter">
            <SelectValue placeholder={t('encyclopedia.all_categories')} />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">{t('encyclopedia.all_categories')}</SelectItem>
            {categories.map(cat => (
              <SelectItem key={cat} value={cat}>{cat}</SelectItem>
            ))}
          </SelectContent>
        </Select>
      </motion.div>

      {/* Goal Filters */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={2} className="flex flex-wrap items-center gap-2 mb-6">
        <Target className="w-4 h-4 text-muted-foreground mr-1" />
        {[
          { key: '', labelEn: lang === 'de' ? 'Alle Ziele' : 'All Goals' },
          { key: 'Fat Loss', labelEn: lang === 'de' ? 'Fettverbrennung' : 'Fat Loss' },
          { key: 'Muscle Building', labelEn: lang === 'de' ? 'Muskelaufbau' : 'Muscle Building' },
          { key: 'Healing', labelEn: lang === 'de' ? 'Heilung' : 'Healing' },
          { key: 'Anti-Aging', labelEn: 'Anti-Aging' },
          { key: 'Cognitive', labelEn: lang === 'de' ? 'Kognitiv' : 'Cognitive' },
          { key: 'Immune', labelEn: lang === 'de' ? 'Immunsystem' : 'Immune Support' },
        ].map((g) => (
          <button
            key={g.key}
            onClick={() => { setGoal(g.key); setPage(1); }}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
              goal === g.key
                ? 'bg-primary text-primary-foreground'
                : 'bg-secondary text-muted-foreground hover:text-foreground hover:bg-secondary/80'
            }`}
          >
            {g.labelEn}
          </button>
        ))}
      </motion.div>

      {/* Results */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {Array.from({ length: 9 }).map((_, i) => (
            <Card key={i} className="border border-border/50">
              <CardContent className="p-5 space-y-3">
                <Skeleton className="h-5 w-32" />
                <Skeleton className="h-4 w-24" />
                <Skeleton className="h-16 w-full" />
              </CardContent>
            </Card>
          ))}
        </div>
      ) : peptides.length > 0 ? (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {peptides.map((p, i) => (
              <motion.div key={p.slug || i} initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp} custom={i % 6}>
                <Card className="card-hover border border-border/50 h-full relative" data-testid={`peptide-card-${p.slug}`}>
                  <Link to={`/encyclopedia/${p.slug}`}>
                    <CardContent className="p-5 pb-12">
                      <div className="flex items-start justify-between mb-2">
                        <h3 className="font-semibold text-base" style={{ fontFamily: 'var(--pdb-font-display)', fontWeight: 500, letterSpacing: '-0.01em' }}>{p.name}</h3>
                        <Badge variant="secondary" className="text-xs shrink-0 ml-2">{p.category || 'Peptide'}</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground line-clamp-3 leading-relaxed">
                        {p.description?.[lang] || p.description?.en || ''}
                      </p>
                      {p.research_status && (() => {
                        const badge = getPhaseBadge(p.research_status);
                        return badge ? (
                          <div className="mt-3 flex flex-wrap items-center gap-2">
                            <span style={{ ...badge.style, display: 'inline-flex', alignItems: 'center', padding: '3px 8px', borderRadius: 4, fontSize: 11, fontWeight: 500, fontFamily: 'var(--pdb-font-mono)', letterSpacing: '0.04em' }}>
                              {badge.label}
                            </span>
                            {p.manufacturer && (
                              <span className="text-xs text-muted-foreground">{p.manufacturer}</span>
                            )}
                          </div>
                        ) : null;
                      })()}
                    </CardContent>
                  </Link>
                  <button
                    onClick={(e) => {
                      e.preventDefault();
                      setCompareList(prev =>
                        prev.includes(p.slug)
                          ? prev.filter(s => s !== p.slug)
                          : prev.length < 3 ? [...prev, p.slug] : prev
                      );
                    }}
                    className={`absolute bottom-3 right-3 px-2.5 py-1 rounded-lg text-xs font-medium transition-colors flex items-center gap-1 ${
                      compareList.includes(p.slug)
                        ? 'bg-primary text-primary-foreground'
                        : 'bg-secondary text-muted-foreground hover:bg-secondary/80'
                    }`}
                  >
                    <GitCompareArrows className="w-3 h-3" />
                    {compareList.includes(p.slug) ? t('detail.remove_from_compare') : t('detail.compare')}
                  </button>
                </Card>
              </motion.div>
            ))}
          </div>

          {/* Pagination */}
          {totalPages > 1 && (
            <div className="flex justify-center items-center gap-2 mt-10">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setPage(p => Math.max(1, p - 1))}
                disabled={page <= 1}
                className="rounded-xl"
              >
                Previous
              </Button>
              <span className="text-sm text-muted-foreground tabular-nums">
                {page} / {totalPages}
              </span>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                disabled={page >= totalPages}
                className="rounded-xl"
              >
                Next
              </Button>
            </div>
          )}
        </>
      ) : (
        <Card className="border border-border/50" data-testid="empty-state">
          <CardContent className="p-12 text-center">
            <FlaskConical className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <h3 className="font-semibold mb-1">{t('encyclopedia.no_results')}</h3>
            <p className="text-sm text-muted-foreground mb-6">{t('encyclopedia.no_results_hint')}</p>
            {query && (
              <Button onClick={handleGenerate} disabled={generating} className="btn-press rounded-xl gap-2">
                {generating ? <Loader2 className="w-4 h-4 animate-spin" /> : <Sparkles className="w-4 h-4" />}
                {t('encyclopedia.generate_new')}: "{query}"
              </Button>
            )}
          </CardContent>
        </Card>
      )}

      {/* Floating Compare Bar */}
      {compareList.length >= 2 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="fixed bottom-6 left-1/2 -translate-x-1/2 z-40"
        >
          <Link
            to={`/encyclopedia/compare?peptides=${compareList.join(',')}`}
            className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl bg-primary text-primary-foreground shadow-lg hover:opacity-90 transition-opacity font-medium text-sm"
          >
            <GitCompareArrows className="w-4 h-4" />
            {t('detail.compare_peptides')} ({compareList.length})
          </Link>
        </motion.div>
      )}
    </div>
  );
}
