"""Add 12 new peptides/compounds from Crystal Peptides shop."""
import json, re
from datetime import datetime

NOW = datetime.utcnow().isoformat()

def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

NEW_PEPTIDES = [
    {
        "name": "HGH (Somatropin)",
        "slug": "hgh-somatropin",
        "category": "Growth Hormone",
        "description": {
            "en": "Human Growth Hormone (HGH), also known as somatropin, is a 191-amino acid peptide hormone produced by somatotroph cells in the anterior pituitary gland. It is essential for growth, cell reproduction, and regeneration. Recombinant HGH (rHGH) is FDA-approved for GH deficiency in adults and children, Turner syndrome, and HIV-associated wasting.",
            "de": "Humanes Wachstumshormon (HGH), auch Somatropin genannt, ist ein 191-Aminosäuren-Peptidhormon, das von Somatotrophen im Hypophysenvorderlappen produziert wird. Es ist essenziell für Wachstum, Zellreproduktion und Regeneration. Rekombinantes HGH ist für GH-Mangel bei Erwachsenen und Kindern, Turner-Syndrom und HIV-assoziierte Kachexie zugelassen."
        },
        "mechanism_of_action": {
            "en": "Binds to the GH receptor (a class I cytokine receptor), activating JAK2/STAT5 signaling pathways. Stimulates IGF-1 production in the liver, promotes lipolysis, increases protein synthesis, and enhances nitrogen retention. Also has direct anabolic effects on muscle and bone independent of IGF-1.",
            "de": "Bindet an den GH-Rezeptor (Klasse-I-Zytokinrezeptor) und aktiviert JAK2/STAT5-Signalwege. Stimuliert IGF-1-Produktion in der Leber, fördert Lipolyse, steigert Proteinsynthese und verbessert Stickstoffretention. Hat auch direkte anabole Effekte auf Muskel und Knochen unabhängig von IGF-1."
        },
        "indications": [
            {"condition_en": "Growth Hormone Deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Adult and childhood GHD with proven hypopituitarism", "description_de": "Erwachsener und kindlicher GHD mit nachgewiesener Hypophyseninsuffizienz"},
            {"condition_en": "Turner Syndrome", "condition_de": "Turner-Syndrom", "description_en": "Short stature in girls with Turner syndrome", "description_de": "Kleinwuchs bei Mädchen mit Turner-Syndrom"},
            {"condition_en": "HIV Wasting Syndrome", "condition_de": "HIV-Wasting-Syndrom", "description_en": "Treatment of muscle wasting in HIV/AIDS", "description_de": "Behandlung von Muskelschwund bei HIV/AIDS"},
            {"condition_en": "Anti-Aging / Body Composition", "condition_de": "Anti-Aging / Körperzusammensetzung", "description_en": "Off-label research for lean mass and fat loss", "description_de": "Off-Label-Forschung für Magermasse und Fettabbau"}
        ],
        "benefits": [
            {"benefit_en": "Increases lean muscle mass", "benefit_de": "Erhöht die Magermuskulatur"},
            {"benefit_en": "Reduces visceral and subcutaneous fat", "benefit_de": "Reduziert viszerales und subkutanes Fett"},
            {"benefit_en": "Improves bone mineral density", "benefit_de": "Verbessert die Knochenmineraldichte"},
            {"benefit_en": "Enhances recovery and wound healing", "benefit_de": "Verbessert Erholung und Wundheilung"},
            {"benefit_en": "Improves energy levels and quality of life", "benefit_de": "Verbessert Energieniveau und Lebensqualität"}
        ],
        "side_effects": [
            {"name_en": "Fluid Retention / Edema", "name_de": "Flüssigkeitsretention / Ödeme", "severity": "moderate", "frequency": "common", "description_en": "Peripheral edema especially in early use", "description_de": "Periphere Ödeme besonders bei Behandlungsbeginn"},
            {"name_en": "Carpal Tunnel Syndrome", "name_de": "Karpaltunnelsyndrom", "severity": "moderate", "frequency": "uncommon", "description_en": "Nerve compression from fluid retention", "description_de": "Nervenkompression durch Flüssigkeitsretention"},
            {"name_en": "Insulin Resistance", "name_de": "Insulinresistenz", "severity": "moderate", "frequency": "uncommon", "description_en": "Can elevate blood glucose levels", "description_de": "Kann den Blutzuckerspiegel erhöhen"},
            {"name_en": "Acromegaly (chronic overdose)", "name_de": "Akromegalie (chronische Überdosierung)", "severity": "severe", "frequency": "rare", "description_en": "Abnormal bone and tissue growth with supraphysiologic doses", "description_de": "Abnormales Knochen- und Gewebewachstum bei übermäßigen Dosen"},
            {"name_en": "Injection Site Reactions", "name_de": "Injektionsstellen-Reaktionen", "severity": "mild", "frequency": "common", "description_en": "Local pain, redness, swelling", "description_de": "Lokaler Schmerz, Rötung, Schwellung"}
        ],
        "dosage": {
            "starting_dose": "1–2 IU/day",
            "maintenance_dose": "2–4 IU/day",
            "frequency_en": "Once daily (preferably before sleep or post-workout)",
            "frequency_de": "Einmal täglich (vorzugsweise vor dem Schlafen oder nach dem Training)",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Typical cycles: 3–6 months. Anti-aging: 1–2 IU/day. Performance: 2–4 IU/day. Higher doses increase side effect risk.",
            "notes_de": "Typische Zyklen: 3–6 Monate. Anti-Aging: 1–2 IE/Tag. Performance: 2–4 IE/Tag. Höhere Dosen erhöhen das Nebenwirkungsrisiko."
        },
        "contraindications": [
            {"en": "Active malignancy", "de": "Aktive Malignome"},
            {"en": "Diabetic retinopathy", "de": "Diabetische Retinopathie"},
            {"en": "Acute critical illness (trauma, surgery)", "de": "Akute kritische Erkrankung (Trauma, Operation)"},
            {"en": "Closed epiphyses (in children)", "de": "Geschlossene Epiphysen (bei Kindern)"}
        ],
        "drug_interactions": ["Insulin (dosage adjustment required)", "Glucocorticoids (oppose GH effects)", "Thyroid hormones (GH may unmask hypothyroidism)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA-approved as Norditropin, Genotropin, Humatrope for specific indications. Research use for off-label applications.", "notes_de": "FDA-zugelassen als Norditropin, Genotropin, Humatrope für spezifische Indikationen."},
        "manufacturer": "Various (Novo Nordisk, Pfizer, Eli Lilly)",
        "molecular_weight": "22124 Da",
        "amino_acid_count": "191",
        "half_life": "3–5 hours (subcutaneous)",
        "storage_conditions": {"en": "Lyophilized: 2–8°C. Reconstituted: 2–8°C, use within 28 days.", "de": "Lyophilisiert: 2–8°C. Rekonstituiert: 2–8°C, innerhalb von 28 Tagen verwenden."},
        "amino_acid_sequence": "FPTIPLSRLFDNAMLRAHRLHQLAFDTYQEFEEAYIPKEQKYSFLQNPQTSLCFSESIPTPSNREETQQKSNLELLRISLLLIQSWLEPVQFLRSVFANSLVYGASDSNVYDLLKDLEEGIQTLMGRLEDGSPRTGQIFKQTYSKFDTNSHNDDALLKNYGLLYCFRKDMDKVETFLRIVQCRSVEGSCGF",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with 1–2 mL bacteriostatic water. Gently swirl, do not shake.",
            "preparation_de": "Mit 1–2 mL bakteriostatischem Wasser rekonstituieren. Sanft schwenken, nicht schütteln.",
            "storage_temperature": "2–8°C",
            "shelf_life_unopened": "24 months at 2–8°C",
            "shelf_life_reconstituted": "28 days at 2–8°C",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"},
            {"goal_en": "Fat Loss", "goal_de": "Fettabbau", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "NAD+",
        "slug": "nad-plus",
        "category": "Coenzyme / NAD Precursor",
        "description": {
            "en": "Nicotinamide Adenine Dinucleotide (NAD+) is a critical coenzyme found in all living cells, essential for cellular energy metabolism (oxidative phosphorylation), DNA repair, and gene expression regulation. NAD+ levels decline with age, and IV/subcutaneous administration is researched for anti-aging, neurological protection, and metabolic optimization.",
            "de": "Nicotinamid-Adenin-Dinukleotid (NAD+) ist ein kritisches Coenzym, das in allen lebenden Zellen vorkommt und essenziell für zelluläre Energiemetabolismus (oxidative Phosphorylierung), DNA-Reparatur und Genexpressionsregulation ist. NAD+-Spiegel sinken mit dem Alter; IV/subkutane Gabe wird für Anti-Aging und Neuroprotektion erforscht."
        },
        "mechanism_of_action": {
            "en": "Acts as an electron carrier in redox reactions, transferring electrons in glycolysis, the TCA cycle, and the electron transport chain. Activates sirtuins (SIRT1–7) which regulate gene expression, inflammation, and mitochondrial biogenesis. Also activates PARP enzymes for DNA repair and CD38 for calcium signaling.",
            "de": "Fungiert als Elektronenträger in Redoxreaktionen, überträgt Elektronen in Glykolyse, TCA-Zyklus und Elektronentransportkette. Aktiviert Sirtuine (SIRT1–7), die Genexpression, Entzündung und mitochondriale Biogenese regulieren. Aktiviert auch PARP-Enzyme für DNA-Reparatur."
        },
        "indications": [
            {"condition_en": "Age-related NAD+ Decline", "condition_de": "Altersbedingter NAD+-Abfall", "description_en": "Restoration of declining cellular NAD+ levels", "description_de": "Wiederherstellung sinkender zellulärer NAD+-Spiegel"},
            {"condition_en": "Addiction Recovery", "condition_de": "Suchtgenesung", "description_en": "IV NAD+ used in addiction treatment protocols", "description_de": "IV NAD+ in Suchtbehandlungsprotokollen"},
            {"condition_en": "Neurodegenerative Disease", "condition_de": "Neurodegenerative Erkrankungen", "description_en": "Research in Alzheimer's, Parkinson's neuroprotection", "description_de": "Forschung bei Alzheimer, Parkinson-Neuroprotektion"},
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Improving mitochondrial function in metabolic disease", "description_de": "Verbesserung der Mitochondrienfunktion bei metabolischen Erkrankungen"}
        ],
        "benefits": [
            {"benefit_en": "Boosts cellular energy (ATP production)", "benefit_de": "Steigert zelluläre Energie (ATP-Produktion)"},
            {"benefit_en": "Activates sirtuins — longevity pathways", "benefit_de": "Aktiviert Sirtuine — Langlebigkeitswege"},
            {"benefit_en": "Enhances DNA repair mechanisms", "benefit_de": "Verbessert DNA-Reparaturmechanismen"},
            {"benefit_en": "Supports neurological function and cognitive clarity", "benefit_de": "Unterstützt neurologische Funktion und kognitive Klarheit"},
            {"benefit_en": "Anti-inflammatory effects via NF-κB inhibition", "benefit_de": "Entzündungshemmende Effekte via NF-κB-Inhibition"}
        ],
        "side_effects": [
            {"name_en": "Flushing / Warmth Sensation", "name_de": "Hitzegefühl / Wärmeempfindung", "severity": "mild", "frequency": "common", "description_en": "Common with IV administration, transient", "description_de": "Häufig bei IV-Gabe, vorübergehend"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Usually dose-dependent with rapid infusion", "description_de": "Meist dosisabhängig bei schneller Infusion"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Transient, usually resolves quickly", "description_de": "Vorübergehend, löst sich normalerweise schnell"}
        ],
        "dosage": {
            "starting_dose": "250–500 mg/day",
            "maintenance_dose": "500–1000 mg/day",
            "frequency_en": "Daily injection or IV infusion for loading, then maintenance",
            "frequency_de": "Tägliche Injektion oder IV-Infusion zur Aufsättigung, dann Erhaltung",
            "route_en": "Subcutaneous injection or intravenous infusion",
            "route_de": "Subkutane Injektion oder intravenöse Infusion",
            "notes_en": "IV administration typically 500 mg–1g over 2–4 hours. Subcutaneous 50–100 mg/day for maintenance.",
            "notes_de": "IV-Gabe typischerweise 500 mg–1 g über 2–4 Stunden. Subkutan 50–100 mg/Tag zur Erhaltung."
        },
        "contraindications": [
            {"en": "Known hypersensitivity to NAD+ or niacin derivatives", "de": "Bekannte Überempfindlichkeit gegen NAD+ oder Niacin-Derivate"}
        ],
        "drug_interactions": ["PARP inhibitors (additive DNA repair effects)", "Sirtuins activators (synergistic)"],
        "research_status": {"phase": "Preclinical / Clinical Research", "fda_approved": False, "ema_approved": False, "notes_en": "Not FDA-approved as a drug. Sold as supplement. Clinical trials ongoing for various indications.", "notes_de": "Nicht FDA-zugelassen als Arzneimittel. Als Nahrungsergänzungsmittel erhältlich. Klinische Studien laufen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "663.4 Da",
        "amino_acid_count": "N/A (coenzyme)",
        "half_life": "~1–2 hours (IV), longer subcutaneous",
        "storage_conditions": {"en": "Store at -20°C, protect from light. Reconstituted: use promptly.", "de": "Bei -20°C lagern, vor Licht schützen. Rekonstituiert: sofort verwenden."},
        "reconstitution_info": {
            "preparation_en": "Dissolve in sterile water for injection. Use immediately after reconstitution.",
            "preparation_de": "In sterilem Wasser für Injektionen auflösen. Sofort nach Rekonstitution verwenden.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "Use within 24 hours",
            "light_sensitive": True,
            "solvent": "Sterile water for injection"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Cognitive Enhancement", "goal_de": "Kognitive Verbesserung", "relevance": "primary"},
            {"goal_en": "Energy & Recovery", "goal_de": "Energie & Erholung", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "Glutathione",
        "slug": "glutathione",
        "category": "Antioxidant Tripeptide",
        "description": {
            "en": "Glutathione (GSH) is a tripeptide (γ-L-glutamyl-L-cysteinyl-glycine) and the most abundant intracellular antioxidant in the human body. It plays a central role in oxidative stress defense, immune function, detoxification, and cellular health. IV/subcutaneous glutathione is researched for skin brightening, liver protection, and anti-aging applications.",
            "de": "Glutathion (GSH) ist ein Tripeptid (γ-L-Glutamyl-L-Cysteinyl-Glycin) und das häufigste intrazelluläre Antioxidans im menschlichen Körper. Es spielt eine zentrale Rolle bei der oxidativen Stressabwehr, Immunfunktion, Entgiftung und zellulärer Gesundheit."
        },
        "mechanism_of_action": {
            "en": "Acts as a reducing agent by donating electrons to reactive oxygen species (ROS), neutralizing oxidative damage. Glutathione peroxidase uses GSH to reduce hydrogen peroxide and lipid peroxides. Supports phase II detoxification by conjugating toxins for excretion. Inhibits melanin synthesis by reducing dopaquinone, accounting for skin-brightening effects.",
            "de": "Wirkt als Reduktionsmittel, indem es Elektronen an reaktive Sauerstoffspezies (ROS) spendet und oxidative Schäden neutralisiert. Glutathionperoxidase nutzt GSH zur Reduktion von Wasserstoffperoxid. Unterstützt Phase-II-Entgiftung durch Konjugation von Toxinen. Hemmt Melaninsynthese."
        },
        "indications": [
            {"condition_en": "Oxidative Stress", "condition_de": "Oxidativer Stress", "description_en": "Combating systemic oxidative damage", "description_de": "Bekämpfung von systemischen oxidativen Schäden"},
            {"condition_en": "Liver Disease", "condition_de": "Lebererkrankungen", "description_en": "Hepatoprotective effects in NAFLD and hepatitis", "description_de": "Hepatoprotektive Wirkungen bei NAFLD und Hepatitis"},
            {"condition_en": "Skin Brightening", "condition_de": "Hautaufhellung", "description_en": "Hyperpigmentation and melanin reduction", "description_de": "Hyperpigmentierung und Melaninreduktion"},
            {"condition_en": "Immune Support", "condition_de": "Immununterstützung", "description_en": "Enhancing lymphocyte function and cytokine balance", "description_de": "Verbesserung der Lymphozytenfunktion und Zytokinbalance"}
        ],
        "benefits": [
            {"benefit_en": "Powerful antioxidant — neutralizes free radicals", "benefit_de": "Starkes Antioxidans — neutralisiert freie Radikale"},
            {"benefit_en": "Liver detoxification and protection", "benefit_de": "Leberentgiftung und -schutz"},
            {"benefit_en": "Skin brightening and anti-aging", "benefit_de": "Hautaufhellung und Anti-Aging"},
            {"benefit_en": "Immune system enhancement", "benefit_de": "Immunsystemstärkung"},
            {"benefit_en": "Reduces inflammation via NF-κB pathway", "benefit_de": "Reduziert Entzündung über NF-κB-Weg"}
        ],
        "side_effects": [
            {"name_en": "Zinc Depletion (long-term)", "name_de": "Zinkverarmung (Langzeit)", "severity": "mild", "frequency": "uncommon", "description_en": "Long-term high-dose use may deplete zinc", "description_de": "Langzeit-Hochdosisanwendung kann Zink verringern"},
            {"name_en": "Allergic Reaction", "name_de": "Allergische Reaktion", "severity": "moderate", "frequency": "rare", "description_en": "Rare hypersensitivity reactions with IV use", "description_de": "Seltene Überempfindlichkeitsreaktionen bei IV-Gabe"}
        ],
        "dosage": {
            "starting_dose": "600 mg/dose",
            "maintenance_dose": "600–1200 mg/dose",
            "frequency_en": "2–3 times per week (IV) or daily (subcutaneous)",
            "frequency_de": "2–3 Mal pro Woche (IV) oder täglich (subkutan)",
            "route_en": "Intravenous or subcutaneous injection",
            "route_de": "Intravenöse oder subkutane Injektion",
            "notes_en": "Best administered IV for maximum bioavailability. Oral glutathione has limited absorption.",
            "notes_de": "Am besten IV für maximale Bioverfügbarkeit. Orales Glutathion hat begrenzte Resorption."
        },
        "contraindications": [
            {"en": "Known allergy to glutathione or its components", "de": "Bekannte Allergie gegen Glutathion oder seine Bestandteile"}
        ],
        "drug_interactions": ["Cisplatin (may reduce efficacy)", "Vitamin C (synergistic antioxidant)", "Alpha-lipoic acid (regenerates GSH)"],
        "research_status": {"phase": "Approved (some markets) / Research", "fda_approved": False, "ema_approved": False, "notes_en": "IV glutathione is used clinically in some countries. Research compound for many applications.", "notes_de": "IV Glutathion wird klinisch in einigen Ländern eingesetzt. Forschungsverbindung für viele Anwendungen."},
        "manufacturer": "Various pharmaceutical and research suppliers",
        "molecular_weight": "307.3 Da",
        "amino_acid_count": "3 (tripeptide)",
        "half_life": "~1 hour (plasma)",
        "storage_conditions": {"en": "Store at -20°C. Protect from light and oxygen. Use immediately after reconstitution.", "de": "Bei -20°C lagern. Vor Licht und Sauerstoff schützen. Sofort nach Rekonstitution verwenden."},
        "amino_acid_sequence": "Glu-Cys-Gly (γ-peptide bond)",
        "reconstitution_info": {
            "preparation_en": "Dissolve in sterile saline or water for injection. Administer promptly.",
            "preparation_de": "In steriler Kochsalzlösung oder Wasser für Injektionen auflösen. Sofort verabreichen.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "Use within 4 hours",
            "light_sensitive": True,
            "solvent": "Sterile saline or water for injection"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Skin Health", "goal_de": "Hautgesundheit", "relevance": "primary"},
            {"goal_en": "Detoxification", "goal_de": "Entgiftung", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "MOTS-c",
        "slug": "mots-c",
        "category": "Mitochondrial-Derived Peptide",
        "description": {
            "en": "MOTS-c (Mitochondrial Open Reading Frame of the 12S rRNA-c) is a 16-amino acid peptide encoded within the mitochondrial genome. It is a novel mitochondrial-derived peptide (MDP) that regulates metabolic homeostasis, insulin sensitivity, and exercise capacity. Research suggests it may mimic the metabolic effects of exercise and has anti-aging potential.",
            "de": "MOTS-c ist ein 16-Aminosäuren-Peptid, das im mitochondrialen Genom kodiert ist. Es ist ein neuartiges mitochondrial-abgeleitetes Peptid (MDP), das metabolische Homöostase, Insulinsensitivität und Trainingskapazität reguliert. Forschungen deuten darauf hin, dass es die metabolischen Effekte von Sport nachahmen kann."
        },
        "mechanism_of_action": {
            "en": "Translocates from mitochondria to the nucleus in response to metabolic stress, where it activates AMPK signaling and regulates the folate cycle and de novo purine synthesis. Inhibits the FOXO1 pathway to reduce glucose production. Activates NRF2 for antioxidant response. The 'exercise in a vial' effect comes from its ability to activate metabolic pathways similar to physical exercise.",
            "de": "Transloziert von Mitochondrien in den Nucleus als Reaktion auf metabolischen Stress, wo es AMPK-Signalgebung aktiviert und den Folsäurezyklus reguliert. Hemmt den FOXO1-Weg zur Reduktion der Glukoseproduktion. Aktiviert NRF2 für die antioxidative Antwort."
        },
        "indications": [
            {"condition_en": "Insulin Resistance / Type 2 Diabetes", "condition_de": "Insulinresistenz / Typ-2-Diabetes", "description_en": "Improving glucose metabolism and insulin sensitivity", "description_de": "Verbesserung des Glukosestoffwechsels und Insulinsensitivität"},
            {"condition_en": "Obesity & Metabolic Syndrome", "condition_de": "Adipositas & Metabolisches Syndrom", "description_en": "Weight reduction and metabolic normalization", "description_de": "Gewichtsreduktion und metabolische Normalisierung"},
            {"condition_en": "Age-related Metabolic Decline", "condition_de": "Altersbedingter metabolischer Abbau", "description_en": "Restoring youthful metabolic function", "description_de": "Wiederherstellung junger Stoffwechselfunktionen"},
            {"condition_en": "Physical Performance", "condition_de": "Körperliche Leistung", "description_en": "Exercise mimetic effects on endurance and capacity", "description_de": "Trainingsimitierende Effekte auf Ausdauer und Kapazität"}
        ],
        "benefits": [
            {"benefit_en": "Improves insulin sensitivity (exercise mimetic)", "benefit_de": "Verbessert Insulinsensitivität (Trainingsmimetikum)"},
            {"benefit_en": "Activates AMPK — key longevity pathway", "benefit_de": "Aktiviert AMPK — wichtiger Langlebigkeitsweg"},
            {"benefit_en": "Reduces body fat, particularly visceral fat", "benefit_de": "Reduziert Körperfett, insbesondere viszerales Fett"},
            {"benefit_en": "Mitochondrial biogenesis promotion", "benefit_de": "Förderung der mitochondrialen Biogenese"},
            {"benefit_en": "Anti-inflammatory via NRF2 activation", "benefit_de": "Entzündungshemmend über NRF2-Aktivierung"}
        ],
        "side_effects": [
            {"name_en": "Injection Site Discomfort", "name_de": "Unbehagen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local redness and mild pain at injection site", "description_de": "Lokale Rötung und leichter Schmerz an der Injektionsstelle"},
            {"name_en": "Hypoglycemia (potential)", "name_de": "Hypoglykämie (potenziell)", "severity": "moderate", "frequency": "rare", "description_en": "Possible blood glucose lowering in susceptible individuals", "description_de": "Mögliche Blutzuckersenkung bei empfindlichen Personen"}
        ],
        "dosage": {
            "starting_dose": "5–10 mg/week",
            "maintenance_dose": "10–20 mg/week",
            "frequency_en": "2–3 injections per week",
            "frequency_de": "2–3 Injektionen pro Woche",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Research protocols typically use 5–20 mg/week. Best administered on training days.",
            "notes_de": "Forschungsprotokolle verwenden typischerweise 5–20 mg/Woche. Am besten an Trainingstagen verabreichen."
        },
        "contraindications": [
            {"en": "Pregnancy and lactation (insufficient data)", "de": "Schwangerschaft und Stillzeit (unzureichende Daten)"},
            {"en": "Active malignancy (precaution)", "de": "Aktive Malignome (Vorsicht)"}
        ],
        "drug_interactions": ["Metformin (may have additive AMPK activation)", "Insulin (monitor blood glucose)"],
        "research_status": {"phase": "Preclinical / Early Clinical", "fda_approved": False, "ema_approved": False, "notes_en": "Discovered in 2015. Preclinical studies show strong metabolic effects. No clinical approval yet.", "notes_de": "2015 entdeckt. Präklinische Studien zeigen starke metabolische Effekte. Noch keine klinische Zulassung."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "2174 Da",
        "amino_acid_count": "16",
        "half_life": "~1–2 hours",
        "storage_conditions": {"en": "Lyophilized: -20°C. Reconstituted: 2–8°C, use within 2 weeks.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C, innerhalb von 2 Wochen verwenden."},
        "amino_acid_sequence": "MRWQEMGYIFYPRKLR",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Gentle swirl, do not shake.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Sanft schwenken, nicht schütteln.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "2 weeks at 2–8°C",
            "light_sensitive": False,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Fat Loss", "goal_de": "Fettabbau", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Metabolische Gesundheit", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "ACE-031",
        "slug": "ace-031",
        "category": "Myostatin Inhibitor / Activin Receptor Decoy",
        "description": {
            "en": "ACE-031 (Ramatercept) is a soluble form of the activin receptor type IIB (ActRIIB) fused to the Fc region of human IgG1. It acts as a decoy receptor for myostatin, activin, GDF-11, and related TGF-β superfamily members that inhibit muscle growth. Developed by Acceleron Pharma for muscle-wasting diseases including Duchenne Muscular Dystrophy.",
            "de": "ACE-031 (Ramatercept) ist eine lösliche Form des Aktivinrezeptors Typ IIB (ActRIIB), fusioniert mit der Fc-Region von humanem IgG1. Es wirkt als Körezeptor für Myostatin, Aktivin, GDF-11 und verwandte TGF-β-Superfamilienmitglieder, die das Muskelwachstum hemmen."
        },
        "mechanism_of_action": {
            "en": "Binds and sequesters myostatin, activin A/B, GDF-11, and BMP-9/-10 before they can activate the endogenous ActRIIB receptor on muscle cells. By blocking these negative regulators of muscle growth, ACE-031 disinhibits muscle hypertrophy pathways (Akt/mTOR). This leads to significant increases in muscle mass even in the absence of exercise.",
            "de": "Bindet und sequestriert Myostatin, Aktivin A/B, GDF-11 und BMP-9/-10, bevor sie den endogenen ActRIIB-Rezeptor auf Muskelzellen aktivieren können. Durch Blockierung dieser negativen Regulatoren des Muskelwachstums aktiviert ACE-031 Muskelhypertrophie-Wege (Akt/mTOR)."
        },
        "indications": [
            {"condition_en": "Duchenne Muscular Dystrophy", "condition_de": "Duchenne-Muskeldystrophie", "description_en": "Phase 2 trials for muscle preservation in DMD", "description_de": "Phase-2-Studien zur Muskelerhaltung bei DMD"},
            {"condition_en": "Sarcopenia", "condition_de": "Sarkopenie", "description_en": "Age-related muscle wasting", "description_de": "Altersbedingter Muskelschwund"},
            {"condition_en": "Cancer Cachexia", "condition_de": "Krebs-Kachexie", "description_en": "Muscle loss associated with malignancy", "description_de": "Muskelschwund bei Malignomen"},
            {"condition_en": "Research: Muscle Hypertrophy", "condition_de": "Forschung: Muskelhypertrophie", "description_en": "Performance research for extreme muscle growth", "description_de": "Leistungsforschung für extremes Muskelwachstum"}
        ],
        "benefits": [
            {"benefit_en": "Significant muscle mass increase (up to 15% in trials)", "benefit_de": "Signifikante Muskelzunahme (bis zu 15% in Studien)"},
            {"benefit_en": "Blocks myostatin and multiple growth inhibitors simultaneously", "benefit_de": "Blockiert Myostatin und mehrere Wachstumsinhibitoren gleichzeitig"},
            {"benefit_en": "Effective without exercise (relevant for disabled patients)", "benefit_de": "Wirksam ohne Sport (relevant für behinderte Patienten)"},
            {"benefit_en": "Long half-life — infrequent dosing", "benefit_de": "Lange Halbwertszeit — seltene Dosierung"}
        ],
        "side_effects": [
            {"name_en": "Nosebleeds (Epistaxis)", "name_de": "Nasenbluten (Epistaxis)", "severity": "moderate", "frequency": "common", "description_en": "Seen in Phase 2 trials, led to partial clinical hold", "description_de": "In Phase-2-Studien beobachtet, führte zu teilweisem klinischem Stopp"},
            {"name_en": "Telangiectasia", "name_de": "Teleangiektasie", "severity": "moderate", "frequency": "uncommon", "description_en": "Abnormal blood vessel dilation", "description_de": "Abnorme Blutgefäßerweiterung"},
            {"name_en": "Gum Bleeding", "name_de": "Zahnfleischbluten", "severity": "mild", "frequency": "uncommon", "description_en": "Likely due to BMP-9/-10 inhibition affecting vascular integrity", "description_de": "Wahrscheinlich durch BMP-9/-10-Inhibition, die die Gefäßintegrität beeinflusst"}
        ],
        "dosage": {
            "starting_dose": "1 mg/kg",
            "maintenance_dose": "1–3 mg/kg",
            "frequency_en": "Once every 2–4 weeks (subcutaneous)",
            "frequency_de": "Einmal alle 2–4 Wochen (subkutan)",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Research compound. Phase 2 trials used 1–3 mg/kg every 3 weeks. Development paused due to vascular side effects.",
            "notes_de": "Forschungsverbindung. Phase-2-Studien verwendeten 1–3 mg/kg alle 3 Wochen. Entwicklung pausiert wegen vaskulärer Nebenwirkungen."
        },
        "contraindications": [
            {"en": "Vascular disorders or bleeding tendencies", "de": "Gefäßerkrankungen oder Blutungsneigung"},
            {"en": "Pregnancy and lactation", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Active malignancy", "de": "Aktive Malignome"}
        ],
        "drug_interactions": ["Anticoagulants (increased bleeding risk)", "Other myostatin inhibitors (additive)"],
        "research_status": {"phase": "Phase 2 (paused)", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 2 trial in DMD was partially paused due to vascular side effects (nosebleeds, telangiectasia). Development ongoing for select indications.", "notes_de": "Phase-2-Studie bei DMD wurde teilweise wegen vaskulärer Nebenwirkungen pausiert."},
        "manufacturer": "Acceleron Pharma (acquired by Merck)",
        "molecular_weight": "~110,000 Da (fusion protein)",
        "amino_acid_count": "~500 (fusion protein)",
        "half_life": "~14 days",
        "storage_conditions": {"en": "2–8°C. Do not freeze reconstituted solution.", "de": "2–8°C. Rekonstituierte Lösung nicht einfrieren."},
        "reconstitution_info": {
            "preparation_en": "Reconstitute with sterile water for injection. Gentle swirl.",
            "preparation_de": "Mit sterilem Wasser für Injektionen rekonstituieren. Sanft schwenken.",
            "storage_temperature": "2–8°C",
            "shelf_life_unopened": "24 months at 2–8°C",
            "shelf_life_reconstituted": "28 days at 2–8°C",
            "light_sensitive": False,
            "solvent": "Sterile water for injection"
        },
        "application_goals": [
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "AICAR",
        "slug": "aicar",
        "category": "AMPK Activator / Exercise Mimetic",
        "description": {
            "en": "AICAR (5-Aminoimidazole-4-Carboxamide Ribonucleoside) is a cell-permeable nucleoside analog that activates AMP-activated protein kinase (AMPK), the master regulator of cellular energy homeostasis. Originally developed as a cardioprotective agent, AICAR gained research attention for its ability to mimic the metabolic effects of exercise, particularly in improving endurance and fat oxidation.",
            "de": "AICAR ist ein zellpermeables Nukleosidanalogon, das AMP-aktivierte Proteinkinase (AMPK) aktiviert, den Masterregulator der zellulären Energiehomöostase. Ursprünglich als kardioproteктives Mittel entwickelt, erlangte AICAR Aufmerksamkeit für seine Fähigkeit, metabolische Trainingseffekte nachzuahmen."
        },
        "mechanism_of_action": {
            "en": "AICAR is phosphorylated intracellularly to ZMP (AICAR monophosphate), which mimics AMP and activates AMPK by allosteric binding. Active AMPK promotes glucose uptake via GLUT4 translocation, enhances fatty acid oxidation, stimulates mitochondrial biogenesis via PGC-1α, and inhibits anabolic pathways (mTOR, ACC) to conserve energy.",
            "de": "AICAR wird intrazellulär zu ZMP (AICAR-Monophosphat) phosphoryliert, das AMP imitiert und AMPK durch allosterische Bindung aktiviert. Aktive AMPK fördert Glukoseaufnahme via GLUT4-Translokation, verbessert Fettsäureoxidation und stimuliert mitochondriale Biogenese via PGC-1α."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes / Insulin Resistance", "condition_de": "Typ-2-Diabetes / Insulinresistenz", "description_en": "Improving glucose uptake and insulin sensitivity", "description_de": "Verbesserung der Glukoseaufnahme und Insulinsensitivität"},
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Addressing dyslipidemia and central obesity", "description_de": "Behandlung von Dyslipidämie und zentraler Adipositas"},
            {"condition_en": "Endurance Enhancement", "condition_de": "Ausdauerverbesserung", "description_en": "Exercise mimetic for physical performance", "description_de": "Trainingsmimetikum für körperliche Leistung"},
            {"condition_en": "Cardiac Ischemia", "condition_de": "Kardiomyopathie", "description_en": "Cardioprotection during ischemia-reperfusion", "description_de": "Kardioprotektion bei Ischämie-Reperfusion"}
        ],
        "benefits": [
            {"benefit_en": "Activates AMPK — key metabolic longevity pathway", "benefit_de": "Aktiviert AMPK — wichtiger metabolischer Langlebigkeitsweg"},
            {"benefit_en": "Increases fat oxidation and endurance capacity", "benefit_de": "Erhöht Fettoxidation und Ausdauerkapazität"},
            {"benefit_en": "Improves insulin sensitivity without insulin secretion", "benefit_de": "Verbessert Insulinsensitivität ohne Insulinsekretion"},
            {"benefit_en": "Mitochondrial biogenesis (more mitochondria)", "benefit_de": "Mitochondriale Biogenese (mehr Mitochondrien)"},
            {"benefit_en": "Anti-inflammatory effects", "benefit_de": "Entzündungshemmende Effekte"}
        ],
        "side_effects": [
            {"name_en": "Lactic Acidosis (high doses)", "name_de": "Laktatazidose (hohe Dosen)", "severity": "severe", "frequency": "rare", "description_en": "High-dose use can impair lactate clearance", "description_de": "Hochdosisanwendung kann Laktateliminierung beeinträchtigen"},
            {"name_en": "Hypoglycemia", "name_de": "Hypoglykämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Enhanced glucose uptake may lower blood sugar", "description_de": "Verbesserte Glukoseaufnahme kann Blutzucker senken"},
            {"name_en": "Injection Site Reactions", "name_de": "Injektionsstellen-Reaktionen", "severity": "mild", "frequency": "common", "description_en": "Local discomfort with subcutaneous use", "description_de": "Lokales Unbehagen bei subkutaner Anwendung"}
        ],
        "dosage": {
            "starting_dose": "250–500 mg/day",
            "maintenance_dose": "500 mg/day",
            "frequency_en": "Once daily (subcutaneous injection)",
            "frequency_de": "Einmal täglich (subkutane Injektion)",
            "route_en": "Subcutaneous injection or intravenous",
            "route_de": "Subkutane Injektion oder intravenös",
            "notes_en": "Research protocols use 500 mg/day subcutaneously. Avoid use before high-intensity training as AMPK inhibits mTOR (anabolism).",
            "notes_de": "Forschungsprotokolle verwenden 500 mg/Tag subkutan. Vermeiden vor hochintensivem Training, da AMPK mTOR hemmt."
        },
        "contraindications": [
            {"en": "Kidney impairment (accumulation risk)", "de": "Niereninsuffizienz (Akkumulationsrisiko)"},
            {"en": "Concurrent metformin use (lactic acidosis risk)", "de": "Gleichzeitige Metformin-Einnahme (Laktatazidose-Risiko)"}
        ],
        "drug_interactions": ["Metformin (additive lactic acidosis risk)", "Insulin (additive hypoglycemia)", "mTOR inhibitors (overlapping pathway)"],
        "research_status": {"phase": "Preclinical / Research", "fda_approved": False, "ema_approved": False, "notes_en": "Research compound. Banned by WADA for sport. AICAR (acadesine IV) approved in some EU countries for cardiac surgery.", "notes_de": "Forschungsverbindung. Von der WADA im Sport verboten. AICAR (Acadesine IV) in einigen EU-Ländern für Herzchirurgie zugelassen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "338.2 Da",
        "amino_acid_count": "N/A (nucleoside analog)",
        "half_life": "~2–4 hours",
        "storage_conditions": {"en": "Store at -20°C. Reconstituted: 2–8°C, use within 1 week.", "de": "Bei -20°C lagern. Rekonstituiert: 2–8°C, innerhalb von 1 Woche verwenden."},
        "reconstitution_info": {
            "preparation_en": "Dissolve in sterile saline (0.9% NaCl). Use within 24 hours of reconstitution.",
            "preparation_de": "In steriler Kochsalzlösung (0,9% NaCl) auflösen. Innerhalb von 24 Stunden nach Rekonstitution verwenden.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "24–48 hours at 2–8°C",
            "light_sensitive": False,
            "solvent": "Sterile saline (0.9% NaCl)"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettabbau", "relevance": "primary"},
            {"goal_en": "Endurance", "goal_de": "Ausdauer", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Metabolische Gesundheit", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "SLU-PP-332",
        "slug": "slu-pp-332",
        "category": "ERR Agonist / Exercise Mimetic",
        "description": {
            "en": "SLU-PP-332 is a synthetic agonist of estrogen-related receptors (ERRα, ERRβ, ERRγ) — nuclear receptors that regulate mitochondrial biogenesis and oxidative metabolism. Research at Washington University showed that SLU-PP-332 dramatically increased running endurance in mice by up to 70% and promoted fat burning. It is one of the most potent exercise mimetics identified to date.",
            "de": "SLU-PP-332 ist ein synthetischer Agonist der östrogenassoziierten Rezeptoren (ERRα, ERRβ, ERRγ) — nukleäre Rezeptoren, die mitochondriale Biogenese und oxidativen Metabolismus regulieren. Forschungen an der Washington University zeigten, dass SLU-PP-332 die Laufausdauer bei Mäusen um bis zu 70% erhöhte."
        },
        "mechanism_of_action": {
            "en": "Activates all three ERR isoforms (α, β, γ), which are constitutively active nuclear receptors that drive mitochondrial gene expression programs. Activation upregulates PGC-1α co-activator networks, increasing oxidative phosphorylation capacity, slow-twitch muscle fiber composition, and fatty acid oxidation. This produces endurance improvements and metabolic benefits comparable to aerobic exercise training.",
            "de": "Aktiviert alle drei ERR-Isoformen (α, β, γ), die konstitutiv aktive nukleäre Rezeptoren sind, die mitochondriale Genexpressionsprogramme steuern. Aktivierung hochreguliert PGC-1α-Koaktivatornetzwerke und erhöht oxidative Phosphorylierungskapazität."
        },
        "indications": [
            {"condition_en": "Exercise Intolerance / Sedentary Conditions", "condition_de": "Belastungsintoleranz / Sedentäre Zustände", "description_en": "Improving metabolic fitness without physical exercise", "description_de": "Verbesserung der metabolischen Fitness ohne körperliches Training"},
            {"condition_en": "Heart Failure", "condition_de": "Herzinsuffizienz", "description_en": "Cardiac mitochondrial function improvement", "description_de": "Verbesserung der kardialen Mitochondrienfunktion"},
            {"condition_en": "Obesity / Metabolic Disease", "condition_de": "Adipositas / Metabolische Erkrankungen", "description_en": "Fat oxidation and metabolic normalization", "description_de": "Fettoxidation und metabolische Normalisierung"}
        ],
        "benefits": [
            {"benefit_en": "Up to 70% increase in endurance (preclinical)", "benefit_de": "Bis zu 70% Ausdauersteigerung (präklinisch)"},
            {"benefit_en": "Activates all three ERR isoforms simultaneously", "benefit_de": "Aktiviert alle drei ERR-Isoformen gleichzeitig"},
            {"benefit_en": "Promotes slow-twitch (endurance) muscle fiber conversion", "benefit_de": "Fördert Umwandlung in langsam zuckende (Ausdauer-) Muskelfasern"},
            {"benefit_en": "Enhanced fat oxidation and mitochondrial density", "benefit_de": "Verbesserte Fettoxidation und mitochondriale Dichte"},
            {"benefit_en": "Potential heart failure benefit", "benefit_de": "Potenzielle Herzinsuffizienz-Behandlung"}
        ],
        "side_effects": [
            {"name_en": "Unknown (limited human data)", "name_de": "Unbekannt (begrenzte Humanstudien)", "severity": "unknown", "frequency": "unknown", "description_en": "Preclinical compound. Human safety profile not yet established.", "description_de": "Präklinische Verbindung. Humane Sicherheitsprofile noch nicht festgestellt."}
        ],
        "dosage": {
            "starting_dose": "Research dose only",
            "maintenance_dose": "Animal studies: ~30 mg/kg",
            "frequency_en": "Research protocols vary",
            "frequency_de": "Forschungsprotokolle variieren",
            "route_en": "Subcutaneous injection (research)",
            "route_de": "Subkutane Injektion (Forschung)",
            "notes_en": "Human dosing not established. Preclinical compound only. No clinical trials completed.",
            "notes_de": "Humane Dosierung nicht etabliert. Nur präklinische Verbindung. Keine abgeschlossenen klinischen Studien."
        },
        "contraindications": [
            {"en": "Not for human use — preclinical compound", "de": "Nicht zur menschlichen Anwendung — präklinische Verbindung"}
        ],
        "drug_interactions": ["PGC-1α activators (additive)", "AMPK activators (complementary pathway)"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Published 2023 in Nature Metabolism. Preclinical animal studies only. No IND filed as of 2025.", "notes_de": "In Nature Metabolism 2023 veröffentlicht. Nur präklinische Tierstudien. Kein IND eingereicht (Stand 2025)."},
        "manufacturer": "Research chemical suppliers",
        "molecular_weight": "~400 Da",
        "amino_acid_count": "N/A (small molecule)",
        "half_life": "Unknown in humans",
        "storage_conditions": {"en": "Store at -20°C, away from moisture and light.", "de": "Bei -20°C lagern, von Feuchtigkeit und Licht fernhalten."},
        "reconstitution_info": {
            "preparation_en": "Dissolve in DMSO then dilute in appropriate vehicle. Specific protocol varies by study.",
            "preparation_de": "In DMSO auflösen, dann in geeignetem Trägerstoff verdünnen.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "Use promptly",
            "light_sensitive": True,
            "solvent": "DMSO / research vehicle"
        },
        "application_goals": [
            {"goal_en": "Endurance", "goal_de": "Ausdauer", "relevance": "primary"},
            {"goal_en": "Fat Loss", "goal_de": "Fettabbau", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "ARA 290",
        "slug": "ara-290",
        "category": "Erythropoietin-Derived Peptide / Neuroprotective",
        "description": {
            "en": "ARA 290 (Cibinetide) is an 11-amino acid synthetic peptide derived from the helix B region of erythropoietin (EPO). Unlike EPO itself, ARA 290 does not stimulate red blood cell production but selectively activates the tissue-protective receptor (EPOR/βcR heterodimer), providing neuroprotection, anti-inflammatory, and metabolic benefits without the thrombotic risks of EPO.",
            "de": "ARA 290 (Cibinetide) ist ein synthetisches 11-Aminosäuren-Peptid, abgeleitet von der Helix-B-Region des Erythropoietins (EPO). Anders als EPO selbst stimuliert ARA 290 keine Erythrozytenprodukton, sondern aktiviert selektiv den gewebeschutzenden Rezeptor (EPOR/βcR-Heterodimer)."
        },
        "mechanism_of_action": {
            "en": "Binds exclusively to the heteromeric tissue-protective receptor (TPR) complex consisting of EPOR and the common beta chain (βcR/CD131), without engaging the homodimeric EPOR responsible for erythropoiesis. TPR activation suppresses NF-κB signaling, reduces inflammatory cytokine production (TNF-α, IL-6), promotes neuronal survival, and enhances nerve fiber density. Also improves insulin secretion from pancreatic beta cells.",
            "de": "Bindet ausschließlich an den heteromeren gewebeschutzenden Rezeptorkomplex (TPR), bestehend aus EPOR und der gemeinsamen Betakette (βcR/CD131), ohne den homodimeren EPOR für die Erythropoiese anzusprechen. TPR-Aktivierung hemmt NF-κB-Signalgebung und reduziert Entzündungszytokine."
        },
        "indications": [
            {"condition_en": "Diabetic Peripheral Neuropathy", "condition_de": "Diabetische periphere Neuropathie", "description_en": "Phase 2/3 trials for neuropathy pain and nerve fiber recovery", "description_de": "Phase-2/3-Studien für Neuropathieschmerzen und Nervenfaserregeneration"},
            {"condition_en": "Sarcoidosis-Associated Neuropathy", "condition_de": "Sarkoidose-assoziierte Neuropathie", "description_en": "FDA Fast Track designation for sarcoidosis neuropathy", "description_de": "FDA Fast Track für Sarkoidose-Neuropathie"},
            {"condition_en": "Traumatic Brain Injury", "condition_de": "Traumatische Hirnverletzung", "description_en": "Neuroprotection and cognitive recovery", "description_de": "Neuroprotektion und kognitive Erholung"},
            {"condition_en": "Type 2 Diabetes", "condition_de": "Typ-2-Diabetes", "description_en": "Beta cell protection and metabolic improvement", "description_de": "Betazellschutz und metabolische Verbesserung"}
        ],
        "benefits": [
            {"benefit_en": "Neuroprotection without erythropoietic risk", "benefit_de": "Neuroprotektion ohne erythropoietisches Risiko"},
            {"benefit_en": "Reduces neuropathic pain", "benefit_de": "Reduziert neuropathische Schmerzen"},
            {"benefit_en": "Promotes nerve fiber regeneration (intraepidermal nerve fiber density)", "benefit_de": "Fördert Nervenfaserregeneration"},
            {"benefit_en": "Anti-inflammatory systemically", "benefit_de": "Systemisch entzündungshemmend"},
            {"benefit_en": "Improves insulin sensitivity and beta cell function", "benefit_de": "Verbessert Insulinsensitivität und Betazellfunktion"}
        ],
        "side_effects": [
            {"name_en": "Injection Site Reactions", "name_de": "Injektionsstellen-Reaktionen", "severity": "mild", "frequency": "common", "description_en": "Mild redness and discomfort at injection site", "description_de": "Leichte Rötung und Unbehagen an der Injektionsstelle"},
            {"name_en": "Flu-like Symptoms (transient)", "name_de": "Grippeähnliche Symptome (vorübergehend)", "severity": "mild", "frequency": "uncommon", "description_en": "Mild systemic reaction in early treatment", "description_de": "Milde systemische Reaktion zu Beginn der Behandlung"}
        ],
        "dosage": {
            "starting_dose": "4 mg/day",
            "maintenance_dose": "4 mg/day",
            "frequency_en": "Once daily subcutaneous injection",
            "frequency_de": "Einmal täglich subkutane Injektion",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Phase 2 trials used 4 mg/day. Treatment periods of 28 days with demonstrated benefit in sarcoidosis neuropathy.",
            "notes_de": "Phase-2-Studien verwendeten 4 mg/Tag. Behandlungsperioden von 28 Tagen mit nachgewiesenem Nutzen bei Sarkoidose-Neuropathie."
        },
        "contraindications": [
            {"en": "Known hypersensitivity to EPO-derived compounds", "de": "Bekannte Überempfindlichkeit gegen EPO-abgeleitete Verbindungen"},
            {"en": "Active malignancy (precaution)", "de": "Aktive Malignome (Vorsicht)"}
        ],
        "drug_interactions": ["Erythropoietin (avoid combination)", "NSAIDs (complementary anti-inflammatory)"],
        "research_status": {"phase": "Phase 2/3", "fda_approved": False, "ema_approved": False, "notes_en": "FDA Fast Track designation for sarcoidosis-associated neuropathy (Araim Pharmaceuticals). Phase 3 trials ongoing.", "notes_de": "FDA Fast Track für Sarkoidose-assoziierte Neuropathie (Araim Pharmaceuticals). Phase-3-Studien laufen."},
        "manufacturer": "Araim Pharmaceuticals / Research suppliers",
        "molecular_weight": "1279.4 Da",
        "amino_acid_count": "11",
        "half_life": "~3 hours",
        "storage_conditions": {"en": "Lyophilized: -20°C. Reconstituted: 2–8°C, use within 2 weeks.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C, innerhalb von 2 Wochen verwenden."},
        "amino_acid_sequence": "QEQLERALNSS",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Gentle swirl.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Sanft schwenken.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "2 weeks at 2–8°C",
            "light_sensitive": False,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Neuroprotection", "goal_de": "Neuroprotektion", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "Melanotan I (MT-1)",
        "slug": "melanotan-i-mt-1",
        "category": "Melanocortin Receptor Agonist",
        "description": {
            "en": "Melanotan I (MT-1), also known as Afamelanotide, is a synthetic analog of alpha-melanocyte-stimulating hormone (α-MSH). Unlike Melanotan II, MT-1 is more selective for the MC1R receptor and has received FDA and EMA approval (as Scenesse) for preventing phototoxicity in adults with erythropoietic protoporphyria (EPP). It provides skin tanning without requiring sun exposure.",
            "de": "Melanotan I (MT-1), auch bekannt als Afamelanotid, ist ein synthetisches Analogon des alpha-Melanozyten-stimulierenden Hormons (α-MSH). Im Gegensatz zu Melanotan II ist MT-1 selektiver für den MC1R-Rezeptor und hat FDA- und EMA-Zulassung (als Scenesse) zur Prävention von Phototoxizität bei erythropoietischer Protoporphyrie."
        },
        "mechanism_of_action": {
            "en": "Binds to and activates the melanocortin 1 receptor (MC1R) on melanocytes, triggering the cAMP/PKA signaling cascade. This promotes the switch from pheomelanin (yellow/red) to eumelanin (brown/black) production, resulting in skin darkening. Unlike Melanotan II, MT-1 has low affinity for MC3R and MC4R, avoiding sexual and appetite-related side effects.",
            "de": "Bindet und aktiviert den Melanocortin-1-Rezeptor (MC1R) auf Melanozyten und löst den cAMP/PKA-Signalweg aus. Dies fördert den Wechsel von Phäomelanin- zur Eumelanin-Produktion, was zur Hautbräunung führt. Anders als Melanotan II hat MT-1 geringe Affinität für MC3R und MC4R."
        },
        "indications": [
            {"condition_en": "Erythropoietic Protoporphyria (EPP)", "condition_de": "Erythropoietische Protoporphyrie (EPP)", "description_en": "FDA/EMA approved indication for preventing phototoxic reactions", "description_de": "FDA/EMA-zugelassene Indikation zur Prävention phototoxischer Reaktionen"},
            {"condition_en": "Photoprotection / Skin Tanning", "condition_de": "Lichtschutz / Hautbräunung", "description_en": "Off-label skin tanning and UV protection", "description_de": "Off-Label-Hautbräunung und UV-Schutz"},
            {"condition_en": "Solar Urticaria", "condition_de": "Sonnenurtikaria", "description_en": "Research for UV-sensitive skin conditions", "description_de": "Forschung bei UV-sensitiven Hauterkrankungen"}
        ],
        "benefits": [
            {"benefit_en": "FDA/EMA-approved — validated safety and efficacy", "benefit_de": "FDA/EMA-zugelassen — validierte Sicherheit und Wirksamkeit"},
            {"benefit_en": "Skin tanning without UV exposure requirement", "benefit_de": "Hautbräunung ohne UV-Exposition"},
            {"benefit_en": "Selective MC1R agonism — no sexual side effects (unlike MT-2)", "benefit_de": "Selektiver MC1R-Agonismus — keine sexuellen Nebenwirkungen (anders als MT-2)"},
            {"benefit_en": "Potentially photoprotective (eumelanin absorbs UV)", "benefit_de": "Potenziell lichtschützend (Eumelanin absorbiert UV)"},
            {"benefit_en": "Anti-inflammatory properties via MC1R", "benefit_de": "Entzündungshemmende Eigenschaften über MC1R"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common side effect, especially at start of treatment", "description_de": "Häufigste Nebenwirkung, besonders zu Beginn der Behandlung"},
            {"name_en": "Flushing", "name_de": "Hautrötung", "severity": "mild", "frequency": "common", "description_en": "Transient facial/body flushing post-injection", "description_de": "Vorübergehende Gesichts-/Körperrötung nach Injektion"},
            {"name_en": "Hyperpigmentation of existing nevi", "name_de": "Hyperpigmentierung bestehender Nävi", "severity": "moderate", "frequency": "common", "description_en": "Darkening of existing moles — requires dermatologic monitoring", "description_de": "Verdunklung bestehender Muttermale — dermatologische Überwachung erforderlich"},
            {"name_en": "Fatigue", "name_de": "Müdigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild fatigue especially with loading doses", "description_de": "Leichte Müdigkeit besonders bei Ladedosen"}
        ],
        "dosage": {
            "starting_dose": "16 mg implant (Scenesse) every 2 months",
            "maintenance_dose": "16 mg every 60 days (clinical) / 0.5–1 mg/day (research peptide)",
            "frequency_en": "Subcutaneous implant every 60 days (clinical) or daily injection (research)",
            "frequency_de": "Subkutanes Implantat alle 60 Tage (klinisch) oder tägliche Injektion (Forschung)",
            "route_en": "Subcutaneous implant (Scenesse) or subcutaneous injection (research)",
            "route_de": "Subkutanes Implantat (Scenesse) oder subkutane Injektion (Forschung)",
            "notes_en": "Research peptide vials: typically 0.5–1 mg/day for 10–20 days loading, then maintenance. Significantly milder side effect profile than MT-2.",
            "notes_de": "Forschungspeptid-Vials: typischerweise 0,5–1 mg/Tag für 10–20 Tage Aufsättigung, dann Erhaltung."
        },
        "contraindications": [
            {"en": "History of melanoma or suspicious nevi", "de": "Melanom-Vorgeschichte oder verdächtige Nävi"},
            {"en": "Pregnancy and lactation", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["Photosensitizing drugs (additive tanning)", "Immunosuppressants (precaution)"],
        "research_status": {"phase": "Approved (EPP)", "fda_approved": True, "ema_approved": True, "notes_en": "EMA approved 2014 (Scenesse, Clinuvel), FDA approved 2019 for EPP. Off-label use for skin tanning as research compound.", "notes_de": "EMA zugelassen 2014 (Scenesse, Clinuvel), FDA zugelassen 2019 für EPP. Off-Label-Anwendung zur Hautbräunung als Forschungsverbindung."},
        "manufacturer": "Clinuvel Pharmaceuticals (Scenesse) / Research suppliers",
        "molecular_weight": "1646.9 Da",
        "amino_acid_count": "13",
        "half_life": "~1 hour (injection); weeks with implant",
        "storage_conditions": {"en": "Lyophilized: -20°C. Reconstituted: 2–8°C, use within 2 weeks.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C, innerhalb von 2 Wochen verwenden."},
        "amino_acid_sequence": "Ac-Ser-Tyr-Ser-Nle-Glu-His-DPhe-Arg-Trp-Gly-Lys-Pro-Val-NH2",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Gentle swirl.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Sanft schwenken.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "2 weeks at 2–8°C",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Skin Health", "goal_de": "Hautgesundheit", "relevance": "primary"},
            {"goal_en": "Photoprotection", "goal_de": "Lichtschutz", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "HCG (Human Chorionic Gonadotropin)",
        "slug": "hcg-human-chorionic-gonadotropin",
        "category": "Glycoprotein Hormone / LH Analog",
        "description": {
            "en": "Human Chorionic Gonadotropin (hCG) is a glycoprotein hormone produced during pregnancy by the trophoblast cells of the placenta. It shares structural homology with luteinizing hormone (LH) and binds to the LH/hCG receptor. In research and clinical use, hCG is employed for testosterone stimulation, fertility treatment, testicular atrophy prevention during TRT, and cryptorchidism.",
            "de": "Humanes Choriongonadotropin (hCG) ist ein Glykoproteinhormon, das während der Schwangerschaft von Trophoblastzellen der Plazenta produziert wird. Es teilt strukturelle Homologie mit dem luteinisierenden Hormon (LH) und bindet an den LH/hCG-Rezeptor. Klinisch für Testosteronstimulation und Fertilitätsbehandlung eingesetzt."
        },
        "mechanism_of_action": {
            "en": "Binds to the LH/CG receptor (LHCGR) on Leydig cells of the testes, activating the cAMP/PKA signaling cascade to stimulate testosterone synthesis. In females, activates LH receptors on granulosa and luteal cells to trigger ovulation and progesterone production. The long half-life (20–36 hours vs 20–30 min for LH) allows for less frequent dosing.",
            "de": "Bindet an den LH/CG-Rezeptor (LHCGR) auf Leydig-Zellen der Hoden, aktiviert cAMP/PKA-Signalwege zur Stimulation der Testosteronsynthese. Bei Frauen aktiviert es LH-Rezeptoren auf Granulosa- und Lutealzellen zur Ovulationsauslösung."
        },
        "indications": [
            {"condition_en": "Hypogonadism (Male)", "condition_de": "Hypogonadismus (männlich)", "description_en": "Stimulating endogenous testosterone production", "description_de": "Stimulierung der endogenen Testosteronproduktion"},
            {"condition_en": "Fertility Treatment (Female)", "condition_de": "Fertilitätsbehandlung (weiblich)", "description_en": "Triggering ovulation in ART protocols", "description_de": "Auslösung der Ovulation in ART-Protokollen"},
            {"condition_en": "Testicular Atrophy Prevention", "condition_de": "Prävention von Hodenatrophie", "description_en": "Used alongside TRT to maintain testicular size and function", "description_de": "Begleitend zur TRT zur Erhaltung von Hodengröße und -funktion"},
            {"condition_en": "Cryptorchidism", "condition_de": "Kryptorchismus", "description_en": "Hormonal treatment for undescended testes in boys", "description_de": "Hormonelle Behandlung bei nicht herabgestiegenen Hoden"}
        ],
        "benefits": [
            {"benefit_en": "Maintains testicular function during TRT/steroid use", "benefit_de": "Erhält Hodenfunktion während TRT/Steroidanwendung"},
            {"benefit_en": "Stimulates endogenous testosterone production", "benefit_de": "Stimuliert endogene Testosteronproduktion"},
            {"benefit_en": "Aids post-cycle recovery (PCT)", "benefit_de": "Unterstützt post-zykliche Erholung (PCT)"},
            {"benefit_en": "Approved fertility treatment for men and women", "benefit_de": "Zugelassene Fertilitätsbehandlung für Männer und Frauen"},
            {"benefit_en": "Long half-life allows convenient dosing", "benefit_de": "Lange Halbwertszeit ermöglicht bequeme Dosierung"}
        ],
        "side_effects": [
            {"name_en": "Gynecomastia", "name_de": "Gynäkomastie", "severity": "moderate", "frequency": "uncommon", "description_en": "Via aromatization of stimulated testosterone to estrogen", "description_de": "Durch Aromatisierung des stimulierten Testosterons zu Östrogen"},
            {"name_en": "Ovarian Hyperstimulation Syndrome (females)", "name_de": "Ovarielles Überstimulationssyndrom (Frauen)", "severity": "severe", "frequency": "uncommon", "description_en": "Risk in ART protocols with excessive response", "description_de": "Risiko in ART-Protokollen bei übermäßiger Reaktion"},
            {"name_en": "Water Retention", "name_de": "Wassereinlagerung", "severity": "mild", "frequency": "common", "description_en": "Fluid retention with high testosterone levels", "description_de": "Flüssigkeitsretention bei hohen Testosteronspiegeln"},
            {"name_en": "Acne", "name_de": "Akne", "severity": "mild", "frequency": "common", "description_en": "Due to elevated androgen levels", "description_de": "Durch erhöhte Androgenspiegel"}
        ],
        "dosage": {
            "starting_dose": "250–500 IU every other day",
            "maintenance_dose": "500–1000 IU 2–3x/week",
            "frequency_en": "2–3 injections per week",
            "frequency_de": "2–3 Injektionen pro Woche",
            "route_en": "Subcutaneous or intramuscular injection",
            "route_de": "Subkutane oder intramuskuläre Injektion",
            "notes_en": "TRT support: 250–500 IU 2x/week. PCT: 500–1000 IU 3x/week for 2–4 weeks. Fertility protocols vary widely.",
            "notes_de": "TRT-Begleitung: 250–500 IE 2x/Woche. PCT: 500–1000 IE 3x/Woche für 2–4 Wochen."
        },
        "contraindications": [
            {"en": "Hormone-sensitive tumors (prostate, breast)", "de": "Hormonabhängige Tumoren (Prostata, Brust)"},
            {"en": "Precocious puberty", "de": "Pubertas praecox"},
            {"en": "Primary gonadal failure (Klinefelter syndrome)", "de": "Primäres Gonadenversagen (Klinefelter-Syndrom)"}
        ],
        "drug_interactions": ["Aromatase inhibitors (reduce estrogen conversion from hCG use)", "GnRH analogs (antagonistic)", "Testosterone (additive — used together in TRT protocols)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved for hypogonadism, cryptorchidism, and ART. Available as Pregnyl, Novarel, Ovidrel.", "notes_de": "FDA zugelassen für Hypogonadismus, Kryptorchismus und ART. Erhältlich als Pregnyl, Novarel, Ovidrel."},
        "manufacturer": "Organon (Pregnyl), Ferring (Ovitrelle) / Research suppliers",
        "molecular_weight": "36700 Da (glycoprotein)",
        "amino_acid_count": "237 (α+β subunits)",
        "half_life": "24–36 hours",
        "storage_conditions": {"en": "Lyophilized: 2–25°C. Reconstituted: 2–8°C, use within 30 days.", "de": "Lyophilisiert: 2–25°C. Rekonstituiert: 2–8°C, innerhalb von 30 Tagen verwenden."},
        "reconstitution_info": {
            "preparation_en": "Reconstitute with provided bacteriostatic saline or sterile water. Gently mix.",
            "preparation_de": "Mit beiliegender bakteriostatischer Kochsalzlösung oder sterilem Wasser rekonstituieren. Sanft mischen.",
            "storage_temperature": "2–8°C (reconstituted)",
            "shelf_life_unopened": "24 months at 2–25°C",
            "shelf_life_reconstituted": "30 days at 2–8°C",
            "light_sensitive": False,
            "solvent": "Bacteriostatic saline or sterile water"
        },
        "application_goals": [
            {"goal_en": "Hormonal Balance", "goal_de": "Hormonelles Gleichgewicht", "relevance": "primary"},
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "secondary"},
            {"goal_en": "Fertility", "goal_de": "Fertilität", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "5-Amino-1MQ",
        "slug": "5-amino-1mq",
        "category": "NNMT Inhibitor / Fat Loss Compound",
        "description": {
            "en": "5-Amino-1-methylquinolinium (5-Amino-1MQ) is a small molecule inhibitor of nicotinamide N-methyltransferase (NNMT), an enzyme highly expressed in white adipose tissue that regulates NAD+ metabolism and fat cell differentiation. By inhibiting NNMT, 5-Amino-1MQ increases NAD+ availability, activates SIRT1, and promotes fat mobilization. Preclinical studies show significant fat loss without loss of muscle mass.",
            "de": "5-Amino-1-Methylchinolinium (5-Amino-1MQ) ist ein Inhibitor der Nicotinamid-N-Methyltransferase (NNMT), einem Enzym, das stark in weißem Fettgewebe exprimiert wird und NAD+-Metabolismus sowie Fettzelldifferenzierung reguliert. Durch Hemmung von NNMT erhöht 5-Amino-1MQ die NAD+-Verfügbarkeit."
        },
        "mechanism_of_action": {
            "en": "Inhibits NNMT, which normally methylates nicotinamide (a NAD+ precursor) rendering it inactive. By blocking this, 5-Amino-1MQ preserves the cellular NAD+ pool, activating SIRT1 and AMPK pathways. This upregulates lipolysis in adipocytes, reduces adipogenesis, increases energy expenditure, and promotes lean body composition. Also reduces SAM (S-adenosyl methionine) depletion in fat cells.",
            "de": "Hemmt NNMT, das normalerweise Nicotinamid (ein NAD+-Vorläufer) methyliert und inaktiviert. Durch Blockierung erhält 5-Amino-1MQ den zellulären NAD+-Pool und aktiviert SIRT1- und AMPK-Wege. Dies hochreguliert Lipolyse in Adipozyten und reduziert Adipogenese."
        },
        "indications": [
            {"condition_en": "Obesity / Excess Body Fat", "condition_de": "Adipositas / Überschüssiges Körperfett", "description_en": "Targeted fat loss through NNMT inhibition", "description_de": "Gezielter Fettabbau durch NNMT-Inhibition"},
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Improving lipid profile and insulin sensitivity", "description_de": "Verbesserung des Lipidprofils und Insulinsensitivität"},
            {"condition_en": "Type 2 Diabetes", "condition_de": "Typ-2-Diabetes", "description_en": "Metabolic normalization via NAD+/SIRT1 pathway", "description_de": "Metabolische Normalisierung über NAD+/SIRT1-Weg"}
        ],
        "benefits": [
            {"benefit_en": "Targeted fat loss without muscle loss", "benefit_de": "Gezielter Fettabbau ohne Muskelverlust"},
            {"benefit_en": "Increases NAD+ availability (anti-aging effect)", "benefit_de": "Erhöht NAD+-Verfügbarkeit (Anti-Aging-Effekt)"},
            {"benefit_en": "Activates SIRT1 longevity pathway", "benefit_de": "Aktiviert SIRT1-Langlebigkeitsweg"},
            {"benefit_en": "Reduces adipocyte size and fat cell number", "benefit_de": "Reduziert Adipozytengröße und Fettzellanzahl"},
            {"benefit_en": "No stimulant effects — well tolerated in preclinical studies", "benefit_de": "Keine stimulierenden Effekte — gut verträglich in präklinischen Studien"}
        ],
        "side_effects": [
            {"name_en": "Limited human safety data", "name_de": "Begrenzte humane Sicherheitsdaten", "severity": "unknown", "frequency": "unknown", "description_en": "Preclinical compound. Human safety profile not fully established.", "description_de": "Präklinische Verbindung. Humanes Sicherheitsprofil nicht vollständig etabliert."},
            {"name_en": "Potential GI Discomfort (oral)", "name_de": "Mögliche GI-Beschwerden (oral)", "severity": "mild", "frequency": "uncommon", "description_en": "Mild gastrointestinal symptoms reported in some users", "description_de": "Milde GI-Symptome bei einigen Anwendern berichtet"}
        ],
        "dosage": {
            "starting_dose": "50–75 mg/day",
            "maintenance_dose": "50–100 mg/day",
            "frequency_en": "Once or twice daily (oral or subcutaneous)",
            "frequency_de": "Einmal oder zweimal täglich (oral oder subkutan)",
            "route_en": "Oral or subcutaneous injection",
            "route_de": "Oral oder subkutane Injektion",
            "notes_en": "Research protocols: 50 mg twice daily. Cycling recommended: 4–6 weeks on, 2 weeks off.",
            "notes_de": "Forschungsprotokolle: 50 mg zweimal täglich. Cycling empfohlen: 4–6 Wochen an, 2 Wochen aus."
        },
        "contraindications": [
            {"en": "Pregnancy and lactation", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Liver disease (NNMT is highly expressed in liver)", "de": "Lebererkrankungen (NNMT stark in der Leber exprimiert)"}
        ],
        "drug_interactions": ["NAD+ precursors (synergistic — NMN, NR)", "SIRT1 activators (resveratrol, synergistic)"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Promising preclinical data (2021 Nature Communications). No clinical trials completed as of 2025.", "notes_de": "Vielversprechende präklinische Daten (Nature Communications 2021). Keine abgeschlossenen klinischen Studien (Stand 2025)."},
        "manufacturer": "Research chemical suppliers",
        "molecular_weight": "174.2 Da",
        "amino_acid_count": "N/A (small molecule)",
        "half_life": "~4–6 hours (estimated)",
        "storage_conditions": {"en": "Store at -20°C or 2–8°C. Protect from moisture.", "de": "Bei -20°C oder 2–8°C lagern. Vor Feuchtigkeit schützen."},
        "reconstitution_info": {
            "preparation_en": "Dissolve in sterile water or DMSO for injection use.",
            "preparation_de": "In sterilem Wasser oder DMSO für Injektionsanwendung auflösen.",
            "storage_temperature": "-20°C or 2–8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "1 week at 2–8°C",
            "light_sensitive": False,
            "solvent": "Sterile water or DMSO"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettabbau", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"},
            {"goal_en": "Metabolic Health", "goal_de": "Metabolische Gesundheit", "relevance": "secondary"}
        ],
        "updated_at": NOW, "created_at": NOW
    },
    {
        "name": "PEG MGF",
        "slug": "peg-mgf",
        "category": "IGF-1 Splice Variant / PEGylated Growth Factor",
        "description": {
            "en": "PEG MGF (PEGylated Mechano Growth Factor) is a modified form of Mechano Growth Factor (MGF) — a splice variant of IGF-1 — where polyethylene glycol (PEG) is conjugated to extend its half-life from ~minutes to ~days. MGF is produced locally in muscle in response to mechanical stress, activating satellite cells for muscle repair. The PEGylated form allows systemic administration with sustained anabolic effects.",
            "de": "PEG MGF ist eine modifizierte Form des Mechano Growth Factor (MGF) — eine Spleißvariante von IGF-1 — bei der Polyethylenglykol (PEG) konjugiert wird, um die Halbwertszeit von Minuten auf Tage zu verlängern. MGF wird lokal in Muskeln als Reaktion auf mechanischen Stress produziert und aktiviert Satellitenzellen für die Muskelreparatur."
        },
        "mechanism_of_action": {
            "en": "The E-domain of MGF (unique to the MGF splice variant) activates satellite cells (muscle stem cells) independently of the IGF-1 receptor, promoting their proliferation before differentiation. The IGF-1 domain of MGF also activates IGF-1R for protein synthesis via PI3K/Akt/mTOR. PEGylation protects the peptide from proteolytic degradation, extending bioavailability and allowing systemic distribution rather than purely local effects.",
            "de": "Die E-Domäne von MGF (einzigartig für die MGF-Spleißvariante) aktiviert Satellitenzellen (Muskelstammzellen) unabhängig vom IGF-1-Rezeptor und fördert deren Proliferation. Die IGF-1-Domäne aktiviert auch IGF-1R für Proteinsynthese. PEGylierung schützt das Peptid vor proteolytischem Abbau."
        },
        "indications": [
            {"condition_en": "Muscle Repair / Injury Recovery", "condition_de": "Muskelreparatur / Verletzungserholung", "description_en": "Satellite cell activation for muscle tissue repair", "description_de": "Satellitenzellaktivierung für Muskelgewebereparatur"},
            {"condition_en": "Muscle Wasting Disorders", "condition_de": "Muskelkachexie", "description_en": "Sarcopenia, cachexia, muscular dystrophies", "description_de": "Sarkopenie, Kachexie, Muskeldystrophien"},
            {"condition_en": "Post-Exercise Muscle Hypertrophy", "condition_de": "Post-Training Muskelhypertrophie", "description_en": "Research for enhanced muscle growth response to training", "description_de": "Forschung zur verbesserten Muskelwachstumsantwort auf Training"}
        ],
        "benefits": [
            {"benefit_en": "Extended half-life vs native MGF (~days vs minutes)", "benefit_de": "Verlängerte Halbwertszeit vs. natives MGF (~Tage vs Minuten)"},
            {"benefit_en": "Systemic administration possible (unlike local MGF)", "benefit_de": "Systemische Gabe möglich (anders als lokales MGF)"},
            {"benefit_en": "Activates satellite cells for muscle stem cell proliferation", "benefit_de": "Aktiviert Satellitenzellen für Muskelstammzellproliferation"},
            {"benefit_en": "Synergistic with IGF-1 LR3 (different receptor mechanisms)", "benefit_de": "Synergistisch mit IGF-1 LR3 (unterschiedliche Rezeptormechanismen)"},
            {"benefit_en": "Promotes faster recovery from intense training", "benefit_de": "Fördert schnellere Erholung von intensivem Training"}
        ],
        "side_effects": [
            {"name_en": "Hypoglycemia (potential)", "name_de": "Hypoglykämie (potenziell)", "severity": "moderate", "frequency": "uncommon", "description_en": "Due to IGF-1-like insulin sensitizing activity", "description_de": "Durch IGF-1-ähnliche insulinsensibilisierende Aktivität"},
            {"name_en": "Injection Site Reactions", "name_de": "Injektionsstellen-Reaktionen", "severity": "mild", "frequency": "common", "description_en": "Local discomfort and mild swelling", "description_de": "Lokales Unbehagen und leichte Schwellung"},
            {"name_en": "PEG Accumulation (theoretical with frequent dosing)", "name_de": "PEG-Akkumulation (theoretisch bei häufiger Dosierung)", "severity": "mild", "frequency": "rare", "description_en": "PEG polymers can accumulate in tissues with chronic use", "description_de": "PEG-Polymere können sich bei chronischer Anwendung in Geweben anreichern"}
        ],
        "dosage": {
            "starting_dose": "200 mcg/week",
            "maintenance_dose": "200–400 mcg/week",
            "frequency_en": "Once or twice per week (subcutaneous)",
            "frequency_de": "Einmal oder zweimal pro Woche (subkutan)",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Unlike native MGF (which is injected immediately post-workout into the muscle), PEG MGF can be injected systemically on non-training days. Typical cycle: 4–6 weeks.",
            "notes_de": "Anders als natives MGF kann PEG MGF systemisch an Nicht-Trainingstagen injiziert werden. Typischer Zyklus: 4–6 Wochen."
        },
        "contraindications": [
            {"en": "Active malignancy", "de": "Aktive Malignome"},
            {"en": "Diabetic retinopathy", "de": "Diabetische Retinopathie"},
            {"en": "Pregnancy and lactation", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["IGF-1 LR3 (synergistic — combine with caution)", "Insulin (additive hypoglycemic risk)", "GH peptides (complementary growth pathway)"],
        "research_status": {"phase": "Preclinical / Research", "fda_approved": False, "ema_approved": False, "notes_en": "Research compound. No clinical trials completed. PEGylation is an established pharmaceutical technology used in approved drugs.", "notes_de": "Forschungsverbindung. Keine abgeschlossenen klinischen Studien. PEGylierung ist eine etablierte pharmazeutische Technologie."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "~5000+ Da (with PEG chain)",
        "amino_acid_count": "24 (MGF E-domain peptide)",
        "half_life": "~24–96 hours (due to PEGylation)",
        "storage_conditions": {"en": "Lyophilized: -20°C. Reconstituted: 2–8°C, use within 2 weeks.", "de": "Lyophilisiert: -20°C. Rekonstituiert: 2–8°C, innerhalb von 2 Wochen verwenden."},
        "amino_acid_sequence": "PEGylated-YQPPSTNKNTKSQRRKGSTFEEHK",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Gentle swirl, do not shake.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Sanft schwenken, nicht schütteln.",
            "storage_temperature": "-20°C",
            "shelf_life_unopened": "24 months at -20°C",
            "shelf_life_reconstituted": "2 weeks at 2–8°C",
            "light_sensitive": False,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"},
            {"goal_en": "Recovery", "goal_de": "Erholung", "relevance": "primary"}
        ],
        "updated_at": NOW, "created_at": NOW
    }
]

def main():
    with open("peptides_export.json", "r", encoding="utf-8") as f:
        existing = json.load(f)

    existing_slugs = {p["slug"] for p in existing}
    added = []
    for p in NEW_PEPTIDES:
        if p["slug"] not in existing_slugs:
            existing.append(p)
            added.append(p["name"])
        else:
            print(f"  SKIP (already exists): {p['name']}")

    with open("peptides_export.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"\nAdded {len(added)} new peptides:")
    for name in added:
        print(f"  + {name}")
    print(f"\nTotal peptides in DB: {len(existing)}")

if __name__ == "__main__":
    main()
