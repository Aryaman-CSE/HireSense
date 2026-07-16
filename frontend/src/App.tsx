import { useEffect, useState } from "react";

/**
 * 100% Pure CSS layout.
 * No Tailwind dependencies required for this to render correctly.
 */

const RESUME_FIELDS = [
  { label: "NAME", value: "Aditi Sharma" },
  { label: "EDUCATION", value: "B.Tech CSE, VIT Vellore" },
  { label: "SKILLS", value: "React · Node.js · AWS" },
  { label: "CURRENT ROLE", value: "Backend Engineer, Nimbus Labs" },
];

function IndexCard() {
  const [revealed, setRevealed] = useState(0);

  useEffect(() => {
    if (revealed >= RESUME_FIELDS.length) return;
    const t = setTimeout(() => setRevealed((r) => r + 1), 350);
    return () => clearTimeout(t);
  }, [revealed]);

  return (
    <div className="hw-card-col">
      {/* Tab - physically overlaps card */}
      <div className="hw-tab hw-tab-candidate">CANDIDATE RECORD</div>
      <div className="hw-card">
        <div className="hw-card-header">
          <span className="hw-mono-label">FILE NO. HS-0148</span>
          <span className="hw-pin"></span>
        </div>
        <dl className="hw-card-body">
          {RESUME_FIELDS.slice(0, revealed).map((f) => (
            <div key={f.label} className="hw-field">
              <dt className="hw-field-label">{f.label}</dt>
              <dd className="hw-field-value">{f.value}</dd>
            </div>
          ))}
          {revealed < RESUME_FIELDS.length && (
            <div className="hw-field-label">
              {RESUME_FIELDS[revealed].label}
              <span className="hw-blink"></span>
            </div>
          )}
        </dl>
      </div>
    </div>
  );
}

function StageLabel({ n, label }) {
  return (
    <div className="hw-stage-row">
      <span className="hw-stage-num">{n}</span>
      <span className="hw-stage-label">{label}</span>
    </div>
  );
}

