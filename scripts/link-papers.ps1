# link-papers.ps1
# Replaces all external arXiv URLs in article plan files and research.md with
# relative paths to local PDFs in articles/papers/.
# Safe to re-run — already-local links are left unchanged.
#
# Usage: from repo root: .\scripts\link-papers.ps1

$repoRoot   = Split-Path $PSScriptRoot -Parent
$articlesDir = Join-Path $repoRoot "articles"

# Map: arXiv ID -> local filename (no path prefix — added per-file below)
$idToFile = [ordered]@{
  "2507.09089" = "arxiv-2507.09089-metr-productivity-rct.pdf"
  "2604.13277" = "arxiv-2604.13277-comprehension-debt.pdf"
  "2603.28592" = "arxiv-2603.28592-debt-behind-ai-boom.pdf"
  "2512.11922" = "arxiv-2512.11922-vibe-coding-in-practice.pdf"
  "2604.00436" = "arxiv-2604.00436-programming-by-chat.pdf"
  "2601.02410" = "arxiv-2601.02410-vibe-check-protocol.pdf"
  "2604.18538" = "arxiv-2604.18538-fast-and-forgettable.pdf"
  "2602.20206" = "arxiv-2602.20206-mitigating-epistemic-debt.pdf"
  "2601.20112" = "arxiv-2601.20112-enterprise-ai-coding-assistants.pdf"
  "2606.05391" = "arxiv-2606.05391-human-oversight-agentic-systems.pdf"
  "2511.06428" = "arxiv-2511.06428-walking-the-tightrope.pdf"
  "2507.03156" = "arxiv-2507.03156-llm-assistant-developer-productivity.pdf"
  "2503.14281" = "arxiv-2503.14281-xoxo-context-poisoning.pdf"
  "2404.17723" = "arxiv-2404.17723-rag-knowledge-graphs.pdf"
  "2602.20684" = "arxiv-2602.20684-agile-v-koch-wellbrock.pdf"
  "2605.20456" = "arxiv-2605.20456-agentic-agile-v-scope-v.pdf"
  "2512.12791" = "arxiv-2512.12791-beyond-task-completion.pdf"
  "2603.02601" = "arxiv-2603.02601-agentassay.pdf"
  "2308.05381" = "arxiv-2308.05381-v-model-ml-software.pdf"
  "2411.09050" = "arxiv-2411.09050-systems-engineering-llms.pdf"
  "2605.17675" = "arxiv-2605.17675-transparency-traceability-v-model.pdf"
  "2412.05579" = "arxiv-2412.05579-llms-as-judges-survey.pdf"
  "2509.06216" = "arxiv-2509.06216-agentic-se-foundational-pillars.pdf"
  "2603.15676" = "arxiv-2603.15676-automated-self-testing-quality-gate.pdf"
  "2604.26275" = "arxiv-2604.26275-agentic-ai-sdlc.pdf"
  "2510.26309" = "arxiv-2510.26309-graphcompliance.pdf"
  "2110.11984" = "arxiv-2110.11984-coupette-law-smells.pdf"
  "2206.14879" = "arxiv-2206.14879-grimmelmann-programming-languages-law.pdf"
  "2401.01301" = "arxiv-2401.01301-dahl-large-legal-fictions.pdf"
}

# Target files — markdown only. HTML files are excluded because browsers treat
# local file:// PDF links as downloads; the dashboard keeps arXiv URLs instead.
$targets = @(
  Get-ChildItem -Path $articlesDir -Filter "*.md" -File
  Get-ChildItem -Path (Join-Path $articlesDir "series-1") -Filter "*.md" -File -ErrorAction SilentlyContinue
  Get-ChildItem -Path (Join-Path $articlesDir "series-2") -Filter "*.md" -File -ErrorAction SilentlyContinue
  Get-ChildItem -Path (Join-Path $articlesDir "series-3") -Filter "*.md" -File -ErrorAction SilentlyContinue
  Get-ChildItem -Path (Join-Path $articlesDir "series-4") -Filter "*.md" -File -ErrorAction SilentlyContinue
)

$totalChanges = 0

foreach ($f in $targets) {
  # Determine relative prefix based on whether the file is in a subdirectory
  $isSubdir = $f.DirectoryName -ne $articlesDir
  $prefix = if ($isSubdir) { "../papers/" } else { "papers/" }

  $content = Get-Content $f.FullName -Raw -Encoding UTF8
  $original = $content
  $fileChanges = 0

  foreach ($id in $idToFile.Keys) {
    $localPath = "$prefix$($idToFile[$id])"
    # Skip if this file already uses the local path for this ID
    if ($content -match [regex]::Escape($idToFile[$id])) {
      # Already linked locally for this ID — still do the replace in case
      # some links are local and some aren't (partial state)
    }
    # Match all arXiv URL variants for this ID:
    #   https://arxiv.org/abs/ID
    #   https://arxiv.org/pdf/ID
    #   https://arxiv.org/html/IDv1  (any version suffix)
    #   with optional trailing .pdf
    $pattern = "https://arxiv\.org/(?:abs|pdf|html)/$([regex]::Escape($id))(?:v\d+)?(?:\.pdf)?"
    $newContent = $content -replace $pattern, $localPath
    if ($newContent -ne $content) {
      $fileChanges++
      $content = $newContent
    }
  }

  if ($content -ne $original) {
    Set-Content -Path $f.FullName -Value $content -Encoding UTF8 -NoNewline
    Write-Host "UPDATED  $($f.Name)  ($fileChanges ID(s) relinked)" -ForegroundColor Green
    $totalChanges += $fileChanges
  } else {
    Write-Host "no-op    $($f.Name)" -ForegroundColor DarkGray
  }
}

Write-Host ""
Write-Host "Done. $totalChanges link(s) updated across $($targets.Count) files." -ForegroundColor Cyan
Write-Host ""
Write-Host "Links NOT automated (no local file yet):" -ForegroundColor Yellow
Write-Host "  Magesh 2025     -> jels-2025-magesh-hallucination-free.pdf"
Write-Host "  Braz de Souza   -> scidir-2025-braz-de-souza-contract-smells.pdf"
Write-Host "  Bjarnason 2023  -> emse-2023-bjarnason-pam-prototyping.pdf"
Write-Host "  IEEE 10207641   -> ieee-2023-v-model-ai-vv.pdf"
Write-Host "  IEEE 11218044   -> ieee-2025-design-constraints.pdf"
Write-Host "  Milliman Q2 2025 -> milliman-2025-q2-rate-filing-days.pdf"
Write-Host "  Run this script again after saving those files to articles/papers/."
