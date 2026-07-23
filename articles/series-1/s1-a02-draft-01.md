# AI Makes Bad Code Worse
### Draft 1 - expanded working draft / research packet

---

## Working Note

This is for me, not for publication.

The goal is not elegance. The goal is to over-collect usable material so I can later cut this
into an article that sounds like me. Keep the structure loose enough that I can move sections
around, throw half of it away, and still have the argument intact.

What this article has to do:

- inherit A1's gamified-work frame instead of sounding like a generic "AI introduces bugs" piece
- show the first structural consequence of continuation-friendly tooling
- separate two mechanisms clearly: amplification and accumulation
- make the "/compact the session, not the codebase" line earn the article

The article should feel cooler and more analytical than A1. The emotional register is not
"this is ruining software." The register is "the system is doing exactly what it is set up to
do, and that becomes dangerous in debt-heavy zones."

---

## Core Move

A1 says the tool keeps rewarding continuation after the phase should have changed.

A2 says: once that happens, the agent does not generate ideal code. It extends the local
pattern. If the local pattern is healthy, that can be helpful. If the local pattern is already
debt-heavy, ambiguity-heavy, or poorly structured, the assistant becomes a debt multiplier.

Important distinction:

- amplification is what happens inside one interaction with a messy codebase
- accumulation is what happens over many interactions when no review artifact or design gate
  interrupts the loop

That second point matters because otherwise the article becomes "AI mirrors bad code."
That is true but not enough. The series needs something sharper:

The real problem is not only that the agent copies local patterns. It is that the continuation
loop silently installs those outputs into the future working context of the team.

This is the place to say:

> Context windows can be reset. Codebases cannot.

That line is doing real work. It explains why this article belongs after A1 and before A3.

---

## What The Article Must Prove

1. AI assistance is context-amplifying, not value-discriminating.
2. The most confusing parts of a codebase are exactly where teams reach for help.
3. Those same zones are where assistance is most likely to deepen debt rather than resolve it.
4. Once merged, the output becomes part of the next session's context and compounds.
5. This is why "I shipped more" is not yet a win.

Possible framing line:

> The assistant is not extending the architecture. It is extending whatever evidence of
> architecture it can still see.

Possible framing line:

> When the local code is confused, "continue the pattern" is not neutral. It is a hazard.

---

## Research Spine

### 1. Debt in the wild, not only in toy tasks

The Liu et al. paper is the empirical anchor for the whole article.

Use it for scale, not rhetoric:

- 302.6k verified AI-authored commits
- 6,299 GitHub repositories
- 484,366 distinct issues
- code smells dominate
- more than 15% of commits from every assistant introduce at least one issue
- 22.7% of tracked AI-introduced issues survive to the latest version

The force of that result is not "AI sometimes makes mistakes." Of course it does.
The force is lifecycle persistence. This debt is not instantly cleaned up. It lives.

