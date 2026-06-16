# download-papers.ps1
# Downloads all referenced academic papers to articles/papers/.
# arXiv papers are fetched directly. Papers requiring access are listed at the end.
# Safe to re-run — skips files that already exist.
#
# Usage: from repo root: .\scripts\download-papers.ps1

$outDir = Join-Path $PSScriptRoot "..\articles\papers"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$ua = "Mozilla/5.0 (compatible; research-downloader/1.0)"

$papers = @(
  # --- Series 1: Vibe Coding / Productivity ---
  [pscustomobject]@{ id="2507.09089"; file="arxiv-2507.09089-metr-productivity-rct.pdf";              articles="S1-A1, S1-A3" },
  [pscustomobject]@{ id="2604.13277"; file="arxiv-2604.13277-comprehension-debt.pdf";                 articles="S1-A1, S1-A2, S1-A3" },
  [pscustomobject]@{ id="2603.28592"; file="arxiv-2603.28592-debt-behind-ai-boom.pdf";                articles="S1-A1, S1-A2" },
  [pscustomobject]@{ id="2512.11922"; file="arxiv-2512.11922-vibe-coding-in-practice.pdf";            articles="S1-A1" },
  [pscustomobject]@{ id="2604.00436"; file="arxiv-2604.00436-programming-by-chat.pdf";                articles="S1-A1, S1-A2" },
  [pscustomobject]@{ id="2601.02410"; file="arxiv-2601.02410-vibe-check-protocol.pdf";                articles="S1-A1, S1-A3" },
  [pscustomobject]@{ id="2604.18538"; file="arxiv-2604.18538-fast-and-forgettable.pdf";               articles="S1-A3" },
  [pscustomobject]@{ id="2602.20206"; file="arxiv-2602.20206-mitigating-epistemic-debt.pdf";          articles="S1-A3" },
  [pscustomobject]@{ id="2601.20112"; file="arxiv-2601.20112-enterprise-ai-coding-assistants.pdf";    articles="S1-A3" },
  [pscustomobject]@{ id="2606.05391"; file="arxiv-2606.05391-human-oversight-agentic-systems.pdf";    articles="S1-A3" },
  [pscustomobject]@{ id="2511.06428"; file="arxiv-2511.06428-walking-the-tightrope.pdf";              articles="S1-A3" },
  [pscustomobject]@{ id="2507.03156"; file="arxiv-2507.03156-llm-assistant-developer-productivity.pdf"; articles="S1-A3" },
  [pscustomobject]@{ id="2503.14281"; file="arxiv-2503.14281-xoxo-context-poisoning.pdf";             articles="S1-A6" },
  [pscustomobject]@{ id="2404.17723"; file="arxiv-2404.17723-rag-knowledge-graphs.pdf";               articles="S1-A8" },

  # --- Series 2: V&V / Agile-V ---
  [pscustomobject]@{ id="2602.20684"; file="arxiv-2602.20684-agile-v-koch-wellbrock.pdf";             articles="S2-A2, S1-A10" },
  [pscustomobject]@{ id="2605.20456"; file="arxiv-2605.20456-agentic-agile-v-scope-v.pdf";            articles="S2-A2" },
  [pscustomobject]@{ id="2512.12791"; file="arxiv-2512.12791-beyond-task-completion.pdf";             articles="S2-A2, S2-A5" },
  [pscustomobject]@{ id="2603.02601"; file="arxiv-2603.02601-agentassay.pdf";                         articles="S2-A2, S2-A5" },
  [pscustomobject]@{ id="2308.05381"; file="arxiv-2308.05381-v-model-ml-software.pdf";                articles="S2-A2" },
  [pscustomobject]@{ id="2411.09050"; file="arxiv-2411.09050-systems-engineering-llms.pdf";           articles="S2-A2" },
  [pscustomobject]@{ id="2605.17675"; file="arxiv-2605.17675-transparency-traceability-v-model.pdf";  articles="S2-A2" },
  [pscustomobject]@{ id="2412.05579"; file="arxiv-2412.05579-llms-as-judges-survey.pdf";              articles="S2-A1" },
  [pscustomobject]@{ id="2509.06216"; file="arxiv-2509.06216-agentic-se-foundational-pillars.pdf";    articles="S2-A3" },
  [pscustomobject]@{ id="2603.15676"; file="arxiv-2603.15676-automated-self-testing-quality-gate.pdf"; articles="S2-A4" },
  [pscustomobject]@{ id="2604.26275"; file="arxiv-2604.26275-agentic-ai-sdlc.pdf";                    articles="S2-A4" },

  # --- Series 4: Legal Tech Debt ---
  [pscustomobject]@{ id="2510.26309"; file="arxiv-2510.26309-graphcompliance.pdf";                    articles="S4-A5, S4-A6" },
  [pscustomobject]@{ id="2110.11984"; file="arxiv-2110.11984-coupette-law-smells.pdf";                articles="S4-A1, S4-A3, S4-A4, S4-A5, S4-A7" },
  [pscustomobject]@{ id="2206.14879"; file="arxiv-2206.14879-grimmelmann-programming-languages-law.pdf"; articles="S4-A1, S4-A3, S4-A5" },
  [pscustomobject]@{ id="2401.01301"; file="arxiv-2401.01301-dahl-large-legal-fictions.pdf";          articles="S4-A5, S4-A6" }
)

