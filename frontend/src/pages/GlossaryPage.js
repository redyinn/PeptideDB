import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { Search, BookOpen } from 'lucide-react';
import { Card, CardContent } from '../components/ui/card';

const fadeUp = {
  hidden: { opacity: 0, y: 8 },
  visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.06, duration: 0.45 } })
};

const GLOSSARY_TERMS = [
  { term_en: "Amino Acid", term_de: "Aminosäure", def_en: "Organic molecules that serve as building blocks for peptides and proteins. There are 20 standard amino acids.", def_de: "Organische Moleküle, die als Bausteine für Peptide und Proteine dienen. Es gibt 20 Standardaminosäuren." },
  { term_en: "Bioavailability", term_de: "Bioverfügbarkeit", def_en: "The proportion of a substance that enters the bloodstream and is available for biological activity.", def_de: "Der Anteil eines Stoffes, der in den Blutkreislauf gelangt und für die biologische Aktivität verfügbar ist." },
  { term_en: "BPC-157", term_de: "BPC-157", def_en: "Body Protection Compound-157, a peptide derived from human gastric juice proteins, studied for tissue healing properties.", def_de: "Body Protection Compound-157, ein aus menschlichen Magensaftproteinen gewonnenes Peptid, das auf Gewebeheilungseigenschaften untersucht wird." },
  { term_en: "Clinical Trial", term_de: "Klinische Studie", def_en: "A research study conducted on human participants to evaluate the safety, efficacy, and side effects of medical interventions.", def_de: "Eine Forschungsstudie an menschlichen Teilnehmern zur Bewertung der Sicherheit, Wirksamkeit und Nebenwirkungen medizinischer Interventionen." },
  { term_en: "Contraindication", term_de: "Kontraindikation", def_en: "A condition or factor that serves as a reason to withhold a certain medical treatment due to potential harm.", def_de: "Ein Zustand oder Faktor, der als Grund dient, eine bestimmte medizinische Behandlung wegen möglicher Schäden zurückzuhalten." },
  { term_en: "Dalton (Da)", term_de: "Dalton (Da)", def_en: "A unit of molecular weight. One Dalton is approximately the mass of one hydrogen atom.", def_de: "Eine Einheit des Molekulargewichts. Ein Dalton entspricht ungefähr der Masse eines Wasserstoffatoms." },
  { term_en: "EMA Approval", term_de: "EMA-Zulassung", def_en: "Authorization by the European Medicines Agency for marketing a medicine in the EU.", def_de: "Genehmigung der Europäischen Arzneimittel-Agentur für die Vermarktung eines Arzneimittels in der EU." },
  { term_en: "FDA Approval", term_de: "FDA-Zulassung", def_en: "Authorization by the U.S. Food and Drug Administration for marketing a drug or biologic.", def_de: "Genehmigung der US-amerikanischen Food and Drug Administration für die Vermarktung eines Medikaments oder Biologikums." },
  { term_en: "GLP-1 Agonist", term_de: "GLP-1-Agonist", def_en: "A class of drugs that mimic glucagon-like peptide-1, used in treating type 2 diabetes and obesity (e.g., Semaglutide, Tirzepatide).", def_de: "Eine Klasse von Medikamenten, die das Glucagon-ähnliche Peptid-1 nachahmen, zur Behandlung von Typ-2-Diabetes und Adipositas (z.B. Semaglutid, Tirzepatid)." },
  { term_en: "Growth Hormone Secretagogue", term_de: "Wachstumshormon-Sekretagog", def_en: "Compounds that stimulate the release of growth hormone from the pituitary gland (e.g., Ipamorelin, CJC-1295).", def_de: "Verbindungen, die die Freisetzung von Wachstumshormon aus der Hypophyse stimulieren (z.B. Ipamorelin, CJC-1295)." },
  { term_en: "Half-Life", term_de: "Halbwertszeit", def_en: "The time required for the concentration of a substance in the body to decrease by half.", def_de: "Die Zeit, die benötigt wird, bis die Konzentration eines Stoffes im Körper um die Hälfte abnimmt." },
  { term_en: "Lyophilization", term_de: "Lyophilisierung", def_en: "Freeze-drying process used to preserve peptides in powder form for storage stability.", def_de: "Gefriertrockungsverfahren zur Konservierung von Peptiden in Pulverform für Lagerstabilität." },
  { term_en: "Mechanism of Action", term_de: "Wirkmechanismus", def_en: "The specific biochemical interaction through which a drug produces its pharmacological effect.", def_de: "Die spezifische biochemische Interaktion, durch die ein Medikament seine pharmakologische Wirkung entfaltet." },
  { term_en: "Molecular Weight", term_de: "Molekulargewicht", def_en: "The sum of atomic weights of all atoms in a molecule, typically measured in Daltons for peptides.", def_de: "Die Summe der Atomgewichte aller Atome in einem Molekül, bei Peptiden typischerweise in Dalton gemessen." },
  { term_en: "NCT Number", term_de: "NCT-Nummer", def_en: "A unique identification code assigned to each clinical study registered on ClinicalTrials.gov.", def_de: "Ein eindeutiger Identifikationscode, der jeder auf ClinicalTrials.gov registrierten klinischen Studie zugewiesen wird." },
  { term_en: "Peptide", term_de: "Peptid", def_en: "A short chain of amino acids (typically 2-50) linked by peptide bonds. Smaller than proteins but biologically active.", def_de: "Eine kurze Kette von Aminosäuren (typischerweise 2-50), die durch Peptidbindungen verbunden sind. Kleiner als Proteine, aber biologisch aktiv." },
  { term_en: "Peptide Bond", term_de: "Peptidbindung", def_en: "A covalent chemical bond between the carboxyl group of one amino acid and the amino group of another.", def_de: "Eine kovalente chemische Bindung zwischen der Carboxylgruppe einer Aminosäure und der Aminogruppe einer anderen." },
  { term_en: "Phase 1/2/3", term_de: "Phase 1/2/3", def_en: "Stages of clinical trials: Phase 1 (safety), Phase 2 (efficacy), Phase 3 (large-scale confirmation).", def_de: "Phasen klinischer Studien: Phase 1 (Sicherheit), Phase 2 (Wirksamkeit), Phase 3 (Bestätigung im großen Maßstab)." },
  { term_en: "PMID", term_de: "PMID", def_en: "PubMed Identifier — a unique number assigned to each article indexed in PubMed.", def_de: "PubMed-Identifikator — eine eindeutige Nummer für jeden in PubMed indizierten Artikel." },
  { term_en: "Reconstitution", term_de: "Rekonstitution", def_en: "The process of adding a solvent (e.g., bacteriostatic water) to a lyophilized peptide powder to prepare it for use.", def_de: "Der Prozess des Hinzufügens eines Lösungsmittels (z.B. bakteriostatisches Wasser) zu einem lyophilisierten Peptidpulver zur Gebrauchsvorbereitung." },
  { term_en: "Subcutaneous Injection", term_de: "Subkutane Injektion", def_en: "An injection into the tissue layer between skin and muscle, the most common route for peptide administration.", def_de: "Eine Injektion in die Gewebeschicht zwischen Haut und Muskel, der häufigste Verabreichungsweg für Peptide." },
  { term_en: "Selectivity", term_de: "Selektivität", def_en: "The ability of a peptide or drug to bind to specific receptors while avoiding others, reducing side effects.", def_de: "Die Fähigkeit eines Peptids oder Medikaments, an spezifische Rezeptoren zu binden und andere zu vermeiden, wodurch Nebenwirkungen reduziert werden." },
  { term_en: "Side Effect", term_de: "Nebenwirkung", def_en: "An unintended effect of a pharmaceutical product that occurs alongside the desired therapeutic effect.", def_de: "Eine unbeabsichtigte Wirkung eines pharmazeutischen Produkts, die neben der gewünschten therapeutischen Wirkung auftritt." },
  { term_en: "Telomere", term_de: "Telomer", def_en: "Protective caps at the ends of chromosomes. Telomere length is associated with aging (relevant to Epitalon research).", def_de: "Schutzkappen an den Enden der Chromosomen. Die Telomerlänge wird mit dem Altern in Verbindung gebracht (relevant für Epitalon-Forschung)." },
];

