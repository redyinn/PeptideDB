import React, { useState, useMemo } from 'react';
import { Helmet } from 'react-helmet-async';
import { motion, AnimatePresence } from 'framer-motion';
import { Calculator, AlertTriangle, CheckCircle2, Info, Syringe, FlaskConical, Droplets, Pill } from 'lucide-react';
import { Card, CardContent } from '../components/ui/card';

// ─── Option Group ─────────────────────────────────────────────────────────────
function OptionGroup({ label, icon: Icon, options, value, onChange, customValue, onCustomChange, unit }) {
  return (
    <div className="space-y-3">
      <div className="flex items-center gap-2">
        <Icon className="w-4 h-4 text-primary" />
        <span className="text-sm font-semibold text-foreground" style={{ fontFamily: 'Space Grotesk' }}>{label}</span>
      </div>
      <div className="flex flex-wrap gap-2">
        {options.map(opt => {
          const isSelected = value === opt.value;
          return (
            <button
              key={opt.value}
              onClick={() => onChange(opt.value)}
              className={`px-3 py-1.5 rounded-lg text-sm font-medium border transition-all duration-150 ${
                isSelected
                  ? 'bg-primary text-primary-foreground border-primary shadow-sm'
                  : 'bg-secondary/50 text-muted-foreground border-border hover:border-primary/40 hover:text-foreground'
              }`}
            >
              {opt.label}
            </button>
          );
        })}
        <button
          onClick={() => onChange('custom')}
          className={`px-3 py-1.5 rounded-lg text-sm font-medium border transition-all duration-150 ${
            value === 'custom'
              ? 'bg-primary text-primary-foreground border-primary shadow-sm'
              : 'bg-secondary/50 text-muted-foreground border-border hover:border-primary/40 hover:text-foreground'
          }`}
        >
          Other
        </button>
      </div>
      <AnimatePresence>
        {value === 'custom' && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.15 }}
            className="overflow-hidden"
          >
            <div className="flex items-center gap-2">
              <input
                type="number"
                min="0"
                step="any"
                placeholder="Enter value"
                value={customValue}
                onChange={e => onCustomChange(e.target.value)}
                className="w-36 px-3 py-1.5 rounded-lg text-sm border border-border bg-background text-foreground focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary/30 transition-colors"
              />
              {unit && <span className="text-sm text-muted-foreground">{unit}</span>}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// ─── Syringe Ruler ────────────────────────────────────────────────────────────
function SyringeRuler({ units, maxUnits, valid }) {
  const pct = Math.min(units / maxUnits, 1) * 100;
  const ticks = Array.from({ length: maxUnits + 1 }, (_, i) => i);
  const labelInterval = maxUnits <= 30 ? 5 : maxUnits <= 50 ? 10 : 20;

  return (
    <div className="space-y-2">
      {/* Ruler bar */}
      <div className="relative h-8 rounded-lg overflow-hidden bg-secondary/60 border border-border">
        {/* Fill */}
        <motion.div
          className={`absolute inset-y-0 left-0 rounded-lg transition-all ${valid ? 'bg-primary' : 'bg-destructive/60'}`}
          initial={{ width: 0 }}
          animate={{ width: `${pct}%` }}
          transition={{ type: 'spring', stiffness: 120, damping: 20 }}
        />
        {/* Tick marks */}
        <div className="absolute inset-0 flex">
          {ticks.map(i => {
            const pos = (i / maxUnits) * 100;
            const isMajor = i % labelInterval === 0;
            return (
              <div
                key={i}
                className="absolute top-0 bottom-0"
                style={{ left: `${pos}%` }}
              >
                <div className={`w-px h-full ${isMajor ? 'bg-border/80' : 'bg-border/30'}`} />
              </div>
            );
          })}
        </div>
        {/* Cursor line */}
        <AnimatePresence>
          {units > 0 && (
            <motion.div
              className="absolute top-0 bottom-0 w-0.5 bg-white/90 shadow-lg"
              initial={{ left: '0%' }}
              animate={{ left: `${pct}%` }}
              transition={{ type: 'spring', stiffness: 120, damping: 20 }}
            />
          )}
        </AnimatePresence>
      </div>
      {/* Labels */}
      <div className="relative h-4 text-xs text-muted-foreground select-none">
        {ticks.filter(i => i % labelInterval === 0).map(i => (
          <span
            key={i}
            className="absolute -translate-x-1/2"
            style={{ left: `${(i / maxUnits) * 100}%` }}
          >
            {i}
          </span>
        ))}
      </div>
    </div>
  );
}

// ─── Main Page ────────────────────────────────────────────────────────────────
const SYRINGE_OPTIONS = [
  { value: '0.3/30', label: '0.3 ml · 30u' },
  { value: '0.5/50', label: '0.5 ml · 50u' },
  { value: '1.0/100', label: '1.0 ml · 100u' },
];

const VIAL_OPTIONS = [
  { value: '5', label: '5 mg' },
  { value: '10', label: '10 mg' },
  { value: '15', label: '15 mg' },
  { value: '20', label: '20 mg' },
];

const WATER_OPTIONS = [
  { value: '1', label: '1 ml' },
  { value: '2', label: '2 ml' },
  { value: '3', label: '3 ml' },
  { value: '5', label: '5 ml' },
];

const DOSE_OPTIONS = [
  { value: '0.05', label: '50 mcg' },
  { value: '0.1', label: '100 mcg' },
  { value: '0.25', label: '250 mcg' },
  { value: '0.5', label: '500 mcg' },
  { value: '1', label: '1 mg' },
  { value: '2.5', label: '2.5 mg' },
  { value: '5', label: '5 mg' },
  { value: '10', label: '10 mg' },
];

export default function DosageCalculatorPage() {
  const [syringe, setSyringe] = useState('0.5/50');
  const [vial, setVial] = useState('10');
  const [customVial, setCustomVial] = useState('');
  const [water, setWater] = useState('2');
  const [customWater, setCustomWater] = useState('');
  const [dose, setDose] = useState('1');
  const [customDose, setCustomDose] = useState('');

  const calc = useMemo(() => {
    const [syringeVol, syringeUnits] = syringe.split('/').map(Number);

    const vialMg = vial === 'custom' ? parseFloat(customVial) : parseFloat(vial);
    const waterMl = water === 'custom' ? parseFloat(customWater) : parseFloat(water);
    const doseMg = dose === 'custom' ? parseFloat(customDose) : parseFloat(dose);

    if (!vialMg || !waterMl || !doseMg || vialMg <= 0 || waterMl <= 0 || doseMg <= 0) {
      return { ready: false };
    }

    const concentration = vialMg / waterMl; // mg/ml
    const volumeNeeded = doseMg / concentration; // ml
    const units = (volumeNeeded / syringeVol) * syringeUnits;
    const fits = volumeNeeded <= syringeVol;

    return {
      ready: true,
      concentration,
      volumeNeeded,
      units,
      syringeUnits,
      syringeVol,
      fits,
      roundedUnits: Math.round(units * 10) / 10,
    };
  }, [syringe, vial, customVial, water, customWater, dose, customDose]);

  return (
    <div className="min-h-screen">
      <Helmet>
        <title>Peptide Dosage Calculator — PeptideDB</title>
        <meta name="description" content="Calculate exact injection volume for reconstituted peptides. Enter your vial size, bacteriostatic water, and desired dose to get precise syringe units." />
      </Helmet>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">

        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
          className="space-y-3"
        >
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-primary/10 border border-primary/20 flex items-center justify-center">
              <Calculator className="w-5 h-5 text-primary" />
            </div>
            <div>
              <h1 className="text-2xl font-bold" style={{ fontFamily: 'Space Grotesk' }}>Peptide Dosage Calculator</h1>
              <p className="text-sm text-muted-foreground">Reconstitution · Injection volume · Syringe units</p>
            </div>
          </div>

          {/* Disclaimer */}
          <div className="flex items-start gap-2.5 px-4 py-3 rounded-xl bg-amber-500/8 border border-amber-500/20 text-sm text-amber-700 dark:text-amber-400">
            <AlertTriangle className="w-4 h-4 mt-0.5 shrink-0" />
            <span>
              For research purposes only. Consult a qualified healthcare professional before any administration.
              Always verify calculations independently.
            </span>
          </div>
        </motion.div>

        {/* Calculator inputs */}
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.08 }}
        >
          <Card className="border-border">
            <CardContent className="p-6 space-y-7">

              {/* Row 1: Syringe + Vial */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-7">
                <OptionGroup
                  label="Syringe volume"
                  icon={Syringe}
                  options={SYRINGE_OPTIONS}
                  value={syringe}
                  onChange={setSyringe}
                  customValue=""
                  onCustomChange={() => {}}
                />
                <OptionGroup
                  label="Peptide vial quantity"
                  icon={FlaskConical}
                  options={VIAL_OPTIONS}
                  value={vial}
                  onChange={setVial}
                  customValue={customVial}
                  onCustomChange={setCustomVial}
                  unit="mg"
                />
              </div>

              <div className="h-px bg-border/50" />

              {/* Row 2: Water + Dose */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-7">
                <OptionGroup
                  label="Bacteriostatic water"
                  icon={Droplets}
                  options={WATER_OPTIONS}
                  value={water}
                  onChange={setWater}
                  customValue={customWater}
                  onCustomChange={setCustomWater}
                  unit="ml"
                />
                <OptionGroup
                  label="Desired dose"
                  icon={Pill}
                  options={DOSE_OPTIONS}
                  value={dose}
                  onChange={setDose}
                  customValue={customDose}
                  onCustomChange={setCustomDose}
                  unit="mg"
                />
              </div>
            </CardContent>
          </Card>
        </motion.div>

        {/* Result */}
        <AnimatePresence mode="wait">
          {calc.ready && (
            <motion.div
              key="result"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 6 }}
              transition={{ duration: 0.35 }}
            >
              <Card className={`border ${calc.fits ? 'border-primary/30 bg-primary/3' : 'border-destructive/30 bg-destructive/3'}`}>
                <CardContent className="p-6 space-y-5">

                  {/* Main result */}
                  <div className="flex items-start justify-between gap-4 flex-wrap">
                    <div>
                      <p className="text-xs text-muted-foreground uppercase tracking-widest font-medium mb-1">
                        Pull your syringe to
                      </p>
                      <div className="flex items-baseline gap-2">
                        <span
                          className={`text-5xl font-bold tabular-nums ${calc.fits ? 'text-primary' : 'text-destructive'}`}
                          style={{ fontFamily: 'Space Grotesk' }}
                        >
                          {calc.fits ? calc.roundedUnits : '—'}
                        </span>
                        {calc.fits && (
                          <span className="text-lg font-medium text-muted-foreground">units</span>
                        )}
                      </div>
                      {calc.fits ? (
                        <p className="text-sm text-muted-foreground mt-1">
                          = {(calc.volumeNeeded * 1000).toFixed(1)} µl &nbsp;·&nbsp; {calc.volumeNeeded.toFixed(3)} ml
                        </p>
                      ) : (
                        <p className="text-sm text-destructive mt-1">
                          Dose exceeds syringe capacity — use a larger syringe or split the dose
                        </p>
                      )}
                    </div>
                    <div className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-medium border ${
                      calc.fits
                        ? 'bg-green-500/10 text-green-500 border-green-500/20'
                        : 'bg-destructive/10 text-destructive border-destructive/20'
                    }`}>
                      {calc.fits
                        ? <><CheckCircle2 className="w-3.5 h-3.5" /> Fits in syringe</>
                        : <><AlertTriangle className="w-3.5 h-3.5" /> Dose too large</>
                      }
                    </div>
                  </div>

                  {/* Syringe ruler */}
                  {calc.fits && (
                    <div className="space-y-1.5">
                      <p className="text-xs text-muted-foreground">
                        Syringe: 0 – {calc.syringeUnits} units ({calc.syringeVol} ml)
                      </p>
                      <SyringeRuler
                        units={calc.roundedUnits}
                        maxUnits={calc.syringeUnits}
                        valid={calc.fits}
                      />
                    </div>
                  )}

                  {/* Info pills */}
                  <div className="flex flex-wrap gap-2 pt-1">
                    <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-secondary/60 border border-border text-xs text-muted-foreground">
                      <Info className="w-3 h-3" />
                      <span>Concentration: <strong className="text-foreground">{calc.concentration.toFixed(2)} mg/ml</strong></span>
                    </div>
                    <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-secondary/60 border border-border text-xs text-muted-foreground">
                      <Info className="w-3 h-3" />
                      <span>Volume needed: <strong className="text-foreground">{calc.volumeNeeded.toFixed(3)} ml</strong></span>
                    </div>
                    <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-secondary/60 border border-border text-xs text-muted-foreground">
                      <Info className="w-3 h-3" />
                      <span>Units to pull: <strong className="text-foreground">{calc.roundedUnits}u / {calc.syringeUnits}u total</strong></span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          )}

          {!calc.ready && (
            <motion.div
              key="placeholder"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              <Card className="border-dashed border-border/60">
                <CardContent className="p-6 flex items-center justify-center gap-3 text-muted-foreground/50">
                  <Calculator className="w-5 h-5" />
                  <span className="text-sm">Select all options above to calculate</span>
                </CardContent>
              </Card>
            </motion.div>
          )}
        </AnimatePresence>

        {/* How it works */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.4, delay: 0.2 }}
        >
          <Card className="border-border/60">
            <CardContent className="p-6 space-y-3">
              <h2 className="text-sm font-semibold flex items-center gap-2" style={{ fontFamily: 'Space Grotesk' }}>
                <Info className="w-4 h-4 text-primary" />
                How reconstitution math works
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs text-muted-foreground">
                <div className="space-y-1">
                  <p className="font-medium text-foreground">1. Concentration</p>
                  <p>Vial (mg) ÷ BAC water (ml) = mg/ml</p>
                  <p className="font-mono bg-secondary/50 rounded px-2 py-1 text-foreground">10 mg ÷ 2 ml = 5 mg/ml</p>
                </div>
                <div className="space-y-1">
                  <p className="font-medium text-foreground">2. Volume needed</p>
                  <p>Dose (mg) ÷ concentration (mg/ml) = ml</p>
                  <p className="font-mono bg-secondary/50 rounded px-2 py-1 text-foreground">1 mg ÷ 5 mg/ml = 0.2 ml</p>
                </div>
                <div className="space-y-1">
                  <p className="font-medium text-foreground">3. Syringe units</p>
                  <p>(Volume ÷ syringe vol) × max units</p>
                  <p className="font-mono bg-secondary/50 rounded px-2 py-1 text-foreground">(0.2 ÷ 0.5) × 50 = 20u</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>

      </div>
    </div>
  );
}
