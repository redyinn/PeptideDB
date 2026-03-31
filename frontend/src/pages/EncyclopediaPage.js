import React, { useState, useEffect, useCallback } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, FlaskConical, Sparkles, Loader2 } from 'lucide-react';
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

export default function EncyclopediaPage() {
  const { t, i18n } = useTranslation();
  const lang = i18n.language;
  const [searchParams, setSearchParams] = useSearchParams();
  const [peptides, setPeptides] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [generating, setGenerating] = useState(false);
  const [query, setQuery] = useState(searchParams.get('q') || '');
  const [category, setCategory] = useState('');
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const loadPeptides = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getPeptides({ query, category, page, limit: 20 });
      setPeptides(res.data.peptides || []);
      setTotalPages(res.data.pages || 1);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [query, category, page]);

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
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
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
              className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
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
                <Link to={`/encyclopedia/${p.slug}`}>
                  <Card className="card-hover border border-border/50 h-full" data-testid={`peptide-card-${p.slug}`}>
                    <CardContent className="p-5">
                      <div className="flex items-start justify-between mb-2">
                        <h3 className="font-semibold text-base" style={{ fontFamily: 'Space Grotesk' }}>{p.name}</h3>
                        <Badge variant="secondary" className="text-xs shrink-0 ml-2">{p.category || 'Peptide'}</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground line-clamp-3 leading-relaxed">
                        {p.description?.[lang] || p.description?.en || ''}
                      </p>
                      {p.research_status && (
                        <div className="mt-3 flex flex-wrap items-center gap-2">
                          <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${p.research_status?.fda_approved ? 'status-completed' : 'status-active'}`}>
                            {p.research_status?.phase || 'Research'}
                          </span>
                          {p.manufacturer && (
                            <span className="text-xs text-muted-foreground">{p.manufacturer}</span>
                          )}
                        </div>
                      )}
                    </CardContent>
                  </Card>
                </Link>
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
    </div>
  );
}
