import React from 'react';

const RESIDUES = [
  { x: 12, y: 50, l: 'G' },
  { x: 22, y: 38, l: 'L' },
  { x: 32, y: 28, l: 'P' },
  { x: 44, y: 24, l: 'K' },
  { x: 56, y: 28, l: 'E' },
  { x: 66, y: 38, l: 'A' },
  { x: 72, y: 50, l: 'R' },
  { x: 70, y: 62, l: 'S' },
  { x: 60, y: 70, l: 'T' },
  { x: 48, y: 72, l: 'F' },
  { x: 36, y: 70, l: 'Y' },
  { x: 26, y: 62, l: 'I' },
  { x: 22, y: 50, l: 'V' },
];

const easeOut = t => 1 - Math.pow(1 - t, 3);

export default function PeptideSequence({ size = 380, progress = 1, flyIn = false }) {
  const total = RESIDUES.length;
  const bondsShown = easeOut(Math.max(0, Math.min(1, (progress - 0.1) / 0.7)));
  const residuesShown = Math.max(0, Math.min(1, progress));

  const pathD = RESIDUES.map((r, i) => `${i === 0 ? 'M' : 'L'} ${r.x} ${r.y}`).join(' ');
  const dashTotal = 600;
  const dashOffset = dashTotal * (1 - bondsShown);

  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 100 100"
      xmlns="http://www.w3.org/2000/svg"
      style={{ display: 'block', overflow: 'visible' }}
      aria-hidden="true"
    >
      <defs>
        <radialGradient id="pdb-seq-glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="rgba(26,26,26,0.08)" />
          <stop offset="70%" stopColor="rgba(26,26,26,0)" />
        </radialGradient>
      </defs>

      <circle cx="50" cy="50" r="48" fill="url(#pdb-seq-glow)" />
      <circle cx="48" cy="50" r="34" fill="none" stroke="var(--pdb-line-2, #E5E5E2)" strokeWidth="0.3" strokeDasharray="0.6 1.4" />

      <path
        d={pathD}
        fill="none"
        stroke="var(--pdb-accent, #1A1A1A)"
        strokeWidth="0.6"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeDasharray={dashTotal}
        strokeDashoffset={dashOffset}
        style={{ transition: 'none' }}
      />

      {RESIDUES.map((r, i) => {
        const sliceStart = (i / total) * 0.7;
        const sliceEnd   = sliceStart + 0.35;
        const local = Math.max(0, Math.min(1, (residuesShown - sliceStart) / (sliceEnd - sliceStart)));
        const eased = easeOut(local);

        const dx = r.x - 48;
        const dy = r.y - 50;
        const len = Math.max(1, Math.sqrt(dx * dx + dy * dy));
        const ndx = dx / len, ndy = dy / len;
        const offset = flyIn ? (1 - eased) * 60 : 0;
        const tx = r.x + ndx * offset;
        const ty = r.y + ndy * offset;

        const opacity = eased;
        const scale = 0.5 + 0.5 * eased;
        const isAccent = i % 4 === 0;

        return (
          <g key={i} transform={`translate(${tx} ${ty}) scale(${scale})`} style={{ opacity }}>
            <circle
              r="4"
              fill={isAccent ? 'var(--pdb-accent, #1A1A1A)' : 'var(--pdb-card, #FFFFFF)'}
              stroke="var(--pdb-accent, #1A1A1A)"
              strokeWidth="0.5"
            />
            <text
              textAnchor="middle"
              dominantBaseline="central"
              fontFamily="var(--pdb-font-mono, ui-monospace)"
              fontSize="3.4"
              fontWeight="600"
              fill={isAccent ? 'var(--pdb-card, #F7F3EA)' : 'var(--pdb-ink, #0F0F0F)'}
              style={{ userSelect: 'none' }}
            >
              {r.l}
            </text>
          </g>
        );
      })}

      {progress > 0.95 && (
        <g transform="translate(22 50)" style={{ opacity: (progress - 0.95) / 0.05 }}>
          <text textAnchor="middle" dominantBaseline="central"
            fontFamily="var(--pdb-font-mono, ui-monospace)" fontSize="2.6"
            fill="var(--pdb-ink-3, #6B6B6B)" x="-12">N′</text>
          <text textAnchor="middle" dominantBaseline="central"
            fontFamily="var(--pdb-font-mono, ui-monospace)" fontSize="2.6"
            fill="var(--pdb-ink-3, #6B6B6B)" x="60" y="0">C′</text>
        </g>
      )}
    </svg>
  );
}