function RecordCard({ n, stage, tab, title, description, cta, tabColor }) {
  return (
    <div className="hw-card-col">
      <div 
        className="hw-tab" 
        style={{ backgroundColor: tabColor, borderColor: tabColor, color: 'white' }}
      >
        {tab}
      </div>
      <div className="hw-card hw-card-full">
        <StageLabel n={n} label={stage} />
        <div className="hw-icon-wrap" style={{ borderColor: `${tabColor}44` }}>
          <div className="hw-icon" style={{ backgroundColor: tabColor }}></div>
        </div>
        <h3 className="hw-title">{title}</h3>
        <p className="hw-desc">{description}</p>
        <button 
          className="hw-btn-outline" 
          style={{ borderColor: tabColor, color: tabColor }}
          onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = tabColor, e.currentTarget.style.color = 'white')}
          onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = 'transparent', e.currentTarget.style.color = tabColor)}
        >
          {cta}
        </button>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <main className="hw-app">
      {/* ====================================================== */}
      {/* PURE CSS STYLES - EMBEDDED DIRECTLY, NO EXTERNAL FILE NEEDED */}
      {/* ====================================================== */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@500;600&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap');

        /* --- BASE RESET --- */
        .hw-app {
          font-family: 'IBM Plex Sans', sans-serif;
          background-color: #EEEAE0;
          color: #1C1B18;
          margin: 0;
          padding: 0;
          min-height: 100vh;
          box-sizing: border-box;
          -webkit-font-smoothing: antialiased;
        }
        .hw-app * { box-sizing: border-box; }
        .hw-app *:before, .hw-app *:after { box-sizing: border-box; }

        /* --- STRICT CONTAINER (1160px max) --- */
        .hw-container {
          max-width: 1160px;
          margin: 0 auto;
          padding: 0 24px;
        }
        @media (min-width: 768px) {
          .hw-container { padding: 0 40px; }
        }

        /* --- NAVBAR --- */
        .hw-nav {
          display: flex;
          justify-content: space-between;
          align-items: center;
          height: 72px;
          border-bottom: 1px solid #D9D4C5;
          background-color: rgba(255, 255, 255, 0.2);
          backdrop-filter: blur(4px);
        }
        .hw-nav-brand {
          font-family: 'IBM Plex Serif', serif;
          font-size: 22px;
          font-weight: 600;
          letter-spacing: -0.02em;
        }
        .hw-nav-brand span { color: #2A3B8F; }
        .hw-nav-sub { display: none; font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #9a9587; margin-left: 8px; }
        @media (min-width: 640px) { .hw-nav-sub { display: inline; } }
        
        .hw-nav-actions { display: flex; gap: 12px; }
        .hw-btn-ghost {
          background: white; border: 1px solid #D9D4C5; padding: 8px 16px;
          font-family: 'IBM Plex Mono', monospace; font-size: 12px; border-radius: 4px;
          cursor: pointer; transition: 0.2s;
        }
        .hw-btn-ghost:hover { border-color: #1C1B18; }
        .hw-btn-solid {
          background: #1C1B18; border: 1px solid #1C1B18; color: white;
          padding: 8px 16px; font-family: 'IBM Plex Mono', monospace; font-size: 12px;
          border-radius: 4px; cursor: pointer; transition: 0.2s;
        }
        .hw-btn-solid:hover { background: #33322c; }

        /* --- HERO SECTION --- */
        .hw-hero {
          display: grid;
          grid-template-columns: 1fr;
          gap: 48px;
          padding: 80px 0 56px 0;
          align-items: center;
        }
        @media (min-width: 1024px) {
          .hw-hero { grid-template-columns: 1fr 1fr; gap: 64px; padding: 112px 0 56px 0; }
        }
        .hw-hero-label {
          font-family: 'IBM Plex Mono', monospace;
          font-size: 10px; letter-spacing: 0.15em; text-transform: uppercase;
          color: #9a9587;
        }
        .hw-hero-title {
          font-family: 'IBM Plex Serif', serif;
          font-size: 42px; font-weight: 500; line-height: 1.1;
          margin-top: 16px; letter-spacing: -0.02em;
        }
        @media (min-width: 768px) { .hw-hero-title { font-size: 52px; } }
        .hw-hero-desc {
          max-width: 440px; margin-top: 20px; font-size: 16px;
          line-height: 1.6; color: #6E6A5F;
        }

        /* --- CARDS PIPELINE --- */
        .hw-pipeline {
          display: grid; grid-template-columns: 1fr; gap: 24px;
          padding-bottom: 96px;
        }
        @media (min-width: 768px) { .hw-pipeline { grid-template-columns: 1fr 1fr; } }

        /* --- CARD SHARED STYLES --- */
        .hw-card-col { display: flex; flex-direction: column; align-items: flex-start; width: 100%; }
        .hw-tab {
          position: relative; z-index: 10; margin-bottom: -1px;
          display: inline-block; border-radius: 4px 4px 0 0;
          border: 1px solid #D9D4C5; border-bottom-width: 0;
          padding: 6px 16px; font-family: 'IBM Plex Mono', monospace;
          font-size: 10px; letter-spacing: 0.1em;
        }
        .hw-tab-candidate { background: #E4DECB; color: #6E6A5F; border-color: #D9D4C5; }
        
        .hw-card {
          position: relative; z-index: 0; width: 100%;
          background: white; border-radius: 0 4px 4px 4px;
          border: 1px solid #D9D4C5; padding: 24px;
          box-shadow: 0 4px 12px -4px rgba(28,27,24,0.03);
          transition: box-shadow 0.2s;
        }
        .hw-card:hover { box-shadow: 0 4px 16px -4px rgba(28,27,24,0.08); }
        @media (min-width: 768px) { .hw-card { padding: 32px; } }
        
        .hw-card-header {
          display: flex; justify-content: space-between; align-items: center;
          border-bottom: 1px dashed #D9D4C5; padding-bottom: 16px; margin-bottom: 20px;
        }
        .hw-mono-label { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #9a9587; letter-spacing: 0.05em; }
        .hw-pin { display: block; width: 14px; height: 14px; border-radius: 50%; border: 1px solid #D9D4C5; background: #EEEAE0; }
        
        .hw-card-body { display: flex; flex-direction: column; gap: 16px; }
        .hw-field-label { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #2A3B8F; letter-spacing: 0.1em; }
        .hw-field-value { font-family: 'IBM Plex Mono', monospace; font-size: 14px; color: #1C1B18; margin-top: 2px; }
        .hw-blink { display: inline-block; height: 12px; width: 5px; background: rgba(42, 59, 143, 0.4); vertical-align: middle; margin-left: 4px; animation: pulse 1s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }

        /* --- CARD FULL HEIGHT (Inputs) --- */
        .hw-card-full { flex: 1; display: flex; flex-direction: column; }
        
        .hw-stage-row { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
        .hw-stage-num {
          display: flex; justify-content: center; align-items: center;
          width: 20px; height: 20px; border-radius: 50%; border: 1px solid #D9D4C5;
          background: white; font-family: 'IBM Plex Mono', monospace; font-size: 9px; color: #6E6A5F;
        }
        .hw-stage-label { font-family: 'IBM Plex Mono', monospace; font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: #6E6A5F; }

        .hw-icon-wrap {
          display: flex; justify-content: center; align-items: center;
          width: 40px; height: 40px; border-radius: 50%; border: 1px solid #ccc;
          margin-bottom: 16px;
        }
        .hw-icon { width: 16px; height: 16px; border-radius: 2px; mask-size: contain; -webkit-mask-size: contain; }

        .hw-title { font-family: 'IBM Plex Serif', serif; font-size: 26px; font-weight: 500; line-height: 1.2; color: #1C1B18; margin: 0; }
        .hw-desc { font-size: 15px; line-height: 1.6; color: #6E6A5F; margin-top: 8px; flex: 1; }
        
        .hw-btn-outline {
          margin-top: 24px; width: fit-content; border-radius: 4px;
          border: 1px solid #ccc; padding: 10px 20px; font-family: 'IBM Plex Mono', monospace;
          font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;
          background: transparent;
        }

        /* --- MATCH CARD --- */
        .hw-match-card {
          margin-top: 24px; background: white; border: 1px solid #D9D4C5;
          border-radius: 4px; padding: 24px; box-shadow: 0 4px 12px -4px rgba(28,27,24,0.03);
        }
        @media (min-width: 768px) { .hw-match-card { padding: 32px; } }
        
        .hw-match-row {
          display: flex; flex-direction: column; gap: 20px; align-items: flex-start;
        }
        @media (min-width: 768px) { .hw-match-row { flex-direction: row; justify-content: space-between; align-items: center; } }
        
        .hw-match-flex {
          display: flex; flex-direction: column; gap: 16px; align-items: flex-start;
        }
        @media (min-width: 640px) { .hw-match-flex { flex-direction: row; align-items: center; } }

        .hw-match-circle {
          display: flex; justify-content: center; align-items: center;
          width: 64px; height: 64px; border-radius: 50%; border: 2px solid #A6790A;
          background: rgba(166, 121, 10, 0.05); flex-shrink: 0;
          font-family: 'IBM Plex Mono', monospace; font-size: 9px; font-weight: 600;
          letter-spacing: 0.1em; color: #A6790A;
        }
        
        .hw-btn-match {
          display: flex; align-items: center; gap: 8px; width: fit-content; flex-shrink: 0;
          border-radius: 4px; border: 2px solid #1C1B18; background: #1C1B18;
          color: white; padding: 12px 24px; font-family: 'IBM Plex Mono', monospace;
          font-size: 12px; font-weight: 600; cursor: pointer; transition: transform 0.2s;
        }
        .hw-btn-match:hover { transform: scale(1.02); }
        .hw-btn-match span { display: inline-block; transition: transform 0.2s; }
        .hw-btn-match:hover span { transform: translateX(4px); }

        /* --- RECENT ANALYSES --- */
        .hw-recent-wrapper { padding-bottom: 128px; margin-top: 40px; }
        .hw-recent-title { font-family: 'IBM Plex Serif', serif; font-size: 22px; font-weight: 500; margin-bottom: 16px; }
        .hw-recent-box {
          width: 100%; border-radius: 4px; border: 2px dashed #D9D4C5;
          background: rgba(255,255,255,0.3); padding: 32px 24px; text-align: center;
          transition: border-color 0.2s;
        }
        .hw-recent-box:hover { border-color: #C0BAA6; }
        .hw-recent-text { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: #9a9587; }

      `}</style>

      {/* ====================================================== */}
      {/* HTML STRUCTURE - 100% MAPPED TO PURE CSS ABOVE */}
      {/* ====================================================== */}

      {/* Navbar */}
      <header className="hw-container">
        <div className="hw-nav">
          <div>
            <span className="hw-nav-brand">Hire<span>Sense</span></span>
            <span className="hw-nav-sub">/ recruitment records</span>
          </div>
          <div className="hw-nav-actions">
            <button className="hw-btn-ghost">GitHub</button>
            <button className="hw-btn-solid">Settings</button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hw-container">
        <div className="hw-hero">
          <div>
            <p className="hw-hero-label">Welcome back</p>
            <h1 className="hw-hero-title">Every resume,<br />filed and matched.</h1>
            <p className="hw-hero-desc">
              HireSense reads resumes and job descriptions, files each as a structured record, and ranks candidates by how well their file matches the role.
            </p>
          </div>
          <IndexCard />
        </div>
      </section>

      {/* Pipeline Section */}
      <section className="hw-container">
        <div className="hw-pipeline">
          <RecordCard
            n="1" stage="Input · candidate" tab="RESUME" title="Upload resume"
            description="PDF or DOCX. HireSense files it as a candidate record — name, skills, experience and role history."
            cta="Upload resume" tabColor="#2A3B8F"
          />
          <RecordCard
            n="2" stage="Input · role" tab="JOB" title="Upload job description"
            description="Paste text or upload a file. Required skills, seniority and scope are filed as a role record."
            cta="Upload job" tabColor="#8C2F2F"
          />
        </div>

        {/* Match Card */}
        <div className="hw-match-card">
          <StageLabel n="3" label="Output · match" />
          <div className="hw-match-row">
            <div className="hw-match-flex">
              <div className="hw-match-circle">MATCH</div>
              <div>
                <h3 className="hw-title">Generate AI match</h3>
                <p className="hw-desc">Compares a resume record against a role record and returns a ranked, scored match.</p>
              </div>
            </div>
            <button className="hw-btn-match">
              Generate match <span>→</span>
            </button>
          </div>
        </div>
      </section>

      {/* Recent Analyses */}
      <section className="hw-container hw-recent-wrapper">
        <h3 className="hw-recent-title">Recent analyses</h3>
        <div className="hw-recent-box">
          <p className="hw-recent-text">No records filed yet — run a match above to see it here.</p>
        </div>
      </section>
    </main>
  );
}