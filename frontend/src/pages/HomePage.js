import React, { useState, useEffect, useCallback } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, ArrowRight, FlaskConical, BookOpen, TestTube, Newspaper, ExternalLink, TrendingUp } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { getPeptides, getTrials, getPapers, getStats, seedPeptides, getSeedStatus } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

function StatCard({ icon: Icon, label, value, loading }) {
  return (
    <Card className="card-hover border border-border/50">
      <CardContent className="p-5 flex items-center gap-4">
        <div className="w-11 h-11 rounded-xl bg-accent flex items-center justify-center shrink-0">
          <Icon className="w-5 h-5 text-primary" />
        </div>
        <div>
          {loading ? (
            <Skeleton className="h-7 w-16 mb-1" />
          ) : (
            <p className="text-2xl font-semibold tabular-nums" style={{ fontFamily: 'Space Grotesk' }}>{value}</p>
          )}
          <p className="text-xs text-muted-foreground">{label}</p>
        </div>
      </CardContent>
    </Card>
  );
}

export default function HomePage() {
  const { t, i18n } = useTranslation();
  const navigate = useNavigate();
  const lang = i18n.language;
  const [searchQuery, setSearchQuery] = useState('');
  const [peptides, setPeptides] = useState([]);
  const [trials, setTrials] = useState([]);
  const [papers, setPapers] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [seeding, setSeeding] = useState(false);

  const loadData = useCallback(async () => {
    setLoading(true);
    try {
      const [pepRes, trialRes, paperRes, statsRes] = await Promise.allSettled([
        getPeptides({ limit: 6 }),
        getTrials({ query: 'peptide', page_size: 5 }),
        getPapers({ query: 'peptide therapeutics', max_results: 5, sort: 'date' }),
        getStats()
      ]);
      if (pepRes.status === 'fulfilled') setPeptides(pepRes.value.data.peptides || []);
      if (trialRes.status === 'fulfilled') setTrials(trialRes.value.data.trials || []);
      if (paperRes.status === 'fulfilled') setPapers(paperRes.value.data.papers || []);
      if (statsRes.status === 'fulfilled') setStats(statsRes.value.data);

      // If no peptides, auto-seed
      if (pepRes.status === 'fulfilled' && (pepRes.value.data.peptides || []).length === 0) {
        setSeeding(true);
        try {
          await seedPeptides();
          // Poll for status
          const pollInterval = setInterval(async () => {
            try {
              const statusRes = await getSeedStatus();
              if (statusRes.data.seeded > 0) {
                const freshPeptides = await getPeptides({ limit: 6 });
                setPeptides(freshPeptides.data.peptides || []);
                const freshStats = await getStats();
                setStats(freshStats.data);
              }
              if (statusRes.data.seeded >= 5) {
                clearInterval(pollInterval);
                setSeeding(false);
              }
            } catch (e) { /* ignore */ }
          }, 8000);
          // Stop after 3 minutes
          setTimeout(() => { clearInterval(pollInterval); setSeeding(false); }, 180000);
        } catch (e) { setSeeding(false); }
      }
    } catch (e) { console.error(e); }
    setLoading(false);
  }, []);

  useEffect(() => { loadData(); }, [loadData]);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) navigate(`/encyclopedia?q=${encodeURIComponent(searchQuery.trim())}`);
  };

  const getStatusClass = (status) => {
    const s = (status || '').toLowerCase();
    if (s.includes('recruit')) return 'status-recruiting';
    if (s.includes('complet')) return 'status-completed';
    if (s.includes('active')) return 'status-active';
    return 'status-default';
  };

  return (
    <div>
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="hero-gradient absolute inset-0" />
        <div className="noise relative" />
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-20 lg:pt-24 lg:pb-28">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
            {/* Left: Copy + Search */}
            <motion.div
              className="lg:col-span-7"
              initial="hidden"
              animate="visible"
              variants={fadeUp}
              custom={0}
            >
              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight text-foreground leading-tight" style={{ fontFamily: 'Space Grotesk' }}>
                {t('home.hero_title')}
              </h1>
              <p className="mt-5 text-base md:text-lg text-muted-foreground max-w-[56ch] leading-7">
                {t('home.hero_subtitle')}
              </p>

              {/* Search */}
              <form onSubmit={handleSearch} className="mt-8 flex gap-2 max-w-xl">
                <div className="relative flex-1">
                  <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4.5 h-4.5 text-muted-foreground" />
                  <input
                    data-testid="hero-search-input"
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder={t('home.search_placeholder')}
                    className="w-full pl-11 pr-4 py-3 rounded-xl border border-border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
                  />
                </div>
                <Button type="submit" data-testid="hero-search-submit" className="btn-press px-5 rounded-xl">
                  <Search className="w-4 h-4" />
                </Button>
              </form>

              <div className="mt-6 flex flex-wrap gap-3">
                <Button asChild variant="default" className="btn-press rounded-xl gap-2">
                  <Link to="/encyclopedia">
                    {t('home.explore_encyclopedia')} <ArrowRight className="w-4 h-4" />
                  </Link>
                </Button>
                <Button asChild variant="outline" className="btn-press rounded-xl gap-2">
                  <Link to="/studies?company=Eli+Lilly">
                    {t('home.track_studies')}
                  </Link>
                </Button>
              </div>
            </motion.div>

            {/* Right: Live Signals */}
            <motion.div
              className="lg:col-span-5 space-y-4"
              initial="hidden"
              animate="visible"
              variants={fadeUp}
              custom={2}
            >
              <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider mb-3">
                {t('home.live_signals')}
              </p>

              {/* Quick stats */}
              <div className="grid grid-cols-2 gap-3">
                <StatCard icon={FlaskConical} label={t('home.stats_peptides')} value={stats?.peptides_in_db || 0} loading={loading} />
                <StatCard icon={TestTube} label={t('home.stats_trials')} value={trials.length || '...'} loading={loading} />
                <StatCard icon={BookOpen} label={t('home.stats_papers')} value={papers.length || '...'} loading={loading} />
                <StatCard icon={TrendingUp} label={t('home.stats_sources')} value={stats?.data_sources?.length || 3} loading={loading} />
              </div>

              {seeding && (
                <Card className="border-primary/20 bg-accent/50">
                  <CardContent className="p-4 flex items-center gap-3">
                    <div className="w-5 h-5 border-2 border-primary border-t-transparent rounded-full animate-spin" />
                    <span className="text-sm text-primary font-medium">{t('home.generating')}</span>
                  </CardContent>
                </Card>
              )}
            </motion.div>
          </div>
        </div>
      </section>

      {/* Featured Peptides */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="flex items-center justify-between mb-8">
          <motion.h2
            className="text-xl md:text-2xl font-semibold tracking-tight"
            style={{ fontFamily: 'Space Grotesk' }}
            initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp}
          >
            {t('home.featured_peptides')}
          </motion.h2>
          <Link to="/encyclopedia" className="text-sm text-primary font-medium hover:underline flex items-center gap-1">
            {t('home.view_all')} <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {loading ? (
            Array.from({ length: 6 }).map((_, i) => (
              <Card key={i} className="border border-border/50">
                <CardContent className="p-5 space-y-3">
                  <Skeleton className="h-5 w-32" />
                  <Skeleton className="h-4 w-24" />
                  <Skeleton className="h-16 w-full" />
                </CardContent>
              </Card>
            ))
          ) : peptides.length > 0 ? (
            peptides.map((p, i) => (
              <motion.div key={p.slug || i} initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp} custom={i}>
                <Link to={`/encyclopedia/${p.slug}`}>
                  <Card className="card-hover border border-border/50 h-full" data-testid={`peptide-card-${p.slug}`}>
                    <CardContent className="p-5">
                      <div className="flex items-start justify-between mb-2">
                        <h3 className="font-semibold text-base" style={{ fontFamily: 'Space Grotesk' }}>{p.name}</h3>
                        <Badge variant="secondary" className="text-xs shrink-0">{p.category || 'Peptide'}</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground line-clamp-3 leading-relaxed">
                        {p.description?.[lang] || p.description?.en || ''}
                      </p>
                      {p.research_status && (
                        <div className="mt-3 flex items-center gap-2">
                          <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${p.research_status?.fda_approved ? 'status-completed' : 'status-active'}`}>
                            {p.research_status?.phase || 'Research'}
                          </span>
                        </div>
                      )}
                    </CardContent>
                  </Card>
                </Link>
              </motion.div>
            ))
          ) : (
            <Card className="col-span-full border border-border/50">
              <CardContent className="p-8 text-center">
                <FlaskConical className="w-10 h-10 text-muted-foreground mx-auto mb-3" />
                <p className="text-sm text-muted-foreground">{t('encyclopedia.no_results')}</p>
              </CardContent>
            </Card>
          )}
        </div>
      </section>

      {/* Latest Studies */}
      <section className="bg-white border-y border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="flex items-center justify-between mb-8">
            <motion.h2
              className="text-xl md:text-2xl font-semibold tracking-tight"
              style={{ fontFamily: 'Space Grotesk' }}
              initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp}
            >
              {t('home.latest_studies')}
            </motion.h2>
            <Link to="/studies" className="text-sm text-primary font-medium hover:underline flex items-center gap-1">
              {t('home.view_all')} <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          <div className="space-y-3">
            {loading ? (
              Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="flex items-center gap-4 p-4 rounded-xl border border-border/50">
                  <Skeleton className="h-4 w-full" />
                </div>
              ))
            ) : trials.length > 0 ? (
              trials.slice(0, 5).map((trial, i) => (
                <motion.a
                  key={trial.nct_id || i}
                  href={trial.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-start gap-4 p-4 rounded-xl border border-border/50 hover:border-primary/20 hover:bg-accent/30 transition-colors group"
                  initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp} custom={i}
                  data-testid={`trial-item-${i}`}
                >
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors truncate">
                      {trial.title}
                    </p>
                    <div className="mt-1.5 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
                      <span className="font-mono">{trial.nct_id}</span>
                      <span>|</span>
                      <span>{trial.sponsor}</span>
                      <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${getStatusClass(trial.status)}`}>
                        {trial.status?.replace(/_/g, ' ')}
                      </span>
                    </div>
                  </div>
                  <ExternalLink className="w-4 h-4 text-muted-foreground group-hover:text-primary shrink-0 mt-1" />
                </motion.a>
              ))
            ) : (
              <p className="text-sm text-muted-foreground text-center py-8">{t('studies.no_results')}</p>
            )}
          </div>
        </div>
      </section>

      {/* Recent Papers */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="flex items-center justify-between mb-8">
          <motion.h2
            className="text-xl md:text-2xl font-semibold tracking-tight"
            style={{ fontFamily: 'Space Grotesk' }}
            initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp}
          >
            {t('home.recent_papers')}
          </motion.h2>
          <Link to="/papers" className="text-sm text-primary font-medium hover:underline flex items-center gap-1">
            {t('home.view_all')} <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {loading ? (
            Array.from({ length: 3 }).map((_, i) => (
              <Card key={i} className="border border-border/50">
                <CardContent className="p-5 space-y-3">
                  <Skeleton className="h-5 w-full" />
                  <Skeleton className="h-4 w-3/4" />
                  <Skeleton className="h-4 w-1/2" />
                </CardContent>
              </Card>
            ))
          ) : papers.length > 0 ? (
            papers.slice(0, 3).map((paper, i) => (
              <motion.a
                key={paper.pmid || i}
                href={paper.url}
                target="_blank"
                rel="noopener noreferrer"
                initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp} custom={i}
              >
                <Card className="card-hover border border-border/50 h-full" data-testid={`paper-card-${i}`}>
                  <CardContent className="p-5">
                    <p className="text-sm font-medium text-foreground line-clamp-2 leading-relaxed mb-2">
                      {paper.title}
                    </p>
                    <p className="text-xs text-muted-foreground">
                      {paper.authors?.slice(0, 2).join(', ')}{paper.authors?.length > 2 ? ' et al.' : ''}
                    </p>
                    <div className="mt-3 flex items-center gap-2">
                      <Badge variant="outline" className="text-xs">{paper.journal}</Badge>
                      <span className="text-xs text-muted-foreground">{paper.pub_date}</span>
                    </div>
                  </CardContent>
                </Card>
              </motion.a>
            ))
          ) : null}
        </div>
      </section>
    </div>
  );
}