export default function GlossaryPage() {
  const { i18n, t } = useTranslation();
  const lang = i18n.language;
  const [search, setSearch] = useState('');

  const filtered = GLOSSARY_TERMS.filter(term => {
    const q = search.toLowerCase();
    return (
      term.term_en.toLowerCase().includes(q) ||
      term.term_de.toLowerCase().includes(q) ||
      term.def_en.toLowerCase().includes(q) ||
      term.def_de.toLowerCase().includes(q)
    );
  });

  // Group by first letter
  const grouped = {};
  filtered.forEach(term => {
    const letter = (lang === 'de' ? term.term_de : term.term_en)[0].toUpperCase();
    if (!grouped[letter]) grouped[letter] = [];
    grouped[letter].push(term);
  });
  const letters = Object.keys(grouped).sort();

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Header */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight" style={{ fontFamily: 'Space Grotesk' }}>
          {t('glossary.title')}
        </h1>
        <p className="mt-2 text-base text-muted-foreground max-w-[64ch]">
          {t('glossary.subtitle')}
        </p>
      </motion.div>

      {/* Search */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={1} className="mb-8">
        <div className="relative max-w-md">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder={t('glossary.search_placeholder')}
            className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-border bg-card text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-colors"
          />
        </div>
      </motion.div>

      {/* Letter nav */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} custom={2} className="flex flex-wrap gap-1 mb-6">
        {letters.map(letter => (
          <a
            key={letter}
            href={`#glossary-${letter}`}
            className="w-8 h-8 rounded-lg bg-secondary text-sm font-medium flex items-center justify-center hover:bg-primary hover:text-primary-foreground transition-colors"
          >
            {letter}
          </a>
        ))}
      </motion.div>

      {/* Terms */}
      <div className="space-y-8">
        {letters.map(letter => (
          <motion.div key={letter} initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp}>
            <h2 id={`glossary-${letter}`} className="text-2xl font-semibold text-primary mb-4 scroll-mt-20" style={{ fontFamily: 'Space Grotesk' }}>
              {letter}
            </h2>
            <div className="space-y-3">
              {grouped[letter].map((term, i) => (
                <Card key={i} className="border border-border/50">
                  <CardContent className="p-4">
                    <div className="flex items-start gap-3">
                      <BookOpen className="w-4 h-4 text-primary mt-1 shrink-0" />
                      <div>
                        <h3 className="font-semibold text-sm" style={{ fontFamily: 'Space Grotesk' }}>
                          {lang === 'de' ? term.term_de : term.term_en}
                          {lang === 'de' && term.term_en !== term.term_de && (
                            <span className="text-muted-foreground font-normal ml-2">({term.term_en})</span>
                          )}
                        </h3>
                        <p className="text-sm text-muted-foreground mt-1 leading-relaxed">
                          {lang === 'de' ? term.def_de : term.def_en}
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </motion.div>
        ))}
      </div>

      {filtered.length === 0 && (
        <Card className="border border-border/50">
          <CardContent className="p-12 text-center">
            <BookOpen className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-sm text-muted-foreground">{t('glossary.no_results')}</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
