import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync, copyFileSync } from 'fs';
import { join } from 'path';

/**
 * /lab — Oracle Skill Factory & Genesis Engine Implementation
 * v2.10.0 (Oracle-Centric Edition)
 */

const LAB_DIR = 'ψ/lab';
const SIGNAL_INBOX = 'ψ/inbox/signals';
const ISSUE_INBOX = 'ψ/inbox/issue';
const REGISTRY_FILE = join(LAB_DIR, 'registry.json');
const CANDIDATES_FILE = join(LAB_DIR, 'candidates.json');
const WORKSPACE_ROOT = '..';

interface FleetMember {
  skills: { [slug: string]: string };
  last_updated?: string;
}

interface ProjectData {
  dev_version: string;
  source_signals?: string[];
  source_issues?: string[];
  stage: 'Incubating' | 'Researching' | 'Shipping' | 'Production';
  ship_to?: string[];
}

interface RegistryDB {
  fleet: { [oracleName: string]: FleetMember };
  projects: { [slug: string]: ProjectData };
}

function loadJSON<T>(file: string): T {
  if (!existsSync(file)) return {} as T;
  try { return JSON.parse(readFileSync(file, 'utf8')); } catch { return {} as T; }
}

function saveJSON(file: string, data: any) {
  writeFileSync(file, JSON.stringify(data, null, 2));
}

function getArgs() {
  const args = process.argv.slice(2);
  const command = args[0];
  const params: Record<string, string | boolean> = {};
  for (let i = 1; i < args.length; i++) {
    if (args[i].startsWith('--')) {
      const key = args[i].slice(2);
      const value = args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true;
      params[key] = value;
      if (typeof value === 'string') i++;
    } else if (!params._) { params._ = args[i]; }
  }
  return { command, params };
}

function updateSkillFrontmatter(content: string, version: string): string {
  const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
  const match = content.match(frontmatterRegex);
  let frontmatter: Record<string, string> = {};
  let body = content;

  if (match) {
    const lines = match[1].split('\n');
    lines.forEach(line => {
      const colonIndex = line.indexOf(':');
      if (colonIndex !== -1) {
        const key = line.substring(0, colonIndex).trim();
        const val = line.substring(colonIndex + 1).trim();
        frontmatter[key] = val;
      }
    });
    body = content.replace(frontmatterRegex, '').trim();
  }

  let desc = frontmatter.description || 'Oracle fleet skill.';
  desc = desc.replace(/^v\d+\.\d+\.\d+\s*\|\s*/, '');
  const finalFrontmatter = ['---', `name: ${frontmatter.name || 'unnamed-skill'}`, `description: v${version} | ${desc}`, '---'].join('\n');
  return `${finalFrontmatter}\n\n${body}`;
}

