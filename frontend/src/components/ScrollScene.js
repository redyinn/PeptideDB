import React from 'react';
import PeptideSequence from './PeptideSequence';

const easeOut  = t => 1 - Math.pow(1 - t, 3);
const easeInOut = t => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;

const headlineStyle = {
  fontFamily: 'var(--pdb-font-display)',
  fontSize: 'clamp(40px, 6vw, 80px)',
  fontWeight: 500,
  letterSpacing: '-0.025em',
  lineHeight: 1.02,
  margin: 0,
  color: 'var(--pdb-ink)',
  maxWidth: '20ch',
  textWrap: 'balance',
};

function Panel({ children, opacity, row }) {
  return (
    <div style={{
      position: 'absolute', inset: 0,
      display: 'flex', flexDirection: row ? 'row' : 'column',
      alignItems: 'center', justifyContent: 'center',
      gap: row ? 80 : 0,
      padding: '0 32px', textAlign: 'center',
      opacity,
      transform: `translateY(${(1 - Math.max(0, opacity)) * 14}px)`,
      pointerEvents: 'none',
      transition: 'none',
    }}>{children}</div>
  );
}

function BigStat({ n, label, comma }) {
  const display = comma ? n.toLocaleString('en-US') : n;
  return (
    <div style={{ textAlign: 'center' }}>
      <div style={{
        fontFamily: 'var(--pdb-font-display)',
        fontSize: 'clamp(56px, 7vw, 96px)',
        fontWeight: 500, color: 'var(--pdb-ink)', lineHeight: 1,
        letterSpacing: '-0.02em',
        fontVariationSettings: '"opsz" 144',
        fontVariantNumeric: 'tabular-nums',
      }}>{display}</div>
      <div style={{
        fontSize: 13, color: 'var(--pdb-ink-3)', marginTop: 12,
        textTransform: 'uppercase', letterSpacing: '0.12em', fontWeight: 600,
      }}>{label}</div>
    </div>
  );
}

export default function ScrollScene() {
  const sectionRef = React.useRef(null);
  const rafRef     = React.useRef(0);
  const targetRef  = React.useRef(0);
  const currentRef = React.useRef(0);
  const [progress, setProgress] = React.useState(0);

  React.useEffect(() => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) { setProgress(1); return; }

    const tick = () => {
      const t = targetRef.current;
      const c = currentRef.current;
      const next = c + (t - c) * 0.12;
      currentRef.current = Math.abs(t - next) < 0.0005 ? t : next;
      setProgress(currentRef.current);
      if (currentRef.current !== t) {
        rafRef.current = requestAnimationFrame(tick);
      } else {
        rafRef.current = 0;
      }
    };

    const onScroll = () => {
      const el = sectionRef.current;
      if (!el) return;
      const r = el.getBoundingClientRect();
      const total = r.height - window.innerHeight;
      const scrolled = -r.top;
      targetRef.current = Math.max(0, Math.min(1, scrolled / total));
      if (!rafRef.current) rafRef.current = requestAnimationFrame(tick);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    return () => {
      window.removeEventListener('scroll', onScroll);
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  }, []);

  const seg = (start, end) => Math.max(0, Math.min(1, (progress - start) / (end - start)));

  const p1 = easeOut(seg(0.00, 0.18)) - easeOut(seg(0.22, 0.36));
  const p2 = easeOut(seg(0.30, 0.46)) - easeOut(seg(0.54, 0.66));
  const p3 = easeOut(seg(0.62, 0.78));

  const scale    = 0.88 + easeInOut(progress) * 0.45;
  const glyphX   = (progress - 0.5) * 60;
  const seqProg  = easeOut(seg(0.00, 0.55));
  const rot      = (progress - 0.5) * 16;

  const tick = (target) => Math.round(target * easeOut(seg(0.36, 0.66)));

  return (
    <section ref={sectionRef} style={{ position: 'relative', height: '220vh', background: 'var(--pdb-page)' }}>
      <div style={{
        position: 'sticky', top: 0, height: '100vh', overflow: 'hidden',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
      }}>
        {/* Background glow */}
        <div style={{
          position: 'absolute', inset: 0,
          background: `radial-gradient(circle at 50% ${50 - progress * 8}%, rgba(62,107,94,${(0.04 + progress * 0.10).toFixed(2)}), transparent 55%)`,
          pointerEvents: 'none',
        }} />

        {/* Centered peptide sequence with fly-in */}
        <div style={{
          position: 'absolute', left: '50%', top: '50%',
          transform: `translate(-50%, -50%) translateX(${glyphX.toFixed(1)}px) scale(${scale.toFixed(3)}) rotate(${rot.toFixed(1)}deg)`,
          willChange: 'transform',
        }}>
          <PeptideSequence size={380} progress={seqProg} flyIn />
        </div>

        {/* Panel 1 */}
        <Panel opacity={Math.max(0, p1)}>
          <div className="pdb-overline" style={{ marginBottom: 18, color: 'var(--pdb-accent)' }}>Built for the evidence</div>
          <h2 style={headlineStyle}>Every claim, traced to a paper.</h2>
        </Panel>

        {/* Panel 2 — stat counters */}
        <Panel opacity={Math.max(0, p2)} row>
          <BigStat n={tick(48)}   label="Peptides indexed" />
          <BigStat n={tick(4212)} label="Papers parsed" comma />
          <BigStat n={tick(318)}  label="Active trials" />
        </Panel>

        {/* Panel 3 */}
        <Panel opacity={p3}>
          <h2 style={{ ...headlineStyle, fontSize: 'clamp(36px, 5vw, 64px)' }}>
            Refreshed every Sunday at 02:00 UTC.
          </h2>
          <p style={{ fontSize: 17, color: 'var(--pdb-ink-3)', marginTop: 16, fontFamily: 'var(--pdb-font-body)' }}>
            From PubMed and ClinicalTrials.gov, automatically.
          </p>
        </Panel>

        {/* Hairline progress bar */}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: 1, background: 'var(--pdb-line-2)' }}>
          <div style={{ height: '100%', width: `${progress * 100}%`, background: 'var(--pdb-accent)', transition: 'none' }} />
        </div>
      </div>
    </section>
  );
}
