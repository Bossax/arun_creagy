#!/usr/bin/env bun
// Fast recap - no AI, just git status
// Usage: bun recap.ts

import { $ } from "bun";
import { existsSync, readdirSync } from "fs";
import { join } from "path";

const DEBUG = process.env.RECAP_DEBUG === "1";
function dlog(msg: string) {
  if (!DEBUG) return;
  console.log(`[RECAP_DEBUG] ${msg.replaceAll("\\", "/")}`);
}

/**
 * Resolve paths that might use Greek 'ψ' or ASCII 'psi'.
 * Prefer exact path if it exists; otherwise fall back to ASCII.
 */
function resolvePsiPath(root: string, relativePath: string): string {
  const p1 = join(root, relativePath);
  if (existsSync(p1)) return p1;
  const asciiPath = relativePath.replace(/^ψ/, "psi");
  return join(root, asciiPath);
}

// Get repo root
const root = (await $`git rev-parse --show-toplevel 2>/dev/null`.text()).trim() || process.cwd();
process.chdir(root);

dlog(`script=${import.meta.url}`);
dlog(`root=${root}`);

// Gather git data
const branch = (await $`git branch --show-current`.text()).trim();
let ahead = "0";
try {
  ahead = (await $`git rev-list --count @{u}..HEAD 2>/dev/null`.text()).trim() || "0";
} catch {}
const lastCommit = (await $`git log --oneline -1`.text()).trim().slice(8, 68);

// Schedule
let schedule = "No schedule";
const scheduleFilePsi = join(root, "ψ/inbox/schedule.md");
const scheduleFileAscii = join(root, "psi/inbox/schedule.md");
const scheduleFile = existsSync(scheduleFilePsi) ? scheduleFilePsi : scheduleFileAscii;
if (existsSync(scheduleFile)) {
  const scheduleContent = await Bun.file(scheduleFile).text();
  const today = new Date();
  const month = today.toLocaleString('en', { month: 'short' });
  const day = today.getDate();
  const tomorrow = day + 1;
  const regex = new RegExp(`${month}\\s*(${day}|${tomorrow})`, 'i');
  const match = scheduleContent.split('\n').find(line => regex.test(line));
  if (match) schedule = match.replace(/\|/g, '').trim().slice(0, 120);
}

type RetroHit = { yyyyMm: string; dd: string; file: string; absPath: string };

function collectRecentRetros(retroBaseDirAbs: string, n: number): RetroHit[] {
  const hits: RetroHit[] = [];
  if (!existsSync(retroBaseDirAbs)) return hits;

  const months = readdirSync(retroBaseDirAbs)
    .filter((m) => /^\d{4}-\d{2}$/.test(m))
    .sort()
    .reverse();

  for (const yyyyMm of months) {
    const monthDir = join(retroBaseDirAbs, yyyyMm);
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
          .reverse();
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

const retroBaseDirAbs = resolvePsiPath(root, "ψ/memory/retrospectives");
const latestRetroHit = collectRecentRetros(retroBaseDirAbs, 1)[0];
dlog(`retroBaseDir=${retroBaseDirAbs}`);
dlog(`latestRetro=${latestRetroHit ? latestRetroHit.file : "(none)"}`);

const handoffDirAbs = resolvePsiPath(root, "ψ/inbox/handoff");
let handoffs: string[] = [];
if (existsSync(handoffDirAbs)) {
  try {
    handoffs = readdirSync(handoffDirAbs)
      .filter((f) => f.endsWith(".md") && !f.includes("CLAUDE"))
      .sort()
      .reverse();
  } catch {}
}
dlog(`handoffDir=${handoffDirAbs}`);
dlog(`handoffs.count=${handoffs.length}`);

// Git status
await $`git config core.quotePath false`.quiet();
const status = (await $`git status --porcelain`.text()).trim();
const lines = status ? status.split('\n') : [];

const modified = lines.filter(l => l.startsWith(' M'));
const untracked = lines.filter(l => l.startsWith('??'));

// Output
const now = new Date();
const time = now.toLocaleTimeString('en', { hour: '2-digit', minute: '2-digit', hour12: false });
const date = now.toLocaleDateString('en', { day: '2-digit', month: 'short', year: 'numeric' });

console.log("# RECAP");
console.log("");
console.log(`🕐 ${time} | ${date}`);
console.log("");
console.log("---");
console.log("");
console.log("## 📅 TODAY");
console.log(schedule);
console.log("");
console.log(`## 📊 GIT: ${branch} (+${ahead} ahead)`);
console.log(`Last: ${lastCommit}`);
console.log("");

if (modified.length) {
  console.log(`**Modified** (${modified.length}):`);
  modified.forEach(l => console.log(`  ${l.slice(3)}`));
  console.log("");
}

if (untracked.length) {
  console.log(`**Untracked** (${untracked.length}):`);
  untracked.forEach(l => console.log(`  ${l.slice(3)}`));
  console.log("");
}

console.log("---");
console.log("");
console.log("## 📝 LAST SESSION");
if (latestRetroHit) {
  console.log(`Retro (authoritative): ${whenLabel(latestRetroHit)} — ${latestRetroHit.file}`);
} else {
  console.log("Retro (authoritative): (none)");
}

const topHandoffs = handoffs.slice(0, 3);
if (topHandoffs.length) {
  console.log("Handoffs (last 3; optional; can be older):");
  topHandoffs.forEach((h) => console.log(`- ${h}`));
} else {
  console.log("Handoffs (optional): (none)");
}
