# Vibe Coding Is Gamified Work
### Draft 4 - expanded working draft

---

## Working Note

This version is intentionally overgrown. It is meant to give me more material than I would ever publish: extra transitions, alternate phrasings, extended examples, and more connective tissue than the final essay needs. The point is not to preserve all of it. The point is to make the argument available in enough forms that I can cut it back into my own voice.

---

Every tool has a right phase.

That sounds obvious enough that it almost disappears. A debugger has a right phase. A profiler has a right phase. A napkin sketch has a right phase. A design document has a right phase. A throwaway prototype has a right phase. A production migration plan has a right phase. A test suite has a right phase. A late-night experiment where you are not sure whether the idea is beautiful or stupid absolutely has a right phase.

Vibe coding has a right phase too.

By vibe coding I mean the specific mode of AI-assisted development where code arrives faster than comprehension. You describe what you want, loosely. The model produces something. You do not fully read it. You run it, nudge it, complain about it, ask for a fix, accept part of it, delete part of it, ask for another pass, and gradually discover what you were trying to build by interacting with a stream of artifacts that are not quite right.

That mode can be irresponsible. It can also be exactly correct.

It is exactly correct when the work is exploratory: when you do not yet know the requirements, when the architecture is not settled, when the problem is still foggy, when the first task is not implementation but discovery. In that phase, generation without full comprehension is not necessarily a defect. It can be the whole point. The output does not have to be maintainable. It does not have to be elegant. It may not even have to survive the afternoon. It has to make the problem concrete enough that your own judgment can wake up and start responding.

That is the generous case for vibe coding, and the article needs to keep it. If the piece starts by treating vibe coding as laziness, it loses the plot immediately. The real issue is not that people are enjoying a tool that helps them move. The real issue is that the tool is very good at helping them move before it is equally good at helping them know when to stop moving.

The phase ends. The tool does not know that.

That sentence is the whole article in miniature.

When I am exploring, the low-friction prompt-response loop is useful because I do not yet know what deserves friction. I need something on the screen. I need a half-wrong implementation, a weird suggestion, a concrete failure, a running demo that exposes the missing requirement. I need the model to lower the activation energy. That is a legitimate job. In fact, it is one of the best jobs for current AI coding tools. They are excellent at turning a blank page into a negotiable artifact.

But after exploration, the job changes. The work stops being primarily about generating possible artifacts and starts being about constraining the artifact that is allowed to survive. The questions become different. What must be true? What behavior is forbidden? What are the acceptance criteria? What invariants matter? What has to remain understandable in six months? What is the rollback path? What will another developer be able to verify without trusting the conversation that produced the code?

Those are engineering questions, not momentum questions.

And this is where the phrase "vibe coding is the new doomscrolling" is useful but incomplete. It is useful because it names the felt experience. One more prompt. One more generated diff. One more pass. One more chance that the next answer will finally snap the problem into focus. The next suggestion might be terrible, but it might also be exactly the missing piece. That intermittent payoff creates the familiar continuation loop. You are not staring at a feed of bad news, but you are still inside a system that makes the next turn feel cheap, promising, and available.

Doomscrolling is the hook. Gamification is the mechanism.

Modern AI coding tools increasingly package work as a stream of immediate rewards: suggestions, patches, tests turning green, todo items crossing off, checkpoints, progress summaries, usage metrics, agent plans, session memory, one-click continue, and the variable reward of a suggestion that might be useless or brilliant. They do not need to hand out cartoon badges. They do not need a leaderboard in the corner. A tool can be gameful without looking like a game.

The reward is progress. The score is the diff. The next level is the next green checkmark.

The problem is not that AI coding feels good. The problem is that the tool keeps rewarding the same behavior after the phase of work has changed.

That is a design problem. It is an incentive problem. It is a phase-boundary problem. It is not a moral failing.

---

## The Better Frame

I started with doomscrolling because it is vivid. Most people understand the loop immediately. You open the feed for a reason. The reason may even be legitimate: you want to know what is happening, check one item, answer one question, see whether anything changed. Then the system keeps offering the next item. Each item is easy to consume. Each item suggests another. The end of the session is not built into the shape of the interaction. Stopping has to come from outside the system.

That maps uncomfortably well onto many AI coding sessions.

You open the assistant for a reason. The reason is often legitimate. You need a quick scaffold. You need help remembering an API. You want a first pass at a test. You want to see whether an approach is plausible. The assistant gives you something. The something is incomplete. Now there is another obvious prompt. Fix this. Add that. Explain this error. Try a different approach. Wire up the missing file. Generate the test. Update the docs. Continue.

The loop does not feel like wasting time because the loop produces artifacts. That is what makes it so much more interesting than a simple distraction critique. Vibe coding is not just a feed. It is a feed that sometimes compiles.

That matters. If the article claims that the productivity feeling is fake, it becomes too easy to reject. The productivity feeling is often real. Peng et al.'s Copilot study is important for exactly that reason: in constrained tasks, developers really can finish faster with AI assistance. The reward loop works because the reward is sometimes genuine. It is not a casino where nothing useful ever comes out. It is a workflow where useful output appears often enough to make continuation feel rational.

But doomscrolling as the main frame has two weaknesses.

First, it can sound moralized. It risks implying that developers are weak, careless, addicted, or irresponsible simply because they keep prompting. That is not the argument I want. The better argument is that a tool's defaults shape behavior. People are not separate from their workflows. A continuation-friendly interface makes continuation more likely. A frictionless acceptance path makes acceptance more likely. A visible todo list makes progress feel more legible. A checkpoint makes another experiment feel safe. A one-click continue button makes stopping require more intentionality than continuing.

Second, doomscrolling describes what the loop feels like, not why it persists. It names the experience but does not fully explain the incentive architecture. Gamification gives a more precise vocabulary because it shifts the critique from content pathology to reward design.

