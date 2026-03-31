import React, { useState, useEffect, useCallback } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { ArrowLeft, ExternalLink, Shield, Pill, Activity, AlertTriangle, Beaker, FlaskConical } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Skeleton } from '../components/ui/skeleton';
import { getPeptideDetail, getTrials, getPapers } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

function InfoRow({ label, value, mono = false }) {
  if (!value) return null;
  return (
    <div className="flex items-start py-2.5 border-b border-border/50 last:border-0">
      <span className="text-sm text-muted-foreground w-40 shrink-0">{label}</span>
      <span className={`text-sm font-medium ${mono ? 'font-mono text-xs' : ''}`}>{value}</span>
    </div>
  );
}

export default function PeptideDetailPage() {
  const { slug } = useParams();
  const { t, i18n } = useTranslation();
  const lang = i18n.language;
  const [peptide, setPeptide] = useState(null);
  const [trials, setTrials] = useState([]);
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('overview');

  const loadData = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getPeptideDetail(slug);
      setPeptide(res.data);
      
      // Fetch related trials and papers
      const name = res.data.name || slug;
      const [trialRes, paperRes] = await Promise.allSettled([
        getTrials({ query: name, page_size: 10 }),
        getPapers({ query: name, max_results: 10 })
      ]);
      if (trialRes.status === 'fulfilled') setTrials(trialRes.value.data.trials || []);
      if (paperRes.status === 'fulfilled') setPapers(paperRes.value.data.papers || []);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, [slug]);

  useEffect(() => { loadData(); }, [loadData]);

  const getStatusClass = (status) => {
    const s = (status || '').toLowerCase();
    if (s.includes('recruit')) return 'status-recruiting';
    if (s.includes('complet')) return 'status-completed';
    if (s.includes('active')) return 'status-active';
    return 'status-default';
  };

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <Skeleton className="h-8 w-48 mb-4" />
        <Skeleton className="h-12 w-96 mb-6" />
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 space-y-4">
            <Skeleton className="h-64 w-full" />
            <Skeleton className="h-40 w-full" />
          </div>
          <Skeleton className="h-80 w-full" />
        </div>
      </div>
    );
  }

  if (!peptide) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
        <FlaskConical className="w-16 h-16 text-muted-foreground mx-auto mb-4" />
        <h2 className="text-xl font-semibold mb-2">{t('detail.not_found')}</h2>
        <Button asChild variant="outline" className="rounded-xl mt-4">
          <Link to="/encyclopedia">{t('detail.back_to_encyclopedia')}</Link>
        </Button>
      </div>
    );
  }

  const p = peptide;

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
        <div className="flex flex-wrap items-start gap-3 mb-3">
          <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
            {p.name}
          </h1>
          <div className="flex flex-wrap gap-2 mt-1">
            <Badge variant="secondary">{p.category || 'Peptide'}</Badge>
            {p.research_status?.fda_approved && <Badge className="bg-green-100 text-green-700 hover:bg-green-100">FDA</Badge>}
            {p.research_status?.ema_approved && <Badge className="bg-blue-100 text-blue-700 hover:bg-blue-100">EMA</Badge>}
          </div>
        </div>
        <p className="text-base text-muted-foreground max-w-[72ch] leading-7">
          {p.description?.[lang] || p.description?.en || ''}
        </p>
      </motion.div>

      {/* Tabs */}
      <Tabs value={activeTab} onValueChange={setActiveTab} data-testid="peptide-detail-tabs">
        <TabsList className="mb-6 bg-secondary/50 rounded-xl p-1">
          <TabsTrigger value="overview" className="rounded-lg text-sm">{t('detail.overview')}</TabsTrigger>
          <TabsTrigger value="mechanism" className="rounded-lg text-sm">{t('detail.mechanism')}</TabsTrigger>
          <TabsTrigger value="dosage" className="rounded-lg text-sm">{t('detail.dosage')}</TabsTrigger>
          <TabsTrigger value="safety" className="rounded-lg text-sm">{t('detail.safety')}</TabsTrigger>
          <TabsTrigger value="studies" className="rounded-lg text-sm">{t('detail.studies')} ({trials.length})</TabsTrigger>
          <TabsTrigger value="papers" className="rounded-lg text-sm">{t('detail.papers')} ({papers.length})</TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2 space-y-6">
              {/* Indications */}
              <Card className="border border-border/50">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <Activity className="w-5 h-5 text-primary" />
                    {t('detail.indications')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {(p.indications || []).map((ind, i) => (
                      <div key={i} className="p-3 rounded-lg bg-secondary/30">
                        <h4 className="text-sm font-semibold">{lang === 'de' ? ind.condition_de : ind.condition_en}</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          {lang === 'de' ? ind.description_de : ind.description_en}
                        </p>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Benefits */}
              <Card className="border border-border/50">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <Shield className="w-5 h-5 text-primary" />
                    {t('detail.benefits')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {(p.benefits || []).map((b, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm">
                        <span className="w-1.5 h-1.5 rounded-full bg-primary mt-2 shrink-0" />
                        <span>{lang === 'de' ? b.benefit_de : b.benefit_en}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            </div>

            {/* Sidebar */}
            <div className="space-y-6">
              <Card className="border border-border/50">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg">{t('detail.research_status')}</CardTitle>
                </CardHeader>
                <CardContent className="space-y-0">
                  <InfoRow label={t('detail.manufacturer')} value={p.manufacturer} />
                  <InfoRow label="Phase" value={p.research_status?.phase} />
                  <InfoRow label={t('detail.fda_approved')} value={p.research_status?.fda_approved ? t('common.yes') : t('common.no')} />
                  <InfoRow label={t('detail.ema_approved')} value={p.research_status?.ema_approved ? t('common.yes') : t('common.no')} />
                  <InfoRow label={t('detail.molecular_weight')} value={p.molecular_weight} mono />
                  <InfoRow label={t('detail.half_life')} value={p.half_life} />
                  <InfoRow label={t('detail.amino_acid_count')} value={p.amino_acid_count} />
                </CardContent>
              </Card>

              {p.drug_interactions && p.drug_interactions.length > 0 && (
                <Card className="border border-border/50">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-lg flex items-center gap-2">
                      <Pill className="w-5 h-5 text-primary" />
                      {t('detail.drug_interactions')}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <ul className="space-y-1.5">
                      {p.drug_interactions.map((di, i) => (
                        <li key={i} className="text-sm text-muted-foreground flex items-start gap-2">
                          <span className="w-1 h-1 rounded-full bg-muted-foreground mt-2 shrink-0" />
                          {di}
                        </li>
                      ))}
                    </ul>
                  </CardContent>
                </Card>
              )}
            </div>
          </div>
        </TabsContent>

        {/* Mechanism Tab */}
        <TabsContent value="mechanism">
          <Card className="border border-border/50">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Beaker className="w-5 h-5 text-primary" />
                {t('detail.mechanism')}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-7 max-w-[72ch]">
                {p.mechanism_of_action?.[lang] || p.mechanism_of_action?.en || 'No mechanism data available.'}
              </p>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Dosage Tab */}
        <TabsContent value="dosage">
          <Card className="border border-border/50">
            <CardContent className="pt-6">
              {p.dosage ? (
                <div className="space-y-0">
                  <InfoRow label={t('detail.starting_dose')} value={p.dosage.starting_dose} mono />
                  <InfoRow label={t('detail.maintenance_dose')} value={p.dosage.maintenance_dose} mono />
                  <InfoRow label={t('detail.frequency')} value={lang === 'de' ? p.dosage.frequency_de : p.dosage.frequency_en} />
                  <InfoRow label={t('detail.route')} value={lang === 'de' ? p.dosage.route_de : p.dosage.route_en} />
                  <InfoRow label={t('detail.notes')} value={lang === 'de' ? p.dosage.notes_de : p.dosage.notes_en} />
                  {p.storage_conditions && (
                    <InfoRow label={t('detail.storage')} value={lang === 'de' ? p.storage_conditions.de : p.storage_conditions.en} />
                  )}
                </div>
              ) : (
                <p className="text-sm text-muted-foreground">No dosage data available.</p>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        {/* Safety Tab */}
        <TabsContent value="safety">
          <div className="space-y-6">
            {/* Side Effects */}
            <Card className="border border-border/50">
              <CardHeader className="pb-3">
                <CardTitle className="flex items-center gap-2">
                  <AlertTriangle className="w-5 h-5 text-amber-500" />
                  {t('detail.side_effects')}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {(p.side_effects || []).map((se, i) => (
                    <div key={i} className="p-3 rounded-lg border border-border/50">
                      <div className="flex items-center gap-2 mb-1">
                        <h4 className="text-sm font-semibold">{lang === 'de' ? se.name_de : se.name_en}</h4>
                        <Badge variant="outline" className={`text-xs ${
                          se.severity === 'severe' ? 'border-red-300 text-red-600' :
                          se.severity === 'moderate' ? 'border-amber-300 text-amber-600' :
                          'border-green-300 text-green-600'
                        }`}>
                          {se.severity}
                        </Badge>
                        <Badge variant="outline" className="text-xs">{se.frequency}</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground">
                        {lang === 'de' ? se.description_de : se.description_en}
                      </p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Contraindications */}
            <Card className="border border-border/50">
              <CardHeader className="pb-3">
                <CardTitle>{t('detail.contraindications')}</CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  {(p.contraindications || []).map((c, i) => (
                    <li key={i} className="text-sm flex items-start gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-red-400 mt-2 shrink-0" />
                      <span>{lang === 'de' ? c.de : c.en}</span>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* Studies Tab */}
        <TabsContent value="studies">
          <div className="space-y-3">
            {trials.length > 0 ? trials.map((trial, i) => (
              <a
                key={trial.nct_id || i}
                href={trial.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-start gap-4 p-4 rounded-xl border border-border/50 hover:border-primary/20 hover:bg-accent/30 transition-colors group"
              >
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                    {trial.title}
                  </p>
                  <div className="mt-1.5 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
                    <span className="font-mono">{trial.nct_id}</span>
                    <span>|</span>
                    <span>{trial.sponsor}</span>
                    <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${getStatusClass(trial.status)}`}>
                      {trial.status?.replace(/_/g, ' ')}
                    </span>
                    {trial.phase !== 'N/A' && <Badge variant="outline" className="text-xs">{trial.phase}</Badge>}
                  </div>
                </div>
                <ExternalLink className="w-4 h-4 text-muted-foreground group-hover:text-primary shrink-0 mt-1" />
              </a>
            )) : (
              <p className="text-sm text-muted-foreground text-center py-8">{t('studies.no_results')}</p>
            )}
          </div>
        </TabsContent>

        {/* Papers Tab */}
        <TabsContent value="papers">
          <div className="space-y-3">
            {papers.length > 0 ? papers.map((paper, i) => (
              <a
                key={paper.pmid || i}
                href={paper.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-start gap-4 p-4 rounded-xl border border-border/50 hover:border-primary/20 hover:bg-accent/30 transition-colors group"
              >
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                    {paper.title}
                  </p>
                  <p className="text-xs text-muted-foreground mt-1">
                    {paper.authors?.slice(0, 3).join(', ')}{paper.authors?.length > 3 ? ' et al.' : ''}
                  </p>
                  <div className="mt-1.5 flex items-center gap-2">
                    <Badge variant="outline" className="text-xs">{paper.journal}</Badge>
                    <span className="text-xs text-muted-foreground">{paper.pub_date}</span>
                  </div>
                </div>
                <ExternalLink className="w-4 h-4 text-muted-foreground group-hover:text-primary shrink-0 mt-1" />
              </a>
            )) : (
              <p className="text-sm text-muted-foreground text-center py-8">{t('papers.no_results')}</p>
            )}
          </div>
        </TabsContent>
      </Tabs>

      {/* Disclaimer */}
      <div className="mt-12 p-4 rounded-xl bg-secondary/30 border border-border/50">
        <p className="text-xs text-muted-foreground">{t('common.disclaimer')}</p>
      </div>
    </div>
  );
}
