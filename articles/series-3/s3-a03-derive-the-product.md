# S3-A3 — Derive the Product from the Path of Least Resistance

**Status:** Not started
**Series position:** 3 of 3 — the synthesis

---

## Thesis

Most teams throw prototypes away. A working thing ran, revealed something, then was deleted.
The insight lived in one engineer's head until a meeting, then evaporated. Running fifty
experiments this way produces nothing accumulated — just a tired team with vague impressions.

The many-MVPs model only produces a derivable product if the experiment history is preserved
in a form that can be read. Not a pile of abandoned repos. Not a folder of screenshots.
A structured record: what was the hypothesis, what was built, what happened, what was revealed,
what changed.

When that history exists, the product isn't chosen — it's derived. The path of least
resistance isn't a metaphor for "easiest to build." It's the direction where the evidence
converges: what users actually did, what was surprisingly easy, what revealed hidden demand,
what consistently failed no matter how it was framed. The product that fits that pattern
exists in the evidence before anyone has consciously decided to build it.

---

## Key Claims

- Preserved experiment history is the primary asset of the many-MVPs model — not the
  prototypes themselves
- The product is derived from the evidence, not chosen from options
- "Path of least resistance" means the direction where evidence converges, not the easiest
  thing to build
- This only works with structured preservation — pile of repos produces nothing; graph of
  outcomes with hypotheses and relationships produces a derivable product
- The experiment history IS the requirements document — it just needs to be read correctly
- Real options theory: preserve the ability to change direction by not committing to
  implementation before the evidence is conclusive

---

## The Derivation Step

After enough experiments, the question is not "which direction should we bet on?" but
"what does the evidence say?" The derivation step reads the accumulated history and asks:

- Where did user behavior consistently surprise us in the same direction?
- Which hypotheses were confirmed by multiple independent experiments?
- What was unexpectedly easy to build — suggesting alignment between the problem and
  available tools?
- What failed consistently regardless of framing — suggesting the problem itself was wrong?
- What produced the most engagement or the strongest "why doesn't this exist?" response?

The product that answers these questions is already latent in the evidence. The derivation
step surfaces it.

## Why Preservation Structure Matters

A pile of abandoned repos preserves the code but not the knowledge. A folder of Loom
recordings preserves observations but not structured findings. A collection of chat logs
preserves the conversation but not the hypothesis-outcome relationship.

The structured record needs:
- The hypothesis stated before the experiment started
- The specific thing built and what it was designed to test
- What actually happened (user behavior, technical surprises, unexpected findings)
- What requirement or finding was produced
- Relationships to other experiments (this confirmed S3, this contradicted E7, this
  made E12 irrelevant)

The relationship layer is what makes derivation possible. Without it, you have a list of
findings. With it, you have a map — and the product is the territory the map describes.

## The Walking Skeleton as Anchor

The walking skeleton pattern provides a useful anchor: the thinnest possible end-to-end
slice of the system that exercises every layer. Early in the many-MVPs process, building
the walking skeleton reveals architectural requirements — what layers exist, how they
connect, where the technical risk actually lives. It's not a product. It's a scaffold
on which experiments can be run.

## Real Options: Don't Commit Until the Evidence Is Conclusive

Kent Beck and Martin Fowler's real options thinking applies here: preserve the ability
to change direction by not committing to implementation before the evidence is conclusive.
Each experiment keeps options open. The many-MVPs model is not about building lots of
throwaway things — it's about deferring the commitment to the real build until the
experiment history makes the right answer obvious.

When the evidence converges, commitment is not a bet. It's a conclusion.

---

## Connection to the Architecture (Series 2)

This is the product discovery reason for the graph-backed memory and evidence bundle
architecture described in Series 2. The graph doesn't just serve code quality — it serves
product derivation. A graph of experiment outcomes, with hypotheses, findings, and
relationships, is the substrate from which a product can be derived.

This is why the architecture is load-bearing, not optional. Without structured preservation,
the many-MVPs model is just prototype fatigue. With it, it's a product development methodology.

---

## Sources

- [Real Options in software development — Kent Beck & Martin Fowler](https://books.google.com/books/about/Planning_Extreme_Programming.html?id=u13hVoYVZa8C)
- [Lessons from Planning Extreme Programming](https://onesoftwaretester.wordpress.com/2018/09/04/lessons-from-kent-beck-and-martin-fowlers-planning-extreme-programming/)
- [The Walking Skeleton — your system's first heartbeat](https://medium.com/@mayantha.jayawardena/the-walking-skeleton-%EF%B8%8F-your-systems-first-heartbeat-61d5f988fa4f)
- [Start Your Project With a Walking Skeleton — Henrico Dolfing](https://www.henricodolfing.com/2018/04/start-your-project-with-walking-skeleton.html)
- [Using Walking Skeleton in Software Development — Medium](https://medium.com/kayvan-kaseb/using-walking-skeleton-approach-in-software-development-943c3d69a8c0)
- [Continuous Discovery Habits — Teresa Torres](https://www.producttalk.org/glossary-discovery-continuous-discovery/)
- [Discovery-Driven Planning — HBR original](https://hbr.org/1995/07/discovery-driven-planning)
- [Jobs to Be Done — Jobs observed behavior vs. stated preferences](https://www.christenseninstitute.org/theory/jobs-to-be-done/)
- [Evolutionary vs. Throwaway Prototyping](https://prototypeinfo.com/evolutionary-prototyping-and-throw-away-prototyping/)
- [Cycles of Disruption with Kent Beck and Martin Fowler — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech)