Source:
- [Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild](https://arxiv.org/abs/2603.28592)

### 2. Conversational programming as progressive specification

The Tang et al. "Programming by Chat" paper is useful because it gives behavioral texture to
how these sessions actually unfold:

- iterative refinement rather than complete upfront specification
- redistribution of cognitive work to the assistant
- externalized plans and negotiated autonomy

This helps the article avoid sounding like a complaint about laziness. The workflow is real.
The problem is what happens when progressive specification never upgrades into explicit design
constraints.

Source:
- [Programming by Chat: A Large-Scale Behavioral Analysis of 11,579 Real-World AI-Assisted IDE Sessions](https://arxiv.org/abs/2604.00436)

### 3. Comprehension debt belongs here, but as the companion mechanism

The Ahmad paper is usually doing work in A3, but some of its vocabulary belongs here too:

- AI-as-black-box code acceptance
- context-mismatch debt
- dependency-induced atrophy
- verification-bypass

For A2, the most useful move is this:

The debt is not only in the code. It also accumulates in the team's understanding of the code.
That lets the article bridge into A3 naturally.

Source:
- [Comprehension Debt in GenAI-Assisted Software Engineering Projects](https://arxiv.org/abs/2604.13277)

### 4. The missing gate

One of the quiet arguments in this article:

Traditional code review and architecture discussion at least create occasions where someone has
to ask "why is this structured like this?"

The continuation loop produces outputs without naturally producing those checkpoints.
So debt does not only appear faster. It appears more quietly.

This is why A5 has to exist later. The solution is not "be more careful." The solution is
explicit friction, constraints, and verification structure.

---

## Angle To Push Hard

This article should not be "AI makes code worse in bad codebases."
That is obvious and not memorable enough.

The sharper claim is:

> The very conditions that make developers ask for AI help are often the conditions under which
> AI extension is least trustworthy.

Messy legacy code, poor naming, weak tests, ambiguous behavior, no ADRs, drifting architecture:

- humans find these zones hard
- therefore they are tempting places to offload
- but they are exactly the zones where "continue the pattern" has the least reliable target

That is the trap.

Possible line:

> Teams reach for the assistant where understanding is already thin. That is also where the
> assistant has the least solid substrate to stand on.

---

## Personal / Practical Material To Add

Need at least one first-person section that makes this feel observed rather than assembled.

Possible material:

- the feeling of watching generated code successfully extend a questionable local abstraction
- the experience of accepting a "good enough" patch in a confusing area because the cost of
  understanding the area exceeded the local appetite for friction
- the next session inheriting that patch as if it were trustworthy precedent

This article probably wants one concrete mini-story rather than many.

Maybe:

1. inherited messy region
2. assistant produces a plausible extension
3. patch works
4. patch later becomes the pattern the next prompt extends
5. now the mess is no longer accidental; it has gained momentum

---

## Counterarguments To Handle

### "But AI also helps clean up bad code"

Yes, sometimes.

Need to concede this directly. The claim is not that assistance cannot improve poor code.
The claim is that improvement requires strong human understanding, explicit goals, and usually
additional constraints or cleanup passes. It does not happen automatically by continuation.

### "This is just a problem with weak engineers"

No. The large-scale debt paper and the behavioral session paper are useful here.
The problem is structural:

- the tool mirrors local context
- confusing zones invite delegation
- review gates are optional unless designed in

Blame the incentive architecture, not the user.

### "But shipping faster still matters"

Yes. Do not sound anti-throughput.

The article should say:

The issue is not speed itself. The issue is speed purchased by installing unreviewed local
patterns into the future codebase.

---

## Suggested Structure

1. Quick callback to A1: the loop kept going.
2. First consequence: the assistant extends the local pattern.
3. Explain amplification in debt-heavy zones.
4. Explain accumulation across sessions.
5. Drop the large-scale Liu numbers.
6. Use Programming by Chat to show the workflow shape.
7. Bridge to comprehension debt and A3.
8. End with the "/compact" asymmetry and a teaser that constraints and memory hygiene are
   the only real answer.

---

## Lines Worth Keeping

- Productive vibes, compounding debt.
- The agent extends the pattern, not the ideal.
- Context windows can be reset. Codebases cannot.
- Yesterday's quick win is today's local precedent.
- The assistant is easiest to trust exactly where it is hardest to verify.

---

## Source Pack

Primary papers from the Series 1 corpus:

- [Comprehension Debt in GenAI-Assisted Software Engineering Projects](https://arxiv.org/abs/2604.13277)
  Local target when pulled: `articles/papers/arxiv-2604.13277-comprehension-debt.pdf`
- [Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild](https://arxiv.org/abs/2603.28592)
  Local target when pulled: `articles/papers/arxiv-2603.28592-debt-behind-ai-boom.pdf`
- [Programming by Chat: A Large-Scale Behavioral Analysis of 11,579 Real-World AI-Assisted IDE Sessions](https://arxiv.org/abs/2604.00436)
  Local target when pulled: `articles/papers/arxiv-2604.00436-programming-by-chat.pdf`

Supporting sources already attached to the outline:

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering](https://arxiv.org/abs/2602.20684)
- [Agentic Agile-V: From Vibe Coding to Verified Engineering](https://arxiv.org/abs/2605.20456)
- [The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming](https://arxiv.org/abs/2601.02410)

