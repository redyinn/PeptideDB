import React, { useState, useEffect, useCallback } from 'react';
import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { ExternalLink, Newspaper, BookOpen, TestTube } from 'lucide-react';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Skeleton } from '../components/ui/skeleton';
import { getNews } from '../lib/api';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

export default function NewsPage() {
  const { t } = useTranslation();
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadNews = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getNews({ topic: 'peptide research', limit: 20 });
      setNews(res.data.news || []);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }, []);

  useEffect(() => { loadNews(); }, [loadNews]);

  const getTypeIcon = (type) => {
    if (type === 'paper') return <BookOpen className="w-4 h-4" />;
    if (type === 'trial') return <TestTube className="w-4 h-4" />;
    return <Newspaper className="w-4 h-4" />;
  };

  const getTypeLabel = (type) => {
    if (type === 'paper') return t('news.paper');
    if (type === 'trial') return t('news.trial');
    return 'News';
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <Helmet>
        <title>Peptide Research News — PeptideDB</title>
        <meta name="description" content="Latest news, research papers, and clinical trial updates for peptide therapeutics. Aggregated from PubMed and ClinicalTrials.gov." />
      </Helmet>
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'var(--pdb-font-display)' }}>
          {t('news.title')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground max-w-[64ch]">
          {t('news.subtitle')}
        </p>
      </motion.div>

      {/* News Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {Array.from({ length: 8 }).map((_, i) => (
            <Card key={i} className="border border-border/50">
              <CardContent className="p-5 space-y-3">
                <Skeleton className="h-5 w-full" />
                <Skeleton className="h-4 w-3/4" />
                <Skeleton className="h-4 w-1/2" />
              </CardContent>
            </Card>
          ))}
        </div>
      ) : news.length > 0 ? (
        <div className="space-y-4">
          {/* Featured item */}
          {news[0] && (
            <motion.a
              href={news[0].url}
              target="_blank"
              rel="noopener noreferrer"
              initial="hidden" animate="visible" variants={fadeUp}
              className="block"
            >
              <Card className="card-hover border border-border/50 overflow-hidden">
                <CardContent className="p-6 md:p-8">
                  <div className="flex items-center gap-2 mb-3">
                    <div className="w-7 h-7 rounded-lg bg-accent flex items-center justify-center text-primary">
                      {getTypeIcon(news[0].type)}
                    </div>
                    <Badge variant="secondary" className="text-xs">{getTypeLabel(news[0].type)}</Badge>
                    <span className="text-xs text-muted-foreground">{news[0].date}</span>
                  </div>
                  <h2 className="text-xl font-semibold tracking-tight mb-2" style={{ fontFamily: 'var(--pdb-font-display)' }}>
                    {news[0].title}
                  </h2>
                  <p className="text-sm text-muted-foreground mb-3">{news[0].summary}</p>
                  <div className="flex items-center gap-2 text-xs text-muted-foreground">
                    <span>{news[0].source}</span>
                    {news[0].authors?.[0] && (
                      <><span>|</span><span>{news[0].authors[0]}</span></>
                    )}
                  </div>
                </CardContent>
              </Card>
            </motion.a>
          )}

          {/* Rest of news */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {news.slice(1).map((item, i) => (
              <motion.a
                key={i}
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                variants={fadeUp}
                custom={i % 6}
                data-testid={`news-item-${i}`}
              >
                <Card className="card-hover border border-border/50 h-full">
                  <CardContent className="p-5">
                    <div className="flex items-center gap-2 mb-2">
                      <div className="w-6 h-6 rounded-md bg-accent flex items-center justify-center text-primary">
                        {getTypeIcon(item.type)}
                      </div>
                      <Badge variant="secondary" className="text-xs">{getTypeLabel(item.type)}</Badge>
                      <span className="text-xs text-muted-foreground">{item.date}</span>
                    </div>
                    <h3 className="text-sm font-medium text-foreground line-clamp-2 leading-relaxed mb-2">
                      {item.title}
                    </h3>
                    <p className="text-xs text-muted-foreground line-clamp-2">{item.summary}</p>
                    <div className="mt-3 flex items-center justify-between">
                      <span className="text-xs text-muted-foreground">{item.source}</span>
                      <ExternalLink className="w-3.5 h-3.5 text-muted-foreground" />
                    </div>
                  </CardContent>
                </Card>
              </motion.a>
            ))}
          </div>
        </div>
      ) : (
        <Card className="border border-border/50" data-testid="empty-state">
          <CardContent className="p-12 text-center">
            <Newspaper className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-sm text-muted-foreground">{t('news.no_results')}</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

