> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](methodology.md) for details.

# Participant handout

This file is a copy of [`CHALLENGE.md`](../CHALLENGE.md) plus this cover note so you can share one Markdown document. Official judge categories are described in `RUBRIC.md` at the hackathon repository root (the directory that contains `pillar-repos`). The body below mirrors `CHALLENGE.md` in this repository.

---

# Thriving Economy: Hackathon Challenge

This file defines the two practical problem statements for this pillar and the top-rated blue sky vision. Read this before reading anything else in the repository.

---

## The Two Problems You're Solving

### Problem 1: Helping Minority-Owned Businesses Identify Relevant City Contract Opportunities

**Statement:**
How might we use technology to help minority-owned businesses in Richmond more easily identify and understand City contracting opportunities that match their capabilities, so that more firms can confidently explore and pursue public work?

**Why this problem matters:**
The City publishes procurement opportunities through its vendor portal, but the portal is designed for vendors already familiar with government contracting. Small or first-time contractors, including minority-owned businesses, struggle to determine which opportunities are relevant, interpret procurement terminology, or understand what the first step toward participation is. The information is public. The barrier is legibility and navigation.

**Build toward:**
- Procurement opportunity finder: plain-language descriptions of open opportunities
- Procurement opportunity translator: converts jargon-heavy listings into business-type-friendly language
- Vendor readiness tool: guides a first-time contractor through what they need before bidding
- Matching interface: a business describes what they do, the tool returns relevant opportunities

**Key constraints:**
- Existing procurement policies and legal requirements cannot be altered
- The existing procurement portal must remain the official source: do not replace it
- Must be accessible to businesses with little or no government contracting experience
- Must not make eligibility determinations or contract award suggestions

**Data sources:**
- City vendor portal: https://mvendor.cgieva.com/Vendor/public/AllOpportunities.jsp?&agencyname=City%20of%20Richmond%20Government
- City Contracts Registry Socrata dataset (xqn7-jvv2)
- Confirm data format before building: API, CSV, or scraping may all be needed

#### Participant guide: connecting to the rubric (if you chose this problem)

Optional prompts: judges refer to [`RUBRIC.md`](../../RUBRIC.md).

- **Impact:** Make **City contracting opportunities** legible to minority-owned and smaller firms: portal stays official source.
- **User Value:** A business owner persona and a clearer “is this for me?” or first-step path.
- **Feasibility:** Respect procurement rules; no eligibility or award **determinations**; verify data access realistically.
- **Innovation:** Plain language, matching, or readiness flow beyond copying the portal.
- **Execution:** Demo uses real listings or a faithful sample with clear limits.
- **Equity and inclusion:** Explicitly serve MBEs and first-time bidders.

**What often works well:** Opportunity finder, jargon translator, readiness checklist tied to real sources.

**What to avoid:** Saying who should win a contract or automating eligibility/legal advice.

*Try asking yourself:* Could a small firm tell in two minutes if an RFP is worth a closer look?

---

### Problem 2: Small Business Navigation & Business Setup Friction

**Statement:**
How might we use technology to improve how emerging and home-based entrepreneurs start and register a business in Richmond so that they can understand the right steps, complete them in the right order, and connect to relevant City services without confusion or repeated handoffs, while respecting existing departmental structures, program eligibility rules, and staffing capacity?

**Why this problem matters:**
First-time entrepreneurs in Richmond must interact with multiple City departments: licensing, Minority Business, Economic Development, code enforcement, and workforce services. There is no clear front door, no coordinated pathway, and no simple way to understand which requirements apply, in what order, or where to go for help. Businesses unknowingly operate out of compliance. Staff spend time redirecting inquiries that a good navigator tool would prevent.

**Build toward:**
- Small business setup navigator: step-by-step guide, plain language, correct sequence
- Business type wizard: answer a few questions about your business, get the specific steps that apply to you
- Staff or nonprofit workflow helper: helps referral organizations route entrepreneurs to the right resource

**Key constraints:**
- Existing departmental roles and structures remain in place: do not redesign City government
- Program eligibility rules must remain intact: do not make eligibility determinations
- Must not claim to be an official City service or provide legal business advice
- Must work within limited staffing capacity: do not build something that requires ongoing City curation

**Data gaps to address before building:**
- The decision tree: which permits apply to which business types, in what order: must be documented (1-2 page artifact). This does not exist yet in this repository.
- Current City website URLs for each relevant department need verification
- A sample "business registration journey" based on a real path would accelerate development significantly

#### Participant guide: connecting to the rubric (if you chose this problem)

Optional prompts: [`RUBRIC.md`](../../RUBRIC.md) is authoritative for judges.

- **Impact:** Reduce wrong-door and repeat-handoff friction for **new** Richmond businesses while keeping departments in their lanes.
- **User Value:** Entrepreneur or referral partner with a sequenced, plain-language path (even if partially illustrative).
- **Feasibility:** No fake “official City” chatbot; no legal/business advice claims; document where the decision tree is still hypothetical.
- **Innovation:** Wizard by business type, navigator, or staff helper that beats a static FAQ.
- **Execution:** Coherent flow with labeled gaps.
- **Equity and inclusion:** Home-based and emerging businesses without lawyers or accountants.

**What often works well:** Setup navigator, business-type wizard, referral helper with honest scope.

**What to avoid:** Eligibility engines, legal advice, or pretending the full City journey is wired when it isn’t.

*Try asking yourself:* Could a first-time founder know **what to do next** without calling three departments?

---

## The Blue Sky Vision

### Rebuilding the Pathway Into the Trades

**Statement:**
How might we use technology to help more Richmond residents: especially residents from underrepresented communities: discover, prepare for, and persist in high-opportunity trades and technical careers?

**Why this fits a weekend build:**
Clear user and lifecycle. The problem is real and documented. Teams can scope to any one of three phases: discover (find out trades careers exist and are viable), prepare (understand what training or certification is required), or persist (navigate barriers to completing a program or keeping a job).

**Hackathon path if you're aiming at this vision:**
Pick one phase of the lifecycle and build for it:
- **Discover:** A trades career explorer for Richmond residents: what jobs exist, what they pay, what training is required
- **Prepare:** A workforce program finder: what training programs exist in Richmond, what do they require, how do you apply
- **Persist:** A navigation tool for apprenticeship programs: what comes after training, who to contact, what barriers to expect

Data challenge: no employer directory or comprehensive workforce program directory currently exists. Teams must curate this content or partner with a workforce organization that has it.

**Rubric connection (blue sky):** Not a perfect match to either targeted statement; closest parallels are **workforce discovery** (curate like Problem 1’s data honesty) and **navigation** (like Problem 2’s stepwise guidance). Pick one phase (discover / prepare / persist) and use the corresponding problem’s guide for feasibility and equity framing.

---

## Judges and the rubric

Hackathon judges evaluate prototypes using the shared categories described in [`RUBRIC.md`](../../RUBRIC.md) at the hackathon repository root. That document lists the category names and what judges are asked to consider.

The **Participant guide** sections under each problem above are optional ways to prepare your pitch. They are not official instructions to judges.
