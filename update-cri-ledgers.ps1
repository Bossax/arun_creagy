function Update-MarkdownTable {
    param(
        [string]$Path,
        [string]$Anchor,
        [string]$AppendBlock,
        [string[]]$IdChecks,
        [hashtable]$LineStatusUpdates
    )

    $content = Get-Content -Path $Path -Raw -Encoding UTF8
    $anchorIndex = $content.IndexOf($Anchor)
    if ($anchorIndex -lt 0) { throw "Anchor not found in $Path : $Anchor" }

    $afterAnchor = $content.Substring($anchorIndex + $Anchor.Length)
    $tableRegex = [regex]'(?ms)(?:^[ \t]*\|.*(?:\r?\n|$))+'
    $match = $tableRegex.Match($afterAnchor)
    if (-not $match.Success) { throw "No markdown table found after anchor in $Path : $Anchor" }

    $tableStart = $anchorIndex + $Anchor.Length + $match.Index
    $tableEnd = $tableStart + $match.Length
    $tableBlock = $content.Substring($tableStart, $match.Length)

    foreach ($key in $LineStatusUpdates.Keys) {
        $replacement = $LineStatusUpdates[$key]
        $pattern = "(?m)^(\\|\s*$([regex]::Escape($key))\s*\\|.*?\\|\s*)(Active|Draft)(\s*\\|.*)$"
        $tableBlock = [regex]::Replace($tableBlock, $pattern, ('$1' + $replacement + '$3'))
    }

    $needsAppend = $false
    foreach ($id in $IdChecks) {
        if ($tableBlock -notmatch [regex]::Escape($id)) {
            $needsAppend = $true
        }
    }

    if ($needsAppend) {
        $tableBlock = $tableBlock.TrimEnd("`r","`n") + "`r`n" + $AppendBlock.Trim() + "`r`n"
    }

    $updatedContent = $content.Substring(0, $tableStart) + $tableBlock + $content.Substring($tableEnd)
    Set-Content -Path $Path -Value $updatedContent -Encoding UTF8
}

$evidenceRows = @'
| E-CRI-035 | CRI Phase 2 v4 Final Comparison Memo | ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/comparison/final-comparison-memo.md | output | Phase 2 | current | capacity; methodology; experiment_comparison; linkage | Cross-experiment comparison memo establishing Experiment B as the preferred working default candidate and preserving Experiments A and C as benchmark and stress-test lineage. |
| E-CRI-036 | CRI Phase 2 v4 Interpretation Note Consolidation | ψ/incubate/DCCE/CRI/output/asset_indicator_dictionary/experimental_runs/2026-04-25_interpretation-note-consolidation.md | note | Phase 2 | current | capacity; methodology; guardrails; linkage | Internal guardrail note consolidating overlay limits, activation-chain cautions, and downstream drafting rules before the governance worksheet was hardened further. |
| E-CRI-037 | Feedback on Governance Indicator Dictionary v5 | ψ/incubate/DCCE/CRI/inbox_note/2026-04-27-feedback on governance indicator dictionary v5.md | note | Phase 2 | current | governance; methodology; review; indicator_vetting | Human review note identifying asset-vs-process ambiguity and pushing clearer process wording for planning feedback loops, finance, and data/digital governance. |
| E-CRI-038 | CRI Phase 2 Capacity Tagging Dictionary v5.1 | ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v5.1.md | output | Phase 2 | current | capacity; governance; methodology; indicator_vetting | Revised working-default governance worksheet that carries the Experiment B decision forward into a process-hardened v5.1 baseline while preserving the six-pillar kernel. |
| E-CRI-039 | Coping-Period Fit Analysis for Current CRI Governance and Asset Dictionaries | ψ/incubate/DCCE/CRI/output/2026-04-27_coping-period-fit-analysis.md | note | Phase 2 | current | capacity; governance; asset_process_fit; coping | Focused analysis note testing whether the current governance and asset dictionaries cover emergency response, immediate relief, and early recovery; tagged high potential for next-round refinement. |
'@