Persuasive-technology research gives a useful starting point. Fogg's behavior model says behavior becomes likely when motivation, ability, and a prompt converge. That is a clean way to understand what AI coding tools increasingly do. They raise ability by making implementation easier. They raise motivation by producing visible progress. They prompt continuously through autocomplete, chat interfaces, agent plans, queued follow-ups, and continuation controls.

Motivation, ability, prompt. All three arrive together.

That convergence is incredibly useful when the desired behavior is exploratory motion. If I am stuck, a suggestion is a gift. If I do not know where to start, a first artifact is a doorway. If I need to test whether an idea is even coherent, a rough implementation is better than staring at an empty file while pretending that my architectural taste will eventually descend from the clouds.

But the same convergence becomes risky when the desired behavior changes. Once the work needs specification, verification, and maintainability, the next good action may not be another prompt. It may be stopping to write down acceptance criteria. It may be deleting the prototype. It may be turning a conversation into tests. It may be asking whether the generated abstraction should exist at all. It may be moving from "can the tool make something happen?" to "what behavior are we willing to own?"

A tool optimized for momentum will not naturally tell you that momentum is no longer the goal.

That is the heart of the gamification frame. Gameful systems are not bad because they are pleasant. They are powerful because they make some actions feel rewarding, repeatable, and obvious. If those actions are aligned with the real goal, the system helps. If those actions are misaligned with the real goal, the system can make the wrong behavior feel productive.

This is why I want to avoid simplistic anti-gamification language. Gamification is not a dirty word. A checklist can be useful. A progress indicator can reduce ambiguity. A visible plan can help a team coordinate. A checkpoint can make experimentation safer. A usage dashboard can help a manager understand whether expensive tools are being used responsibly. Even badges and leaderboards can sometimes steer behavior in useful ways.

The problem is not gameful mechanics in general. The problem is gameful mechanics without phase awareness.

A progress bar in an exploratory prototype says, "keep moving, generate options, learn fast." That can be healthy. The same progress bar in a production change can quietly say, "keep moving, finish the generated plan, accept the next patch," when the team should instead be asking, "is this plan correct, is this behavior specified, and do we understand what changed?"

Same mechanic. Different phase. Different risk.
---

## What The Tools Reward

The mechanics are already visible in contemporary AI coding tools, even when nobody calls them gamification.

Autocomplete rewards acceptance. The suggestion appears inline, already placed where your cursor is. It asks almost nothing of you. Press the key and the code exists. The reward is immediate: a line completed, a branch filled in, an API call assembled, a test scaffolded. Even when the suggestion is small, the rhythm matters. Tiny acceptances accumulate into a session where the path of least resistance is to keep letting the tool propose the next move.

Chat rewards continuation. The model answers, but the answer is rarely final. It invites the next clarification. If the code fails, paste the error. If the explanation is vague, ask for a more concrete version. If the approach is too broad, ask for a smaller patch. If the patch works, ask for tests. If the tests fail, ask for a fix. Each turn produces a new object to respond to. The conversation becomes a machine for manufacturing the next obvious action.

Agents reward delegation. An agent that can plan, search, edit, test, and summarize gives the session a shape that resembles work management. There is a plan. There are steps. There are intermediate results. There may be a todo list. There may be a final summary. That structure is useful because it makes complex work visible. It is also risky because visible structure can be mistaken for correct structure. A plan generated by an agent can feel more complete than it is because it is formatted like a plan.

Memory rewards staying in the loop. If the tool remembers the project, the conversation, the preferences, the prior decision, or the local conventions, then the session feels increasingly valuable the longer it runs. Continuity reduces friction. That can be helpful. It can also make stopping feel like losing context, even when stopping is exactly what the work needs.

Checkpoints and reverts reduce the felt cost of continuing. They make experimentation safer, which is good. But they can also convert caution into another reason to continue. If I can always roll back, why not try one more thing? If the agent saved a checkpoint, why not let it attempt the next step? The safety mechanism becomes part of the continuation loop.

Todo lists make momentum legible. Watching tasks move from pending to done is satisfying. It is also a classic gameful pattern: progress becomes visible, discrete, and countable. Again, that is not inherently bad. But the danger is that the todo list measures completion of the plan, not validity of the plan. A wrong plan with crossed-off tasks still creates a feeling of forward motion.

Usage metrics and credits make activity countable. They can help teams manage cost and adoption. They can also subtly shift attention toward volume: requests, acceptances, active users, lines, commits, interactions. Once activity is visible, it can become a proxy for value. That does not require a formal leaderboard. The comparison can be latent. The organization does not need to say "more prompts are better" for people to notice that usage is being measured.

Pull-request generation and auto-review make the work feel closer to completion. A generated PR has a title, a summary, a diff, maybe tests. It looks like a unit of engineering work. But the existence of a PR is not the same as understanding the change. A review checklist is not the same as having the right invariants. A generated summary is not the same as design rationale.

These features are not mistakes. That is important. I do not want to write an article that sounds like it was composed by someone who has never had a tool save him from a tedious afternoon. These features are useful because software work is full of friction, and some of that friction is just waste.

The issue is that friction has categories.

Some friction is accidental. It is the friction of boilerplate, forgotten syntax, bad docs, inconsistent APIs, setup tasks, and repetitive edits. Removing that friction is usually good.

Some friction is cognitive. It is the friction of deciding what should exist, what must be true, what tradeoff is acceptable, and what failure mode matters. Removing that friction is not always good. Sometimes that friction is the work.

Some friction is social. It is the friction of making a change legible to other people: writing a spec, leaving a rationale trail, opening a review, explaining a constraint, documenting why a shortcut is temporary. Removing that friction can make one person faster while making the team slower.

