import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname, resolve } from 'path';

// Resolve assets relative to the script's own location within the skill folder
const SKILL_ROOT = dirname(dirname(__filename));
const MCP_ASSET = join(SKILL_ROOT, 'assets/mcp-fleet.json'); 
const MANDATE_ASSET = join(SKILL_ROOT, 'assets/SILICON_MANDATES.md');
const BRAIN_ROOT = 'ψ';

// Fleet Configuration Paths
const WORKSPACE_ROOT = 'C:/Users/sitth/OracleWorkspace';
const DOCKER_COMPOSE_PATH = join(WORKSPACE_ROOT, 'docker-compose.yml');

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

/**
 * Anchors the Oracle's physical container in the fleet docker-compose.yml
 */
function provisionContainer(projectName: string, containerName: string) {
  if (!existsSync(DOCKER_COMPOSE_PATH)) {
    console.warn(`⚠️  docker-compose.yml not found at ${DOCKER_COMPOSE_PATH}. Skipping physical provisioning.`);
    return;
  }

  console.log(`⚓ Provisioning Physical Anchor: ${containerName}...`);
  const composeContent = readFileSync(DOCKER_COMPOSE_PATH, 'utf8');

  // Check if service already exists
  if (composeContent.includes(`container_name: ${containerName}`)) {
    console.log(`✅ Physical anchor already exists for ${containerName}.`);
    return;
  }

  // Determine next available port (starting from 47780 for new oracles)
  const portMatches = composeContent.match(/"(\d{5}):47778"/g) || [];
  const usedPorts = portMatches.map(m => parseInt(m.match(/\d{5}/)![0]));
  const nextPort = usedPorts.length > 0 ? Math.max(...usedPorts) + 1 : 47780;

  const newServiceBlock = `
  ${containerName}:
    image: oven/bun:latest
    container_name: ${containerName}
    ports:
      - "${nextPort}:47778"
    depends_on:
      oracle-archon:
        condition: service_started
    volumes:
      - ./engine:/app
      - ./${projectName}:/vault
      - ./.oracle-data:/root/.arra-oracle-v3
    working_dir: /app
    environment:
      - ORACLE_REPO_ROOT=/vault
      - ORACLE_DATA_DIR=/root/.arra-oracle-v3
      - ORACLE_PORT=47778
    command: bun run server
`;

  // Safely append to services section
  const updatedCompose = composeContent.replace(/services:/, `services:${newServiceBlock}`);
  writeFileSync(DOCKER_COMPOSE_PATH, updatedCompose);
  console.log(`🚀 Physical anchor deployed to port ${nextPort}. Run 'docker-compose up -d' to activate.`);
}

async function anchorEnvironment() {
  console.log('🌉 [Oracle] Initiating Anchoring Ritual...');

  // 1. Project Identity
  const projectDir = process.cwd();
  const projectName = projectDir.split(/[\\/]/).pop() || 'archon';
  const projectSlug = projectName.toLowerCase();
  
  let containerName = 'oracle-archon';
  if (projectSlug.includes('arun')) containerName = 'oracle-arun-creagy';
  else if (projectSlug.includes('susu')) containerName = 'oracle-susu-ocean';
  else if (projectSlug !== 'archon') containerName = `oracle-${projectSlug}`;

  // 2. Physical Provisioning (Host-side)
  provisionContainer(projectName, containerName);

  // 3. Brain Pillars (Registry-side)
  PILLARS.forEach(pillar => {
    const path = join(BRAIN_ROOT, pillar);
    if (!existsSync(path)) {
      console.log(`✨ Creating pillar: ${pillar}`);
      mkdirSync(path, { recursive: true });
    }
  });

  // 4. Mandate Injection (Agent-side)
  if (existsSync(MANDATE_ASSET)) {
    const mandates = readFileSync(MANDATE_ASSET, 'utf8');
    if (!existsSync('.gemini')) mkdirSync('.gemini', { recursive: true });
    writeFileSync('.gemini/GEMINI.md', mandates);
    if (!existsSync('.roo/rules')) mkdirSync('.roo/rules', { recursive: true });
    writeFileSync('.roo/rules/00-rule.md', mandates);
    console.log(`✅ Mandates injected.`);
  }

  // 5. MCP Fleet (Agent-side)
  if (existsSync(MCP_ASSET)) {
    const mcpConfig = JSON.parse(readFileSync(MCP_ASSET, 'utf8'));
    console.log(`🤖 Detected Project: ${projectName} -> Local Oracle Container: ${containerName}`);
    
    let configStr = JSON.stringify({ mcpServers: mcpConfig.servers }, null, 2);
    configStr = configStr.replace(/{{ORACLE_CONTAINER}}/g, containerName);

    if (!existsSync('.gemini')) mkdirSync('.gemini', { recursive: true });
    writeFileSync('.gemini/settings.json', configStr);
    if (!existsSync('.roo')) mkdirSync('.roo', { recursive: true });
    writeFileSync('.roo/mcp.json', configStr);
    console.log(`✅ MCP Fleet registered.`);
  }

  console.log('✨ Anchoring Ritual Complete.');
}

anchorEnvironment().catch(err => {
  console.error('❌ Ritual Failed:', err);
  process.exit(1);
});
