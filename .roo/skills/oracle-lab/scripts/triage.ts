import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'fs';
import { join, basename } from 'path';

const INBOX_DIR = 'ψ/inbox/signals';
const LAB_DIR = 'ψ/lab';
const CANDIDATES_FILE = join(LAB_DIR, 'candidates.json');

async function triageSignals() {
  console.log('📡 Scanning Oracle Signal Inbox...');
  
  if (!existsSync(INBOX_DIR)) {
    console.error(`❌ Inbox directory not found: ${INBOX_DIR}`);
    return;
  }

  const signals = readdirSync(INBOX_DIR).filter(f => f.startsWith('SIG-') && f.endsWith('.md'));
  
  if (signals.length === 0) {
    console.log('✅ No new signals to triage.');
    return;
  }

  // Load existing candidates
  let candidates: any = {};
  if (existsSync(CANDIDATES_FILE)) {
    candidates = JSON.parse(readFileSync(CANDIDATES_FILE, 'utf8'));
  }

  for (const signalFile of signals) {
    const signalPath = join(INBOX_DIR, signalFile);
    const content = readFileSync(signalPath, 'utf8');
    
    // Extract title from YAML frontmatter or H1 header
    const titleMatch = content.match(/^title:\s*(.*)$/m);
    const h1Match = content.match(/^#\s+(?:Oracle Signal:\s+)?(.*)$/m);
    const title = (titleMatch ? titleMatch[1].trim() : (h1Match ? h1Match[1].trim() : 'untitled-signal'));
    
    // Create slug from title
    const slug = title.toLowerCase()
      .replace(/[^a-z0-9]/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');
      
    const projectDir = join(LAB_DIR, slug);

    console.log(`🔍 Triaging: ${signalFile} -> [${title}] (${slug})`);

    // Add to candidates if not present
    if (!candidates[slug]) {
      candidates[slug] = {
        slug: slug,
        type: "Signal",
        files: [signalFile],
        oracles: []
      };
    } else if (!candidates[slug].files.includes(signalFile)) {
      candidates[slug].files.push(signalFile);
    }

    if (existsSync(projectDir)) {
      console.log(`⚠️ Project directory already exists: ${projectDir}. Skipping incubation.`);
      continue;
    }

    // Phase 2: Incubation (The Sandbox)
    console.log(`🧪 Incubating: Creating project at ${projectDir}`);
    mkdirSync(projectDir, { recursive: true });
    
    // Initialize with standard DRD and Signal reference
    const drdContent = `# Design Requirement Document (DRD): ${title}\n\n**Signal Reference**: ${signalFile}\n**Status**: Incubating\n\n## Summary\nCaptured from Signal: ${signalFile}\n\n> "The architecture must be strong enough to hold shape, but flexible enough to contain the void." 🟦`;
    
    writeFileSync(join(projectDir, 'DRD.md'), drdContent);
    writeFileSync(join(projectDir, 'STATUS.md'), `# Status: Incubating\n\n- [ ] Initial Signal Triage\n- [ ] Research & Trace\n- [ ] Draft Implementation\n- [ ] Validation`);
    
    console.log(`✅ Success: ${signalFile} escalated to ${slug}`);
  }

  // Save updated candidates
  writeFileSync(CANDIDATES_FILE, JSON.stringify(candidates, null, 2));
  console.log('💾 Updated candidates.json');
}

triageSignals().catch(err => {
  console.error('❌ Triage failed:', err);
  process.exit(1);
});
