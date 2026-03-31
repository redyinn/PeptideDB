import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import en from './en.json';
import de from './de.json';

const savedLang = typeof window !== 'undefined' ? localStorage.getItem('peptide-lang') : null;
const browserLang = typeof navigator !== 'undefined' ? navigator.language.substring(0, 2) : 'en';

i18n
  .use(initReactI18next)
  .init({
    resources: {
      en: { translation: en },
      de: { translation: de }
    },
    lng: savedLang || (browserLang === 'de' ? 'de' : 'en'),
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

i18n.on('languageChanged', (lng) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('peptide-lang', lng);
    document.documentElement.lang = lng;
  }
});

export default i18n;
