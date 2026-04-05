import React, { useState, useEffect, useCallback } from 'react';
import { Helmet } from 'react-helmet-async';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { ArrowLeft, ExternalLink, Shield, Pill, Activity, AlertTriangle, Beaker, FlaskConical, Copy, Check, Thermometer, Droplets, Clock, GitCompareArrows } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Skeleton } from '../components/ui/skeleton';
import { getPeptideDetail, getTrials, getPapers, getPeptides } from '../lib/api';
import { toast } from 'sonner';

function copyCitation(paper, lang) {
  const authors = paper.authors?.slice(0, 3).join(', ') + (paper.authors?.length > 3 ? ' et al.' : '');
  const citation = `${authors} "${paper.title}" ${paper.journal}${paper.volume ? ` ${paper.volume}` : ''}${paper.issue ? `(${paper.issue})` : ''}${paper.pages ? `:${paper.pages}` : ''} (${paper.pub_date}). PMID: ${paper.pmid}`;
  navigator.clipboard.writeText(citation);
  toast.success(lang === 'de' ? 'Zitat kopiert' : 'Citation copied');
}

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

function getEvidenceBadge(trial) {
  const phase = (trial.phase || '').toLowerCase();
  if (phase.includes('phase 3') || phase.includes('phase iii') || phase.includes('phase 4') || phase.includes('phase iv'))
    return { label: 'Level A', title: 'RCT / Phase 3+', className: 'bg-green-500/10 text-green-400 border border-green-500/20' };
  if (phase.includes('phase 2') || phase.includes('phase ii'))
    return { label: 'Level B', title: 'Phase 2', className: 'bg-blue-500/10 text-blue-400 border border-blue-500/20' };
  if (phase.includes('phase 1') || phase.includes('phase i'))
    return { label: 'Level C', title: 'Phase 1', className: 'bg-secondary text-muted-foreground border border-border' };
  return null;
}

function InfoRow({ label, value, mono = false }) {
  if (!value) return null;
  return (
    <div className="flex items-start py-2.5 border-b border-border/50 last:border-0">
      <span className="text-sm text-muted-foreground w-40 shrink-0">{label}</span>
      <span className={`text-sm font-medium ${mono ? 'font-mono text-xs' : ''}`}>{value}</span>
    </div>
  );
}

