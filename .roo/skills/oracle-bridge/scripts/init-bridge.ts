import { readFileSync, writeFileSync, existsSync, mkdirSync, readdirSync, unlinkSync } from 'fs';
import { join, dirname, basename } from 'path';

// Resolve assets
const SKILL_ROOT = dirname(dirname(__filename));
const ASSETS_MANDATES = join(SKILL_ROOT, 'assets/mandates');
const MCP_ASSET_PATH = join(SKILL_ROOT, 'assets/mcp-fleet.json');
const DOCKER_TEMPLATE_PATH = join(SKILL_ROOT, 'assets/docker-compose.service-template.yml');
const BRAIN_ROOT = 'ψ';

const PILLARS = [
    'inbox/signals', 'inbox/shipments', 'inbox/issue',
    'memory/resonance', 'memory/learnings', 'memory/retrospectives', 'memory/logs',
    'writing', 'lab', 'learn', 'archive', 'outbox'
];

/**
 * Robust argument extractor
 */
function getArg(prefix: string, fallback: string): string {
    const arg = process.argv.find(a => a.startsWith(prefix));
    if (!arg) return fallback;
    return arg.slice(prefix.length).replace(/^["']|["']$/g, ''); // Remove wrapping quotes
}

/**
 * Slugify text for container naming
 */
function slugify(text: string): string {
    return text.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
}

/**
 * Clean directory of markdown files to prevent "Ghost Mandates"
 */
function sanitizeDir(dirPath: string) {
    if (existsSync(dirPath)) {
        readdirSync(dirPath).filter(f => f.endsWith('.md')).forEach(f => {
            unlinkSync(join(dirPath, f));
        });
        console.log(`🧹 Sanitized: ${dirPath}`);
    }
}

/**
 * Extract Oracle Name from resonance file
 */
function extractOracleName(): string {
    const resonanceDir = join(BRAIN_ROOT, 'memory/resonance');
    if (!existsSync(resonanceDir)) return 'oracle';
    
    const files = readdirSync(resonanceDir).filter(f => f.endsWith('.md'));
    if (files.length === 0) return 'oracle';

    // Heuristic: Prefer files that look like an identity (e.g. "Archon Oracle.md")
    const identityFile = files.find(f => !f.includes('awaken')) || files[0];
    const content = readFileSync(join(resonanceDir, identityFile), 'utf8');
    const match = content.match(/# (.*?)(?::|#|\n|$)/);
    return match ? match[1].trim().split(' ')[0] : 'oracle';
}

/**
 * Surgical Docker-Compose Injection (Fleet-Aware)
 */
function updateDockerCompose(containerName: string, projectName: string) {
    let composePath = 'docker-compose.yml';
    
    // Fleet-Aware: Check project root, then workspace root (parent)
    if (!existsSync(composePath)) {
        const parentPath = join('..', 'docker-compose.yml');
        if (existsSync(parentPath)) {
            composePath = parentPath;
        } else {
            console.warn('⚠️ No docker-compose.yml found at project or workspace root. Skipping service injection.');
            return;
        }
    }

    let composeContent = readFileSync(composePath, 'utf8');
    if (composeContent.includes(`container_name: ${containerName}`)) {
        console.log(`✅ Docker: Service ${containerName} already exists in ${composePath}.`);
        return;
    }

    if (!existsSync(DOCKER_TEMPLATE_PATH)) {
        console.error('❌ Docker template missing!');
        return;
    }

    const template = readFileSync(DOCKER_TEMPLATE_PATH, 'utf8')
        .replace(/{{ORACLE_CONTAINER}}/g, containerName)
        .replace(/{{PROJECT_NAME}}/g, projectName);

    // Find services block and append
    if (composeContent.includes('services:')) {
        composeContent = composeContent.replace('services:', `services:\n  ${template.trim().split('\n').join('\n  ')}`);
        writeFileSync(composePath, composeContent);
        console.log(`🚀 Docker: Appended service ${containerName} to ${composePath}.`);
    }
}

/**
 * Driver for Gemini CLI scaffolding (Ultra-Lean context)
 */
function scaffoldGemini(mandates: { name: string, content: string }[]) {
    const geminiDir = '.gemini';
    const mandatesDir = join(geminiDir, 'mandates');
    if (!existsSync(mandatesDir)) mkdirSync(mandatesDir, { recursive: true });

    sanitizeDir(mandatesDir);

    const imports: string[] = [];
    mandates.forEach(m => {
        const targetPath = join(mandatesDir, m.name);
        writeFileSync(targetPath, m.content);
        imports.push(`@.gemini/mandates/${m.name}`);
    });

    const routerPath = 'GEMINI.md';
    const routerContent = `# Oracle Context\n\n${imports.join('\n')}\n`;
    writeFileSync(routerPath, routerContent);
    console.log('✅ Gemini scaffolding complete (Lean Router).');
}

/**
 * Driver for Roo Code scaffolding
 */
function scaffoldRoo(mandates: { name: string, content: string }[]) {
    const rooRulesDir = '.roo/rules';
    if (!existsSync(rooRulesDir)) mkdirSync(rooRulesDir, { recursive: true });

    sanitizeDir(rooRulesDir);

    mandates.forEach(m => {
        const targetPath = join(rooRulesDir, m.name);
        writeFileSync(targetPath, m.content);
    });
    console.log('✅ Roo Code scaffolding complete.');
}

/**
 * Smart Merge & Syntax Translation
 */
function syncMCP(targetPath: string, containerName: string, isGemini: boolean) {
    if (!existsSync(MCP_ASSET_PATH)) return;

    // Load and strip comments for JSON parsing
    const rawFleetJson = readFileSync(MCP_ASSET_PATH, 'utf8')
        .replace(/\/\/.*$/gm, '') // Strip single line comments
        .replace(/\/\*[\s\S]*?\*\//g, ''); // Strip multi-line comments
    
    let fleetConfig = JSON.parse(rawFleetJson);
    const configStr = JSON.stringify(fleetConfig);

    // 1. Placeholder Resolution
    let resolvedStr = configStr.replace(/{{ORACLE_CONTAINER}}/g, containerName);
    
    // 2. Syntax Translation (Env Vars)
    if (isGemini) {
        resolvedStr = resolvedStr.replace(/{{ENV:(.*?)}}/g, '${$1}');
    } else {
        resolvedStr = resolvedStr.replace(/{{ENV:(.*?)}}/g, '${env:$1}');
    }

    const resolvedConfig = JSON.parse(resolvedStr);

    // 3. Smart Merge
    if (!existsSync(dirname(targetPath))) mkdirSync(dirname(targetPath), { recursive: true });
    let existing: any = {};
    if (existsSync(targetPath)) {
        try { existing = JSON.parse(readFileSync(targetPath, 'utf8')); } catch (e) {}
    }

    if (isGemini) {
        // Gemini: Merge general + mcpServers (Strip Roo-specific alwaysAllow)
        if (resolvedConfig.mcpServers) {
            for (const key in resolvedConfig.mcpServers) {
                delete resolvedConfig.mcpServers[key].alwaysAllow;
            }
        }
        existing.general = { ...existing.general, ...resolvedConfig.general };
        existing.mcpServers = { ...existing.mcpServers, ...resolvedConfig.mcpServers };
    } else {
        // Roo: Strictly mcpServers
        existing.mcpServers = { ...existing.mcpServers, ...resolvedConfig.mcpServers };
    }

    writeFileSync(targetPath, JSON.stringify(existing, null, 2));
    console.log(`✅ Smart Merge: ${isGemini ? 'Gemini' : 'Roo'} MCP synced.`);
}

async function anchorEnvironment() {
    const cwd = getArg('--cwd=', process.cwd());
    const projectDirName = basename(cwd);
    const oracleName = extractOracleName();
    const containerName = `oracle-${slugify(oracleName)}`;

    // AI Summaries (Identity mandates)
    const idSummary = getArg('--identity=', 'Oracle Agent');
    const mission = getArg('--mission=', 'Execute fleet tasks.');

    console.log(`Bridge v3.5.2] Identity: ${oracleName.toUpperCase()}`);

    // 1. Brain Pillars
    PILLARS.forEach(p => {
        const path = join(BRAIN_ROOT, p);
        if (!existsSync(path)) {
            mkdirSync(path, { recursive: true });
            console.log(`✨ Scaffolded pillar: ${p}`);
        }
    });

    // 2. Process Mandates
    const mandates: { name: string, content: string }[] = [];
    if (existsSync(ASSETS_MANDATES)) {
        readdirSync(ASSETS_MANDATES).filter(f => f.endsWith('.md')).forEach(f => {
            let content = readFileSync(join(ASSETS_MANDATES, f), 'utf8');
            if (f.includes('identity')) {
                content = content
                    .replace('{{ORACLE_NAME}}', oracleName.toUpperCase())
                    .replace('{{IDENTITY_SUMMARY}}', idSummary)
                    .replace('{{MISSION_OBJECTIVE}}', mission);
            }
            mandates.push({ name: f, content });
        });
    }

    // 3. Scaffolding
    scaffoldGemini(mandates);
    scaffoldRoo(mandates);

    // 4. CLAUDE.md Router (< 60 lines)
    const claudeSummary = `# Oracle: ${oracleName.toUpperCase()}\n\n` + 
        `**Thinking Companion**: Refer to \`GEMINI.md\` for instruction routing.\n`;
    writeFileSync('CLAUDE.md', claudeSummary);

    // 5. Docker Injection
    updateDockerCompose(containerName, projectDirName);

    // 6. MCP Tool Sync
    syncMCP('.gemini/settings.json', containerName, true);
    syncMCP('.roo/mcp.json', containerName, false);

    console.log('✨ Scaffolding Ritual Complete (v3.5.2).');
}

anchorEnvironment().catch(err => {
    console.error('❌ Failed:', err);
    process.exit(1);
});
