import React from 'react';
import { useTranslation } from 'react-i18next';
import { FlaskConical } from 'lucide-react';

export default function Footer() {
  const { t } = useTranslation();

  return (
    <footer className="border-t border-border bg-white mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
              <FlaskConical className="w-4 h-4 text-primary-foreground" />
            </div>
            <span className="font-semibold text-sm" style={{ fontFamily: 'Space Grotesk' }}>
              PeptideDB
            </span>
          </div>

          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4 text-xs text-muted-foreground">
            <span>{t('footer.data_sources')}: ClinicalTrials.gov, PubMed, OpenAI</span>
            <span className="hidden sm:block">|</span>
            <span>{t('footer.disclaimer')}</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
