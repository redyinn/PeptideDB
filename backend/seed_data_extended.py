"""Extended seed: 50+ additional scientifically accurate peptide profiles."""
import re
from datetime import datetime, timezone
from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "peptide_research"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

NOW = datetime.now(timezone.utc).isoformat()

PEPTIDES = [
    # ── GLP-1 / METABOLIC ───────────────────────────────────────
    {
        "name": "Exenatide",
        "slug": "exenatide",
        "category": "GLP-1 Receptor Agonist",
        "description": {
            "en": "Exenatide (Byetta/Bydureon) is a synthetic version of exendin-4, a peptide originally found in the saliva of the Gila monster lizard. It was the first GLP-1 receptor agonist approved for type 2 diabetes in 2005. Exenatide stimulates insulin secretion and suppresses glucagon in a glucose-dependent manner, reducing the risk of hypoglycemia.",
            "de": "Exenatid (Byetta/Bydureon) ist eine synthetische Version von Exendin-4, einem Peptid, das ursprünglich im Speichel der Gila-Krustenechse gefunden wurde. Es war der erste GLP-1-Rezeptoragonist, der 2005 für Typ-2-Diabetes zugelassen wurde. Exenatid stimuliert die Insulinsekretion und unterdrückt Glukagon glukoseabhängig."
        },
        "mechanism_of_action": {
            "en": "Binds to and activates the GLP-1 receptor, enhancing glucose-dependent insulin secretion, suppressing inappropriately elevated glucagon, slowing gastric emptying, and promoting satiety.",
            "de": "Bindet an den GLP-1-Rezeptor und aktiviert ihn, verstärkt die glukoseabhängige Insulinsekretion, unterdrückt unangemessen erhöhtes Glukagon, verlangsamt die Magenentleerung und fördert das Sättigungsgefühl."
        },
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "Adjunct therapy for glycemic control", "description_de": "Begleittherapie zur Blutzuckerkontrolle"},
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Off-label use for weight management", "description_de": "Off-Label-Anwendung zur Gewichtskontrolle"},
            {"condition_en": "Metabolic Syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Improvement of metabolic parameters", "description_de": "Verbesserung metabolischer Parameter"}
        ],
        "benefits": [
            {"benefit_en": "HbA1c reduction of 0.8-1.5%", "benefit_de": "HbA1c-Senkung von 0,8-1,5%"},
            {"benefit_en": "Moderate weight loss (2-4 kg)", "benefit_de": "Moderate Gewichtsabnahme (2-4 kg)"},
            {"benefit_en": "Low hypoglycemia risk", "benefit_de": "Niedriges Hypoglykämierisiko"},
            {"benefit_en": "Extended-release formulation available (weekly)", "benefit_de": "Retardformulierung verfügbar (wöchentlich)"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common, usually transient", "description_de": "Am häufigsten, meist vorübergehend"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "mild", "frequency": "common", "description_en": "GI side effect during initiation", "description_de": "GI-Nebenwirkung bei Therapiebeginn"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "Usually mild and self-limiting", "description_de": "Meist mild und selbstlimitierend"},
            {"name_en": "Injection site nodules", "name_de": "Knötchen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Especially with extended-release form", "description_de": "Besonders bei Retardformulierung"},
            {"name_en": "Pancreatitis", "name_de": "Pankreatitis", "severity": "severe", "frequency": "rare", "description_en": "Acute pancreatitis reported in post-marketing", "description_de": "Akute Pankreatitis in Post-Marketing berichtet"}
        ],
        "dosage": {"starting_dose": "5 mcg", "maintenance_dose": "10 mcg BID or 2 mg weekly", "frequency_en": "Twice daily or once weekly (ER)", "frequency_de": "Zweimal täglich oder einmal wöchentlich (Retard)", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Administer within 60 min before meals", "notes_de": "Innerhalb von 60 Min vor den Mahlzeiten verabreichen"},
        "contraindications": [
            {"en": "Personal or family history of medullary thyroid carcinoma", "de": "Persönliche oder familiäre Vorgeschichte eines medullären Schilddrüsenkarzinoms"},
            {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"},
            {"en": "Severe renal impairment (CrCl <30 mL/min)", "de": "Schwere Nierenfunktionsstörung (CrCl <30 ml/min)"}
        ],
        "drug_interactions": ["Insulin (increased hypoglycemia)", "Sulfonylureas", "Warfarin (delayed absorption)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved 2005 (Byetta), 2012 (Bydureon)", "notes_de": "FDA-Zulassung 2005 (Byetta), 2012 (Bydureon)"},
        "manufacturer": "AstraZeneca",
        "molecular_weight": "4186 Da",
        "amino_acid_count": "39",
        "half_life": "2.4 hours (IR), steady state weekly (ER)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C before first use", "de": "Vor Erstgebrauch bei 2-8°C kühlen"},
        "amino_acid_sequence": "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPPS",
        "reconstitution_info": {"preparation_en": "Pre-filled pen, no reconstitution needed", "preparation_de": "Fertigpen, keine Rekonstitution nötig", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "30 days at room temperature", "light_sensitive": False, "solvent": "Pre-filled solution"},
        "application_goals": [
            {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"},
            {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}
        ],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Lixisenatide",
        "slug": "lixisenatide",
        "category": "GLP-1 Receptor Agonist",
        "description": {
            "en": "Lixisenatide (Adlyxin) is a once-daily GLP-1 receptor agonist approved for type 2 diabetes. It is also available in a fixed-ratio combination with insulin glargine (Soliqua). Lixisenatide primarily targets postprandial glucose through delayed gastric emptying.",
            "de": "Lixisenatid (Adlyxin) ist ein einmal täglich angewendeter GLP-1-Rezeptoragonist für Typ-2-Diabetes. Es ist auch als Fixkombination mit Insulin Glargin (Soliqua) erhältlich. Lixisenatid wirkt vor allem auf den postprandialen Blutzucker durch verzögerte Magenentleerung."
        },
        "mechanism_of_action": {"en": "Selective GLP-1 receptor agonist that primarily reduces postprandial glucose via slowed gastric emptying and glucose-dependent insulin secretion.", "de": "Selektiver GLP-1-Rezeptoragonist, der postprandiale Glukose hauptsächlich durch verzögerte Magenentleerung und glukoseabhängige Insulinsekretion senkt."},
        "indications": [
            {"condition_en": "Type 2 Diabetes Mellitus", "condition_de": "Typ-2-Diabetes mellitus", "description_en": "Adjunct to diet and exercise", "description_de": "Ergänzung zu Diät und Bewegung"},
            {"condition_en": "Combination with basal insulin", "condition_de": "Kombination mit Basalinsulin", "description_en": "Available as Soliqua (with insulin glargine)", "description_de": "Erhältlich als Soliqua (mit Insulin Glargin)"},
            {"condition_en": "Postprandial hyperglycemia", "condition_de": "Postprandiale Hyperglykämie", "description_en": "Particularly effective for post-meal glucose spikes", "description_de": "Besonders wirksam bei Blutzuckerspitzen nach Mahlzeiten"}
        ],
        "benefits": [
            {"benefit_en": "Effective postprandial glucose reduction", "benefit_de": "Effektive postprandiale Glukosesenkung"},
            {"benefit_en": "Once-daily dosing", "benefit_de": "Einmal tägliche Dosierung"},
            {"benefit_en": "Combination option with basal insulin", "benefit_de": "Kombinationsmöglichkeit mit Basalinsulin"},
            {"benefit_en": "Moderate weight loss", "benefit_de": "Moderate Gewichtsabnahme"}
        ],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "Most common side effect", "description_de": "Häufigste Nebenwirkung"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "mild", "frequency": "common", "description_en": "Usually transient", "description_de": "Meist vorübergehend"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Mild and self-limiting", "description_de": "Mild und selbstlimitierend"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional occurrence", "description_de": "Gelegentliches Auftreten"},
            {"name_en": "Pancreatitis", "name_de": "Pankreatitis", "severity": "severe", "frequency": "rare", "description_en": "Rare but serious", "description_de": "Selten aber schwerwiegend"}
        ],
        "dosage": {"starting_dose": "10 mcg", "maintenance_dose": "20 mcg", "frequency_en": "Once daily", "frequency_de": "Einmal täglich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Administer within 1 hour before first meal", "notes_de": "Innerhalb 1 Stunde vor der ersten Mahlzeit verabreichen"},
        "contraindications": [{"en": "Hypersensitivity to lixisenatide", "de": "Überempfindlichkeit gegen Lixisenatid"}, {"en": "History of medullary thyroid carcinoma", "de": "Vorgeschichte eines medullären Schilddrüsenkarzinoms"}, {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"}],
        "drug_interactions": ["Oral contraceptives (take 1h before or 11h after)", "Antibiotics", "Warfarin"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved 2016", "notes_de": "FDA-Zulassung 2016"},
        "manufacturer": "Sanofi",
        "molecular_weight": "4858 Da", "amino_acid_count": "44", "half_life": "3 hours",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPSKKKKKK",
        "reconstitution_info": {"preparation_en": "Pre-filled pen", "preparation_de": "Fertigpen", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "14 days at room temperature", "light_sensitive": False, "solvent": "Pre-filled solution"},
        "application_goals": [{"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}, {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── GROWTH HORMONE SECRETAGOGUES ─────────────────────────────
    {
        "name": "GHRP-6",
        "slug": "ghrp-6",
        "category": "Growth Hormone Releasing Peptide",
        "description": {
            "en": "GHRP-6 (Growth Hormone Releasing Peptide-6) is a synthetic hexapeptide that stimulates growth hormone release by acting on the ghrelin receptor (GHS-R1a). It is one of the earliest and most studied growth hormone secretagogues. GHRP-6 also stimulates appetite and has cytoprotective properties, particularly for the gastrointestinal tract and heart.",
            "de": "GHRP-6 (Growth Hormone Releasing Peptide-6) ist ein synthetisches Hexapeptid, das die Wachstumshormonfreisetzung durch Wirkung auf den Ghrelin-Rezeptor (GHS-R1a) stimuliert. Es ist einer der frühesten und am meisten untersuchten Wachstumshormon-Sekretagoga. GHRP-6 stimuliert auch den Appetit und hat zytoprotektive Eigenschaften."
        },
        "mechanism_of_action": {"en": "Acts as a ghrelin mimetic, binding to GHS-R1a receptors in the pituitary and hypothalamus to stimulate pulsatile growth hormone release. Also increases appetite via ghrelin pathway activation and has direct cytoprotective effects.", "de": "Wirkt als Ghrelin-Mimetikum, bindet an GHS-R1a-Rezeptoren in Hypophyse und Hypothalamus zur Stimulation der pulsatilen Wachstumshormonfreisetzung. Steigert auch den Appetit und hat direkte zytoprotektive Effekte."},
        "indications": [
            {"condition_en": "Growth hormone deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Stimulation of endogenous GH production", "description_de": "Stimulation der endogenen GH-Produktion"},
            {"condition_en": "Muscle wasting", "condition_de": "Muskelschwund", "description_en": "Research for cachexia and sarcopenia", "description_de": "Forschung bei Kachexie und Sarkopenie"},
            {"condition_en": "Gastroprotection", "condition_de": "Gastroprotektion", "description_en": "Protective effects on GI mucosa", "description_de": "Schützende Wirkung auf die GI-Schleimhaut"}
        ],
        "benefits": [
            {"benefit_en": "Potent GH release stimulation", "benefit_de": "Potente GH-Freisetzungsstimulation"},
            {"benefit_en": "Increased IGF-1 levels", "benefit_de": "Erhöhte IGF-1-Spiegel"},
            {"benefit_en": "Appetite stimulation (useful in wasting)", "benefit_de": "Appetitstimulation (nützlich bei Auszehrung)"},
            {"benefit_en": "Cytoprotective properties", "benefit_de": "Zytoprotektive Eigenschaften"}
        ],
        "side_effects": [
            {"name_en": "Increased appetite", "name_de": "Gesteigerter Appetit", "severity": "mild", "frequency": "common", "description_en": "Strong hunger increase due to ghrelin activation", "description_de": "Starke Hungersteigerung durch Ghrelin-Aktivierung"},
            {"name_en": "Water retention", "name_de": "Wassereinlagerungen", "severity": "mild", "frequency": "common", "description_en": "Temporary fluid retention", "description_de": "Vorübergehende Flüssigkeitsretention"},
            {"name_en": "Cortisol increase", "name_de": "Kortisolanstieg", "severity": "mild", "frequency": "common", "description_en": "Transient cortisol elevation", "description_de": "Vorübergehende Kortisolerhöhung"},
            {"name_en": "Tingling/numbness", "name_de": "Kribbeln/Taubheit", "severity": "mild", "frequency": "uncommon", "description_en": "Paresthesias in extremities", "description_de": "Parästhesien in den Extremitäten"},
            {"name_en": "Elevated prolactin", "name_de": "Erhöhtes Prolaktin", "severity": "mild", "frequency": "uncommon", "description_en": "Mild prolactin increase", "description_de": "Leichter Prolaktinanstieg"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "100-300 mcg", "frequency_en": "1-3 times daily", "frequency_de": "1-3 mal täglich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Best administered on empty stomach", "notes_de": "Am besten nüchtern verabreichen"},
        "contraindications": [{"en": "Active malignancy", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy and breastfeeding", "de": "Schwangerschaft und Stillzeit"}, {"en": "Pituitary tumors", "de": "Hypophysentumoren"}],
        "drug_interactions": ["Exogenous GH (synergistic)", "Insulin (altered sensitivity)", "Glucocorticoids"],
        "research_status": {"phase": "Phase II", "fda_approved": False, "ema_approved": False, "notes_en": "Research compound, not approved for clinical use", "notes_de": "Forschungssubstanz, nicht für klinische Anwendung zugelassen"},
        "manufacturer": "Research compound",
        "molecular_weight": "873 Da", "amino_acid_count": "6", "half_life": "15-60 minutes",
        "storage_conditions": {"en": "Store lyophilized at -20°C, reconstituted at 2-8°C", "de": "Lyophilisiert bei -20°C, rekonstituiert bei 2-8°C lagern"},
        "amino_acid_sequence": "His-D-Trp-Ala-Trp-D-Phe-Lys-NH2",
        "reconstitution_info": {"preparation_en": "Reconstitute lyophilized powder with bacteriostatic water", "preparation_de": "Lyophilisiertes Pulver mit bakteriostatischem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months at -20°C", "shelf_life_reconstituted": "21 days refrigerated", "light_sensitive": True, "solvent": "Bacteriostatic water"},
        "application_goals": [{"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "GHRP-2",
        "slug": "ghrp-2",
        "category": "Growth Hormone Releasing Peptide",
        "description": {
            "en": "GHRP-2 (Growth Hormone Releasing Peptide-2, Pralmorelin) is a synthetic hexapeptide and one of the most potent growth hormone secretagogues. Unlike GHRP-6, it causes less appetite stimulation while producing stronger GH release. GHRP-2 is approved in Japan as a diagnostic agent for GH deficiency under the name Pralmorelin.",
            "de": "GHRP-2 (Growth Hormone Releasing Peptide-2, Pralmorelin) ist ein synthetisches Hexapeptid und einer der potentesten Wachstumshormon-Sekretagoga. Im Gegensatz zu GHRP-6 verursacht es weniger Appetitsteigerung bei stärkerer GH-Freisetzung. GHRP-2 ist in Japan als Diagnostikum für GH-Mangel unter dem Namen Pralmorelin zugelassen."
        },
        "mechanism_of_action": {"en": "Binds to the GHS-R1a receptor, stimulating growth hormone release from the anterior pituitary. Has a stronger GH-releasing effect than GHRP-6 with less ghrelin-related appetite stimulation. Also mildly stimulates ACTH and cortisol.", "de": "Bindet an den GHS-R1a-Rezeptor und stimuliert die Wachstumshormonfreisetzung aus dem Hypophysenvorderlappen. Hat eine stärkere GH-freisetzende Wirkung als GHRP-6 mit weniger ghrelinbedingter Appetitstimulation."},
        "indications": [
            {"condition_en": "GH deficiency diagnosis", "condition_de": "GH-Mangel-Diagnostik", "description_en": "Approved diagnostic agent in Japan", "description_de": "Zugelassenes Diagnostikum in Japan"},
            {"condition_en": "Growth hormone deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Research for GH replacement", "description_de": "Forschung zur GH-Substitution"},
            {"condition_en": "Anti-aging research", "condition_de": "Anti-Aging-Forschung", "description_en": "Investigation of age-related GH decline", "description_de": "Untersuchung des altersbedingten GH-Rückgangs"}
        ],
        "benefits": [
            {"benefit_en": "Most potent GHRP for GH release", "benefit_de": "Potentestes GHRP zur GH-Freisetzung"},
            {"benefit_en": "Less appetite stimulation than GHRP-6", "benefit_de": "Weniger Appetitsteigerung als GHRP-6"},
            {"benefit_en": "Improved sleep quality", "benefit_de": "Verbesserte Schlafqualität"},
            {"benefit_en": "Increased lean body mass", "benefit_de": "Erhöhte fettfreie Körpermasse"}
        ],
        "side_effects": [
            {"name_en": "Mild appetite increase", "name_de": "Leichte Appetitsteigerung", "severity": "mild", "frequency": "common", "description_en": "Less than GHRP-6 but still present", "description_de": "Weniger als GHRP-6 aber vorhanden"},
            {"name_en": "Water retention", "name_de": "Wassereinlagerungen", "severity": "mild", "frequency": "common", "description_en": "Temporary", "description_de": "Vorübergehend"},
            {"name_en": "Cortisol elevation", "name_de": "Kortisolerhöhung", "severity": "mild", "frequency": "common", "description_en": "Transient ACTH/cortisol increase", "description_de": "Vorübergehender ACTH/Kortisol-Anstieg"},
            {"name_en": "Drowsiness", "name_de": "Schläfrigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Especially with evening dosing", "description_de": "Besonders bei abendlicher Dosierung"},
            {"name_en": "Prolactin increase", "name_de": "Prolaktinanstieg", "severity": "mild", "frequency": "uncommon", "description_en": "Mild and transient", "description_de": "Mild und vorübergehend"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "100-300 mcg", "frequency_en": "1-3 times daily", "frequency_de": "1-3 mal täglich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Administer on empty stomach for best GH pulse", "notes_de": "Nüchtern verabreichen für besten GH-Puls"},
        "contraindications": [{"en": "Active cancer", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy/lactation", "de": "Schwangerschaft/Stillzeit"}, {"en": "Hypothalamic-pituitary tumors", "de": "Hypothalamus-Hypophysen-Tumoren"}],
        "drug_interactions": ["Growth hormone", "Insulin", "Corticosteroids"],
        "research_status": {"phase": "Approved (Japan only)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved in Japan as Pralmorelin for GH testing", "notes_de": "In Japan als Pralmorelin für GH-Tests zugelassen"},
        "manufacturer": "Kaken Pharmaceutical",
        "molecular_weight": "817 Da", "amino_acid_count": "6", "half_life": "25-30 minutes",
        "storage_conditions": {"en": "Store at -20°C lyophilized", "de": "Lyophilisiert bei -20°C lagern"},
        "amino_acid_sequence": "D-Ala-D-2Nal-Ala-Trp-D-Phe-Lys-NH2",
        "reconstitution_info": {"preparation_en": "Reconstitute with bacteriostatic water", "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "21 days", "light_sensitive": True, "solvent": "Bacteriostatic water"},
        "application_goals": [{"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Hexarelin",
        "slug": "hexarelin",
        "category": "Growth Hormone Releasing Peptide",
        "description": {
            "en": "Hexarelin is a synthetic hexapeptide growth hormone secretagogue that acts on the ghrelin receptor. It is considered the most potent GHRP for acute GH release but shows more desensitization with chronic use than other GHRPs. Hexarelin also has notable cardioprotective effects independent of GH release.",
            "de": "Hexarelin ist ein synthetisches Hexapeptid-Wachstumshormon-Sekretagogum, das am Ghrelin-Rezeptor wirkt. Es gilt als das potenteste GHRP für akute GH-Freisetzung, zeigt aber bei chronischer Anwendung mehr Desensibilisierung als andere GHRPs. Hexarelin hat auch bemerkenswerte kardioprotektive Effekte."
        },
        "mechanism_of_action": {"en": "Activates GHS-R1a and CD36 receptors. The GHS-R1a activation stimulates GH release while CD36 binding mediates cardioprotective effects including improved cardiac contractility and coronary vasodilation.", "de": "Aktiviert GHS-R1a- und CD36-Rezeptoren. Die GHS-R1a-Aktivierung stimuliert die GH-Freisetzung, während die CD36-Bindung kardioprotektive Effekte vermittelt."},
        "indications": [
            {"condition_en": "GH deficiency research", "condition_de": "GH-Mangel-Forschung", "description_en": "Investigational for GH stimulation", "description_de": "Experimentell zur GH-Stimulation"},
            {"condition_en": "Cardiac protection", "condition_de": "Herzschutz", "description_en": "Research for cardioprotective applications", "description_de": "Forschung für kardioprotektive Anwendungen"},
            {"condition_en": "Heart failure", "condition_de": "Herzinsuffizienz", "description_en": "Early research for cardiac function improvement", "description_de": "Frühe Forschung zur Verbesserung der Herzfunktion"}
        ],
        "benefits": [{"benefit_en": "Strongest acute GH release among GHRPs", "benefit_de": "Stärkste akute GH-Freisetzung unter den GHRPs"}, {"benefit_en": "Significant cardioprotective effects", "benefit_de": "Signifikante kardioprotektive Effekte"}, {"benefit_en": "Anti-fibrotic properties in heart tissue", "benefit_de": "Anti-fibrotische Eigenschaften im Herzgewebe"}, {"benefit_en": "Minimal appetite stimulation", "benefit_de": "Minimale Appetitstimulation"}],
        "side_effects": [
            {"name_en": "Cortisol increase", "name_de": "Kortisolanstieg", "severity": "mild", "frequency": "common", "description_en": "Higher cortisol response than other GHRPs", "description_de": "Höhere Kortisolreaktion als andere GHRPs"},
            {"name_en": "Prolactin elevation", "name_de": "Prolaktinerhöhung", "severity": "mild", "frequency": "common", "description_en": "More pronounced than GHRP-2", "description_de": "Ausgeprägter als bei GHRP-2"},
            {"name_en": "Desensitization", "name_de": "Desensibilisierung", "severity": "moderate", "frequency": "common", "description_en": "GH response diminishes with chronic use", "description_de": "GH-Reaktion nimmt bei chronischer Anwendung ab"},
            {"name_en": "Flushing", "name_de": "Hautrötung", "severity": "mild", "frequency": "uncommon", "description_en": "Temporary facial flushing", "description_de": "Vorübergehende Gesichtsrötung"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "uncommon", "description_en": "Transient", "description_de": "Vorübergehend"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "200 mcg", "frequency_en": "1-2 times daily", "frequency_de": "1-2 mal täglich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Cycling recommended due to desensitization", "notes_de": "Zyklen empfohlen aufgrund von Desensibilisierung"},
        "contraindications": [{"en": "Active malignancy", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "Pituitary tumors", "de": "Hypophysentumoren"}],
        "drug_interactions": ["Growth hormone", "Insulin", "Cortisone"],
        "research_status": {"phase": "Phase II", "fda_approved": False, "ema_approved": False, "notes_en": "Research compound, cardiac studies ongoing", "notes_de": "Forschungssubstanz, Herzstudien laufen"},
        "manufacturer": "Research compound",
        "molecular_weight": "887 Da", "amino_acid_count": "6", "half_life": "70 minutes",
        "storage_conditions": {"en": "Store lyophilized at -20°C", "de": "Lyophilisiert bei -20°C lagern"},
        "amino_acid_sequence": "His-D-2MeTrp-Ala-Trp-D-Phe-Lys-NH2",
        "reconstitution_info": {"preparation_en": "Reconstitute with bacteriostatic water", "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "14 days", "light_sensitive": True, "solvent": "Bacteriostatic water"},
        "application_goals": [{"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "MK-677 (Ibutamoren)",
        "slug": "mk-677",
        "category": "Growth Hormone Secretagogue",
        "description": {
            "en": "MK-677 (Ibutamoren) is an orally active, non-peptide growth hormone secretagogue that mimics ghrelin's action at the GHS-R1a receptor. Unlike injectable GHRPs, it can be taken orally and has a long half-life allowing once-daily dosing. MK-677 increases GH and IGF-1 levels without significantly affecting cortisol. It has been extensively studied for age-related muscle wasting, osteoporosis, and GH deficiency.",
            "de": "MK-677 (Ibutamoren) ist ein oral wirksamer, nicht-peptidischer Wachstumshormon-Sekretagogum, das die Wirkung von Ghrelin am GHS-R1a-Rezeptor nachahmt. Im Gegensatz zu injizierbaren GHRPs kann es oral eingenommen werden und hat eine lange Halbwertszeit. MK-677 erhöht GH- und IGF-1-Spiegel ohne Cortisol signifikant zu beeinflussen."
        },
        "mechanism_of_action": {"en": "Non-peptide ghrelin mimetic that activates GHS-R1a receptors, stimulating pulsatile GH release from the pituitary. Increases both GH and IGF-1 levels to youthful ranges. Does not suppress the hypothalamic-pituitary-adrenal axis.", "de": "Nicht-peptidisches Ghrelin-Mimetikum, das GHS-R1a-Rezeptoren aktiviert und pulsatile GH-Freisetzung stimuliert. Erhöht sowohl GH- als auch IGF-1-Spiegel auf jugendliche Werte."},
        "indications": [
            {"condition_en": "Growth hormone deficiency", "condition_de": "Wachstumshormonmangel", "description_en": "Oral alternative to GH injections", "description_de": "Orale Alternative zu GH-Injektionen"},
            {"condition_en": "Sarcopenia", "condition_de": "Sarkopenie", "description_en": "Age-related muscle loss prevention", "description_de": "Prävention altersbedingten Muskelverlustes"},
            {"condition_en": "Osteoporosis", "condition_de": "Osteoporose", "description_en": "Bone density improvement in elderly", "description_de": "Verbesserung der Knochendichte bei Älteren"}
        ],
        "benefits": [{"benefit_en": "Oral administration (no injection needed)", "benefit_de": "Orale Verabreichung (keine Injektion nötig)"}, {"benefit_en": "Sustained IGF-1 elevation", "benefit_de": "Anhaltende IGF-1-Erhöhung"}, {"benefit_en": "Improved sleep quality", "benefit_de": "Verbesserte Schlafqualität"}, {"benefit_en": "Increased bone mineral density", "benefit_de": "Erhöhte Knochenmineraldichte"}, {"benefit_en": "Preserved muscle mass in caloric deficit", "benefit_de": "Erhaltene Muskelmasse im Kaloriendefizit"}],
        "side_effects": [
            {"name_en": "Increased appetite", "name_de": "Gesteigerter Appetit", "severity": "mild", "frequency": "common", "description_en": "Strong hunger increase", "description_de": "Starke Hungersteigerung"},
            {"name_en": "Water retention", "name_de": "Wassereinlagerungen", "severity": "mild", "frequency": "common", "description_en": "Edema, especially initially", "description_de": "Ödeme, besonders anfänglich"},
            {"name_en": "Elevated blood glucose", "name_de": "Erhöhter Blutzucker", "severity": "moderate", "frequency": "common", "description_en": "Insulin resistance with prolonged use", "description_de": "Insulinresistenz bei Langzeitanwendung"},
            {"name_en": "Numbness/tingling", "name_de": "Taubheit/Kribbeln", "severity": "mild", "frequency": "uncommon", "description_en": "Carpal tunnel-like symptoms", "description_de": "Karpaltunnel-ähnliche Symptome"},
            {"name_en": "Lethargy", "name_de": "Lethargie", "severity": "mild", "frequency": "common", "description_en": "Sleepiness, especially initially", "description_de": "Schläfrigkeit, besonders anfangs"}
        ],
        "dosage": {"starting_dose": "10 mg", "maintenance_dose": "25 mg", "frequency_en": "Once daily (oral)", "frequency_de": "Einmal täglich (oral)", "route_en": "Oral", "route_de": "Oral", "notes_en": "Take before bedtime to minimize appetite effects", "notes_de": "Vor dem Schlafengehen einnehmen"},
        "contraindications": [{"en": "Active cancer or history of cancer", "de": "Aktive oder vorherige Krebserkrankung"}, {"en": "Diabetes mellitus (relative)", "de": "Diabetes mellitus (relativ)"}, {"en": "Pregnancy/breastfeeding", "de": "Schwangerschaft/Stillzeit"}],
        "drug_interactions": ["Insulin/oral hypoglycemics", "Growth hormone", "Corticosteroids"],
        "research_status": {"phase": "Phase II", "fda_approved": False, "ema_approved": False, "notes_en": "Extensively studied but not FDA approved. Multiple Phase II trials completed.", "notes_de": "Umfassend untersucht aber nicht FDA-zugelassen. Mehrere Phase-II-Studien abgeschlossen."},
        "manufacturer": "Merck (original developer)",
        "molecular_weight": "528 Da", "amino_acid_count": "Non-peptide", "half_life": "24 hours",
        "storage_conditions": {"en": "Store at room temperature, protect from moisture", "de": "Bei Raumtemperatur lagern, vor Feuchtigkeit schützen"},
        "amino_acid_sequence": "Non-peptide small molecule (C27H36N4O5S)",
        "reconstitution_info": {"preparation_en": "Oral capsule, no reconstitution needed", "preparation_de": "Orale Kapsel, keine Rekonstitution nötig", "storage_temperature": "15-25°C", "shelf_life_unopened": "36 months", "shelf_life_reconstituted": "N/A", "light_sensitive": False, "solvent": "N/A"},
        "application_goals": [{"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Tesamorelin",
        "slug": "tesamorelin",
        "category": "Growth Hormone Releasing Hormone Analog",
        "description": {
            "en": "Tesamorelin (Egrifta) is a synthetic analog of growth hormone-releasing hormone (GHRH) approved by the FDA for the reduction of excess abdominal fat in HIV-infected patients with lipodystrophy. It is the only GHRH analog approved for clinical use in the US and stimulates natural, pulsatile GH secretion.",
            "de": "Tesamorelin (Egrifta) ist ein synthetisches Analogon des Wachstumshormon-Releasing-Hormons (GHRH), das von der FDA zur Reduktion von überschüssigem Bauchfett bei HIV-infizierten Patienten mit Lipodystrophie zugelassen ist. Es stimuliert die natürliche, pulsatile GH-Sekretion."
        },
        "mechanism_of_action": {"en": "Binds to GHRH receptors on pituitary somatotrophs, stimulating synthesis and pulsatile release of endogenous growth hormone. This increases IGF-1 and preferentially reduces visceral adipose tissue.", "de": "Bindet an GHRH-Rezeptoren der Hypophysen-Somatotrophen und stimuliert Synthese und pulsatile Freisetzung von endogenem Wachstumshormon."},
        "indications": [
            {"condition_en": "HIV-associated lipodystrophy", "condition_de": "HIV-assoziierte Lipodystrophie", "description_en": "FDA-approved for visceral fat reduction", "description_de": "FDA-zugelassen zur Reduktion des viszeralen Fetts"},
            {"condition_en": "Visceral adiposity", "condition_de": "Viszerale Adipositas", "description_en": "Research for general visceral fat reduction", "description_de": "Forschung zur allgemeinen viszeralen Fettreduktion"},
            {"condition_en": "Cognitive decline", "condition_de": "Kognitiver Abbau", "description_en": "Emerging research for neuroprotection", "description_de": "Neue Forschung zum Nervenschutz"}
        ],
        "benefits": [{"benefit_en": "FDA-approved with established safety profile", "benefit_de": "FDA-zugelassen mit etabliertem Sicherheitsprofil"}, {"benefit_en": "Significant visceral fat reduction", "benefit_de": "Signifikante Reduktion des viszeralen Fetts"}, {"benefit_en": "Natural pulsatile GH release", "benefit_de": "Natürliche pulsatile GH-Freisetzung"}, {"benefit_en": "Improved body composition", "benefit_de": "Verbesserte Körperzusammensetzung"}],
        "side_effects": [
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Erythema, pruritus, pain", "description_de": "Erythem, Juckreiz, Schmerz"},
            {"name_en": "Arthralgia", "name_de": "Gelenkschmerzen", "severity": "mild", "frequency": "common", "description_en": "Joint pain", "description_de": "Gelenkschmerzen"},
            {"name_en": "Peripheral edema", "name_de": "Periphere Ödeme", "severity": "mild", "frequency": "common", "description_en": "Fluid retention in extremities", "description_de": "Flüssigkeitsretention in den Extremitäten"},
            {"name_en": "Myalgia", "name_de": "Myalgie", "severity": "mild", "frequency": "uncommon", "description_en": "Muscle pain", "description_de": "Muskelschmerzen"},
            {"name_en": "Hyperglycemia", "name_de": "Hyperglykämie", "severity": "moderate", "frequency": "uncommon", "description_en": "Blood glucose elevation", "description_de": "Blutzuckererhöhung"}
        ],
        "dosage": {"starting_dose": "2 mg", "maintenance_dose": "2 mg", "frequency_en": "Once daily", "frequency_de": "Einmal täglich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Inject into abdomen", "notes_de": "In den Bauch injizieren"},
        "contraindications": [{"en": "Active malignancy", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "Disrupted hypothalamic-pituitary axis", "de": "Gestörte Hypothalamus-Hypophysen-Achse"}],
        "drug_interactions": ["Cortisone (may need dose adjustment)", "Insulin", "Antiretroviral drugs"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": False, "notes_en": "FDA approved 2010 (Egrifta) for HIV lipodystrophy", "notes_de": "FDA-Zulassung 2010 (Egrifta) für HIV-Lipodystrophie"},
        "manufacturer": "Theratechnologies",
        "molecular_weight": "5136 Da", "amino_acid_count": "44", "half_life": "26-38 minutes",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "trans-3-hexenoic acid-YADAIFTNSYRKVLGQLSARKLLQDIMSRQQGESNQERGARARL-NH2",
        "reconstitution_info": {"preparation_en": "Reconstitute with provided sterile water diluent", "preparation_de": "Mit mitgeliefertem sterilem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "18 months", "shelf_life_reconstituted": "Use immediately", "light_sensitive": True, "solvent": "Sterile water for injection"},
        "application_goals": [{"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── HEALING / RECOVERY PEPTIDES ──────────────────────────────
    {
        "name": "Pentadecarginine (BPC-157 Arginate)",
        "slug": "bpc-157-arginate",
        "category": "Body Protection Compound",
        "description": {
            "en": "BPC-157 Arginate (Pentadecarginine) is a salt form of BPC-157 with arginine, designed for improved oral bioavailability and stability. While standard BPC-157 is primarily administered by injection, the arginate form allows for effective oral and sublingual dosing. It retains the same healing properties as BPC-157 for tendons, ligaments, gut, and overall tissue repair.",
            "de": "BPC-157 Arginat (Pentadecarginin) ist eine Salzform von BPC-157 mit Arginin, entwickelt für verbesserte orale Bioverfügbarkeit und Stabilität. Das Arginat ermöglicht effektive orale und sublinguale Dosierung und behält die gleichen heilenden Eigenschaften wie BPC-157."
        },
        "mechanism_of_action": {"en": "Promotes angiogenesis, upregulates growth factor expression (VEGF, FGF), modulates NO system, and activates the FAK-paxillin pathway for accelerated tissue repair. The arginine salt improves pH stability for oral absorption.", "de": "Fördert Angiogenese, reguliert Wachstumsfaktor-Expression hoch (VEGF, FGF), moduliert das NO-System und aktiviert den FAK-Paxillin-Signalweg für beschleunigte Gewebereparatur."},
        "indications": [
            {"condition_en": "Tendon/ligament injuries", "condition_de": "Sehnen-/Bandverletzungen", "description_en": "Accelerated healing of connective tissue", "description_de": "Beschleunigte Heilung von Bindegewebe"},
            {"condition_en": "Gastrointestinal conditions", "condition_de": "Gastrointestinale Erkrankungen", "description_en": "Gut lining protection and repair", "description_de": "Schutz und Reparatur der Darmschleimhaut"},
            {"condition_en": "Inflammatory conditions", "condition_de": "Entzündliche Erkrankungen", "description_en": "Systemic anti-inflammatory effects", "description_de": "Systemische anti-entzündliche Wirkung"}
        ],
        "benefits": [{"benefit_en": "Oral bioavailability (no injection required)", "benefit_de": "Orale Bioverfügbarkeit (keine Injektion nötig)"}, {"benefit_en": "Comprehensive tissue healing", "benefit_de": "Umfassende Gewebeheilung"}, {"benefit_en": "Gut-protective properties", "benefit_de": "Darmschützende Eigenschaften"}, {"benefit_en": "Anti-inflammatory effects", "benefit_de": "Anti-entzündliche Wirkung"}],
        "side_effects": [
            {"name_en": "Mild GI discomfort", "name_de": "Leichtes GI-Unbehagen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional stomach upset", "description_de": "Gelegentliche Magenverstimmung"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "rare", "description_en": "Infrequent and mild", "description_de": "Selten und mild"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "rare", "description_en": "Rare occurrence", "description_de": "Seltenes Auftreten"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "rare", "description_en": "Minimal with oral form", "description_de": "Minimal bei oraler Form"},
            {"name_en": "Unknown long-term effects", "name_de": "Unbekannte Langzeiteffekte", "severity": "moderate", "frequency": "rare", "description_en": "Limited human clinical data", "description_de": "Begrenzte klinische Humandaten"}
        ],
        "dosage": {"starting_dose": "250 mcg", "maintenance_dose": "500 mcg", "frequency_en": "1-2 times daily", "frequency_de": "1-2 mal täglich", "route_en": "Oral or sublingual", "route_de": "Oral oder sublingual", "notes_en": "Take on empty stomach for best absorption", "notes_de": "Nüchtern einnehmen für beste Absorption"},
        "contraindications": [{"en": "Active cancer (theoretical)", "de": "Aktive Krebserkrankung (theoretisch)"}, {"en": "Pregnancy/breastfeeding", "de": "Schwangerschaft/Stillzeit"}, {"en": "Concurrent use of blood thinners (caution)", "de": "Gleichzeitige Anwendung von Blutverdünnern (Vorsicht)"}],
        "drug_interactions": ["Anticoagulants", "NSAIDs (potential interaction)", "Growth factors"],
        "research_status": {"phase": "Pre-clinical/Phase I", "fda_approved": False, "ema_approved": False, "notes_en": "Research compound with extensive animal data", "notes_de": "Forschungssubstanz mit umfangreichen Tierdaten"},
        "manufacturer": "Research compound",
        "molecular_weight": "1419 Da", "amino_acid_count": "15", "half_life": "Stable in gastric juice",
        "storage_conditions": {"en": "Store at room temperature, protect from light", "de": "Bei Raumtemperatur lagern, vor Licht schützen"},
        "amino_acid_sequence": "Gly-Glu-Pro-Pro-Pro-Gly-Lys-Pro-Ala-Asp-Asp-Ala-Gly-Leu-Val (arginine salt)",
        "reconstitution_info": {"preparation_en": "Capsule or sublingual tablet, no reconstitution needed", "preparation_de": "Kapsel oder Sublingualtablette, keine Rekonstitution nötig", "storage_temperature": "15-25°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "N/A", "light_sensitive": True, "solvent": "N/A (oral form)"},
        "application_goals": [{"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"}, {"goal_en": "Immune", "goal_de": "Immunsystem", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Thymosin Beta-4",
        "slug": "thymosin-beta-4",
        "category": "Thymic Peptide",
        "description": {
            "en": "Thymosin Beta-4 (TB-4) is the full-length 43-amino acid peptide from which TB-500 (the active fragment) is derived. It is the most abundant member of the beta-thymosin family and is found in virtually all human cells. Thymosin Beta-4 plays critical roles in wound healing, tissue repair, and inflammation regulation through its effects on actin polymerization and cell migration.",
            "de": "Thymosin Beta-4 (TB-4) ist das vollständige 43-Aminosäure-Peptid, von dem TB-500 (das aktive Fragment) abgeleitet ist. Es ist das häufigste Mitglied der Beta-Thymosin-Familie und kommt in praktisch allen menschlichen Zellen vor. Es spielt eine kritische Rolle bei Wundheilung und Gewebereparatur."
        },
        "mechanism_of_action": {"en": "Sequesters G-actin monomers to regulate actin polymerization and cytoskeletal dynamics. Promotes cell migration, angiogenesis, and stem cell differentiation. Reduces inflammation through NF-kB modulation.", "de": "Bindet G-Aktin-Monomere zur Regulation der Aktin-Polymerisation und Zytoskelett-Dynamik. Fördert Zellmigration, Angiogenese und Stammzelldifferenzierung."},
        "indications": [
            {"condition_en": "Wound healing", "condition_de": "Wundheilung", "description_en": "Accelerated dermal and corneal wound repair", "description_de": "Beschleunigte dermale und korneale Wundheilung"},
            {"condition_en": "Corneal injury", "condition_de": "Hornhautverletzung", "description_en": "Ophthalmic applications for corneal repair", "description_de": "Ophthalmologische Anwendungen zur Hornhautreparatur"},
            {"condition_en": "Cardiac repair post-MI", "condition_de": "Herzreparatur nach Infarkt", "description_en": "Research for myocardial regeneration", "description_de": "Forschung zur Myokardregeneration"}
        ],
        "benefits": [{"benefit_en": "Comprehensive wound healing acceleration", "benefit_de": "Umfassende Beschleunigung der Wundheilung"}, {"benefit_en": "Anti-inflammatory properties", "benefit_de": "Anti-entzündliche Eigenschaften"}, {"benefit_en": "Corneal healing (ophthalmic use)", "benefit_de": "Hornhautheilung (ophthalmische Anwendung)"}, {"benefit_en": "Cardiac tissue protection", "benefit_de": "Herzgewebeschutz"}],
        "side_effects": [
            {"name_en": "Injection site discomfort", "name_de": "Unbehagen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local pain and redness", "description_de": "Lokaler Schmerz und Rötung"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional", "description_de": "Gelegentlich"},
            {"name_en": "Fatigue", "name_de": "Müdigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Transient", "description_de": "Vorübergehend"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "rare", "description_en": "Infrequent", "description_de": "Selten"},
            {"name_en": "Theoretical cancer concern", "name_de": "Theoretische Krebsbedenken", "severity": "moderate", "frequency": "rare", "description_en": "Elevated in some tumors (causal role debated)", "description_de": "In einigen Tumoren erhöht (kausale Rolle umstritten)"}
        ],
        "dosage": {"starting_dose": "750 mcg", "maintenance_dose": "750 mcg - 2 mg", "frequency_en": "2-3 times weekly", "frequency_de": "2-3 mal wöchentlich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Often combined with BPC-157 for synergistic healing", "notes_de": "Oft mit BPC-157 kombiniert für synergistische Heilung"},
        "contraindications": [{"en": "Active cancer", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "History of melanoma", "de": "Vorgeschichte eines Melanoms"}],
        "drug_interactions": ["Anticoagulants", "Chemotherapy agents", "Immunosuppressants"],
        "research_status": {"phase": "Phase II/III", "fda_approved": False, "ema_approved": False, "notes_en": "RegeneRx developing RGN-259 eye drops (Phase III)", "notes_de": "RegeneRx entwickelt RGN-259 Augentropfen (Phase III)"},
        "manufacturer": "RegeneRx Biopharmaceuticals",
        "molecular_weight": "4963 Da", "amino_acid_count": "43", "half_life": "2 hours",
        "storage_conditions": {"en": "Store lyophilized at -20°C", "de": "Lyophilisiert bei -20°C lagern"},
        "amino_acid_sequence": "SDKPDMAEIEKFDKSKLKKTETQEKNPLPSKETIEQEKQAGES",
        "reconstitution_info": {"preparation_en": "Reconstitute with bacteriostatic water", "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "28 days", "light_sensitive": True, "solvent": "Bacteriostatic water"},
        "application_goals": [{"goal_en": "Healing", "goal_de": "Heilung", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── COSMETIC / SKIN PEPTIDES ─────────────────────────────────
    {
        "name": "Palmitoyl Pentapeptide-4 (Matrixyl)",
        "slug": "matrixyl",
        "category": "Cosmetic Peptide",
        "description": {
            "en": "Matrixyl (Palmitoyl Pentapeptide-4) is a lipopeptide used extensively in anti-aging skincare. It is a fragment of collagen type I precursor that signals fibroblasts to produce more collagen, fibronectin, and hyaluronic acid. Clinical studies have shown it can reduce wrinkle depth by up to 68% in 2 months. It is one of the most validated anti-aging peptides in cosmetics.",
            "de": "Matrixyl (Palmitoyl Pentapeptid-4) ist ein Lipopeptid, das weitverbreitet in Anti-Aging-Hautpflege verwendet wird. Es ist ein Fragment des Kollagen-Typ-I-Vorläufers, das Fibroblasten signalisiert, mehr Kollagen, Fibronektin und Hyaluronsäure zu produzieren. Klinische Studien zeigen eine Faltenreduktion von bis zu 68%."
        },
        "mechanism_of_action": {"en": "Mimics a collagen fragment that signals fibroblasts through the TGF-beta pathway to increase production of collagens I, III, and IV, as well as fibronectin and glycosaminoglycans. Acts as a matrikine signal peptide.", "de": "Ahmt ein Kollagenfragment nach, das Fibroblasten über den TGF-beta-Signalweg signalisiert, die Produktion von Kollagen I, III und IV sowie Fibronektin und Glykosaminoglykanen zu erhöhen."},
        "indications": [
            {"condition_en": "Skin aging", "condition_de": "Hautalterung", "description_en": "Wrinkle reduction and prevention", "description_de": "Faltenreduktion und -prävention"},
            {"condition_en": "Photo-damage", "condition_de": "Lichtschäden", "description_en": "UV-induced collagen degradation", "description_de": "UV-induzierter Kollagenabbau"},
            {"condition_en": "Skin elasticity loss", "condition_de": "Elastizitätsverlust der Haut", "description_en": "Improvement of skin firmness", "description_de": "Verbesserung der Hautfestigkeit"}
        ],
        "benefits": [{"benefit_en": "Up to 68% wrinkle depth reduction", "benefit_de": "Bis zu 68% Faltenreduktion"}, {"benefit_en": "Stimulates natural collagen production", "benefit_de": "Stimuliert natürliche Kollagenproduktion"}, {"benefit_en": "Well-tolerated topical application", "benefit_de": "Gut verträgliche topische Anwendung"}, {"benefit_en": "Extensive clinical validation", "benefit_de": "Umfangreiche klinische Validierung"}],
        "side_effects": [
            {"name_en": "Mild skin irritation", "name_de": "Leichte Hautreizung", "severity": "mild", "frequency": "rare", "description_en": "Very rare with topical use", "description_de": "Sehr selten bei topischer Anwendung"},
            {"name_en": "Contact dermatitis", "name_de": "Kontaktdermatitis", "severity": "mild", "frequency": "rare", "description_en": "In sensitive individuals", "description_de": "Bei empfindlichen Personen"},
            {"name_en": "Redness", "name_de": "Rötung", "severity": "mild", "frequency": "rare", "description_en": "Transient erythema", "description_de": "Vorübergehendes Erythem"},
            {"name_en": "No systemic effects", "name_de": "Keine systemischen Wirkungen", "severity": "mild", "frequency": "rare", "description_en": "Topical peptide with minimal absorption", "description_de": "Topisches Peptid mit minimaler Absorption"},
            {"name_en": "Photosensitivity (theoretical)", "name_de": "Lichtempfindlichkeit (theoretisch)", "severity": "mild", "frequency": "rare", "description_en": "Use with sunscreen recommended", "description_de": "Anwendung mit Sonnenschutz empfohlen"}
        ],
        "dosage": {"starting_dose": "Products with 2-8% concentration", "maintenance_dose": "Daily application", "frequency_en": "1-2 times daily", "frequency_de": "1-2 mal täglich", "route_en": "Topical (cream/serum)", "route_de": "Topisch (Creme/Serum)", "notes_en": "Apply to clean skin before moisturizer", "notes_de": "Auf saubere Haut vor Feuchtigkeitscreme auftragen"},
        "contraindications": [{"en": "Known allergy to peptide components", "de": "Bekannte Allergie gegen Peptidkomponenten"}, {"en": "Open wounds (avoid direct application)", "de": "Offene Wunden (direkte Anwendung vermeiden)"}, {"en": "None significant for topical use", "de": "Keine signifikanten bei topischer Anwendung"}],
        "drug_interactions": ["Retinoids (use at different times of day)", "AHAs/BHAs (layer carefully)", "Vitamin C serums (compatible)"],
        "research_status": {"phase": "Marketed", "fda_approved": False, "ema_approved": False, "notes_en": "Widely used in cosmetics, GRAS status for topical use", "notes_de": "Weit verbreitet in Kosmetik, GRAS-Status für topische Anwendung"},
        "manufacturer": "Sederma (Croda International)",
        "molecular_weight": "802 Da", "amino_acid_count": "5", "half_life": "Topical (local action)",
        "storage_conditions": {"en": "Store at room temperature, protect from heat", "de": "Bei Raumtemperatur lagern, vor Hitze schützen"},
        "amino_acid_sequence": "Pal-KTTKS",
        "reconstitution_info": {"preparation_en": "Ready-to-use in cosmetic formulations", "preparation_de": "Gebrauchsfertig in kosmetischen Formulierungen", "storage_temperature": "15-25°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "N/A", "light_sensitive": False, "solvent": "N/A (topical)"},
        "application_goals": [{"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Copper Peptide AHK-Cu",
        "slug": "ahk-cu",
        "category": "Cosmetic Peptide",
        "description": {
            "en": "AHK-Cu (Alanine-Histidine-Lysine-Copper) is a tripeptide-copper complex that stimulates hair growth and skin rejuvenation. Related to GHK-Cu but with distinct properties, AHK-Cu has shown potent hair follicle stimulation capabilities, particularly for androgenetic alopecia. It promotes dermal papilla cell proliferation and increases expression of growth factors important for hair cycling.",
            "de": "AHK-Cu (Alanin-Histidin-Lysin-Kupfer) ist ein Tripeptid-Kupfer-Komplex, der Haarwachstum und Hautverjüngung stimuliert. Verwandt mit GHK-Cu, hat AHK-Cu ausgeprägte Fähigkeiten zur Haarfollikelstimulation, besonders bei androgenetischer Alopezie."
        },
        "mechanism_of_action": {"en": "Stimulates dermal papilla cells and VEGF expression to promote hair follicle cycling. The copper ion facilitates enzymatic processes essential for collagen cross-linking and antioxidant defense. Upregulates Wnt/beta-catenin signaling in hair follicles.", "de": "Stimuliert Dermalpapillenzellen und VEGF-Expression zur Förderung des Haarfollikelzyklus. Das Kupfer-Ion ermöglicht enzymatische Prozesse für Kollagen-Vernetzung und Antioxidantienschutz."},
        "indications": [
            {"condition_en": "Androgenetic alopecia", "condition_de": "Androgenetische Alopezie", "description_en": "Hair loss treatment", "description_de": "Haarausfallbehandlung"},
            {"condition_en": "Skin aging", "condition_de": "Hautalterung", "description_en": "Anti-aging and skin rejuvenation", "description_de": "Anti-Aging und Hautverjüngung"},
            {"condition_en": "Wound healing", "condition_de": "Wundheilung", "description_en": "Copper-mediated tissue repair", "description_de": "Kupfervermittelte Gewebereparatur"}
        ],
        "benefits": [{"benefit_en": "Hair growth stimulation", "benefit_de": "Haarwuchsstimulation"}, {"benefit_en": "Collagen synthesis promotion", "benefit_de": "Kollagensynthese-Förderung"}, {"benefit_en": "Antioxidant properties via copper", "benefit_de": "Antioxidative Eigenschaften durch Kupfer"}, {"benefit_en": "Non-hormonal hair loss treatment", "benefit_de": "Nicht-hormonelle Haarausfallbehandlung"}],
        "side_effects": [
            {"name_en": "Scalp irritation", "name_de": "Kopfhautreizung", "severity": "mild", "frequency": "uncommon", "description_en": "Mild irritation with topical use", "description_de": "Leichte Reizung bei topischer Anwendung"},
            {"name_en": "Skin discoloration", "name_de": "Hautverfärbung", "severity": "mild", "frequency": "rare", "description_en": "Blue-green tint from copper at high concentrations", "description_de": "Blau-grüne Tönung durch Kupfer bei hohen Konzentrationen"},
            {"name_en": "Contact allergy", "name_de": "Kontaktallergie", "severity": "mild", "frequency": "rare", "description_en": "In copper-sensitive individuals", "description_de": "Bei kupferempfindlichen Personen"},
            {"name_en": "Dryness", "name_de": "Trockenheit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild skin dryness initially", "description_de": "Anfänglich leichte Hauttrockenheit"},
            {"name_en": "Stinging sensation", "name_de": "Brennen", "severity": "mild", "frequency": "uncommon", "description_en": "Temporary upon application", "description_de": "Vorübergehend bei Anwendung"}
        ],
        "dosage": {"starting_dose": "Topical: 1-5 ppm copper", "maintenance_dose": "Daily topical application", "frequency_en": "1-2 times daily", "frequency_de": "1-2 mal täglich", "route_en": "Topical (scalp/skin)", "route_de": "Topisch (Kopfhaut/Haut)", "notes_en": "Apply to scalp or skin, massage gently", "notes_de": "Auf Kopfhaut oder Haut auftragen, sanft einmassieren"},
        "contraindications": [{"en": "Wilson's disease (copper metabolism disorder)", "de": "Morbus Wilson (Kupferstoffwechselstörung)"}, {"en": "Copper hypersensitivity", "de": "Kupferüberempfindlichkeit"}, {"en": "Open scalp wounds", "de": "Offene Kopfhautwunden"}],
        "drug_interactions": ["Vitamin C (may reduce copper stability)", "Zinc supplements (copper antagonist)", "Minoxidil (can be combined)"],
        "research_status": {"phase": "Marketed (cosmetic)", "fda_approved": False, "ema_approved": False, "notes_en": "Available in cosmetic products, ongoing hair loss research", "notes_de": "In Kosmetikprodukten erhältlich, laufende Haarausfallforschung"},
        "manufacturer": "Various cosmetic manufacturers",
        "molecular_weight": "403 Da", "amino_acid_count": "3", "half_life": "Topical (local action)",
        "storage_conditions": {"en": "Store at room temperature", "de": "Bei Raumtemperatur lagern"},
        "amino_acid_sequence": "Ala-His-Lys-Cu",
        "reconstitution_info": {"preparation_en": "Ready-to-use in topical formulations", "preparation_de": "Gebrauchsfertig in topischen Formulierungen", "storage_temperature": "15-25°C", "shelf_life_unopened": "18 months", "shelf_life_reconstituted": "N/A", "light_sensitive": False, "solvent": "N/A"},
        "application_goals": [{"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── NEUROPEPTIDES / COGNITIVE ─────────────────────────────────
    {
        "name": "Selank",
        "slug": "selank",
        "category": "Neuropeptide",
        "description": {
            "en": "Selank is a synthetic analog of the endogenous immunomodulatory peptide tuftsin, developed at the Institute of Molecular Genetics of the Russian Academy of Sciences. It is approved in Russia as an anxiolytic and nootropic drug. Selank modulates GABA, serotonin, and dopamine systems without sedation or addiction potential, making it unique among anxiolytics.",
            "de": "Selank ist ein synthetisches Analogon des endogenen immunmodulatorischen Peptids Tuftsin, entwickelt am Institut für Molekulargenetik der Russischen Akademie der Wissenschaften. Es ist in Russland als Anxiolytikum und Nootropikum zugelassen. Selank moduliert GABA-, Serotonin- und Dopamin-Systeme ohne Sedierung oder Suchtpotential."
        },
        "mechanism_of_action": {"en": "Enhances GABA-B receptor expression, modulates BDNF and serotonin metabolism, stabilizes enkephalin degradation, and influences IL-6 expression. Acts on multiple neurotransmitter systems simultaneously for anxiolytic and nootropic effects.", "de": "Erhöht GABA-B-Rezeptorexpression, moduliert BDNF und Serotoninmetabolismus, stabilisiert Enkephalin-Abbau und beeinflusst IL-6-Expression."},
        "indications": [
            {"condition_en": "Generalized anxiety disorder", "condition_de": "Generalisierte Angststörung", "description_en": "Anxiolytic without sedation", "description_de": "Anxiolytikum ohne Sedierung"},
            {"condition_en": "Cognitive enhancement", "condition_de": "Kognitive Verbesserung", "description_en": "Nootropic for memory and focus", "description_de": "Nootropikum für Gedächtnis und Fokus"},
            {"condition_en": "Immune modulation", "condition_de": "Immunmodulation", "description_en": "Tuftsin-derived immune support", "description_de": "Tuftsin-basierte Immununterstützung"}
        ],
        "benefits": [{"benefit_en": "Anxiolytic without sedation or dependence", "benefit_de": "Anxiolytikum ohne Sedierung oder Abhängigkeit"}, {"benefit_en": "Improved memory and learning", "benefit_de": "Verbessertes Gedächtnis und Lernen"}, {"benefit_en": "Immune system modulation", "benefit_de": "Immunsystem-Modulation"}, {"benefit_en": "BDNF upregulation", "benefit_de": "BDNF-Hochregulation"}],
        "side_effects": [
            {"name_en": "Fatigue", "name_de": "Müdigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild drowsiness in some users", "description_de": "Leichte Schläfrigkeit bei einigen Anwendern"},
            {"name_en": "Nasal irritation", "name_de": "Nasale Reizung", "severity": "mild", "frequency": "common", "description_en": "With intranasal administration", "description_de": "Bei intranasaler Verabreichung"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional mild headache", "description_de": "Gelegentliche leichte Kopfschmerzen"},
            {"name_en": "Lightheadedness", "name_de": "Benommenheit", "severity": "mild", "frequency": "rare", "description_en": "Transient", "description_de": "Vorübergehend"},
            {"name_en": "Allergic reaction", "name_de": "Allergische Reaktion", "severity": "moderate", "frequency": "rare", "description_en": "In hypersensitive individuals", "description_de": "Bei überempfindlichen Personen"}
        ],
        "dosage": {"starting_dose": "250 mcg", "maintenance_dose": "250-750 mcg", "frequency_en": "1-3 times daily", "frequency_de": "1-3 mal täglich", "route_en": "Intranasal spray or subcutaneous", "route_de": "Intranasales Spray oder subkutan", "notes_en": "Nasal spray is the standard delivery method in Russia", "notes_de": "Nasenspray ist die Standardverabreichung in Russland"},
        "contraindications": [{"en": "Pregnancy/breastfeeding", "de": "Schwangerschaft/Stillzeit"}, {"en": "Severe liver disease", "de": "Schwere Lebererkrankung"}, {"en": "Known peptide hypersensitivity", "de": "Bekannte Peptidüberempfindlichkeit"}],
        "drug_interactions": ["Benzodiazepines (potential synergy)", "SSRIs", "Immunosuppressants"],
        "research_status": {"phase": "Approved (Russia)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved in Russia since 2009, not approved elsewhere", "notes_de": "Seit 2009 in Russland zugelassen, andernorts nicht"},
        "manufacturer": "Institute of Molecular Genetics (Russia)",
        "molecular_weight": "751 Da", "amino_acid_count": "7", "half_life": "Several minutes (active metabolites longer)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "Thr-Lys-Pro-Arg-Pro-Gly-Pro",
        "reconstitution_info": {"preparation_en": "Available as nasal spray or lyophilized powder", "preparation_de": "Erhältlich als Nasenspray oder lyophilisiertes Pulver", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "30 days", "light_sensitive": True, "solvent": "Bacteriostatic water (for injection form)"},
        "application_goals": [{"goal_en": "Cognitive", "goal_de": "Kognitiv", "relevance": "primary"}, {"goal_en": "Immune", "goal_de": "Immunsystem", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Semax",
        "slug": "semax",
        "category": "Neuropeptide",
        "description": {
            "en": "Semax is a synthetic analog of ACTH(4-10) (the fragment of adrenocorticotropic hormone) developed in Russia. It is approved as a nootropic and neuroprotective drug. Unlike ACTH itself, Semax does not affect the adrenal cortex or cortisol levels. It enhances BDNF, NGF, and TrkB expression, making it one of the most potent nootropic peptides studied.",
            "de": "Semax ist ein synthetisches Analogon von ACTH(4-10), entwickelt in Russland. Es ist als Nootropikum und Neuroprotektivum zugelassen. Anders als ACTH selbst beeinflusst Semax nicht die Nebennierenrinde oder Cortisolspiegel. Es steigert BDNF-, NGF- und TrkB-Expression."
        },
        "mechanism_of_action": {"en": "Melanocortin system modulation via MC3/MC4 receptors. Dramatically increases BDNF and TrkB expression (up to 8-fold in hippocampus). Enhances neurotransmitter systems including dopamine, serotonin, and acetylcholine. Neuroprotective via anti-inflammatory and antioxidant mechanisms.", "de": "Melanocortin-System-Modulation über MC3/MC4-Rezeptoren. Steigert BDNF und TrkB-Expression dramatisch (bis zu 8-fach im Hippocampus). Neuroprotektiv durch anti-entzündliche und antioxidative Mechanismen."},
        "indications": [
            {"condition_en": "Cognitive enhancement", "condition_de": "Kognitive Verbesserung", "description_en": "Memory, attention, and learning improvement", "description_de": "Verbesserung von Gedächtnis, Aufmerksamkeit und Lernen"},
            {"condition_en": "Stroke recovery", "condition_de": "Schlaganfall-Rehabilitation", "description_en": "Neuroprotection and neurorecovery", "description_de": "Neuroprotektion und Neurorehabilitation"},
            {"condition_en": "ADHD", "condition_de": "ADHS", "description_en": "Attention and focus improvement", "description_de": "Verbesserung von Aufmerksamkeit und Fokus"}
        ],
        "benefits": [{"benefit_en": "Dramatic BDNF increase (up to 8x)", "benefit_de": "Dramatische BDNF-Steigerung (bis zu 8x)"}, {"benefit_en": "Enhanced memory and learning", "benefit_de": "Verbessertes Gedächtnis und Lernen"}, {"benefit_en": "No cortisol or adrenal effects", "benefit_de": "Keine Cortisol- oder Nebennierenwirkungen"}, {"benefit_en": "Neuroprotective against oxidative stress", "benefit_de": "Neuroprotektiv gegen oxidativen Stress"}],
        "side_effects": [
            {"name_en": "Nasal irritation", "name_de": "Nasale Reizung", "severity": "mild", "frequency": "common", "description_en": "With nasal spray delivery", "description_de": "Bei Nasenspray-Verabreichung"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Usually mild and transient", "description_de": "Meist mild und vorübergehend"},
            {"name_en": "Dizziness", "name_de": "Schwindel", "severity": "mild", "frequency": "rare", "description_en": "Infrequent", "description_de": "Selten"},
            {"name_en": "Hair loss (high doses)", "name_de": "Haarausfall (hohe Dosen)", "severity": "moderate", "frequency": "rare", "description_en": "Reported with extended high-dose use", "description_de": "Bei langfristiger Hochdosis-Anwendung berichtet"},
            {"name_en": "Insomnia", "name_de": "Schlaflosigkeit", "severity": "mild", "frequency": "uncommon", "description_en": "If taken too late in the day", "description_de": "Bei zu später Einnahme"}
        ],
        "dosage": {"starting_dose": "200 mcg", "maintenance_dose": "600-900 mcg", "frequency_en": "2-3 times daily", "frequency_de": "2-3 mal täglich", "route_en": "Intranasal", "route_de": "Intranasal", "notes_en": "Morning/afternoon dosing recommended, avoid evening", "notes_de": "Morgen-/Nachmittagsdosierung empfohlen, Abend vermeiden"},
        "contraindications": [{"en": "Acute psychosis", "de": "Akute Psychose"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "History of seizures (caution)", "de": "Krampfanfälle in der Vorgeschichte (Vorsicht)"}],
        "drug_interactions": ["Stimulants (synergistic)", "MAO inhibitors", "Antidepressants"],
        "research_status": {"phase": "Approved (Russia/Ukraine)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved in Russia since 2011, listed in Russian pharmacopoeia", "notes_de": "Seit 2011 in Russland zugelassen, im russischen Arzneibuch gelistet"},
        "manufacturer": "Institute of Molecular Genetics (Russia)",
        "molecular_weight": "813 Da", "amino_acid_count": "7", "half_life": "Several minutes (effects last hours)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "Met-Glu-His-Phe-Pro-Gly-Pro",
        "reconstitution_info": {"preparation_en": "Nasal spray solution (0.1%)", "preparation_de": "Nasenspraylösung (0,1%)", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "30 days once opened", "light_sensitive": True, "solvent": "Preserved saline"},
        "application_goals": [{"goal_en": "Cognitive", "goal_de": "Kognitiv", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Dihexa",
        "slug": "dihexa",
        "category": "Neuropeptide",
        "description": {
            "en": "Dihexa (N-hexanoic-Tyr-Ile-(6)-aminohexanoic amide) is a synthetic peptide derivative of angiotensin IV with extraordinary nootropic potential. In animal studies, it was found to be approximately 10 million times more potent than BDNF at promoting new synapse formation. Dihexa acts through the hepatocyte growth factor (HGF)/c-Met receptor system to promote neuronal connectivity.",
            "de": "Dihexa ist ein synthetisches Peptidderivat von Angiotensin IV mit außerordentlichem nootropischem Potential. In Tierstudien war es etwa 10 Millionen Mal potenter als BDNF bei der Förderung neuer Synapsenbildung. Dihexa wirkt über das HGF/c-Met-Rezeptorsystem zur Förderung neuronaler Konnektivität."
        },
        "mechanism_of_action": {"en": "Potentiates HGF/c-Met receptor signaling, which promotes synaptogenesis, neuronal survival, and dendritic spine formation. Acts as an allosteric modulator of the HGF/c-Met system rather than a direct agonist, explaining its extraordinary potency.", "de": "Potenziert HGF/c-Met-Rezeptorsignalgebung, die Synaptogenese, neuronales Überleben und dendritische Dornenbildung fördert. Wirkt als allosterischer Modulator."},
        "indications": [
            {"condition_en": "Cognitive decline / dementia research", "condition_de": "Kognitiver Abbau / Demenzforschung", "description_en": "Experimental compound for neurodegeneration", "description_de": "Experimentelle Substanz für Neurodegeneration"},
            {"condition_en": "Alzheimer's disease research", "condition_de": "Alzheimer-Forschung", "description_en": "Synaptogenesis promotion", "description_de": "Förderung der Synaptogenese"},
            {"condition_en": "Traumatic brain injury", "condition_de": "Schädel-Hirn-Trauma", "description_en": "Neuronal repair research", "description_de": "Forschung zur neuronalen Reparatur"}
        ],
        "benefits": [{"benefit_en": "10 million times more potent than BDNF for synaptogenesis", "benefit_de": "10 Millionen Mal potenter als BDNF für Synaptogenese"}, {"benefit_en": "Promotes new neural connections", "benefit_de": "Fördert neue neuronale Verbindungen"}, {"benefit_en": "Orally bioavailable", "benefit_de": "Oral bioverfügbar"}, {"benefit_en": "Crosses blood-brain barrier", "benefit_de": "Überwindet die Blut-Hirn-Schranke"}],
        "side_effects": [
            {"name_en": "Unknown long-term effects", "name_de": "Unbekannte Langzeiteffekte", "severity": "moderate", "frequency": "rare", "description_en": "Very limited human data", "description_de": "Sehr begrenzte Humandaten"},
            {"name_en": "Theoretical cancer risk", "name_de": "Theoretisches Krebsrisiko", "severity": "severe", "frequency": "rare", "description_en": "HGF/c-Met pathway is implicated in some cancers", "description_de": "HGF/c-Met-Signalweg ist bei einigen Krebsarten beteiligt"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Reported anecdotally", "description_de": "Anekdotisch berichtet"},
            {"name_en": "Overstimulation", "name_de": "Überstimulation", "severity": "mild", "frequency": "uncommon", "description_en": "Excessive neural activity", "description_de": "Übermäßige neuronale Aktivität"},
            {"name_en": "Anxiety", "name_de": "Angst", "severity": "mild", "frequency": "uncommon", "description_en": "At higher doses", "description_de": "Bei höheren Dosen"}
        ],
        "dosage": {"starting_dose": "10 mg", "maintenance_dose": "10-20 mg", "frequency_en": "Once daily", "frequency_de": "Einmal täglich", "route_en": "Oral or sublingual", "route_de": "Oral oder sublingual", "notes_en": "Extremely early-stage research compound", "notes_de": "Sehr frühes Forschungsstadium"},
        "contraindications": [{"en": "Any active or history of cancer", "de": "Jede aktive oder vergangene Krebserkrankung"}, {"en": "Pregnancy/breastfeeding", "de": "Schwangerschaft/Stillzeit"}, {"en": "Seizure disorders", "de": "Krampfanfallsleiden"}],
        "drug_interactions": ["Nootropics (potential synergy)", "Chemotherapy drugs", "Anti-angiogenic drugs"],
        "research_status": {"phase": "Pre-clinical", "fda_approved": False, "ema_approved": False, "notes_en": "Animal studies only, no human clinical trials conducted", "notes_de": "Nur Tierstudien, keine klinischen Humanstudien durchgeführt"},
        "manufacturer": "Research compound (Washington State University)",
        "molecular_weight": "507 Da", "amino_acid_count": "Modified dipeptide", "half_life": "Unknown (orally active)",
        "storage_conditions": {"en": "Store at -20°C", "de": "Bei -20°C lagern"},
        "amino_acid_sequence": "N-hexanoic-Tyr-Ile-(6)-aminohexanoic amide",
        "reconstitution_info": {"preparation_en": "Oral capsule or sublingual solution", "preparation_de": "Orale Kapsel oder Sublinguallösung", "storage_temperature": "-20°C", "shelf_life_unopened": "12 months", "shelf_life_reconstituted": "N/A", "light_sensitive": True, "solvent": "N/A"},
        "application_goals": [{"goal_en": "Cognitive", "goal_de": "Kognitiv", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── ANTIMICROBIAL PEPTIDES ────────────────────────────────────
    {
        "name": "Defensin Alpha-1 (HNP-1)",
        "slug": "hnp-1",
        "category": "Antimicrobial Peptide",
        "description": {
            "en": "Human Neutrophil Peptide-1 (HNP-1) is an alpha-defensin, a natural antimicrobial peptide produced by neutrophils. It is a key component of the innate immune system with broad-spectrum activity against bacteria, fungi, and some enveloped viruses. HNP-1 is being researched for its potential as a novel antibiotic and anti-cancer agent.",
            "de": "Human Neutrophil Peptide-1 (HNP-1) ist ein Alpha-Defensin, ein natürliches antimikrobielles Peptid der Neutrophilen. Es ist eine Schlüsselkomponente des angeborenen Immunsystems mit Breitspektrumaktivität gegen Bakterien, Pilze und einige behüllte Viren."
        },
        "mechanism_of_action": {"en": "Forms pores in microbial membranes through electrostatic interaction with anionic lipids, causing cell lysis. Also has immunomodulatory effects, recruiting T-cells and dendritic cells. Shows direct cytotoxic activity against some tumor cells.", "de": "Bildet Poren in mikrobiellen Membranen durch elektrostatische Interaktion mit anionischen Lipiden. Hat auch immunmodulatorische Effekte und zeigt direkte zytotoxische Aktivität gegen einige Tumorzellen."},
        "indications": [
            {"condition_en": "Antibiotic-resistant infections", "condition_de": "Antibiotikaresistente Infektionen", "description_en": "Research for novel antimicrobial therapy", "description_de": "Forschung für neuartige antimikrobielle Therapie"},
            {"condition_en": "Immune deficiency", "condition_de": "Immundefizienz", "description_en": "Innate immune system support", "description_de": "Unterstützung des angeborenen Immunsystems"},
            {"condition_en": "Cancer immunotherapy", "condition_de": "Krebsimmuntherapie", "description_en": "Direct tumor cytotoxicity research", "description_de": "Forschung zur direkten Tumorzytotoxizität"}
        ],
        "benefits": [{"benefit_en": "Broad-spectrum antimicrobial activity", "benefit_de": "Breitspektrum antimikrobielle Aktivität"}, {"benefit_en": "Effective against resistant bacteria", "benefit_de": "Wirksam gegen resistente Bakterien"}, {"benefit_en": "Natural immune component", "benefit_de": "Natürliche Immunkomponente"}, {"benefit_en": "Anti-tumor properties", "benefit_de": "Anti-Tumor-Eigenschaften"}],
        "side_effects": [
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local inflammation", "description_de": "Lokale Entzündung"},
            {"name_en": "Hemolytic potential", "name_de": "Hämolytisches Potential", "severity": "moderate", "frequency": "uncommon", "description_en": "At high concentrations", "description_de": "Bei hohen Konzentrationen"},
            {"name_en": "Nephrotoxicity", "name_de": "Nephrotoxizität", "severity": "moderate", "frequency": "rare", "description_en": "Kidney damage at high systemic doses", "description_de": "Nierenschaden bei hohen systemischen Dosen"},
            {"name_en": "Pro-inflammatory response", "name_de": "Pro-entzündliche Reaktion", "severity": "mild", "frequency": "common", "description_en": "Expected as part of immune activation", "description_de": "Erwartet als Teil der Immunaktivierung"},
            {"name_en": "Fever", "name_de": "Fieber", "severity": "mild", "frequency": "uncommon", "description_en": "Immune activation response", "description_de": "Immunaktivierungsreaktion"}
        ],
        "dosage": {"starting_dose": "Research doses vary", "maintenance_dose": "Experimental", "frequency_en": "Experimental protocols", "frequency_de": "Experimentelle Protokolle", "route_en": "IV or topical (research)", "route_de": "IV oder topisch (Forschung)", "notes_en": "Not approved for therapeutic use", "notes_de": "Nicht für therapeutische Anwendung zugelassen"},
        "contraindications": [{"en": "Autoimmune conditions", "de": "Autoimmunerkrankungen"}, {"en": "Renal impairment", "de": "Nierenfunktionsstörung"}, {"en": "Active hemolytic disorders", "de": "Aktive hämolytische Störungen"}],
        "drug_interactions": ["Immunosuppressants (antagonistic)", "Antibiotics (potential synergy)", "Nephrotoxic drugs"],
        "research_status": {"phase": "Pre-clinical/Phase I", "fda_approved": False, "ema_approved": False, "notes_en": "Extensive research, no approved therapeutic yet", "notes_de": "Umfangreiche Forschung, noch keine zugelassene Therapie"},
        "manufacturer": "Research compound",
        "molecular_weight": "3442 Da", "amino_acid_count": "30", "half_life": "Minutes (serum)",
        "storage_conditions": {"en": "Store at -20°C lyophilized", "de": "Lyophilisiert bei -20°C lagern"},
        "amino_acid_sequence": "ACYCRIPACIAGERRYGTCIYQGRLWAFCC",
        "reconstitution_info": {"preparation_en": "Reconstitute in sterile buffer", "preparation_de": "In sterilem Puffer rekonstituieren", "storage_temperature": "-20°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "7 days", "light_sensitive": False, "solvent": "PBS buffer"},
        "application_goals": [{"goal_en": "Immune", "goal_de": "Immunsystem", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── HORMONAL / REPRODUCTIVE ──────────────────────────────────
    {
        "name": "Gonadorelin",
        "slug": "gonadorelin",
        "category": "Gonadotropin-Releasing Hormone",
        "description": {
            "en": "Gonadorelin is a synthetic form of gonadotropin-releasing hormone (GnRH), the natural decapeptide that controls the reproductive axis. It is used diagnostically to assess pituitary function and therapeutically for hypogonadotropic hypogonadism. Pulsatile administration mimics natural GnRH release and can restore fertility.",
            "de": "Gonadorelin ist eine synthetische Form des Gonadotropin-Releasing-Hormons (GnRH), des natürlichen Dekapeptids, das die Reproduktionsachse steuert. Es wird diagnostisch zur Beurteilung der Hypophysenfunktion und therapeutisch bei hypogonadotropem Hypogonadismus eingesetzt."
        },
        "mechanism_of_action": {"en": "Binds to GnRH receptors on pituitary gonadotropes, stimulating release of LH and FSH. Pulsatile delivery (every 60-120 min) mimics physiological GnRH secretion, while continuous exposure causes receptor desensitization and suppression.", "de": "Bindet an GnRH-Rezeptoren der Hypophysen-Gonadotropen und stimuliert LH- und FSH-Freisetzung. Pulsatile Gabe ahmt physiologische GnRH-Sekretion nach."},
        "indications": [
            {"condition_en": "Hypogonadotropic hypogonadism", "condition_de": "Hypogonadotroper Hypogonadismus", "description_en": "Restoration of gonadal function", "description_de": "Wiederherstellung der Gonadenfunktion"},
            {"condition_en": "Pituitary function testing", "condition_de": "Hypophysenfunktionstest", "description_en": "GnRH stimulation test", "description_de": "GnRH-Stimulationstest"},
            {"condition_en": "Infertility", "condition_de": "Unfruchtbarkeit", "description_en": "Pulsatile therapy for anovulation", "description_de": "Pulsatile Therapie bei Anovulation"}
        ],
        "benefits": [{"benefit_en": "Restores natural hormone axis", "benefit_de": "Stellt natürliche Hormonachse wieder her"}, {"benefit_en": "Diagnostic tool for pituitary assessment", "benefit_de": "Diagnostisches Werkzeug zur Hypophysenbeurteilung"}, {"benefit_en": "Can restore fertility", "benefit_de": "Kann Fruchtbarkeit wiederherstellen"}, {"benefit_en": "Preserves testicular function", "benefit_de": "Erhält die Hodenfunktion"}],
        "side_effects": [
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Frequent occurrence", "description_de": "Häufiges Auftreten"},
            {"name_en": "Flushing", "name_de": "Hautrötung", "severity": "mild", "frequency": "common", "description_en": "Vasomotor symptoms", "description_de": "Vasomotorische Symptome"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "uncommon", "description_en": "Mild GI symptoms", "description_de": "Leichte GI-Symptome"},
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local irritation", "description_de": "Lokale Reizung"},
            {"name_en": "Ovarian hyperstimulation (women)", "name_de": "Ovarielle Überstimulation (Frauen)", "severity": "severe", "frequency": "rare", "description_en": "With excessive stimulation", "description_de": "Bei übermäßiger Stimulation"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "100 mcg pulsatile", "frequency_en": "Every 60-120 minutes (pulsatile) or single diagnostic dose", "frequency_de": "Alle 60-120 Minuten (pulsatil) oder Einzeldiagnostikdosis", "route_en": "IV or subcutaneous", "route_de": "IV oder subkutan", "notes_en": "Pulsatile delivery requires programmable pump", "notes_de": "Pulsatile Gabe erfordert programmierbare Pumpe"},
        "contraindications": [{"en": "Hormone-dependent tumors", "de": "Hormonabhängige Tumoren"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "Pituitary apoplexy", "de": "Hypophysenapoplexie"}],
        "drug_interactions": ["Testosterone (antagonistic with pulsatile)", "Oral contraceptives", "GnRH analogs"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved for diagnostic use (Factrel)", "notes_de": "FDA-zugelassen für diagnostische Anwendung (Factrel)"},
        "manufacturer": "Various",
        "molecular_weight": "1182 Da", "amino_acid_count": "10", "half_life": "2-4 minutes",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "pGlu-His-Trp-Ser-Tyr-Gly-Leu-Arg-Pro-Gly-NH2",
        "reconstitution_info": {"preparation_en": "Reconstitute with provided diluent", "preparation_de": "Mit mitgeliefertem Lösungsmittel rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "1 day", "light_sensitive": True, "solvent": "Sterile water for injection"},
        "application_goals": [{"goal_en": "Hormonal Health", "goal_de": "Hormonelle Gesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Triptorelin",
        "slug": "triptorelin",
        "category": "GnRH Agonist",
        "description": {
            "en": "Triptorelin (Trelstar, Decapeptyl) is a synthetic GnRH agonist decapeptide that is approximately 100 times more potent than natural GnRH. After initial stimulation, chronic administration causes pituitary GnRH receptor downregulation, leading to suppression of LH, FSH, and sex hormones. It is used in prostate cancer, endometriosis, precocious puberty, and fertility treatments.",
            "de": "Triptorelin (Trelstar, Decapeptyl) ist ein synthetischer GnRH-Agonist, etwa 100-mal potenter als natürliches GnRH. Nach anfänglicher Stimulation führt chronische Gabe zur Herunterregulation der GnRH-Rezeptoren und Suppression von LH, FSH und Sexualhormonen."
        },
        "mechanism_of_action": {"en": "Initial agonist effect stimulates gonadotropin release (flare). Continuous exposure causes GnRH receptor downregulation and desensitization, resulting in suppression of the hypothalamic-pituitary-gonadal axis to castrate-level sex hormones.", "de": "Anfänglicher Agonisteneffekt stimuliert Gonadotropin-Freisetzung (Flare). Kontinuierliche Exposition verursacht GnRH-Rezeptor-Herunterregulation und Suppression der HPG-Achse."},
        "indications": [
            {"condition_en": "Advanced prostate cancer", "condition_de": "Fortgeschrittenes Prostatakarzinom", "description_en": "Androgen deprivation therapy", "description_de": "Androgenentzugstherapie"},
            {"condition_en": "Endometriosis", "condition_de": "Endometriose", "description_en": "Symptom management through estrogen suppression", "description_de": "Symptomkontrolle durch Östrogensuppression"},
            {"condition_en": "Central precocious puberty", "condition_de": "Zentrale Pubertas praecox", "description_en": "Puberty suppression in children", "description_de": "Pubertätsunterdrückung bei Kindern"}
        ],
        "benefits": [{"benefit_en": "Effective androgen/estrogen suppression", "benefit_de": "Effektive Androgen-/Östrogensuppression"}, {"benefit_en": "Long-acting depot formulations available", "benefit_de": "Langwirkende Depotformulierungen verfügbar"}, {"benefit_en": "Reversible hormonal suppression", "benefit_de": "Reversible hormonelle Suppression"}, {"benefit_en": "Fertility preservation option with IVF", "benefit_de": "Fertilitätserhaltung bei IVF möglich"}],
        "side_effects": [
            {"name_en": "Hot flashes", "name_de": "Hitzewallungen", "severity": "moderate", "frequency": "common", "description_en": "Due to sex hormone suppression", "description_de": "Durch Sexhormon-Suppression"},
            {"name_en": "Decreased libido", "name_de": "Verminderte Libido", "severity": "moderate", "frequency": "common", "description_en": "Expected with hormone suppression", "description_de": "Erwartet bei Hormonsuppression"},
            {"name_en": "Bone density loss", "name_de": "Knochendichteverlust", "severity": "moderate", "frequency": "common", "description_en": "With prolonged use", "description_de": "Bei Langzeitanwendung"},
            {"name_en": "Initial flare (tumor)", "name_de": "Anfänglicher Flare (Tumor)", "severity": "severe", "frequency": "common", "description_en": "Transient symptom worsening in first 2 weeks", "description_de": "Vorübergehende Symptomverschlechterung in den ersten 2 Wochen"},
            {"name_en": "Mood changes", "name_de": "Stimmungsveränderungen", "severity": "moderate", "frequency": "common", "description_en": "Depression, irritability", "description_de": "Depression, Reizbarkeit"}
        ],
        "dosage": {"starting_dose": "3.75 mg", "maintenance_dose": "3.75 mg monthly or 11.25 mg quarterly", "frequency_en": "Monthly or every 3 months (depot)", "frequency_de": "Monatlich oder alle 3 Monate (Depot)", "route_en": "Intramuscular injection", "route_de": "Intramuskuläre Injektion", "notes_en": "Anti-androgen co-administered in first weeks for prostate cancer", "notes_de": "Anti-Androgen in den ersten Wochen bei Prostatakarzinom mitverabreicht"},
        "contraindications": [{"en": "Pregnancy (teratogenic)", "de": "Schwangerschaft (teratogen)"}, {"en": "Undiagnosed vaginal bleeding", "de": "Nicht abgeklärte Vaginalblutung"}, {"en": "Hypersensitivity to GnRH analogs", "de": "Überempfindlichkeit gegen GnRH-Analoga"}],
        "drug_interactions": ["Drugs affecting pituitary function", "QT-prolonging medications", "Hyperprolactinemic drugs"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "Approved globally for prostate cancer, endometriosis, precocious puberty", "notes_de": "Weltweit zugelassen für Prostatakarzinom, Endometriose, Pubertas praecox"},
        "manufacturer": "Ipsen / Ferring",
        "molecular_weight": "1311 Da", "amino_acid_count": "10", "half_life": "7.6 hours (3-4 weeks effective with depot)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "pGlu-His-Trp-Ser-Tyr-D-Trp-Leu-Arg-Pro-Gly-NH2",
        "reconstitution_info": {"preparation_en": "Depot microspheres: reconstitute with provided diluent", "preparation_de": "Depot-Mikrosphären: mit mitgeliefertem Lösungsmittel rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "36 months", "shelf_life_reconstituted": "Use immediately after reconstitution", "light_sensitive": True, "solvent": "Sterile water with carboxymethylcellulose"},
        "application_goals": [{"goal_en": "Hormonal Health", "goal_de": "Hormonelle Gesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── CARDIOVASCULAR / NATRIURETIC ─────────────────────────────
    {
        "name": "BNP (Nesiritide)",
        "slug": "nesiritide",
        "category": "Natriuretic Peptide",
        "description": {
            "en": "Nesiritide is a recombinant form of human B-type natriuretic peptide (BNP). It is FDA-approved for the treatment of acutely decompensated heart failure with dyspnea at rest. BNP is naturally produced by ventricular cardiomyocytes in response to volume overload and wall stretch, serving as a key biomarker and therapeutic target in heart failure.",
            "de": "Nesiritid ist eine rekombinante Form des humanen B-Typ natriuretischen Peptids (BNP). Es ist FDA-zugelassen zur Behandlung akut dekompensierter Herzinsuffizienz mit Ruhedyspnoe. BNP wird natürlich von ventrikulären Kardiomyozyten als Reaktion auf Volumenüberladung produziert."
        },
        "mechanism_of_action": {"en": "Binds to natriuretic peptide receptor A (NPR-A), activating guanylate cyclase and increasing cGMP. This causes vasodilation (both arterial and venous), natriuresis, diuresis, and suppression of RAAS and sympathetic nervous system. Reduces cardiac preload and afterload.", "de": "Bindet an den natriuretischen Peptidrezeptor A (NPR-A), aktiviert Guanylatzyklase und erhöht cGMP. Dies verursacht Vasodilatation, Natriurese, Diurese und RAAS-Suppression."},
        "indications": [
            {"condition_en": "Acute decompensated heart failure", "condition_de": "Akut dekompensierte Herzinsuffizienz", "description_en": "IV treatment for dyspnea at rest", "description_de": "IV-Behandlung bei Ruhedyspnoe"},
            {"condition_en": "Acute pulmonary edema", "condition_de": "Akutes Lungenödem", "description_en": "Rapid symptom relief", "description_de": "Schnelle Symptomlinderung"},
            {"condition_en": "Cardiorenal syndrome", "condition_de": "Kardiorenales Syndrom", "description_en": "Renal blood flow improvement", "description_de": "Verbesserung des renalen Blutflusses"}
        ],
        "benefits": [{"benefit_en": "Rapid hemodynamic improvement", "benefit_de": "Schnelle hämodynamische Verbesserung"}, {"benefit_en": "Reduces pulmonary capillary wedge pressure", "benefit_de": "Senkt den pulmonalkapillären Verschlussdruck"}, {"benefit_en": "Symptom relief in acute HF", "benefit_de": "Symptomlinderung bei akuter Herzinsuffizienz"}, {"benefit_en": "RAAS suppression", "benefit_de": "RAAS-Suppression"}],
        "side_effects": [
            {"name_en": "Hypotension", "name_de": "Hypotonie", "severity": "severe", "frequency": "common", "description_en": "Most significant adverse effect, dose-dependent", "description_de": "Bedeutendste Nebenwirkung, dosisabhängig"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Vasodilation-related", "description_de": "Vasodilatationsbedingt"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "common", "description_en": "GI symptoms", "description_de": "GI-Symptome"},
            {"name_en": "Renal impairment", "name_de": "Nierenfunktionsstörung", "severity": "moderate", "frequency": "uncommon", "description_en": "Creatinine elevation", "description_de": "Kreatininerhöhung"},
            {"name_en": "Ventricular arrhythmias", "name_de": "Ventrikuläre Arrhythmien", "severity": "severe", "frequency": "rare", "description_en": "Rare but serious", "description_de": "Selten aber schwerwiegend"}
        ],
        "dosage": {"starting_dose": "2 mcg/kg IV bolus", "maintenance_dose": "0.01 mcg/kg/min infusion", "frequency_en": "Continuous IV infusion", "frequency_de": "Kontinuierliche IV-Infusion", "route_en": "Intravenous", "route_de": "Intravenös", "notes_en": "Hospital use only, hemodynamic monitoring required", "notes_de": "Nur im Krankenhaus, hämodynamisches Monitoring erforderlich"},
        "contraindications": [{"en": "Cardiogenic shock", "de": "Kardiogener Schock"}, {"en": "Systolic BP <90 mmHg", "de": "Systolischer BD <90 mmHg"}, {"en": "Aortic stenosis", "de": "Aortenstenose"}],
        "drug_interactions": ["ACE inhibitors (additive hypotension)", "Diuretics (enhanced effect)", "Other vasodilators"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": False, "notes_en": "FDA approved 2001 (Natrecor), use has declined due to safety concerns", "notes_de": "FDA-Zulassung 2001 (Natrecor), Anwendung rückläufig aufgrund von Sicherheitsbedenken"},
        "manufacturer": "Janssen (Johnson & Johnson)",
        "molecular_weight": "3464 Da", "amino_acid_count": "32", "half_life": "18 minutes",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "SPKMVQGSGCFGRKMDRISSSSGLGCKVLRRH",
        "reconstitution_info": {"preparation_en": "Reconstitute 1.5mg vial with 5mL D5W", "preparation_de": "1,5mg Durchstechflasche mit 5ml G5W rekonstituieren", "storage_temperature": "2-25°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "24 hours", "light_sensitive": False, "solvent": "D5W or 0.9% NaCl"},
        "application_goals": [{"goal_en": "Cardiovascular Health", "goal_de": "Kardiovaskuläre Gesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── DIABETES / METABOLIC (advanced) ──────────────────────────
    {
        "name": "Pramlintide",
        "slug": "pramlintide",
        "category": "Amylin Analog",
        "description": {
            "en": "Pramlintide (Symlin) is a synthetic analog of amylin, a peptide hormone co-secreted with insulin by pancreatic beta cells. It is the only FDA-approved amylin analog, used as adjunct therapy for type 1 and type 2 diabetes. Pramlintide slows gastric emptying, suppresses postprandial glucagon, and promotes satiety, addressing aspects of glucose control that insulin alone cannot.",
            "de": "Pramlintid (Symlin) ist ein synthetisches Analogon von Amylin, einem Peptidhormon, das zusammen mit Insulin von den Beta-Zellen der Bauchspeicheldrüse sezerniert wird. Es ist das einzige FDA-zugelassene Amylin-Analogon, als Zusatztherapie bei Typ-1- und Typ-2-Diabetes eingesetzt."
        },
        "mechanism_of_action": {"en": "Mimics the effects of natural amylin: slows gastric emptying, suppresses postprandial glucagon secretion, and promotes centrally mediated satiety. Does not directly affect insulin secretion but complements insulin therapy for improved postprandial glucose control.", "de": "Ahmt die Wirkungen von natürlichem Amylin nach: verlangsamt Magenentleerung, unterdrückt postprandiale Glukagonsekretion und fördert zentral vermitteltes Sättigungsgefühl."},
        "indications": [
            {"condition_en": "Type 1 Diabetes", "condition_de": "Typ-1-Diabetes", "description_en": "Adjunct to mealtime insulin", "description_de": "Ergänzung zum Mahlzeiteninsulin"},
            {"condition_en": "Type 2 Diabetes", "condition_de": "Typ-2-Diabetes", "description_en": "Adjunct to mealtime insulin with/without metformin", "description_de": "Ergänzung zum Mahlzeiteninsulin mit/ohne Metformin"},
            {"condition_en": "Postprandial hyperglycemia", "condition_de": "Postprandiale Hyperglykämie", "description_en": "Specific control of post-meal glucose spikes", "description_de": "Spezifische Kontrolle postprandialer Glukosespitzen"}
        ],
        "benefits": [{"benefit_en": "Improved postprandial glucose control", "benefit_de": "Verbesserte postprandiale Glukosekontrolle"}, {"benefit_en": "Weight loss (average 1-2 kg)", "benefit_de": "Gewichtsverlust (durchschnittlich 1-2 kg)"}, {"benefit_en": "Reduced insulin requirements", "benefit_de": "Reduzierter Insulinbedarf"}, {"benefit_en": "Unique mechanism complementing insulin", "benefit_de": "Einzigartiger Mechanismus, der Insulin ergänzt"}],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "moderate", "frequency": "common", "description_en": "Most common, usually decreases over time", "description_de": "Am häufigsten, nimmt meist mit der Zeit ab"},
            {"name_en": "Severe hypoglycemia", "name_de": "Schwere Hypoglykämie", "severity": "severe", "frequency": "common", "description_en": "Especially in T1DM, requires insulin dose reduction", "description_de": "Besonders bei T1DM, erfordert Insulindosisreduktion"},
            {"name_en": "Anorexia", "name_de": "Appetitlosigkeit", "severity": "mild", "frequency": "common", "description_en": "Decreased appetite", "description_de": "Verminderter Appetit"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "common", "description_en": "Frequent occurrence", "description_de": "Häufig"},
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "uncommon", "description_en": "Mild local reactions", "description_de": "Leichte lokale Reaktionen"}
        ],
        "dosage": {"starting_dose": "15 mcg (T1DM) / 60 mcg (T2DM)", "maintenance_dose": "30-60 mcg (T1DM) / 120 mcg (T2DM)", "frequency_en": "Before major meals", "frequency_de": "Vor Hauptmahlzeiten", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Reduce mealtime insulin by 50% when starting pramlintide", "notes_de": "Mahlzeiteninsulin um 50% reduzieren bei Pramlintid-Start"},
        "contraindications": [{"en": "Gastroparesis", "de": "Gastroparese"}, {"en": "Hypoglycemia unawareness", "de": "Hypoglykämie-Wahrnehmungsstörung"}, {"en": "HbA1c >9% (T1DM)", "de": "HbA1c >9% (T1DM)"}],
        "drug_interactions": ["Insulin (must reduce dose)", "Oral hypoglycemics", "Drugs affecting GI motility"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": False, "notes_en": "FDA approved 2005 (Symlin), only approved amylin analog", "notes_de": "FDA-Zulassung 2005 (Symlin), einziges zugelassenes Amylin-Analogon"},
        "manufacturer": "AstraZeneca (originally Amylin Pharmaceuticals)",
        "molecular_weight": "3949 Da", "amino_acid_count": "37", "half_life": "48 minutes",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "KCNTATCATQRLANFLVHSSNNFGPILPPTNVGSNTY-NH2",
        "reconstitution_info": {"preparation_en": "Pre-filled pen, no reconstitution needed", "preparation_de": "Fertigpen, keine Rekonstitution nötig", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "28 days at room temperature in use", "light_sensitive": True, "solvent": "Pre-filled solution"},
        "application_goals": [{"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}, {"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── CANCER / ONCOLOGY PEPTIDES ────────────────────────────────
    {
        "name": "Octreotide",
        "slug": "octreotide",
        "category": "Somatostatin Analog",
        "description": {
            "en": "Octreotide (Sandostatin) is a synthetic somatostatin analog approximately 45 times more potent than natural somatostatin for inhibiting growth hormone release. It is FDA-approved for acromegaly, carcinoid tumors, and VIPomas. Octreotide inhibits multiple hormones including GH, insulin, glucagon, and gastrointestinal peptides.",
            "de": "Octreotid (Sandostatin) ist ein synthetisches Somatostatin-Analogon, etwa 45-mal potenter als natürliches Somatostatin bei der Hemmung der Wachstumshormonfreisetzung. Es ist FDA-zugelassen für Akromegalie, Karzinoide und VIPome."
        },
        "mechanism_of_action": {"en": "Binds to somatostatin receptors (primarily SSTR2 and SSTR5) to inhibit secretion of GH, TSH, insulin, glucagon, VIP, serotonin, gastrin, and other GI/pancreatic hormones. Also has antiproliferative effects on neuroendocrine tumor cells.", "de": "Bindet an Somatostatinrezeptoren (hauptsächlich SSTR2 und SSTR5) zur Hemmung der Sekretion von GH, TSH, Insulin, Glukagon, VIP, Serotonin, Gastrin und anderen Hormonen."},
        "indications": [
            {"condition_en": "Acromegaly", "condition_de": "Akromegalie", "description_en": "GH/IGF-1 suppression when surgery insufficient", "description_de": "GH/IGF-1-Suppression wenn Operation unzureichend"},
            {"condition_en": "Carcinoid tumors", "condition_de": "Karzinoide Tumoren", "description_en": "Symptom control (flushing, diarrhea)", "description_de": "Symptomkontrolle (Flushing, Durchfall)"},
            {"condition_en": "VIPomas", "condition_de": "VIPome", "description_en": "Control of watery diarrhea", "description_de": "Kontrolle der wässrigen Diarrhoe"}
        ],
        "benefits": [{"benefit_en": "Effective GH/IGF-1 suppression", "benefit_de": "Effektive GH/IGF-1-Suppression"}, {"benefit_en": "Long-acting depot formulation available", "benefit_de": "Langwirkende Depotformulierung verfügbar"}, {"benefit_en": "Symptom control in neuroendocrine tumors", "benefit_de": "Symptomkontrolle bei neuroendokrinen Tumoren"}, {"benefit_en": "Well-established safety profile", "benefit_de": "Gut etabliertes Sicherheitsprofil"}],
        "side_effects": [
            {"name_en": "Gallstones", "name_de": "Gallensteine", "severity": "moderate", "frequency": "common", "description_en": "15-30% incidence with long-term use", "description_de": "15-30% Inzidenz bei Langzeitanwendung"},
            {"name_en": "GI disturbances", "name_de": "GI-Störungen", "severity": "mild", "frequency": "common", "description_en": "Diarrhea, abdominal pain, nausea", "description_de": "Durchfall, Bauchschmerzen, Übelkeit"},
            {"name_en": "Hyperglycemia", "name_de": "Hyperglykämie", "severity": "moderate", "frequency": "common", "description_en": "Insulin/glucagon suppression imbalance", "description_de": "Insulin/Glukagon-Suppressions-Ungleichgewicht"},
            {"name_en": "Injection site pain", "name_de": "Schmerzen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Especially with depot formulation", "description_de": "Besonders bei Depotformulierung"},
            {"name_en": "Bradycardia", "name_de": "Bradykardie", "severity": "moderate", "frequency": "uncommon", "description_en": "Heart rate reduction", "description_de": "Herzfrequenzreduktion"}
        ],
        "dosage": {"starting_dose": "50 mcg SC 2-3x daily", "maintenance_dose": "100-600 mcg/day SC or 20 mg LAR monthly", "frequency_en": "2-3 times daily (SC) or monthly (LAR depot)", "frequency_de": "2-3 mal täglich (SC) oder monatlich (LAR-Depot)", "route_en": "Subcutaneous or intramuscular (depot)", "route_de": "Subkutan oder intramuskulär (Depot)", "notes_en": "LAR depot must be administered by healthcare professional", "notes_de": "LAR-Depot muss von medizinischem Fachpersonal verabreicht werden"},
        "contraindications": [{"en": "Hypersensitivity to octreotide", "de": "Überempfindlichkeit gegen Octreotid"}, {"en": "None absolute", "de": "Keine absoluten"}],
        "drug_interactions": ["Insulin/oral hypoglycemics (dose adjustment needed)", "Cyclosporine (decreased absorption)", "Bromocriptine (increased bioavailability)", "Beta-blockers (additive bradycardia)"],
        "research_status": {"phase": "Approved", "fda_approved": True, "ema_approved": True, "notes_en": "FDA approved 1988, one of the most prescribed peptide drugs", "notes_de": "FDA-Zulassung 1988, eines der am häufigsten verschriebenen Peptidmedikamente"},
        "manufacturer": "Novartis",
        "molecular_weight": "1019 Da", "amino_acid_count": "8", "half_life": "1.5 hours (SC), 28 days effective (LAR)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "D-Phe-Cys-Phe-D-Trp-Lys-Thr-Cys-Thr-ol (cyclic)",
        "reconstitution_info": {"preparation_en": "SC: ready-to-use solution. LAR: reconstitute with provided diluent", "preparation_de": "SC: gebrauchsfertige Lösung. LAR: mit mitgeliefertem Lösungsmittel rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "Use immediately (LAR)", "light_sensitive": True, "solvent": "Mannitol diluent (LAR)"},
        "application_goals": [{"goal_en": "Hormonal Health", "goal_de": "Hormonelle Gesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── ANTI-AGING / LONGEVITY ───────────────────────────────────
    {
        "name": "FOXO4-DRI",
        "slug": "foxo4-dri",
        "category": "Senolytic Peptide",
        "description": {
            "en": "FOXO4-DRI is a cell-penetrating peptide designed to selectively eliminate senescent cells. It works by disrupting the FOXO4-p53 interaction that keeps senescent cells alive. In mouse studies, it restored fitness, fur density, and renal function in aged mice. It represents a novel approach to anti-aging through targeted removal of 'zombie cells' that drive inflammation and tissue dysfunction.",
            "de": "FOXO4-DRI ist ein zellpenetrierendes Peptid zur selektiven Eliminierung seneszenter Zellen. Es unterbricht die FOXO4-p53-Interaktion, die seneszente Zellen am Leben hält. In Mausstudien stellte es Fitness, Felldichte und Nierenfunktion bei alten Mäusen wieder her."
        },
        "mechanism_of_action": {"en": "Contains D-retro-inverso amino acids for protease resistance. Competes with endogenous FOXO4 for p53 binding in senescent cells, releasing p53 to the mitochondria where it triggers intrinsic apoptosis. Normal cells are unaffected as they do not rely on FOXO4-p53 interaction for survival.", "de": "Enthält D-Retro-Inverso-Aminosäuren für Proteaseresistenz. Konkurriert mit endogenem FOXO4 um p53-Bindung in seneszenten Zellen und löst deren Apoptose aus."},
        "indications": [
            {"condition_en": "Cellular senescence", "condition_de": "Zelluläre Seneszenz", "description_en": "Targeted elimination of senescent cells", "description_de": "Gezielte Eliminierung seneszenter Zellen"},
            {"condition_en": "Age-related disease", "condition_de": "Altersbedingte Erkrankungen", "description_en": "Research for healthspan extension", "description_de": "Forschung zur Verlängerung der Gesundheitsspanne"},
            {"condition_en": "Fibrosis", "condition_de": "Fibrose", "description_en": "Senescent cell-driven fibrosis", "description_de": "Seneszenz-getriebene Fibrose"}
        ],
        "benefits": [{"benefit_en": "Selective senescent cell elimination", "benefit_de": "Selektive Elimination seneszenter Zellen"}, {"benefit_en": "Restored organ function in animal models", "benefit_de": "Wiederhergestellte Organfunktion in Tiermodellen"}, {"benefit_en": "Does not harm normal cells", "benefit_de": "Schädigt keine normalen Zellen"}, {"benefit_en": "Novel anti-aging mechanism", "benefit_de": "Neuartiger Anti-Aging-Mechanismus"}],
        "side_effects": [
            {"name_en": "Unknown human safety profile", "name_de": "Unbekanntes humanes Sicherheitsprofil", "severity": "moderate", "frequency": "rare", "description_en": "No human clinical trials yet", "description_de": "Noch keine klinischen Humanstudien"},
            {"name_en": "Potential immune reaction", "name_de": "Mögliche Immunreaktion", "severity": "moderate", "frequency": "rare", "description_en": "Release of SASP from dying senescent cells", "description_de": "Freisetzung von SASP aus sterbenden seneszenten Zellen"},
            {"name_en": "Theoretical off-target effects", "name_de": "Theoretische Off-Target-Effekte", "severity": "moderate", "frequency": "rare", "description_en": "Potential effects on non-senescent cells", "description_de": "Mögliche Effekte auf nicht-seneszente Zellen"},
            {"name_en": "Inflammation (transient)", "name_de": "Entzündung (vorübergehend)", "severity": "mild", "frequency": "uncommon", "description_en": "From senescent cell clearance", "description_de": "Durch Seneszente-Zellen-Clearance"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Expected with peptide injection", "description_de": "Bei Peptidinjektion erwartet"}
        ],
        "dosage": {"starting_dose": "Research: 5 mg/kg (mice)", "maintenance_dose": "Experimental", "frequency_en": "3x per week for 3 weeks (mouse protocol)", "frequency_de": "3x pro Woche für 3 Wochen (Mausprotokoll)", "route_en": "Intravenous or intraperitoneal (research)", "route_de": "Intravenös oder intraperitoneal (Forschung)", "notes_en": "No established human dosing protocol", "notes_de": "Kein etabliertes humanes Dosierungsprotokoll"},
        "contraindications": [{"en": "Not for human use (research only)", "de": "Nicht für humane Anwendung (nur Forschung)"}, {"en": "Active infections", "de": "Aktive Infektionen"}, {"en": "Immunocompromised state", "de": "Immunsupprimierter Zustand"}],
        "drug_interactions": ["Other senolytics (dasatinib+quercetin)", "Chemotherapy", "Immunosuppressants"],
        "research_status": {"phase": "Pre-clinical", "fda_approved": False, "ema_approved": False, "notes_en": "Published in Cell 2017 (Baar et al.), no human trials yet", "notes_de": "Veröffentlicht in Cell 2017 (Baar et al.), noch keine Humanstudien"},
        "manufacturer": "Research compound (Erasmus University Medical Center)",
        "molecular_weight": "~4800 Da", "amino_acid_count": "49 (D-retro-inverso)", "half_life": "Hours (protease resistant)",
        "storage_conditions": {"en": "Store at -80°C", "de": "Bei -80°C lagern"},
        "amino_acid_sequence": "D-retro-inverso peptide targeting FOXO4-p53 interface",
        "reconstitution_info": {"preparation_en": "Reconstitute in sterile PBS", "preparation_de": "In sterilem PBS rekonstituieren", "storage_temperature": "-80°C", "shelf_life_unopened": "12 months", "shelf_life_reconstituted": "24 hours at 4°C", "light_sensitive": True, "solvent": "Sterile PBS"},
        "application_goals": [{"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Humanin",
        "slug": "humanin",
        "category": "Mitochondrial-Derived Peptide",
        "description": {
            "en": "Humanin is a 24-amino acid peptide encoded in the mitochondrial genome (MT-RNR2 gene). It was discovered in 2001 as a neuroprotective factor in Alzheimer's disease research. Humanin and its analogs protect cells against a wide range of stressors including amyloid-beta toxicity, oxidative stress, and serum starvation. Levels decline with age, making it a biomarker and therapeutic target for aging.",
            "de": "Humanin ist ein 24-Aminosäure-Peptid, kodiert im mitochondrialen Genom (MT-RNR2-Gen). Es wurde 2001 als neuroprotektiver Faktor in der Alzheimer-Forschung entdeckt. Humanin schützt Zellen gegen diverse Stressoren und nimmt mit dem Alter ab."
        },
        "mechanism_of_action": {"en": "Binds to FPRL1 (formyl peptide receptor-like 1), IGFBP-3, and BAX. Activates STAT3 and ERK1/2 survival signaling. Inhibits BAX-mediated apoptosis, reduces ROS, and improves mitochondrial function. Also enhances insulin sensitivity via IGFBP-3 interaction.", "de": "Bindet an FPRL1, IGFBP-3 und BAX. Aktiviert STAT3- und ERK1/2-Überlebenssignale. Hemmt BAX-vermittelte Apoptose, reduziert ROS und verbessert Mitochondrienfunktion."},
        "indications": [
            {"condition_en": "Alzheimer's disease research", "condition_de": "Alzheimer-Forschung", "description_en": "Neuroprotection against amyloid toxicity", "description_de": "Neuroprotektion gegen Amyloid-Toxizität"},
            {"condition_en": "Age-related decline", "condition_de": "Altersbedingter Rückgang", "description_en": "Mitochondrial function restoration", "description_de": "Wiederherstellung der Mitochondrienfunktion"},
            {"condition_en": "Metabolic syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Insulin sensitivity improvement", "description_de": "Verbesserung der Insulinsensitivität"}
        ],
        "benefits": [{"benefit_en": "Neuroprotective against multiple insults", "benefit_de": "Neuroprotektiv gegen multiple Schädigungen"}, {"benefit_en": "Cytoprotective (anti-apoptotic)", "benefit_de": "Zytoprotektiv (anti-apoptotisch)"}, {"benefit_en": "Improved insulin sensitivity", "benefit_de": "Verbesserte Insulinsensitivität"}, {"benefit_en": "Mitochondrial function support", "benefit_de": "Unterstützung der Mitochondrienfunktion"}],
        "side_effects": [
            {"name_en": "Limited safety data", "name_de": "Begrenzte Sicherheitsdaten", "severity": "moderate", "frequency": "rare", "description_en": "Mostly animal studies", "description_de": "Hauptsächlich Tierstudien"},
            {"name_en": "Potential tumor support (theoretical)", "name_de": "Mögliche Tumorunterstützung (theoretisch)", "severity": "moderate", "frequency": "rare", "description_en": "Anti-apoptotic effects could theoretically protect tumor cells", "description_de": "Anti-apoptotische Effekte könnten theoretisch Tumorzellen schützen"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local irritation", "description_de": "Lokale Reizung"},
            {"name_en": "Hypoglycemia (theoretical)", "name_de": "Hypoglykämie (theoretisch)", "severity": "mild", "frequency": "rare", "description_en": "Due to insulin sensitizing effects", "description_de": "Durch insulinsensibilisierende Effekte"},
            {"name_en": "Unknown long-term effects", "name_de": "Unbekannte Langzeiteffekte", "severity": "moderate", "frequency": "rare", "description_en": "No long-term human data", "description_de": "Keine humanen Langzeitdaten"}
        ],
        "dosage": {"starting_dose": "Research: varies", "maintenance_dose": "Experimental", "frequency_en": "Experimental protocols", "frequency_de": "Experimentelle Protokolle", "route_en": "Subcutaneous or IV (research)", "route_de": "Subkutan oder IV (Forschung)", "notes_en": "HNG (S14G-humanin) is a more potent analog", "notes_de": "HNG (S14G-Humanin) ist ein potenteres Analogon"},
        "contraindications": [{"en": "Active malignancy", "de": "Aktive Krebserkrankung"}, {"en": "Pregnancy", "de": "Schwangerschaft"}, {"en": "Not for human therapeutic use yet", "de": "Noch nicht für humane therapeutische Anwendung"}],
        "drug_interactions": ["Insulin (potential synergy)", "Chemotherapy (potential antagonism)", "Other neuroprotective agents"],
        "research_status": {"phase": "Pre-clinical", "fda_approved": False, "ema_approved": False, "notes_en": "Extensive research since 2001, human trials for analogs pending", "notes_de": "Umfangreiche Forschung seit 2001, Humanstudien für Analoga ausstehend"},
        "manufacturer": "Research compound",
        "molecular_weight": "2687 Da", "amino_acid_count": "24", "half_life": "Minutes (native), hours (analogs)",
        "storage_conditions": {"en": "Store at -20°C", "de": "Bei -20°C lagern"},
        "amino_acid_sequence": "MAPRGFSCLLLLTSEIDLPVKRRA",
        "reconstitution_info": {"preparation_en": "Reconstitute in sterile saline", "preparation_de": "In steriler Kochsalzlösung rekonstituieren", "storage_temperature": "-20°C", "shelf_life_unopened": "12 months", "shelf_life_reconstituted": "48 hours at 4°C", "light_sensitive": True, "solvent": "Sterile saline"},
        "application_goals": [{"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}, {"goal_en": "Cognitive", "goal_de": "Kognitiv", "relevance": "primary"}, {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── IMMUNE / INFLAMMATION ────────────────────────────────────
    {
        "name": "Thymalin",
        "slug": "thymalin",
        "category": "Thymic Peptide",
        "description": {
            "en": "Thymalin is a polypeptide complex extracted from calf thymus glands, developed at the St. Petersburg Institute of Bioregulation and Gerontology. It is approved in Russia for immune restoration and has been used for decades in immunodeficiency states. Thymalin modulates T-cell function and has shown remarkable life-extension properties in animal studies and a 6-year human trial.",
            "de": "Thymalin ist ein Polypeptidkomplex aus Kälber-Thymusdrüsen, entwickelt am St. Petersburger Institut für Bioregulation und Gerontologie. Es ist in Russland für Immunrestauration zugelassen und hat bemerkenswerte lebensverlängernde Eigenschaften in Tier- und Humanstudien gezeigt."
        },
        "mechanism_of_action": {"en": "Restores T-lymphocyte function including T-helper/T-suppressor ratio normalization. Enhances phagocytosis, NK cell activity, and interferon production. Modulates neuroendocrine-immune interactions and normalizes circadian cortisol rhythm.", "de": "Stellt T-Lymphozyten-Funktion wieder her einschließlich T-Helfer/T-Suppressor-Ratio-Normalisierung. Verstärkt Phagozytose, NK-Zell-Aktivität und Interferon-Produktion."},
        "indications": [
            {"condition_en": "Immunodeficiency states", "condition_de": "Immundefizienzzustände", "description_en": "Primary and secondary immune restoration", "description_de": "Primäre und sekundäre Immunrestauration"},
            {"condition_en": "Post-surgical immunosuppression", "condition_de": "Postoperative Immunsuppression", "description_en": "Immune recovery after surgery/radiation", "description_de": "Immunerholung nach OP/Bestrahlung"},
            {"condition_en": "Age-related immune decline", "condition_de": "Altersbedingter Immunrückgang", "description_en": "Thymic involution reversal", "description_de": "Umkehr der Thymusinvolution"}
        ],
        "benefits": [{"benefit_en": "Immune function restoration", "benefit_de": "Wiederherstellung der Immunfunktion"}, {"benefit_en": "Life-extension effects (animal + human data)", "benefit_de": "Lebensverlängernde Effekte (Tier- + Humandaten)"}, {"benefit_en": "T-cell ratio normalization", "benefit_de": "T-Zell-Ratio-Normalisierung"}, {"benefit_en": "Decades of clinical use in Russia", "benefit_de": "Jahrzehnte klinischer Anwendung in Russland"}],
        "side_effects": [
            {"name_en": "Allergic reaction", "name_de": "Allergische Reaktion", "severity": "moderate", "frequency": "rare", "description_en": "Animal-derived product", "description_de": "Tierisches Produkt"},
            {"name_en": "Injection site pain", "name_de": "Schmerzen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local discomfort", "description_de": "Lokales Unbehagen"},
            {"name_en": "Flu-like symptoms", "name_de": "Grippeähnliche Symptome", "severity": "mild", "frequency": "uncommon", "description_en": "Immune activation response", "description_de": "Immunaktivierungsreaktion"},
            {"name_en": "Fever", "name_de": "Fieber", "severity": "mild", "frequency": "uncommon", "description_en": "Transient", "description_de": "Vorübergehend"},
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "mild", "frequency": "rare", "description_en": "Infrequent", "description_de": "Selten"}
        ],
        "dosage": {"starting_dose": "10 mg", "maintenance_dose": "10 mg daily for 5-10 days", "frequency_en": "Daily for 5-10 day courses", "frequency_de": "Täglich für 5-10 Tage Kuren", "route_en": "Intramuscular injection", "route_de": "Intramuskuläre Injektion", "notes_en": "Courses repeated 1-6 months apart", "notes_de": "Kuren werden alle 1-6 Monate wiederholt"},
        "contraindications": [{"en": "Allergy to animal-derived proteins", "de": "Allergie gegen tierische Proteine"}, {"en": "Autoimmune diseases (relative)", "de": "Autoimmunerkrankungen (relativ)"}, {"en": "Pregnancy", "de": "Schwangerschaft"}],
        "drug_interactions": ["Immunosuppressants (antagonistic)", "Vaccines (potential enhanced response)", "Corticosteroids"],
        "research_status": {"phase": "Approved (Russia)", "fda_approved": False, "ema_approved": False, "notes_en": "Approved in Russia for decades, 6-year human longevity trial published", "notes_de": "Seit Jahrzehnten in Russland zugelassen, 6-Jahres-Langlebigkeitsstudie veröffentlicht"},
        "manufacturer": "St. Petersburg Institute of Bioregulation and Gerontology",
        "molecular_weight": "~1200-6000 Da (complex)", "amino_acid_count": "Polypeptide complex", "half_life": "Hours",
        "storage_conditions": {"en": "Store at 2-8°C", "de": "Bei 2-8°C lagern"},
        "amino_acid_sequence": "Polypeptide complex (multiple peptide chains)",
        "reconstitution_info": {"preparation_en": "Dissolve lyophilized powder in 1-2 mL saline", "preparation_de": "Lyophilisiertes Pulver in 1-2 ml Kochsalzlösung lösen", "storage_temperature": "2-8°C", "shelf_life_unopened": "36 months", "shelf_life_reconstituted": "Use immediately", "light_sensitive": False, "solvent": "0.9% NaCl"},
        "application_goals": [{"goal_en": "Immune", "goal_de": "Immunsystem", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Vasoactive Intestinal Peptide (VIP)",
        "slug": "vip",
        "category": "Neuropeptide / Immunomodulator",
        "description": {
            "en": "Vasoactive Intestinal Peptide (VIP) is a 28-amino acid neuropeptide found in the gut, brain, and immune system. It acts as a neurotransmitter, vasodilator, and potent immunomodulator. VIP has gained attention for treating chronic inflammatory response syndrome (CIRS) and mold illness. It regulates innate immunity, reduces cytokine storms, and protects mucosal barriers.",
            "de": "Vasoaktives Intestinales Peptid (VIP) ist ein 28-Aminosäure-Neuropeptid im Darm, Gehirn und Immunsystem. Es wirkt als Neurotransmitter, Vasodilator und potenter Immunmodulator. VIP wird zur Behandlung des chronischen Entzündungssyndroms (CIRS) und Schimmelpilzerkrankungen eingesetzt."
        },
        "mechanism_of_action": {"en": "Binds to VPAC1 and VPAC2 receptors, activating adenylate cyclase and increasing cAMP. Suppresses pro-inflammatory cytokines (TNF-alpha, IL-6, IL-12), promotes Th2/Treg differentiation, protects mucosal epithelium, and acts as a pulmonary vasodilator.", "de": "Bindet an VPAC1- und VPAC2-Rezeptoren, aktiviert Adenylatcyclase und erhöht cAMP. Unterdrückt pro-inflammatorische Zytokine und schützt mukosale Epithelien."},
        "indications": [
            {"condition_en": "Chronic Inflammatory Response Syndrome (CIRS)", "condition_de": "Chronisches Entzündungsreaktionssyndrom (CIRS)", "description_en": "Mold illness and biotoxin exposure", "description_de": "Schimmelpilzerkrankung und Biotoxin-Exposition"},
            {"condition_en": "Pulmonary arterial hypertension", "condition_de": "Pulmonale arterielle Hypertonie", "description_en": "Pulmonary vasodilation", "description_de": "Pulmonale Vasodilatation"},
            {"condition_en": "Inflammatory bowel disease", "condition_de": "Entzündliche Darmerkrankungen", "description_en": "Gut immune modulation", "description_de": "Darm-Immunmodulation"}
        ],
        "benefits": [{"benefit_en": "Potent anti-inflammatory effects", "benefit_de": "Potente anti-entzündliche Effekte"}, {"benefit_en": "Mucosal barrier protection", "benefit_de": "Schleimhautbarriereschutz"}, {"benefit_en": "Pulmonary vasodilation", "benefit_de": "Pulmonale Vasodilatation"}, {"benefit_en": "Regulatory T-cell induction", "benefit_de": "Induktion regulatorischer T-Zellen"}],
        "side_effects": [
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "VIP stimulates intestinal secretion", "description_de": "VIP stimuliert intestinale Sekretion"},
            {"name_en": "Hypotension", "name_de": "Hypotonie", "severity": "moderate", "frequency": "uncommon", "description_en": "Vasodilation effect", "description_de": "Vasodilatationseffekt"},
            {"name_en": "Nasal congestion", "name_de": "Nasale Kongestion", "severity": "mild", "frequency": "common", "description_en": "With nasal spray delivery", "description_de": "Bei Nasenspray-Verabreichung"},
            {"name_en": "Flushing", "name_de": "Hautrötung", "severity": "mild", "frequency": "uncommon", "description_en": "Vasodilation-related", "description_de": "Vasodilatationsbedingt"},
            {"name_en": "Cough", "name_de": "Husten", "severity": "mild", "frequency": "uncommon", "description_en": "With inhaled delivery", "description_de": "Bei inhalativer Verabreichung"}
        ],
        "dosage": {"starting_dose": "50 mcg nasal spray", "maintenance_dose": "50 mcg 4x daily", "frequency_en": "4 times daily (nasal)", "frequency_de": "4 mal täglich (nasal)", "route_en": "Intranasal or subcutaneous", "route_de": "Intranasal oder subkutan", "notes_en": "Shoemaker protocol for CIRS", "notes_de": "Shoemaker-Protokoll für CIRS"},
        "contraindications": [{"en": "VIPoma (VIP-secreting tumor)", "de": "VIPom (VIP-sezernierender Tumor)"}, {"en": "Severe hypotension", "de": "Schwere Hypotonie"}, {"en": "Active diarrheal illness", "de": "Aktive Durchfallerkrankung"}],
        "drug_interactions": ["Antihypertensives (additive)", "Diuretics", "ACE inhibitors"],
        "research_status": {"phase": "Off-label / Research", "fda_approved": False, "ema_approved": False, "notes_en": "Used off-label for CIRS (Shoemaker protocol), Phase II for PAH", "notes_de": "Off-Label für CIRS (Shoemaker-Protokoll), Phase II für PAH"},
        "manufacturer": "Compounding pharmacies",
        "molecular_weight": "3326 Da", "amino_acid_count": "28", "half_life": "1-2 minutes (IV)",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "HSDAVFTDNYTRLRKQMAVKKYLNSILN-NH2",
        "reconstitution_info": {"preparation_en": "Nasal spray from compounding pharmacy", "preparation_de": "Nasenspray von Apotheke", "storage_temperature": "2-8°C", "shelf_life_unopened": "6 months", "shelf_life_reconstituted": "30 days", "light_sensitive": True, "solvent": "Preserved saline"},
        "application_goals": [{"goal_en": "Immune", "goal_de": "Immunsystem", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── PAIN / OPIOID PEPTIDES ───────────────────────────────────
    {
        "name": "DSIP (Delta Sleep-Inducing Peptide)",
        "slug": "dsip",
        "category": "Neuropeptide",
        "description": {
            "en": "Delta Sleep-Inducing Peptide (DSIP) is a naturally occurring nonapeptide found in the brain that promotes deep delta-wave sleep. First isolated in 1977 from cerebral venous blood of rabbits during electrically induced sleep, DSIP modulates sleep architecture, has analgesic properties, reduces stress hormones, and shows potential for treating insomnia and opioid withdrawal.",
            "de": "Delta Sleep-Inducing Peptide (DSIP) ist ein natürlich vorkommendes Nonapeptid im Gehirn, das tiefen Delta-Wellen-Schlaf fördert. 1977 erstmals isoliert, moduliert DSIP die Schlafarchitektur, hat analgetische Eigenschaften und zeigt Potential bei Schlaflosigkeit und Opioidentzug."
        },
        "mechanism_of_action": {"en": "Modulates GABA-ergic transmission, suppresses cortisol and ACTH secretion, increases LH release, and alters the ratio of delta to sigma sleep. May act through somatostatin receptors and modulate endorphin systems. Normalizes disturbed sleep patterns rather than inducing sedation.", "de": "Moduliert GABA-erge Transmission, unterdrückt Cortisol- und ACTH-Sekretion, erhöht LH-Freisetzung und verändert das Verhältnis von Delta- zu Sigma-Schlaf."},
        "indications": [
            {"condition_en": "Insomnia", "condition_de": "Schlaflosigkeit", "description_en": "Sleep normalization without sedation", "description_de": "Schlafnormalisierung ohne Sedierung"},
            {"condition_en": "Chronic pain", "condition_de": "Chronische Schmerzen", "description_en": "Analgesic and pain modulation", "description_de": "Analgetische und schmerzmodulierende Wirkung"},
            {"condition_en": "Opioid withdrawal", "condition_de": "Opioidentzug", "description_en": "Withdrawal symptom reduction", "description_de": "Reduktion von Entzugssymptomen"}
        ],
        "benefits": [{"benefit_en": "Promotes natural delta-wave sleep", "benefit_de": "Fördert natürlichen Delta-Wellen-Schlaf"}, {"benefit_en": "Non-sedative sleep normalization", "benefit_de": "Nicht-sedierende Schlafnormalisierung"}, {"benefit_en": "Stress hormone reduction", "benefit_de": "Stresshormon-Reduktion"}, {"benefit_en": "Analgesic properties", "benefit_de": "Analgetische Eigenschaften"}],
        "side_effects": [
            {"name_en": "Drowsiness", "name_de": "Schläfrigkeit", "severity": "mild", "frequency": "common", "description_en": "Expected effect", "description_de": "Erwarteter Effekt"},
            {"name_en": "Headache", "name_de": "Kopfschmerzen", "severity": "mild", "frequency": "uncommon", "description_en": "Occasional occurrence", "description_de": "Gelegentliches Auftreten"},
            {"name_en": "Vivid dreams", "name_de": "Lebhafte Träume", "severity": "mild", "frequency": "common", "description_en": "Increased dream recall and vividness", "description_de": "Verstärkte Traumerinnerung und Lebhaftigkeit"},
            {"name_en": "Morning grogginess", "name_de": "Morgendliche Benommenheit", "severity": "mild", "frequency": "uncommon", "description_en": "If dose too high", "description_de": "Bei zu hoher Dosis"},
            {"name_en": "Injection site reaction", "name_de": "Reaktion an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local irritation", "description_de": "Lokale Reizung"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "100-300 mcg", "frequency_en": "Once daily before bedtime", "frequency_de": "Einmal täglich vor dem Schlafengehen", "route_en": "Subcutaneous or intranasal", "route_de": "Subkutan oder intranasal", "notes_en": "Administer 30-60 minutes before desired sleep", "notes_de": "30-60 Minuten vor gewünschtem Schlaf verabreichen"},
        "contraindications": [{"en": "Severe respiratory depression", "de": "Schwere Atemdepression"}, {"en": "Pregnancy/breastfeeding", "de": "Schwangerschaft/Stillzeit"}, {"en": "CNS depressant use (caution)", "de": "ZNS-Depressiva (Vorsicht)"}],
        "drug_interactions": ["Benzodiazepines (potential synergy)", "Opioids (potential synergy)", "Alcohol (enhanced sedation)"],
        "research_status": {"phase": "Phase II (various)", "fda_approved": False, "ema_approved": False, "notes_en": "Studied since 1977, not approved in any major market", "notes_de": "Seit 1977 untersucht, in keinem großen Markt zugelassen"},
        "manufacturer": "Research compound",
        "molecular_weight": "848 Da", "amino_acid_count": "9", "half_life": "7-8 minutes",
        "storage_conditions": {"en": "Store lyophilized at -20°C", "de": "Lyophilisiert bei -20°C lagern"},
        "amino_acid_sequence": "Trp-Ala-Gly-Gly-Asp-Ala-Ser-Gly-Glu",
        "reconstitution_info": {"preparation_en": "Reconstitute with bacteriostatic water", "preparation_de": "Mit bakteriostatischem Wasser rekonstituieren", "storage_temperature": "2-8°C", "shelf_life_unopened": "24 months", "shelf_life_reconstituted": "21 days", "light_sensitive": True, "solvent": "Bacteriostatic water"},
        "application_goals": [{"goal_en": "Cognitive", "goal_de": "Kognitiv", "relevance": "primary"}, {"goal_en": "Healing", "goal_de": "Heilung", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── WEIGHT MANAGEMENT ────────────────────────────────────────
    {
        "name": "Survodutide",
        "slug": "survodutide",
        "category": "Glucagon/GLP-1 Dual Agonist",
        "description": {
            "en": "Survodutide (BI 456906) is a novel dual glucagon and GLP-1 receptor agonist developed by Boehringer Ingelheim. In Phase II trials, it achieved up to 19% body weight loss in 46 weeks, making it one of the most effective obesity treatments in development. Unlike other dual agonists, survodutide uniquely combines glucagon's fat-burning and energy expenditure effects with GLP-1's appetite suppression.",
            "de": "Survodutid (BI 456906) ist ein neuartiger dualer Glukagon- und GLP-1-Rezeptoragonist von Boehringer Ingelheim. In Phase-II-Studien erreichte es bis zu 19% Gewichtsverlust in 46 Wochen. Survodutid kombiniert Glukagons fettverbrennende Effekte mit der Appetitunterdrückung von GLP-1."
        },
        "mechanism_of_action": {"en": "Dual agonist at glucagon and GLP-1 receptors. Glucagon receptor activation increases energy expenditure, hepatic fatty acid oxidation, and thermogenesis. GLP-1 activation suppresses appetite and slows gastric emptying. The combination produces greater weight loss than either target alone.", "de": "Dualer Agonist an Glukagon- und GLP-1-Rezeptoren. Glukagonrezeptor-Aktivierung erhöht Energieverbrauch und Thermogenese. GLP-1-Aktivierung unterdrückt Appetit."},
        "indications": [
            {"condition_en": "Obesity", "condition_de": "Adipositas", "description_en": "Weight management in adults with BMI ≥30", "description_de": "Gewichtsmanagement bei Erwachsenen mit BMI ≥30"},
            {"condition_en": "NASH/MASH", "condition_de": "NASH/MASH", "description_en": "Non-alcoholic steatohepatitis treatment", "description_de": "Behandlung der nicht-alkoholischen Steatohepatitis"},
            {"condition_en": "Type 2 Diabetes", "condition_de": "Typ-2-Diabetes", "description_en": "Glycemic control with weight loss", "description_de": "Blutzuckerkontrolle mit Gewichtsverlust"}
        ],
        "benefits": [{"benefit_en": "Up to 19% body weight loss", "benefit_de": "Bis zu 19% Körpergewichtsverlust"}, {"benefit_en": "Increased energy expenditure via glucagon", "benefit_de": "Erhöhter Energieverbrauch durch Glukagon"}, {"benefit_en": "Liver fat reduction (NASH benefit)", "benefit_de": "Leberfettreduktion (NASH-Vorteil)"}, {"benefit_en": "Improved metabolic parameters", "benefit_de": "Verbesserte metabolische Parameter"}],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "moderate", "frequency": "common", "description_en": "Most common, usually decreases", "description_de": "Am häufigsten, nimmt meist ab"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "moderate", "frequency": "common", "description_en": "GI side effect", "description_de": "GI-Nebenwirkung"},
            {"name_en": "Diarrhea", "name_de": "Durchfall", "severity": "mild", "frequency": "common", "description_en": "During dose escalation", "description_de": "Während der Dosiseskalation"},
            {"name_en": "Increased heart rate", "name_de": "Erhöhte Herzfrequenz", "severity": "mild", "frequency": "common", "description_en": "Glucagon-mediated effect", "description_de": "Glukagonvermittelter Effekt"},
            {"name_en": "Hyperglycemia (transient)", "name_de": "Hyperglykämie (vorübergehend)", "severity": "mild", "frequency": "uncommon", "description_en": "Glucagon effect, offset by GLP-1", "description_de": "Glukagoneffekt, ausgeglichen durch GLP-1"}
        ],
        "dosage": {"starting_dose": "0.3 mg", "maintenance_dose": "Up to 4.8 mg", "frequency_en": "Once weekly", "frequency_de": "Einmal wöchentlich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Dose escalation over 16+ weeks", "notes_de": "Dosiseskalation über 16+ Wochen"},
        "contraindications": [{"en": "Personal/family history of MTC", "de": "Persönliche/familiäre Vorgeschichte von MTC"}, {"en": "MEN 2 syndrome", "de": "MEN-2-Syndrom"}, {"en": "Severe hepatic impairment", "de": "Schwere Leberfunktionsstörung"}],
        "drug_interactions": ["Insulin (hypoglycemia risk)", "Sulfonylureas", "Oral medications (delayed absorption)"],
        "research_status": {"phase": "Phase III", "fda_approved": False, "ema_approved": False, "notes_en": "Phase III SYNCHRONIZE trials ongoing, potential approval 2026", "notes_de": "Phase-III-SYNCHRONIZE-Studien laufen, mögliche Zulassung 2026"},
        "manufacturer": "Boehringer Ingelheim / Zealand Pharma",
        "molecular_weight": "~4000 Da", "amino_acid_count": "~30", "half_life": "~6 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "Modified glucagon/GLP-1 hybrid sequence (proprietary)",
        "reconstitution_info": {"preparation_en": "Pre-filled pen (anticipated)", "preparation_de": "Fertigpen (erwartet)", "storage_temperature": "2-8°C", "shelf_life_unopened": "TBD", "shelf_life_reconstituted": "TBD", "light_sensitive": True, "solvent": "Pre-filled solution"},
        "application_goals": [{"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"}, {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    {
        "name": "Cagrilintide",
        "slug": "cagrilintide",
        "category": "Amylin Analog",
        "description": {
            "en": "Cagrilintide is a long-acting amylin analog developed by Novo Nordisk. When combined with semaglutide (as CagriSema), it has achieved unprecedented weight loss of up to 25% in clinical trials, potentially becoming the most effective obesity medication ever developed. Cagrilintide targets the amylin receptor pathway, complementing GLP-1 effects on appetite and metabolism.",
            "de": "Cagrilintid ist ein langwirkendes Amylin-Analogon von Novo Nordisk. In Kombination mit Semaglutid (als CagriSema) wurde ein beispielloser Gewichtsverlust von bis zu 25% in klinischen Studien erreicht. Cagrilintid zielt auf den Amylinrezeptor-Signalweg."
        },
        "mechanism_of_action": {"en": "Long-acting amylin receptor agonist that activates CTR/RAMP complexes in the area postrema and nucleus tractus solitarius. Promotes satiety, slows gastric emptying, and suppresses postprandial glucagon. When combined with semaglutide, provides dual appetite suppression through complementary CNS pathways.", "de": "Langwirkender Amylinrezeptor-Agonist, der CTR/RAMP-Komplexe aktiviert. Fördert Sättigung, verlangsamt Magenentleerung und unterdrückt postprandiales Glukagon."},
        "indications": [
            {"condition_en": "Obesity (as CagriSema)", "condition_de": "Adipositas (als CagriSema)", "description_en": "Combination therapy for severe obesity", "description_de": "Kombinationstherapie bei schwerer Adipositas"},
            {"condition_en": "Type 2 Diabetes (as CagriSema)", "condition_de": "Typ-2-Diabetes (als CagriSema)", "description_en": "Glycemic control with superior weight loss", "description_de": "Blutzuckerkontrolle mit überlegenem Gewichtsverlust"},
            {"condition_en": "Metabolic syndrome", "condition_de": "Metabolisches Syndrom", "description_en": "Comprehensive metabolic improvement", "description_de": "Umfassende metabolische Verbesserung"}
        ],
        "benefits": [{"benefit_en": "Up to 25% weight loss with CagriSema", "benefit_de": "Bis zu 25% Gewichtsverlust mit CagriSema"}, {"benefit_en": "Novel amylin-based mechanism", "benefit_de": "Neuartiger Amylin-basierter Mechanismus"}, {"benefit_en": "Once-weekly dosing", "benefit_de": "Einmal wöchentliche Dosierung"}, {"benefit_en": "Synergy with GLP-1 agonists", "benefit_de": "Synergie mit GLP-1-Agonisten"}],
        "side_effects": [
            {"name_en": "Nausea", "name_de": "Übelkeit", "severity": "moderate", "frequency": "common", "description_en": "Most common GI side effect", "description_de": "Häufigste GI-Nebenwirkung"},
            {"name_en": "Vomiting", "name_de": "Erbrechen", "severity": "moderate", "frequency": "common", "description_en": "During dose escalation", "description_de": "Während der Dosiseskalation"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Erythema, pain at injection site", "description_de": "Erythem, Schmerz an der Injektionsstelle"},
            {"name_en": "Constipation", "name_de": "Verstopfung", "severity": "mild", "frequency": "common", "description_en": "Slowed GI motility", "description_de": "Verlangsamte GI-Motilität"},
            {"name_en": "Decreased appetite", "name_de": "Verminderter Appetit", "severity": "mild", "frequency": "common", "description_en": "Intended therapeutic effect", "description_de": "Beabsichtigter therapeutischer Effekt"}
        ],
        "dosage": {"starting_dose": "0.25 mg", "maintenance_dose": "2.4 mg (CagriSema: cagri 2.4 mg + sema 2.4 mg)", "frequency_en": "Once weekly", "frequency_de": "Einmal wöchentlich", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Dose escalation over 16 weeks", "notes_de": "Dosiseskalation über 16 Wochen"},
        "contraindications": [{"en": "MTC or MEN 2 (semaglutide component)", "de": "MTC oder MEN 2 (Semaglutid-Komponente)"}, {"en": "Gastroparesis", "de": "Gastroparese"}, {"en": "Pregnancy", "de": "Schwangerschaft"}],
        "drug_interactions": ["Insulin (hypoglycemia risk)", "Oral medications (delayed absorption)", "Other GLP-1 agonists"],
        "research_status": {"phase": "Phase III", "fda_approved": False, "ema_approved": False, "notes_en": "CagriSema Phase III REDEFINE trials: results expected 2025, potential approval 2026", "notes_de": "CagriSema Phase-III-REDEFINE-Studien: Ergebnisse 2025, mögliche Zulassung 2026"},
        "manufacturer": "Novo Nordisk",
        "molecular_weight": "~3900 Da", "amino_acid_count": "~37", "half_life": "~7 days",
        "storage_conditions": {"en": "Refrigerate at 2-8°C", "de": "Bei 2-8°C kühlen"},
        "amino_acid_sequence": "Modified amylin analog with acylation (proprietary)",
        "reconstitution_info": {"preparation_en": "Pre-filled pen", "preparation_de": "Fertigpen", "storage_temperature": "2-8°C", "shelf_life_unopened": "TBD", "shelf_life_reconstituted": "TBD", "light_sensitive": True, "solvent": "Pre-filled solution"},
        "application_goals": [{"goal_en": "Fat Loss", "goal_de": "Fettverbrennung", "relevance": "primary"}, {"goal_en": "Metabolic Health", "goal_de": "Stoffwechselgesundheit", "relevance": "primary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
    # ── MUSCULOSKELETAL ──────────────────────────────────────────
    {
        "name": "Follistatin 344",
        "slug": "follistatin-344",
        "category": "Myostatin Inhibitor",
        "description": {
            "en": "Follistatin 344 is a recombinant form of the naturally occurring glycoprotein follistatin, which binds and neutralizes activin A, myostatin, and other TGF-beta superfamily members. By inhibiting myostatin (the primary negative regulator of muscle growth), follistatin promotes significant muscle hypertrophy. It has applications in muscle-wasting diseases, gene therapy, and sports science research.",
            "de": "Follistatin 344 ist eine rekombinante Form des natürlich vorkommenden Glykoproteins Follistatin, das Activin A, Myostatin und andere TGF-beta-Superfamilienmitglieder bindet und neutralisiert. Durch Myostatin-Hemmung fördert Follistatin signifikante Muskelhypertrophie."
        },
        "mechanism_of_action": {"en": "Binds and sequesters myostatin, activin A, and GDF-11 with high affinity, preventing their interaction with ActRIIB receptors. This removes the 'brake' on muscle growth mediated by the myostatin-Smad2/3 pathway, resulting in muscle fiber hypertrophy and hyperplasia.", "de": "Bindet und neutralisiert Myostatin, Activin A und GDF-11 mit hoher Affinität. Dies entfernt die 'Bremse' des Muskelwachstums und führt zu Muskelfaser-Hypertrophie und -Hyperplasie."},
        "indications": [
            {"condition_en": "Muscle-wasting diseases", "condition_de": "Muskelabbau-Erkrankungen", "description_en": "Duchenne muscular dystrophy, sarcopenia", "description_de": "Duchenne-Muskeldystrophie, Sarkopenie"},
            {"condition_en": "Inclusion body myositis", "condition_de": "Einschlusskörper-Myositis", "description_en": "Gene therapy trials (AAV-follistatin)", "description_de": "Gentherapie-Studien (AAV-Follistatin)"},
            {"condition_en": "Age-related muscle loss", "condition_de": "Altersbedingter Muskelverlust", "description_en": "Preventing sarcopenia in elderly", "description_de": "Prävention von Sarkopenie bei Älteren"}
        ],
        "benefits": [{"benefit_en": "Powerful myostatin inhibition", "benefit_de": "Starke Myostatin-Hemmung"}, {"benefit_en": "Significant muscle mass increase", "benefit_de": "Signifikante Muskelmasseerhöhung"}, {"benefit_en": "Gene therapy applications (AAV-FS344)", "benefit_de": "Gentherapie-Anwendungen (AAV-FS344)"}, {"benefit_en": "Potential for muscle disease treatment", "benefit_de": "Potential für Muskelerkrankungsbehandlung"}],
        "side_effects": [
            {"name_en": "Reproductive effects", "name_de": "Reproduktive Effekte", "severity": "moderate", "frequency": "common", "description_en": "Activin binding affects FSH and fertility", "description_de": "Activin-Bindung beeinflusst FSH und Fruchtbarkeit"},
            {"name_en": "Injection site reactions", "name_de": "Reaktionen an der Injektionsstelle", "severity": "mild", "frequency": "common", "description_en": "Local inflammation", "description_de": "Lokale Entzündung"},
            {"name_en": "Immune response", "name_de": "Immunantwort", "severity": "moderate", "frequency": "uncommon", "description_en": "Antibody formation against protein", "description_de": "Antikörperbildung gegen Protein"},
            {"name_en": "Tendon/ligament risk", "name_de": "Sehnen-/Bandrisiko", "severity": "moderate", "frequency": "uncommon", "description_en": "Rapid muscle growth may stress connective tissue", "description_de": "Schnelles Muskelwachstum kann Bindegewebe belasten"},
            {"name_en": "Unknown long-term effects", "name_de": "Unbekannte Langzeiteffekte", "severity": "moderate", "frequency": "rare", "description_en": "Limited human safety data", "description_de": "Begrenzte humane Sicherheitsdaten"}
        ],
        "dosage": {"starting_dose": "100 mcg", "maintenance_dose": "100-300 mcg", "frequency_en": "Daily or every other day", "frequency_de": "Täglich oder jeden zweiten Tag", "route_en": "Subcutaneous injection", "route_de": "Subkutane Injektion", "notes_en": "Very limited human dosing data available", "notes_de": "Sehr begrenzte humane Dosierungsdaten verfügbar"},
        "contraindications": [{"en": "Pregnancy/breastfeeding (teratogenic potential)", "de": "Schwangerschaft/Stillzeit (teratogenes Potential)"}, {"en": "Active hormone-sensitive cancers", "de": "Aktive hormonsensitive Krebserkrankungen"}, {"en": "Fertility intentions (activin effects)", "de": "Kinderwunsch (Activin-Effekte)"}],
        "drug_interactions": ["Anabolic agents (potential synergy)", "Hormonal contraceptives (interference)", "Immunosuppressants"],
        "research_status": {"phase": "Phase I/II", "fda_approved": False, "ema_approved": False, "notes_en": "AAV-follistatin gene therapy Phase I/II for IBM and Becker MD completed", "notes_de": "AAV-Follistatin-Gentherapie Phase I/II für IBM und Becker-MD abgeschlossen"},
        "manufacturer": "Research compound / Nationwide Children's Hospital (gene therapy)",
        "molecular_weight": "~38000 Da (full protein)", "amino_acid_count": "344", "half_life": "Hours (protein)",
        "storage_conditions": {"en": "Store at -20°C", "de": "Bei -20°C lagern"},
        "amino_acid_sequence": "Full-length follistatin isoform FS344 (315 aa mature + signal peptide)",
        "reconstitution_info": {"preparation_en": "Reconstitute lyophilized protein in sterile water", "preparation_de": "Lyophilisiertes Protein in sterilem Wasser rekonstituieren", "storage_temperature": "-20°C", "shelf_life_unopened": "12 months", "shelf_life_reconstituted": "7 days at 4°C", "light_sensitive": True, "solvent": "Sterile water for injection"},
        "application_goals": [{"goal_en": "Muscle Building", "goal_de": "Muskelaufbau", "relevance": "primary"}, {"goal_en": "Anti-Aging", "goal_de": "Anti-Aging", "relevance": "secondary"}],
        "created_at": NOW, "updated_at": NOW, "generated_by": "seed-data"
    },
]


def main():
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    col = db["peptides"]

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
