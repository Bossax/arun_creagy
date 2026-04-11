#!/usr/bin/env bun
import { readFile, writeFile } from 'fs/promises';
import { resolve } from 'path';

/**
 * replace-md-table.ts
 * Deterministic block-level replacement for Markdown tables.
 * Bypasses line-based patch diffing failures for AI agents.
 */
async function main() {
  const args = process.argv.slice(2);
  if (args.length < 3) {
    console.error('Usage: bun run scripts/replace-md-table.ts <target_file> "<header_anchor>" <new_table_file>');
    process.exit(1);
  }

  const [targetFile, anchor, newTableFile] = args;
  const targetPath = resolve(process.cwd(), targetFile);
  const newTablePath = resolve(process.cwd(), newTableFile);

  const content = await readFile(targetPath, 'utf-8');
  const newTable = await readFile(newTablePath, 'utf-8');

  const anchorIdx = content.indexOf(anchor);
  if (anchorIdx === -1) {
    console.error(`Error: Anchor "${anchor}" not found in ${targetFile}`);
    process.exit(1);
  }

  const contentAfterAnchor = content.substring(anchorIdx + anchor.length);
  
  // Match the table block: contiguous rows containing '|' characters
  const tableRegex = /(?:^[ \t]*\|.*(?:\r?\n|$))+/m;
  const match = tableRegex.exec(contentAfterAnchor);
  
  if (!match) {
    console.error(`Error: No markdown table found directly after anchor "${anchor}"`);
    process.exit(1);
  }

  const tableStartIdx = anchorIdx + anchor.length + match.index;
  const tableEndIdx = tableStartIdx + match[0].length;

  const before = content.substring(0, tableStartIdx);
  const after = content.substring(tableEndIdx);

  const updatedContent = `${before}\n${newTable.trim()}\n\n${after.trimStart()}`;

  await writeFile(targetPath, updatedContent, 'utf-8');
  console.log(`✅ Successfully replaced table under anchor: "${anchor}"`);
}

main().catch(console.error);