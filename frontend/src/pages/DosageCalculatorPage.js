import React, { useState, useMemo } from 'react';
import { Helmet } from 'react-helmet-async';
import { motion, AnimatePresence } from 'framer-motion';
import { Calculator, AlertTriangle, CheckCircle2, Syringe } from 'lucide-react';
import { Card, CardContent } from '../components/ui/card';

// ─── Pill toggle button ───────────────────────────────────────────────────────
function Opt({ label, active, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`px-3 py-1.5 rounded-lg text-sm font-medium border transition-all duration-150 ${
        active
          ? 'bg-primary text-primary-foreground border-primary'
          : 'bg-transparent text-muted-foreground border-border hover:border-primary/50 hover:text-foreground'
      }`}
    >
      {label}
    </button>
  );
}

// ─── Input section ────────────────────────────────────────────────────────────
function Section({ label, options, value, onChange, customVal, onCustomVal, unit }) {
  return (
    <div className="space-y-2">
      <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">{label}</p>
      <div className="flex flex-wrap gap-1.5">
        {options.map(o => (
          <Opt key={o.v} label={o.l} active={value === o.v} onClick={() => onChange(o.v)} />
        ))}
        <Opt label="Other" active={value === 'custom'} onClick={() => onChange('custom')} />
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
            <div className="flex items-center gap-2 pt-1">
              <input
                type="number"
                min="0"
                step="any"
                placeholder="0"
                value={customVal}
                onChange={e => onCustomVal(e.target.value)}
                className="w-28 px-3 py-1.5 rounded-lg text-sm border border-border bg-background text-foreground focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary/30"
              />
              {unit && <span className="text-sm text-muted-foreground">{unit}</span>}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// ─── Syringe ruler ────────────────────────────────────────────────────────────
function Ruler({ units, max }) {
  const pct = Math.min(units / max, 1) * 100;
  const step = max <= 30 ? 5 : max <= 50 ? 10 : 20;
  const labels = Array.from({ length: Math.floor(max / step) + 1 }, (_, i) => i * step);

  return (
    <div className="space-y-1.5">
      <div className="relative h-7 rounded-lg overflow-hidden bg-secondary/50 border border-border">
        <motion.div
          className="absolute inset-y-0 left-0 bg-primary rounded-lg"
          animate={{ width: `${pct}%` }}
          transition={{ type: 'spring', stiffness: 140, damping: 22 }}
        />
        {labels.map(i => (
          <div
            key={i}
            className="absolute top-0 bottom-0 w-px bg-border/40"
            style={{ left: `${(i / max) * 100}%` }}
          />
        ))}
        <motion.div
          className="absolute top-0 bottom-0 w-0.5 bg-white/80"
          animate={{ left: `${pct}%` }}
          transition={{ type: 'spring', stiffness: 140, damping: 22 }}
        />
      </div>
      <div className="relative h-3">
        {labels.map(i => (
          <span
            key={i}
            className="absolute text-[10px] text-muted-foreground -translate-x-1/2"
            style={{ left: `${(i / max) * 100}%` }}
          >
            {i}
          </span>
        ))}
      </div>
    </div>
  );
}

// ─── Page ─────────────────────────────────────────────────────────────────────
const SYRINGES = [
  { v: '0.3/30', l: '0.3 ml · 30u' },
  { v: '0.5/50', l: '0.5 ml · 50u' },
  { v: '1.0/100', l: '1.0 ml · 100u' },
];
const VIALS = [
  { v: '5', l: '5 mg' }, { v: '10', l: '10 mg' },
  { v: '15', l: '15 mg' }, { v: '20', l: '20 mg' },
];
const WATER = [
  { v: '1', l: '1 ml' }, { v: '2', l: '2 ml' },
  { v: '3', l: '3 ml' }, { v: '5', l: '5 ml' },
];
const DOSES = [
  { v: '0.05', l: '50 mcg' }, { v: '0.1', l: '100 mcg' },
  { v: '0.25', l: '250 mcg' }, { v: '0.5', l: '500 mcg' },
  { v: '1', l: '1 mg' }, { v: '2.5', l: '2.5 mg' },
  { v: '5', l: '5 mg' }, { v: '10', l: '10 mg' },
];

export default function DosageCalculatorPage() {
  const [syringe, setSyringe] = useState('0.5/50');
  const [vial, setVial] = useState('10');
  const [cvial, setCvial] = useState('');
  const [water, setWater] = useState('2');
  const [cwater, setCwater] = useState('');
  const [dose, setDose] = useState('1');
  const [cdose, setCdose] = useState('');

  const r = useMemo(() => {
    const [svol, sunits] = syringe.split('/').map(Number);
    const vmg = vial === 'custom' ? parseFloat(cvial) : parseFloat(vial);
    const wml = water === 'custom' ? parseFloat(cwater) : parseFloat(water);
    const dmg = dose === 'custom' ? parseFloat(cdose) : parseFloat(dose);
    if (!vmg || !wml || !dmg || vmg <= 0 || wml <= 0 || dmg <= 0) return null;
    const conc = vmg / wml;
    const vol = dmg / conc;
    const units = (vol / svol) * sunits;
    return { conc, vol, units: Math.round(units * 10) / 10, sunits, svol, fits: vol <= svol };
  }, [syringe, vial, cvial, water, cwater, dose, cdose]);

  return (
    <div className="min-h-screen">
      <Helmet>
        <title>Peptide Dosage Calculator — PeptideDB</title>
        <meta name="description" content="Calculate exact syringe units for reconstituted peptides." />
      </Helmet>

      <div className="max-w-2xl mx-auto px-4 sm:px-6 py-10 space-y-5">

        {/* Header */}
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-primary/10 border border-primary/20 flex items-center justify-center">
            <Calculator className="w-4 h-4 text-primary" />
          </div>
          <div>
            <h1 className="text-xl font-bold" style={{ fontFamily: 'var(--pdb-font-display)' }}>Dosage Calculator</h1>
            <p className="text-xs text-muted-foreground">Peptide reconstitution · syringe units</p>
          </div>
        </div>

        {/* Inputs */}
        <Card>
          <CardContent className="p-5 space-y-5">
            <Section label="Syringe" options={SYRINGES} value={syringe} onChange={setSyringe} customVal="" onCustomVal={() => {}} />
            <div className="h-px bg-border/50" />
            <Section label="Peptide vial" options={VIALS} value={vial} onChange={setVial} customVal={cvial} onCustomVal={setCvial} unit="mg" />
            <div className="h-px bg-border/50" />
            <Section label="Bacteriostatic water" options={WATER} value={water} onChange={setWater} customVal={cwater} onCustomVal={setCwater} unit="ml" />
            <div className="h-px bg-border/50" />
            <Section label="Desired dose" options={DOSES} value={dose} onChange={setDose} customVal={cdose} onCustomVal={setCdose} unit="mg" />
          </CardContent>
        </Card>

        {/* Result */}
        <AnimatePresence mode="wait">
          {r ? (
            <motion.div key="res" initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} transition={{ duration: 0.25 }}>
              <Card className={r.fits ? 'border-primary/25' : 'border-destructive/30'}>
                <CardContent className="p-5 space-y-4">
                  {/* Main number */}
                  <div className="flex items-end justify-between">
                    <div>
                      <p className="text-xs text-muted-foreground mb-1">Pull your syringe to</p>
                      <div className="flex items-baseline gap-1.5">
                        <span
                          className={`text-5xl font-bold tabular-nums ${r.fits ? 'text-primary' : 'text-destructive'}`}
                          style={{ fontFamily: 'var(--pdb-font-display)' }}
                        >
                          {r.fits ? r.units : '—'}
                        </span>
                        {r.fits && <span className="text-base text-muted-foreground font-medium">units</span>}
                      </div>
                      <p className="text-xs text-muted-foreground mt-1">
                        {r.fits
                          ? `${(r.vol * 1000).toFixed(1)} µl  ·  ${r.conc.toFixed(2)} mg/ml`
                          : 'Dose exceeds syringe — use larger syringe or split'}
                      </p>
                    </div>
                    <div className={`flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${
                      r.fits
                        ? 'bg-green-500/10 text-green-500 border-green-500/20'
                        : 'bg-destructive/10 text-destructive border-destructive/20'
                    }`}>
                      {r.fits ? <><CheckCircle2 className="w-3 h-3" /> OK</> : <><AlertTriangle className="w-3 h-3" /> Error</>}
                    </div>
                  </div>

                  {/* Ruler */}
                  {r.fits && (
                    <div>
                      <div className="flex items-center gap-1.5 mb-2">
                        <Syringe className="w-3 h-3 text-muted-foreground" />
                        <span className="text-xs text-muted-foreground">0 – {r.sunits} units ({r.svol} ml)</span>
                      </div>
                      <Ruler units={r.units} max={r.sunits} />
                    </div>
                  )}
                </CardContent>
              </Card>
            </motion.div>
          ) : (
            <motion.div key="empty" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
              <div className="flex items-center justify-center gap-2 py-6 text-muted-foreground/40 text-sm border border-dashed border-border/50 rounded-xl">
                <Calculator className="w-4 h-4" />
                Select all options to calculate
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Disclaimer */}
        <p className="text-xs text-muted-foreground/60 text-center leading-relaxed">
          For research purposes only. Not medical advice. Always verify calculations independently.
        </p>

      </div>
    </div>
  );
}

