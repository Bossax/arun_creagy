import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';

// Resolve assets
const SKILL_ROOT = dirname(dirname(__filename));
const MCP_ASSET = join(SKILL_ROOT, 'assets/mcp-fleet.json');
const MANDATE_ASSET = join(SKILL_ROOT, 'assets/SILICON_MANDATES.md');
const DOCKER_TEMPLATE_ASSET = join(SKILL_ROOT, 'assets/docker-compose.service-template.yml');
const BRAIN_ROOT = 'ψ';

const PILLARS = [
  'inbox/signals', 'inbox/shipments', 'memory/resonance', 'memory/learnings',
  'memory/retrospectives', 'memory/logs', 'writing', 'lab', 'active',
  'archive/signals', 'outbox', 'learn'
];

/**
 * Surgical merge of MCP configuration
 */
function mergeMcpConfig(targetPath: string, fleetConfig: any, containerName: string) {
  let existing = { mcpServers: {} };
  if (existsSync(targetPath)) {
    try {
      existing = JSON.parse(readFileSync(targetPath, 'utf8'));
    } catch (e) {
      console.warn(`⚠️  Could not parse ${targetPath}, starting fresh.`);
    }
  }

  const fleetServers = fleetConfig.servers;
  for (const [name, config] of Object.entries(fleetServers) as [string, any][]) {
    const serialized = JSON.stringify(config).replace(/{{ORACLE_CONTAINER}}/g, containerName);
    existing.mcpServers[name] = JSON.parse(serialized);
  }

  writeFileSync(targetPath, JSON.stringify(existing, null, 2));
  console.log(`✅ MCP Fleet merged into ${targetPath}.`);
}

/**
 * Verify docker-compose.yml for drift
 */
function checkDockerCompose(containerName: string, projectName: string) {
    const DOCKER_COMPOSE_PATH = 'C:/Users/sitth/OracleWorkspace/docker-compose.yml';
    if (!existsSync(DOCKER_COMPOSE_PATH) || !existsSync(DOCKER_TEMPLATE_ASSET)) {
        console.warn('⚠️ docker-compose.yml or template not found. Skipping drift detection.');
        return;
    }

    const composeContent = readFileSync(DOCKER_COMPOSE_PATH, 'utf8');
    const templateContent = readFileSync(DOCKER_TEMPLATE_ASSET, 'utf8')
        .replace(/{{ORACLE_CONTAINER}}/g, containerName)
        .replace(/{{PROJECT_NAME}}/g, projectName);

    if (!composeContent.includes(`container_name: ${containerName}`)) {
        console.log(`🔎 Drift Detected: Service ${containerName} not found. Appending...`);
        const updatedCompose = composeContent.replace(/services:/, `services:\n${templateContent}`);
        writeFileSync(DOCKER_COMPOSE_PATH, updatedCompose);
        console.log('✅ Service block appended.');
    } else {
        // Basic check for volume drift
        if (!composeContent.includes(`./${projectName}:/vault`)) {
            console.log(`❌ Drift Detected: Incorrect volume mounts for ${containerName}. Manual review needed.`);
            // In a real scenario, you might patch this, but for safety, we'll just report.
        } else {
            console.log('✅ Docker service appears correct.');
        }
    }
}


async function anchorEnvironment() {
  console.log('🌉 [Oracle] Initiating Idempotent Anchoring (v2.0.0)...');

  // 1. Args & Identity
  const args = process.argv.slice(2);
  const cwd = args.find(a => a.startsWith('--cwd='))?.split('=')[1] || process.cwd();
  
  const projectName = cwd.split(/[\\/]/).pop() || 'archon';
  const containerName = projectName === 'archon' ? 'oracle-archon' : `oracle-${projectName.toLowerCase()}`;

  // 2. Physical Anchor Drift Detection
  checkDockerCompose(containerName, projectName);

  // 3. Brain Integrity
  PILLARS.forEach(pillar => {
    const path = join(BRAIN_ROOT, pillar);
    if (!existsSync(path)) {
      mkdirSync(path, { recursive: true });
      console.log(`✨ Restored pillar: ${pillar}`);
    }
  });

  // 4. Mandates
  if (existsSync(MANDATE_ASSET)) {
    const mandates = readFileSync(MANDATE_ASSET, 'utf8');
    const targetPaths = ['.gemini/GEMINI.md', '.roo/rules/00-rule.md', '.roo/rules/silicon-anchor.md'];
    targetPaths.forEach(p => {
      if (!existsSync(dirname(p))) mkdirSync(dirname(p), { recursive: true });
      writeFileSync(p, mandates);
});
    console.log(`✅ Mandates injected.`);
  }

  // 5. MCP Merge
  if (existsSync(MCP_ASSET)) {
    const fleetConfig = JSON.parse(readFileSync(MCP_ASSET, 'utf8'));
    mergeMcpConfig('.gemini/settings.json', fleetConfig, containerName);
    mergeMcpConfig('.roo/mcp.json', fleetConfig, containerName);
  }

  console.log('✨ Anchoring Ritual Complete.');
}

anchorEnvironment().catch(err => {
  console.error('❌ Ritual Failed:', err);
  process.exit(1);
});
