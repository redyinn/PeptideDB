"""Add ~20 new peptides to peptides_export.json — 2026 batch."""
import json, re
from datetime import datetime

NOW = datetime.utcnow().isoformat()

def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

NEW_PEPTIDES = [
    # ── 1. Cerebrolysin ────────────────────────────────────────────────────────
    {
        "name": "Cerebrolysin",
        "slug": "cerebrolysin",
        "category": "Neuroprotective / Nootropic",
        "description": {
            "en": "Cerebrolysin is a standardised neuropeptide preparation derived from porcine brain tissue, comprising low-molecular-weight peptides (<10 kDa) and free amino acids. It has been used clinically in many countries for Alzheimer's disease, stroke rehabilitation, and traumatic brain injury. Multiple meta-analyses support its efficacy over placebo.",
            "de": "Cerebrolysin ist eine standardisierte Neuropeptid-Zubereitung aus Schweinehirngewebe, bestehend aus niedermolekularen Peptiden (<10 kDa) und freien Aminosäuren. Es wird klinisch in vielen Ländern bei Alzheimer, Schlaganfallrehabilitation und Schädel-Hirn-Trauma eingesetzt."
        },
        "mechanism_of_action": {
            "en": "Simultaneously activates BDNF, GDNF, NGF, and CNTF signalling pathways by delivering neuropeptide fragments that mimic endogenous neurotrophins. Crosses the blood–brain barrier, reduces neuroapoptosis via Bcl-2 upregulation, attenuates excitotoxicity, and promotes neurogenesis and synaptic plasticity.",
            "de": "Aktiviert gleichzeitig BDNF-, GDNF-, NGF- und CNTF-Signalwege durch Neuropeptidfragmente, die endogene Neurotrophine imitieren. Überquert die Blut-Hirn-Schranke, reduziert Neuroapoptose, vermindert Exzitotoxizität und fördert Neurogenese und synaptische Plastizität."
        },
        "indications": [
            {"condition_en": "Alzheimer's Disease", "condition_de": "Alzheimer-Erkrankung", "description_en": "Positive meta-analyses vs placebo for cognitive outcomes", "description_de": "Positive Metaanalysen vs. Placebo für kognitive Endpunkte"},
            {"condition_en": "Acute Ischaemic Stroke", "condition_de": "Ischämischer Schlaganfall", "description_en": "Neuroprotection and functional recovery post-stroke", "description_de": "Neuroprotektionund funktionelle Erholung nach Schlaganfall"},
            {"condition_en": "Traumatic Brain Injury", "condition_de": "Schädel-Hirn-Trauma", "description_en": "Accelerates cognitive recovery", "description_de": "Beschleunigt kognitive Erholung"}
        ],
        "benefits": [
            {"benefit_en": "Multi-neurotrophin pathway activation (BDNF, NGF, GDNF)", "benefit_de": "Aktivierung mehrerer Neurotrophin-Wege (BDNF, NGF, GDNF)"},
            {"benefit_en": "Crosses blood–brain barrier", "benefit_de": "Überquert die Blut-Hirn-Schranke"},
            {"benefit_en": "Approved / registered in 35+ countries", "benefit_de": "In 35+ Ländern zugelassen / registriert"},
            {"benefit_en": "Reduces neuroinflammation and oxidative stress", "benefit_de": "Reduziert Neuroinflammation und oxidativen Stress"}
        ],
        "side_effects": [
            {"name_en": "Injection site discomfort", "name_de": "Beschwerden an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local pain or burning with IM injection", "description_de": "Lokaler Schmerz oder Brennen bei IM-Injektion"},
            {"name_en": "Dizziness / headache", "name_de": "Schwindel / Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Transient neurological symptoms", "description_de": "Vorübergehende neurologische Symptome"},
            {"name_en": "Hypersensitivity reactions", "name_de": "Überempfindlichkeitsreaktionen", "severity": "moderate", "frequency": "rare", "description_en": "Allergic reaction to porcine-derived components", "description_de": "Allergische Reaktion auf porcine Bestandteile"}
        ],
        "dosage": {
            "starting_dose": "5 mL IV/IM",
            "maintenance_dose": "10–20 mL IV/IM",
            "frequency_en": "Daily for 10–28 consecutive days per course",
            "frequency_de": "Täglich für 10–28 aufeinanderfolgende Tage pro Kurs",
            "route_en": "Intravenous infusion or intramuscular injection",
            "route_de": "Intravenöse Infusion oder intramuskuläre Injektion",
            "notes_en": "Higher doses (10–20 mL/day) used for acute neurological events. 5 mL/day for cognitive maintenance.",
            "notes_de": "Höhere Dosen (10–20 mL/Tag) bei akuten neurologischen Ereignissen. 5 mL/Tag zur kognitiven Erhaltung."
        },
        "contraindications": [
            {"en": "Known hypersensitivity to porcine-derived products", "de": "Bekannte Überempfindlichkeit gegenüber porcinen Produkten"},
            {"en": "Severe renal impairment", "de": "Schwere Niereninsuffizienz"},
            {"en": "Status epilepticus", "de": "Status epilepticus"}
        ],
        "drug_interactions": ["CNS stimulants (additive excitatory effect)", "MAO inhibitors", "Antidepressants"],
        "research_status": {"phase": "Approved (multiple countries)", "fda_approved": False, "ema_approved": False, "notes_en": "Not FDA/EMA approved but registered in 35+ countries. Orphan drug reviews ongoing in EU.", "notes_de": "Nicht FDA/EMA-zugelassen, aber in 35+ Ländern registriert."},
        "manufacturer": "EVER Neuro Pharma",
        "molecular_weight": "<10 kDa (peptide mixture)",
        "amino_acid_count": "N/A (mixture)",
        "half_life": "Short (individual peptide components vary)",
        "storage_conditions": {"en": "2–8°C. Protect from light. Do not freeze.", "de": "2–8°C. Vor Licht schützen. Nicht einfrieren."},
        "availability": "Prescription in approved countries; research vials available",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 2. NAP / Davunetide ────────────────────────────────────────────────────
    {
        "name": "NAP (Davunetide)",
        "slug": "nap-davunetide",
        "category": "Neuroprotective / Nootropic",
        "description": {
            "en": "NAP (NAPVSIPQ, davunetide) is an 8-amino-acid neuroprotective peptide derived from Activity-Dependent Neuroprotective Protein (ADNP). It stabilises microtubules, reduces tau pathology, and has shown efficacy in Alzheimer's disease and amnestic mild cognitive impairment in Phase 2 clinical trials.",
            "de": "NAP (NAPVSIPQ, Davunetid) ist ein 8-Aminosäure-neuroprotektives Peptid aus dem Activity-Dependent Neuroprotective Protein (ADNP). Es stabilisiert Mikrotubuli, reduziert Tau-Pathologie und zeigte Wirksamkeit bei Alzheimer und amnestischer MCI in Phase-2-Studien."
        },
        "mechanism_of_action": {
            "en": "Binds tubulin and stabilises microtubules by protecting the Tau–tubulin interface. Activates PI3K/Akt and MAPK/MEK1 survival pathways. Penetrates neuronal nuclei and modulates gene expression. Reduces amyloid-beta toxicity and neurofibrillary tangle formation.",
            "de": "Bindet Tubulin und stabilisiert Mikrotubuli durch Schutz der Tau–Tubulin-Grenzfläche. Aktiviert PI3K/Akt- und MAPK/MEK1-Überlebenswege. Penetriert Neuronenkerne und moduliert Genexpression. Reduziert Amyloid-beta-Toxizität und Bildung neurofibriller Tangles."
        },
        "indications": [
            {"condition_en": "Alzheimer's Disease", "condition_de": "Alzheimer-Erkrankung", "description_en": "Phase 2 trials demonstrated memory improvement in aMCI patients", "description_de": "Phase-2-Studien zeigten Gedächtnisverbesserung bei aMCI-Patienten"},
            {"condition_en": "Progressive Supranuclear Palsy", "condition_de": "Progressive supranukleäre Blickparese", "description_en": "Phase 2 trial in tauopathy; primary endpoint not met but biomarker signals noted", "description_de": "Phase-2-Studie bei Tauopathie"},
            {"condition_en": "Cognitive Enhancement", "condition_de": "Kognitive Verbesserung", "description_en": "Nootropic research use for memory consolidation", "description_de": "Nootropischer Forschungseinsatz zur Gedächtniskonsolidierung"}
        ],
        "benefits": [
            {"benefit_en": "Microtubule stabilisation and tau protection", "benefit_de": "Mikrotubuli-Stabilisierung und Tau-Schutz"},
            {"benefit_en": "Intranasal delivery achieves CNS levels directly", "benefit_de": "Intranasale Verabreichung erreicht ZNS-Spiegel direkt"},
            {"benefit_en": "Demonstrated memory improvement in human MCI trial", "benefit_de": "Bewiesene Gedächtnisverbesserung in humaner MCI-Studie"},
            {"benefit_en": "Reduces amyloid-beta neurotoxicity", "benefit_de": "Reduziert Amyloid-beta-Neurotoxizität"}
        ],
        "side_effects": [
            {"name_en": "Nasal irritation", "name_de": "Nasale Reizung", "severity": "mild", "frequency": "common", "description_en": "Minor local irritation with intranasal use", "description_de": "Geringe lokale Reizung bei intranasaler Anwendung"},
            {"name_en": "Headache", "name_de": "Kopfschmerz", "severity": "mild", "frequency": "uncommon", "description_en": "Mild transient headache", "description_de": "Leichter vorübergehender Kopfschmerz"}
        ],
        "dosage": {
            "starting_dose": "5 mg intranasally twice daily",
            "maintenance_dose": "5–30 mg intranasally twice daily",
            "frequency_en": "Twice daily intranasal administration",
            "frequency_de": "Zweimal täglich intranasale Verabreichung",
            "route_en": "Intranasal spray",
            "route_de": "Intranasales Spray",
            "notes_en": "Clinical trials used 5 or 30 mg intranasal doses (AL-108 formulation). Community research use: 1–5 mg/day.",
            "notes_de": "Klinische Studien verwendeten 5 oder 30 mg intranasale Dosen (AL-108-Formulierung). Community-Forschungseinsatz: 1–5 mg/Tag."
        },
        "contraindications": [
            {"en": "Hypersensitivity to any component", "de": "Überempfindlichkeit gegenüber Bestandteilen"},
            {"en": "Active nasal/sinus infection", "de": "Aktive Nasen-/Sinusinfektion"}
        ],
        "drug_interactions": ["Data limited; theoretical interaction with microtubule-targeting chemotherapy"],
        "research_status": {"phase": "Phase 2 (completed)", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 2 trials completed; no Phase 3 initiated as of 2026. Available as research peptide.", "notes_de": "Phase-2-Studien abgeschlossen; keine Phase 3 bis 2026 initiiert."},
        "manufacturer": "Allon Therapeutics (clinical); various research suppliers",
        "molecular_weight": "838 Da",
        "amino_acid_count": "8",
        "half_life": "~1–2 hours (intranasal)",
        "storage_conditions": {"en": "Lyophilised: -20°C. Reconstituted solution: 2–8°C, use within 1 week.", "de": "Lyophilisiert: -20°C. Rekonstituierte Lösung: 2–8°C, innerhalb einer Woche verwenden."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 3. PE-22-28 ────────────────────────────────────────────────────────────
    {
        "name": "PE-22-28",
        "slug": "pe-22-28",
        "category": "Neuroprotective / Antidepressant",
        "description": {
            "en": "PE-22-28 is a synthetic 7-amino-acid peptide derived from spadin, a fragment of the NTSR3/sortilin propeptide. It acts as a selective TREK-1 potassium channel blocker and has shown rapid antidepressant effects within 4 days in animal models — significantly faster than SSRIs (3+ weeks). Currently preclinical only.",
            "de": "PE-22-28 ist ein synthetisches 7-Aminosäure-Peptid aus Spadin, einem Fragment des NTSR3/Sortilin-Propeptids. Es wirkt als selektiver TREK-1-Kaliumkanalblocker und zeigt in Tiermodellen schnelle antidepressive Wirkung innerhalb von 4 Tagen — deutlich schneller als SSRIs."
        },
        "mechanism_of_action": {
            "en": "Selectively blocks TREK-1 (TWIK-related potassium channel 1), a leak K⁺ channel whose overactivation is linked to depression. TREK-1 blockade leads to neuronal membrane depolarisation, upregulation of BDNF, and serotonergic pathway enhancement. Mechanism is completely distinct from all existing antidepressants.",
            "de": "Selektive Blockade von TREK-1 (TWIK-verwandter Kaliumkanal 1), dessen Überaktivierung mit Depression verknüpft ist. TREK-1-Blockade führt zu neuronaler Membrandepolarisation, BDNF-Hochregulierung und Verbesserung serotonergener Wege."
        },
        "indications": [
            {"condition_en": "Major Depressive Disorder", "condition_de": "Major Depression", "description_en": "Rapid antidepressant effect in preclinical models", "description_de": "Schnelle antidepressive Wirkung in präklinischen Modellen"},
            {"condition_en": "Treatment-Resistant Depression", "condition_de": "Therapieresistente Depression", "description_en": "Novel mechanism offers alternative for SSRI non-responders", "description_de": "Neuartiger Mechanismus bietet Alternative für SSRI-Non-Responder"},
            {"condition_en": "Anxiety", "condition_de": "Angststörungen", "description_en": "Anxiolytic effects observed in preclinical studies", "description_de": "Anxiolytische Effekte in präklinischen Studien beobachtet"}
        ],
        "benefits": [
            {"benefit_en": "Onset of action ~4 days vs 3+ weeks for SSRIs (preclinical)", "benefit_de": "Wirkungseintritt ~4 Tage vs. 3+ Wochen für SSRIs (präklinisch)"},
            {"benefit_en": "Completely novel mechanism (TREK-1 blockade)", "benefit_de": "Völlig neuer Mechanismus (TREK-1-Blockade)"},
            {"benefit_en": "Upregulates BDNF", "benefit_de": "Hochregulierung von BDNF"},
            {"benefit_en": "Intranasal delivery suitable", "benefit_de": "Intranasale Verabreichung geeignet"}
        ],
        "side_effects": [
            {"name_en": "Unknown (no human trials)", "name_de": "Unbekannt (keine Humanstudien)", "severity": "unknown", "frequency": "unknown", "description_en": "No human safety data available", "description_de": "Keine Humansicherheitsdaten verfügbar"}
        ],
        "dosage": {
            "starting_dose": "No established human dose",
            "maintenance_dose": "No established human dose",
            "frequency_en": "Intranasal — research use only",
            "frequency_de": "Intranasal — nur Forschungseinsatz",
            "route_en": "Intranasal",
            "route_de": "Intranasal",
            "notes_en": "Preclinical animal studies only. No validated human dosing protocol exists.",
            "notes_de": "Nur präklinische Tierstudien. Kein validiertes Humandosierungsprotokoll."
        },
        "contraindications": [
            {"en": "Human use not established — preclinical compound only", "de": "Humaneinsatz nicht etabliert — nur präklinische Verbindung"}
        ],
        "drug_interactions": ["Theoretical interactions with serotonergic antidepressants and other TREK-1 modulators"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Animal studies only. Promising antidepressant candidate but no human trials initiated.", "notes_de": "Nur Tierstudien. Vielversprechender Antidepressivum-Kandidat, aber keine Humanstudien."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "847 Da",
        "amino_acid_count": "7",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -20°C. Reconstituted: 2–8°C, use within 1 week.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C, innerhalb einer Woche verwenden."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 4. Ac-SDKP (TB-4 Fragment 1-4) ────────────────────────────────────────
    {
        "name": "Ac-SDKP (TB-4 Fragment 1-4)",
        "slug": "ac-sdkp",
        "category": "Anti-fibrotic / Tissue Repair",
        "description": {
            "en": "Ac-SDKP is the N-terminal tetrapeptide fragment of Thymosin Beta-4 (Ac-Ser-Asp-Lys-Pro), produced endogenously by meprin-α and prolyl oligopeptidase cleavage. It is a potent anti-fibrotic agent that suppresses TGF-β1 signalling, prevents myofibroblast differentiation, and reduces fibrosis in lung, kidney, heart, and liver.",
            "de": "Ac-SDKP ist das N-terminale Tetrapeptid-Fragment von Thymosin Beta-4 (Ac-Ser-Asp-Lys-Pro), endogen durch Meprin-α- und Prolyl-Oligopeptidase-Spaltung produziert. Es ist ein potenter antifibrotischer Wirkstoff, der TGF-β1-Signalgebung unterdrückt und Fibrose in Lunge, Niere, Herz und Leber reduziert."
        },
        "mechanism_of_action": {
            "en": "Inhibits TGF-β1–induced SMAD2/3 phosphorylation, preventing fibroblast-to-myofibroblast transition. Reduces macrophage infiltration and pro-inflammatory cytokine production (IL-1β, TNF-α). Endogenously broken down by ACE; ACE inhibitors raise Ac-SDKP levels — one mechanism behind their anti-fibrotic benefit.",
            "de": "Hemmt TGF-β1-induzierte SMAD2/3-Phosphorylierung, verhindert Fibroblasten-zu-Myofibroblasten-Übergang. Reduziert Makrophagen-Infiltration und proinflammatorische Zytokine. Wird endogen durch ACE abgebaut — ein Mechanismus hinter dem antifibrotischen Benefit von ACE-Hemmern."
        },
        "indications": [
            {"condition_en": "Pulmonary Fibrosis", "condition_de": "Lungenfibroseose", "description_en": "Anti-fibrotic effects in IPF models", "description_de": "Antifibrotische Effekte in IPF-Modellen"},
            {"condition_en": "Renal Fibrosis", "condition_de": "Nierenfibroseose", "description_en": "Reduces glomerulosclerosis and tubulointerstitial fibrosis", "description_de": "Reduziert Glomerulosklerose und tubulointerstitielle Fibrose"},
            {"condition_en": "Cardiac Fibrosis", "condition_de": "Herzfibrose", "description_en": "Prevents post-MI fibrotic remodelling", "description_de": "Verhindert fibrotisches Remodeling nach Herzinfarkt"},
            {"condition_en": "Liver Fibrosis", "condition_de": "Leberfibrose", "description_en": "Reduces hepatic stellate cell activation", "description_de": "Reduziert hepatische Sternzell-Aktivierung"}
        ],
        "benefits": [
            {"benefit_en": "Potent multi-organ anti-fibrotic", "benefit_de": "Potentes Multi-Organ-Antifibrotikum"},
            {"benefit_en": "Reduces TGF-β1 and SMAD signalling", "benefit_de": "Reduziert TGF-β1- und SMAD-Signalgebung"},
            {"benefit_en": "Anti-inflammatory (reduces IL-1β, TNF-α, macrophage infiltration)", "benefit_de": "Entzündungshemmend (reduziert IL-1β, TNF-α, Makrophagen-Infiltration)"},
            {"benefit_en": "Endogenous peptide — good tolerability profile expected", "benefit_de": "Endogenes Peptid — gutes Verträglichkeitsprofil erwartet"}
        ],
        "side_effects": [
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Minor local irritation", "description_de": "Geringfügige lokale Reizung"}
        ],
        "dosage": {
            "starting_dose": "500 mcg SC or oral",
            "maintenance_dose": "500 mcg SC daily or as directed",
            "frequency_en": "Once daily; some protocols use oral capsules",
            "frequency_de": "Einmal täglich; einige Protokolle verwenden orale Kapseln",
            "route_en": "Subcutaneous injection or oral",
            "route_de": "Subkutane Injektion oder oral",
            "notes_en": "Experimental. Sold by some vendors as 500 mcg oral capsules. No validated human clinical protocol exists.",
            "notes_de": "Experimentell. Von einigen Anbietern als orale Kapseln (500 mcg) verkauft. Kein validiertes Humandosierungsprotokoll."
        },
        "contraindications": [
            {"en": "Pregnancy (insufficient data)", "de": "Schwangerschaft (unzureichende Daten)"},
            {"en": "Known hypersensitivity", "de": "Bekannte Überempfindlichkeit"}
        ],
        "drug_interactions": ["ACE inhibitors (Ac-SDKP is an ACE substrate — ACEi elevates endogenous levels)"],
        "research_status": {"phase": "Preclinical / Research", "fda_approved": False, "ema_approved": False, "notes_en": "Preclinical anti-fibrotic research. No human trials completed.", "notes_de": "Präklinische antifibrotische Forschung. Keine Humanstudien abgeschlossen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "487.5 Da",
        "amino_acid_count": "4",
        "half_life": "Minutes (cleaved by ACE endogenously)",
        "storage_conditions": {"en": "Lyophilised: -20°C. Stable at room temperature short-term.", "de": "Lyophilisiert: -20°C. Kurzfristig bei Raumtemperatur stabil."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 5. Thymogen ────────────────────────────────────────────────────────────
    {
        "name": "Thymogen (Glu-Trp)",
        "slug": "thymogen",
        "category": "Immunomodulator / Bioregulator",
        "description": {
            "en": "Thymogen is a synthetic dipeptide (Glutamic acid – Tryptophan) derived from thymopoietin, representing the smallest active thymic bioregulator. Developed by Russian gerontologists, it enhances T-cell maturation and immune function and is used clinically in Russia for immunodeficiency and post-surgical immune recovery.",
            "de": "Thymogen ist ein synthetisches Dipeptid (Glutaminsäure – Tryptophan) aus Thymopoietin, das kleinste aktive Thymus-Bioregulator. Von russischen Gerontologen entwickelt, verbessert es T-Zell-Reifung und Immunfunktion und wird klinisch in Russland bei Immundefizienz eingesetzt."
        },
        "mechanism_of_action": {
            "en": "Binds thymopoietin receptor on T-lymphocyte precursors. Stimulates T-cell maturation and differentiation in the thymus. Upregulates IL-2 receptor expression. Restores T-helper/T-suppressor balance. May penetrate cell nuclei and regulate gene expression as a bioregulator peptide.",
            "de": "Bindet Thymopoietin-Rezeptor auf T-Lymphozyten-Vorläufern. Stimuliert T-Zell-Reifung und -Differenzierung im Thymus. Hochregulierung der IL-2-Rezeptor-Expression. Stellt T-Helfer/T-Suppressor-Balance wieder her."
        },
        "indications": [
            {"condition_en": "Immunodeficiency States", "condition_de": "Immundefizienz-Zustände", "description_en": "T-cell deficiency and immune hypofunction", "description_de": "T-Zell-Defizienz und Immun-Hypofunktion"},
            {"condition_en": "Chronic Infectious Diseases", "condition_de": "Chronische Infektionskrankheiten", "description_en": "Adjuvant immune support for recurrent infections", "description_de": "Adjuvante Immununterstützung bei rezidivierenden Infektionen"},
            {"condition_en": "Post-surgical Immune Recovery", "condition_de": "Postoperative Immunerholung", "description_en": "Restoration of immune function following surgery", "description_de": "Wiederherstellung der Immunfunktion nach Operationen"},
            {"condition_en": "Anti-aging / Longevity", "condition_de": "Anti-Aging / Langlebigkeit", "description_en": "Age-related thymic involution and immune senescence", "description_de": "Altersbedingte Thymus-Involution und Immunseneszenz"}
        ],
        "benefits": [
            {"benefit_en": "Smallest effective thymic bioregulator (dipeptide)", "benefit_de": "Kleinster wirksamer Thymus-Bioregulator (Dipeptid)"},
            {"benefit_en": "Restores T-cell function and IL-2 signalling", "benefit_de": "Stellt T-Zellfunktion und IL-2-Signalgebung wieder her"},
            {"benefit_en": "Intranasal delivery option available", "benefit_de": "Intranasale Verabreichungsoption verfügbar"},
            {"benefit_en": "Very low molecular weight — high bioavailability", "benefit_de": "Sehr niedriges Molekulargewicht — hohe Bioverfügbarkeit"}
        ],
        "side_effects": [
            {"name_en": "Mild injection site reaction", "name_de": "Leichte Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "uncommon", "description_en": "Local redness or discomfort", "description_de": "Lokale Rötung oder Beschwerden"},
            {"name_en": "Transient immune activation symptoms", "name_de": "Vorübergehende Immunaktivierungssymptome", "severity": "mild", "frequency": "rare", "description_en": "Mild fatigue or fever with initiation", "description_de": "Leichte Müdigkeit oder Fieber bei Beginn"}
        ],
        "dosage": {
            "starting_dose": "1 mcg/kg",
            "maintenance_dose": "1 mcg/kg daily for 5–10 days",
            "frequency_en": "Once daily for 5–10 consecutive days; repeat 2–3x per year",
            "frequency_de": "Einmal täglich für 5–10 aufeinanderfolgende Tage; 2–3x jährlich wiederholen",
            "route_en": "Intramuscular injection or intranasal spray",
            "route_de": "Intramuskuläre Injektion oder intranasales Spray",
            "notes_en": "Russian clinical protocols use 1 mcg/kg IM or SC. Intranasal form used for convenience.",
            "notes_de": "Russische klinische Protokolle verwenden 1 mcg/kg IM oder SC. Intranasale Form für Komfort."
        },
        "contraindications": [
            {"en": "Autoimmune conditions (may exacerbate)", "de": "Autoimmunerkrankungen (können sich verschlimmern)"},
            {"en": "Pregnancy (insufficient data)", "de": "Schwangerschaft (unzureichende Daten)"}
        ],
        "drug_interactions": ["Immunosuppressants (antagonism)", "Cytokine-modulating biologics"],
        "research_status": {"phase": "Approved (Russia/CIS)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved drug in Russia and CIS countries. Research peptide in Western markets.", "notes_de": "Zugelassenes Medikament in Russland und GUS-Ländern. Forschungspeptid in westlichen Märkten."},
        "manufacturer": "Cytomedics (Russia); various research suppliers",
        "molecular_weight": "333 Da",
        "amino_acid_count": "2",
        "half_life": "Short (minutes to hours)",
        "storage_conditions": {"en": "Dry: room temperature stable. Solutions: 2–8°C.", "de": "Trocken: raumtemperaturstabil. Lösungen: 2–8°C."},
        "availability": "Research peptide in Western markets",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 6. Vilon (Lys-Glu) ────────────────────────────────────────────────────
    {
        "name": "Vilon (Lys-Glu)",
        "slug": "vilon",
        "category": "Immunomodulator / Bioregulator",
        "description": {
            "en": "Vilon is a synthetic dipeptide (Lysine–Glutamic acid) developed as part of the Russian bioregulator peptide programme under Vladimir Khavinson. It regulates bone marrow haematopoiesis and T-lymphocyte function. Featured in landmark Russian longevity studies alongside Thymalin and Epithalon, showing significant reduction in mortality.",
            "de": "Vilon ist ein synthetisches Dipeptid (Lysin–Glutaminsäure), entwickelt im russischen Bioregulator-Peptid-Programm unter Vladimir Khavinson. Es reguliert Knochenmark-Hämatopoese und T-Lymphozyten-Funktion. Beteiligt an wegweisenden russischen Langlebigkeitsstudien zusammen mit Thymalin und Epithalon."
        },
        "mechanism_of_action": {
            "en": "Stimulates haematopoietic progenitor cell differentiation in bone marrow. Modulates T-lymphocyte maturation and cytokine balance. Normalises IL-1, IL-2, and TNF production. As a bioregulator dipeptide, may enter cell nuclei and modulate gene expression through chromatin interaction.",
            "de": "Stimuliert hämatopoetische Vorläuferzell-Differenzierung im Knochenmark. Moduliert T-Lymphozyten-Reifung und Zytokin-Balance. Normalisiert IL-1-, IL-2- und TNF-Produktion. Als Bioregulator-Dipeptid kann es Zellkerne betreten und Genexpression durch Chromatin-Interaktion modulieren."
        },
        "indications": [
            {"condition_en": "Age-related Immune Decline", "condition_de": "Altersbedingte Immunabnahme", "description_en": "Restoration of T-cell and bone marrow function in aging", "description_de": "Wiederherstellung von T-Zell- und Knochenmarkfunktion im Alter"},
            {"condition_en": "Haematopoietic Support", "condition_de": "Hämatopoetische Unterstützung", "description_en": "Bone marrow progenitor stimulation", "description_de": "Knochenmark-Vorläuferzellstimulation"},
            {"condition_en": "Longevity / Anti-aging", "condition_de": "Langlebigkeit / Anti-Aging", "description_en": "Part of multi-peptide longevity protocols", "description_de": "Teil von Multi-Peptid-Langlebigkeitsprotokollen"}
        ],
        "benefits": [
            {"benefit_en": "Part of Russian longevity programme showing 2.5× mortality reduction", "benefit_de": "Teil des russischen Langlebigkeitsprogramms mit 2,5-facher Sterblichkeitsreduktion"},
            {"benefit_en": "Stimulates bone marrow haematopoiesis", "benefit_de": "Stimuliert Knochenmark-Hämatopoese"},
            {"benefit_en": "Minimal dipeptide — very high bioavailability", "benefit_de": "Minimales Dipeptid — sehr hohe Bioverfügbarkeit"},
            {"benefit_en": "Normalises immune cytokine balance", "benefit_de": "Normalisiert Immun-Zytokin-Balance"}
        ],
        "side_effects": [
            {"name_en": "Generally well tolerated", "name_de": "Im Allgemeinen gut verträglich", "severity": "mild", "frequency": "rare", "description_en": "Minimal adverse effects reported in clinical use", "description_de": "Minimale Nebenwirkungen im klinischen Einsatz berichtet"}
        ],
        "dosage": {
            "starting_dose": "1 mcg/kg SC or IM",
            "maintenance_dose": "1 mcg/kg daily for 5–10 days",
            "frequency_en": "Daily for 5–10 days; 1–2 courses per year",
            "frequency_de": "Täglich für 5–10 Tage; 1–2 Kuren pro Jahr",
            "route_en": "Subcutaneous or intramuscular injection",
            "route_de": "Subkutane oder intramuskuläre Injektion",
            "notes_en": "Often used in combination with Thymalin and Epithalon in Russian longevity protocols.",
            "notes_de": "Häufig in Kombination mit Thymalin und Epithalon in russischen Langlebigkeitsprotokollen verwendet."
        },
        "contraindications": [
            {"en": "Autoimmune conditions (insufficient data)", "de": "Autoimmunerkrankungen (unzureichende Daten)"},
            {"en": "Haematological malignancy (theoretical risk)", "de": "Hämatologische Malignome (theoretisches Risiko)"}
        ],
        "drug_interactions": ["Immunosuppressants (antagonism)"],
        "research_status": {"phase": "Approved (Russia/CIS)", "fda_approved": False, "ema_approved": False, "notes_en": "Used clinically in Russia. Research peptide in Western markets.", "notes_de": "Klinisch in Russland eingesetzt. Forschungspeptid in westlichen Märkten."},
        "manufacturer": "Cytomedics / Peptide Sciences / various",
        "molecular_weight": "275 Da",
        "amino_acid_count": "2",
        "half_life": "Short (minutes to hours)",
        "storage_conditions": {"en": "Room temperature stable (powder). Solutions at 2–8°C.", "de": "Raumtemperaturstabil (Pulver). Lösungen bei 2–8°C."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 7. SHLP2 ───────────────────────────────────────────────────────────────
    {
        "name": "SHLP2 (Small Humanin-Like Peptide 2)",
        "slug": "shlp2",
        "category": "Mitochondrial / Metabolic",
        "description": {
            "en": "SHLP2 is a mitochondria-encoded small peptide belonging to the humanin/SHLP family, encoded within the 12S rRNA region. It regulates energy homeostasis, stimulates hypothalamic anorexigenic neurons, and has anti-apoptotic and antioxidant properties. Circulating levels decline with age, correlating with metabolic dysfunction.",
            "de": "SHLP2 ist ein mitochondrial kodiertes kleines Peptid aus der Humanin/SHLP-Familie, kodiert in der 12S-rRNA-Region. Es reguliert Energiehomöostase, stimuliert hypothalamische anorexigene Neuronen und hat antiapoptotische und antioxidative Eigenschaften."
        },
        "mechanism_of_action": {
            "en": "Activates hypothalamic POMC/CART neurons involved in anorexigenic signalling, reducing food intake and improving energy balance. Anti-apoptotic via inhibition of cytochrome c release from mitochondria. Antioxidant by reducing ROS production in the mitochondrial electron transport chain. Levels are regulated by physiological stress and aging.",
            "de": "Aktiviert hypothalamische POMC/CART-Neuronen, die an anorexigener Signalgebung beteiligt sind, reduziert Nahrungsaufnahme und verbessert Energiebilanz. Antiapoptotisch durch Hemmung der Cytochrom-c-Freisetzung aus Mitochondrien. Antioxidativ durch Reduktion der ROS-Produktion."
        },
        "indications": [
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Improves energy homeostasis and insulin sensitivity in preclinical models", "description_de": "Verbessert Energiehomöostase und Insulinsensitivität in präklinischen Modellen"},
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Anorexigenic hypothalamic stimulation reduces food intake", "description_de": "Anorexigene Hypothalamus-Stimulation reduziert Nahrungsaufnahme"},
            {"condition_en": "Age-related Metabolic Decline", "condition_de": "Altersbedingte metabolische Abnahme", "description_en": "Restoration of declining mitochondrial peptide levels", "description_de": "Wiederherstellung sinkender mitochondrialer Peptidspiegel"}
        ],
        "benefits": [
            {"benefit_en": "Mitochondria-encoded — endogenous origin", "benefit_de": "Mitochondrial kodiert — endogene Herkunft"},
            {"benefit_en": "Regulates hypothalamic energy sensing", "benefit_de": "Reguliert hypothalamisches Energiesensing"},
            {"benefit_en": "Anti-apoptotic and antioxidant", "benefit_de": "Antiapoptotisch und antioxidativ"},
            {"benefit_en": "Declines with aging — supplementation may restore youthful levels", "benefit_de": "Sinkt mit dem Altern — Supplementierung kann jugendliche Spiegel wiederherstellen"}
        ],
        "side_effects": [
            {"name_en": "Unknown (preclinical only)", "name_de": "Unbekannt (nur präklinisch)", "severity": "unknown", "frequency": "unknown", "description_en": "No human safety data", "description_de": "Keine Humansicherheitsdaten"}
        ],
        "dosage": {
            "starting_dose": "Preclinical only — no human dose established",
            "maintenance_dose": "Preclinical only",
            "frequency_en": "Research only",
            "frequency_de": "Nur Forschung",
            "route_en": "Subcutaneous (preclinical)",
            "route_de": "Subkutan (präklinisch)",
            "notes_en": "No validated human dosing. Preclinical studies use 1–10 mg/kg SC in rodent models.",
            "notes_de": "Kein validiertes Humandosierungsprotokoll. Präklinische Studien verwenden 1–10 mg/kg SC in Nagetiermodellen."
        },
        "contraindications": [
            {"en": "No human data — use with extreme caution", "de": "Keine Humandaten — äußerste Vorsicht"}
        ],
        "drug_interactions": ["Unknown"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Preclinical research stage. Emerging interest as longevity/metabolic peptide.", "notes_de": "Präklinisches Forschungsstadium. Wachsendes Interesse als Langlebigkeits-/metabolisches Peptid."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~2,500 Da",
        "amino_acid_count": "~20",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -20°C.", "de": "Lyophilisiert: -20°C."},
        "availability": "Emerging research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 8. PNC-27 ──────────────────────────────────────────────────────────────
    {
        "name": "PNC-27",
        "slug": "pnc-27",
        "category": "Oncology Research / Experimental",
        "description": {
            "en": "PNC-27 is a synthetic dual-domain anticancer peptide consisting of the HDM-2-binding domain of p53 (residues 12–26) fused to a membrane-penetrating domain. It selectively induces necrosis in cancer cells expressing surface HDM-2 while leaving normal cells unharmed. Currently preclinical with no human trials.",
            "de": "PNC-27 ist ein synthetisches zweifach-domänen-Antikrebspeptid, bestehend aus der HDM-2-Bindungsdomäne von p53 (Reste 12–26) fusioniert mit einer membrandurchdringenden Domäne. Es induziert selektiv Nekrose in Krebszellen, die oberflächliches HDM-2 exprimieren."
        },
        "mechanism_of_action": {
            "en": "The p53 domain (aa 12–26) binds HDM-2 expressed on the cancer cell surface membrane (a feature absent in normal cells). The membrane-penetrating domain creates pores in the lipid bilayer, leading to rapid tumour cell necrosis independent of apoptosis. Selectivity is conferred by differential surface HDM-2 expression.",
            "de": "Die p53-Domäne (aa 12–26) bindet HDM-2, das auf der Krebszell-Oberflächenmembran exprimiert wird (ein Merkmal, das in normalen Zellen fehlt). Die membrandurchdringende Domäne erzeugt Poren im Lipid-Bilayer und führt zu rascher Tumorzell-Nekrose."
        },
        "indications": [
            {"condition_en": "Cancer (preclinical research)", "condition_de": "Krebs (präklinische Forschung)", "description_en": "Selective anticancer activity in multiple cancer cell lines expressing surface HDM-2", "description_de": "Selektive Antikrebsaktivität in mehreren Krebszelllinien, die oberflächliches HDM-2 exprimieren"}
        ],
        "benefits": [
            {"benefit_en": "Selective for cancer cells expressing surface HDM-2", "benefit_de": "Selektiv für Krebszellen mit oberflächlichem HDM-2"},
            {"benefit_en": "Apoptosis-independent necrosis mechanism", "benefit_de": "Apoptose-unabhängiger Nekrose-Mechanismus"},
            {"benefit_en": "Spares normal HDM-2-negative cells", "benefit_de": "Schont normale HDM-2-negative Zellen"},
            {"benefit_en": "IC50 ~12.4 μM in cervical cancer cells (2025 data)", "benefit_de": "IC50 ~12,4 μM in Zervixkarzinom-Zellen (2025 Daten)"}
        ],
        "side_effects": [
            {"name_en": "Unknown (no human data)", "name_de": "Unbekannt (keine Humandaten)", "severity": "unknown", "frequency": "unknown", "description_en": "No human safety profile available", "description_de": "Kein Humansicherheitsprofil verfügbar"}
        ],
        "dosage": {
            "starting_dose": "Experimental only",
            "maintenance_dose": "Experimental only",
            "frequency_en": "Experimental — intratumoral in animal models",
            "frequency_de": "Experimentell — intratumoral in Tiermodellen",
            "route_en": "Experimental (intratumoral / intravenous in animal models)",
            "route_de": "Experimentell (intratumoral / intravenös in Tiermodellen)",
            "notes_en": "No validated human dosing. In vitro concentrations 10–500 mcg/mL.",
            "notes_de": "Kein validiertes Humandosierungsprotokoll. In-vitro-Konzentrationen 10–500 mcg/mL."
        },
        "contraindications": [
            {"en": "Human use not established — experimental compound", "de": "Humaneinsatz nicht etabliert — experimentelle Verbindung"}
        ],
        "drug_interactions": ["Unknown"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Preclinical anticancer peptide. No IND filed. Research-only compound.", "notes_de": "Präklinisches Antikrebspeptid. Kein IND eingereicht. Nur Forschungsverbindung."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~3,200 Da",
        "amino_acid_count": "~30",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -20°C. Stable at -80°C long-term.", "de": "Lyophilisiert: -20°C. Langzeitstabil bei -80°C."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 9. Thymopentin (TP-5) ──────────────────────────────────────────────────
    {
        "name": "Thymopentin (TP-5)",
        "slug": "thymopentin",
        "category": "Immunomodulator",
        "description": {
            "en": "Thymopentin (TP-5) is a synthetic pentapeptide corresponding to the active site of thymopoietin (residues 32–36): Arg-Lys-Asp-Val-Tyr. It restores immune function by promoting T-lymphocyte maturation and has been used clinically for rheumatoid arthritis, systemic lupus erythematosus, and HIV-related immunodeficiency.",
            "de": "Thymopentin (TP-5) ist ein synthetisches Pentapeptid, das dem aktiven Zentrum von Thymopoietin (Reste 32–36) entspricht: Arg-Lys-Asp-Val-Tyr. Es stellt Immunfunktion durch Förderung der T-Lymphozyten-Reifung wieder her und wurde klinisch bei rheumatoider Arthritis, SLE und HIV-bedingter Immundefizienz eingesetzt."
        },
        "mechanism_of_action": {
            "en": "Binds thymopoietin receptor on immature thymocytes. Induces T-cell differentiation from pre-T cells, normalising the CD4+/CD8+ ratio. Stimulates IL-2 secretion and upregulates IL-2R. Modulates B-cell and NK cell activity. Reduces autoantibody production in autoimmune conditions.",
            "de": "Bindet Thymopoietin-Rezeptor auf unreifen Thymozyten. Induziert T-Zell-Differenzierung von Prä-T-Zellen, normalisiert das CD4+/CD8+-Verhältnis. Stimuliert IL-2-Sekretion und hochreguliert IL-2R. Moduliert B-Zell- und NK-Zell-Aktivität."
        },
        "indications": [
            {"condition_en": "Rheumatoid Arthritis", "condition_de": "Rheumatoide Arthritis", "description_en": "Clinical trials showed improvement in T-cell ratios and disease activity", "description_de": "Klinische Studien zeigten Verbesserung der T-Zell-Verhältnisse und Krankheitsaktivität"},
            {"condition_en": "Systemic Lupus Erythematosus", "condition_de": "Systemischer Lupus erythematodes", "description_en": "Immunomodulation of autoimmune dysregulation", "description_de": "Immunmodulation der Autoimmun-Dysregulation"},
            {"condition_en": "HIV / AIDS Immunodeficiency", "condition_de": "HIV/AIDS-Immundefizienz", "description_en": "CD4+ T-cell restoration in HIV-positive patients", "description_de": "CD4+-T-Zell-Wiederherstellung bei HIV-positiven Patienten"},
            {"condition_en": "Recurrent Respiratory Infections", "condition_de": "Rezidivierende Atemwegsinfektionen", "description_en": "Prevention of recurrent infections via immune normalisation", "description_de": "Prävention rezidivierender Infektionen durch Immunnormalisierung"}
        ],
        "benefits": [
            {"benefit_en": "Restores T-cell CD4+/CD8+ balance", "benefit_de": "Stellt T-Zell CD4+/CD8+-Balance wieder her"},
            {"benefit_en": "Well-studied with multiple human clinical trials", "benefit_de": "Gut untersucht mit mehreren Humankliniken"},
            {"benefit_en": "Reduces autoimmune activity without immunosuppression", "benefit_de": "Reduziert Autoimmunaktivität ohne Immunsuppression"},
            {"benefit_en": "Stimulates NK cell and B-cell function", "benefit_de": "Stimuliert NK-Zell- und B-Zellfunktion"}
        ],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local pain and erythema", "description_de": "Lokaler Schmerz und Erythem"},
            {"name_en": "Mild fever", "name_de": "Leichtes Fieber", "severity": "mild", "frequency": "uncommon", "description_en": "Transient low-grade fever post-injection", "description_de": "Vorübergehendes leichtes Fieber nach Injektion"},
            {"name_en": "Autoimmune flare risk", "name_de": "Autoimmun-Aufflamm-Risiko", "severity": "moderate", "frequency": "rare", "description_en": "Theoretical risk in active severe autoimmune disease", "description_de": "Theoretisches Risiko bei aktiver schwerer Autoimmunerkrankung"}
        ],
        "dosage": {
            "starting_dose": "50 mg IM daily",
            "maintenance_dose": "50 mg IM daily for 5–30 days",
            "frequency_en": "Daily IM injection for defined course",
            "frequency_de": "Tägliche IM-Injektion für definierten Kurs",
            "route_en": "Intramuscular injection",
            "route_de": "Intramuskuläre Injektion",
            "notes_en": "Clinical trials used 50 mg IM daily. Research community uses lower doses (1–50 mg).",
            "notes_de": "Klinische Studien verwendeten 50 mg IM täglich. Community verwendet niedrigere Dosen (1–50 mg)."
        },
        "contraindications": [
            {"en": "Active severe autoimmune conditions without medical supervision", "de": "Aktive schwere Autoimmunerkrankungen ohne ärztliche Aufsicht"},
            {"en": "Organ transplant recipients on immunosuppression", "de": "Organtransplantationsempfänger unter Immunsuppression"}
        ],
        "drug_interactions": ["Immunosuppressants (functional antagonism)", "Corticosteroids"],
        "research_status": {"phase": "Clinical (approved in some countries)", "fda_approved": False, "ema_approved": False, "notes_en": "Multiple completed human clinical trials. Approved as Timunox in some countries.", "notes_de": "Mehrere abgeschlossene Humankliniken. Als Timunox in einigen Ländern zugelassen."},
        "manufacturer": "Various; Timunox formulation",
        "molecular_weight": "679.8 Da",
        "amino_acid_count": "5",
        "half_life": "~30 minutes",
        "storage_conditions": {"en": "Lyophilised: -20°C. Solutions: 2–8°C, use within 24 hours.", "de": "Lyophilisiert: -20°C. Lösungen: 2–8°C, innerhalb von 24 Stunden verwenden."},
        "availability": "Research peptide; approved in select countries",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 10. Abaloparatide ──────────────────────────────────────────────────────
    {
        "name": "Abaloparatide",
        "slug": "abaloparatide",
        "category": "Bone / Endocrine",
        "description": {
            "en": "Abaloparatide (BA058) is a synthetic 34-amino-acid analogue of parathyroid hormone-related protein (PTHrP), FDA-approved in 2017 for postmenopausal osteoporosis with high fracture risk. It preferentially activates the RG conformation of the PTH1R receptor, promoting bone formation with a lower risk of hypercalcaemia than teriparatide.",
            "de": "Abaloparatid (BA058) ist ein synthetisches 34-Aminosäure-Analogon des Parathormon-verwandten Proteins (PTHrP), von der FDA 2017 für postmenopausale Osteoporose mit hohem Frakturrisiko zugelassen. Es aktiviert bevorzugt die RG-Konformation des PTH1R-Rezeptors und fördert Knochenbildung mit geringerem Hyperkalzämie-Risiko als Teriparatid."
        },
        "mechanism_of_action": {
            "en": "Selective agonist of PTH1R, preferentially stabilising the transient RG (G-protein coupled) receptor conformation. This results in a more transient cAMP signal vs teriparatide, promoting anabolic bone formation (osteoblast activation) with reduced resorption side effects. Activates Wnt and BMP pathways secondarily.",
            "de": "Selektiver Agonist des PTH1R, der bevorzugt die transiente RG-Rezeptorkonformation stabilisiert. Dies führt zu einem transienteren cAMP-Signal vs. Teriparatid, fördert anabole Knochenbildung (Osteoblasten-Aktivierung) mit reduzierten Resorptions-Nebenwirkungen."
        },
        "indications": [
            {"condition_en": "Postmenopausal Osteoporosis", "condition_de": "Postmenopausale Osteoporose", "description_en": "FDA-approved for women with high fracture risk", "description_de": "FDA-zugelassen für Frauen mit hohem Frakturrisiko"},
            {"condition_en": "Osteoporosis in Men", "condition_de": "Osteoporose bei Männern", "description_en": "Under investigation for male osteoporosis", "description_de": "In Untersuchung für männliche Osteoporose"},
            {"condition_en": "Glucocorticoid-induced Osteoporosis", "condition_de": "Glukokortikoid-induzierte Osteoporose", "description_en": "Research into steroid-induced bone loss", "description_de": "Forschung bei steroid-induziertem Knochenverlust"}
        ],
        "benefits": [
            {"benefit_en": "FDA-approved anabolic bone agent (2017)", "benefit_de": "FDA-zugelassenes anaboles Knochenmittel (2017)"},
            {"benefit_en": "Reduces vertebral fractures by 86% and non-vertebral by 43% vs placebo", "benefit_de": "Reduziert Wirbelbrüche um 86% und nicht-vertebrale um 43% vs. Placebo"},
            {"benefit_en": "Lower hypercalcaemia risk vs teriparatide", "benefit_de": "Geringeres Hyperkalzämie-Risiko vs. Teriparatid"},
            {"benefit_en": "Transdermal patch formulation available (Tymlos patch)", "benefit_de": "Transdermale Pflasterformulierung verfügbar (Tymlos-Pflaster)"}
        ],
        "side_effects": [
            {"name_en": "Hypercalcaemia", "name_de": "Hyperkalzämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Elevated serum calcium, monitor levels", "description_de": "Erhöhtes Serumkalzium, Spiegel überwachen"},
            {"name_en": "Nausea / Dizziness", "name_de": "Übelkeit / Schwindel", "severity": "mild", "frequency": "common", "description_en": "Postural hypotension and GI effects", "description_de": "Orthostatische Hypotonie und GI-Effekte"},
            {"name_en": "Osteosarcoma risk (theoretical, rodent data)", "name_de": "Osteosarkom-Risiko (theoretisch, Nagetierdaten)", "severity": "severe", "frequency": "rare", "description_en": "Black box warning: osteosarcoma in rats at high doses; limit use to ≤2 years", "description_de": "Schwarze-Box-Warnung: Osteosarkom in Ratten bei hohen Dosen; Anwendung auf ≤2 Jahre begrenzen"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local erythema and pain", "description_de": "Lokale Rötung und Schmerz"}
        ],
        "dosage": {
            "starting_dose": "80 mcg SC daily",
            "maintenance_dose": "80 mcg SC once daily",
            "frequency_en": "Once daily subcutaneous injection (approved protocol)",
            "frequency_de": "Einmal täglich subkutane Injektion (zugelassenes Protokoll)",
            "route_en": "Subcutaneous injection; transdermal patch (investigational)",
            "route_de": "Subkutane Injektion; transdermales Pflaster (in Untersuchung)",
            "notes_en": "Maximum treatment duration 2 years (lifetime). Must be followed by antiresorptive therapy.",
            "notes_de": "Maximale Behandlungsdauer 2 Jahre (Lebenszeit). Muss von antiresorptiver Therapie gefolgt werden."
        },
        "contraindications": [
            {"en": "Paget's disease of bone", "de": "Paget-Krankheit des Knochens"},
            {"en": "Unexplained alkaline phosphatase elevation", "de": "Ungeklärte Alkalische-Phosphatase-Erhöhung"},
            {"en": "Prior radiation therapy involving skeleton", "de": "Frühere Strahlentherapie des Skeletts"},
            {"en": "Bone metastases or skeletal malignancy", "de": "Knochenmetastasen oder Skelettmalignome"},
            {"en": "Hypercalcaemia", "de": "Hyperkalzämie"}
        ],
        "drug_interactions": ["Digoxin (hypercalcaemia potentiates toxicity)", "Loop diuretics", "Calcium supplements (adjust timing)"],
        "research_status": {"phase": "FDA-Approved (2017)", "fda_approved": True, "ema_approved": False, "notes_en": "FDA-approved as Tymlos for postmenopausal osteoporosis. Not EMA approved.", "notes_de": "FDA-zugelassen als Tymlos für postmenopausale Osteoporose. Nicht EMA-zugelassen."},
        "manufacturer": "Radius Health / AstraZeneca",
        "molecular_weight": "3,961 Da",
        "amino_acid_count": "34",
        "half_life": "~1.7 hours",
        "storage_conditions": {"en": "Pre-filled pen: 2–8°C. Once punctured: room temperature up to 30°C for 30 days.", "de": "Vorgeladener Pen: 2–8°C. Nach Anbruch: Raumtemperatur bis 30°C für 30 Tage."},
        "availability": "Prescription (FDA-approved, US and some international markets)",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 11. GDF-11 ─────────────────────────────────────────────────────────────
    {
        "name": "GDF-11 (Growth Differentiation Factor 11)",
        "slug": "gdf-11",
        "category": "Longevity / Regenerative",
        "description": {
            "en": "GDF-11 is a TGF-β superfamily member that gained significant attention from 2013–2014 parabiosis experiments suggesting it reverses cardiac and skeletal muscle aging. Subsequent research has been conflicted, with some studies confirming rejuvenation effects and others failing to replicate. Circulating levels and their age-related changes remain debated.",
            "de": "GDF-11 ist ein TGF-β-Superfamilienmitglied, das durch Parabiose-Experimente 2013–2014 Aufmerksamkeit erhielt, die auf Umkehrung von Herz- und Skelettmuskel-Alterung hindeuteten. Nachfolgende Forschung war widersprüchlich."
        },
        "mechanism_of_action": {
            "en": "Binds ActRIIB receptor, activating SMAD2/3 signalling. In cardiac muscle, reduces hypertrophic hypertrophy markers (ACTA1) that increase with age. Proposed to activate muscle satellite cells and neural progenitors. However, it also inhibits muscle growth via myostatin-like SMAD pathway activation — making net effects highly context-dependent.",
            "de": "Bindet ActRIIB-Rezeptor, aktiviert SMAD2/3-Signalgebung. Im Herzmuskel reduziert es hypertrophische Marker (ACTA1), die mit dem Alter zunehmen. Aktiviert Satellitenzellen und neuronale Vorläufer, hemmt aber auch Muskelwachstum über Myostatin-ähnliche SMAD-Aktivierung."
        },
        "indications": [
            {"condition_en": "Age-related Cardiac Hypertrophy", "condition_de": "Altersbedingte Herzhypertrophie", "description_en": "Reduction of age-related hypertrophic gene expression in cardiac tissue", "description_de": "Reduktion altersbedingter hypertrophischer Genexpression im Herzgewebe"},
            {"condition_en": "Brain Aging / Neurogenesis", "condition_de": "Gehirnalterung / Neurogenese", "description_en": "Potential improvement of hippocampal neurogenesis via GDF-11/ActRIIB signalling", "description_de": "Mögliche Verbesserung der hippocampalen Neurogenese durch GDF-11/ActRIIB-Signalgebung"},
            {"condition_en": "Longevity Research", "condition_de": "Langlebigkeitsforschung", "description_en": "Parabiosis model suggesting circulating factor rejuvenation", "description_de": "Parabiose-Modell, das auf Verjüngung durch zirkulierende Faktoren hindeutet"}
        ],
        "benefits": [
            {"benefit_en": "Reduces age-related cardiac gene expression markers", "benefit_de": "Reduziert altersbedingte kardiäre Genexpressionsmarker"},
            {"benefit_en": "May promote hippocampal neurogenesis", "benefit_de": "Kann hippocampale Neurogenese fördern"},
            {"benefit_en": "Interesting longevity mechanism via systemic circulation", "benefit_de": "Interessanter Langlebigkeitsmechanismus über systemische Zirkulation"}
        ],
        "side_effects": [
            {"name_en": "Muscle mass reduction (myostatin-like)", "name_de": "Muskelmasse-Reduktion (myostatin-ähnlich)", "severity": "moderate", "frequency": "common", "description_en": "GDF-11 activates the same receptor as myostatin and may reduce muscle mass at higher doses", "description_de": "GDF-11 aktiviert denselben Rezeptor wie Myostatin und kann bei höheren Dosen Muskelmasse reduzieren"},
            {"name_en": "Unknown systemic effects (no human trials)", "name_de": "Unbekannte systemische Effekte (keine Humanstudien)", "severity": "unknown", "frequency": "unknown", "description_en": "No human safety profile", "description_de": "Kein Humansicherheitsprofil"}
        ],
        "dosage": {
            "starting_dose": "Preclinical only",
            "maintenance_dose": "Preclinical only",
            "frequency_en": "Research only — no human protocol established",
            "frequency_de": "Nur Forschung — kein Humanprotokoll etabliert",
            "route_en": "Subcutaneous (preclinical)",
            "route_de": "Subkutan (präklinisch)",
            "notes_en": "No validated human dosing exists. Research peptide only. Conflicting data on optimal dosing and net effects.",
            "notes_de": "Kein validiertes Humandosierungsprotokoll. Nur Forschungspeptid. Widersprüchliche Daten über optimale Dosierung."
        },
        "contraindications": [
            {"en": "Human use not validated — research compound", "de": "Humaneinsatz nicht validiert — Forschungsverbindung"},
            {"en": "Muscle wasting conditions (myostatin-like inhibition may worsen)", "de": "Muskelabbauzustände (Myostatin-ähnliche Hemmung kann verschlimmern)"}
        ],
        "drug_interactions": ["Myostatin inhibitors (additive muscle loss)", "ACE-031, follistatin (opposing effects)"],
        "research_status": {"phase": "Preclinical (highly debated)", "fda_approved": False, "ema_approved": False, "notes_en": "Highly debated longevity factor. Multiple groups failed to replicate initial findings. Research-only compound.", "notes_de": "Hoch umstrittener Langlebigkeitsfaktor. Mehrere Gruppen konnten Ausgangsbefunde nicht replizieren."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~25 kDa (processed dimer)",
        "amino_acid_count": "~109 (processed form)",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -80°C recommended. Reconstituted: 2–8°C, use within 1 week.", "de": "Lyophilisiert: -80°C empfohlen. Rekonstituiert: 2–8°C, innerhalb einer Woche verwenden."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 12. Ghrelin ────────────────────────────────────────────────────────────
    {
        "name": "Ghrelin",
        "slug": "ghrelin",
        "category": "Metabolic / GH Secretagogue",
        "description": {
            "en": "Ghrelin is the endogenous ligand of the growth hormone secretagogue receptor (GHS-R1a), produced primarily by gastric X/A-like cells. It is the only known circulating orexigenic hormone, stimulating appetite, GH secretion, and gastric motility. The acylated form (acyl-ghrelin) is the active GH-releasing isoform; des-acyl ghrelin has separate metabolic actions.",
            "de": "Ghrelin ist der endogene Ligand des Wachstumshormon-Sekretaogen-Rezeptors (GHS-R1a), hauptsächlich von gastrischen X/A-ähnlichen Zellen produziert. Es ist das einzige bekannte zirkulierende orexigene Hormon, das Appetit, GH-Sekretion und gastrische Motilität stimuliert."
        },
        "mechanism_of_action": {
            "en": "Acyl-ghrelin binds GHS-R1a (Gq-coupled), triggering intracellular Ca²⁺ release and PKC activation. In the hypothalamus, activates NPY/AgRP neurons (orexigenic) and inhibits POMC neurons. In the pituitary, synergises with GHRH to amplify GH pulses. Regulates gastric emptying via vagal pathways. Des-acyl ghrelin acts via different, less characterised receptors.",
            "de": "Acyl-Ghrelin bindet GHS-R1a (Gq-gekoppelt), löst intrazelluläre Ca²⁺-Freisetzung und PKC-Aktivierung aus. Im Hypothalamus aktiviert es NPY/AgRP-Neuronen (orexigen) und hemmt POMC-Neuronen. In der Hypophyse synergiert es mit GHRH zur Amplifikation von GH-Pulsen."
        },
        "indications": [
            {"condition_en": "Cachexia / Appetite Stimulation", "condition_de": "Kachexie / Appetitstimulation", "description_en": "Ghrelin analogues under development for cancer cachexia and COPD", "description_de": "Ghrelin-Analoga in Entwicklung für Kachexie und COPD"},
            {"condition_en": "Gastroparesis", "condition_de": "Gastroparese", "description_en": "Ghrelin agonists (relamorelin) in Phase 3 for diabetic gastroparesis", "description_de": "Ghrelin-Agonisten (Relamorelin) in Phase 3 für diabetische Gastroparese"},
            {"condition_en": "Growth Hormone Deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Endogenous GH-releasing hormone; native ghrelin infusions studied in GHD", "description_de": "Endogenes GH-freisetzungshormon; native Ghrelin-Infusionen bei Wachstumshormonmangel untersucht"}
        ],
        "benefits": [
            {"benefit_en": "Most potent endogenous GH releaser in combination with GHRH", "benefit_de": "Stärkster endogener GH-Freisetzer in Kombination mit GHRH"},
            {"benefit_en": "Appetite stimulation and gastric motility improvement", "benefit_de": "Appetitstimulation und Verbesserung der gastrischen Motilität"},
            {"benefit_en": "Cardioprotective effects (direct GHS-R1a on cardiomyocytes)", "benefit_de": "Kardioprotektive Effekte (direktes GHS-R1a auf Kardiomyozyten)"},
            {"benefit_en": "Anti-inflammatory via GHS-R1a on macrophages", "benefit_de": "Entzündungshemmend über GHS-R1a auf Makrophagen"}
        ],
        "side_effects": [
            {"name_en": "Increased appetite and weight gain", "name_de": "Gesteigerter Appetit und Gewichtszunahme", "severity": "mild", "frequency": "common", "description_en": "Primary pharmacodynamic effect — dose-dependent", "description_de": "Primärer pharmakodynamischer Effekt — dosisabhängig"},
            {"name_en": "Elevated cortisol and prolactin", "name_de": "Erhöhtes Cortisol und Prolaktin", "severity": "mild", "frequency": "common", "description_en": "Secondary hormonal effects distinct from cleaner GHS peptides", "description_de": "Sekundäre hormonelle Effekte im Gegensatz zu saubereren GHS-Peptiden"},
            {"name_en": "Nausea at high doses", "name_de": "Übelkeit bei hohen Dosen", "severity": "mild", "frequency": "uncommon", "description_en": "Gastric motility stimulation at supratherapeutic doses", "description_de": "Gastrische Motilitätsstimulation bei supratherapeutischen Dosen"}
        ],
        "dosage": {
            "starting_dose": "100 mcg IV or SC (research)",
            "maintenance_dose": "100–300 mcg SC",
            "frequency_en": "Research protocols vary; typically once daily or pulsatile IV",
            "frequency_de": "Forschungsprotokolle variieren; typischerweise einmal täglich oder pulsatile IV",
            "route_en": "Intravenous (research studies); subcutaneous (community use)",
            "route_de": "Intravenös (Forschungsstudien); subkutan (Community-Einsatz)",
            "notes_en": "Native ghrelin must be kept at -20°C and has very short t½ (~30 min SC). Synthetic analogues (GHRP-6, Ipamorelin) are preferred for GH stimulation.",
            "notes_de": "Natives Ghrelin muss bei -20°C gelagert werden und hat sehr kurze HWZ (~30 min SC). Synthetische Analoga (GHRP-6, Ipamorelin) bevorzugt für GH-Stimulation."
        },
        "contraindications": [
            {"en": "Active malignancy (orexigenic effect may support tumour growth)", "de": "Aktive Malignome (orexigener Effekt kann Tumorwachstum unterstützen)"},
            {"en": "Obesity without concomitant cachexia indication", "de": "Adipositas ohne gleichzeitige Kachexie-Indikation"}
        ],
        "drug_interactions": ["GHRH analogues (synergistic GH release)", "Somatostatin analogues (antagonism)", "Insulin (opposing metabolic effects)"],
        "research_status": {"phase": "Research / Clinical analogues in trials", "fda_approved": False, "ema_approved": False, "notes_en": "Native ghrelin not approved. Synthetic analogues (relamorelin) in Phase 3. MK-677 (ibutamoren) is an oral ghrelin mimetic.", "notes_de": "Natives Ghrelin nicht zugelassen. Synthetische Analoga (Relamorelin) in Phase 3."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "3,370 Da (acylated form)",
        "amino_acid_count": "28",
        "half_life": "~30 minutes (SC)",
        "storage_conditions": {"en": "Lyophilised: -80°C recommended. Reconstituted: 2–8°C, use within 24 hours. Very labile.", "de": "Lyophilisiert: -80°C empfohlen. Rekonstituiert: 2–8°C, innerhalb von 24 Stunden verwenden."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 13. Lanreotide ─────────────────────────────────────────────────────────
    {
        "name": "Lanreotide",
        "slug": "lanreotide",
        "category": "Somatostatin Analogue / Endocrine",
        "description": {
            "en": "Lanreotide (Somatuline) is a synthetic long-acting somatostatin analogue, FDA-approved for acromegaly, neuroendocrine tumours (NET), and pancreatic NET. It inhibits GH, IGF-1, insulin, glucagon, and gastrin secretion. Available as a deep SC depot injection releasing active drug for 28 days.",
            "de": "Lanreotid (Somatuline) ist ein synthetisches langwirksames Somatostatin-Analogon, FDA-zugelassen für Akromegalie, neuroendokrine Tumoren (NET) und pankreatische NET. Es hemmt die Sekretion von GH, IGF-1, Insulin, Glukagon und Gastrin."
        },
        "mechanism_of_action": {
            "en": "Selectively binds somatostatin receptor subtypes SSTR2 (primary) and SSTR5, which are widely expressed on pituitary somatotrophs and neuroendocrine tumour cells. Receptor activation inhibits adenylyl cyclase (Gi-coupled), reducing intracellular cAMP and thereby suppressing hormone and peptide secretion and tumour cell proliferation.",
            "de": "Bindet selektiv Somatostatin-Rezeptorsubtypen SSTR2 (primär) und SSTR5, die auf hypophysären Somatotrophen und neuroendokrinen Tumorzellen exprimiert sind. Rezeptoraktivierung hemmt Adenylyl-Cyclase, reduziert intrazelluläres cAMP und unterdrückt Hormon- und Peptidsekretion sowie Tumorzellproliferation."
        },
        "indications": [
            {"condition_en": "Acromegaly", "condition_de": "Akromegalie", "description_en": "FDA-approved for GH/IGF-1 normalisation", "description_de": "FDA-zugelassen zur GH/IGF-1-Normalisierung"},
            {"condition_en": "Neuroendocrine Tumours (NET)", "condition_de": "Neuroendokrine Tumoren (NET)", "description_en": "FDA-approved for unresectable/metastatic GEP-NET", "description_de": "FDA-zugelassen für nicht resezierbare/metastatische GEP-NET"},
            {"condition_en": "Carcinoid Syndrome", "condition_de": "Karzinoid-Syndrom", "description_en": "Controls flushing and diarrhoea", "description_de": "Kontrolliert Hitzewallungen und Durchfall"},
            {"condition_en": "ADPKD (Polycystic Kidney)", "condition_de": "ADPKD (Polyzystische Niere)", "description_en": "Slows kidney cyst growth (approved in EU)", "description_de": "Verlangsamt Nierenzystenwachstum (in EU zugelassen)"}
        ],
        "benefits": [
            {"benefit_en": "FDA-approved for acromegaly, GEP-NET, and pancreatic NET", "benefit_de": "FDA-zugelassen für Akromegalie, GEP-NET und pankreatische NET"},
            {"benefit_en": "Monthly dosing via autogel depot formulation", "benefit_de": "Monatliche Dosierung über Autogel-Depot-Formulierung"},
            {"benefit_en": "Reduces GH/IGF-1 levels and tumour volume", "benefit_de": "Reduziert GH/IGF-1-Spiegel und Tumorvolumen"},
            {"benefit_en": "EU-approved for ADPKD kidney cyst progression", "benefit_de": "EU-zugelassen für ADPKD-Nierenzystenprogression"}
        ],
        "side_effects": [
            {"name_en": "Gallstones (cholelithiasis)", "name_de": "Gallensteine (Cholelithiasis)", "severity": "moderate", "frequency": "common", "description_en": "Reduced gallbladder motility; biliary monitoring recommended", "description_de": "Reduzierte Gallenblasenmotilität; biliäre Überwachung empfohlen"},
            {"name_en": "GI symptoms (diarrhoea, flatulence)", "name_de": "GI-Symptome (Durchfall, Blähungen)", "severity": "mild", "frequency": "common", "description_en": "Reduced digestive enzyme secretion", "description_de": "Reduzierte Verdauungsenzymsekretion"},
            {"name_en": "Hyperglycaemia or hypoglycaemia", "name_de": "Hyperglykämie oder Hypoglykämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Disruption of insulin/glucagon balance", "description_de": "Störung der Insulin/Glukagon-Balance"},
            {"name_en": "Bradycardia", "name_de": "Bradykardie", "severity": "mild", "frequency": "uncommon", "description_en": "Somatostatin-mediated cardiac rate reduction", "description_de": "Somatostatin-vermittelte kardiäre Frequenzreduktion"}
        ],
        "dosage": {
            "starting_dose": "60–90 mg deep SC every 28 days",
            "maintenance_dose": "60–120 mg deep SC every 28 days",
            "frequency_en": "Once every 28 days (deep subcutaneous injection by healthcare provider)",
            "frequency_de": "Einmal alle 28 Tage (tiefe subkutane Injektion durch medizinisches Fachpersonal)",
            "route_en": "Deep subcutaneous injection (Autogel formulation)",
            "route_de": "Tiefe subkutane Injektion (Autogel-Formulierung)",
            "notes_en": "Healthcare provider-administered deep SC injection in buttock. Dose adjusted based on GH/IGF-1 response.",
            "notes_de": "Von medizinischem Fachpersonal verabreichte tiefe SC-Injektion in die Gesäßregion. Dosisanpassung nach GH/IGF-1-Ansprechen."
        },
        "contraindications": [
            {"en": "Known hypersensitivity to lanreotide or excipients", "de": "Bekannte Überempfindlichkeit gegenüber Lanreotid oder Hilfsstoffen"},
            {"en": "Uncontrolled diabetes during dose initiation", "de": "Unkontrollierter Diabetes bei Therapiebeginn"}
        ],
        "drug_interactions": ["Cyclosporin (reduced oral bioavailability)", "Antidiabetics (glucose monitoring required)", "Bromocriptine (additive GH reduction)", "QT-prolonging drugs"],
        "research_status": {"phase": "FDA-Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA-approved as Somatuline Depot. EMA-approved as Somatuline Autogel. Also EMA-approved for ADPKD.", "notes_de": "FDA-zugelassen als Somatuline Depot. EMA-zugelassen als Somatuline Autogel. Auch EMA-zugelassen für ADPKD."},
        "manufacturer": "Ipsen",
        "molecular_weight": "1,096 Da",
        "amino_acid_count": "8 (cyclic octapeptide)",
        "half_life": "23–30 days (depot formulation)",
        "storage_conditions": {"en": "Refrigerate 2–8°C. Protect from light. Allow to reach room temperature 30 min before injection.", "de": "Kühl bei 2–8°C lagern. Vor Licht schützen. 30 Minuten vor Injektion auf Raumtemperatur erwärmen."},
        "availability": "Prescription (FDA/EMA approved)",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 14. FGL Peptide (NCAM-derived) ─────────────────────────────────────────
    {
        "name": "FGL Peptide",
        "slug": "fgl-peptide",
        "category": "Nootropic / Neuroprotective",
        "description": {
            "en": "FGL is a 15-amino-acid synthetic peptide derived from the FG loop of the fibronectin type III module 2 domain of NCAM (neural cell adhesion molecule). It activates the FGFR1 receptor and enhances hippocampal long-term potentiation (LTP), synaptic plasticity, and spatial memory in rodent models. No human trials completed.",
            "de": "FGL ist ein 15-Aminosäure-synthetisches Peptid aus der FG-Schleife des Fibronektin-Typ-III-Modul-2-Domäne von NCAM (Neuronales Zelladhäsionsmolekül). Es aktiviert den FGFR1-Rezeptor und verbessert hippocampale LTP, synaptische Plastizität und räumliches Gedächtnis in Nagetiermodellen."
        },
        "mechanism_of_action": {
            "en": "Mimics NCAM's FGFR1 activation sequence without binding NCAM's polysialic acid site. Triggers FGFR1→PI3K/Akt→mTOR signalling for synaptic protein synthesis. Enhances NMDAR-dependent LTP at Schaffer collateral–CA1 synapses. Promotes post-injury hippocampal neurogenesis. May reduce neuroinflammation via microglial modulation.",
            "de": "Imitiert NCAM's FGFR1-Aktivierungssequenz ohne Bindung an NCAM's polysialic-Säure-Stelle. Löst FGFR1→PI3K/Akt→mTOR-Signalgebung für synaptische Proteinsynthese aus. Verbessert NMDAR-abhängige LTP an Schaffer-Kollateralen–CA1-Synapsen."
        },
        "indications": [
            {"condition_en": "Alzheimer's Disease / Cognitive Decline", "condition_de": "Alzheimer / Kognitiver Abbau", "description_en": "Preclinical neuroprotection and memory improvement", "description_de": "Präklinische Neuroprotektion und Gedächtnisverbesserung"},
            {"condition_en": "Cognitive Enhancement", "condition_de": "Kognitive Verbesserung", "description_en": "LTP enhancement and memory consolidation in rodent models", "description_de": "LTP-Verbesserung und Gedächtniskonsolidierung in Nagetiermodellen"},
            {"condition_en": "Traumatic Brain Injury", "condition_de": "Schädel-Hirn-Trauma", "description_en": "Post-injury hippocampal recovery in animal studies", "description_de": "Post-Trauma hippocampale Erholung in Tierstudien"}
        ],
        "benefits": [
            {"benefit_en": "Selective FGFR1 activation (non-mitogenic, safe profile)", "benefit_de": "Selektive FGFR1-Aktivierung (nicht-mitogen, sicheres Profil)"},
            {"benefit_en": "Enhances hippocampal LTP and spatial memory", "benefit_de": "Verbessert hippocampale LTP und räumliches Gedächtnis"},
            {"benefit_en": "Promotes neurogenesis post-injury", "benefit_de": "Fördert Neurogenese nach Trauma"},
            {"benefit_en": "Small peptide size allows potential CNS penetration", "benefit_de": "Kleine Peptidgröße ermöglicht potenzielle ZNS-Penetration"}
        ],
        "side_effects": [
            {"name_en": "Unknown (no human data)", "name_de": "Unbekannt (keine Humandaten)", "severity": "unknown", "frequency": "unknown", "description_en": "Preclinical compound only", "description_de": "Nur präklinische Verbindung"}
        ],
        "dosage": {
            "starting_dose": "No human protocol",
            "maintenance_dose": "No human protocol",
            "frequency_en": "Research only — animal studies use 2–10 mg/kg SC",
            "frequency_de": "Nur Forschung — Tierstudien verwenden 2–10 mg/kg SC",
            "route_en": "Subcutaneous (animal studies); intranasal (theoretical)",
            "route_de": "Subkutan (Tierstudien); intranasal (theoretisch)",
            "notes_en": "No validated human dosing. Emerging nootropic research peptide.",
            "notes_de": "Kein validiertes Humandosierungsprotokoll. Aufkommendes nootropes Forschungspeptid."
        },
        "contraindications": [
            {"en": "No human use data — preclinical only", "de": "Keine Humandaten — nur präklinisch"}
        ],
        "drug_interactions": ["Theoretical: FGFR inhibitors (anticancer drugs, e.g. erdafitinib)"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Preclinical nootropic peptide. No IND or human trials.", "notes_de": "Präklinisches nootropes Peptid. Keine IND oder Humanstudien."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~2,400 Da",
        "amino_acid_count": "15",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -20°C.", "de": "Lyophilisiert: -20°C."},
        "availability": "Research peptide",
        "created_at": NOW, "updated_at": NOW
    },

    # ── 15. P21 Peptide ────────────────────────────────────────────────────────
    {
        "name": "P21 Peptide",
        "slug": "p21-peptide",
        "category": "Nootropic / Neuroprotective",
        "description": {
            "en": "P21 is a synthetic peptide derived from ciliary neurotrophic factor (CNTF), designed to penetrate the blood–brain barrier and mimic CNTF's neurogenic and tau-lowering effects without the systemic inflammatory drawbacks of full CNTF. In Alzheimer's animal models, P21 increases hippocampal neurogenesis, reduces tau phosphorylation and amyloid-beta, and rescues synaptic plasticity.",
            "de": "P21 ist ein synthetisches Peptid aus dem Ciliary Neurotrophic Factor (CNTF), das die Blut-Hirn-Schranke überwinden und CNTFs neurogene und tau-senkende Effekte ohne systemische entzündliche Nachteile von vollem CNTF imitieren soll."
        },
        "mechanism_of_action": {
            "en": "Binds CNTFR-α on neural stem cells and neurons, activating JAK2/STAT3 and PI3K/Akt pathways. Promotes hippocampal neural stem cell differentiation into neurons rather than astrocytes. Reduces tau hyperphosphorylation at AD-relevant epitopes (Ser199, Thr231) via GSK-3β inhibition. Reduces amyloid-beta plaque burden in transgenic AD mice.",
            "de": "Bindet CNTFR-α auf neuralen Stammzellen und Neuronen, aktiviert JAK2/STAT3 und PI3K/Akt-Wege. Fördert hippocampale neurale Stammzell-Differenzierung in Neuronen statt Astrozyten. Reduziert Tau-Hyperphosphorylierung via GSK-3β-Hemmung. Reduziert Amyloid-beta-Plaques in transgenen AD-Mäusen."
        },
        "indications": [
            {"condition_en": "Alzheimer's Disease", "condition_de": "Alzheimer-Erkrankung", "description_en": "Preclinical reduction of tau, amyloid, and synaptic deficit", "description_de": "Präklinische Reduktion von Tau, Amyloid und synaptischem Defizit"},
            {"condition_en": "Down Syndrome Cognitive Impairment", "condition_de": "Kognitive Beeinträchtigung bei Down-Syndrom", "description_en": "Improved neurogenesis in mouse models of trisomy 21", "description_de": "Verbesserte Neurogenese in Mausmodellen der Trisomie 21"},
            {"condition_en": "Cognitive Enhancement", "condition_de": "Kognitive Verbesserung", "description_en": "Hippocampal neurogenesis promotion in healthy rodents", "description_de": "Förderung der hippocampalen Neurogenese bei gesunden Nagetieren"}
        ],
        "benefits": [
            {"benefit_en": "Crosses blood–brain barrier (unlike full CNTF)", "benefit_de": "Überquert die Blut-Hirn-Schranke (im Gegensatz zu vollem CNTF)"},
            {"benefit_en": "Reduces tau phosphorylation and amyloid-beta", "benefit_de": "Reduziert Tau-Phosphorylierung und Amyloid-beta"},
            {"benefit_en": "Promotes hippocampal neurogenesis", "benefit_de": "Fördert hippocampale Neurogenese"},
            {"benefit_en": "Rescues synaptic plasticity and memory in AD mouse models", "benefit_de": "Stellt synaptische Plastizität und Gedächtnis in AD-Mausmodellen wieder her"}
        ],
        "side_effects": [
            {"name_en": "Unknown (no human data)", "name_de": "Unbekannt (keine Humandaten)", "severity": "unknown", "frequency": "unknown", "description_en": "No human safety profile — preclinical only", "description_de": "Kein Humansicherheitsprofil — nur präklinisch"}
        ],
        "dosage": {
            "starting_dose": "No human protocol established",
            "maintenance_dose": "No human protocol established",
            "frequency_en": "Research only — animal studies: 0.05–0.2 mg/kg intranasal",
            "frequency_de": "Nur Forschung — Tierstudien: 0,05–0,2 mg/kg intranasal",
            "route_en": "Intranasal (animal studies); subcutaneous",
            "route_de": "Intranasal (Tierstudien); subkutan",
            "notes_en": "Emerging nootropic peptide. Community research use not well established.",
            "notes_de": "Aufkommendes nootropes Peptid. Community-Forschungseinsatz nicht gut etabliert."
        },
        "contraindications": [
            {"en": "Human use not validated", "de": "Humaneinsatz nicht validiert"}
        ],
        "drug_interactions": ["Theoretical: GSK-3β inhibitors (lithium — additive tau lowering)"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Preclinical Alzheimer's research peptide. No human trials.", "notes_de": "Präklinisches Alzheimer-Forschungspeptid. Keine Humanstudien."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~2,800 Da",
        "amino_acid_count": "~22",
        "half_life": "Unknown",
        "storage_conditions": {"en": "Lyophilised: -20°C. Reconstituted: 2–8°C.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C."},
        "availability": "Emerging research peptide",
        "created_at": NOW, "updated_at": NOW
    },
]

# ── Load, merge, and save ──────────────────────────────────────────────────────
with open("peptides_export.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_slugs = {p.get("slug") for p in existing}
added = 0
for p in NEW_PEPTIDES:
    if p["slug"] not in existing_slugs:
        existing.append(p)
        added += 1
        print(f"  + Added: {p['name']}")
    else:
        print(f"  ~ Skipped (exists): {p['name']}")

with open("peptides_export.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"\nDone. Added {added} peptides. Total: {len(existing)}")
