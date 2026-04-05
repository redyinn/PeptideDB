import React, { useState, useEffect, useCallback } from 'react';
import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, ExternalLink, BookOpen } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { getPapers } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

export default function PapersPage() {
  const { t } = useTranslation();
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState('peptide therapeutics');
  const [sort, setSort] = useState('relevance');
  const [totalAvailable, setTotalAvailable] = useState(0);

  const loadPapers = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getPapers({ query, sort, max_results: 25 });
      setPapers(res.data.papers || []);
      setTotalAvailable(res.data.total_available || 0);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [query, sort]);

  useEffect(() => { loadPapers(); }, [loadPapers]);

  const handleSearch = (e) => {
    e.preventDefault();
    loadPapers();
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <Helmet>
        <title>Research Papers — PeptideDB</title>
        <meta name="description" content="Search PubMed research papers on peptide therapeutics. Sort by relevance or date. Access full citations and DOI links." />
      </Helmet>
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
          {t('papers.title')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground max-w-[64ch]">
          {t('papers.subtitle')}
        </p>
        {totalAvailable > 0 && (
          <p className="mt-1 text-xs text-muted-foreground tabular-nums">
            {totalAvailable.toLocaleString()} {t('papers.title').toLowerCase()} available
          </p>
        )}
      </motion.div>

      {/* Filters */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="flex flex-col sm:flex-row gap-3 mb-8">
        <form onSubmit={handleSearch} className="flex gap-2 flex-1 max-w-lg">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <input
              data-testid="papers-search"
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={t('papers.search_placeholder')}
              className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
            />
          </div>
          <Button type="submit" size="sm" className="btn-press rounded-xl">
            <Search className="w-4 h-4" />
          </Button>
        </form>

        <Select value={sort} onValueChange={setSort}>
          <SelectTrigger className="w-full sm:w-[200px] rounded-xl" data-testid="sort-select">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="relevance">{t('papers.sort_relevance')}</SelectItem>
            <SelectItem value="date">{t('papers.sort_date')}</SelectItem>
          </SelectContent>
        </Select>
      </motion.div>

      {/* Results */}
      <div className="space-y-3" data-testid="papers-table">
        {loading ? (
          Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="p-4 rounded-xl border border-border/50">
              <Skeleton className="h-5 w-full mb-2" />
              <Skeleton className="h-4 w-2/3 mb-1" />
              <Skeleton className="h-4 w-1/3" />
            </div>
          ))
        ) : papers.length > 0 ? (
          papers.map((paper, i) => (
            <motion.a
              key={paper.pmid || i}
              href={paper.url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-start gap-4 p-4 rounded-xl border border-border/50 hover:border-primary/20 hover:bg-accent/30 transition-colors group"
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true }}
              variants={fadeUp}
              custom={i % 8}
              data-testid={`paper-row-${i}`}
            >
              <div className="w-10 h-10 rounded-lg bg-accent flex items-center justify-center shrink-0">
                <BookOpen className="w-5 h-5 text-primary" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors leading-relaxed">
                  {paper.title}
                </p>
                <p className="text-xs text-muted-foreground mt-1.5">
                  {paper.authors?.slice(0, 3).join(', ')}{paper.authors?.length > 3 ? ' et al.' : ''}
                </p>
                <div className="mt-2 flex flex-wrap items-center gap-2">
                  <Badge variant="outline" className="text-xs">{paper.journal}</Badge>
                  <span className="text-xs text-muted-foreground">{paper.pub_date}</span>
                  <span className="text-xs font-mono text-muted-foreground">PMID: {paper.pmid}</span>
                </div>
              </div>
              <ExternalLink className="w-4 h-4 text-muted-foreground group-hover:text-primary shrink-0 mt-1" />
            </motion.a>
          ))
        ) : (
          <Card className="border border-border/50" data-testid="empty-state">
            <CardContent className="p-12 text-center">
              <BookOpen className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
              <p className="text-sm text-muted-foreground">{t('papers.no_results')}</p>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