function AminoAcidSequenceCard({ sequence, t, lang }) {
  const [copied, setCopied] = React.useState(false);
  const handleCopy = () => {
    navigator.clipboard.writeText(sequence);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  return (
    <Card className="border border-border/50">
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="text-lg flex items-center gap-2">
            <Droplets className="w-5 h-5 text-primary" />
            {t('detail.amino_acid_sequence')}
          </CardTitle>
          <Button variant="ghost" size="sm" onClick={handleCopy} className="gap-1.5 text-xs">
            {copied ? <Check className="w-3.5 h-3.5 text-green-500" /> : <Copy className="w-3.5 h-3.5" />}
            {copied ? (lang === 'de' ? 'Kopiert' : 'Copied') : (lang === 'de' ? 'Kopieren' : 'Copy')}
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        <div className="p-3 rounded-lg bg-secondary/30 overflow-x-auto">
          <p className="font-mono text-xs leading-6 break-all select-all whitespace-pre-wrap">
            {sequence}
          </p>
        </div>
        <p className="mt-2 text-xs text-muted-foreground">
          {sequence.length} {t('detail.amino_acid_count')}
        </p>
      </CardContent>
    </Card>
  );
}

export default function PeptideDetailPage() {
  const { slug } = useParams();
  const { t, i18n } = useTranslation();
  const lang = i18n.language;
  const [peptide, setPeptide] = useState(null);
  const [trials, setTrials] = useState([]);
  const [papers, setPapers] = useState([]);
  const [related, setRelated] = useState([]);
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
      // Fetch related peptides from same category
      if (res.data.category) {
        try {
          const relRes = await getPeptides({ category: res.data.category, limit: 4 });
          setRelated((relRes.data.peptides || []).filter(rp => rp.slug !== slug).slice(0, 3));
        } catch (_) {}
      }
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
      <Helmet>
        <title>{p.name} — PeptideDB</title>
        <meta name="description" content={`${p.description?.en || ''}`.slice(0, 160)} />
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Drug",
          "name": p.name,
          "description": p.description?.en || '',
          "mechanismOfAction": p.mechanism_of_action?.en || '',
          "activeIngredient": p.name,
          "administrationRoute": p.dosage?.route_en || '',
          "url": `https://peptide-db-six.vercel.app/encyclopedia/${slug}`,
          "manufacturer": p.manufacturer ? { "@type": "Organization", "name": p.manufacturer } : undefined,
        })}</script>
      </Helmet>
      {/* Breadcrumb */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-6">
        <Link to="/encyclopedia" className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-primary transition-colors">
          <ArrowLeft className="w-4 h-4" />
          {t('detail.back_to_encyclopedia')}
        </Link>
      </motion.div>

      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="mb-8">
        <div className="flex flex-wrap items-start justify-between gap-3 mb-3">
          <div>
            <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
              {p.name}
            </h1>
            <div className="flex flex-wrap gap-2 mt-2">
              <Badge variant="secondary">{p.category || 'Peptide'}</Badge>
              {p.research_status?.fda_approved && <Badge className="bg-green-500/10 text-green-400 border border-green-500/20">FDA Approved</Badge>}
              {p.research_status?.ema_approved && <Badge className="bg-blue-500/10 text-blue-400 border border-blue-500/20">EMA Approved</Badge>}
            </div>
          </div>
          <Link
            to={`/encyclopedia/compare?peptides=${slug}`}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl border border-border bg-secondary text-sm font-medium text-muted-foreground hover:text-primary hover:border-primary/40 transition-colors shrink-0"
          >
            <GitCompareArrows className="w-4 h-4" />
            {lang === 'de' ? 'Vergleichen' : 'Compare'}
          </Link>
        </div>
        <p className="text-base text-muted-foreground max-w-[72ch] leading-7">
          {p.description?.[lang] || p.description?.en || ''}
        </p>
        {p.updated_at && (
          <div className="mt-3 flex items-center gap-1.5 text-xs text-muted-foreground">
            <Clock className="w-3.5 h-3.5" />
            <span>{t('encyclopedia.last_updated')} {new Date(p.updated_at).toLocaleDateString(lang === 'de' ? 'de-DE' : 'en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</span>
            {p.generated_by && <span className="text-muted-foreground/60">({p.generated_by})</span>}
          </div>
        )}
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

              {/* Amino Acid Sequence */}
              {p.amino_acid_sequence && (
                <AminoAcidSequenceCard sequence={p.amino_acid_sequence} t={t} lang={lang} />
              )}
            </div>

            {/* Sidebar */}
            <div className="space-y-6">
              <Card className="border border-border/50">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg">{t('detail.research_status')}</CardTitle>
                </CardHeader>
                <CardContent className="space-y-0">
                  {/* Phase Progress Bar */}
                  {p.research_status?.phase && (() => {
                    const ph = (p.research_status.phase || '').toLowerCase();
                    const approved = p.research_status.fda_approved || p.research_status.ema_approved;
                    const steps = ['Preclinical', 'Phase 1', 'Phase 2', 'Phase 3', 'Approved'];
                    let activeIdx = 0;
                    if (approved) activeIdx = 4;
                    else if (ph.includes('phase 3') || ph.includes('phase iii')) activeIdx = 3;
                    else if (ph.includes('phase 2') || ph.includes('phase ii')) activeIdx = 2;
                    else if (ph.includes('phase 1') || ph.includes('phase i')) activeIdx = 1;
                    return (
                      <div className="mb-4 pb-4 border-b border-border/50">
                        <p className="text-xs text-muted-foreground mb-2">{lang === 'de' ? 'Forschungsphase' : 'Research Phase'}</p>
                        <div className="flex items-center gap-1">
                          {steps.map((s, i) => (
                            <React.Fragment key={s}>
                              <div className={`flex flex-col items-center gap-1 flex-1`}>
                                <div className={`w-full h-1.5 rounded-full ${i <= activeIdx ? 'bg-primary' : 'bg-secondary'}`} />
                                <span className={`text-[9px] font-medium text-center leading-tight ${i <= activeIdx ? 'text-primary' : 'text-muted-foreground/50'}`}>{s}</span>
                              </div>
                            </React.Fragment>
                          ))}
                        </div>
                      </div>
                    );
                  })()}
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
          <div className="mb-5 flex items-start gap-3 p-4 rounded-xl border" style={{ background: 'hsl(38 92% 50% / 0.07)', borderColor: 'hsl(38 92% 50% / 0.25)' }}>
            <AlertTriangle className="w-4 h-4 shrink-0 mt-0.5" style={{ color: 'hsl(38 92% 60%)' }} />
            <p className="text-xs leading-relaxed" style={{ color: 'hsl(38 92% 65%)' }}>
              {lang === 'de'
                ? 'Die Dosierungsangaben dienen ausschließlich Forschungszwecken und ersetzen keine medizinische Beratung. Konsultiere einen qualifizierten Arzt vor der Anwendung.'
                : 'Dosage information is for research purposes only and does not constitute medical advice. Consult a qualified healthcare professional before use.'}
            </p>
          </div>
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

          {/* Reconstitution Info */}
          {p.reconstitution_info && (
            <Card className="border border-border/50 mt-6">
              <CardHeader className="pb-3">
                <CardTitle className="text-lg flex items-center gap-2">
                  <Thermometer className="w-5 h-5 text-primary" />
                  {t('detail.reconstitution')}
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-0">
                <InfoRow
                  label={t('detail.preparation')}
                  value={lang === 'de' ? p.reconstitution_info.preparation_de : p.reconstitution_info.preparation_en}
                />
                <InfoRow label={t('detail.solvent')} value={p.reconstitution_info.solvent} />
                <InfoRow label={t('detail.storage_temperature')} value={p.reconstitution_info.storage_temperature} mono />
                <InfoRow label={t('detail.shelf_life_unopened')} value={p.reconstitution_info.shelf_life_unopened} />
                <InfoRow label={t('detail.shelf_life_reconstituted')} value={p.reconstitution_info.shelf_life_reconstituted} />
                <InfoRow
                  label={t('detail.light_sensitive')}
                  value={p.reconstitution_info.light_sensitive ? t('common.yes') : t('common.no')}
                />
              </CardContent>
            </Card>
          )}
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
              <Card key={trial.nct_id || i} className="border border-border/50 hover:border-primary/20 transition-colors group">
                <CardContent className="p-4">
                  <a href={trial.url} target="_blank" rel="noopener noreferrer" className="block">
                    <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors leading-relaxed">
                      {trial.title}
                    </p>
                  </a>
                  <div className="mt-2 flex flex-wrap items-center gap-2">
                    <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium ${getStatusClass(trial.status)}`}>
                      {trial.status?.replace(/_/g, ' ')}
                    </span>
                    {trial.phase !== 'N/A' && <Badge variant="outline" className="text-xs">{trial.phase}</Badge>}
                    {(() => {
                      const ev = getEvidenceBadge(trial);
                      return ev ? (
                        <span title={ev.title} className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium font-mono ${ev.className}`}>
                          {ev.label}
                        </span>
                      ) : null;
                    })()}
                    {trial.sponsor && <span className="text-xs text-muted-foreground">{trial.sponsor}</span>}
                  </div>
                  {trial.conditions?.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-1">
                      {trial.conditions.slice(0, 4).map((c, ci) => (
                        <Badge key={ci} variant="secondary" className="text-xs">{c}</Badge>
                      ))}
                    </div>
                  )}
                  <div className="mt-2">
                    <a href={trial.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-primary hover:underline">
                      <span className="font-mono">{trial.nct_id}</span>
                      <ExternalLink className="w-3 h-3" />
                    </a>
                  </div>
                </CardContent>
              </Card>
            )) : (
              <p className="text-sm text-muted-foreground text-center py-8">{t('studies.no_results')}</p>
            )}
          </div>
        </TabsContent>

        {/* Papers Tab */}
        <TabsContent value="papers">
          <div className="space-y-3">
            {papers.length > 0 ? papers.map((paper, i) => (
              <Card key={paper.pmid || i} className="border border-border/50 hover:border-primary/20 transition-colors group">
                <CardContent className="p-4">
                  <a href={paper.url} target="_blank" rel="noopener noreferrer" className="block">
                    <p className="text-sm font-medium text-foreground group-hover:text-primary transition-colors leading-relaxed">
                      {paper.title}
                    </p>
                  </a>
                  <p className="text-xs text-muted-foreground mt-1.5">
                    {paper.authors?.slice(0, 3).join(', ')}{paper.authors?.length > 3 ? ' et al.' : ''}
                  </p>
                  <div className="mt-2 flex flex-wrap items-center gap-2">
                    {paper.journal && <Badge variant="outline" className="text-xs">{paper.journal}</Badge>}
                    {paper.pub_date && <span className="text-xs text-muted-foreground">{paper.pub_date}</span>}
                    {paper.volume && <span className="text-xs text-muted-foreground">Vol. {paper.volume}{paper.issue ? `(${paper.issue})` : ''}</span>}
                  </div>
                  <div className="mt-2 flex flex-wrap items-center gap-2">
                    <a href={paper.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-primary hover:underline">
                      <span className="font-mono">PMID: {paper.pmid}</span>
                      <ExternalLink className="w-3 h-3" />
                    </a>
                    {paper.doi && (
                      <a href={`https://doi.org/${paper.doi.replace('doi: ', '')}`} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-primary hover:underline">
                        <span className="font-mono">DOI</span>
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    )}
                    <button
                      onClick={() => copyCitation(paper, lang)}
                      className="inline-flex items-center gap-1 text-xs text-muted-foreground hover:text-primary transition-colors ml-auto"
                    >
                      <Copy className="w-3 h-3" />
                      {lang === 'de' ? 'Zitieren' : 'Cite'}
                    </button>
                  </div>
                </CardContent>
              </Card>
            )) : (
              <p className="text-sm text-muted-foreground text-center py-8">{t('papers.no_results')}</p>
            )}
          </div>
        </TabsContent>
      </Tabs>

      {/* Related Peptides */}
      {related.length > 0 && (
        <div className="mt-12">
          <h2 className="text-lg font-semibold mb-4" style={{ fontFamily: 'Space Grotesk' }}>
            {lang === 'de' ? 'Ähnliche Peptide' : 'Related Peptides'}
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {related.map(rp => (
              <Link key={rp.slug} to={`/encyclopedia/${rp.slug}`}>
                <Card className="border border-border/50 hover:border-primary/30 transition-colors h-full">
                  <CardContent className="p-4">
                    <div className="flex items-start justify-between gap-2 mb-2">
                      <h3 className="font-semibold text-sm" style={{ fontFamily: 'Space Grotesk' }}>{rp.name}</h3>
                      <Badge variant="secondary" className="text-xs shrink-0">{rp.category}</Badge>
                    </div>
                    <p className="text-xs text-muted-foreground line-clamp-2 leading-relaxed">
                      {rp.description?.[lang] || rp.description?.en || ''}
                    </p>
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Disclaimer */}
      <div className="mt-8 p-4 rounded-xl bg-secondary/30 border border-border/50">
        <p className="text-xs text-muted-foreground">{t('common.disclaimer')}</p>
      </div>
    </div>
  );
}