$ok = 0; $skipped = 0; $failed = @()

foreach ($p in $papers) {
  $dest = Join-Path $outDir $p.file
  if (Test-Path $dest) {
    Write-Host "SKIP  $($p.file)" -ForegroundColor DarkGray
    $skipped++
    continue
  }
  $url = "https://arxiv.org/pdf/$($p.id)"
  try {
    Invoke-WebRequest -Uri $url -OutFile $dest -UserAgent $ua -TimeoutSec 30 -ErrorAction Stop
    $size = [math]::Round((Get-Item $dest).Length / 1KB)
    Write-Host "OK    $($p.file)  ($($size) KB)" -ForegroundColor Green
    $ok++
  } catch {
    Write-Host "FAIL  $($p.file) — $($_.Exception.Message)" -ForegroundColor Red
    $failed += $p.file
    if (Test-Path $dest) { Remove-Item $dest }
  }
  Start-Sleep -Milliseconds 600
}

Write-Host ""
Write-Host "Downloaded: $ok  Skipped: $skipped  Failed: $($failed.Count)" -ForegroundColor Cyan

if ($failed.Count -gt 0) {
  Write-Host "Failed files:" -ForegroundColor Yellow
  $failed | ForEach-Object { Write-Host "  $_" }
}

Write-Host ""
Write-Host "--- Manual downloads required ---" -ForegroundColor Yellow
Write-Host "These have no arXiv preprint. Download and save to articles/papers/ manually."
Write-Host ""
Write-Host "  Magesh et al. 2025 — Hallucination-Free? Assessing AI Legal Research Tools"
Write-Host "  Venue: JELS 2025 (Stanford RegLab)"
Write-Host "  Try: https://reglab.stanford.edu/  or search SSRN"
Write-Host "  Save as: jels-2025-magesh-hallucination-free.pdf"
Write-Host ""
Write-Host "  Braz de Souza et al. 2025 — Software engineering meets legal texts (contract smells)"
Write-Host "  Venue: ScienceDirect / Elsevier 2025"
Write-Host "  Try: ResearchGate or author pages"
Write-Host "  Save as: scidir-2025-braz-de-souza-contract-smells.pdf"
Write-Host ""
Write-Host "  Bjarnason et al. 2023 — Empirically Based Model of Software Prototyping (PAM)"
Write-Host "  Venue: Springer EMSE — doi.org/10.1007/s10664-023-10331-w"
Write-Host "  Try: ResearchGate or author pages (Lund University)"
Write-Host "  Save as: emse-2023-bjarnason-pam-prototyping.pdf"
Write-Host ""
Write-Host "  IEEE 10207641 — Proposed V-Model for AI Verification and Validation"
Write-Host "  Venue: IEEE Xplore — ieeexplore.ieee.org/document/10207641/"
Write-Host "  Try: author preprint search"
Write-Host "  Save as: ieee-2023-v-model-ai-vv.pdf"
Write-Host ""
Write-Host "  IEEE 11218044 — Design-constraint research"
Write-Host "  Venue: IEEE Xplore — ieeexplore.ieee.org/document/11218044"
Write-Host "  Save as: ieee-2025-design-constraints.pdf"
Write-Host ""
Write-Host "  Milliman Q2 2025 — Rate Filing Average Days to Approval"
Write-Host "  Try: milliman.com  (free industry report)"
Write-Host "  Save as: milliman-2025-q2-rate-filing-days.pdf"
