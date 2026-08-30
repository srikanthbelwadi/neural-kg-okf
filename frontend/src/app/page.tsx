"use client";

import React, { useState, useEffect, useRef } from "react";
import { Sparkles, Search, Database, Cpu, FileText, Github, Zap, ArrowRight, CheckCircle, HelpCircle, Download } from "lucide-react";

interface VisualBlock {
  type: string;
  title?: string;
  entity?: string;
  value?: string | number;
  period?: string;
  source?: string;
  columns?: Array<{ key: string; label: string; type: string }>;
  rows?: Array<Record<string, any>>;
  data?: Array<{ label?: string; period?: string; value: number }>;
}

export default function Home() {
  const [activeTab, setActiveTab] = useState<"query" | "catalog" | "how">("query");
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [traceLogs, setTraceLogs] = useState<string[]>([]);
  const [traceStatus, setTraceStatus] = useState("");
  const [elapsed, setElapsed] = useState("0.0");
  const [answer, setAnswer] = useState<string | null>(null);
  const [shape, setShape] = useState<string | null>(null);
  const [visualBlocks, setVisualBlocks] = useState<VisualBlock[]>([]);
  const [clarification, setClarification] = useState<any | null>(null);
  
  const eventSourceRef = useRef<EventSource | null>(null);

  const sampleQueries = [
    "Which foundations fund Stanford?",
    "What was Apple total revenue in 2023?",
    "Which counties have the highest poverty rate in the US?",
    "Which public companies have the highest gross profit?",
    "Which counties have the highest diabetes prevalence?",
  ];

  const handleAsk = (qToRun: string, assumptions: any = null) => {
    if (!qToRun.trim()) return;
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
    }

    setLoading(true);
    setTraceLogs([]);
    setAnswer(null);
    setShape(null);
    setVisualBlocks([]);
    setClarification(null);
    setTraceStatus("Discovering matching resources via ARD...");

    const startTime = performance.now();
    const interval = setInterval(() => {
      setElapsed(((performance.now() - startTime) / 1000).toFixed(1));
    }, 100);

    const endpoint = `/ask?query=${encodeURIComponent(qToRun)}&streaming=true&on_ambiguity=ask${assumptions ? `&assumptions=${encodeURIComponent(JSON.stringify(assumptions))}` : ''}`;
    const es = new EventSource(endpoint);
    eventSourceRef.current = es;

    es.onmessage = (e) => {
      try {
        const msg = JSON.parse(e.data);
        if (msg.message_type === "intermediate_message") {
          setTraceLogs((prev) => [...prev, msg.content]);
          setTraceStatus(msg.content);
        } else if (msg.message_type === "nlws") {
          const payload = msg.content;
          if (payload["@type"] === "ClarificationRequest" || payload.status === "needs_clarification") {
            setClarification(payload);
          } else {
            setAnswer(payload.answer || "Answer computed.");
            setShape(payload.shape || null);
            if (payload.visual_payload && payload.visual_payload.blocks) {
              setVisualBlocks(payload.visual_payload.blocks);
            }
          }
        } else if (msg.message_type === "complete" || msg.message_type === "end-nlweb-response") {
          clearInterval(interval);
          setLoading(false);
          es.close();
        }
      } catch (err) {
        console.error("Stream parse error", err);
      }
    };

    es.onerror = () => {
      clearInterval(interval);
      setLoading(false);
      es.close();
    };
  };

  const handleExportCsv = (block: VisualBlock) => {
    if (!block.rows || !block.columns) return;
    const headers = block.columns.map((c) => `"${c.label}"`).join(",");
    const rows = block.rows.map((r) => block.columns!.map((c) => `"${r[c.key] ?? ""}"`).join(","));
    const csvContent = [headers, ...rows].join("\n");
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `data_export_${Date.now()}.csv`;
    link.click();
  };

  return (
    <div className="min-h-screen flex flex-col antialiased">
      {/* Navigation Bar */}
      <header className="sticky top-0 z-50 glass border-b border-[#202b42] px-6 py-3.5 flex items-center justify-between">
        <div className="flex items-center gap-3.5">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center shadow-lg shadow-blue-500/20">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
                Neural KG
              </span>
              <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-400 border border-blue-500/30">
                ARD + OKF
              </span>
            </div>
            <p className="text-xs text-slate-400">Agentic Resource Discovery & BigQuery Universal Knowledge</p>
          </div>
        </div>

        <nav className="hidden md:flex items-center p-1 rounded-xl bg-[#0a0e17]/80 border border-[#202b42] text-sm">
          <button
            onClick={() => setActiveTab("query")}
            className={`px-4 py-1.5 rounded-lg font-medium transition-all flex items-center gap-2 ${
              activeTab === "query" ? "bg-blue-600 text-white shadow-sm" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            <Search className="w-4 h-4" /> Query Explorer
          </button>
          <button
            onClick={() => setActiveTab("catalog")}
            className={`px-4 py-1.5 rounded-lg font-medium transition-all flex items-center gap-2 ${
              activeTab === "catalog" ? "bg-blue-600 text-white shadow-sm" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            <Database className="w-4 h-4" /> BigQuery & OKF Catalog
          </button>
          <button
            onClick={() => setActiveTab("how")}
            className={`px-4 py-1.5 rounded-lg font-medium transition-all flex items-center gap-2 ${
              activeTab === "how" ? "bg-blue-600 text-white shadow-sm" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            <Cpu className="w-4 h-4" /> How It Works
          </button>
        </nav>

        <div className="flex items-center gap-3">
          <a
            href="https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing"
            target="_blank"
            rel="noreferrer"
            className="text-xs text-slate-400 hover:text-blue-400 transition-colors flex items-center gap-1.5 bg-[#131b2e] px-3 py-1.5 rounded-lg border border-[#202b42]"
          >
            <FileText className="w-3.5 h-3.5" /> OKF Spec
          </a>
          <a
            href="https://github.com/TechSoup/resource-raiser"
            target="_blank"
            rel="noreferrer"
            className="text-xs text-slate-300 hover:text-white transition-colors flex items-center gap-1.5 bg-blue-950/60 text-blue-300 px-3 py-1.5 rounded-lg border border-blue-800/50"
          >
            <Github className="w-3.5 h-3.5" /> GitHub
          </a>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-8 flex flex-col gap-8">
        {activeTab === "query" && (
          <section className="flex flex-col gap-6">
            <div className="flex flex-col items-center text-center gap-3 max-w-3xl mx-auto mt-4">
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight bg-gradient-to-b from-white via-slate-100 to-slate-300 bg-clip-text text-transparent">
                Explore Any Data with Agentic Discovery
              </h1>
              <p className="text-sm text-slate-400 leading-relaxed max-w-2xl">
                Ask questions across US Census, SEC EDGAR, IRS 990 Grant Graph, CDC PLACES, NOAA Weather, and all Google Cloud Public BigQuery Datasets.
              </p>
            </div>

            {/* Input Bar */}
            <div className="max-w-4xl w-full mx-auto">
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleAsk(query);
                }}
                className="relative group"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-2xl blur-md opacity-25 group-hover:opacity-40 transition-opacity"></div>
                <div className="relative flex items-center glass rounded-2xl border border-slate-700/80 p-2 shadow-2xl">
                  <div className="pl-4 pr-2 text-slate-400">
                    <Search className="w-5 h-5 text-blue-400" />
                  </div>
                  <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="e.g. Which foundations fund Stanford? or What is the poverty rate in Cook County?"
                    className="w-full bg-transparent text-white placeholder-slate-400 focus:outline-none px-2 py-2.5 text-base font-normal"
                  />
                  <button
                    type="submit"
                    disabled={loading || !query.trim()}
                    className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium px-6 py-3 rounded-xl transition-all shadow-lg shadow-blue-600/30 flex items-center gap-2 shrink-0 disabled:opacity-50"
                  >
                    <span>{loading ? "Searching..." : "Ask"}</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              </form>

              {/* Sample Chips */}
              <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs">
                <span className="text-slate-400 flex items-center gap-1">
                  <Zap className="w-3.5 h-3.5 text-amber-400" /> Try asking:
                </span>
                {sampleQueries.map((sq, i) => (
                  <button
                    key={i}
                    onClick={() => {
                      setQuery(sq);
                      handleAsk(sq);
                    }}
                    className="px-3 py-1 rounded-full bg-[#131b2e] hover:bg-[#1a243d] border border-[#202b42] text-slate-300 hover:text-blue-300 transition-all"
                  >
                    {sq}
                  </button>
                ))}
              </div>
            </div>

            {/* Trace Panel */}
            {loading && (
              <div className="max-w-4xl w-full mx-auto glass rounded-2xl p-4 border border-[#202b42]">
                <div className="flex items-center justify-between border-b border-[#202b42] pb-3 mb-3">
                  <div className="flex items-center gap-2 text-sm font-semibold text-slate-200">
                    <span className="relative flex h-2.5 w-2.5">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-500"></span>
                    </span>
                    <span>{traceStatus}</span>
                  </div>
                  <span className="text-xs font-mono text-slate-400">{elapsed}s</span>
                </div>
                <div className="flex flex-col gap-1.5 text-xs font-mono text-slate-300 max-h-48 overflow-y-auto">
                  {traceLogs.map((log, i) => (
                    <div key={i} className="flex items-center gap-2 py-0.5">
                      <span className="text-blue-400">›</span>
                      <span>{log}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Clarification Modal / Card */}
            {clarification && (
              <div className="max-w-4xl w-full mx-auto glass rounded-2xl p-6 border-2 border-amber-500/40 bg-amber-950/10">
                <div className="flex items-start gap-3">
                  <div className="p-2 rounded-lg bg-amber-500/20 text-amber-400 shrink-0">
                    <HelpCircle className="w-5 h-5" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-base font-bold text-amber-200">Clarification Needed</h3>
                    <p className="text-sm text-slate-300 mt-1">{clarification.question}</p>
                    <div className="mt-4 flex flex-col gap-2.5">
                      {(clarification.options || []).map((opt: any, idx: number) => (
                        <button
                          key={idx}
                          onClick={() => handleAsk(query, opt.assumptions || { concept: opt.id })}
                          className="flex items-center justify-between p-3.5 rounded-xl bg-[#131b2e] hover:bg-[#1a243d] border border-[#202b42] hover:border-amber-500/50 text-left transition-all"
                        >
                          <div>
                            <div className="font-semibold text-white text-sm">{opt.label || opt.id}</div>
                            <div className="text-xs text-slate-400 mt-0.5">{opt.id} {opt.period ? `· ${opt.period}` : ""}</div>
                          </div>
                          {opt.value && (
                            <span className="font-mono font-bold text-emerald-400 text-sm bg-emerald-950/60 px-2.5 py-1 rounded-lg border border-emerald-800/50">
                              {typeof opt.value === "number" ? `$${opt.value.toLocaleString()}` : opt.value}
                            </span>
                          )}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Results Canvas */}
            {answer && (
              <div className="max-w-5xl w-full mx-auto flex flex-col gap-6">
                <div className="glass-card rounded-2xl p-6 border-l-4 border-emerald-500 shadow-xl">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                      <CheckCircle className="w-4 h-4" /> Grounded AI Response
                    </span>
                    {shape && (
                      <span className="text-xs font-medium px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                        Shape: {shape.toUpperCase()}
                      </span>
                    )}
                  </div>
                  <div className="text-base sm:text-lg text-slate-100 font-medium leading-relaxed">
                    {answer}
                  </div>
                </div>

                {/* Visual Blocks */}
                <div className="grid grid-cols-1 gap-6">
                  {visualBlocks.map((block, idx) => (
                    <React.Fragment key={idx}>
                      {block.type === "kpi_card" && (
                        <div className="glass-card rounded-2xl p-6 border border-[#202b42] flex flex-col gap-2">
                          <div className="flex items-center justify-between">
                            <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">{block.entity}</span>
                            <span className="text-xs font-mono text-slate-400">{block.period}</span>
                          </div>
                          <div className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">{block.value}</div>
                          <div className="text-xs text-slate-400 flex items-center gap-2 mt-1">
                            <span>{block.title}</span>
                            <span>·</span>
                            <span className="text-blue-400">{block.source}</span>
                          </div>
                        </div>
                      )}

                      {block.type === "data_table" && block.columns && block.rows && (
                        <div className="glass-card rounded-2xl p-6 border border-[#202b42] flex flex-col gap-4">
                          <div className="flex items-center justify-between">
                            <div>
                              <h3 className="text-base font-bold text-white">{block.title || "Data Records"}</h3>
                              <p className="text-xs text-slate-400 mt-0.5">{block.rows.length} records from {block.source}</p>
                            </div>
                            <button
                              onClick={() => handleExportCsv(block)}
                              className="px-3 py-1.5 rounded-lg bg-[#131b2e] hover:bg-[#1a243d] border border-[#202b42] text-xs text-slate-300 hover:text-white flex items-center gap-1.5"
                            >
                              <Download className="w-3.5 h-3.5" /> Export CSV
                            </button>
                          </div>
                          <div className="overflow-x-auto rounded-xl border border-[#202b42]">
                            <table className="w-full border-collapse">
                              <thead>
                                <tr>
                                  {block.columns.map((c, i) => (
                                    <th key={i} className="px-4 py-3 text-left text-xs font-bold uppercase tracking-wider text-slate-300 bg-[#0a0e17]/60 border-b border-[#202b42]">
                                      {c.label}
                                    </th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody>
                                {block.rows.map((row, rI) => (
                                  <tr key={rI} className="hover:bg-[#1a243d]/50 transition-colors">
                                    {block.columns!.map((c, cI) => (
                                      <td key={cI} className="px-4 py-3 text-xs text-slate-200 border-b border-[#202b42]/40 font-mono">
                                        {row[c.key] ?? ""}
                                      </td>
                                    ))}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      )}
                    </React.Fragment>
                  ))}
                </div>
              </div>
            )}
          </section>
        )}

        {/* Catalog Tab */}
        {activeTab === "catalog" && (
          <section className="flex flex-col gap-6">
            <div>
              <h2 className="text-2xl font-bold text-white">Universal BigQuery & OKF Data Catalog</h2>
              <p className="text-sm text-slate-400">Discover all connected data sources described as actionable OKF descriptors.</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              <div className="glass-card rounded-xl p-5 border border-[#202b42]">
                <span className="text-xs font-semibold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">Google BigQuery</span>
                <h3 className="font-bold text-white text-base mt-2">US Census ACS Demographics</h3>
                <p className="text-xs text-slate-300 mt-1">Socio-economic statistics across all ~3,200 US counties with server-side SQL aggregation.</p>
              </div>
              <div className="glass-card rounded-xl p-5 border border-[#202b42]">
                <span className="text-xs font-semibold px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">SEC EDGAR + BQ</span>
                <h3 className="font-bold text-white text-base mt-2">SEC Quarterly Financials (US-GAAP)</h3>
                <p className="text-xs text-slate-300 mt-1">Revenues, profits, and balance sheets for all US public companies.</p>
              </div>
              <div className="glass-card rounded-xl p-5 border border-[#202b42]">
                <span className="text-xs font-semibold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Relational Graph</span>
                <h3 className="font-bold text-white text-base mt-2">IRS 990 Grant Graph</h3>
                <p className="text-xs text-slate-300 mt-1">Who funds whom across all US foundations and nonprofits (~7M edges).</p>
              </div>
            </div>
          </section>
        )}

        {/* How it Works Tab */}
        {activeTab === "how" && (
          <section className="glass rounded-2xl p-6 sm:p-8 flex flex-col gap-6">
            <h2 className="text-2xl font-bold text-white">How Neural KG Works: The Life of a Query</h2>
            <p className="text-sm text-slate-300">
              Neural KG connects natural language questions to live databases without pre-integration. It discovers OKF sources via ARD, verifies capabilities before querying, crosswalks entity identifiers, fetches live data, and strictly validates the answer against hallucination.
            </p>
          </section>
        )}
      </main>

      <footer className="mt-auto border-t border-[#202b42] py-6 px-6 text-center text-xs text-slate-500">
        Built with Open Knowledge Format (OKF) & Agentic Resource Discovery (ARD) · Powered by Google Gemini & BigQuery Public Datasets
      </footer>
    </div>
  );
}
