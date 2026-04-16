import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';

// Resolve assets relative to the script's own location within the skill folder
const SKILL_ROOT = dirname(dirname(__filename));
const MCP_ASSET = join(SKILL_ROOT, 'assets/mcp-fleet.json'); 
const MANDATE_ASSET = join(SKILL_ROOT, 'assets/SILICON_MANDATES.md');
const BRAIN_ROOT = 'ψ';

const PILLARS = [
  'inbox/signals',
  'inbox/shipments',
  'memory/resonance',
  'memory/learnings',
  'memory/retrospectives',
  'memory/logs',
  'writing',
  'lab',
  'active',
  'archive/signals',
  'outbox',
  'learn'
];

async function anchorEnvironment() {
  console.log('🌉 [Oracle] Initiating Anchoring Ritual...');

  // 1. Brain Pillars (R4)
  PILLARS.forEach(pillar => {
    const path = join(BRAIN_ROOT, pillar);
    if (!existsSync(path)) {
      console.log(`✨ Creating pillar: ${pillar}`);
      mkdirSync(path, { recursive: true });
    }
  });

  // 2. Mandate Injection (R3)
  if (existsSync(MANDATE_ASSET)) {
    const mandates = readFileSync(MANDATE_ASSET, 'utf8');
    writeFileSync('.gemini/GEMINI.md', mandates);
    if (!existsSync('.roo/rules')) mkdirSync('.roo/rules', { recursive: true });
    writeFileSync('.roo/rules/00-rule.md', mandates);
    console.log(`✅ Mandates injected.`);
  } else {
    console.warn(`❌ Mandate asset missing at: ${MANDATE_ASSET}`);
  }

  // 3. MCP Fleet (R2)
  if (existsSync(MCP_ASSET)) {
    const mcpConfig = JSON.parse(readFileSync(MCP_ASSET, 'utf8'));
    const config = JSON.stringify({ mcpServers: mcpConfig.servers }, null, 2);
    writeFileSync('.gemini/settings.json', config);
    writeFileSync('.roo/mcp.json', config);
    console.log(`✅ MCP Fleet registered.`);
  } else {
    console.warn(`❌ MCP asset missing at: ${MCP_ASSET}`);
  }

  console.log('✨ Anchoring Ritual Complete.');
}

anchorEnvironment().catch(err => {
  console.error('❌ Ritual Failed:', err);
  process.exit(1);
});