async function triage() {
  console.log('📡 [Lab] Triage: Identifying candidates...');
  const candidates: Record<string, any> = {};
  const registry = loadJSON<RegistryDB>(REGISTRY_FILE);

  if (existsSync(SIGNAL_INBOX)) {
    readdirSync(SIGNAL_INBOX).filter(f => f.startsWith('SIG-') && f.endsWith('.md')).forEach(file => {
      const content = readFileSync(join(SIGNAL_INBOX, file), 'utf8');
      const titleMatch = content.match(/# (?:Oracle Signal|Production Shipment): (.*)/);
      const title = titleMatch ? titleMatch[1].trim() : 'untitled';
      const slug = title.toLowerCase().replace(/[^a-z0-9]/g, '-');
      if (!registry.projects[slug]) {
        if (!candidates[slug]) candidates[slug] = { slug, type: 'Signal', files: [], oracles: [] };
        candidates[slug].files.push(file);
      }
    });
  }

  if (existsSync(ISSUE_INBOX)) {
    readdirSync(ISSUE_INBOX).filter(f => f.endsWith('.md')).forEach(file => {
      const content = readFileSync(join(ISSUE_INBOX, file), 'utf8');
      const tagsMatch = content.match(/tags:\s*\n\s*-\s*(.*)/);
      const tag = tagsMatch ? tagsMatch[1].trim() : 'general-friction';
      const slug = tag.toLowerCase().replace(/[^a-z0-9]/g, '-');
      if (!registry.projects[slug]) {
        if (!candidates[slug]) candidates[slug] = { slug, type: 'Issue', files: [], oracles: [] };
        if (!candidates[slug].files.includes(file)) candidates[slug].files.push(file);
      }
    });
  }
  saveJSON(CANDIDATES_FILE, candidates);
  console.log(`✅ Triage complete. ${Object.keys(candidates).length} candidates identified.`);
}

function analyze() {
  const registry = loadJSON<RegistryDB>(REGISTRY_FILE);
  const candidates = loadJSON<Record<string, any>>(CANDIDATES_FILE);
  console.log('\n📊 [Lab] Strategic Analysis:');
  console.log('\n--- EXISTING PROJECTS ---');
  for (const [slug, data] of Object.entries(registry.projects)) {
    console.log(`- ${slug.toUpperCase()} | v${data.dev_version} | ${data.stage}`);
  }
  console.log('\n--- NEW CANDIDATES ---');
  for (const c of Object.values(candidates)) {
    console.log(`\nCandidate: [ ${c.slug.toUpperCase()} ] | Source: ${c.files.join(', ')}`);
    const match = Object.keys(registry.projects).find(s => c.slug.includes(s) || s.includes(c.slug));
    console.log(`💡 Recommendation: ${match ? `IMPROVE [${match}]` : `CREATE [${c.slug}]`}`);
  }
}

function ship(name: string, versionArg?: string) {
  const slug = name.toLowerCase().replace(/[^a-z0-9]/g, '-');
  const projectDir = join(LAB_DIR, slug);
  const registry = loadJSON<RegistryDB>(REGISTRY_FILE);
  if (!registry.projects[slug]) return console.error(`❌ Project not found: ${slug}`);

  const skillSource = join(projectDir, 'SKILL.md');
  if (!existsSync(skillSource)) return console.error(`❌ SKILL.md missing in ${slug}`);
  
  const originalContent = readFileSync(skillSource, 'utf8');
  let version = versionArg;
  if (!version) {
    const vMatch = originalContent.match(/description: v(\d+\.\d+\.\d+)/);
    version = vMatch ? vMatch[1] : registry.projects[slug].dev_version || '1.0.0';
  }

  console.log(`🚢 [Lab] Shipping Skill: ${slug} (v${version})...`);
  const productionContent = updateSkillFrontmatter(originalContent, version);

  const targets = registry.projects[slug].ship_to || ['Archon'];

  targets.forEach(member => {
    const memberRoot = (member === 'Archon' || member === '.') ? '.' : join(WORKSPACE_ROOT, member);
    const agentTargets = [join(memberRoot, '.gemini/skills', slug), join(memberRoot, '.roo/skills', slug)];

    agentTargets.forEach(targetDir => {
      try {
        if (!existsSync(targetDir)) mkdirSync(targetDir, { recursive: true });
        writeFileSync(join(targetDir, 'SKILL.md'), productionContent);
        ['scripts', 'assets'].forEach(dir => {
          const s = join(projectDir, dir);
          const d = join(targetDir, dir);
          if (existsSync(s)) {
            if (!existsSync(d)) mkdirSync(d, { recursive: true });
            readdirSync(s).forEach(f => {
              if (!readdirSync(s, { withFileTypes: true }).find(item => item.name === f)?.isDirectory()) {
                copyFileSync(join(s, f), join(d, f));
              } else {
                // Shallow recursive copy for assets subfolders
                const subS = join(s, f);
                const subD = join(d, f);
                if (!existsSync(subD)) mkdirSync(subD, { recursive: true });
                readdirSync(subS).forEach(sf => copyFileSync(join(subS, sf), join(subD, sf)));
              }
            });
          }
        });
        
        // Update Fleet Record
        if (!registry.fleet[member]) registry.fleet[member] = { skills: {} };
        registry.fleet[member].skills[slug] = version;
        registry.fleet[member].last_updated = new Date().toISOString();

      } catch (err: any) { console.error(`❌ Shipment to ${member} failed: ${err.message}`); }
    });
  });

  registry.projects[slug].dev_version = version;
  saveJSON(REGISTRY_FILE, registry);
  console.log('✨ [Lab] Shipment complete and registry updated.');
}

function status() {
  const reg = loadJSON<RegistryDB>(REGISTRY_FILE);
  console.log('\n📡 [Oracle Fleet] Payload Status:');
  console.log(''.padEnd(90, '='));
  console.log(`${'Oracle'.padEnd(20)} | ${'Last Updated'.padEnd(25)} | ${'Installed Skills'}`);
  console.log(''.padEnd(90, '-'));
  for (const [name, data] of Object.entries(reg.fleet)) {
    const skills = Object.entries(data.skills)
      .map(([slug, ver]) => `${slug}(v${ver})`)
      .join(', ') || 'None';
    const updated = data.last_updated ? new Date(data.last_updated).toLocaleString() : 'Never';
    console.log(`${name.padEnd(20)} | ${updated.padEnd(25)} | ${skills}`);
  }
  console.log(''.padEnd(90, '='));

  console.log('\n🏭 [Lab Projects]:');
  for (const [slug, data] of Object.entries(reg.projects)) {
    console.log(`- ${slug.toUpperCase()}: v${data.dev_version} [${data.stage}]`);
  }
}

async function main() {
  const { command, params } = getArgs();
  switch (command) {
    case 'triage': await triage(); break;
    case 'analyze': analyze(); break;
    case 'ship': ship(params._ as string, params.version as string | undefined); break;
    case 'status': status(); break;
    default: console.log('Usage: /lab <status|ship|triage|analyze>');
  }
}

main();