Some friction is governance. It is the friction of approvals, audits, rollback paths, security checks, and policy boundaries. Removing all of it can make a demo feel magical and a production system feel haunted.

AI coding tools are very good at collapsing friction. The question is which friction.

In exploration, collapsing friction is often the point. If I am trying to discover what the problem is, I want to move quickly through many possible shapes. I do not want a ceremony before every experiment. I do not want a full design review before a throwaway renderer prototype. I do not want to write a polished requirements document for an idea that may die in forty minutes. The whole value of the exploratory loop is that it lets me generate enough concrete material for judgment to become possible.

But later, the valuable friction is the phase boundary itself. The work has to slow down long enough to turn discovery into commitment. It has to ask what is now known. It has to name what is allowed to survive. It has to translate a pile of exploratory artifacts into a smaller set of specified behaviors.

That is where current tools are often weak. They make it easy to keep going in the same mode. They do not always make it equally easy to say: stop, summarize the discovered requirements, delete the prototype, write the tests, define the invariants, and only then generate production code.

Vibe coding becomes dangerous when the exploration reward loop quietly becomes the shipping workflow.

That sentence is worth keeping. It is probably one of the load-bearing beams of the article.

---

## The Phase Argument

The distinction that matters is between phases of work.

Not between people who use AI and people who do not. Not between real programmers and fake programmers. Not between craft and automation. Not between typing and prompting. Those debates are loud because they are emotionally available, but they are not the cleanest engineering boundary.

The clean boundary is phase.

Bjarnason et al.'s empirically based model of software prototyping gives useful vocabulary here. It distinguishes exploratory prototypes from evolutionary prototypes. Exploratory prototypes are built to answer a question. They are explicitly throwaway. Their purpose is learning. Once the question has been answered, the prototype has done its job. Evolutionary prototypes are different. They are expected to grow into the final system. Their purpose is not only learning but survival. They have to be built on foundations that can carry future work.

Those two kinds of prototypes may look similar on the screen. Both may compile. Both may have a UI. Both may produce screenshots. Both may be impressive in a demo. But they have different truth conditions.

An exploratory prototype is successful if it teaches the team something important. It can be ugly and still succeed. It can be incomplete and still succeed. It can be deleted and still succeed. In fact, deletion may be evidence that it succeeded. It answered the question, and now the team knows not to build that version.

An evolutionary prototype is successful only if it can continue. It has to tolerate change. It has to be understandable. It has to be testable. It has to be maintainable enough that the next layer does not collapse into the previous one. It cannot hide its assumptions entirely in the conversation that created it.

Vibe coding belongs naturally to the exploratory side. Agentic engineering belongs on the evolutionary side, after the work has acquired constraints.

That is why Karpathy's distinction between vibe coding raising the floor and agentic engineering raising the ceiling is so useful. It avoids the bad binary. The same underlying technology can make it easier for more people to make something and also make expert practitioners more powerful when used inside discipline. The difference is not magic. It is the relationship between the tool and the phase.

Vibe coding raises the floor because it lowers the cost of trying. That is real. A person who would previously have bounced off the blank page can now make a prototype. A founder can explore a workflow. A designer can test an interaction. A backend engineer can rough out a UI. A student can get a program running and then inspect it. A senior engineer can use it to generate a first pass at an unfamiliar integration. Those are meaningful changes.

Agentic engineering raises the ceiling because it lets experienced practitioners delegate work inside constraints. The practitioner is not just asking for code by feel. They are defining the loop the agent runs inside: requirements, tests, invariants, style rules, architecture boundaries, permissions, review gates, rollback paths, audit trails. The agent is not replacing engineering judgment. It is operating inside it.

That distinction makes Karpathy's nanochat decision more interesting, not less. When he said in October 2025 that nanochat was basically handwritten because Claude and Codex agents had been net unhelpful there, the lazy reading is: the inventor of vibe coding admits vibe coding does not work. The better reading is: he recognized the phase. The work required a level of comprehension and control the agents were not providing. Handwriting the code was not a rejection of AI in general. It was a phase-boundary decision.

That is the move I want the article to make. The answer is not "use AI" or "do not use AI." The answer is "know which phase you are in."

If the work is pre-requirements, use the loop. Explore. Generate. Break things. Let the model produce weird artifacts that help you think. Name the experiments as disposable. Keep the scope small enough that deletion is painless.

If the work is requirements-bearing, change modes. Write the acceptance criteria. Define the interfaces. Name the invariants. Decide what evidence would prove the behavior works. Turn the conversation into a spec. Then use the agent inside that harness.

If the work is production-bearing, change modes again. Ask about maintainability, observability, security, rollback, reviewability, and future comprehension. The question is no longer "can the model make this work?" The question is "can we own this after the model leaves?"

The failure mode is not using vibe coding. The failure mode is letting a throwaway loop become a production process because the local rewards keep paying out.

That is a more precise critique than doomscrolling. Doomscrolling says the loop is sticky. Gamification says the loop is sticky because the system rewards continuation. The phase argument says continuation is not always wrong, but it becomes wrong when the task has changed and the reward structure has not.
---

## The Positive Case

I know what the exit looks like because I have seen one.

This matters because I do not want the article to become an anti-tool sermon. I have used the loop. I have benefited from the loop. I have watched it produce something I could not have specified up front. The critique is stronger if it admits that.

<!-- TODO: decide whether to use the project name or "a D3D12 puzzle game I have been building" -->
A D3D12 puzzle game I have been building started exactly where vibe coding should start: with no settled requirements, no finished design, and a set of questions worth answering. The world had existed in my head for a very long time, but that is not the same as a game design. A setting is not a mechanic. A mood is not a renderer. A thirty-year imaginative itch is not an architecture. To turn any of that into software, I needed concrete artifacts.

