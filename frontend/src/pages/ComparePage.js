import React, { useState, useEffect, useCallback } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { ArrowLeft, X, Search, FlaskConical } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { comparePeptides, getPeptides } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

function CompareRow({ label, values, mono = false }) {
  return (
    <div className="grid grid-cols-[180px_1fr_1fr] gap-4 py-3 border-b border-border/50 last:border-0">
      <span className="text-sm text-muted-foreground font-medium">{label}</span>
      {values.map((val, i) => (
        <span key={i} className={`text-sm ${mono ? 'font-mono text-xs' : ''}`}>
          {val || '—'}
        </span>
      ))}
    </div>
  );
}

export default function ComparePage() {
  const { t, i18n } = useTranslation();
  const lang = i18n.language;
  const [searchParams, setSearchParams] = useSearchParams();
  const [peptides, setPeptides] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [searching, setSearching] = useState(false);

  const slugs = searchParams.get('peptides') || '';

  const loadComparison = useCallback(async () => {
    if (!slugs) {
      setPeptides([]);
      setLoading(false);
      return;
    }
    setLoading(true);
    try {
      const res = await comparePeptides(slugs);
      setPeptides(res.data.peptides || []);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [slugs]);

  useEffect(() => { loadComparison(); }, [loadComparison]);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    setSearching(true);
    try {
      const res = await getPeptides({ query: searchQuery.trim(), limit: 5 });
      setSearchResults(res.data.peptides || []);
    } catch (e) { /* ignore */ }
    setSearching(false);
  };

  const addPeptide = (slug) => {
    const current = slugs ? slugs.split(',') : [];
    if (current.includes(slug) || current.length >= 3) return;
    const updated = [...current, slug].join(',');
    setSearchParams({ peptides: updated });
    setSearchResults([]);
    setSearchQuery('');
  };

  const removePeptide = (slug) => {
    const current = slugs.split(',').filter(s => s !== slug);
    if (current.length > 0) {
      setSearchParams({ peptides: current.join(',') });
    } else {
      setSearchParams({});
    }
  };

  const getVal = (p, path) => {
    const parts = path.split('.');
    let val = p;
    for (const part of parts) { val = val?.[part]; }
    return val;
  };

  const getBilingual = (p, path) => {
    const obj = getVal(p, path);
    if (!obj) return '';
    if (typeof obj === 'string') return obj;
    return obj[lang] || obj.en || '';
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Breadcrumb */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-6">
        <Link to="/encyclopedia" className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-primary transition-colors">
          <ArrowLeft className="w-4 h-4" />
          {t('detail.back_to_encyclopedia')}
        </Link>
      </motion.div>

      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'var(--pdb-font-display)' }}>
          {t('detail.compare_peptides')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground">{t('detail.select_peptides')}</p>
      </motion.div>

      {/* Search to add peptides */}
      {peptides.length < 3 && (
        <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={2} className="mb-8">
          <form onSubmit={handleSearch} className="flex gap-2 max-w-md">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder={t('encyclopedia.search_placeholder')}
                className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-card text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
              />
            </div>
            <Button type="submit" size="sm" className="btn-press rounded-xl" disabled={searching}>
              <Search className="w-4 h-4" />
            </Button>
          </form>

          {/* Search Results */}
          {searchResults.length > 0 && (
            <div className="mt-3 space-y-1 max-w-md">
              {searchResults.map(sr => (
                <button
                  key={sr.slug}
                  onClick={() => addPeptide(sr.slug)}
                  disabled={slugs.includes(sr.slug)}
                  className="w-full flex items-center justify-between p-3 rounded-lg border border-border/50 hover:bg-accent/30 transition-colors text-left disabled:opacity-50"
                >
                  <div>
                    <span className="text-sm font-medium">{sr.name}</span>
                    <Badge variant="secondary" className="text-xs ml-2">{sr.category}</Badge>
                  </div>
                  <span className="text-xs text-primary">{t('detail.add_to_compare')}</span>
                </button>
              ))}
            </div>
          )}
        </motion.div>
      )}

      {/* Selected Peptides Chips */}
      {peptides.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-6">
          {peptides.map(p => (
            <Badge key={p.slug} variant="secondary" className="gap-1.5 py-1.5 px-3 text-sm">
              {p.name}
              <button onClick={() => removePeptide(p.slug)} className="ml-1 hover:text-destructive">
                <X className="w-3.5 h-3.5" />
              </button>
            </Badge>
          ))}
        </div>
      )}

      {/* Comparison Table */}
      {loading ? (
        <div className="space-y-4">
          <Skeleton className="h-10 w-full" />
          <Skeleton className="h-64 w-full" />
        </div>
      ) : peptides.length >= 2 ? (
        <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={3}>
          <Card className="border border-border/50 overflow-x-auto">
            <CardContent className="pt-6">
              {/* Header Row */}
              <div className="grid grid-cols-[180px_1fr_1fr] gap-4 pb-4 border-b-2 border-border mb-2">
                <span className="text-sm font-semibold text-muted-foreground">{t('detail.property')}</span>
                {peptides.map(p => (
                  <Link key={p.slug} to={`/encyclopedia/${p.slug}`} className="hover:text-primary transition-colors">
                    <span className="text-sm font-semibold" style={{ fontFamily: 'var(--pdb-font-display)' }}>{p.name}</span>
                  </Link>
                ))}
              </div>

              <CompareRow label={t('encyclopedia.all_categories')} values={peptides.map(p => p.category)} />
              <CompareRow label={t('detail.manufacturer')} values={peptides.map(p => p.manufacturer)} />
              <CompareRow label="Phase" values={peptides.map(p => p.research_status?.phase)} />
              <CompareRow label={t('detail.fda_approved')} values={peptides.map(p => p.research_status?.fda_approved ? 'Yes' : 'No')} />
              <CompareRow label={t('detail.ema_approved')} values={peptides.map(p => p.research_status?.ema_approved ? 'Yes' : 'No')} />
              <CompareRow label={t('detail.molecular_weight')} values={peptides.map(p => p.molecular_weight)} mono />
              <CompareRow label={t('detail.half_life')} values={peptides.map(p => p.half_life)} />
              <CompareRow label={t('detail.amino_acid_count')} values={peptides.map(p => String(p.amino_acid_count || ''))} />
              <CompareRow label={t('detail.starting_dose')} values={peptides.map(p => p.dosage?.starting_dose)} mono />
              <CompareRow label={t('detail.maintenance_dose')} values={peptides.map(p => p.dosage?.maintenance_dose)} mono />
              <CompareRow label={t('detail.frequency')} values={peptides.map(p => lang === 'de' ? p.dosage?.frequency_de : p.dosage?.frequency_en)} />
              <CompareRow label={t('detail.route')} values={peptides.map(p => lang === 'de' ? p.dosage?.route_de : p.dosage?.route_en)} />
              <CompareRow label={t('detail.storage')} values={peptides.map(p => getBilingual(p, 'storage_conditions'))} />

              {/* Description */}
              <div className="grid grid-cols-[180px_1fr_1fr] gap-4 py-3 border-b border-border/50">
                <span className="text-sm text-muted-foreground font-medium">{lang === 'de' ? 'Beschreibung' : 'Description'}</span>
                {peptides.map((p, i) => (
                  <p key={i} className="text-sm text-muted-foreground line-clamp-4">
                    {getBilingual(p, 'description')}
                  </p>
                ))}
              </div>

              {/* Side Effects Count */}
              <CompareRow
                label={t('detail.side_effects')}
                values={peptides.map(p => `${(p.side_effects || []).length} ${lang === 'de' ? 'bekannt' : 'known'}`)}
              />
              <CompareRow
                label={t('detail.contraindications')}
                values={peptides.map(p => `${(p.contraindications || []).length} ${lang === 'de' ? 'bekannt' : 'known'}`)}
              />
            </CardContent>
          </Card>
        </motion.div>
      ) : (
        <Card className="border border-border/50">
          <CardContent className="p-12 text-center">
            <FlaskConical className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <h3 className="font-semibold mb-1">{t('detail.compare_peptides')}</h3>
            <p className="text-sm text-muted-foreground">{t('detail.select_peptides')}</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

