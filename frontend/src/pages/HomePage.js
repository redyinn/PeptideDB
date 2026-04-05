import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Helmet } from 'react-helmet-async';
import { Link, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, ArrowRight, FlaskConical, BookOpen, TestTube, Newspaper, ExternalLink, TrendingUp } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { SplineScene } from '../components/ui/splite';
import { Spotlight } from '../components/ui/spotlight';
import { LampContainer } from '../components/ui/lamp';
import AnimatedShaderBackground from '../components/ui/animated-shader-background';
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
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [suggestLoading, setSuggestLoading] = useState(false);
  const searchRef = useRef(null);
  const debounceRef = useRef(null);
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

  // Close dropdown on outside click
  useEffect(() => {
    const handler = (e) => { if (searchRef.current && !searchRef.current.contains(e.target)) setShowSuggestions(false); };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  const getStatusClass = (status) => {
    const s = (status || '').toLowerCase();
    if (s.includes('recruit')) return 'status-recruiting';
    if (s.includes('complet')) return 'status-completed';
    if (s.includes('active')) return 'status-active';
    return 'status-default';
  };

  return (
    <div>
      <Helmet>
        <title>PeptideDB — Peptide Research Database</title>
        <meta name="description" content="Explore 48+ peptide therapeutics with clinical trial data, PubMed research papers, dosage information, and mechanisms of action. BPC-157, Semaglutide, Tirzepatide and more." />
      </Helmet>
      {/* Hero Section — Lamp + Shader Background */}
      <div className="relative">
        <AnimatedShaderBackground />
        {/* dark overlay so lamp glow stays readable */}
        <div className="absolute inset-0 bg-black/50 z-[1]" />
      <LampContainer className="bg-transparent relative z-10">
        <motion.h1
          initial={{ opacity: 0.5, y: 100 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3, duration: 0.8, ease: "easeInOut" }}
          className="bg-gradient-to-br from-slate-100 to-slate-400 py-2 bg-clip-text text-center text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight text-transparent"
          style={{ fontFamily: 'Space Grotesk' }}
        >
          {t('home.hero_title')}
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 60 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5, duration: 0.7, ease: "easeInOut" }}
          className="mt-4 text-slate-400 text-base md:text-lg max-w-[52ch] text-center leading-7"
        >
          {t('home.hero_subtitle')}
        </motion.p>
        <motion.div
          ref={searchRef}
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.65, duration: 0.7, ease: "easeInOut" }}
          className="mt-8 w-full max-w-xl relative"
        >
          <form onSubmit={handleSearch} className="flex gap-2">
            <div className="relative flex-1">
              <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
              {suggestLoading && (
                <div className="absolute right-3.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 border border-cyan-500 border-t-transparent rounded-full animate-spin" />
              )}
              <input
                data-testid="hero-search-input"
                type="text"
                value={searchQuery}
                onChange={handleSearchChange}
                onFocus={() => suggestions.length > 0 && setShowSuggestions(true)}
                placeholder={t('home.search_placeholder')}
                className="w-full pl-11 pr-4 py-3 rounded-xl border border-slate-700 bg-slate-900 text-slate-200 text-sm placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/40 focus:border-cyan-500/60 transition-colors"
                autoComplete="off"
              />
            </div>
            <Button type="submit" data-testid="hero-search-submit" className="btn-press px-5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950">
              <Search className="w-4 h-4" />
            </Button>
          </form>

          {/* Autocomplete Dropdown */}
          {showSuggestions && suggestions.length > 0 && (
            <div className="absolute top-full mt-2 left-0 right-12 bg-slate-900 border border-slate-700 rounded-xl shadow-2xl z-50 overflow-hidden">
              {suggestions.map((p) => (
                <button
                  key={p.slug}
                  onMouseDown={() => { setShowSuggestions(false); navigate(`/encyclopedia/${p.slug}`); }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 hover:bg-slate-800 transition-colors text-left"
                >
                  <FlaskConical className="w-4 h-4 text-cyan-500 shrink-0" />
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-slate-200 truncate">{p.name}</p>
                    <p className="text-xs text-slate-500 truncate">{p.category}</p>
                  </div>
                  <ArrowRight className="w-3.5 h-3.5 text-slate-600 shrink-0" />
                </button>
              ))}
              <button
                onMouseDown={handleSearch}
                className="w-full flex items-center gap-2 px-4 py-2.5 border-t border-slate-800 text-xs text-cyan-400 hover:bg-slate-800 transition-colors"
              >
                <Search className="w-3.5 h-3.5" />
                {lang === 'de' ? `Alle Ergebnisse für „${searchQuery}" anzeigen` : `Show all results for "${searchQuery}"`}
              </button>
            </div>
          )}
        </motion.div>
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.8, duration: 0.6, ease: "easeInOut" }}
          className="mt-6 flex flex-wrap justify-center gap-3"
        >
          <Button asChild variant="default" className="btn-press rounded-xl gap-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 border-0">
            <Link to="/encyclopedia">
              {t('home.explore_encyclopedia')} <ArrowRight className="w-4 h-4" />
            </Link>
          </Button>
          <Button asChild variant="outline" className="btn-press rounded-xl gap-2 border-slate-700 text-slate-300 hover:bg-slate-800 hover:text-white">
            <Link to="/studies?company=Eli+Lilly">
              {t('home.track_studies')}
            </Link>
          </Button>
        </motion.div>
      </LampContainer>
      </div>

      {/* Stats Bar */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider mb-4">
          {t('home.live_signals')}
        </p>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <StatCard icon={FlaskConical} label={t('home.stats_peptides')} value={stats?.peptides_in_db || 0} loading={loading} />
          <StatCard icon={TestTube} label={t('home.stats_trials')} value={trials.length || '...'} loading={loading} />
          <StatCard icon={BookOpen} label={t('home.stats_papers')} value={papers.length || '...'} loading={loading} />
          <StatCard icon={TrendingUp} label={t('home.stats_sources')} value={stats?.data_sources?.length || 3} loading={loading} />
        </div>
        {seeding && (
          <Card className="mt-3 border-primary/20 bg-accent/50">
            <CardContent className="p-4 flex items-center gap-3">
              <div className="w-5 h-5 border-2 border-primary border-t-transparent rounded-full animate-spin" />
              <span className="text-sm text-primary font-medium">{t('home.generating')}</span>
            </CardContent>
          </Card>
        )}
      </section>

      {/* 3D Interactive Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <Card className="w-full h-[420px] bg-black/[0.96] relative overflow-hidden border-border/30">
          <Spotlight className="-top-40 left-0 md:left-60 md:-top-20" fill="white" />
          <div className="flex h-full">
            <div className="flex-1 p-8 relative z-10 flex flex-col justify-center">
              <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={0}>
                <h2
                  className="text-3xl md:text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-neutral-50 to-neutral-400"
                  style={{ fontFamily: 'Space Grotesk' }}
                >
                  Explore Peptide Science in 3D
                </h2>
                <p className="mt-4 text-neutral-400 max-w-sm text-sm leading-relaxed">
                  Visualize molecular structures and research insights in an interactive 3D environment.
                </p>
                <Button asChild variant="outline" className="mt-6 rounded-xl border-neutral-700 text-neutral-200 hover:bg-neutral-800 hover:text-white w-fit">
                  <a href="/encyclopedia">Browse Encyclopedia</a>
                </Button>
              </motion.div>
            </div>
            <div className="flex-1 relative hidden md:block">
              <SplineScene
                scene="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"
                className="w-full h-full"
              />
            </div>
          </div>
        </Card>
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
      <section className="border-y border-border/20">
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
                  className="flex items-start gap-4 p-4 rounded-xl border border-border/20 hover:border-primary/30 hover:bg-accent/10 transition-colors group"
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
                <div className="card-hover rounded-xl border border-border/20 h-full" data-testid={`paper-card-${i}`}>
                  <div className="p-5">
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
                  </div>
                </div>
              </motion.a>
            ))
          ) : null}
        </div>
      </section>
    </div>
  );
}
