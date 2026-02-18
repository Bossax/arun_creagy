#!/usr/bin/env bun
// recap-rich.ts - Full context recap with path fixes and reliable sorting
import { $ } from "bun";
import { existsSync, readdirSync } from "fs";
import { join } from "path";

// Keep this as env-driven so the skill runner doesn't need to pass extra args.
const DEBUG = process.env.RECAP_DEBUG === "1";
function dlog(msg: string) {
  if (!DEBUG) return;
  // Keep debug single-line and Windows-safe (prefer forward slashes when paths appear)
  console.log(`[RECAP_DEBUG] ${msg.replaceAll("\\", "/")}`);
}

// Get Root
const ROOT = process.env.ROOT || (await $`git rev-parse --show-toplevel`.text().catch(() => process.cwd())).trim();
await $`git -C ${ROOT} config core.quotePath false`.quiet().catch(() => {});

dlog(`script=${import.meta.url}`);
dlog(`ROOT=${ROOT}`);

/**
 * Helper: Resolve paths that might use Greek 'ψ' or ASCII 'psi'.
 * Tries 'ψ' first, falls back to 'psi'.
 */
function resolvePsiPath(root: string, relativePath: string): string {
  // 1. Try exact path (e.g. "ψ/data")
  const p1 = join(root, relativePath);
  if (existsSync(p1)) return p1;

  // 2. Try ASCII substitution (e.g. "psi/data")
  const asciiPath = relativePath.replace(/^ψ/, "psi");
  const p2 = join(root, asciiPath);
  
  // Return p2 (ASCII) by default so if we create files, we prefer ASCII 
  // unless the Greek one already exists.
  if (existsSync(p2)) return p2;
  return p2; 
}

const now = new Date();
const date = now.toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });
const time = now.toTimeString().slice(0, 5);

// Use local time for folder structure YYYY-MM
const year = now.getFullYear();
const monthStr = String(now.getMonth() + 1).padStart(2, "0");
const monthFolder = `${year}-${monthStr}`;

console.log("# RECAP (Rich)");
console.log(`\n${time} | ${date}\n\n---\n`);