That is where exploratory AI assistance helped.

grass-field-001 through grass-field-004 were not a roadmap. They were probes. Four column raycast renderer prototypes, each named as a disposable stage, each one answering a specific visual or technical question before being set aside. That naming convention matters more than it might look. The number at the end was a small act of phase discipline. It said: this is a stage, not a forever-system. It said: this artifact exists to answer a question. It said: when the question is answered, the next thing can have a new name.

That is very different from the quiet slide where a prototype becomes the codebase because it is already there.

The RAII extraction work that followed was also bounded. It was not "let the assistant improve the architecture" in some open-ended way. It was renderer phases, a local extraction, a defined shape of improvement. The work had a finish line. It had a scope. It was not an infinite conversation.

Then the Wave Function Collapse notes, the scalar field simulation, and the formal solvability model started to emerge. Those are the tell. They are not just more generated code. They are requirements taking shape. They are the artifacts that exploration was trying to make possible. Once those existed, the work had crossed a boundary. The question was no longer only "what might this be?" It had become "what must this system guarantee?"

That is the moment when vibe coding has done its job.

The important part is not that the project is a game. The game is color. The structural point is that bounded experiments produced a requirements shape. The exploratory phase crystallized into something more definite: a solvability gate, a simulation model, a puzzle system that could be described in terms of constraints instead of vibes.

That is the positive case. Vibe coding did not replace engineering. It created the material that engineering could then organize.

This is where I want to be careful with the language. I do not want to say, "vibe coding works when it produces a good prototype." That is too weak. Lots of things produce prototypes. The stronger claim is: vibe coding works when the prototype is allowed to remain exploratory until it has extracted the knowledge needed for the next phase.

The output of exploration is not the code. The output of exploration is the spec that could not have been written before the exploration.

That sentence may be the cleanest bridge between the personal example and the broader argument. The grass-field prototypes were useful because they were disposable. The WFC notes were valuable because they were not disposable in the same way. The prototypes helped reveal the design. The design then had to become explicit.

That is what good phase transition looks like. It is not dramatic. No trumpet sounds. The tool does not pop up and say, "Congratulations, you have exited vibe coding." The transition appears in artifacts: named experiments, discarded prototypes, notes that become requirements, tests that encode behavior, a narrowing of possibilities, a shift from generating options to defending constraints.

That is also why the transition is easy to miss. From inside the loop, it all feels like the same work. You are still in the editor. You are still prompting. You are still reading output. You are still making changes. But the nature of the work has changed under your feet.

A good workflow needs to make that change visible.

Gameful momentum is excellent at moving work from nothing to something. It is much less reliable at moving work from something to accountable. That line is blunt, but I think it is true. The first move benefits from low friction. Accountability often requires the reintroduction of the right friction.

There is also a lesson here about naming. Disposable things should be named as disposable. Experiments should look like experiments. Spike branches, prototype folders, numbered stages, scratch docs, and explicit "throw this away" notes are not bureaucratic clutter. They are markers that protect the future codebase from the enthusiasm of the present session. They tell the next person, including future me, that this artifact was built to learn, not to last.

The opposite is dangerous. If the prototype has the same name, same directory, same branch, and same process as production code, then the organization has to rely on memory to preserve the distinction. Memory is a bad boundary. It decays. It gets interrupted. It does not survive onboarding. It does not survive a quarter of unrelated work. If the artifact is exploratory, the artifact itself should say so.

That is one of the simplest practical takeaways from the positive case: make the phase visible in the shape of the work.
---

## The Measurements

The empirical record is now interesting enough that the argument does not have to rest on vibes about vibes.

It would be convenient if the evidence said one simple thing. AI coding tools make developers faster. AI coding tools make developers slower. AI coding tools improve quality. AI coding tools harm quality. Pick one, argue loudly, and go home.

But the actual pattern is more useful than that. The evidence is mixed in exactly the way a phase and incentive argument would predict. AI assistance can produce real short-term throughput gains in constrained settings. It can also produce miscalibrated confidence, weaker comprehension, slower performance in mature codebases, integration drag, and persistent quality problems.

That mixed pattern is not a problem for the article. It is the article.

Peng et al.'s Copilot experiment matters because it establishes the positive case. On a bounded programming task, developers using Copilot finished much faster. That is not trivial. It explains why the loop is compelling. If AI assistance never worked, nobody would need a theory of its failure modes. The reason this conversation matters is that the tool often does work, especially when the task is constrained enough that local suggestions are likely to be useful.

That is the reward side of the loop. A suggestion appears. It saves time. A test appears. It gets you unstuck. A small implementation appears. It mostly works. A fix appears. It clears the error. The user learns, reasonably, that continuing can pay off.

Then METR complicates the story in the right direction. Their early-2025 randomized trial put sixteen experienced open-source developers on 246 real tasks in mature repositories they knew well. The developers expected large speedups. Instead, AI tools made them 19% slower while they believed they were roughly 20-24% faster.

That perception gap is central. The shocking part is not only the slowdown. The shocking part is that the developers felt faster. The local experience of assistance did not match the measured outcome. That is exactly the kind of gap a gamified workflow can create: visible progress, frequent feedback, and a strong feeling of motion that does not necessarily translate into system-level productivity.

The local reward signal says: something happened, the assistant helped, the task is moving.
The measured outcome says: the whole job took longer.

Both can be true.

That is why subjective productivity is a dangerous sole metric. The experience of momentum is not meaningless, but it is incomplete. It captures how the work feels from inside the loop. It does not necessarily capture review time, integration cost, rework, lost comprehension, or the future cost of code that nobody fully understands.

Speed is one bill. Comprehension is another.

