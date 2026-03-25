# Thriving Economy — Hackathon Challenge

This file defines the two practical problem statements for this pillar and the top-rated blue sky vision. Read this before reading anything else in the repository.

---

## The Two Problems You're Solving

### Problem 1: Helping Minority-Owned Businesses Identify Relevant City Contract Opportunities

**Score: 26/32 — Strong**

**Statement:**
How might we use technology to help minority-owned businesses in Richmond more easily identify and understand City contracting opportunities that match their capabilities, so that more firms can confidently explore and pursue public work?

**Why this problem matters:**
The City publishes procurement opportunities through its vendor portal, but the portal is designed for vendors already familiar with government contracting. Small or first-time contractors — including minority-owned businesses — struggle to determine which opportunities are relevant, interpret procurement terminology, or understand what the first step toward participation is. The information is public. The barrier is legibility and navigation.

**Build toward:**
- Procurement opportunity finder — plain-language descriptions of open opportunities
- Procurement opportunity translator — converts jargon-heavy listings into business-type-friendly language
- Vendor readiness tool — guides a first-time contractor through what they need before bidding
- Matching interface — a business describes what they do, the tool returns relevant opportunities

**Key constraints:**
- Existing procurement policies and legal requirements cannot be altered
- The existing procurement portal must remain the official source — do not replace it
- Must be accessible to businesses with little or no government contracting experience
- Must not make eligibility determinations or contract award suggestions

**Data sources:**
- City vendor portal: https://mvendor.cgieva.com/Vendor/public/AllOpportunities.jsp?&agencyname=City%20of%20Richmond%20Government
- City Contracts Registry Socrata dataset (xqn7-jvv2)
- Confirm data format before building: API, CSV, or scraping may all be needed

---

### Problem 2: Small Business Navigation & Business Setup Friction

**Score: 24/32 — Strong**

**Statement:**
How might we use technology to improve how emerging and home-based entrepreneurs start and register a business in Richmond so that they can understand the right steps, complete them in the right order, and connect to relevant City services without confusion or repeated handoffs, while respecting existing departmental structures, program eligibility rules, and staffing capacity?

**Why this problem matters:**
First-time entrepreneurs in Richmond must interact with multiple City departments — licensing, Minority Business, Economic Development, code enforcement, and workforce services. There is no clear front door, no coordinated pathway, and no simple way to understand which requirements apply, in what order, or where to go for help. Businesses unknowingly operate out of compliance. Staff spend time redirecting inquiries that a good navigator tool would prevent.

**Build toward:**
- Small business setup navigator — step-by-step guide, plain language, correct sequence
- Business type wizard — answer a few questions about your business, get the specific steps that apply to you
- Staff or nonprofit workflow helper — helps referral organizations route entrepreneurs to the right resource

**Key constraints:**
- Existing departmental roles and structures remain in place — do not redesign City government
- Program eligibility rules must remain intact — do not make eligibility determinations
- Must not claim to be an official City service or provide legal business advice
- Must work within limited staffing capacity — do not build something that requires ongoing City curation

**Data gaps to address before building:**
- The decision tree — which permits apply to which business types, in what order — must be documented (1–2 page artifact). This does not exist yet in this repository.
- Current City website URLs for each relevant department need verification
- A sample "business registration journey" based on a real path would accelerate development significantly

---

## The Blue Sky Vision

### Rebuilding the Pathway Into the Trades — 22/27 — Strong ★ Recommended

**Statement:**
How might we use technology to help more Richmond residents — especially residents from underrepresented communities — discover, prepare for, and persist in high-opportunity trades and technical careers?

**Why this scored well:**
Clear user and lifecycle. The problem is real and documented. Teams can scope to any one of three phases: discover (find out trades careers exist and are viable), prepare (understand what training or certification is required), or persist (navigate barriers to completing a program or keeping a job).

**Hackathon path if you're aiming at this vision:**
Pick one phase of the lifecycle and build for it:
- **Discover:** A trades career explorer for Richmond residents — what jobs exist, what they pay, what training is required
- **Prepare:** A workforce program finder — what training programs exist in Richmond, what do they require, how do you apply
- **Persist:** A navigation tool for apprenticeship programs — what comes after training, who to contact, what barriers to expect

Data challenge: no employer directory or comprehensive workforce program directory currently exists. Teams must curate this content or partner with a workforce organization that has it.

---

## How Your Solution Will Be Judged (Pillar Award)

The Pillar Award uses the following weights. For full category definitions and scoring anchors, see [`/RUBRIC.md`](../../RUBRIC.md) at the hackathon root.

| Category | Weight | What judges are asking |
|----------|--------|------------------------|
| **Impact** | **5** | Does this directly address one of the two problem statements above? |
| **User Value** | 4 | Is there a specific, real user? Does the prototype improve their experience? |
| **Feasibility** | 3 | Could this be piloted by a City department or economic development partner? |
| **Innovation** | 3 | Does the team bring fresh thinking to procurement access or business navigation? |
| **Execution** | 3 | Does a working demo exist? Is the flow coherent? |
| **Equity** | 3 | Does the solution specifically reach minority-owned businesses and first-time entrepreneurs? |

**Score formula:** Sum of (category score 1–5 × weight). Maximum 105.

**Tiebreaker:** User Value score.

**What wins here:** A prototype that makes City contracting more accessible to small and minority-owned businesses, or makes the business registration process navigable for first-time entrepreneurs, using real public data.

**What loses here:** Tools making eligibility or legal determinations, solutions claiming to automate procurement awards, or projects requiring integration with internal City licensing or procurement systems.