$triggerRows = @'
| T-CRI-009 | 2026-04-27 | Experiment-selection follow-through + governance feedback hardening + coping-fit review | Sprint seal / refinement baseline | Phase 2 governance working default; process hardening; coping-period refinement | High | E-CRI-035, E-CRI-036, E-CRI-037, E-CRI-038, E-CRI-039 | Experiment B working default; v5.1 process-hardening; coping-period refinement baseline | D-CRI-012, D-CRI-013 | Logged | After the post-Friday experiment-selection sprint was accepted, targeted critique and follow-on coping analysis hardened the governance worksheet into v5.1 and produced a bounded refinement baseline for the next round. |
'@

$changeRows = @'
| CH-CRI-008 | 2026-04-27 | Sealed the post-experiment governance sprint by carrying the Experiment B working default into a process-hardened v5.1 governance worksheet and by producing a coping-period fit analysis to guide the next refinement round. | T-CRI-009 | Experiment B working default; v5.1 process-hardening; coping-period refinement baseline | D-CRI-012, D-CRI-013 | Converts the Friday-to-Monday sprint from scattered drafting, critique, and analysis artifacts into an explicit milestone: the governance working default is now hardened and the next refinement round has a bounded diagnostic starting point. | This change does not reopen the six-pillar kernel or replace the sealed asset-side baseline. It records the move from experiment selection and critique into a usable revised governance artifact plus a targeted follow-on analysis. |
'@

$deliverableRows = @'
| D-CRI-012 | `output/CRI_Capacity_Tagging_Dictionary_v5.1.md` | Project team, DCCE, Oracle, indicator-vetting users | Revised working-default governance worksheet that hardens v5 into a more process-explicit Phase 2 governance pack while preserving the six-pillar institutional-readiness kernel and cross-cutting CSOS logic. | T-CRI-009 | Experiment B working default; v5.1 process-hardening after targeted critique; governance-process emphasis for next vetting pass | E-CRI-035, E-CRI-036, E-CRI-037, E-CRI-038 | Active | Revisit when the next Thai administrative indicator-vetting pass or v5.2 refinement begins. | Treat as the current canonical governance worksheet downstream of v4/v5. It supersedes v5 as the working governance draft without deleting earlier lineage. |
| D-CRI-013 | `output/2026-04-27_coping-period-fit-analysis.md` | Project team, Oracle, next-round refinement users | Focused analysis note testing whether the current governance and asset dictionaries adequately cover the coping window defined as emergency response, immediate relief, and early recovery. | T-CRI-009 | Coping-period refinement baseline; next-round gap identification for command, relief targeting, shelters, assessment loops, and support uptake | E-CRI-038, E-CRI-039 | Active | Use as the starting diagnostic when scoping v5.2 governance refinement or asset/governance coping-gap adjustments. | Tagged high potential for next-round refinement; this is an internal analytical baseline rather than a stakeholder-facing deliverable. |
'@

Update-MarkdownTable -Path 'ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md' -Anchor '## Table' -AppendBlock $evidenceRows -IdChecks @('E-CRI-035','E-CRI-036','E-CRI-037','E-CRI-038','E-CRI-039') -LineStatusUpdates @{}
Update-MarkdownTable -Path 'ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md' -Anchor '## Trigger table' -AppendBlock $triggerRows -IdChecks @('T-CRI-009') -LineStatusUpdates @{'T-CRI-006'='Logged';'T-CRI-008'='Logged'}
Update-MarkdownTable -Path 'ψ/incubate/DCCE/CRI/CRI-Change-Log.md' -Anchor '## Change log' -AppendBlock $changeRows -IdChecks @('CH-CRI-008') -LineStatusUpdates @{}
Update-MarkdownTable -Path 'ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md' -Anchor '# Deliverable map' -AppendBlock $deliverableRows -IdChecks @('D-CRI-012','D-CRI-013') -LineStatusUpdates @{}

Write-Host 'CRI ledger update script completed.'
