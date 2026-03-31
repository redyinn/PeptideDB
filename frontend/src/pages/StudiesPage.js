import React, { useState, useEffect, useCallback } from 'react';
import { useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, ExternalLink, TestTube, Filter } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { getTrials } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

export default function StudiesPage() {
  const { t } = useTranslation();
  const [searchParams, setSearchParams] = useSearchParams();
  const [trials, setTrials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState(searchParams.get('q') || 'peptide');
  const [company, setCompany] = useState(searchParams.get('company') || '');
  const [status, setStatus] = useState('');

  const loadTrials = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getTrials({ query, company, status, page_size: 30 });
      setTrials(res.data.trials || []);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [query, company, status]);

  useEffect(() => { loadTrials(); }, [loadTrials]);

  const handleSearch = (e) => {
    e.preventDefault();
    const params = {};
    if (query) params.q = query;
    if (company) params.company = company;
    setSearchParams(params);
    loadTrials();
  };

  const getStatusClass = (s) => {
    const st = (s || '').toLowerCase();
    if (st.includes('recruit')) return 'status-recruiting';
    if (st.includes('complet')) return 'status-completed';
    if (st.includes('active')) return 'status-active';
    return 'status-default';
  };

  const companyQuickFilters = ['Eli Lilly', 'Novo Nordisk', 'Pfizer', 'Sanofi'];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
          {t('studies.title')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground max-w-[64ch]">
          {t('studies.subtitle')}
        </p>
      </motion.div>

      {/* Filters */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="mb-8 space-y-4">
        <div className="flex flex-col sm:flex-row gap-3">
          <form onSubmit={handleSearch} className="flex gap-2 flex-1 max-w-lg">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <input
                data-testid="studies-search"
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder={t('studies.search_placeholder')}
                className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
              />
            </div>
            <Button type="submit" size="sm" className="btn-press rounded-xl">
              <Search className="w-4 h-4" />
            </Button>
          </form>

          <Select value={status || 'all'} onValueChange={(val) => setStatus(val === 'all' ? '' : val)}>
            <SelectTrigger className="w-full sm:w-[180px] rounded-xl" data-testid="status-filter">
              <SelectValue placeholder={t('studies.all_statuses')} />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">{t('studies.all_statuses')}</SelectItem>
              <SelectItem value="recruiting">{t('studies.recruiting')}</SelectItem>
              <SelectItem value="completed">{t('studies.completed')}</SelectItem>
              <SelectItem value="active">{t('studies.active')}</SelectItem>
              <SelectItem value="not_yet">{t('studies.not_yet')}</SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* Company quick filters */}
        <div className="flex flex-wrap gap-2">
          <span className="text-xs text-muted-foreground flex items-center gap-1 mr-1">
            <Filter className="w-3 h-3" /> {t('studies.filter_company')}:
          </span>
          <Badge
            variant={company === '' ? 'default' : 'outline'}
            className="cursor-pointer text-xs"
            onClick={() => setCompany('')}
          >
            {t('studies.all_companies')}
          </Badge>
          {companyQuickFilters.map(c => (
            <Badge
              key={c}
              variant={company === c ? 'default' : 'outline'}
              className="cursor-pointer text-xs"
              onClick={() => setCompany(company === c ? '' : c)}
              data-testid={`company-filter-${c.toLowerCase().replace(/\s/g, '-')}`}
            >
              {c}
            </Badge>
          ))}
        </div>
      </motion.div>

      {/* Results */}
      <div className="space-y-3" data-testid="studies-table">
        {loading ? (
          Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="p-4 rounded-xl border border-border/50">
              <Skeleton className="h-5 w-full mb-2" />
              <Skeleton className="h-4 w-2/3" />
            </div>
          ))
        ) : trials.length > 0 ? (
          trials.map((trial, i) => (
            <motion.a
              key={trial.nct_id || i}
              href={trial.url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-start gap-4 p-4 rounded-xl border border-border/50 hover:border-primary/20 hover:bg-accent/30 transition-colors group"
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true }}
              variants={fadeUp}
              custom={i % 8}
              data-testid={`study-row-${i}`}
            >
              <div className="w-10 h-10 rounded-lg bg-accent flex items-center justify-center shrink-0">
                <TestTube className="w-5 h-5 text-primary" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                  {trial.title}
                </p>
                <div className="mt-2 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
                  <span className="font-mono">{trial.nct_id}</span>
                  <span>|</span>
                  <span className="font-medium">{trial.sponsor}</span>
                  <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${getStatusClass(trial.status)}`}>
                    {trial.status?.replace(/_/g, ' ')}
                  </span>
                  {trial.phase !== 'N/A' && (
                    <Badge variant="outline" className="text-xs">{trial.phase}</Badge>
                  )}
                </div>
                {trial.conditions && trial.conditions.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-1">
                    {trial.conditions.slice(0, 3).map((c, ci) => (
                      <Badge key={ci} variant="secondary" className="text-xs">{c}</Badge>
                    ))}
                    {trial.conditions.length > 3 && (
                      <Badge variant="secondary" className="text-xs">+{trial.conditions.length - 3}</Badge>
                    )}
                  </div>
                )}
              </div>
              <ExternalLink className="w-4 h-4 text-muted-foreground group-hover:text-primary shrink-0 mt-1" />
            </motion.a>
          ))
        ) : (
          <Card className="border border-border/50" data-testid="empty-state">
            <CardContent className="p-12 text-center">
              <TestTube className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
              <p className="text-sm text-muted-foreground">{t('studies.no_results')}</p>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