function extractSection(md: string, heading: RegExp): string | null {
  // CRLF-safe, line-based extraction.
  const lines = md.split(/\r?\n/);
  let start = -1;
  for (let i = 0; i < lines.length; i++) {
    if (heading.test(lines[i].trim())) {
      start = i + 1;
      break;
    }
  }
  if (start === -1) return null;

  const out: string[] = [];
  for (let i = start; i < lines.length; i++) {
    const line = lines[i];
    // Stop at next heading of same or higher level.
    if (/^#{1,2}\s+/.test(line.trim())) break;
    out.push(line);
  }
  const text = out.join("\n").trim();
  return text.length ? text : null;
}

function extractSessionSummary(md: string): string | null {
  return (
    extractSection(md, /^##\s+Session Summary\s*$/i) ||
    extractSection(md, /^##\s+Summary\s*$/i)
  );
}

function bulletsFromSummary(summary: string, maxBullets = 3): string[] {
  const lines = summary.split(/\r?\n/).map((l) => l.trimRight());
  const bullets = lines
    .map((l) => l.trim())
    .filter((l) => /^[-*]\s+/.test(l))
    .map((l) => `- ${l.replace(/^[-*]\s+/, "").trim()}`);

  const truncate = (s: string, n = 240) => (s.length > n ? `${s.slice(0, n - 1)}…` : s);

  const splitSentences = (text: string): string[] => {
    // Split only on punctuation that is followed by whitespace.
    // This avoids breaking tokens like `streak.days`.
    const parts: string[] = [];
    let buf = "";
    for (let i = 0; i < text.length; i++) {
      const ch = text[i];
      buf += ch;
      const isEnd = ch === "." || ch === "!" || ch === "?";
      const next = text[i + 1] ?? "";
      if (isEnd && (next === " " || next === "\t" || next === "\n")) {
        parts.push(buf.trim());
        buf = "";
      }
    }
    if (buf.trim()) parts.push(buf.trim());
    return parts;
  };

  if (bullets.length) return bullets.slice(0, maxBullets).map((b) => truncate(b));

  // If no bullets exist, take first non-empty content lines and coerce to bullets.
  const nonEmpty = lines
    .map((l) => l.trim())
    .filter((l) => l.length > 0)
    .filter((l) => !/^#+\s+/.test(l));

  const blob = nonEmpty.join(" ").replace(/\s+/g, " ").trim();

  // Try sentence extraction for paragraph-style summaries.
  const sentences = splitSentences(blob)
    .filter(Boolean)
    .slice(0, maxBullets)
    .map((s) => `- ${truncate(s)}`);

  if (sentences.length) return sentences;

  // Fallback to line fragments.
  return nonEmpty.slice(0, maxBullets).map((l) => `- ${truncate(l)}`);
}

type RetroHit = {
  yyyyMm: string;
  dd: string;
  file: string;
  absPath: string;
};

function collectRecentRetros(retroBaseDirAbs: string, n: number): RetroHit[] {
  const hits: RetroHit[] = [];
  if (!existsSync(retroBaseDirAbs)) return hits;

  const months = readdirSync(retroBaseDirAbs)
    .filter((m) => /^\d{4}-\d{2}$/.test(m))
    .sort()
    .reverse();

  for (const yyyyMm of months) {
    const monthDir = join(retroBaseDirAbs, yyyyMm);

    // Guard against Windows noise (e.g., desktop.ini) or non-dirs.
    let days: string[] = [];
    try {
      days = readdirSync(monthDir)
        .filter((d) => /^\d{2}$/.test(d))
        .sort()
        .reverse();
    } catch {
      continue;
    }

    for (const dd of days) {
      const dayDir = join(monthDir, dd);
      let files: string[] = [];
      try {
        files = readdirSync(dayDir)
          .filter((f) => f.endsWith(".md") && /^\d{2}\.\d{2}_/.test(f))
          .sort()
          .reverse(); // newest first within day
      } catch {
        continue;
      }

      for (const file of files) {
        hits.push({ yyyyMm, dd, file, absPath: join(dayDir, file) });
        if (hits.length >= n) return hits;
      }
    }
  }

  return hits;
}

function whenLabel(hit: RetroHit): string {
  const hh = hit.file.slice(0, 2);
  const mm = hit.file.slice(3, 5);
  return `${hit.yyyyMm}-${hit.dd} ${hh}:${mm}`;
}

// 1) RECENT WORK (authoritative: retrospectives)
console.log("## RECENT WORK (Last 3 retrospectives)");

// Resolve "ψ/memory/retrospectives" and scan across months so month rollovers don't hide the latest session.
const retroBaseDir = resolvePsiPath(ROOT, "ψ/memory/retrospectives");

dlog(`retroBaseDir=${retroBaseDir}`);

const recentRetros = collectRecentRetros(retroBaseDir, 3);
dlog(`recentRetros.count=${recentRetros.length}`);
dlog(`recentRetros.files=${recentRetros.map((r) => r.file).join(", ")}`);

if (!recentRetros.length) {
  console.log("(No retrospective found)");
} else {
  for (const hit of recentRetros) {
    console.log(`\n### ${whenLabel(hit)} — ${hit.file}`);
    try {
      const md = await Bun.file(hit.absPath).text();
      const summary = extractSessionSummary(md);
      if (!summary) {
        console.log("- (No 'Session Summary' section found)");
        continue;
      }
      const bullets = bulletsFromSummary(summary, 3);
      if (!bullets.length) {
        console.log("- (Session Summary empty)");
        continue;
      }
      bullets.forEach((b) => console.log(b));
    } catch {
      console.log("- (Failed to read retrospective file)");
    }
  }
}


// 2) HANDOFFS
const handoffDir = resolvePsiPath(ROOT, "ψ/inbox/handoff");
if (existsSync(handoffDir)) {
  const handoffs = readdirSync(handoffDir)
    .filter((f) => f.endsWith(".md") && !f.includes("CLAUDE"))
    .sort()
    .reverse(); // Newest first

  dlog(`handoffDir=${handoffDir}`);
  dlog(`handoffs.count=${handoffs.length}`);
  dlog(`handoffs.files=${handoffs.slice(0, 10).join(", ")}`);

  const top = handoffs.slice(0, 3);
  if (top.length) {
    console.log("\n## HANDOFFS (Last 3)");
    console.log("_Handoffs update only when you explicitly create them. They can be older than retrospectives._");

    for (const f of top) {
      console.log(`\n### ${f}`);
      try {
        const content = await Bun.file(join(handoffDir, f)).text();
        // Show a compact excerpt: first ~6 non-empty lines after any title
        const lines = content.split(/\r?\n/);
        const excerpt = lines
          .slice(0, 30)
          .filter((l) => l.trim().length > 0)
          .slice(0, 6)
          .join("\n");
        if (excerpt) console.log(excerpt);
      } catch {
        console.log("(Failed to read handoff file)");
      }
    }
  }
}

// Print debug footer last so it doesn't interrupt human-readable recap.
if (DEBUG) {
  console.log("\n---\n\n## DEBUG\n");
  console.log("Set RECAP_DEBUG=0 to hide this section.");
}

// 4. CONTEXT (Git & Pulse)
console.log("\n---\n\n## CONTEXT\n");
const status = await $`git -C ${ROOT} status -sb`.text();
console.log(status.trim());

// Pulse Data
const pProj = resolvePsiPath(ROOT, "ψ/data/pulse/project.json");
const pHeart = resolvePsiPath(ROOT, "ψ/data/pulse/heartbeat.json");

if (existsSync(pProj) && existsSync(pHeart)) {
  try {
    const proj = await Bun.file(pProj).json();
    const heart = await Bun.file(pHeart).json();
    
    const sess = proj.totalSessions || 0;
    const streak = heart.streak?.days || 0;
    const week = heart.weekChange || 0;
    const sign = week >= 0 ? "+" : "";
    
    console.log(`\n⚡ Session #${sess} | Streak: ${streak} days | Week: ${sign}${week}% msgs`);
  } catch (e) {
    // Ignore JSON parse errors
  }
}