Shen and Tamkin's work on AI and skill formation is important because it focuses on learning, not just completion. Their findings point toward a risk that is easy to miss in day-to-day tool use: AI assistance can impair conceptual understanding, code reading, and debugging when people are learning an unfamiliar library or domain. That does not mean AI always prevents learning. It means the workflow matters. If the tool supplies working code before the developer has formed a mental model, the developer may finish the task while retaining less of the structure that would help them debug the next one.

That is a different kind of debt. It does not live only in the codebase. It lives in the person or team that now owns the code.

Ahmad's Comprehension Debt paper gives useful vocabulary for this. Black-box acceptance, context mismatch, dependency-induced atrophy, verification bypass: these are not just bad habits. They are ways understanding can be externalized to the tool and then not recovered. The code exists, but the rationale does not. The system works, but the developer cannot confidently explain why. The generated patch passes the immediate check, but the team has not built the mental model that would let them maintain it.

That matters because software is not done when code appears. Software has to be changed. It has to be debugged under pressure. It has to be explained to someone else. It has to survive a handoff. It has to be modified after the original conversation has vanished from working memory.

Liu et al.'s large-scale repository study pushes the point into production. Across 304,362 verified AI-authored commits in 6,275 repositories, they identified 484,606 introduced issues - code smells, bugs, and security vulnerabilities - and 24.2% of those issues survived to the latest revision. That is not a vibes-based objection. It is a durability signal. Some of the issues introduced by AI-authored commits did not get cleaned up by the ordinary churn of future work.

The meta-analysis evidence is useful too because it keeps the piece from overclaiming. The broad picture is not doom. Generative AI can have positive productivity effects. But the effects are heterogeneous, and learning benefits are not reliably positive. That is exactly the nuance the article needs. Benefits are real, but context-sensitive. The question is not whether AI helps. The question is under what phase, with what constraints, measured by what outcomes.

This is where the gamification frame earns its keep.

A gameful workflow can make local progress salient. It can make the next action obvious. It can make activity legible. It can make the user feel effective. None of that guarantees durable understanding, maintainability, or quality. In fact, those deeper outcomes are often delayed. They do not pay out every thirty seconds. They do not flash green. They do not always appear in a usage dashboard. They show up later, during review, debugging, integration, onboarding, and maintenance.

That lag matters. Rewards that arrive immediately can dominate costs that arrive later.

The core measurement problem is therefore not just time-to-completion. It is the mismatch between what the tool rewards and what the engineering system eventually needs. If the tool rewards accepted suggestions, completed todos, longer sessions, and generated diffs, but the organization needs retained understanding, review depth, defect reduction, and integration stability, then the measurement layer is misaligned.

A better metric suite would look different. It would include time-to-spec, not just time-to-code. It would include spec completeness, not just diff size. It would include prompt-to-accept ratio, blind-accept rate, post-task comprehension, review depth, integration latency, defect introduction, defect survival rate, and the misprediction gap between perceived and actual productivity.

That last one is especially important. The misprediction gap is the gamification danger in a single number: how much more effective did the workflow feel than it actually was?

If a team wants to understand whether AI coding is helping, it cannot only ask whether developers like the tool. It cannot only ask whether they feel faster. It cannot only count how many lines were generated or how many tasks were closed. It has to ask what moved downstream. Did review get harder? Did integration slow down? Did defects survive longer? Did developers retain enough understanding to debug the system later? Did the tool help convert exploration into specification, or did it let exploration masquerade as implementation?

Those are less glamorous questions. They are also the engineering questions.

There is another subtle point here: the studies do not have to prove that AI coding tools are addictive, or that every AI-generated line is suspect, or that every developer becomes less skilled. Those would be overclaims. The empirical evidence only has to show that local assistance, subjective productivity, retained understanding, and durable quality can diverge. Once that divergence exists, the central design question becomes unavoidable: which of those outcomes does the workflow reward most visibly?

Most current workflows reward the visible part. The diff. The passing test. The closed task. The accepted suggestion. The completed agent plan. Those things matter, but they are not the whole system. The hidden variables are where the long-term cost lives.

That is why the article should not argue against speed. Speed is good when it is speed through accidental work. Speed is dangerous when it is speed past understanding. The difference is not visible in a simple productivity chart. It becomes visible only when we measure the phase transition.
---

## Why This Is Not An Anti-AI Argument

This section may or may not survive in the final version, but I want it in the working draft because the article is easy to misread.

The argument is not that developers should stop using AI coding tools. That would be both unrealistic and wrong. The tools are too useful, and the useful parts are not accidental. They lower the cost of experimentation. They reduce boilerplate. They help with unfamiliar APIs. They can produce scaffolding, tests, examples, documentation, refactors, and implementation passes that would otherwise consume attention.

The argument is also not that manual typing is morally superior. Typing code by hand is not a virtue ritual. If an agent can correctly implement a well-specified behavior inside a harness of tests, constraints, and review gates, forcing a human to type every character is theater. The human role is not keystrokes. The human role is judgment, taste, specification, oversight, and responsibility for the system that remains after the tool has finished.

That point matters because many critiques of vibe coding collapse into nostalgia. They sound like complaints that the new generation is not suffering through the same rituals as the old one. That is not a serious engineering argument. We should automate accidental labor where we can. We should not preserve manual work merely because it used to be the only way to do the job.

But there is a difference between automating labor and outsourcing understanding.

Automating labor says: the behavior is specified, the constraints are known, the tests express what matters, the agent can produce the patch, and the human can review the result at the right level.

Outsourcing understanding says: the agent produced something that seems to work, and now the team owns code whose rationale lives mostly in a vanished conversation.

Those are not the same practice.

The gamification frame helps because it avoids turning the issue into a personality test. The problem is not that some developers are virtuous and others are weak. The problem is that a workflow can reward automation while quietly encouraging the outsourcing of understanding. It can make it easier to continue than to consolidate. It can make it easier to accept than to specify. It can make it easier to generate than to verify.

