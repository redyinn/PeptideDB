"""Seed MongoDB with 20 scientifically accurate peptide profiles."""
import re
from datetime import datetime
from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "peptide_research"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

NOW = datetime.utcnow().isoformat()

PEPTIDES = [
    {
        "name": "Tirzepatide",
        "slug": "tirzepatide",
        "category": "GIP/GLP-1 Dual Receptor Agonist",
        "description": {
            "en": "Tirzepatide is a novel dual glucose-dependent insulinotropic polypeptide (GIP) and glucagon-like peptide-1 (GLP-1) receptor agonist. It was developed by Eli Lilly and approved by the FDA in 2022 under the brand name Mounjaro for type 2 diabetes. It has shown remarkable efficacy in weight loss, with clinical trials demonstrating up to 22.5% body weight reduction. Tirzepatide represents a new class of incretin-based therapies with dual receptor activity.",
            "de": "Tirzepatid ist ein neuartiger dualer Rezeptoragonist des glukoseabhängigen insulinotropen Polypeptids (GIP) und des Glucagon-like Peptide-1 (GLP-1). Es wurde von Eli Lilly entwickelt und 2022 von der FDA unter dem Markennamen Mounjaro für Typ-2-Diabetes zugelassen. In klinischen Studien zeigte es eine bemerkenswerte Wirksamkeit bei der Gewichtsreduktion von bis zu 22,5% des Körpergewichts. Tirzepatid repräsentiert eine neue Klasse inkretinbasierter Therapien mit dualer Rezeptoraktivität."
        },
        "mechanism_of_action": {
            "en": "Tirzepatide activates both GIP and GLP-1 receptors, enhancing insulin secretion in a glucose-dependent manner, suppressing glucagon release, slowing gastric emptying, and reducing appetite through central nervous system signaling. The dual agonism provides synergistic metabolic benefits beyond single-receptor targeting.",
            "de": "Tirzepatid aktiviert sowohl GIP- als auch GLP-1-Rezeptoren, verstärkt die glukoseabhängige Insulinsekretion, unterdrückt die Glukagonfreisetzung, verlangsamt die Magenentleerung und reduziert den Appetit durch Signalgebung im Zentralnervensystem. Der duale Agonismus bietet synergistische metabolische Vorteile gegenüber der Einzelrezeptor-Aktivierung."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "Primary indication for glycemic control in adults with T2DM", "description_de": "Primäre Indikation zur Blutzuckerkontrolle bei Erwachsenen mit T2DM"},
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Chronic weight management in adults with BMI ≥30 or ≥27 with comorbidities", "description_de": "Chronisches Gewichtsmanagement bei Erwachsenen mit BMI ≥30 oder ≥27 mit Komorbiditäten"},
            {"condition_en": "Cardiovascular Risk Reduction", "condition_de": "Kardiovaskuläre Risikoreduktion", "description_en": "Under investigation for MACE reduction in high-risk patients", "description_de": "Wird untersucht zur Reduktion schwerer kardiovaskulärer Ereignisse bei Hochrisikopatienten"}
        ],
        "benefits": [
            {"benefit_en": "Superior HbA1c reduction (up to 2.4%)", "benefit_de": "Überlegene HbA1c-Senkung (bis zu 2,4%)"},
            {"benefit_en": "Significant weight loss (up to 22.5% body weight)", "benefit_de": "Signifikante Gewichtsabnahme (bis zu 22,5% Körpergewicht)"},
            {"benefit_en": "Improved insulin sensitivity", "benefit_de": "Verbesserte Insulinsensitivität"},
            {"benefit_en": "Reduced cardiovascular risk factors", "benefit_de": "Reduzierte kardiovaskuläre Risikofaktoren"},
            {"benefit_en": "Once-weekly dosing convenience", "benefit_de": "Komfortable einmal wöchentliche Dosierung"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common side effect, usually diminishes over time", "description_de": "Häufigste Nebenwirkung, lässt meist mit der Zeit nach"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "GI disturbance typically during dose escalation", "description_de": "GI-Störung typischerweise während der Dosiseskalation"},
            {"name_en": "Decreased appetite", "name_de": "Verminderter Appetit", "severity": "mild", "frequency": "common", "description_en": "Related to mechanism of action", "description_de": "Zusammenhängend mit dem Wirkmechanismus"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "uncommon", "description_en": "Redness, swelling at injection site", "description_de": "Rötung, Schwellung an der Injektionsstelle"},
            {"name_en": "Pancreatitis", "name_de": "Pankreatitis", "severity": "severe", "frequency": "rare", "description_en": "Acute inflammation of the pancreas, requires immediate medical attention", "description_de": "Akute Entzündung der Bauchspeicheldrüse, erfordert sofortige ärztliche Behandlung"}
        ],
        "dosage": {
            "starting_dose": "2.5 mg",
            "maintenance_dose": "5-15 mg",
            "frequency_en": "Once weekly",
            "frequency_de": "Einmal wöchentlich",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Dose escalation in 2.5 mg increments every 4 weeks",
            "notes_de": "Dosiseskalation in 2,5 mg Schritten alle 4 Wochen"
        },
        "contraindications": [
            {"en": "Personal or family history of medullary thyroid carcinoma", "de": "Persönliche oder familiäre Vorgeschichte eines medullären Schilddrüsenkarzinoms"},
            {"en": "Multiple Endocrine Neoplasia syndrome type 2 (MEN 2)", "de": "Multiples Endokrines Neoplasie-Syndrom Typ 2 (MEN 2)"},
            {"en": "History of severe pancreatitis", "de": "Vorgeschichte einer schweren Pankreatitis"}
        ],
        "drug_interactions": ["Insulin (increased hypoglycemia risk)", "Sulfonylureas", "Oral medications (delayed absorption due to slowed gastric emptying)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved 2022 (Mounjaro), Zepbound for obesity 2023", "notes_de": "FDA-Zulassung 2022 (Mounjaro), Zepbound für Adipositas 2023"},
        "manufacturer": "Eli Lilly",
        "molecular_weight": "4810 Da",
        "amino_acid_count": "39",
        "half_life": "5 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C. May be stored at room temperature (up to 30°C) for 21 days.", "de": "Kühlschrank bei 2-8°C lagern. Kann bis zu 21 Tage bei Raumtemperatur (bis 30°C) aufbewahrt werden."},
        "amino_acid_sequence": "YXEGTFTSDYSIXLDKIAQKAFVQWLIAGGPSSGAPPPS",
        "reconstitution_info": {
            "preparation_en": "Pre-filled pen, no reconstitution required",
            "preparation_de": "Fertigpen, keine Rekonstitution erforderlich",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "21 days at room temperature after first use",
            "light_sensitive": True,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Semaglutide",
        "slug": "semaglutide",
        "category": "GLP-1 Receptor Agonist",
        "description": {
            "en": "Semaglutide is a GLP-1 receptor agonist developed by Novo Nordisk, available as Ozempic (injection for diabetes), Wegovy (injection for weight management), and Rybelsus (oral for diabetes). It has revolutionized obesity treatment with up to 15% body weight loss in clinical trials. Semaglutide mimics the incretin hormone GLP-1 to regulate blood sugar and appetite.",
            "de": "Semaglutid ist ein GLP-1-Rezeptoragonist von Novo Nordisk, verfügbar als Ozempic (Injektion bei Diabetes), Wegovy (Injektion zur Gewichtskontrolle) und Rybelsus (oral bei Diabetes). Es hat die Adipositasbehandlung revolutioniert mit bis zu 15% Körpergewichtsverlust in klinischen Studien. Semaglutid ahmt das Inkretinhormon GLP-1 nach, um Blutzucker und Appetit zu regulieren."
        },
        "mechanism_of_action": {
            "en": "Semaglutide binds to and activates the GLP-1 receptor, stimulating glucose-dependent insulin secretion, suppressing glucagon, delaying gastric emptying, and promoting satiety through hypothalamic appetite centers.",
            "de": "Semaglutid bindet an den GLP-1-Rezeptor und aktiviert ihn, stimuliert die glukoseabhängige Insulinsekretion, unterdrückt Glukagon, verzögert die Magenentleerung und fördert das Sättigungsgefühl über hypothalamische Appetitzentren."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "Adjunct to diet and exercise for glycemic control", "description_de": "Ergänzung zu Diät und Bewegung zur Blutzuckerkontrolle"},
            {"condition_en": "Chronic Weight Management", "condition_de": "Chronisches Gewichtsmanagement", "description_en": "Adults with BMI ≥30 or ≥27 with weight-related comorbidity", "description_de": "Erwachsene mit BMI ≥30 oder ≥27 mit gewichtsbezogener Komorbidität"},
            {"condition_en": "Cardiovascular Risk Reduction", "condition_de": "Kardiovaskuläre Risikoreduktion", "description_en": "Reduction of MACE in adults with T2DM and established CVD", "description_de": "Reduktion von MACE bei Erwachsenen mit T2DM und bestehender KHK"}
        ],
        "benefits": [
            {"benefit_en": "Effective weight loss (up to 15% body weight)", "benefit_de": "Effektiver Gewichtsverlust (bis zu 15% Körpergewicht)"},
            {"benefit_en": "Significant HbA1c reduction", "benefit_de": "Signifikante HbA1c-Senkung"},
            {"benefit_en": "Cardiovascular benefit proven in SELECT trial", "benefit_de": "Kardiovaskulärer Nutzen in SELECT-Studie nachgewiesen"},
            {"benefit_en": "Available in oral formulation (Rybelsus)", "benefit_de": "Verfügbar als orale Formulierung (Rybelsus)"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most frequent, improves with continued use", "description_de": "Am häufigsten, bessert sich bei fortgesetzter Anwendung"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "moderate", "frequency": "common", "description_en": "Often accompanies nausea during titration", "description_de": "Tritt oft zusammen mit Übelkeit während der Titration auf"},
            {"name_en": "Constipation", "name_de": "Verstopfung", "severity": "mild", "frequency": "common", "description_en": "Due to slowed gastric motility", "description_de": "Durch verlangsamte Magenmotilität"},
            {"name_en": "Gallbladder disorders", "name_de": "Gallenblasenerkrankungen", "severity": "moderate", "frequency": "uncommon", "description_en": "Cholelithiasis and cholecystitis reported", "description_de": "Cholelithiasis und Cholezystitis berichtet"},
            {"name_en": "Pancreatitis", "name_de": "Pankreatitis", "severity": "severe", "frequency": "rare", "description_en": "Rare but serious inflammation of the pancreas", "description_de": "Seltene aber schwere Entzündung der Bauchspeicheldrüse"}
        ],
        "dosage": {
            "starting_dose": "0.25 mg",
            "maintenance_dose": "0.5-2.4 mg",
            "frequency_en": "Once weekly",
            "frequency_de": "Einmal wöchentlich",
            "route_en": "Subcutaneous injection or oral tablet",
            "route_de": "Subkutane Injektion oder orale Tablette",
            "notes_en": "Titrate every 4 weeks. Wegovy max 2.4 mg, Ozempic max 2 mg",
            "notes_de": "Alle 4 Wochen titrieren. Wegovy max 2,4 mg, Ozempic max 2 mg"
        },
        "contraindications": [
            {"en": "Personal or family history of medullary thyroid carcinoma", "de": "Persönliche oder familiäre Vorgeschichte eines medullären Schilddrüsenkarzinoms"},
            {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"},
            {"en": "Hypersensitivity to semaglutide", "de": "Überempfindlichkeit gegen Semaglutid"}
        ],
        "drug_interactions": ["Insulin (hypoglycemia risk)", "Sulfonylureas", "Warfarin (monitor INR)", "Oral contraceptives (delayed absorption)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "Ozempic (2017), Rybelsus (2019), Wegovy (2021). SELECT cardiovascular outcomes trial positive.", "notes_de": "Ozempic (2017), Rybelsus (2019), Wegovy (2021). SELECT kardiovaskuläre Ergebnisstudie positiv."},
        "manufacturer": "Novo Nordisk",
        "molecular_weight": "4114 Da",
        "amino_acid_count": "31",
        "half_life": "7 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C. After first use, store below 30°C for up to 56 days.", "de": "Kühlschrank bei 2-8°C. Nach Erstgebrauch unter 30°C bis zu 56 Tage aufbewahren."},
        "amino_acid_sequence": "HXEGTFTSDVSSYLEGQAAKEFIAWLVKGRG",
        "reconstitution_info": {
            "preparation_en": "Pre-filled pen, no reconstitution needed",
            "preparation_de": "Fertigpen, keine Rekonstitution erforderlich",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "56 days after first use",
            "light_sensitive": True,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Liraglutide",
        "slug": "liraglutide",
        "category": "GLP-1 Receptor Agonist",
        "description": {
            "en": "Liraglutide is a GLP-1 receptor agonist developed by Novo Nordisk, marketed as Victoza for type 2 diabetes and Saxenda for chronic weight management. It was one of the first GLP-1 agonists to gain widespread clinical adoption. Liraglutide shares 97% sequence homology with native human GLP-1.",
            "de": "Liraglutid ist ein GLP-1-Rezeptoragonist von Novo Nordisk, vermarktet als Victoza bei Typ-2-Diabetes und Saxenda zur chronischen Gewichtskontrolle. Es war einer der ersten GLP-1-Agonisten mit breiter klinischer Anwendung. Liraglutid hat 97% Sequenzhomologie mit nativem humanem GLP-1."
        },
        "mechanism_of_action": {
            "en": "Liraglutide activates the GLP-1 receptor to enhance insulin secretion, suppress glucagon, delay gastric emptying, and promote satiety. Its fatty acid chain enables albumin binding, extending its half-life.",
            "de": "Liraglutid aktiviert den GLP-1-Rezeptor zur Verstärkung der Insulinsekretion, Unterdrückung von Glukagon, Verzögerung der Magenentleerung und Förderung des Sättigungsgefühls. Seine Fettsäurekette ermöglicht Albuminbindung und verlängert die Halbwertszeit."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "Adjunct therapy for glycemic control", "description_de": "Begleittherapie zur Blutzuckerkontrolle"},
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Weight management at 3.0 mg dose (Saxenda)", "description_de": "Gewichtsmanagement bei 3,0 mg Dosis (Saxenda)"},
            {"condition_en": "Pediatric Obesity", "condition_de": "Pädiatrische Adipositas", "description_en": "Approved for adolescents aged 12+ with obesity", "description_de": "Zugelassen für Jugendliche ab 12 Jahren mit Adipositas"}
        ],
        "benefits": [
            {"benefit_en": "Proven cardiovascular benefit (LEADER trial)", "benefit_de": "Nachgewiesener kardiovaskulärer Nutzen (LEADER-Studie)"},
            {"benefit_en": "Weight loss of 5-8% body weight", "benefit_de": "Gewichtsverlust von 5-8% des Körpergewichts"},
            {"benefit_en": "Well-established safety profile", "benefit_de": "Gut etabliertes Sicherheitsprofil"},
            {"benefit_en": "Daily dosing allows flexible dose adjustment", "benefit_de": "Tägliche Dosierung ermöglicht flexible Dosisanpassung"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common, usually transient", "description_de": "Am häufigsten, meist vorübergehend"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Occurs in early treatment phase", "description_de": "Tritt in der frühen Behandlungsphase auf"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "GI side effect during dose titration", "description_de": "GI-Nebenwirkung während der Dosistitration"},
            {"name_en": "Hypoglycemia", "name_de": "Hypoglykämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Mainly when combined with sulfonylureas or insulin", "description_de": "Hauptsächlich in Kombination mit Sulfonylharnstoffen oder Insulin"},
            {"name_en": "Thyroid C-cell tumors", "name_de": "Schilddrüsen-C-Zell-Tumore", "severity": "severe", "frequency": "rare", "description_en": "Risk observed in rodent studies, boxed warning", "description_de": "Risiko in Nagetierstudien beobachtet, Warnhinweis"}
        ],
        "dosage": {
            "starting_dose": "0.6 mg",
            "maintenance_dose": "1.2-3.0 mg",
            "frequency_en": "Once daily",
            "frequency_de": "Einmal täglich",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Victoza: max 1.8 mg. Saxenda: titrate to 3.0 mg over 5 weeks",
            "notes_de": "Victoza: max 1,8 mg. Saxenda: über 5 Wochen auf 3,0 mg titrieren"
        },
        "contraindications": [
            {"en": "Medullary thyroid carcinoma history", "de": "Vorgeschichte eines medullären Schilddrüsenkarzinoms"},
            {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"},
            {"en": "Pregnancy", "de": "Schwangerschaft"}
        ],
        "drug_interactions": ["Insulin", "Sulfonylureas", "Oral medications with narrow therapeutic index"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "Victoza approved 2010, Saxenda 2014. LEADER trial showed CV benefit.", "notes_de": "Victoza zugelassen 2010, Saxenda 2014. LEADER-Studie zeigte kardiovaskulären Nutzen."},
        "manufacturer": "Novo Nordisk",
        "molecular_weight": "3751 Da",
        "amino_acid_count": "31",
        "half_life": "13 hours",
        "storage_conditions": {"en": "Refrigerate at 2-8°C before first use. After first use, store below 30°C for up to 30 days.", "de": "Vor Erstgebrauch bei 2-8°C kühlen. Nach Erstgebrauch unter 30°C bis 30 Tage aufbewahren."},
        "amino_acid_sequence": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGR",
        "reconstitution_info": {
            "preparation_en": "Pre-filled pen, ready to use",
            "preparation_de": "Fertigpen, gebrauchsfertig",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "30 months",
            "shelf_life_reconstituted": "30 days after first use",
            "light_sensitive": True,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Dulaglutide",
        "slug": "dulaglutide",
        "category": "GLP-1 Receptor Agonist",
        "description": {
            "en": "Dulaglutide is a long-acting GLP-1 receptor agonist marketed as Trulicity by Eli Lilly. It consists of a GLP-1 analog covalently linked to a modified human IgG4 Fc fragment, providing extended duration of action. It is one of the most prescribed GLP-1 agonists globally for type 2 diabetes.",
            "de": "Dulaglutid ist ein langwirksamer GLP-1-Rezeptoragonist, vermarktet als Trulicity von Eli Lilly. Es besteht aus einem GLP-1-Analogon, das kovalent an ein modifiziertes humanes IgG4-Fc-Fragment gebunden ist. Es ist weltweit eines der am häufigsten verschriebenen GLP-1-Agonisten bei Typ-2-Diabetes."
        },
        "mechanism_of_action": {
            "en": "Dulaglutide activates the GLP-1 receptor through its GLP-1 analog moiety. The Fc fusion extends its half-life to approximately 5 days. It enhances glucose-dependent insulin secretion and suppresses glucagon.",
            "de": "Dulaglutid aktiviert den GLP-1-Rezeptor durch seine GLP-1-Analog-Komponente. Die Fc-Fusion verlängert seine Halbwertszeit auf etwa 5 Tage. Es verstärkt die glukoseabhängige Insulinsekretion und unterdrückt Glukagon."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "First-line or add-on therapy for glycemic control", "description_de": "Erst- oder Zusatztherapie zur Blutzuckerkontrolle"},
            {"condition_en": "Cardiovascular Risk Reduction", "condition_de": "Kardiovaskuläre Risikoreduktion", "description_en": "Reduction of MACE in adults with T2DM (REWIND trial)", "description_de": "Reduktion von MACE bei Erwachsenen mit T2DM (REWIND-Studie)"},
            {"condition_en": "Pre-diabetes Management", "condition_de": "Prädiabetes-Management", "description_en": "Under investigation for diabetes prevention", "description_de": "Wird zur Diabetesprävention untersucht"}
        ],
        "benefits": [
            {"benefit_en": "Simple once-weekly auto-injector", "benefit_de": "Einfacher einmal wöchentlicher Autoinjektor"},
            {"benefit_en": "No needle visible during injection", "benefit_de": "Keine sichtbare Nadel während der Injektion"},
            {"benefit_en": "Proven cardiovascular benefit (REWIND)", "benefit_de": "Nachgewiesener kardiovaskulärer Nutzen (REWIND)"},
            {"benefit_en": "Moderate weight loss (3-5 kg)", "benefit_de": "Moderate Gewichtsabnahme (3-5 kg)"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Typically mild and transient", "description_de": "Typischerweise mild und vorübergehend"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "Common GI side effect", "description_de": "Häufige GI-Nebenwirkung"},
            {"name_en": "Abdominal pain", "name_de": "Bauchschmerzen", "severity": "mild", "frequency": "common", "description_en": "Usually mild and self-limiting", "description_de": "Meist mild und selbstlimitierend"},
            {"name_en": "Decreased appetite", "name_de": "Verminderter Appetit", "severity": "mild", "frequency": "common", "description_en": "Contributes to weight loss effect", "description_de": "Trägt zum Gewichtsverlust bei"},
            {"name_en": "Acute kidney injury", "name_de": "Akute Nierenschädigung", "severity": "severe", "frequency": "rare", "description_en": "Reported in patients with dehydration from GI effects", "description_de": "Berichtet bei Patienten mit Dehydration durch GI-Effekte"}
        ],
        "dosage": {
            "starting_dose": "0.75 mg",
            "maintenance_dose": "1.5-4.5 mg",
            "frequency_en": "Once weekly",
            "frequency_de": "Einmal wöchentlich",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Single-dose pen, can be administered any time of day",
            "notes_de": "Einzeldosis-Pen, kann zu jeder Tageszeit verabreicht werden"
        },
        "contraindications": [
            {"en": "Medullary thyroid carcinoma history", "de": "Vorgeschichte eines medullären Schilddrüsenkarzinoms"},
            {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"},
            {"en": "Severe gastrointestinal disease", "de": "Schwere gastrointestinale Erkrankung"}
        ],
        "drug_interactions": ["Insulin", "Sulfonylureas", "Oral medications sensitive to delayed gastric emptying"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "Approved 2014. REWIND trial demonstrated CV benefit in broader T2DM population.", "notes_de": "Zugelassen 2014. REWIND-Studie zeigte CV-Nutzen in breiterer T2DM-Population."},
        "manufacturer": "Eli Lilly",
        "molecular_weight": "63000 Da",
        "amino_acid_count": "275",
        "half_life": "5 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C. Single-use pen, discard after use.", "de": "Kühlschrank bei 2-8°C. Einmalpen, nach Gebrauch entsorgen."},
        "amino_acid_sequence": "GLP-1 analog fused to modified IgG4-Fc fragment",
        "reconstitution_info": {
            "preparation_en": "Pre-filled single-dose pen, ready to use",
            "preparation_de": "Vorgefüllter Einzeldosis-Pen, gebrauchsfertig",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "Single use only",
            "light_sensitive": True,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Oxytocin",
        "slug": "oxytocin",
        "category": "Neuropeptide Hormone",
        "description": {
            "en": "Oxytocin is a naturally occurring neuropeptide hormone produced in the hypothalamus and released by the posterior pituitary. Known as the 'love hormone', it plays crucial roles in labor induction, lactation, social bonding, and emotional regulation. It is one of the oldest known peptide hormones, first synthesized in 1953.",
            "de": "Oxytocin ist ein natürlich vorkommendes Neuropeptidhormon, das im Hypothalamus produziert und von der Neurohypophyse freigesetzt wird. Als 'Liebeshormon' bekannt, spielt es eine entscheidende Rolle bei Wehentätigkeit, Laktation, sozialer Bindung und emotionaler Regulation. Es ist eines der ältesten bekannten Peptidhormone, erstmals 1953 synthetisiert."
        },
        "mechanism_of_action": {
            "en": "Oxytocin binds to G-protein coupled oxytocin receptors in the uterus, mammary glands, and brain. It triggers smooth muscle contraction in the uterus, stimulates milk ejection, and modulates neural circuits involved in social cognition and bonding.",
            "de": "Oxytocin bindet an G-Protein-gekoppelte Oxytocinrezeptoren in Uterus, Brustdrüsen und Gehirn. Es löst glatte Muskelkontraktion im Uterus aus, stimuliert den Milchausstoß und moduliert neuronale Schaltkreise für soziale Kognition und Bindung."
        },
        "indications": [
            {"condition_en": "Labor Induction", "condition_de": "Geburtseinleitung", "description_en": "Induction or augmentation of labor contractions", "description_de": "Einleitung oder Verstärkung von Wehentätigkeit"},
            {"condition_en": "Postpartum Hemorrhage", "condition_de": "Postpartale Blutung", "description_en": "Prevention and treatment of uterine bleeding after delivery", "description_de": "Prävention und Behandlung von Uterusblutungen nach der Entbindung"},
            {"condition_en": "Lactation Support", "condition_de": "Laktationsunterstützung", "description_en": "Stimulation of milk let-down reflex", "description_de": "Stimulation des Milchspendereflexes"}
        ],
        "benefits": [
            {"benefit_en": "Well-established safety profile over decades", "benefit_de": "Über Jahrzehnte etabliertes Sicherheitsprofil"},
            {"benefit_en": "Essential for labor and delivery management", "benefit_de": "Unverzichtbar für Geburtsmanagement"},
            {"benefit_en": "Research into social behavior and autism therapy", "benefit_de": "Forschung zu Sozialverhalten und Autismus-Therapie"},
            {"benefit_en": "Short half-life allows precise dosing control", "benefit_de": "Kurze Halbwertszeit ermöglicht präzise Dosierungskontrolle"}
        ],
        "side_effects": [
            {"name_en": "Uterine hyperstimulation", "name_de": "Uterine Überstimulation", "severity": "severe", "frequency": "uncommon", "description_en": "Excessive contractions can cause fetal distress", "description_de": "Übermäßige Kontraktionen können fetalen Distress verursachen"},
            {"name_en": "Water intoxication", "name_de": "Wasserintoxikation", "severity": "severe", "frequency": "rare", "description_en": "Antidiuretic effect at high doses can cause hyponatremia", "description_de": "Antidiuretische Wirkung bei hohen Dosen kann Hyponatriämie verursachen"},
            {"name_en": "Nausea and vomiting", "name_de": "Übelkeit und Erbrechen", "severity": "mild", "frequency": "common", "description_en": "Common during IV administration", "description_de": "Häufig bei IV-Verabreichung"},
            {"name_en": "Hypotension", "name_de": "Hypotonie", "severity": "moderate", "frequency": "uncommon", "description_en": "Transient blood pressure decrease", "description_de": "Vorübergehender Blutdruckabfall"},
            {"name_en": "Cardiac arrhythmias", "name_de": "Herzrhythmusstörungen", "severity": "severe", "frequency": "rare", "description_en": "Rare cardiac effects at high doses", "description_de": "Seltene kardiale Effekte bei hohen Dosen"}
        ],
        "dosage": {
            "starting_dose": "0.5-1 mU/min IV",
            "maintenance_dose": "1-20 mU/min IV",
            "frequency_en": "Continuous IV infusion (labor) or IM/intranasal",
            "frequency_de": "Kontinuierliche IV-Infusion (Geburt) oder IM/intranasal",
            "route_en": "Intravenous, intramuscular, or intranasal",
            "route_de": "Intravenös, intramuskulär oder intranasal",
            "notes_en": "Dose titrated based on contraction pattern during labor",
            "notes_de": "Dosis wird anhand des Kontraktionsmusters während der Geburt titriert"
        },
        "contraindications": [
            {"en": "Significant cephalopelvic disproportion", "de": "Signifikantes Kopf-Becken-Missverhältnis"},
            {"en": "Abnormal fetal presentation (transverse lie)", "de": "Abnormale fetale Lage (Querlage)"},
            {"en": "Placenta previa or vasa previa", "de": "Placenta praevia oder Vasa praevia"}
        ],
        "drug_interactions": ["Prostaglandins (synergistic uterotonic effect)", "Vasopressors", "Cyclopropane anesthesia"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "Long-established drug. Active research in autism spectrum disorder and social anxiety.", "notes_de": "Langjährig etabliertes Medikament. Aktive Forschung bei Autismus-Spektrum-Störung und sozialer Angst."},
        "manufacturer": "Various (generic)",
        "molecular_weight": "1007 Da",
        "amino_acid_count": "9",
        "half_life": "3-5 minutes",
        "storage_conditions": {"en": "Refrigerate at 2-8°C. Protect from light.", "de": "Kühlschrank bei 2-8°C. Vor Licht schützen."},
        "amino_acid_sequence": "CYIQNCPLG",
        "reconstitution_info": {
            "preparation_en": "Available as ready-to-use solution for injection",
            "preparation_de": "Verfügbar als gebrauchsfertige Injektionslösung",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "Use immediately after opening",
            "light_sensitive": True,
            "solvent": "0.9% sodium chloride for IV dilution"
        },
        "application_goals": [
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"},
            {"goal_en": "Cognitive Enhancement", "goal_de": "Kognitive Verbesserung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Insulin",
        "slug": "insulin",
        "category": "Metabolic Hormone",
        "description": {
            "en": "Insulin is a peptide hormone produced by the beta cells of the pancreatic islets of Langerhans. It is essential for glucose metabolism and is the primary treatment for type 1 diabetes and advanced type 2 diabetes. Modern insulin therapy includes rapid-acting, short-acting, intermediate, and long-acting formulations. Insulin was first isolated in 1921 by Banting and Best.",
            "de": "Insulin ist ein Peptidhormon, das von den Betazellen der Langerhans-Inseln der Bauchspeicheldrüse produziert wird. Es ist essentiell für den Glukosestoffwechsel und die primäre Behandlung für Typ-1-Diabetes und fortgeschrittenen Typ-2-Diabetes. Moderne Insulintherapie umfasst schnell-, kurz-, mittel- und langwirksame Formulierungen. Insulin wurde 1921 von Banting und Best erstmals isoliert."
        },
        "mechanism_of_action": {
            "en": "Insulin binds to the insulin receptor tyrosine kinase, triggering autophosphorylation and activation of PI3K/Akt and Ras/MAPK pathways. This promotes GLUT4 translocation for glucose uptake, glycogen synthesis, lipogenesis, and protein synthesis while inhibiting gluconeogenesis and lipolysis.",
            "de": "Insulin bindet an die Insulinrezeptor-Tyrosinkinase, löst Autophosphorylierung und Aktivierung der PI3K/Akt- und Ras/MAPK-Signalwege aus. Dies fördert die GLUT4-Translokation für Glukoseaufnahme, Glykogensynthese, Lipogenese und Proteinsynthese bei gleichzeitiger Hemmung der Glukoneogenese und Lipolyse."
        },
        "indications": [
            {"condition_en": "Type 1 Diabetes Mellitus", "condition_de": "Typ-1-Diabetes mellitus", "description_en": "Essential lifelong therapy for absolute insulin deficiency", "description_de": "Essenzielle lebenslange Therapie bei absolutem Insulinmangel"},
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "When oral agents insufficient for glycemic control", "description_de": "Wenn orale Antidiabetika zur Blutzuckerkontrolle nicht ausreichen"},
            {"condition_en": "Diabetic Ketoacidosis", "condition_de": "Diabetische Ketoazidose", "description_en": "Emergency treatment with IV insulin", "description_de": "Notfallbehandlung mit IV-Insulin"}
        ],
        "benefits": [
            {"benefit_en": "Life-saving in type 1 diabetes", "benefit_de": "Lebensrettend bei Typ-1-Diabetes"},
            {"benefit_en": "Most effective glucose-lowering therapy", "benefit_de": "Wirksamste blutzuckersenkende Therapie"},
            {"benefit_en": "Multiple formulations for flexible regimens", "benefit_de": "Multiple Formulierungen für flexible Therapieschemata"},
            {"benefit_en": "Proven to prevent microvascular complications", "benefit_de": "Nachweislich Prävention mikrovaskulärer Komplikationen"}
        ],
        "side_effects": [
            {"name_en": "Hypoglycemia", "name_de": "Hypoglykämie", "severity": "severe", "frequency": "common", "description_en": "Most significant risk, can be life-threatening", "description_de": "Bedeutendstes Risiko, kann lebensbedrohlich sein"},
            {"name_en": "Weight gain", "name_de": "Gewichtszunahme", "severity": "mild", "frequency": "common", "description_en": "Anabolic effect promotes fat storage", "description_de": "Anabole Wirkung fördert Fettspeicherung"},
            {"name_en": "Lipodystrophy", "name_de": "Lipodystrophie", "severity": "mild", "frequency": "uncommon", "description_en": "Fat tissue changes at injection sites", "description_de": "Fettgewebsveränderungen an Injektionsstellen"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Redness, swelling, itching", "description_de": "Rötung, Schwellung, Juckreiz"},
            {"name_en": "Hypokalemia", "name_de": "Hypokaliämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Insulin shifts potassium intracellularly", "description_de": "Insulin verschiebt Kalium intrazellulär"}
        ],
        "dosage": {
            "starting_dose": "0.1-0.2 U/kg/day",
            "maintenance_dose": "0.5-1.0 U/kg/day",
            "frequency_en": "Multiple daily injections or continuous pump infusion",
            "frequency_de": "Mehrfache tägliche Injektionen oder kontinuierliche Pumpeninfusion",
            "route_en": "Subcutaneous injection or IV (regular insulin only)",
            "route_de": "Subkutane Injektion oder IV (nur Normalinsulin)",
            "notes_en": "Highly individualized dosing based on blood glucose monitoring",
            "notes_de": "Hochindividualisierte Dosierung basierend auf Blutzuckerüberwachung"
        },
        "contraindications": [
            {"en": "Hypoglycemia", "de": "Hypoglykämie"},
            {"en": "Hypersensitivity to insulin or excipients", "de": "Überempfindlichkeit gegen Insulin oder Hilfsstoffe"},
            {"en": "Use during hypoglycemic episodes", "de": "Anwendung während hypoglykämischer Episoden"}
        ],
        "drug_interactions": ["Beta-blockers (mask hypoglycemia symptoms)", "Thiazide diuretics (hyperglycemia)", "ACE inhibitors (enhanced insulin sensitivity)", "Alcohol (unpredictable glucose effects)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "First approved 1982 (recombinant). Multiple analogs available: lispro, aspart, glargine, detemir, degludec.", "notes_de": "Erstmals 1982 zugelassen (rekombinant). Zahlreiche Analoga verfügbar: Lispro, Aspart, Glargin, Detemir, Degludec."},
        "manufacturer": "Novo Nordisk, Eli Lilly, Sanofi",
        "molecular_weight": "5808 Da",
        "amino_acid_count": "51",
        "half_life": "5-6 minutes (IV), varies by formulation",
        "storage_conditions": {"en": "Refrigerate at 2-8°C unopened. In-use pen/vial: room temperature up to 28-30 days.", "de": "Ungeöffnet bei 2-8°C kühlen. Angebrochener Pen/Durchstichflasche: Raumtemperatur bis zu 28-30 Tage."},
        "amino_acid_sequence": "A-chain: GIVEQCCTSICSLYQLENYCN; B-chain: FVNQHLCGSHLVEALYLVCGERGFFYTPKT",
        "reconstitution_info": {
            "preparation_en": "Most formulations are pre-filled pens or vials ready for injection",
            "preparation_de": "Die meisten Formulierungen sind vorgefüllte Pens oder Durchstichflaschen",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24-36 months",
            "shelf_life_reconstituted": "28 days at room temperature after first use",
            "light_sensitive": False,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"},
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "BPC-157",
        "slug": "bpc-157",
        "category": "Body Protection Compound",
        "description": {
            "en": "BPC-157 (Body Protection Compound-157) is a synthetic pentadecapeptide derived from a protein found in human gastric juice. It has shown remarkable regenerative and protective properties in numerous animal studies, including accelerated healing of tendons, muscles, ligaments, and the gastrointestinal tract. Despite extensive preclinical research, it has not yet undergone formal human clinical trials.",
            "de": "BPC-157 (Body Protection Compound-157) ist ein synthetisches Pentadekapeptid, abgeleitet von einem Protein aus dem menschlichen Magensaft. Es hat in zahlreichen Tierstudien bemerkenswerte regenerative und schützende Eigenschaften gezeigt, einschließlich beschleunigter Heilung von Sehnen, Muskeln, Bändern und dem Gastrointestinaltrakt. Trotz umfangreicher präklinischer Forschung wurden noch keine formellen klinischen Studien am Menschen durchgeführt."
        },
        "mechanism_of_action": {
            "en": "BPC-157 modulates the NO system, upregulates growth factor expression (VEGF, EGF), promotes angiogenesis, and interacts with the dopamine and serotonin systems. It activates FAK-paxillin signaling for cell migration and has been shown to counteract organ damage from NSAIDs and alcohol.",
            "de": "BPC-157 moduliert das NO-System, reguliert die Wachstumsfaktor-Expression hoch (VEGF, EGF), fördert die Angiogenese und interagiert mit dem Dopamin- und Serotoninsystem. Es aktiviert FAK-Paxillin-Signalwege für Zellmigration und wirkt nachweislich Organschäden durch NSAIDs und Alkohol entgegen."
        },
        "indications": [
            {"condition_en": "Tendon and Ligament Injuries", "condition_de": "Sehnen- und Bandverletzungen", "description_en": "Accelerates healing of connective tissue injuries (preclinical)", "description_de": "Beschleunigt die Heilung von Bindegewebsverletzungen (präklinisch)"},
            {"condition_en": "Gastrointestinal Disorders", "condition_de": "Gastrointestinale Störungen", "description_en": "Protective against ulcers and inflammatory bowel conditions (preclinical)", "description_de": "Schützend gegen Ulzera und entzündliche Darmerkrankungen (präklinisch)"},
            {"condition_en": "Muscle Injuries", "condition_de": "Muskelverletzungen", "description_en": "Enhanced muscle healing and regeneration (preclinical)", "description_de": "Verbesserte Muskelheilung und -regeneration (präklinisch)"}
        ],
        "benefits": [
            {"benefit_en": "Broad tissue-protective and regenerative effects", "benefit_de": "Breite gewebeschützende und regenerative Effekte"},
            {"benefit_en": "Gastric juice-stable (oral bioavailability)", "benefit_de": "Magensaftstabil (orale Bioverfügbarkeit)"},
            {"benefit_en": "No reported toxicity in animal studies", "benefit_de": "Keine berichtete Toxizität in Tierstudien"},
            {"benefit_en": "Multi-organ protective properties", "benefit_de": "Multi-Organ-schützende Eigenschaften"}
        ],
        "side_effects": [
            {"name_en": "Limited human safety data", "name_de": "Begrenzte Sicherheitsdaten am Menschen", "severity": "moderate", "frequency": "uncommon", "description_en": "No formal clinical trials, safety profile not established", "description_de": "Keine formellen klinischen Studien, Sicherheitsprofil nicht etabliert"},
            {"name_en": "Injection site discomfort", "name_de": "Beschwerden an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Mild pain or redness at injection site", "description_de": "Leichte Schmerzen oder Rötung an der Injektionsstelle"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional GI discomfort reported anecdotally", "description_de": "Gelegentliche GI-Beschwerden anekdotisch berichtet"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "uncommon", "description_en": "Transient lightheadedness", "description_de": "Vorübergehende Benommenheit"},
            {"name_en": "Unknown long-term effects", "name_de": "Unbekannte Langzeiteffekte", "severity": "moderate", "frequency": "uncommon", "description_en": "Long-term safety in humans not studied", "description_de": "Langzeitsicherheit am Menschen nicht untersucht"}
        ],
        "dosage": {
            "starting_dose": "200-300 mcg",
            "maintenance_dose": "250-500 mcg",
            "frequency_en": "Once or twice daily",
            "frequency_de": "Ein- oder zweimal täglich",
            "route_en": "Subcutaneous injection or oral",
            "route_de": "Subkutane Injektion oder oral",
            "notes_en": "Research compound - no established clinical dosing protocol",
            "notes_de": "Forschungssubstanz - kein etabliertes klinisches Dosierungsprotokoll"
        },
        "contraindications": [
            {"en": "Pregnancy and breastfeeding (no safety data)", "de": "Schwangerschaft und Stillzeit (keine Sicherheitsdaten)"},
            {"en": "Active cancer (theoretical angiogenesis concern)", "de": "Aktive Krebserkrankung (theoretische Angiogenese-Bedenken)"},
            {"en": "Children and adolescents", "de": "Kinder und Jugendliche"}
        ],
        "drug_interactions": ["NSAIDs (BPC-157 may counteract GI damage)", "Dopaminergic drugs", "Anticoagulants (theoretical interaction)"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Extensive animal research with promising results. No formal human clinical trials completed. Widely used in research settings.", "notes_de": "Umfangreiche Tierforschung mit vielversprechenden Ergebnissen. Keine formellen klinischen Humanstudien abgeschlossen. Weit verbreitet in Forschungseinrichtungen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "1419 Da",
        "amino_acid_count": "15",
        "half_life": "Estimated 4 hours",
        "storage_conditions": {"en": "Store lyophilized powder at -20°C. Reconstituted solution at 2-8°C.", "de": "Lyophilisiertes Pulver bei -20°C lagern. Rekonstituierte Lösung bei 2-8°C."},
        "amino_acid_sequence": "GEPPPGKPADDAGLV",
        "reconstitution_info": {
            "preparation_en": "Reconstitute lyophilized powder with bacteriostatic water. Inject slowly along vial wall.",
            "preparation_de": "Lyophilisiertes Pulver mit bakteriostatischem Wasser rekonstituieren. Langsam entlang der Fläschchenwand injizieren.",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "14 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"},
            {"goal_en": "Immune Support", "goal_de": "Immununterstützung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "TB-500",
        "slug": "tb-500",
        "category": "Thymosin Beta-4 Fragment",
        "description": {
            "en": "TB-500 is a synthetic peptide fragment of Thymosin Beta-4 (Tβ4), a naturally occurring 43-amino acid peptide involved in tissue repair and regeneration. TB-500 specifically contains the active region responsible for actin binding and cell migration. It has shown potential in promoting wound healing, reducing inflammation, and supporting cardiac and neurological repair in preclinical studies.",
            "de": "TB-500 ist ein synthetisches Peptidfragment von Thymosin Beta-4 (Tβ4), einem natürlich vorkommenden 43-Aminosäure-Peptid, das an Gewebereparatur und -regeneration beteiligt ist. TB-500 enthält speziell die aktive Region für Aktinbindung und Zellmigration. Es hat in präklinischen Studien Potenzial bei Wundheilung, Entzündungsreduktion und kardialer sowie neurologischer Reparatur gezeigt."
        },
        "mechanism_of_action": {
            "en": "TB-500 sequesters G-actin monomers, promoting actin polymerization and cell motility. It upregulates Akt signaling for cell survival, promotes angiogenesis, reduces inflammatory cytokines, and facilitates stem cell migration to injury sites.",
            "de": "TB-500 sequestriert G-Aktin-Monomere, fördert Aktinpolymerisation und Zellmotilität. Es reguliert Akt-Signalwege für Zellüberleben hoch, fördert Angiogenese, reduziert entzündliche Zytokine und erleichtert die Stammzellmigration zu Verletzungsstellen."
        },
        "indications": [
            {"condition_en": "Wound Healing", "condition_de": "Wundheilung", "description_en": "Acceleration of dermal and tissue wound repair (preclinical)", "description_de": "Beschleunigung der dermalen und Gewebereparatur (präklinisch)"},
            {"condition_en": "Cardiac Repair", "condition_de": "Kardiale Reparatur", "description_en": "Post-myocardial infarction recovery (preclinical)", "description_de": "Erholung nach Myokardinfarkt (präklinisch)"},
            {"condition_en": "Neurological Recovery", "condition_de": "Neurologische Erholung", "description_en": "TBI and stroke recovery support (preclinical)", "description_de": "Unterstützung bei SHT- und Schlaganfall-Erholung (präklinisch)"}
        ],
        "benefits": [
            {"benefit_en": "Promotes tissue repair and regeneration", "benefit_de": "Fördert Gewebereparatur und -regeneration"},
            {"benefit_en": "Anti-inflammatory properties", "benefit_de": "Entzündungshemmende Eigenschaften"},
            {"benefit_en": "Promotes new blood vessel formation", "benefit_de": "Fördert Bildung neuer Blutgefäße"},
            {"benefit_en": "Supports flexibility and joint mobility", "benefit_de": "Unterstützt Flexibilität und Gelenkbeweglichkeit"}
        ],
        "side_effects": [
            {"name_en": "Head rush or lightheadedness", "name_de": "Schwindelgefühl", "severity": "mild", "frequency": "common", "description_en": "Brief episode after injection", "description_de": "Kurze Episode nach Injektion"},
            {"name_en": "Injection site irritation", "name_de": "Irritation an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Mild redness or swelling", "description_de": "Leichte Rötung oder Schwellung"},
            {"name_en": "Fatigue", "name_de": "Müdigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Temporary tiredness post-injection", "description_de": "Vorübergehende Müdigkeit nach Injektion"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild GI discomfort", "description_de": "Leichte GI-Beschwerden"},
            {"name_en": "Theoretical cancer risk", "name_de": "Theoretisches Krebsrisiko", "severity": "moderate", "frequency": "rare", "description_en": "Cell migration promotion raises theoretical concerns in cancer patients", "description_de": "Förderung der Zellmigration wirft theoretische Bedenken bei Krebspatienten auf"}
        ],
        "dosage": {
            "starting_dose": "2 mg",
            "maintenance_dose": "2-5 mg",
            "frequency_en": "Twice weekly during loading, weekly for maintenance",
            "frequency_de": "Zweimal wöchentlich initial, wöchentlich zur Erhaltung",
            "route_en": "Subcutaneous or intramuscular injection",
            "route_de": "Subkutane oder intramuskuläre Injektion",
            "notes_en": "Research compound - loading phase typically 4-6 weeks",
            "notes_de": "Forschungssubstanz - Ladephase typischerweise 4-6 Wochen"
        },
        "contraindications": [
            {"en": "Active cancer or malignancy", "de": "Aktive Krebserkrankung oder Malignität"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Children under 18", "de": "Kinder unter 18 Jahren"}
        ],
        "drug_interactions": ["Anticoagulants (potential synergy)", "Immunosuppressants", "Growth factors"],
        "research_status": {"phase": "Preclinical", "fda_approved": False, "ema_approved": False, "notes_en": "Thymosin Beta-4 has been in clinical trials (RegranEx for wound healing). TB-500 as a specific fragment is used primarily in research.", "notes_de": "Thymosin Beta-4 war in klinischen Studien (RegranEx zur Wundheilung). TB-500 als spezifisches Fragment wird primär in der Forschung verwendet."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "4963 Da",
        "amino_acid_count": "43",
        "half_life": "Estimated 2-3 hours",
        "storage_conditions": {"en": "Store lyophilized powder at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiertes Pulver bei -20°C. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "LKKTETQEKNPLPSKETIEQEKQAGES",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Roll gently, do not shake.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Vorsichtig rollen, nicht schütteln.",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "14 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "GHK-Cu",
        "slug": "ghk-cu",
        "category": "Copper Peptide",
        "description": {
            "en": "GHK-Cu (Glycyl-L-Histidyl-L-Lysine Copper) is a naturally occurring tripeptide-copper complex found in human plasma, saliva, and urine. Its concentration in plasma declines with age. GHK-Cu has broad regenerative properties including wound healing, skin remodeling, antioxidant activity, and anti-inflammatory effects. It is widely used in skincare and cosmetic medicine.",
            "de": "GHK-Cu (Glycyl-L-Histidyl-L-Lysin-Kupfer) ist ein natürlich vorkommender Tripeptid-Kupfer-Komplex in humanem Plasma, Speichel und Urin. Seine Plasmakonzentration sinkt mit dem Alter. GHK-Cu hat breite regenerative Eigenschaften einschließlich Wundheilung, Hautumbau, antioxidative Aktivität und entzündungshemmende Effekte. Es wird breit in Hautpflege und kosmetischer Medizin eingesetzt."
        },
        "mechanism_of_action": {
            "en": "GHK-Cu modulates gene expression of over 4,000 genes, promoting collagen synthesis, glycosaminoglycan production, and stem cell attraction. The copper ion acts as a cofactor for superoxide dismutase and lysyl oxidase, supporting antioxidant defense and extracellular matrix integrity.",
            "de": "GHK-Cu moduliert die Genexpression von über 4.000 Genen, fördert Kollagensynthese, Glykosaminoglykan-Produktion und Stammzellattraktion. Das Kupferion wirkt als Cofaktor für Superoxiddismutase und Lysyloxidase und unterstützt antioxidative Abwehr und extrazelluläre Matrixintegrität."
        },
        "indications": [
            {"condition_en": "Skin Aging and Photoaging", "condition_de": "Hautalterung und Photoaging", "description_en": "Topical treatment for wrinkles, skin laxity, and age spots", "description_de": "Topische Behandlung von Falten, Hauterschlaffung und Altersflecken"},
            {"condition_en": "Wound Healing", "condition_de": "Wundheilung", "description_en": "Acceleration of surgical and chronic wound repair", "description_de": "Beschleunigung der chirurgischen und chronischen Wundreparatur"},
            {"condition_en": "Hair Loss", "condition_de": "Haarausfall", "description_en": "Stimulation of hair follicle growth", "description_de": "Stimulation des Haarfollikelwachstums"}
        ],
        "benefits": [
            {"benefit_en": "Stimulates collagen and elastin production", "benefit_de": "Stimuliert Kollagen- und Elastinproduktion"},
            {"benefit_en": "Powerful antioxidant and anti-inflammatory", "benefit_de": "Starkes Antioxidans und entzündungshemmend"},
            {"benefit_en": "Promotes hair growth and thickness", "benefit_de": "Fördert Haarwachstum und -dicke"},
            {"benefit_en": "Well-tolerated in topical and injectable forms", "benefit_de": "Gut verträglich in topischer und injizierbarer Form"}
        ],
        "side_effects": [
            {"name_en": "Skin irritation (topical)", "name_de": "Hautreizung (topisch)", "severity": "mild", "frequency": "uncommon", "description_en": "Mild redness or tingling with topical use", "description_de": "Leichte Rötung oder Kribbeln bei topischer Anwendung"},
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Brief discomfort at injection site", "description_de": "Kurze Beschwerden an der Injektionsstelle"},
            {"name_en": "Copper sensitivity", "name_de": "Kupferempfindlichkeit", "severity": "moderate", "frequency": "rare", "description_en": "Rare allergic reaction to copper component", "description_de": "Seltene allergische Reaktion auf Kupferkomponente"},
            {"name_en": "Temporary skin discoloration", "name_de": "Vorübergehende Hautverfärbung", "severity": "mild", "frequency": "uncommon", "description_en": "Blue-green tint from copper in high concentrations", "description_de": "Blau-grüne Tönung durch Kupfer bei hohen Konzentrationen"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional headache with systemic use", "description_de": "Gelegentliche Kopfschmerzen bei systemischer Anwendung"}
        ],
        "dosage": {
            "starting_dose": "1-2 mg (injectable), 1-2% (topical)",
            "maintenance_dose": "1-3 mg (injectable)",
            "frequency_en": "Daily (topical), 2-3 times weekly (injectable)",
            "frequency_de": "Täglich (topisch), 2-3 mal wöchentlich (injizierbar)",
            "route_en": "Topical, subcutaneous injection, or mesotherapy",
            "route_de": "Topisch, subkutane Injektion oder Mesotherapie",
            "notes_en": "Topical most common; injectable use primarily in aesthetic medicine",
            "notes_de": "Topisch am häufigsten; injizierbar primär in ästhetischer Medizin"
        },
        "contraindications": [
            {"en": "Wilson's disease (copper metabolism disorder)", "de": "Morbus Wilson (Kupferstoffwechselstörung)"},
            {"en": "Known copper allergy", "de": "Bekannte Kupferallergie"},
            {"en": "Pregnancy (injectable form)", "de": "Schwangerschaft (injizierbare Form)"}
        ],
        "drug_interactions": ["Zinc supplements (compete for absorption)", "Copper chelating agents", "Retinoids (may enhance skin effects)"],
        "research_status": {"phase": "Preclinical / Cosmetic Use", "fda_approved": False, "ema_approved": False, "notes_en": "Widely used in cosmetic products. Preclinical research ongoing for systemic applications.", "notes_de": "Weit verbreitet in Kosmetikprodukten. Präklinische Forschung für systemische Anwendungen läuft."},
        "manufacturer": "Various (cosmetic and research suppliers)",
        "molecular_weight": "403 Da",
        "amino_acid_count": "3",
        "half_life": "Estimated 1-2 hours",
        "storage_conditions": {"en": "Store powder at -20°C. Solutions at 2-8°C. Protect from light.", "de": "Pulver bei -20°C lagern. Lösungen bei 2-8°C. Vor Licht schützen."},
        "amino_acid_sequence": "GHK",
        "reconstitution_info": {
            "preparation_en": "Dissolve in sterile water or bacteriostatic water for injection use",
            "preparation_de": "In sterilem Wasser oder bakteriostatischem Wasser für Injektionszwecke lösen",
            "storage_temperature": "-20°C (powder), 2-8°C (solution)",
            "shelf_life_unopened": "24 months (powder)",
            "shelf_life_reconstituted": "14 days refrigerated",
            "light_sensitive": True,
            "solvent": "Sterile water or bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Ipamorelin",
        "slug": "ipamorelin",
        "category": "Growth Hormone Secretagogue",
        "description": {
            "en": "Ipamorelin is a selective growth hormone secretagogue (GHS) and ghrelin mimetic pentapeptide. Unlike other GH secretagogues, it does not significantly increase cortisol or prolactin levels, making it one of the most selective GHRP available. It stimulates pulsatile GH release from the pituitary gland, mimicking natural GH secretion patterns.",
            "de": "Ipamorelin ist ein selektiver Wachstumshormon-Sekretagoge (GHS) und Ghrelin-mimetisches Pentapeptid. Anders als andere GH-Sekretagoge erhöht es Cortisol- oder Prolaktinspiegel nicht signifikant, was es zu einem der selektivsten GHRP macht. Es stimuliert die pulsatile GH-Freisetzung aus der Hypophyse und ahmt natürliche GH-Sekretionsmuster nach."
        },
        "mechanism_of_action": {
            "en": "Ipamorelin binds to the ghrelin receptor (GHS-R1a) on pituitary somatotroph cells, stimulating growth hormone release through the phospholipase C/IP3 pathway. It acts synergistically with GHRH and does not suppress natural GH feedback mechanisms.",
            "de": "Ipamorelin bindet an den Ghrelin-Rezeptor (GHS-R1a) auf somatotropen Hypophysenzellen und stimuliert die Wachstumshormon-Freisetzung über den Phospholipase C/IP3-Signalweg. Es wirkt synergistisch mit GHRH und unterdrückt keine natürlichen GH-Rückkopplungsmechanismen."
        },
        "indications": [
            {"condition_en": "Growth Hormone Deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Stimulation of endogenous GH production (research)", "description_de": "Stimulation der endogenen GH-Produktion (Forschung)"},
            {"condition_en": "Age-Related GH Decline", "condition_de": "Altersbedingte GH-Abnahme", "description_en": "Anti-aging and body composition optimization (research)", "description_de": "Anti-Aging und Körperzusammensetzung-Optimierung (Forschung)"},
            {"condition_en": "Bone Density", "condition_de": "Knochendichte", "description_en": "Potential to increase bone mineral density through GH stimulation", "description_de": "Potenzial zur Erhöhung der Knochenmineraldichte durch GH-Stimulation"}
        ],
        "benefits": [
            {"benefit_en": "Highly selective GH release without cortisol spike", "benefit_de": "Hochselektive GH-Freisetzung ohne Cortisolanstieg"},
            {"benefit_en": "Mimics natural pulsatile GH secretion", "benefit_de": "Ahmt natürliche pulsatile GH-Sekretion nach"},
            {"benefit_en": "Improved sleep quality and recovery", "benefit_de": "Verbesserte Schlafqualität und Erholung"},
            {"benefit_en": "Better body composition (reduced fat, lean mass)", "benefit_de": "Bessere Körperzusammensetzung (weniger Fett, mehr Muskelmasse)"}
        ],
        "side_effects": [
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Mild headache, especially initially", "description_de": "Leichte Kopfschmerzen, besonders anfangs"},
            {"name_en": "Water retention", "name_de": "Wassereinlagerung", "severity": "mild", "frequency": "common", "description_en": "Mild fluid retention from GH increase", "description_de": "Leichte Flüssigkeitsretention durch GH-Anstieg"},
            {"name_en": "Tingling/numbness", "name_de": "Kribbeln/Taubheit", "severity": "mild", "frequency": "uncommon", "description_en": "Paresthesia in extremities", "description_de": "Parästhesie in den Extremitäten"},
            {"name_en": "Increased hunger", "name_de": "Verstärkter Hunger", "severity": "mild", "frequency": "common", "description_en": "Ghrelin pathway activation increases appetite", "description_de": "Ghrelin-Aktivierung steigert den Appetit"},
            {"name_en": "Joint pain", "name_de": "Gelenkschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Related to GH-mediated tissue changes", "description_de": "Zusammenhängend mit GH-vermittelten Gewebeveränderungen"}
        ],
        "dosage": {
            "starting_dose": "100 mcg",
            "maintenance_dose": "200-300 mcg",
            "frequency_en": "1-3 times daily (before bed optimal)",
            "frequency_de": "1-3 mal täglich (vor dem Schlafengehen optimal)",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Best administered on empty stomach. Often combined with CJC-1295.",
            "notes_de": "Am besten nüchtern verabreichen. Oft kombiniert mit CJC-1295."
        },
        "contraindications": [
            {"en": "Active cancer or malignancy", "de": "Aktive Krebserkrankung oder Malignität"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Pituitary tumors", "de": "Hypophysentumore"}
        ],
        "drug_interactions": ["Exogenous GH (synergistic)", "CJC-1295 (commonly stacked)", "Glucocorticoids (may attenuate GH response)"],
        "research_status": {"phase": "Phase 2", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 2 clinical trials completed for postoperative ileus. Widely used in research settings.", "notes_de": "Phase-2-Studien abgeschlossen für postoperativen Ileus. Weit verbreitet in Forschungseinrichtungen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "711 Da",
        "amino_acid_count": "5",
        "half_life": "2 hours",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei -20°C lagern. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "Aib-His-D-2Nal-D-Phe-Lys-NH2",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Typical concentration: 200 mcg per 0.1 mL",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Typische Konzentration: 200 mcg pro 0,1 ml",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "21 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "CJC-1295",
        "slug": "cjc-1295",
        "category": "Growth Hormone Releasing Hormone Analog",
        "description": {
            "en": "CJC-1295 is a synthetic analog of growth hormone-releasing hormone (GHRH) with a Drug Affinity Complex (DAC) that extends its half-life. It stimulates sustained GH release from the pituitary gland. CJC-1295 is often combined with Ipamorelin for synergistic GH stimulation. Both DAC and non-DAC (MOD GRF 1-29) versions exist.",
            "de": "CJC-1295 ist ein synthetisches Analogon des Wachstumshormon-Releasing-Hormons (GHRH) mit einem Drug Affinity Complex (DAC), der seine Halbwertszeit verlängert. Es stimuliert eine anhaltende GH-Freisetzung aus der Hypophyse. CJC-1295 wird oft mit Ipamorelin für synergistische GH-Stimulation kombiniert."
        },
        "mechanism_of_action": {
            "en": "CJC-1295 binds to GHRH receptors on pituitary somatotrophs, activating the cAMP/PKA pathway to stimulate GH synthesis and secretion. The DAC modification enables covalent binding to serum albumin, extending half-life from minutes to days.",
            "de": "CJC-1295 bindet an GHRH-Rezeptoren auf somatotropen Hypophysenzellen und aktiviert den cAMP/PKA-Signalweg zur Stimulation der GH-Synthese und -Sekretion. Die DAC-Modifikation ermöglicht kovalente Albuminbindung und verlängert die Halbwertszeit von Minuten auf Tage."
        },
        "indications": [
            {"condition_en": "Growth Hormone Deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Stimulation of endogenous GH axis (research)", "description_de": "Stimulation der endogenen GH-Achse (Forschung)"},
            {"condition_en": "Body Composition Optimization", "condition_de": "Körperzusammensetzung-Optimierung", "description_en": "Fat reduction and lean mass increase via GH elevation", "description_de": "Fettreduktion und Magermasse-Zunahme durch GH-Erhöhung"},
            {"condition_en": "Sleep and Recovery", "condition_de": "Schlaf und Erholung", "description_en": "Enhanced deep sleep and tissue recovery through GH pulse optimization", "description_de": "Verbesserter Tiefschlaf und Gewebeerholung durch GH-Puls-Optimierung"}
        ],
        "benefits": [
            {"benefit_en": "Sustained GH elevation over days (DAC version)", "benefit_de": "Anhaltende GH-Erhöhung über Tage (DAC-Version)"},
            {"benefit_en": "Synergistic effect when combined with GHRP", "benefit_de": "Synergistischer Effekt in Kombination mit GHRP"},
            {"benefit_en": "Improved deep sleep and recovery", "benefit_de": "Verbesserter Tiefschlaf und Erholung"},
            {"benefit_en": "Enhanced fat metabolism", "benefit_de": "Verbesserter Fettstoffwechsel"}
        ],
        "side_effects": [
            {"name_en": "Flushing", "name_de": "Flush/Hautrötung", "severity": "mild", "frequency": "common", "description_en": "Warmth and redness after injection", "description_de": "Wärme und Rötung nach Injektion"},
            {"name_en": "Water retention", "name_de": "Wassereinlagerung", "severity": "mild", "frequency": "common", "description_en": "Mild edema from GH increase", "description_de": "Leichtes Ödem durch GH-Anstieg"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Usually during first week of use", "description_de": "Meist in der ersten Anwendungswoche"},
            {"name_en": "Tingling in extremities", "name_de": "Kribbeln in den Extremitäten", "severity": "mild", "frequency": "uncommon", "description_en": "GH-related paresthesia", "description_de": "GH-bedingte Parästhesie"},
            {"name_en": "Increased cortisol", "name_de": "Erhöhtes Cortisol", "severity": "moderate", "frequency": "uncommon", "description_en": "DAC version may modestly raise cortisol", "description_de": "DAC-Version kann Cortisol leicht erhöhen"}
        ],
        "dosage": {
            "starting_dose": "1 mg (DAC) or 100 mcg (no DAC)",
            "maintenance_dose": "2 mg weekly (DAC) or 100 mcg 1-3x daily (no DAC)",
            "frequency_en": "Once or twice weekly (DAC), 1-3 times daily (no DAC)",
            "frequency_de": "Ein- oder zweimal wöchentlich (DAC), 1-3 mal täglich (ohne DAC)",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Often combined with Ipamorelin. Administer on empty stomach.",
            "notes_de": "Oft kombiniert mit Ipamorelin. Nüchtern verabreichen."
        },
        "contraindications": [
            {"en": "Active malignancy", "de": "Aktive Malignität"},
            {"en": "Uncontrolled diabetes", "de": "Unkontrollierter Diabetes"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["Ipamorelin (synergistic stack)", "Exogenous GH", "Somatostatin analogs (antagonistic)"],
        "research_status": {"phase": "Phase 2", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 2 trials conducted. Not approved for clinical use. Widely used in research.", "notes_de": "Phase-2-Studien durchgeführt. Nicht für klinische Anwendung zugelassen. Weit verbreitet in Forschung."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "3368 Da",
        "amino_acid_count": "29",
        "half_life": "6-8 days (DAC), 30 minutes (no DAC)",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei -20°C lagern. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "YADAIFTNSYRKVLGQLSARKLLQDIMSRQQGESNQERGARARL",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water. Inject along vial wall.",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren. Entlang der Fläschchenwand injizieren.",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "21 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Sermorelin",
        "slug": "sermorelin",
        "category": "Growth Hormone Releasing Hormone Analog",
        "description": {
            "en": "Sermorelin is a synthetic peptide analog corresponding to the first 29 amino acids of GHRH. It was FDA-approved for diagnostic evaluation and treatment of GH deficiency in children. It stimulates the natural production and release of growth hormone from the pituitary gland, preserving the body's feedback mechanisms.",
            "de": "Sermorelin ist ein synthetisches Peptidanalogon der ersten 29 Aminosäuren von GHRH. Es war FDA-zugelassen zur diagnostischen Bewertung und Behandlung von GH-Mangel bei Kindern. Es stimuliert die natürliche Produktion und Freisetzung von Wachstumshormon und erhält die körpereigenen Rückkopplungsmechanismen."
        },
        "mechanism_of_action": {
            "en": "Sermorelin binds to GHRH receptors on pituitary somatotrophs, stimulating GH synthesis and pulsatile release via cAMP signaling. Unlike exogenous GH, it maintains the hypothalamic-pituitary axis feedback.",
            "de": "Sermorelin bindet an GHRH-Rezeptoren auf somatotropen Hypophysenzellen und stimuliert GH-Synthese und pulsatile Freisetzung über cAMP-Signalwege. Anders als exogenes GH erhält es die Hypothalamus-Hypophysen-Achsen-Rückkopplung."
        },
        "indications": [
            {"condition_en": "Pediatric Growth Hormone Deficiency", "condition_de": "Pädiatrischer Wachstumshormonmangel", "description_en": "Historically approved for GH deficiency in children", "description_de": "Historisch zugelassen bei GH-Mangel im Kindesalter"},
            {"condition_en": "Adult GH Deficiency", "condition_de": "GH-Mangel bei Erwachsenen", "description_en": "Off-label use for age-related GH decline", "description_de": "Off-Label-Anwendung bei altersbedingtem GH-Rückgang"},
            {"condition_en": "Diagnostic Testing", "condition_de": "Diagnostische Testung", "description_en": "Pituitary function assessment", "description_de": "Beurteilung der Hypophysenfunktion"}
        ],
        "benefits": [
            {"benefit_en": "Natural GH release pattern preservation", "benefit_de": "Erhaltung des natürlichen GH-Freisetzungsmusters"},
            {"benefit_en": "Lower risk than exogenous GH therapy", "benefit_de": "Geringeres Risiko als exogene GH-Therapie"},
            {"benefit_en": "Improved sleep quality", "benefit_de": "Verbesserte Schlafqualität"},
            {"benefit_en": "Enhanced body composition and vitality", "benefit_de": "Verbesserte Körperzusammensetzung und Vitalität"}
        ],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Pain, redness, or swelling", "description_de": "Schmerzen, Rötung oder Schwellung"},
            {"name_en": "Facial flushing", "name_de": "Gesichtsrötung", "severity": "mild", "frequency": "common", "description_en": "Transient warmth and redness", "description_de": "Vorübergehende Wärme und Rötung"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Usually mild and self-resolving", "description_de": "Meist mild und selbstlimitierend"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "uncommon", "description_en": "Brief lightheadedness", "description_de": "Kurze Benommenheit"},
            {"name_en": "Hyperactivity", "name_de": "Hyperaktivität", "severity": "mild", "frequency": "uncommon", "description_en": "Increased energy in some patients", "description_de": "Erhöhte Energie bei manchen Patienten"}
        ],
        "dosage": {
            "starting_dose": "200 mcg",
            "maintenance_dose": "200-300 mcg",
            "frequency_en": "Once daily at bedtime",
            "frequency_de": "Einmal täglich vor dem Schlafengehen",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Administer on empty stomach before bed for optimal GH pulse",
            "notes_de": "Nüchtern vor dem Schlafengehen für optimalen GH-Puls verabreichen"
        },
        "contraindications": [
            {"en": "Active malignancy", "de": "Aktive Malignität"},
            {"en": "Hypersensitivity to sermorelin", "de": "Überempfindlichkeit gegen Sermorelin"},
            {"en": "Pregnancy", "de": "Schwangerschaft"}
        ],
        "drug_interactions": ["Glucocorticoids (may blunt GH response)", "Thyroid hormones", "Exogenous GH"],
        "research_status": {"phase": "Approved (historically)", "fda_approved": True, "ema_approved": False, "notes_en": "FDA approved 1997 as Geref. Manufacturer discontinued production in 2008. Available through compounding pharmacies.", "notes_de": "FDA-zugelassen 1997 als Geref. Hersteller stellte Produktion 2008 ein. Über Rezepturapotheken verfügbar."},
        "manufacturer": "EMD Serono (discontinued), compounding pharmacies",
        "molecular_weight": "3358 Da",
        "amino_acid_count": "29",
        "half_life": "10-20 minutes",
        "storage_conditions": {"en": "Store lyophilized at 2-8°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei 2-8°C lagern. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "YADAIFTNSYRKVLGQLSARKLLQDIMSRQ",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with provided diluent or bacteriostatic water",
            "preparation_de": "Mit beiliegendem Lösungsmittel oder bakteriostatischem Wasser rekonstituieren",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "24 months",
            "shelf_life_reconstituted": "14 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water (0.9% benzyl alcohol)"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Melanotan II",
        "slug": "melanotan-ii",
        "category": "Melanocortin Agonist",
        "description": {
            "en": "Melanotan II is a synthetic cyclic heptapeptide analog of alpha-melanocyte-stimulating hormone (α-MSH). It activates melanocortin receptors MC1R through MC5R, producing skin tanning, appetite suppression, and sexual arousal effects. It was originally developed at the University of Arizona for skin cancer prevention through tanning.",
            "de": "Melanotan II ist ein synthetisches zyklisches Heptapeptid-Analogon des Alpha-Melanozyten-stimulierenden Hormons (α-MSH). Es aktiviert Melanocortin-Rezeptoren MC1R bis MC5R und erzeugt Hautbräunung, Appetitunterdrückung und sexuelle Erregung. Es wurde ursprünglich an der University of Arizona zur Hautkrebsprävention durch Bräunung entwickelt."
        },
        "mechanism_of_action": {
            "en": "Melanotan II non-selectively activates melanocortin receptors. MC1R activation stimulates melanogenesis (tanning). MC4R activation in the hypothalamus affects appetite and sexual function. MC3R activation modulates energy homeostasis.",
            "de": "Melanotan II aktiviert nicht-selektiv Melanocortin-Rezeptoren. MC1R-Aktivierung stimuliert Melanogenese (Bräunung). MC4R-Aktivierung im Hypothalamus beeinflusst Appetit und Sexualfunktion. MC3R-Aktivierung moduliert die Energiehomöostase."
        },
        "indications": [
            {"condition_en": "Skin Tanning", "condition_de": "Hautbräunung", "description_en": "UV-independent melanogenesis stimulation (research)", "description_de": "UV-unabhängige Melanogenese-Stimulation (Forschung)"},
            {"condition_en": "Erectile Dysfunction", "condition_de": "Erektile Dysfunktion", "description_en": "Sexual function enhancement via MC4R (led to PT-141 development)", "description_de": "Sexualfunktionsverbesserung über MC4R (führte zur PT-141-Entwicklung)"},
            {"condition_en": "Appetite Regulation", "condition_de": "Appetitregulation", "description_en": "Appetite suppression through central melanocortin signaling", "description_de": "Appetitunterdrückung durch zentrale Melanocortin-Signalgebung"}
        ],
        "benefits": [
            {"benefit_en": "Rapid skin darkening without UV exposure", "benefit_de": "Schnelle Hautbräunung ohne UV-Exposition"},
            {"benefit_en": "Appetite suppression", "benefit_de": "Appetitunterdrückung"},
            {"benefit_en": "Enhanced libido in both sexes", "benefit_de": "Gesteigerte Libido bei beiden Geschlechtern"},
            {"benefit_en": "Potential photoprotective effects", "benefit_de": "Potenzielle photoprotektive Effekte"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "moderate", "frequency": "common", "description_en": "Very common especially with initial doses", "description_de": "Sehr häufig besonders bei Anfangsdosen"},
            {"name_en": "Facial flushing", "name_de": "Gesichtsrötung", "severity": "mild", "frequency": "common", "description_en": "Warmth and redness in face", "description_de": "Wärme und Rötung im Gesicht"},
            {"name_en": "Spontaneous erections", "name_de": "Spontane Erektionen", "severity": "mild", "frequency": "common", "description_en": "MC4R-mediated sexual side effect", "description_de": "MC4R-vermittelte sexuelle Nebenwirkung"},
            {"name_en": "Mole darkening", "name_de": "Muttermal-Verdunkelung", "severity": "moderate", "frequency": "common", "description_en": "Existing moles may darken, requires monitoring", "description_de": "Bestehende Muttermale können sich verdunkeln, erfordert Überwachung"},
            {"name_en": "Increased blood pressure", "name_de": "Erhöhter Blutdruck", "severity": "moderate", "frequency": "uncommon", "description_en": "Transient hypertension", "description_de": "Vorübergehende Hypertonie"}
        ],
        "dosage": {
            "starting_dose": "0.25 mg",
            "maintenance_dose": "0.5-1 mg",
            "frequency_en": "Daily during loading, then as needed",
            "frequency_de": "Täglich während der Ladephase, dann nach Bedarf",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Start low to assess tolerance. Administer before UV exposure for tanning.",
            "notes_de": "Niedrig beginnen zur Verträglichkeitsprüfung. Vor UV-Exposition zur Bräunung verabreichen."
        },
        "contraindications": [
            {"en": "History of melanoma or atypical moles", "de": "Vorgeschichte von Melanom oder atypischen Muttermalen"},
            {"en": "Cardiovascular disease", "de": "Kardiovaskuläre Erkrankung"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["Antihypertensives", "PDE5 inhibitors (sildenafil — additive)", "Appetite suppressants"],
        "research_status": {"phase": "Research", "fda_approved": False, "ema_approved": False, "notes_en": "Not approved for clinical use. Research compound. Led to development of FDA-approved bremelanotide (PT-141).", "notes_de": "Nicht für klinische Anwendung zugelassen. Forschungssubstanz. Führte zur Entwicklung des FDA-zugelassenen Bremelanotid (PT-141)."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "1024 Da",
        "amino_acid_count": "7",
        "half_life": "1-2 hours",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei -20°C. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "Ac-Nle-c[Asp-His-D-Phe-Arg-Trp-Lys]-NH2",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "30 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "PT-141",
        "slug": "pt-141",
        "category": "Melanocortin Receptor Agonist",
        "description": {
            "en": "PT-141 (Bremelanotide) is a synthetic melanocortin receptor agonist approved by the FDA as Vyleesi for hypoactive sexual desire disorder (HSDD) in premenopausal women. It is derived from Melanotan II but with greater selectivity for MC4R. It works through the central nervous system rather than the vascular system, distinguishing it from PDE5 inhibitors.",
            "de": "PT-141 (Bremelanotid) ist ein synthetischer Melanocortin-Rezeptoragonist, von der FDA als Vyleesi für hypoaktive sexuelle Appetenzstörung (HSDD) bei prämenopausalen Frauen zugelassen. Es ist von Melanotan II abgeleitet, jedoch mit größerer Selektivität für MC4R. Es wirkt über das Zentralnervensystem statt über das vaskuläre System."
        },
        "mechanism_of_action": {
            "en": "PT-141 activates melanocortin-4 receptors (MC4R) in the hypothalamus, modulating neural pathways involved in sexual arousal and desire. Unlike PDE5 inhibitors, it acts centrally on sexual desire rather than peripherally on blood flow.",
            "de": "PT-141 aktiviert Melanocortin-4-Rezeptoren (MC4R) im Hypothalamus und moduliert neuronale Signalwege für sexuelle Erregung und Verlangen. Anders als PDE5-Hemmer wirkt es zentral auf das sexuelle Verlangen statt peripher auf den Blutfluss."
        },
        "indications": [
            {"condition_en": "Hypoactive Sexual Desire Disorder (HSDD)", "condition_de": "Hypoaktive sexuelle Appetenzstörung (HSDD)", "description_en": "FDA-approved for premenopausal women with generalized HSDD", "description_de": "FDA-zugelassen für prämenopausale Frauen mit generalisierter HSDD"},
            {"condition_en": "Male Erectile Dysfunction", "condition_de": "Männliche erektile Dysfunktion", "description_en": "Under investigation as alternative to PDE5 inhibitors", "description_de": "Wird als Alternative zu PDE5-Hemmern untersucht"},
            {"condition_en": "Female Sexual Dysfunction", "condition_de": "Weibliche sexuelle Dysfunktion", "description_en": "Broader female sexual arousal and desire disorders", "description_de": "Breitere weibliche sexuelle Erregungs- und Verlangenstörungen"}
        ],
        "benefits": [
            {"benefit_en": "First FDA-approved on-demand treatment for female HSDD", "benefit_de": "Erste FDA-zugelassene Bedarfsbehandlung für weibliche HSDD"},
            {"benefit_en": "Works through central nervous system (novel mechanism)", "benefit_de": "Wirkt über das Zentralnervensystem (neuartiger Mechanismus)"},
            {"benefit_en": "Effective in both men and women", "benefit_de": "Wirksam bei Männern und Frauen"},
            {"benefit_en": "On-demand dosing (as needed)", "benefit_de": "Bedarfsdosierung (nach Bedarf)"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "moderate", "frequency": "common", "description_en": "Most common side effect (40% in trials)", "description_de": "Häufigste Nebenwirkung (40% in Studien)"},
            {"name_en": "Flushing", "name_de": "Hautrötung", "severity": "mild", "frequency": "common", "description_en": "Warmth and redness, especially facial", "description_de": "Wärme und Rötung, besonders im Gesicht"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Common during first uses", "description_de": "Häufig bei ersten Anwendungen"},
            {"name_en": "Skin hyperpigmentation", "name_de": "Hauthyperpigmentierung", "severity": "mild", "frequency": "uncommon", "description_en": "Focal darkening of gums, face, or breasts", "description_de": "Fokale Verdunkelung von Zahnfleisch, Gesicht oder Brüsten"},
            {"name_en": "Blood pressure increase", "name_de": "Blutdruckanstieg", "severity": "moderate", "frequency": "uncommon", "description_en": "Transient BP elevation, monitor in hypertensive patients", "description_de": "Vorübergehender BD-Anstieg, bei Hypertonie-Patienten überwachen"}
        ],
        "dosage": {
            "starting_dose": "1.75 mg",
            "maintenance_dose": "1.75 mg",
            "frequency_en": "As needed, at least 45 minutes before activity",
            "frequency_de": "Nach Bedarf, mindestens 45 Minuten vor Aktivität",
            "route_en": "Subcutaneous injection (auto-injector)",
            "route_de": "Subkutane Injektion (Autoinjektor)",
            "notes_en": "Maximum one dose per 24 hours, max 8 doses per month",
            "notes_de": "Maximal eine Dosis pro 24 Stunden, max 8 Dosen pro Monat"
        },
        "contraindications": [
            {"en": "Uncontrolled hypertension", "de": "Unkontrollierter Bluthochdruck"},
            {"en": "Cardiovascular disease", "de": "Kardiovaskuläre Erkrankung"},
            {"en": "Concurrent use with naltrexone", "de": "Gleichzeitige Anwendung mit Naltrexon"}
        ],
        "drug_interactions": ["Naltrexone (contraindicated)", "Antihypertensives", "PDE5 inhibitors (additive effects)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": False, "notes_en": "FDA approved 2019 as Vyleesi for HSDD in premenopausal women. Not EMA approved.", "notes_de": "FDA-zugelassen 2019 als Vyleesi für HSDD bei prämenopausalen Frauen. Nicht EMA-zugelassen."},
        "manufacturer": "AMAG Pharmaceuticals / Palatin Technologies",
        "molecular_weight": "1025 Da",
        "amino_acid_count": "7",
        "half_life": "2.7 hours",
        "storage_conditions": {"en": "Store at room temperature 20-25°C. Protect from light.", "de": "Bei Raumtemperatur 20-25°C lagern. Vor Licht schützen."},
        "amino_acid_sequence": "Ac-Nle-c[Asp-His-D-Phe-Arg-Trp-Lys]-OH",
        "reconstitution_info": {
            "preparation_en": "Pre-filled auto-injector, ready to use",
            "preparation_de": "Vorgefüllter Autoinjektor, gebrauchsfertig",
            "storage_temperature": "20-25°C",
            "shelf_life_unopened": "36 months",
            "shelf_life_reconstituted": "Single use auto-injector",
            "light_sensitive": True,
            "solvent": "Pre-filled solution"
        },
        "application_goals": [
            {"goal_en": "Cognitive Enhancement", "goal_de": "Kognitive Verbesserung", "relevance": "secondary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "AOD-9604",
        "slug": "aod-9604",
        "category": "Growth Hormone Fragment",
        "description": {
            "en": "AOD-9604 (Advanced Obesity Drug) is a modified fragment of human growth hormone comprising amino acids 176-191 of the hGH polypeptide. It was developed to isolate the fat-burning properties of GH without its growth-promoting or diabetogenic effects. AOD-9604 stimulates lipolysis and inhibits lipogenesis without affecting blood sugar or growth.",
            "de": "AOD-9604 (Advanced Obesity Drug) ist ein modifiziertes Fragment des menschlichen Wachstumshormons, bestehend aus den Aminosäuren 176-191 des hGH-Polypeptids. Es wurde entwickelt, um die fettverbrennenden Eigenschaften von GH ohne wachstumsfördernde oder diabetogene Effekte zu isolieren. AOD-9604 stimuliert Lipolyse und hemmt Lipogenese ohne Blutzucker oder Wachstum zu beeinflussen."
        },
        "mechanism_of_action": {
            "en": "AOD-9604 mimics the lipolytic action of the C-terminal fragment of growth hormone. It stimulates beta-3 adrenergic receptors in adipose tissue, promotes fat oxidation, and inhibits de novo lipogenesis without binding to the GH receptor.",
            "de": "AOD-9604 ahmt die lipolytische Wirkung des C-terminalen Fragments von Wachstumshormon nach. Es stimuliert Beta-3-adrenerge Rezeptoren im Fettgewebe, fördert Fettoxidation und hemmt die De-novo-Lipogenese ohne an den GH-Rezeptor zu binden."
        },
        "indications": [
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Fat reduction without GH side effects (research)", "description_de": "Fettreduktion ohne GH-Nebenwirkungen (Forschung)"},
            {"condition_en": "Osteoarthritis", "condition_de": "Arthrose", "description_en": "Cartilage repair and joint health (under investigation)", "description_de": "Knorpelreparatur und Gelenkgesundheit (in Untersuchung)"},
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Metabolic optimization without IGF-1 elevation", "description_de": "Stoffwechseloptimierung ohne IGF-1-Erhöhung"}
        ],
        "benefits": [
            {"benefit_en": "Targeted fat loss without GH side effects", "benefit_de": "Gezielte Fettabnahme ohne GH-Nebenwirkungen"},
            {"benefit_en": "No effect on blood glucose or IGF-1", "benefit_de": "Kein Einfluss auf Blutzucker oder IGF-1"},
            {"benefit_en": "Potential cartilage regeneration", "benefit_de": "Potenzielle Knorpelregeneration"},
            {"benefit_en": "Good safety profile in clinical trials", "benefit_de": "Gutes Sicherheitsprofil in klinischen Studien"}
        ],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Mild redness and discomfort", "description_de": "Leichte Rötung und Beschwerden"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional mild headache", "description_de": "Gelegentliche leichte Kopfschmerzen"},
            {"name_en": "Flu-like symptoms", "name_de": "Grippeähnliche Symptome", "severity": "mild", "frequency": "uncommon", "description_en": "Transient cold-like symptoms", "description_de": "Vorübergehende erkältungsähnliche Symptome"},
            {"name_en": "Chest tightness", "name_de": "Engegefühl in der Brust", "severity": "moderate", "frequency": "rare", "description_en": "Rare chest discomfort reported", "description_de": "Seltene Brustbeschwerden berichtet"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "uncommon", "description_en": "Brief episodes of lightheadedness", "description_de": "Kurze Episoden von Benommenheit"}
        ],
        "dosage": {
            "starting_dose": "250 mcg",
            "maintenance_dose": "250-500 mcg",
            "frequency_en": "Once daily on empty stomach",
            "frequency_de": "Einmal täglich nüchtern",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Administer in morning before breakfast for best results",
            "notes_de": "Morgens vor dem Frühstück verabreichen für beste Ergebnisse"
        },
        "contraindications": [
            {"en": "Active cancer", "de": "Aktive Krebserkrankung"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Severe cardiac disease", "de": "Schwere Herzerkrankung"}
        ],
        "drug_interactions": ["Growth hormone therapy", "Beta-blockers (may reduce efficacy)", "Insulin"],
        "research_status": {"phase": "Phase 3 (completed)", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 3 trials completed for obesity but did not gain FDA approval. TGA (Australia) approved for food supplement use. Under investigation for osteoarthritis.", "notes_de": "Phase-3-Studien für Adipositas abgeschlossen, aber keine FDA-Zulassung. TGA (Australien) für Nahrungsergänzung zugelassen. Wird für Arthrose untersucht."},
        "manufacturer": "Metabolic Pharmaceuticals / Various",
        "molecular_weight": "1815 Da",
        "amino_acid_count": "16",
        "half_life": "Estimated 30-60 minutes",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei -20°C. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "YLRIVQCRSVEGSCGF",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water",
            "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "21 days refrigerated",
            "light_sensitive": True,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Epitalon",
        "slug": "epitalon",
        "category": "Telomerase Activator",
        "description": {
            "en": "Epitalon (Epithalon) is a synthetic tetrapeptide (Ala-Glu-Asp-Gly) based on the natural peptide Epithalamin extracted from the pineal gland. Developed by Russian scientist Vladimir Khavinson, it is one of the most studied anti-aging peptides. Epitalon activates telomerase, the enzyme that maintains telomere length, potentially slowing cellular aging.",
            "de": "Epitalon (Epithalon) ist ein synthetisches Tetrapeptid (Ala-Glu-Asp-Gly), basierend auf dem natürlichen Peptid Epithalamin aus der Zirbeldrüse. Entwickelt vom russischen Wissenschaftler Vladimir Khavinson, ist es eines der am meisten erforschten Anti-Aging-Peptide. Epitalon aktiviert Telomerase, das Enzym das Telomerlängen erhält."
        },
        "mechanism_of_action": {
            "en": "Epitalon activates the telomerase enzyme (hTERT), which adds telomeric repeats to chromosome ends, preventing telomere shortening during cell division. It also stimulates melatonin production from the pineal gland and modulates neuroendocrine function.",
            "de": "Epitalon aktiviert das Telomerase-Enzym (hTERT), das Telomer-Wiederholungen an Chromosomenenden anfügt und Telomerverkürzung bei der Zellteilung verhindert. Es stimuliert auch die Melatoninproduktion der Zirbeldrüse und moduliert neuroendokrine Funktionen."
        },
        "indications": [
            {"condition_en": "Cellular Aging", "condition_de": "Zelluläre Alterung", "description_en": "Telomere maintenance and longevity (research)", "description_de": "Telomererhaltung und Langlebigkeit (Forschung)"},
            {"condition_en": "Sleep Disorders", "condition_de": "Schlafstörungen", "description_en": "Melatonin cycle restoration in elderly (research)", "description_de": "Wiederherstellung des Melatonin-Zyklus bei Älteren (Forschung)"},
            {"condition_en": "Immune Senescence", "condition_de": "Immunseneszenz", "description_en": "Restoration of immune function with aging", "description_de": "Wiederherstellung der Immunfunktion im Alter"}
        ],
        "benefits": [
            {"benefit_en": "Telomerase activation and telomere maintenance", "benefit_de": "Telomerase-Aktivierung und Telomererhaltung"},
            {"benefit_en": "Restoration of melatonin production", "benefit_de": "Wiederherstellung der Melatoninproduktion"},
            {"benefit_en": "Potential lifespan extension (shown in animal studies)", "benefit_de": "Potenzielle Lebensverlängerung (in Tierstudien gezeigt)"},
            {"benefit_en": "Improved sleep quality", "benefit_de": "Verbesserte Schlafqualität"}
        ],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Mild discomfort at injection site", "description_de": "Leichte Beschwerden an der Injektionsstelle"},
            {"name_en": "Drowsiness", "name_de": "Schläfrigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Due to increased melatonin production", "description_de": "Durch erhöhte Melatoninproduktion"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Transient mild headache", "description_de": "Vorübergehende leichte Kopfschmerzen"},
            {"name_en": "Muscle stiffness", "name_de": "Muskelsteifheit", "severity": "mild", "frequency": "rare", "description_en": "Occasional muscle tension", "description_de": "Gelegentliche Muskelverspannung"},
            {"name_en": "Limited human safety data", "name_de": "Begrenzte Sicherheitsdaten am Menschen", "severity": "moderate", "frequency": "uncommon", "description_en": "Long-term safety not fully established", "description_de": "Langzeitsicherheit nicht vollständig etabliert"}
        ],
        "dosage": {
            "starting_dose": "5 mg",
            "maintenance_dose": "5-10 mg",
            "frequency_en": "Daily for 10-20 days, repeat every 4-6 months",
            "frequency_de": "Täglich für 10-20 Tage, alle 4-6 Monate wiederholen",
            "route_en": "Subcutaneous or intramuscular injection",
            "route_de": "Subkutane oder intramuskuläre Injektion",
            "notes_en": "Cycled protocol: 10-20 day courses with 4-6 month breaks",
            "notes_de": "Zyklisches Protokoll: 10-20 Tage Kuren mit 4-6 Monaten Pause"
        },
        "contraindications": [
            {"en": "Active cancer (theoretical telomerase concern)", "de": "Aktive Krebserkrankung (theoretische Telomerase-Bedenken)"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"},
            {"en": "Autoimmune disorders (caution)", "de": "Autoimmunerkrankungen (Vorsicht)"}
        ],
        "drug_interactions": ["Melatonin supplements (additive)", "Immunosuppressants", "Chemotherapy agents"],
        "research_status": {"phase": "Preclinical / Early Clinical", "fda_approved": False, "ema_approved": False, "notes_en": "Extensive research in Russia. Published studies show telomere elongation and lifespan extension in animals. Not approved in Western countries.", "notes_de": "Umfangreiche Forschung in Russland. Publizierte Studien zeigen Telomerverlängerung und Lebensverlängerung bei Tieren. In westlichen Ländern nicht zugelassen."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "390 Da",
        "amino_acid_count": "4",
        "half_life": "Estimated 2-3 hours",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C.", "de": "Lyophilisiert bei -20°C. Rekonstituiert bei 2-8°C."},
        "amino_acid_sequence": "AEDG",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with bacteriostatic water or sterile saline",
            "preparation_de": "Mit bakteriostatischem Wasser oder steriler Kochsalzlösung rekonstituieren",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "24 months (lyophilized)",
            "shelf_life_reconstituted": "14 days refrigerated",
            "light_sensitive": False,
            "solvent": "Bacteriostatic water"
        },
        "application_goals": [
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"},
            {"goal_en": "Immune Support", "goal_de": "Immununterstützung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Thymosin Alpha 1",
        "slug": "thymosin-alpha-1",
        "category": "Immune Modulator",
        "description": {
            "en": "Thymosin Alpha 1 (Tα1) is a naturally occurring peptide originally isolated from thymic tissue. Marketed as Zadaxin, it is approved in over 35 countries for treatment of hepatitis B and C, and as an immune adjuvant. It is a potent immune modulator that enhances T-cell function, dendritic cell maturation, and antibody responses.",
            "de": "Thymosin Alpha 1 (Tα1) ist ein natürlich vorkommendes Peptid, ursprünglich aus Thymusgewebe isoliert. Als Zadaxin vermarktet, ist es in über 35 Ländern zur Behandlung von Hepatitis B und C und als Immunadjuvans zugelassen. Es ist ein potenter Immunmodulator, der T-Zell-Funktion, dendritische Zellreifung und Antikörperantworten verstärkt."
        },
        "mechanism_of_action": {
            "en": "Thymosin Alpha 1 acts on toll-like receptors (TLR2, TLR9) on dendritic cells, enhancing antigen presentation. It promotes T-cell differentiation, activates natural killer cells, increases IL-2 and IFN-alpha production, and modulates both innate and adaptive immunity.",
            "de": "Thymosin Alpha 1 wirkt auf Toll-like-Rezeptoren (TLR2, TLR9) auf dendritischen Zellen und verstärkt die Antigenpräsentation. Es fördert T-Zell-Differenzierung, aktiviert natürliche Killerzellen, steigert IL-2- und IFN-alpha-Produktion und moduliert angeborene und adaptive Immunität."
        },
        "indications": [
            {"condition_en": "Chronic Hepatitis B", "condition_de": "Chronische Hepatitis B", "description_en": "Approved treatment in multiple countries", "description_de": "Zugelassene Behandlung in vielen Ländern"},
            {"condition_en": "Hepatitis C", "condition_de": "Hepatitis C", "description_en": "Combination therapy with interferon", "description_de": "Kombinationstherapie mit Interferon"},
            {"condition_en": "Immune Deficiency", "condition_de": "Immundefizienz", "description_en": "Immune restoration in immunocompromised patients", "description_de": "Immunwiederherstellung bei immungeschwächten Patienten"}
        ],
        "benefits": [
            {"benefit_en": "Powerful immune system enhancement", "benefit_de": "Starke Immunsystemverstärkung"},
            {"benefit_en": "Approved in 35+ countries", "benefit_de": "In über 35 Ländern zugelassen"},
            {"benefit_en": "Well-established safety record", "benefit_de": "Gut etabliertes Sicherheitsprofil"},
            {"benefit_en": "Synergistic with vaccines and other immunotherapies", "benefit_de": "Synergistisch mit Impfstoffen und anderen Immuntherapien"}
        ],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local redness, pain, or swelling", "description_de": "Lokale Rötung, Schmerzen oder Schwellung"},
            {"name_en": "Fatigue", "name_de": "Müdigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Temporary tiredness after injection", "description_de": "Vorübergehende Müdigkeit nach Injektion"},
            {"name_en": "Fever", "name_de": "Fieber", "severity": "mild", "frequency": "uncommon", "description_en": "Low-grade fever from immune activation", "description_de": "Leichtes Fieber durch Immunaktivierung"},
            {"name_en": "Muscle pain", "name_de": "Muskelschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Myalgia as part of immune response", "description_de": "Myalgie als Teil der Immunantwort"},
            {"name_en": "Rash", "name_de": "Hautausschlag", "severity": "mild", "frequency": "rare", "description_en": "Rare hypersensitivity reaction", "description_de": "Seltene Überempfindlichkeitsreaktion"}
        ],
        "dosage": {
            "starting_dose": "1.6 mg",
            "maintenance_dose": "1.6 mg",
            "frequency_en": "Twice weekly",
            "frequency_de": "Zweimal wöchentlich",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Standard protocol: 1.6 mg twice weekly for 6-12 months for hepatitis",
            "notes_de": "Standardprotokoll: 1,6 mg zweimal wöchentlich für 6-12 Monate bei Hepatitis"
        },
        "contraindications": [
            {"en": "Hypersensitivity to thymosin alpha 1", "de": "Überempfindlichkeit gegen Thymosin Alpha 1"},
            {"en": "Organ transplant recipients (may trigger rejection)", "de": "Organtransplantat-Empfänger (kann Abstoßung auslösen)"},
            {"en": "Severe autoimmune disease", "de": "Schwere Autoimmunerkrankung"}
        ],
        "drug_interactions": ["Immunosuppressants (antagonistic)", "Interferon (synergistic)", "Vaccines (adjuvant effect)"],
        "research_status": {"phase": "Approved (international)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved in 35+ countries (not US/EU). Orphan drug status in US. Studied for COVID-19, cancer immunotherapy, and vaccine enhancement.", "notes_de": "In über 35 Ländern zugelassen (nicht USA/EU). Orphan Drug Status in den USA. Untersucht für COVID-19, Krebsimmuntherapie und Impfverstärkung."},
        "manufacturer": "SciClone Pharmaceuticals (Zadaxin)",
        "molecular_weight": "3108 Da",
        "amino_acid_count": "28",
        "half_life": "2 hours",
        "storage_conditions": {"en": "Store lyophilized at 2-8°C. Protect from light.", "de": "Lyophilisiert bei 2-8°C lagern. Vor Licht schützen."},
        "amino_acid_sequence": "SDAAVDTSSEITTKDLKEKKEVVEEAEN",
        "reconstitution_info": {
            "preparation_en": "Reconstitute lyophilized powder with provided sterile diluent",
            "preparation_de": "Lyophilisiertes Pulver mit beiliegendem sterilem Lösungsmittel rekonstituieren",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "36 months",
            "shelf_life_reconstituted": "Use within 24 hours",
            "light_sensitive": True,
            "solvent": "Sterile water for injection"
        },
        "application_goals": [
            {"goal_en": "Immune Support", "goal_de": "Immununterstützung", "relevance": "primary"},
            {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "LL-37",
        "slug": "ll-37",
        "category": "Antimicrobial Peptide",
        "description": {
            "en": "LL-37 is the only human cathelicidin antimicrobial peptide, derived from the C-terminal domain of the precursor protein hCAP18. It is a 37-amino acid peptide with broad-spectrum antimicrobial activity against bacteria, viruses, and fungi. Beyond its antimicrobial role, LL-37 modulates inflammation, promotes wound healing, and has anti-biofilm properties.",
            "de": "LL-37 ist das einzige menschliche Cathelicidin-antimikrobielle Peptid, abgeleitet von der C-terminalen Domäne des Vorläuferproteins hCAP18. Es ist ein 37-Aminosäure-Peptid mit breitem antimikrobiellem Spektrum gegen Bakterien, Viren und Pilze. Über seine antimikrobielle Rolle hinaus moduliert LL-37 Entzündungen, fördert Wundheilung und hat Anti-Biofilm-Eigenschaften."
        },
        "mechanism_of_action": {
            "en": "LL-37 disrupts microbial membranes through electrostatic interaction with negatively charged bacterial surfaces. It also acts as an immunomodulator by binding to formyl peptide receptor 2 (FPR2), P2X7 receptor, and TLRs, modulating cytokine production and immune cell recruitment.",
            "de": "LL-37 stört mikrobielle Membranen durch elektrostatische Interaktion mit negativ geladenen bakteriellen Oberflächen. Es wirkt auch als Immunmodulator durch Bindung an Formylpeptidrezeptor 2 (FPR2), P2X7-Rezeptor und TLRs und moduliert Zytokinproduktion und Immunzellrekrutierung."
        },
        "indications": [
            {"condition_en": "Bacterial Infections", "condition_de": "Bakterielle Infektionen", "description_en": "Broad-spectrum antimicrobial activity (research)", "description_de": "Breitspektrum-antimikrobielle Aktivität (Forschung)"},
            {"condition_en": "Chronic Wounds", "condition_de": "Chronische Wunden", "description_en": "Biofilm disruption and wound healing promotion", "description_de": "Biofilm-Zerstörung und Wundheilungsförderung"},
            {"condition_en": "Upper Respiratory Infections", "condition_de": "Obere Atemwegsinfektionen", "description_en": "Antiviral and immunomodulatory effects (research)", "description_de": "Antivirale und immunmodulatorische Effekte (Forschung)"}
        ],
        "benefits": [
            {"benefit_en": "Broad antimicrobial spectrum (bacteria, viruses, fungi)", "benefit_de": "Breites antimikrobielles Spektrum (Bakterien, Viren, Pilze)"},
            {"benefit_en": "Anti-biofilm activity", "benefit_de": "Anti-Biofilm-Aktivität"},
            {"benefit_en": "Wound healing promotion", "benefit_de": "Wundheilungsförderung"},
            {"benefit_en": "Immunomodulatory properties", "benefit_de": "Immunmodulatorische Eigenschaften"}
        ],
        "side_effects": [
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local pain and redness", "description_de": "Lokale Schmerzen und Rötung"},
            {"name_en": "Hemolytic activity", "name_de": "Hämolytische Aktivität", "severity": "moderate", "frequency": "rare", "description_en": "At high concentrations, may affect red blood cells", "description_de": "Bei hohen Konzentrationen können rote Blutkörperchen beeinflusst werden"},
            {"name_en": "Inflammation at high doses", "name_de": "Entzündung bei hohen Dosen", "severity": "moderate", "frequency": "uncommon", "description_en": "Pro-inflammatory effects at supraphysiologic levels", "description_de": "Pro-inflammatorische Effekte bei supraphysiologischen Spiegeln"},
            {"name_en": "Cytotoxicity concerns", "name_de": "Zytotoxizitätsbedenken", "severity": "moderate", "frequency": "rare", "description_en": "High doses may affect host cells", "description_de": "Hohe Dosen können Wirtszellen beeinflussen"},
            {"name_en": "Limited clinical data", "name_de": "Begrenzte klinische Daten", "severity": "moderate", "frequency": "uncommon", "description_en": "Human dosing protocols not well established", "description_de": "Humandosierungsprotokolle nicht gut etabliert"}
        ],
        "dosage": {
            "starting_dose": "50-100 mcg",
            "maintenance_dose": "100-200 mcg",
            "frequency_en": "1-2 times daily (research protocols vary)",
            "frequency_de": "1-2 mal täglich (Forschungsprotokolle variieren)",
            "route_en": "Subcutaneous injection or topical",
            "route_de": "Subkutane Injektion oder topisch",
            "notes_en": "Research compound - clinical dosing not standardized",
            "notes_de": "Forschungssubstanz - klinische Dosierung nicht standardisiert"
        },
        "contraindications": [
            {"en": "Known hypersensitivity", "de": "Bekannte Überempfindlichkeit"},
            {"en": "Active autoimmune disorders (may exacerbate)", "de": "Aktive Autoimmunerkrankungen (kann verschlechtern)"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["Immunosuppressants", "Antibiotics (potential synergy)", "Anti-inflammatory agents"],
        "research_status": {"phase": "Preclinical / Phase 1", "fda_approved": False, "ema_approved": False, "notes_en": "Active research for wound healing, infections, and cancer. Some analogs in clinical development.", "notes_de": "Aktive Forschung für Wundheilung, Infektionen und Krebs. Einige Analoga in klinischer Entwicklung."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "4493 Da",
        "amino_acid_count": "37",
        "half_life": "Estimated 1 hour (plasma)",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Reconstituted at 2-8°C. Avoid repeated freeze-thaw.", "de": "Lyophilisiert bei -20°C. Rekonstituiert bei 2-8°C. Wiederholtes Einfrieren-Auftauen vermeiden."},
        "amino_acid_sequence": "LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with sterile water. Use aseptic technique.",
            "preparation_de": "Mit sterilem Wasser rekonstituieren. Aseptische Technik anwenden.",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "12 months (lyophilized)",
            "shelf_life_reconstituted": "7 days refrigerated",
            "light_sensitive": True,
            "solvent": "Sterile water for injection"
        },
        "application_goals": [
            {"goal_en": "Immune Support", "goal_de": "Immununterstützung", "relevance": "primary"},
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Kisspeptin",
        "slug": "kisspeptin",
        "category": "Reproductive Neuropeptide",
        "description": {
            "en": "Kisspeptin is a neuropeptide encoded by the KISS1 gene that plays a master regulatory role in the hypothalamic-pituitary-gonadal (HPG) axis. It is the primary trigger for GnRH release, making it essential for puberty onset and reproductive function. Various forms exist (kisspeptin-54, -14, -13, -10), all sharing the same C-terminal active decapeptide.",
            "de": "Kisspeptin ist ein Neuropeptid, codiert durch das KISS1-Gen, das eine übergeordnete regulatorische Rolle in der Hypothalamus-Hypophysen-Gonaden-Achse (HPG) spielt. Es ist der primäre Auslöser der GnRH-Freisetzung und damit essentiell für Pubertätsbeginn und Fortpflanzungsfunktion. Verschiedene Formen existieren (Kisspeptin-54, -14, -13, -10)."
        },
        "mechanism_of_action": {
            "en": "Kisspeptin binds to the GPR54 (KISS1R) receptor on GnRH neurons in the hypothalamus, stimulating GnRH secretion and subsequently LH and FSH release. This cascade drives gonadal steroid production and gametogenesis.",
            "de": "Kisspeptin bindet an den GPR54 (KISS1R)-Rezeptor auf GnRH-Neuronen im Hypothalamus und stimuliert die GnRH-Sekretion und anschließend LH- und FSH-Freisetzung. Diese Kaskade treibt die gonadale Steroidproduktion und Gametogenese an."
        },
        "indications": [
            {"condition_en": "Infertility Diagnostics", "condition_de": "Infertilitätsdiagnostik", "description_en": "Assessment of HPG axis function and GnRH neuron responsiveness", "description_de": "Beurteilung der HPG-Achsen-Funktion und GnRH-Neuron-Ansprechbarkeit"},
            {"condition_en": "Hypogonadotropic Hypogonadism", "condition_de": "Hypogonadotroper Hypogonadismus", "description_en": "Potential treatment for GnRH-deficient conditions", "description_de": "Potenzielle Behandlung bei GnRH-defizienten Zuständen"},
            {"condition_en": "IVF Oocyte Maturation", "condition_de": "IVF-Oozytenreifung", "description_en": "Trigger for final oocyte maturation in IVF (research)", "description_de": "Auslöser für finale Oozytenreifung bei IVF (Forschung)"}
        ],
        "benefits": [
            {"benefit_en": "Physiological HPG axis stimulation", "benefit_de": "Physiologische HPG-Achsen-Stimulation"},
            {"benefit_en": "Lower OHSS risk than hCG trigger in IVF", "benefit_de": "Geringeres OHSS-Risiko als hCG-Trigger bei IVF"},
            {"benefit_en": "Diagnostic tool for reproductive disorders", "benefit_de": "Diagnostisches Werkzeug für reproduktive Störungen"},
            {"benefit_en": "Short-acting (predictable kinetics)", "benefit_de": "Kurzwirksam (vorhersehbare Kinetik)"}
        ],
        "side_effects": [
            {"name_en": "Hot flashes", "name_de": "Hitzewallungen", "severity": "mild", "frequency": "common", "description_en": "From acute gonadotropin stimulation", "description_de": "Durch akute Gonadotropin-Stimulation"},
            {"name_en": "Abdominal discomfort", "name_de": "Bauchbeschwerden", "severity": "mild", "frequency": "common", "description_en": "Related to ovarian stimulation in women", "description_de": "Zusammenhängend mit ovarieller Stimulation bei Frauen"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Common after infusion", "description_de": "Häufig nach Infusion"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild GI side effect", "description_de": "Leichte GI-Nebenwirkung"},
            {"name_en": "Tachyphylaxis", "name_de": "Tachyphylaxie", "severity": "moderate", "frequency": "common", "description_en": "Continuous exposure leads to GnRH neuron desensitization", "description_de": "Kontinuierliche Exposition führt zur GnRH-Neuron-Desensibilisierung"}
        ],
        "dosage": {
            "starting_dose": "1 nmol/kg (IV) or 6.4 nmol/kg (SC)",
            "maintenance_dose": "Variable by protocol",
            "frequency_en": "Single bolus or pulsatile infusion",
            "frequency_de": "Einzelbolus oder pulsatile Infusion",
            "route_en": "Intravenous or subcutaneous injection",
            "route_de": "Intravenöse oder subkutane Injektion",
            "notes_en": "Continuous administration causes desensitization; pulsatile preferred",
            "notes_de": "Kontinuierliche Gabe verursacht Desensibilisierung; pulsatil bevorzugt"
        },
        "contraindications": [
            {"en": "Hormone-sensitive cancers", "de": "Hormonsensitive Krebserkrankungen"},
            {"en": "Pregnancy", "de": "Schwangerschaft"},
            {"en": "Severe hepatic impairment", "de": "Schwere Leberfunktionsstörung"}
        ],
        "drug_interactions": ["GnRH agonists/antagonists", "Hormone replacement therapy", "Gonadotropins"],
        "research_status": {"phase": "Phase 2", "fda_approved": False, "ema_approved": False, "notes_en": "Active clinical trials for IVF trigger, diagnostic use, and reproductive disorders. Kisspeptin-54 most studied form.", "notes_de": "Aktive klinische Studien als IVF-Trigger, diagnostische Anwendung und reproduktive Störungen. Kisspeptin-54 ist die am meisten untersuchte Form."},
        "manufacturer": "Various research suppliers",
        "molecular_weight": "5863 Da (kisspeptin-54)",
        "amino_acid_count": "54 (full form)",
        "half_life": "28 minutes (kisspeptin-54 IV)",
        "storage_conditions": {"en": "Store lyophilized at -20°C. Protect from light.", "de": "Lyophilisiert bei -20°C lagern. Vor Licht schützen."},
        "amino_acid_sequence": "GTSLSPPPESSGSRQQPGLSAPHSRQIPAPQGAVLVQREKDLPNYNWNSFGLRF",
        "reconstitution_info": {
            "preparation_en": "Reconstitute with sterile saline for IV use",
            "preparation_de": "Mit steriler Kochsalzlösung für IV-Anwendung rekonstituieren",
            "storage_temperature": "-20°C (powder), 2-8°C (reconstituted)",
            "shelf_life_unopened": "12 months (lyophilized)",
            "shelf_life_reconstituted": "Use within 4 hours",
            "light_sensitive": True,
            "solvent": "0.9% sodium chloride"
        },
        "application_goals": [
            {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"},
            {"goal_en": "Cognitive Enhancement", "goal_de": "Kognitive Verbesserung", "relevance": "secondary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Retatrutide",
        "slug": "retatrutide",
        "category": "Triple Incretin Receptor Agonist",
        "description": {
            "en": "Retatrutide (LY3437943) is a novel triple agonist targeting GIP, GLP-1, and glucagon receptors simultaneously. Developed by Eli Lilly, it represents the next generation of incretin-based therapies. Phase 2 trials showed unprecedented weight loss of up to 24% body weight at 48 weeks, making it potentially the most effective obesity treatment ever studied.",
            "de": "Retatrutid (LY3437943) ist ein neuartiger Tripleagonist, der gleichzeitig GIP-, GLP-1- und Glukagonrezeptoren aktiviert. Von Eli Lilly entwickelt, repräsentiert es die nächste Generation inkretinbasierter Therapien. Phase-2-Studien zeigten beispiellosen Gewichtsverlust von bis zu 24% des Körpergewichts nach 48 Wochen."
        },
        "mechanism_of_action": {
            "en": "Retatrutide simultaneously activates three receptors: GIP-R enhances insulin secretion and may improve fat metabolism; GLP-1R provides appetite suppression, insulin release, and gastric slowing; Glucagon-R increases energy expenditure and hepatic fat oxidation. The triple action provides additive metabolic benefits.",
            "de": "Retatrutid aktiviert gleichzeitig drei Rezeptoren: GIP-R verstärkt Insulinsekretion und kann Fettstoffwechsel verbessern; GLP-1R bietet Appetitunterdrückung, Insulinfreisetzung und Magenverlangsamung; Glukagon-R erhöht Energieverbrauch und hepatische Fettoxidation. Die Dreifachwirkung bietet additive metabolische Vorteile."
        },
        "indications": [
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Chronic weight management with unprecedented efficacy", "description_de": "Chronisches Gewichtsmanagement mit beispielloser Wirksamkeit"},
            {"condition_en": "Type 2 Diabetes", "condition_de": "Typ-2-Diabetes", "description_en": "Glycemic control with significant weight reduction", "description_de": "Blutzuckerkontrolle mit signifikanter Gewichtsreduktion"},
            {"condition_en": "MASLD/NASH", "condition_de": "MASLD/NASH", "description_en": "Metabolic liver disease improvement through glucagon receptor activation", "description_de": "Verbesserung metabolischer Lebererkrankung durch Glukagonrezeptor-Aktivierung"}
        ],
        "benefits": [
            {"benefit_en": "Up to 24% body weight reduction (Phase 2)", "benefit_de": "Bis zu 24% Körpergewichtsreduktion (Phase 2)"},
            {"benefit_en": "Triple receptor mechanism for additive benefits", "benefit_de": "Dreifacher Rezeptormechanismus für additive Vorteile"},
            {"benefit_en": "Potential liver fat reduction via glucagon activity", "benefit_de": "Potenzielle Leberfettreduktion durch Glukagonaktivität"},
            {"benefit_en": "Once-weekly dosing", "benefit_de": "Einmal wöchentliche Dosierung"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common GI side effect", "description_de": "Häufigste GI-Nebenwirkung"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "GI disturbance during dose escalation", "description_de": "GI-Störung während Dosiseskalation"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "moderate", "frequency": "common", "description_en": "More common at higher doses", "description_de": "Häufiger bei höheren Dosen"},
            {"name_en": "Decreased appetite", "name_de": "Verminderter Appetit", "severity": "mild", "frequency": "common", "description_en": "Therapeutic effect contributing to weight loss", "description_de": "Therapeutischer Effekt der zur Gewichtsabnahme beiträgt"},
            {"name_en": "Increased heart rate", "name_de": "Erhöhte Herzfrequenz", "severity": "moderate", "frequency": "uncommon", "description_en": "Small increase in resting heart rate observed", "description_de": "Kleiner Anstieg der Ruheherzfrequenz beobachtet"}
        ],
        "dosage": {
            "starting_dose": "0.5 mg",
            "maintenance_dose": "4-12 mg",
            "frequency_en": "Once weekly",
            "frequency_de": "Einmal wöchentlich",
            "route_en": "Subcutaneous injection",
            "route_de": "Subkutane Injektion",
            "notes_en": "Dose escalation over 24 weeks. Phase 3 trials ongoing.",
            "notes_de": "Dosiseskalation über 24 Wochen. Phase-3-Studien laufen."
        },
        "contraindications": [
            {"en": "Medullary thyroid carcinoma history or MEN 2", "de": "Vorgeschichte eines medullären Schilddrüsenkarzinoms oder MEN 2"},
            {"en": "Severe gastrointestinal disease", "de": "Schwere gastrointestinale Erkrankung"},
            {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"}
        ],
        "drug_interactions": ["Insulin (hypoglycemia risk)", "Sulfonylureas", "Oral medications (delayed absorption)"],
        "research_status": {"phase": "Phase 3", "fda_approved": False, "ema_approved": False, "notes_en": "Phase 3 trials ongoing (TRIUMPH program). Phase 2 showed best-in-class weight loss up to 24.2%. Expected FDA submission anticipated.", "notes_de": "Phase-3-Studien laufen (TRIUMPH-Programm). Phase 2 zeigte klassenbesten Gewichtsverlust bis 24,2%. FDA-Einreichung erwartet."},
        "manufacturer": "Eli Lilly",
        "molecular_weight": "4482 Da",
        "amino_acid_count": "39",
        "half_life": "6 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C (clinical trial formulation)", "de": "Kühlschrank bei 2-8°C (klinische Studienformulierung)"},
        "amino_acid_sequence": "HXEGTFTSDYSIXLDKIAQRAFVQWLIAGGPSSGAPPPS",
        "reconstitution_info": {
            "preparation_en": "Pre-filled pen expected for commercial formulation",
            "preparation_de": "Fertigpen für kommerzielle Formulierung erwartet",
            "storage_temperature": "2-8°C",
            "shelf_life_unopened": "To be determined",
            "shelf_life_reconstituted": "Pre-filled, single use expected",
            "light_sensitive": True,
            "solvent": "Pre-filled solution (expected)"
        },
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    }
]


def main():
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    col = db["peptides"]

    # Create indexes
    col.create_index("slug", unique=True)
    col.create_index([("name", "text"), ("category", "text")])

    inserted = 0
    skipped = 0

    for peptide in PEPTIDES:
        if col.find_one({"slug": peptide["slug"]}):
            print(f"  SKIP: {peptide['name']} (already exists)")
            skipped += 1
        else:
            col.insert_one(peptide)
            print(f"  OK:   {peptide['name']}")
            inserted += 1

    print(f"\nDone! Inserted: {inserted}, Skipped: {skipped}, Total in DB: {col.count_documents({})}")
    client.close()


if __name__ == "__main__":
    main()
