import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync, copyFileSync, statSync } from 'fs';
import { join } from 'path';

const LAB_DIR = 'ψ/lab';
const SHIPMENT_LOG = 'ψ/memory/logs/shipments';
const WORKSPACE_ROOT = '..';

function getArgs() {
  const args = process.argv.slice(2);
  const params: Record<string, string | boolean> = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith('--')) {
      const key = args[i].slice(2);
      const value = args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true;
      params[key] = value;
    }
  }
  return params;
}

function copyRecursiveSync(src: string, dest: string) {
  const stats = statSync(src);
  if (stats.isDirectory()) {
    if (!existsSync(dest)) mkdirSync(dest, { recursive: true });
    readdirSync(src).forEach(childItemName => {
      copyRecursiveSync(join(src, childItemName), join(dest, childItemName));
    });
  } else {
    copyFileSync(src, dest);
  }
}

function ship(projectName: string, version: string) {
  console.log(`🚢 [Archon] Shipping Production Skill: ${projectName} (v${version})...`);
  const projectDir = join(LAB_DIR, projectName);
  
  if (!existsSync(projectDir)) {
    console.error(`❌ Project not found in lab: ${projectName}`);
    return;
  }

  const fleetMembers = readdirSync(WORKSPACE_ROOT, { withFileTypes: true })
    .filter(dirent => {
      if (!dirent.isDirectory() || dirent.name === 'temp' || dirent.name === 'engine' || dirent.name.startsWith('.')) return false;
      // Heartbeat Check: Only ship to folders with a CLAUDE.md manifest
      return existsSync(join(WORKSPACE_ROOT, dirent.name, 'CLAUDE.md'));
    })
    .map(dirent => dirent.name);

  fleetMembers.forEach(member => {
    const memberRoot = join(WORKSPACE_ROOT, member);
    const agentTargets = [
      join(memberRoot, '.gemini/skills', projectName),
      join(memberRoot, '.roo/skills', projectName)
    ];

    console.log(`📦 Delivering Production Payload to ${member}...`);
    agentTargets.forEach(targetDir => {
      try {
        if (!existsSync(targetDir)) mkdirSync(targetDir, { recursive: true });

        // 🧬 ONLY SHIP PRODUCTION ARTIFACTS
        const prodFiles = ['SKILL.md'];
        prodFiles.forEach(file => {
          const src = join(projectDir, file);
          if (existsSync(src)) copyFileSync(src, join(targetDir, file));
        });

        ['scripts', 'assets'].forEach(dir => {
          const srcDir = join(projectDir, dir);
          const destDir = join(targetDir, dir);
          if (existsSync(srcDir)) {
            copyRecursiveSync(srcDir, destDir);
          }
        });
      } catch (err) {
        console.error(`❌ Delivery to ${targetDir} failed:`, err.message);
      }
    });

    // Notify via Signal (Trigger)
    const memberSignals = join(memberRoot, 'ψ/inbox/signals');
    try {
      if (!existsSync(memberSignals)) mkdirSync(memberSignals, { recursive: true });
      const signalId = `SIG-SHIP-${projectName.toUpperCase()}-${version.replace(/\./g, '')}`;
      const signalContent = `---\nsignal_id: "${signalId}"\nsource_oracle: "Archon Oracle"\ntimestamp: "${new Date().toISOString()}"\npriority: "high"\ntags: ["shipment-available", "production-skill"]\n---\n\n# Production Shipment: ${projectName} v${version}\n\nA refined production version of this skill has been integrated into your agent configuration.\n\n**Action Required**: Run the anchoring ritual to apply the latest mandates:\n\n\`\`\`powershell\nbun .gemini/skills/${projectName}/scripts/init-bridge.ts\n\`\`\``;
      writeFileSync(join(memberSignals, `${signalId}.md`), signalContent);
    } catch (err) {
      console.error(`❌ Signal failed for ${member}:`, err.message);
    }
  });

  if (!existsSync(SHIPMENT_LOG)) mkdirSync(SHIPMENT_LOG, { recursive: true });
  const logFile = join(SHIPMENT_LOG, `${new Date().toISOString().split('T')[0]}_prod_shipment_${projectName}_v${version}.json`);
  writeFileSync(logFile, JSON.stringify({ projectName, version, status: "Production Delivered", fleet: fleetMembers }, null, 2));
  
  console.log(`✨ [Archon] Fleet-wide Production Shipment complete.`);
}

const params = getArgs();
if (params.ship) ship(params.ship as string, (params.version as string) || '1.0.2');