The answer is not less AI. The answer is better phase control.

A mature AI-assisted workflow should make exploration cheap and transition expensive. That sounds backward until you think about it. Exploration should be cheap because most exploratory artifacts should die. The transition into engineering should be expensive because that is where the team starts making commitments. A commitment should cost something. It should require naming what has been learned, what will be preserved, what will be tested, and what will be thrown away.

Right now, many tools make continuation cheap in every phase.

That is the design flaw.

---

## What Has To Change

The solution is not discipline instead of vibe coding. It is discipline about when to stop.

That stopping point cannot be a vague feeling. The whole problem is that the loop feels good even when it has passed its useful boundary. The stop signal has to be designed into the workflow. It has to appear as an artifact, a checklist, a gate, a mode switch, or a team norm that changes the reward structure.

One simple version is timeboxed exploration. Give the loop a container. For the next hour, the goal is not maintainable code. The goal is to generate options, discover constraints, and identify unknowns. At the end of the hour, the output is not a pull request. The output is a short summary: what we learned, what failed, what looks promising, what assumptions appeared, and what would have to be true before any of this became implementation.

Another version is a specification gate. Before an agent is allowed to implement beyond a small exploratory patch, the developer has to write acceptance criteria. Not a novel. Not a full formal spec. Just enough to say what success means. The gate forces a mode change: from "make something" to "make this behavior under these constraints."

A stronger version is a test-first or contract-first constraint. Before the implementation pass, write the tests, invariants, schemas, or evaluation cases. The agent can help draft them, but the human has to approve the target before the agent fills in the solution. This reverses the reward order. Instead of rewarding generated code first and understanding later, the workflow rewards explicit expectations first and generated code second.

Another useful intervention is friction before repeated continuation. The third consecutive "continue" should not be as cheap as the first. After a few agent turns, the tool could ask for a plan review, a summary of what changed, or a decision about whether the session is still exploration. This is not because users need to be scolded. It is because repeated continuation is exactly where phase-slippage hides.

The friction does not have to be heavy. In fact, it should not be. Heavy process would kill the exploratory value. The point is not to make AI coding miserable. The point is to insert a small moment where the user has to ask: what phase are we in now?

Social-feed friction research is useful here. Design friction can reduce mindless continuation and improve recall, even when users find it annoying. That tradeoff is important. Good engineering design is not always the design that maximizes fluency per click. Sometimes a little annoyance is the system protecting the user from an easier mistake.

For AI coding, healthy friction might look like this:

- Before auto-applying a multi-file patch, ask for the invariant or acceptance criterion it is meant to satisfy.
- Before the third agent continuation, require a summary of what has changed and what remains uncertain.
- Before converting a prototype into a PR, ask which files are exploratory and which are intended to survive.
- Before generating production code, require tests or evaluation cases.
- Before merging AI-authored code, require a human-readable rationale that is not just the agent's own summary of what it did.
- Before reusing session memory, surface what assumptions are being carried forward.

That last point is important. Memory is powerful, but memory without expiration becomes context pollution. If an agent remembers the wrong exploratory assumption, the workflow may keep paying interest on a decision that was never actually made. Phase transitions should therefore include context pruning. What did we learn? What should be preserved? What should be discarded? What was only true for the prototype?

This connects to the broader architecture of the series. RAG, GraphRAG, context architecture, quality gates, and token frugality are not separate topics. They are all ways of answering the same question: what information deserves to be active at this phase of work?

Exploration needs breadth. Specification needs clarity. Implementation needs constraints. Review needs evidence. Maintenance needs durable rationale. A single undifferentiated chat context is a bad fit for all five.

That is why the phase boundary matters so much. It is not just a psychological reminder. It is an information architecture boundary. It changes what context should be loaded, what artifacts matter, what metrics should be tracked, and what actions should feel rewarding.

In exploration, reward novelty and learning.

In specification, reward clarity and testability.

In implementation, reward constraint satisfaction.

In review, reward evidence and comprehensibility.

In maintenance, reward durable rationale and low surprise.

Most AI coding tools currently reward motion across all of those phases. Motion is not enough.

---

## Tool Design Implications

This is also a tool-design argument, not only a workflow argument.

The current generation of AI coding tools is understandably optimized around reducing friction. That is what users notice first. Faster autocomplete, better chat, stronger agents, persistent memory, background work, checkpoints, reverts, task lists, PR generation. The product promise is momentum. You are stuck; now you are not. You had an idea; now it has code. You had an error; now it has a suggested fix. You had a task; now the agent has a plan.

That is a good product promise for exploration.

But mature engineering tools should eventually become phase-aware. They should know that the same feature can mean different things at different moments. A continue button in exploration means "try another route." A continue button in production implementation might mean "accumulate more unreviewed changes." A memory feature in exploration means "remember the shape of what we are trying." A memory feature in maintenance might mean "carry forward assumptions that need audit." A checkpoint in exploration means "experiment safely." A checkpoint near merge time means "make rollback and review evidence explicit."

The UI does not have to become bureaucratic. It just has to stop pretending all continuation is the same.

Imagine an AI coding tool with explicit modes:

- Explore: generate options, prototypes, spikes, and questions. Outputs are marked disposable by default.
- Specify: convert exploration into requirements, acceptance criteria, invariants, and tests.
- Implement: generate changes only against approved constraints.
- Verify: run tests, inspect diffs, check invariants, and produce evidence.
- Maintain: summarize rationale, update docs, prune context, and prepare handoff.

Those modes do not need to be rigid. Real work is messy. But even a visible phase label would make the hidden transition easier to notice. The tool could ask different questions in each mode. It could surface different metrics. It could change what the next suggested action is. It could make "continue" mean something more specific than "do more AI."

