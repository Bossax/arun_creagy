import { readFileSync, writeFileSync, existsSync, mkdirSync, readdirSync } from 'fs';
import { join, dirname, basename } from 'path';

// Resolve assets
const SKILL_ROOT = dirname(dirname(__filename));
const ASSETS_MANDATES = join(SKILL_ROOT, 'assets/mandates');
const MCP_ASSET = join(SKILL_ROOT, 'assets/mcp-fleet.json');
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
 * Driver for Gemini CLI scaffolding
 */
function scaffoldGemini(mandates: { name: string, content: string }[]) {
    const geminiDir = '.gemini';
    const mandatesDir = join(geminiDir, 'mandates');
    if (!existsSync(mandatesDir)) mkdirSync(mandatesDir, { recursive: true });

    const imports: string[] = [];
    mandates.forEach(m => {
        const targetPath = join(mandatesDir, m.name);
        writeFileSync(targetPath, m.content);
        imports.push(`@./mandates/${m.name}`);
    });

    const routerPath = 'GEMINI.md';
    const routerContent = `# Oracle Context\n\n${imports.join('\n')}\n`;
    writeFileSync(routerPath, routerContent);
    console.log('✅ Gemini scaffolding complete.');
}

/**
 * Driver for Roo Code scaffolding
 */
function scaffoldRoo(mandates: { name: string, content: string }[]) {
    const rooRulesDir = '.roo/rules';
    if (!existsSync(rooRulesDir)) mkdirSync(rooRulesDir, { recursive: true });

    mandates.forEach(m => {
        const targetPath = join(rooRulesDir, m.name);
        writeFileSync(targetPath, m.content);
    });
    console.log('✅ Roo Code scaffolding complete.');
}

/**
 * Merge fleet settings into local files
 */
function mergeSettings(targetPath: string, fleetConfig: any) {
    if (!existsSync(dirname(targetPath))) mkdirSync(dirname(targetPath), { recursive: true });
    let existing: any = {};
    if (existsSync(targetPath)) {
        try { existing = JSON.parse(readFileSync(targetPath, 'utf8')); } catch (e) {}
    }

    if (targetPath.endsWith('mcp.json')) {
        existing.mcpServers = { ...existing.mcpServers, ...fleetConfig.servers };
    } else {
        Object.assign(existing, fleetConfig.settings || {});
    }

    writeFileSync(targetPath, JSON.stringify(existing, null, 2));
    console.log(`✅ Fleet settings merged into ${targetPath}.`);
}

async function anchorEnvironment() {
    const cwd = getArg('--cwd=', process.cwd());
    const projectName = basename(cwd) || 'archon';

    // Extract summaries from arguments (deterministic inputs from AI)
    const idSummary = getArg('--identity=', 'Oracle Agent');
    const mission = getArg('--mission=', 'Execute domain tasks.');
    const traits = getArg('--traits=', 'Technical Integrity');

    console.log(`🌉 [Oracle Bridge] Scaffolding for: ${projectName.toUpperCase()}`);

    // 1. Brain Pillars (Deterministic)
    PILLARS.forEach(p => {
        const path = join(BRAIN_ROOT, p);
        if (!existsSync(path)) {
            mkdirSync(path, { recursive: true });
            console.log(`✨ Scaffolded pillar: ${p}`);
        }
    });

    // 2. Process Mandates (Deterministic Transformation)
    const mandates: { name: string, content: string }[] = [];
    if (existsSync(ASSETS_MANDATES)) {
        readdirSync(ASSETS_MANDATES).filter(f => f.endsWith('.md')).forEach(f => {
            let content = readFileSync(join(ASSETS_MANDATES, f), 'utf8');
            if (f.includes('identity')) {
                content = content
                    .replace('{{IDENTITY_SUMMARY}}', idSummary)
                    .replace('{{MISSION_OBJECTIVE}}', mission)
                    .replace('{{CORE_TRAITS}}', traits);
            }
            mandates.push({ name: f, content });
        });
    }

    // 3. Execute Drivers (Deterministic Implementation)
    scaffoldGemini(mandates);
    scaffoldRoo(mandates);

    // 4. Update CLAUDE.md (Router Summary)
    const claudeSummary = `# Oracle: ${projectName.toUpperCase()}\n\n` + 
        `**Identity**: ${idSummary}\n\n` +
        `**Mandates**: Refer to \`ψ/lab/oracle-bridge/assets/mandates/\` for fleet standards.\n`;
    writeFileSync('CLAUDE.md', claudeSummary);

    // 5. Tool Sync (Deterministic Merge)
    if (existsSync(MCP_ASSET)) {
        const fleetConfig = JSON.parse(readFileSync(MCP_ASSET, 'utf8'));
        mergeSettings('.roo/mcp.json', fleetConfig);
        mergeSettings('.gemini/settings.json', fleetConfig);
    }

    console.log('✨ Scaffolding Ritual Complete.');
}

anchorEnvironment().catch(err => {
    console.error('❌ Failed:', err);
    process.exit(1);
});