In Explore mode, the tool might ask: what question is this prototype answering?

In Specify mode, it might ask: what behavior must survive?

In Implement mode, it might ask: which tests or contracts define success?

In Verify mode, it might ask: what evidence would convince another developer?

In Maintain mode, it might ask: what rationale should future readers see?

That would be a very different reward structure. It would still use AI aggressively. It would not be anti-automation. But it would stop treating momentum as the universal good.

Organizations can approximate this before tools support it natively. They can define their own mode labels in issue templates, PR templates, agent instructions, and team norms. They can require an "exploration output" before implementation. They can mark prototype directories as disposable. They can ban direct promotion of exploratory code without a spec pass. They can add review questions that focus on understanding, not just correctness. They can measure rework and review load, not just AI adoption.

The important move is to separate activity metrics from engineering outcomes.

A dashboard that shows AI usage is not enough. A dashboard that shows accepted suggestions is not enough. A dashboard that shows generated lines is actively suspicious if treated as value. Better questions include: did AI-heavy work increase review time? Did it increase follow-up fixes? Did it reduce time-to-spec or only time-to-first-diff? Did it improve test coverage? Did developers understand the code a week later? Did incidents involve AI-authored areas? Did the team delete exploratory artifacts or accidentally preserve them?

If those questions sound less exciting than a productivity graph, yes. That is because they are engineering questions rather than marketing questions.
---

## A Possible Structure For The Final Cut

This working draft is too long on purpose. If I were cutting it into a publishable essay, I would probably keep the spine and compress most of the evidence.

The spine is:

1. Every tool has a right phase.
2. Vibe coding is correct for exploration.
3. The phase ends; the tool does not know that.
4. Doomscrolling names the feeling, but gamification explains the mechanism.
5. Current AI coding tools reward continuation, visible progress, and cheap next actions.
6. Those rewards align with exploration and misalign with specification, verification, and maintenance.
7. The empirical evidence is mixed in exactly the way this theory predicts: real local gains, unstable comprehension, misperceived productivity, integration and quality costs.
8. The answer is not manual typing. The answer is explicit phase control.

Everything else is material to cut from.

Possible short thesis paragraph:

The problem with vibe coding is not that it feels good. The problem is that AI coding tools increasingly reward the wrong things at the wrong phase of work. Doomscrolling names the felt loop: one more prompt, one more diff, one more chance that the next answer will snap the problem into focus. Gamification explains why the loop persists: immediate rewards, visible progress, cheap continuation, and weak stopping cues. Those mechanics are excellent for exploration. They become dangerous when they continue governing work that now needs specification, verification, and maintainable understanding.

Possible punchier version:

Vibe coding is not the enemy. Phase-slippage is. The same prompt-response loop that helps a team find the problem can also help it avoid noticing that the problem has become engineering. The loop keeps paying out local rewards after the objective has changed.

Possible closing:

Use vibe coding to discover what the thing is. Then stop. Then engineer. The future of software work is not humans heroically typing what agents could generate. It is humans designing the boundaries agents run inside: specs, tests, invariants, review gates, context architecture, and memory that knows when to forget. Everything else is just doomscrolling with a CI pipeline.

Possible very short LinkedIn-style hook:

Vibe coding is not dangerous because it feels good. It is dangerous because the tool keeps rewarding exploration after the work has become engineering.

Possible more formal hook:

The next failure mode in AI-assisted software development is not bad prompts. It is phase-misaligned incentives: tools optimized for momentum being used in phases that require specification, verification, and durable understanding.

Possible personal hook:

I have used vibe coding the way it is supposed to be used. It helped me turn a vague game idea into concrete prototypes, then into requirements I could actually reason about. The problem is not the loop. The problem is never exiting it.

Possible sentence to keep somewhere near the end:

The output of exploration is not the code. The output of exploration is the spec that could not have been written before the exploration.

Possible title variants:

- Vibe Coding Is Gamified Work
- Vibe Coding Is Not Doomscrolling. It Is Gamified Engineering.
- The Problem With Vibe Coding Is The Reward Loop
- Vibe Coding Has A Phase Boundary
- AI Coding Tools Reward The Wrong Things At The Wrong Time

---

## Alternate Angles To Cut From

There are several possible articles hiding inside this draft. The final version probably should not try to be all of them, but naming them helps decide what to keep.

One version is primarily for individual developers. That version asks: how do I know when I am still exploring and when I am avoiding the harder work of specification? The practical answer is to watch the artifact I am producing. If the artifact is a prototype, a question list, a spike branch, or a disposable demo, I am probably still exploring. If the artifact is supposed to be merged, depended on, handed off, or maintained, I am no longer only exploring. At that point, I need a different standard. I need tests, invariants, acceptance criteria, and a record of what I think is true.

That version would be more personal and more operational. It would talk about the moment in an AI session when the loop starts feeling too smooth. It would name the little signs: I am asking for another pass instead of writing down what I learned; I am accepting changes faster than I can explain them; I am using the agent's summary as a substitute for my own understanding; I am letting the existence of a patch convince me that a design decision has been made. Those are not sins. They are signals. They tell me the workflow has shifted from exploration into offloading.

Another version is for engineering leads. That version asks: what should a team measure if it wants AI assistance without letting local productivity theater take over? The answer is not just adoption. Adoption is easy to count and easy to misunderstand. A team can have high adoption and still have worse review load, more rework, weaker ownership, and more defects surviving into later revisions. A better leadership question is: where did the work move? Did writing get faster while review got harder? Did implementation get cheaper while integration got slower? Did junior developers ship more code while retaining less understanding? Did senior developers spend more time supervising agent output than the original estimates assumed?

That version would emphasize organizational incentive design. If a manager praises AI usage volume, the team will learn that usage volume matters. If a dashboard highlights accepted suggestions, accepted suggestions become status. If velocity metrics reward closed tickets without measuring review depth or defect survival, the system will pull people toward generated closure. The problem is not that anyone explicitly says, "please game the system." The problem is that people respond to what the system makes visible.

A third version is for tool designers. That version asks: what would an AI coding tool look like if it understood phases? It would not merely offer stronger agents. It would offer different defaults in different modes. It would make disposable prototypes visibly disposable. It would make specification a first-class artifact, not a thing users do in a separate document if they happen to be disciplined. It would notice repeated continuation and ask whether the session is still exploratory. It would treat memory as something to curate, not merely accumulate. It would make context expiration feel normal. It would make review evidence easier to produce than a vague agent summary.

That version would probably be the most original tool-design argument: the next frontier is not just more capable agents, but better phase-aware interfaces. A stronger model can make phase-slippage worse if the workflow still rewards the wrong action. A better agent that produces larger patches faster may intensify the need for specification gates. More autonomy increases the value of boundaries. The more powerful the tool becomes, the more important it is to know which phase the tool is serving.

A fourth version is about metrics. That article would start with the METR perception gap and build outward. Developers thought they were faster. They were slower. That is the whole problem in one study. Not because the study proves AI always slows experts down, but because it shows the felt signal and the measured outcome can diverge sharply. Once that divergence is possible, every productivity claim has to ask: measured where? At the keyboard? At the pull request? At merge? After review? After the incident? After the next developer has to modify the code?

That metrics version would pair well with the gamification frame because gamified systems often make progress legible at the local level. They give the user something to see. But software engineering outcomes often live at the system level. The gap between local legibility and system outcome is where the trouble starts.

A fifth version is the series-level version. That one uses this article as the opening move for everything that follows. Article 1 says the loop rewards the wrong things at the wrong phase. Article 2 can then say AI amplifies the quality of the codebase around it. Article 3 can say velocity without understanding produces cognitive debt. Article 4 can say documentation fails when it becomes unfiltered generated noise. Article 5 can say constraints are the first real answer. Articles 7 and 8 can say memory architecture matters because context has to be selected, not merely accumulated. Article 10 can say the real architecture is the system of boundaries around the agent, not the agent itself.

That is probably the right version for publication. It needs enough individual, leadership, tool-design, and metrics material to feel grounded, but it should not try to exhaust any one of them. The purpose of Article 1 is to name the failure mode clearly enough that the rest of the series feels inevitable.

The shortest version of that failure mode is still this:

Vibe coding is useful when the goal is discovery. It becomes dangerous when discovery mechanics continue to govern engineering work.

Everything else is evidence, vocabulary, and practical consequence.
---

## References

- Andrej Karpathy / Simon Willison, "vibe coding" definition and context:
  [Simon Willison](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- Karpathy's floor/ceiling distinction and agentic engineering framing:
  [SD Times](https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/)
- Karpathy on nanochat being handwritten:
  [Futurism](https://futurism.com/artificial-intelligence/inventor-vibe-coding-doesnt-work)
- B. J. Fogg, "A Behavior Model for Persuasive Design":
  [ACM DOI](https://dl.acm.org/doi/10.1145/1541948.1541999)
- Chen et al., "Do Persuasive Designs Make Smartphones More Addictive?":
  [local PDF](../papers/arxiv-2106.02604-persuasive-design-smartphones.pdf)
- Ruiz, Molina Leon, and Heuer, "Design Frictions on Social Media":
  [local PDF](../papers/arxiv-2407.18803-design-frictions-social-media.pdf)
- Bennett and Mekler, "Beyond Intrinsic Motivation":
  [local PDF](../papers/arxiv-2410.12991-autonomous-motivation-ux.pdf)
- Ayoup, Costa, and Shihab, "Achievement Unlocked":
  [local PDF](../papers/arxiv-2208.05860-achievement-unlocked-devops-gamification.pdf)
- Almeida et al., "Negative Effects of Gamification in Education Software":
  [local PDF](../papers/arxiv-2305.08346-negative-effects-gamification.pdf)
- Hydari, Adjerid, and Striegel, "Health Wearables, Gamification, and Healthful Activity":
  [local PDF](../papers/arxiv-2301.02767-health-wearables-gamification.pdf)
- Peng et al., "The Impact of AI on Developer Productivity":
  [local PDF](../papers/arxiv-2302.06590-copilot-productivity.pdf)
- Becker et al. / METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity":
  [local PDF](../papers/arxiv-2507.09089-metr-productivity-rct.pdf)
- Waseem et al., "Vibe Coding in Practice: Flow, Technical Debt, and Guidelines":
  [local PDF](../papers/arxiv-2512.11922-vibe-coding-in-practice.pdf)
- Shen and Tamkin, "How AI Impacts Skill Formation":
  [local PDF](../papers/arxiv-2601.20245-ai-skill-formation.pdf)
- Ahmad, "Comprehension Debt in GenAI-Assisted Software Engineering Projects":
  [local PDF](../papers/arxiv-2604.13277-comprehension-debt.pdf)
- Liu et al., "Debt Behind the AI Boom":
  [local PDF](../papers/arxiv-2603.28592-debt-behind-ai-boom.pdf)
- Maier et al., "A meta-analysis of the effect of generative AI on productivity and learning in programming":
  [local PDF](../papers/arxiv-2605.04779-genai-productivity-learning-meta-analysis.pdf)
- Bjarnason et al., "An empirically based model of software prototyping":
  [Springer DOI](https://doi.org/10.1007/s10664-023-10331-w)

---

*Systems Engineering Applied to Agentic Systems is a series about making that stop signal explicit - and understanding why, without it, the loop does not end on its own.*