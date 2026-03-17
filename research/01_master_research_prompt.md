# Richmond Small Business Civic Opportunity Brief: A Research Foundation for the 2026 Civic Hackathon

This research brief identifies evidence-based software opportunities aligned with the Mayor's Action Plan Pillar 4 (A Thriving Economy That Leaves No One Behind) and Pillar 7 (A City That Tells Its Stories), specifically targeting two interconnected challenges: empowering minority-owned businesses to navigate City contracting opportunities and simplifying business registration pathways for emerging entrepreneurs. This brief synthesizes Richmond's current public information landscape, existing support infrastructure, user journey friction points, and feasibility constraints to guide hackathon teams toward realistic, high-impact weekend prototypes that respect existing institutions while filling genuine knowledge and navigation gaps.

## Executive Summary: The Core Problems and Opportunity Space

Richmond is experiencing documented growth in minority business ownership, with recent analysis showing that 7.6 percent of businesses in Richmond are Black-owned, representing an increase from 5.6 percent in the prior year and positioning the city among the top ten U.S. cities for Black-owned business concentration[27]. This economic potential, however, faces structural friction at two critical junctures. First, emerging business owners struggle to navigate a fragmented set of regulatory requirements, departmental contact points, and sequencing rules for business registration—a process that requires engagement with the Department of Finance, Planning and Development Review's Zoning Administration, the Virginia Department of Health (for food businesses), state contractor licensing boards, and various specialized agencies depending on industry. Second, businesses seeking to work with the City of Richmond or adjacent institutions face substantial barriers to identifying, understanding, and pursuing procurement opportunities, despite the existence of public data and established supplier programs. These are not generic problems; they are specific to Richmond's institutional architecture, data infrastructure, and the particular mix of support organizations already embedded in the region.

The opportunity is not to replace existing institutions or policy frameworks, but to create intelligence layers—software tools that make existing public information, processes, and opportunities more navigable, discoverable, and legible to the business community. Successful weekend prototypes will work within institutional constraints, respect departmental authority and existing system boundaries, and position themselves as complements to rather than replacements for human support services provided by organizations like the Capital Region Small Business Development Center, Startup Virginia, SCORE, BizWorks, the Jackson Ward Collective, and the newly enhanced programming from the JWC Foundation[7][8][9][42][43].

## Richmond's Business Registration Ecosystem: Current State

### Regulatory Architecture and Fragmentation

Starting a business in Richmond requires navigation of a complex but ultimately documented set of procedures distributed across city departments, state agencies, and industry-specific regulators. The foundational requirement is a **Business, Professional, and Occupational License (BPOL) Tax** registration, managed by the Department of Finance[3]. New businesses must obtain this license within 30 days of opening. However, the BPOL application process has a prerequisite that many first-time entrepreneurs discover late or incompletely: businesses must first obtain a **Certificate of Zoning Compliance (CZC)** from the Planning and Development Review Department's Zoning Administration Division before they can proceed with BPOL registration[3][41]. This sequencing requirement is documented in the city's guidance materials but appears to cause repeated confusion and delays, with entrepreneurs often submitting BPOL applications before completing zoning clearance.

The CZC process itself requires applicants to navigate the city's Online Permit Portal, provide detailed business descriptions, square footage information, and property owner consent[41]. For businesses operating in specific industries, additional regulatory layers activate immediately. **Food businesses** must obtain permits from the Richmond City Health District and comply with Virginia Food and Drink Law, with applications, fees, and inspection requirements varying by whether the operation is a home-based food processing operation, a commercial kitchen operation, a temporary food vendor, or a mobile food unit[6][38]. **Construction contractors** must hold valid Virginia Department of Professional Occupational Regulations (DPOR) licenses before they can legally work, and if their annual work in Richmond exceeds $25,000, they must also hold a Richmond business license[40]. **Sidewalk vendors** must provide evidence of commercial liability insurance naming the city as co-insured, and food vendors must provide health certificates[3]. For businesses involving alcohol service, regulated securities, healthcare delivery, firearms, or other controlled activities, state-level licensing requirements layer on top of city requirements.

This architecture is not inherently inefficient or irrational—it reflects legitimate public health, safety, zoning, and revenue interests—but it is fragmented across institutional boundaries and presented through multiple information channels with varying degrees of clarity and completeness. A business owner seeking to start a cafe with retail merchandise in Jackson Ward must understand and coordinate: city zoning rules (Planning and Development Review), food safety requirements (Richmond City Health District), business registration and tax implications (Department of Finance), possible contractor work (if renovations are needed, DPOR licensing), potential sidewalk vendor regulations (if there is outside seating), possible alcohol service licensing (Virginia Alcoholic Beverage and Cannabis Control Authority), trademark registration (if pursuing trademark protection), and benefits of possible minority business certification (Office of Minority Business Development for city contracting preference)[1][41]. Each of these requirements has its own application form, fee structure, timeline, and point of contact.

### The Department of Finance's New Portal and Business Personal Property Reporting

A significant positive development occurred in January 2025, when the City of Richmond Department of Finance launched a new **RVA Business Portal** designed to streamline Business Personal Property and BPOL License filing for the 2025 period and beyond[3]. This portal represents an attempt to consolidate at least the finance-side registration workflow and is meant to simplify the previously manual filing process. However, the portal addresses only one piece of the larger registration puzzle—it does not eliminate the prerequisite CZC requirement, does not integrate with health department food permitting, does not capture state-level contractor licensing, and does not provide business owners with clear guidance on sequencing or on how city-level registration connects to state and federal requirements (such as federal Employer Identification Number (EIN) acquisition, beneficial ownership reporting, or state tax registration)[3][22].

### Information Architecture and Knowledge Silos

The current-state information landscape reflects a pattern common in government: important procedural knowledge exists in multiple locations with varying levels of completeness, clarity, and discoverability. The Department of Finance's website provides BPOL FAQs that answer common questions such as "Do I need a license to operate my business in the City of Richmond?" and "What basic information do I need to apply for a business license?"[3]. The Planning and Development Review department provides detailed PDF guides for commercial building permits and CZC applications, including step-by-step screenshots of the Online Permit Portal process[40][41]. The Richmond City Health District publishes comprehensive guidance on food establishment permit requirements, distinguishing between home-based operations, commercial kitchens, mobile units, and temporary vendors, with links to Virginia Food and Drink Law[38]. But these resources are scattered across different city department websites, use inconsistent terminology, assume varying levels of prior knowledge, and do not explicitly map dependencies (e.g., "you cannot apply for your BPOL until your CZC is approved") or decision trees (e.g., "if your business involves food, here are the additional steps in the order you should take them").

The most complete orientation material available to new entrepreneurs often comes not from the city directly, but from nonprofit support organizations. The Capital Region SBDC, which has reestablished its presence in Richmond as of 2024, offers free one-on-one business counseling, business assessments, and workshops that explicitly help business owners navigate startup requirements[7]. SCORE, a national nonprofit network providing free mentoring, also serves the Richmond region and offers resources on business registration and legal structure[8]. Startup Virginia, focused on high-growth innovation ventures, offers incubator programs and educational events but primarily serves founders pursuing venture-backed models[9]. BizWorks, a nonprofit focused on main-street businesses, offers membership and structured business development support[42]. The Jackson Ward Collective and the newly enhanced programming at the JWC Foundation offer culturally-centered support specifically for Black business owners, including an incubator launching in June 2026 and monthly skills workshops[43]. These organizations collectively serve hundreds of business owners and provide genuine value, but their existence and the fragmentation of support creates a dynamic where knowledge about how to register a business in Richmond is concentrated in nonprofit staff rather than openly codified in city systems.

### User Confusion Points: Evidence from Indirect Sources

While no recent audit-level study of Richmond business registration friction appears to be publicly available, several indirect signals suggest where confusion concentrates. First, the existence of the BPOL application itself requires applicants to gather and understand specific information: the business name as it will be licensed, the trade name (if different from the licensee name and if not already registered with the Virginia State Corporation Commission), the physical address and mailing address, a description of business type, an ID number (Social Security number or federal EIN), the business begin date, and the business entity type (sole proprietor, partnership, corporation, LLC)[3]. Each of these fields can create confusion or delay for an uninformed applicant. For instance, the distinction between "licensee name" and "trade name" is not obvious, and the requirement to pre-register trade names with the State Corporation Commission before proceeding with city registration creates a sequential dependency that is easily missed. Similarly, the requirement to obtain a federal EIN, while required by the IRS for most businesses, is not framed as a prerequisite in city guidance—an applicant might assume they need to register with the city first to get an EIN, when in reality, the EIN application process should happen independently and in parallel.

Second, the CZC prerequisite for BPOL registration is mentioned in BPOL FAQs but is not prominently featured in introductory materials, and the CZC process itself is managed through a separate portal with separate instructions[3][41]. An entrepreneur might begin filling out a BPOL application, reach a field asking for zoning compliance information, and only then discover they need to apply for a CZC first—a discovery that feels like a system failure rather than a logical sequence. Third, for food businesses, the overlay of Richmond City Health District requirements, Virginia Department of Health regulations, and possible local board of health rulings creates a knowledge burden that is nontrivial. The distinction between a home-based food processing operation (which may qualify for exemptions under certain conditions) and a commercial kitchen operation (which requires a full commercial facility and inspection) is important but not always clear to someone with a food business idea and no prior regulatory experience.

### Data Infrastructure and Open Information

Richmond maintains several public-facing data systems that could support business intelligence. The city's **Open Data Portal** publishes a City Contracts dataset that includes agency name, contract number, contract dollar amount, supplier name, procurement type, and contract end date, updated monthly[12][15]. However, this dataset is historical and transactional rather than forward-looking—it does not help a business owner understand what opportunities are coming or how to position themselves to compete. The **Planning and Development Review Department** maintains an **Online Permit Portal** for submission and tracking of commercial and residential permits[10][40][41]. The city's **RVA311 system** serves as a centralized contact point for city service requests and inquiries, accessible by phone (804-646-7000) or online[3][10][11]. The **Office of Minority Business Development (OMBD)** maintains a vendor registration application and publishes information about available workshops and certification resources[1]. Yet these systems, while individually functional, do not interoperate in a way that provides a seamless picture of how to start a business.

## City Contracting and Procurement: Landscape for Minority-Owned and Emerging Businesses

### Institutional Structure and Programs

The City of Richmond has established several formal mechanisms intended to expand procurement opportunities for minority-owned businesses, women-owned businesses, and disadvantaged businesses. The **Office of Minority Business Development (OMBD)**, located at 1500 East Main Street, 5th Floor, operates multiple programs offering free services to minority business enterprises (MBEs), emerging small businesses (ESBs), and disadvantaged business enterprises (DBEs)[1]. These programs include business technical assistance, business start-up and growth development, one-on-one business counseling, business assessments, business development workshops and series, registration and certification assistance, and financial options counseling and referrals—all provided free of charge[1]. The OMBD explicitly encourages interested firms to complete a vendor registration application, which provides access to notifications about upcoming workshops, conferences, seminars, and procurement opportunities[1].

Beyond OMBD, the city operates a **Procurement Services Department** that manages the supplier portal, which all suppliers and prospective suppliers must use to register on the iSupplier system[2]. This portal is described as a connection for current and future business, accounts payable, and communication with the city. To register, suppliers must complete required forms including IRS W-9 forms, Direct Deposit Bank forms (ACH/EDI Payment Agreement), and supporting documentation such as a voided check or bank document[2]. The registration process can be started and saved, with approval typically completed within 3–5 business days[2]. Once approved, an Email confirmation with User ID and Password is sent to the applicant[2].

The city also participates in **purchase card (P-Card) programs** through Bank of America, where agencies have VISA cards to use for small purchases under $10,000[2]. This mechanism, while not directly accessible to external vendors, does affect cash flow and payment timing for vendors working with the city.

### Virginia and Federal Procurement Ecosystems

The City of Richmond's procurement is situated within and constrained by Virginia's broader public procurement framework and federal requirements. The **Virginia Public Procurement Act** and **Richmond City Code Chapter 21** govern the city's processes[2]. **Virginia Business Opportunities (VBO)** is a state-level portal where procurement opportunities are published[14]. At the federal level, contracts over $25,000 must be listed on **SAM.gov** (System for Award Management)[16]. The **General Services Administration (GSA) Schedule** provides another federal contracting pathway for vendors seeking to sell to the government[16].

For businesses seeking to qualify as certified small businesses or minority-owned businesses at the state level, the **Virginia Department of Small Business and Supplier Diversity (SBSD)** manages the **SWaM certification** (Small, Women, and Minority business certification) and **DBE certification** (Disadvantaged Business Enterprise, a federal program)[13]. These certifications are free to apply for through SBSD but require a verification process and are often prerequisites for competing in state and federally-funded procurement set-asides[13].

### Current-State Procurement Navigation for Small and Minority-Owned Businesses

Despite these formal structures, research from other jurisdictions and national analysis identifies substantial barriers that small and minority-owned businesses face in identifying, understanding, and pursuing government contracts. A recent analysis of procurement challenges in Chicagoland found that while federal government spending exceeds $600 billion in contracts annually, only 27 percent of funding goes to small businesses, with minority-owned business enterprises (MBEs) facing even deeper disparities[48]. Key barriers include complexity of the procurement process (complex solicitations, fast turnaround times, outdated tracking systems), limited networks and knowledge (many small businesses lack visibility into contracting opportunities), and financial and resource limitations (higher costs to become "contract-ready," burdensome insurance or bonding requirements)[48].

In Richmond's specific context, the question is: how legible is the procurement landscape for an emerging minority-owned business? What does that business owner need to know and where do they go to learn it? First, they may benefit from OMBD's free services and should learn about these through either the city website, referral from a nonprofit partner, or word-of-mouth. Second, they should understand the distinction between city-only procurement, state-level procurement (via VBO), federal procurement (via SAM.gov), and potentially procurement from anchor institutions like Virginia Commonwealth University, the University of Richmond, or the Virginia Department of Transportation (which may have their own small business programs). Third, they should know whether they qualify for SWaM or DBE certification and whether those certifications would meaningfully increase their competitive odds for relevant opportunities. Fourth, they should be able to search the City Contracts dataset, understand what types of goods and services the city has historically procured, and identify which categories match their capability.

However, the pathway from "I own a business" to "I found relevant procurement opportunities and positioned myself to compete" is not clearly marked. The city's procurement page provides contact information for Procurement Services and links to relevant statutes and resources, but does not provide a beginner's guide to "how to position your business to work with the City of Richmond" that is tailored to different business types, maturity levels, or demographic characteristics[2]. The OMBD page advertises free services but does not provide a searchable directory of recent or upcoming procurement opportunities[1]. The iSupplier registration process is functional but provides no guidance on strategic sourcing or competitive positioning[2]. The City Contracts open data can be downloaded or queried through an API but does not offer visualization or filtering tools targeted at prospective suppliers seeking to understand procurement patterns[12][15].

### Known Gaps in Public Procurement Visibility

The Richmond Civic Hackathon brief on procurement issues noted that businesses face significant friction in understanding what opportunities exist and preparing bids. The current city procurement portal is the official source for all solicitations, but it is not indexed in a way that helps small businesses browse by industry, contract size, or timing. The City Contracts open dataset is historical and does not indicate which agencies have upcoming needs. The procurement forecasting and pipeline visibility that exists within city departments is not systematized or publicly available in a machine-readable format. For federal contracts, SAM.gov provides the authoritative source, but navigating federal procurement for a business without prior government contracting experience is a significant lift.

Additionally, the availability of "sales visit" appointments with city buyers is mentioned but appears to require knowledge that this opportunity exists and initiative to call during business hours[2]. A more proactive, digital, and asynchronous pathway for small businesses to understand the city's procurement landscape could meaningfully reduce friction.

## Existing Support Infrastructure and Ecosystem Actors

### Free and Subsidized Business Support Organizations

Richmond benefits from a robust network of organizations providing business education, mentoring, and resource navigation. The **Capital Region SBDC** (Small Business Development Center) is the region's primary federally-backed small business support organization, offering free one-on-one counseling, business planning assistance, market research support, and financial management guidance[7]. Since 2020, it has served 1,500 clients, supported the launch of 111 new businesses, and created or retained 853 jobs while providing $41.73 million in capital investments[7]. SBDC advisors are available by appointment and can help businesses think through structure, registration requirements, financing, and growth strategy.

**SCORE** is a national nonprofit providing free business mentoring through a network of experienced business volunteers[8]. In fiscal year 2024 alone, SCORE supported 59,447 new business launches, contributed to 143,623 new jobs, and provided the equivalent of more than four centuries of expert mentoring through 4 million volunteer hours[8]. SCORE mentors work one-on-one with business owners and can be matched based on specific business needs.

**Startup Virginia** is the region's nonprofit organization dedicated to startup founders and entrepreneurs, operating an incubator, offering educational programs and networking events, and providing workspace[9]. Since inception, Startup Virginia has advanced 261 startups through its incubator, provided $1.8 million in scholarship funding, enabled $526 million in revenue for alumni startups, and facilitated $315 million in capital raises[9].

**BizWorks** is a nonprofit organization focused specifically on supporting small business owners through workshops, mentoring, and community events[42]. BizWorks offers a "Pathways to Success Business Series" and is recognized as a core partner in the business support ecosystem.

**The Jackson Ward Collective and the JWC Foundation** focus specifically on Black business owners and emerging entrepreneurs in Richmond, offering culturally centered programming, business launch and growth support, and an incubator program launching in June 2026 with 12 months of intensive training, small cohorts, culturally relevant curriculum, access to micro-grants, and a community of peer business owners[43]. The JWC Foundation has supported 500+ Black business owners since 2020, with 83 incubator graduates since 2022 and 120 businesses launched or strengthened[43].

**Activation Capital** (formerly the Virginia Biosciences Development Center) supports high-growth entrepreneurship in life sciences and advanced manufacturing, offering shared laboratory space, dedicated labs, private office space, events, resources, mentors, and programs such as Start the Journey (a pre-accelerator) and Frontier BioHealth (an accelerator)[45]. This organization serves a more specialized niche (life sciences and biotech) but represents the kind of vertical-focus support available for particular industries.

These organizations collectively provide a genuine safety net for entrepreneurs in Richmond, but their existence does not eliminate the need for clearer public-facing pathways and information architecture. Someone new to Richmond or new to entrepreneurship may not know that these organizations exist. Someone who does know they exist may not know which organization to contact for their specific situation. And none of these organizations, while valuable, can scale to meet all informational and navigational needs individually.

### The City's Strategic Plan for Equitable Economic Development (SPEED)

The City of Richmond's **Strategic Plan for Equitable Economic Development (SPEED)** establishes five aggressive economic development goals through Fiscal Year 2026, including $3 billion in capital investment, 3,000 announced new jobs with annual salaries at or above $52,000, a 5 percentage point reduction in the poverty rate, $25 million in annual real estate tax revenue from development activities, and 2,500 postsecondary credentials awarded to Richmond residents[29]. SPEED emphasizes community, innovation, and industry as organizing principles and is designed to address long-standing inequities in education, poverty, housing, and health that have been exacerbated by the COVID-19 pandemic[29]. This plan sets the policy context and ambition level for economic development in Richmond but does not directly specify the operational pathways for business registration or procurement transparency.

### The 2026 Civic Hackathon: Hack for RVA

The City of Richmond's first-ever civic hackathon, **Hack for RVA**, is scheduled for March 27–29, 2026, and represents an institutional commitment to collaborative problem-solving across city challenges[19]. The hackathon is sponsored by the City of Richmond, AI Ready RVA, Plan RVA, and VCU School of Business and will challenge participants to develop solutions aligned with the seven pillars of the Mayor's Action Plan, including A Thriving Economy That Leaves No One Behind. The hackathon will award $10,000 in prizes ($5,000 Mayor's Choice Award, $2,500 Moonshot/People's Choice Award, and $1,000 for each of the seven MAP pillars)[19]. Unlike traditional hackathons focused on speed and technology alone, Hack for RVA explicitly prioritizes people, place, and purpose, encouraging cross-disciplinary teams to develop solutions grounded in lived experience and focused on real impact[19].

## Current-State User Journey Maps

### Journey 1: Emerging Entrepreneur Registering a Business in Richmond

**Starting State:** Founder has a business idea and wants to operate it legally in Richmond.

**Trigger:** Decision to launch; may be prompted by a job loss, a side income idea formalization, or a long-standing ambition.

**Steps and Friction Points:**

*Step 1: Deciding on Business Structure.* The founder must decide whether to operate as a sole proprietor, partnership, corporation, S-corp, LLC, or other entity. This decision has tax, liability, and administrative implications. Information sources include the IRS website, general-purpose sites like LegalZoom or Stripe Atlas, word-of-mouth advice, or consultation with an accountant or lawyer. A Capital Region SBDC advisor can help walk through this decision, but requires the founder to know that the SBDC exists and to proactively request counseling. *Friction:* This decision is often made without good information, leading to later need for restructuring.

*Step 2: Reserving or Registering a Business Name.* For LLCs, corporations, partnerships, and other entities requiring state registration, the founder must check name availability and file with the Virginia Secretary of State. For sole proprietors operating under a personal name, this step may be skipped. *Friction:* If operating under a trade name, the founder must register with the State Corporation Commission before registering with the City, but this prerequisite is not always clear.

*Step 3: Obtaining a Federal Employer Identification Number (EIN).* For any entity other than a sole proprietor, an EIN from the IRS is required. This can be obtained free of charge online through the IRS website[22]. *Friction:* While straightforward, this step requires knowing that it is necessary and that the IRS website is the source.

*Step 4: Understanding City Zoning and Obtaining a Certificate of Zoning Compliance.* The founder must determine whether their business type is allowed in their intended location according to Richmond's zoning code. This requires using the city's zoning map and understanding the zoning restrictions. An application for a Certificate of Zoning Compliance (CZC) must be submitted through the city's Online Permit Portal, providing a detailed business description and square footage information, and obtaining property owner consent. The CZC application must be approved before the BPOL license application can proceed. *Friction:* This prerequisite is stated in BPOL FAQs but is not prominently featured in introductory material. The CZC process requires navigating a separate portal and understanding zoning concepts. For a founder without real estate experience, the distinction between zoning compliance and operational permits may be unclear.

*Step 5: Obtaining a Certificate of Zoning Compliance (CZC) Approval.* Contingent on Step 4, the founder receives approval via email and download from the Online Permit Portal. *Friction:* The portal uses a tracking number ("Plan Number") distinct from the eventual permit number, which can be confusing.

*Step 6: Registering and Paying for the Business License (BPOL Tax).* After CZC approval, the founder registers through the city's RVA Business Portal (as of 2025), providing business name, entity type, address, type of business, ID number, and begin business date. The registration generates an invoice, fees are paid through the portal, and confirmation is provided. *Friction:* The portal is new (January 2025) and may not be widely known. Fee structures vary by business type and can be unclear without calling the Department of Finance. The portal requires EIN or Social Security number, which assumes the founder has already obtained an EIN or is willing to provide their personal Social Security number.

*Step 7: Industry-Specific Regulatory Compliance.* Depending on business type, additional registrations and permits may be required. For food businesses, a Food Establishment Permit and possibly a Plan Review must be obtained from the Richmond City Health District; applications cost $40 each[38]. For construction contractors, DPOR licensure is required and annual Richmond business licensing may also be required if work exceeds $25,000[40]. For sidewalk vendors, Commercial Liability Insurance is required (naming the city as co-insured), and for food vendors, a Health Certificate is required[3]. *Friction:* These requirements are not coordinated through a single portal or contact point. A business owner may not know which regulations apply until they begin the BPOL process or attempt to operate and are contacted by a regulatory agency.

*Step 8: Opening a Business Bank Account.* Once the founder has an EIN and BPOL registration, most banks require these documents to open a business account. *Friction:* Timing is flexible but late bank account opening can complicate financial record-keeping.

*Step 9: Connecting to Support, Financing, and Growth Resources.* The founder may, at any point, benefit from consulting with a business advisor at SBDC, SCORE, Startup Virginia, BizWorks, or another organization. Access to these services is optional but valuable. *Friction:* These organizations are not actively promoted by the city during business registration, leading many founders to go it alone or discover these resources only by chance.

**Current Information Sources Used by This Persona:**
- City of Richmond website (Department of Finance BPOL page, Planning and Development Review page)
- IRS website (for EIN application)
- Virginia Secretary of State website (for business name registration)
- City's Online Permit Portal (for CZC and BPOL registration)
- Possibly Google search for "how to start a business in Richmond VA" or "business registration Richmond Virginia"
- Possibly referral from a nonprofit partner (SBDC, SCORE, BizWorks, Startup Virginia)
- Possibly phone call to Department of Finance (804-646-7000) or RVA311 (3-1-1)

**Pain Points:**
1. Sequencing confusion: CZC prerequisite for BPOL is not prominent; many founders discover it too late.
2. Fragmentation: Multiple portals (state website, city Online Permit Portal, RVA Business Portal, Industry-specific agency sites) create context switching.
3. Missing decision trees: No clear guidance on "what applies to my business?"
4. Industry-specific regulatory requirements are not surfaced upfront.
5. Connection to support resources is passive and dependent on founder initiative.
6. Mobile-unfriendly processes and assumption of desktop access and Adobe Acrobat familiarity.

### Journey 2: Minority-Owned or Emerging Business Seeking City Contracting Opportunities

**Starting State:** A business has been registered and is looking to grow revenue by working with the City of Richmond or related public sector entities.

**Trigger:** Desire to access stable, predictable revenue; awareness (via word-of-mouth, nonprofit advisor, or peer) that the city buys goods and services; desire to position for potential preference or set-aside opportunities.

**Steps and Friction Points:**

*Step 1: Understanding Business Certification Options.* The business owner learns (or may not learn, depending on their information sources) that minority-owned, women-owned, or disadvantaged businesses can pursue SWaM certification (state-level) or DBE certification (federal, for certain contracting types). OMBD provides free registration and certification assistance, but the business owner must know to contact OMBD. *Friction:* Certification options are not surfaced as a standard part of business registration or growth planning. Many business owners operate for years without understanding that certifications could unlock opportunities.

*Step 2: Registering with OMBD.* The business owner completes the OMBD vendor registration application and becomes eligible to receive notifications about workshops, conferences, seminars, and procurement opportunities. *Friction:* The registration is simple, but OMBD's capacity to proactively market these opportunities depends on newsletter updates and direct outreach—scalability is constrained by staff time.

*Step 3: Registering on the iSupplier Portal.* The business owner must register on the City's iSupplier portal (Supplier Portal) to be eligible to bid on city contracts. Registration requires IRS W-9, ACH/EDI Payment Agreement forms, and supporting documentation[2]. Approval typically takes 3–5 business days. *Friction:* This is a separate registration process from OMBD registration and from general business registration. The purpose and urgency of this registration are not clear to a founder who has just opened their business and may not even be thinking about government contracts yet.

*Step 4: Identifying Relevant Procurement Opportunities.* The business owner must somehow find out about procurement opportunities. Current methods include: (a) checking the City of Richmond's procurement page manually for new solicitations, (b) receiving notifications from OMBD (if registered and on mailing list), (c) checking Virginia Business Opportunities (VBO) portal for state-level opportunities, (d) checking SAM.gov for federal opportunities, or (e) networking and asking directly whether specific city departments have upcoming needs. *Friction:* There is no single place where a business owner can see "here are the procurement opportunities that match your business type in the next 3–6 months." Opportunities are not indexed by industry, contract size, or timeline. The city's historical contracts data is available via open data but does not predict future opportunities.

*Step 5: Becoming "Contract-Ready."* If the business owner identifies a relevant opportunity, they must ensure they have the required insurance, bonding, financial documentation, and operational stability to meet bidding requirements. The cost of becoming contract-ready can be substantial ($50,000–$500,000 for larger firms)[48]. *Friction:* This is a significant operational and financial hurdle for emerging businesses. Guidance on what "contract-ready" means for a specific opportunity is not readily available.

*Step 6: Understanding and Submitting a Bid.* The business owner must download the solicitation, understand the requirements, prepare a bid or proposal, and submit it. For government contracts, bid language can be legal and dense, and there may be specific technical or financial requirements. *Friction:* Without prior government contracting experience, the bid submission process can feel opaque. Technical support from organizations like SBDC can help, but is not automatically provided.

*Step 7: Award and Fulfillment.* If awarded, the business must fulfill the contract on time, manage invoicing through the city's payment systems (which may involve significant payment delays), and maintain compliance with reporting and documentation requirements. *Friction:* Cash flow can be strained if payment is delayed. Reporting requirements and compliance obligations can be burdensome for a small team.

**Current Information Sources Used by This Persona:**
- OMBD website and direct outreach
- City's Procurement Services website and iSupplier portal
- Virginia Business Opportunities (VBO)
- SAM.gov
- Word-of-mouth and peer networks
- Local nonprofit advisors (SBDC, SCORE, BizWorks)
- Possibly chamber of commerce or business association newsletters

**Pain Points:**
1. Discovery friction: No obvious starting place for "I want to sell to the city." Opportunities are scattered across multiple platforms.
2. Lack of forward visibility: Historical contracts data does not signal upcoming needs or allow pipeline planning.
3. Certification complexity: The relationship between OMBD registration, SWaM certification, DBE certification, and iSupplier registration is not clear; these appear as separate processes.
4. Readiness gap: A business may be operationally ready to fulfill a contract but may not understand they are "contract-ready" in a procurement sense (bonding, insurance, financial documentation).
5. Information density: Government bid language and procurement regulations are opaque to small business owners without prior experience.
6. Support access: Mentoring on government contracting is available through SBDC or other organizations but is not proactively offered; owners must request it.
7. Cash flow risk: Delayed payment from city contracts can strain emerging businesses.

## Source Inventory and Data Landscape

### City of Richmond Public Information and Systems

| **System / Dataset** | **Owner / Publisher** | **URL** | **Data Format** | **Current Use Case** | **Known Limitations** |
|---|---|---|---|---|---|
| Department of Finance Business Page | City of Richmond | rva.gov/finance/business | HTML web portal | Tax, fee, license information for businesses | Scattered across multiple pages; no integrated workflow |
| BPOL Tax FAQ | City of Richmond | rva.gov/finance/bpol-tax | HTML FAQ | Business licensing questions | Does not explain CZC prerequisite clearly |
| RVA Business Portal | City of Richmond (Finance Dept) | RVA Business Portal (new as of Jan 2025) | Web application | BPOL and Business Personal Property filing | New system; may not be widely known; only addresses finance-side registration |
| Planning & Development Review | City of Richmond | rva.gov/planning-development-review | HTML + PDF guides | Zoning, permitting, development info | Extensive PDFs; not mobile-friendly; requires Adobe Acrobat knowledge |
| Online Permit Portal | City of Richmond (PDR) | Online Permit Portal | Web application | CZC, building permits, site plan submissions | Separate from BPOL portal; duplicative account creation |
| Certificate of Zoning Compliance Guide | City of Richmond (PDR) | PDF guide | PDF | Step-by-step CZC application instructions | 13-page step-by-step with screenshots; assumes comfort with web portals |
| Building Permit Process for Commercial Construction | City of Richmond (PDR) | PDF guide | PDF | Commercial construction permitting workflow | 26 pages; comprehensive but dense; assumes design/engineering background |
| City Contracts Open Data | City of Richmond | data.richmondgov.com (Socrata platform) | CSV, API, Tableau | Historical contracts; agency spending patterns | Historical only, not forward-looking; updated monthly but no supplier-side interface |
| Office of Minority Business Development | City of Richmond | rva.gov/minority-business | HTML + email / PDF forms | OMBD services, vendor registration, certification assistance | No searchable directory of opportunities; relies on email/newsletter distribution |
| Procurement Services | City of Richmond | rva.gov/procurement-services | HTML + links | Supplier Portal registration, purchase card info, procurement resources | Limited information for prospective suppliers; does not explain how to position a business |
| iSupplier Portal | City of Richmond (Procurement) | iSupplier system (vendor registration) | Web application | Supplier registration, vendor account management | Assumes vendor knowledge; no beginner's guide |
| RVA311 | City of Richmond | RVA311.com + 804-646-7000 | Web portal + phone | General city service requests and information | Centralized contact point; effectiveness depends on call center knowledge |
| Strategic Plan for Equitable Economic Development (SPEED) | City of Richmond | rva.gov/economic-development/speed | HTML + PDF | Economic development strategy and goals | Policy-level; does not specify operational pathways |

### Virginia State-Level Systems

| **System** | **Owner** | **URL** | **Format** | **Use Case** | **Limitations** |
|---|---|---|---|---|---|
| Virginia Secretary of State | Virginia | sos.virginia.gov | Web portal | Business entity registration, name reservation | State-level; does not integrate with city registration |
| Virginia Business Opportunities (VBO) | Virginia | eva.virginia.gov | Web portal + email | State procurement opportunities | Requires account creation and email subscription; not beginner-friendly |
| Virginia Department of Small Business & Supplier Diversity (SBSD) | Virginia | sbsd.virginia.gov | Web portal | SWaM and DBE certification | Certification process is transparent but can take weeks; application-heavy |
| Virginia Stormwater Management | Virginia DEQ | deq.virginia.gov/water/stormwater | HTML | Stormwater permits for construction | Applicable to commercial construction; separate from building permits |
| Virginia Department of Health Food Safety | Virginia | vdh.virginia.gov | HTML + PDF | Food establishment regulations and guidance | Regulatory; not designed as business guidance |
| Virginia Food and Drink Law | Virginia | vdh.virginia.gov | PDF | Food business regulations | Regulatory language; assumes legal knowledge |
| Virginia Department of Professional & Occupational Regulations (DPOR) | Virginia | dpor.virginia.gov | Web portal | Contractor licensing, trades licensing | Industry-specific; not integrated with business registration |

### Federal Systems

| **System** | **Owner** | **URL** | **Format** | **Use Case** | **Limitations** |
|---|---|---|---|---|---|
| IRS EIN Online Application | IRS | irs.gov (Form SS-4) | Web application | Employer Identification Number | Free; straightforward for those who know about it |
| System for Award Management (SAM.gov) | GSA | sam.gov | Web portal | Federal contract opportunities over $25K | Designed for government contracting; complex for small businesses |
| Federal Procurement Data System | GSA | fpds.gov | Database | Historical federal contracts; trends | Historical; requires data literacy to extract insights |
| USASpending.gov | OMB | usaspending.gov | Web portal + data | Federal spending data | Informational; not actionable for small business bidding |
| GSA Schedules | GSA | gsa.gov | Web portal | Pre-approved federal vendor lists | Competitive; requires prior contracting experience to apply |
| FinCEN Beneficial Ownership Reporting | Treasury | fincen.gov/boi | Web system | Beneficial ownership information reporting | Administrative; required for most businesses formed after 2024 |

### Nonprofit Support Organizations and Private Services

| **Organization** | **Services** | **Website** | **Contact** | **Coverage** | **Known Gaps** |
|---|---|---|---|---|---|
| Capital Region SBDC | Free business counseling, planning, market research, financial guidance | capitalregionvasbdc.com | intake@capitalregionvasbdc.com | Greater Richmond, including Henrico, Goochland | Appointment-based; not 24/7 available |
| SCORE | Free business mentoring, workshops, templates | score.org | Varies by location | National network; Richmond chapter serves region | Volunteer-based; match quality varies |
| Startup Virginia | Incubator, educational programs, networking, workspace | startupvirginia.org | Varies | High-growth startups; tech-focused | Not focused on main-street businesses; venture capital orientation |
| BizWorks | Business support, workshops, membership, co-working | bizworkscenter.org | Varies | Main-street businesses in Chesterfield, Richmond area | Membership-based model; resource constraints |
| Jackson Ward Collective / JWC Foundation | Black business owner support, workshops, incubator (launching June 2026), community building | thejwcfoundation.org | Varies | Black and minority-owned businesses in Richmond | New incubator (June 2026); capacity constraints |
| Activation Capital | Life sciences and advanced manufacturing support, shared lab space, accelerators | activation.capital | Varies | Biotech and life sciences startups | Sector-specific; not general purpose |
| Virginia Tech Corporate Engagement Center | Business startup and growth (likely serves region) | Not directly referenced in search results | Various | Academic resource; limited scope |
| Stripe Atlas | Delaware incorporation service, startup legal templates | stripe.com/atlas | Varies | High-tech startups; not local | National service; oriented toward venture-backed companies |
| Cooley LLP (legal partner) | Startup legal and incorporation services | cooley.com | Varies | High-end legal support for startups | Expensive; not accessible to most emerging entrepreneurs |

### Data Quality and Completeness Assessment

**Strengths of Current Information Landscape:**
- City BPOL FAQ and Planning & Development Review guides are detailed and attempt to be comprehensive.
- Open Data Portal provides historical contracting data in machine-readable formats (CSV, API).
- Major support organizations are present and provide free or low-cost services.
- City has made recent effort to modernize (RVA Business Portal, new Online Permit Portal).

**Weaknesses of Current Information Landscape:**
- Information is fragmented across multiple websites, portals, and systems with no integrated navigation.
- Procedural sequencing is documented piecemeal but not explicitly mapped (e.g., CZC prerequisite for BPOL is mentioned in FAQs but not prominent in initial guidance).
- No decision tree or branching logic guides users to relevant information based on their business type or situation.
- Forward-looking procurement data (opportunities, pipeline, forecast) is absent; only historical data exists.
- Nonprofit support organizations are robust but their existence and services are not integrated into official city information flows.
- Mobile experience is poor for PDF-heavy processes.
- No Spanish-language or other language alternatives are prominently featured (though RVA311 mentions translation services upon request).
- Industry-specific requirements (food, construction, etc.) are scattered across multiple agencies with no unified "if your business involves X" guide.

---

## Benchmark Scan: Comparable Tools and Approaches from Other Cities

### 1. San Francisco's City Business Portal

San Francisco's **City Business Portal** (businessportal.sfgov.org) provides a comprehensive repository for business guidance, accessible through a single web address, with sections on starting, managing, and growing a business, and obtaining compliance[36]. The portal consolidates information from multiple city departments and agencies into a unified information architecture, reducing the need for business owners to navigate across multiple sites. The tool does not appear to handle all permitting or registration (those still require separate portals), but it serves as a centralized information and guidance hub.

**Relevance to Richmond:** San Francisco's approach demonstrates that a single, well-organized entry point for business information, even if it does not handle all transactions, can reduce confusion and increase usability. Richmond could adopt a similar model, creating a "Richmond Business Portal" or expanding RVA311 to include business-specific guidance trees.

### 2. Austin, Texas: Doing Business Hub and MBE/WBE Program

Austin's **Doing Business** page (austintexas.gov/business/doing-business) provides organized categories of business-related resources, including permits, utilities, recycling, small/minority business resources, and common code violations[35]. Austin separately maintains detailed information about its **MBE/WBE Program**, including certification, compliance, and contracting opportunity information[35]. Austin's approach separates the general business guidance from the minority business program but makes both easily discoverable from the main business page.

**Relevance to Richmond:** Richmond's OMBD serves a similar function to Austin's MBE/WBE program, but integration with general business guidance is weaker. Improving the visibility and linkage between general business registration and minority business programs could help minority entrepreneurs understand available pathways and resources.

### 3. Chicago: Procurement Barriers Research and Support Recommendations

Research into procurement barriers for small and minority-owned businesses in Chicagoland identified the need for streamlined MBE certification, better access to procurement forecasts and opportunities, and targeted support for "contract-readiness."[48] While Chicago has not (to date of search results) fully implemented all recommendations, the research provides evidence for what types of tools would meaningfully reduce barriers.

**Relevance to Richmond:** The research finding that small businesses need visibility into pipeline opportunities and clearer pathways to "contract-readiness" directly informs what a Richmond procurement tool should focus on. Forward-looking procurement forecasts and skill-building resources on requirements like insurance and bonding would be high-value.

### 4. Texas: Civic Marketplace and Cooperative Procurement

**Civic Marketplace** is a platform that helps governments streamline procurement by providing access to pre-vetted, pre-bid suppliers, comparative tools, and documentation management in a single place[34]. Texas has used Civic Marketplace as part of its cooperative procurement strategy to accelerate vendor discovery and reduce RFP timelines[34]. The platform was co-designed with public agencies to solve real procurement challenges, including complexity of rules, overlooked suppliers, and lengthy timelines.

**Relevance to Richmond:** The Civic Marketplace model demonstrates that a dedicated platform focused on supplier discovery, vetting, and comparison can reduce friction. For Richmond, a scaled-down version focused on helping small and minority-owned businesses discover relevant city procurement opportunities could be prototyped in a hackathon weekend.

### 5. National Day of Civic Hacking Projects: Code for America Brigade Examples

Several Code for America brigade projects provide relevant examples of civic hackathon outcomes that addressed business and economic development challenges[18]. For instance:
- **Apptology** (Sacramento) used open data to map food assistance (WIC) service providers on an interactive map, helping consumers find nearby resources.
- **Open Pittsburgh's #hackforchange** involved using open data and mapping (Open Street Map) to identify vacant properties and overlapping datasets from county assessment and nonprofit surveys.
- **Code for KC** developed a Parcel Assessment Tool (PAT) allowing citizens and developers to assess land suitability using zoning and parcel size specifications.

**Relevance to Richmond:** These projects demonstrate that hackathon prototypes can successfully combine open data, simple mapping or comparison interfaces, and user-centered design to address real discovery and decision-making problems. Similar approaches could work for Richmond procurement discovery or business registration guidance.

### 6. Federal "Ask Once" Initiative and Intergovernmental Data Sharing

The federal government's "Ask Once" initiative aims to reduce burden on public and businesses by collecting data once and sharing it across agencies rather than asking the same entity to provide the same information repeatedly[47]. Successful intergovernmental data sharing requires committed leadership, effective processes, and data quality standards[47]. While full implementation across all government is not realistic for a hackathon project, the "ask once" principle can inform the design of business registration tools—for instance, capturing business name, address, and entity type once and auto-filling those in subsequent forms.

**Relevance to Richmond:** Many business registration steps require the same information (business name, address, entity type, owner information). A tool that captured this information once and pre-populated it in downstream forms (CZC, BPOL, iSupplier) could significantly reduce friction.

## Feasibility Assessment: What Can Be Prototyped in 48 Hours

Given the Richmond Civic Hackathon timeline (March 27–29, 2026, 48 hours), a realistic assessment of scope is essential. The hackathon guidance indicates that successful prototypes will have clear scope, leverage readily available data and APIs, and focus on solving a specific user problem rather than attempting to replace institutional systems.

### High-Feasibility Opportunities (Recommended)

**1. Business Registration Decision Tree / Guided Intake Tool**

A web application that guides a prospective business owner through a series of questions (business type, industry, location, ownership structure) and returns a personalized, sequenced checklist of steps they need to take, with links to relevant city forms, online portals, and support organizations. The tool would encode the logic currently scattered across FAQs and PDFs into an interactive format.

*Feasibility:* High. Requires basic web development (React, Vue, or similar), no backend database or privileged data access. Data sources (city requirements) are already public and in documentation. A prototype can be built to cover the most common business types in 48 hours.

*MVP Scope:* Sole proprietor starting a retail or service business in Richmond; LLC formation; food business startup.

*Technical Stack:* Frontend web application with branching logic. No authentication or payment required. Can be deployed on GitHub Pages or similar.

*Data Requirements:* Manual knowledge engineering from existing city FAQs, BPOL, CZC, food permit documentation. No real-time data updates needed for prototype.

*User Value:* Clear, personalized guidance reduces confusion, prevents rework (e.g., discovering CZC requirement too late), saves time.

*Partnership / Authority:* Does not require approval from city departments; acts as a public-facing tool amplifying existing city information.

---

**2. Procurement Opportunity Aggregator and Filter Tool**

A web application that aggregates procurement opportunities from multiple sources (City of Richmond Procurement page, Virginia Business Opportunities, potentially SAM.gov for federal), displays them in a searchable, filterable interface (by industry, contract size, timeline, SWaM/DBE set-asides), and provides notifications when new opportunities matching a user's profile are posted.

*Feasibility:* Moderate-to-High for MVP. Requires web scraping or API integration to pull data from Procurement pages and potentially VBO. Notification/email subscription functionality adds complexity. A basic MVP can prototype data aggregation and filtering in 48 hours; notification system can be deferred to post-hackathon.

*MVP Scope:* Aggregation and display of City of Richmond procurement opportunities + Virginia Business Opportunities. Filtering by industry keyword, contract size (if available). Manual addition of new opportunities (not automated pulling).

*Technical Stack:* Frontend web application with backend data management. Could use Airtable or similar low-code backend to manage opportunities data during hackathon, migrate to proper database post-hackathon.

*Data Requirements:* Publicly available procurement data from city and VBO. Some data cleaning and standardization needed (formatting dates, categories, contract values).

*User Value:* One-stop visibility into opportunities; reduced need to monitor multiple sites. Filtering enables businesses to find relevant opportunities quickly. Notifications support proactive opportunity discovery.

*Partnership / Authority:* Could be built as a third-party tool (like a civic tech prototype) without requiring city approval, as long as it links to official city procurement portal as the authoritative source for bids. Value-add is aggregation and discoverability, not replacement.

---

**3. Business Registration Information Architecture Redesign (Interactive Guide)**

A more ambitious information design project: create a visually appealing, mobile-friendly interactive guide (using web design principles and possibly tools like Figma or Webflow) that walks through Richmond business registration requirements. Unlike the Decision Tree tool, this focuses on comprehensive, well-designed information presentation and navigation rather than personalized branching.

*Feasibility:* High for design / information architecture. Moderate for development if coding is needed. Can be designed as a static web prototype or low-code tool in 48 hours.

*MVP Scope:* Overview of business registration steps; clear explanation of CZC prerequisite; links to all relevant city forms and portals; FAQ section addressing common confusion points.

*Technical Stack:* Could be designed in Figma and prototyped as clickable prototype, or built as a static website using HTML/CSS/JavaScript.

*Data Requirements:* Same as Decision Tree (public city documentation).

*User Value:* Reduced confusion; clear sequencing; all information in one place; mobile-friendly reduces friction for business owners looking up requirements on smartphones.

*Partnership / Authority:* Could be proposed to the city as a replacement for or supplement to existing scattered guidance. Ideally, city would host this or link to it prominently.

---

**4. Minority Business Program Resource Hub**

A web application that centralizes information about OMBD services, local nonprofit support (SBDC, BizWorks, JWC Foundation, SCORE), SWaM/DBE certification, and vendor registration requirements, with guidance on how these resources interconnect and which ones are relevant for different business types and life stages.

*Feasibility:* High. Primarily information design and curation; limited technical complexity.

*MVP Scope:* Directory of support organizations with descriptions, contact info, and service details. Explanation of SWaM/DBE certification. Guide to OMBD services. Vendor registration (iSupplier) guide.

*Technical Stack:* Static or simple dynamic website; no complex backend.

*Data Requirements:* Public information from OMBD, nonprofit websites, state SBSD information.

*User Value:* Minority entrepreneurs, unsure where to go for support, can quickly find relevant resources and understand how they interconnect. Reduces wheel-spinning and false starts.

*Partnership / Authority:* Could be proposed to OMBD or city as a resource to support their programs. OMBD could link from its website.

---

### Moderate-Feasibility Opportunities (Consider If Team Capacity Allows)

**5. Small Business "Contract Readiness" Self-Assessment Tool**

An interactive tool that helps a small business evaluate whether they meet typical requirements for city contracting (insurance, bonding, financial documentation, operational capacity), identifies gaps, and provides guidance on how to close gaps (e.g., which insurance broker provides business liability, what bonding costs, financial documentation needed).

*Feasibility:* Moderate. Requires research into typical contracting requirements, insurance industry knowledge, and assessment logic. But can be scoped as a simple questionnaire with results-based guidance.

*MVP Scope:* Self-assessment covering insurance, bonding, financial documentation, company size/experience, compliance/legal status. Results show gaps and resources for closing them.

*Technical Stack:* Web form with branching results. Backend can be simple.

*Data Requirements:* Research on typical city requirements, insurance broker/bonding company information (can be generic or Richmond-specific).

*User Value:* Helps small businesses understand what "contract-ready" means and what they should prioritize. Bridges a key knowledge gap in procurement navigation.

*Partnership / Authority:* Could be co-developed with SBDC or OMBD as a tool they offer to their clients.

---

### Lower-Feasibility Opportunities (Not Recommended for Hackathon, But Valuable as Post-Hackathon Initiatives)

**6. Integrated Business Registration Portal (Connects RVA Business Portal + Online Permit Portal + iSupplier)**

A unified portal that consolidates BPOL registration, CZC permitting, and supplier registration into a single workflow, eliminating duplicate account creation and pre-filling common information.

*Feasibility:* Low for hackathon. Requires backend integration with existing city systems, data model alignment, likely IT department buy-in, and ongoing maintenance. Prototype could show the concept but cannot achieve true system integration in 48 hours.

*Why not for hackathon:* Requires privileged access to city systems, institutional commitment, and post-hackathon maintenance and support. This is not a tool a volunteer team can build and hand off; it requires city ownership.

*Post-hackathon path:* Present as a recommendation to the Department of Finance IT and Planning & Development Review IT; propose as a multi-quarter IT initiative.

---

**7. Real-Time Procurement Forecasting and Pipeline Visibility**

An internal tool (not public-facing) that aggregates procurement needs from city departments and displays a forward-looking pipeline of opportunities, allowing city to publish forecasts and allowing suppliers to see what's coming.

*Feasibility:* Low for hackathon. Requires department-by-department outreach, data standardization across departments, and likely an internal database or ERP system integration. Without institutional commitment, data collection is infeasible in 48 hours.

*Why not for hackathon:* Depends on data that does not currently exist in public form; requires city staff to actively populate and maintain.

*Post-hackathon path:* Recommend to Department of Finance, Procurement Services, and OMBD as a strategic initiative requiring budget and staff time.

---

**8. Multilingual Business Registration Guide**

High-quality translations of business registration requirements into Spanish, Mandarin, Vietnamese, and other Richmond languages.

*Feasibility:* Low for hackathon given translation quality standards. Professional translation services are expensive and time-consuming.

*Why not for hackathon:* Requires professional translation; volunteer translation may be unreliable. Better handled as a post-hackathon initiative with budget for professional translation.

*Post-hackathon path:* Recommend to city; connect with RVA311's existing translation services and language access plan.

---

## Risks, Ethics, and Data Quality Concerns

### Data Quality and Accuracy Risks

**Problem:** Much of the information about Richmond business registration requirements exists in PDFs, FAQs, and city webpages that are updated irregularly. If a hackathon prototype encodes this information, it may become outdated if city policies change.

**Mitigation:** Any tool should clearly state "last updated [date]" and recommend users verify critical information directly with city departments before making decisions. Tools should link to official sources rather than copying information. Ideally, the city would commit to updating any tool maintained on city servers.

**Problem:** Procurement opportunity data from City Contracts open data is historical and updated monthly. A tool showing "here are opportunities you should pursue" based on historical data may mislead if procurement patterns have changed.

**Mitigation:** Tool should clearly indicate that historical data is being used and recommend users consult official procurement pages for current opportunities. Tool should not create a false impression of predictability.

### Accessibility and Equity Risks

**Problem:** A web-based tool assumes users have reliable internet access, basic computer literacy, and comfort with digital interfaces. Some business owners, particularly older business owners or those without prior tech experience, may not benefit from or may be excluded by a digital tool.

**Mitigation:** Tools should be designed mobile-first and with accessibility standards (WCAG 2.1 AA compliance). But acknowledge that tools complement rather than replace human support. Ensure PDFs, phone numbers, and in-person contact options remain available and promoted.

**Problem:** If a Procurement Opportunity tool is very effective, it may increase competition for opportunities, benefiting more sophisticated businesses (those with resources to bid well) while potentially disadvantaging the least resourced businesses.

**Mitigation:** Tool can include information about support available to emerging businesses (SBDC, SCORE, etc.), but the risk is structural and not fully addressable by the tool. This is a reason to ensure that companion initiatives (like SBDC contracting support or BizWorks workshops) are adequately resourced.

### Privacy and Data Security Risks

**Problem:** If a tool collects user data (e.g., business profile, email for notifications), that data must be stored securely and not sold or misused.

**Mitigation:** For a hackathon prototype, minimize data collection. If notifications/subscriptions are included, partner with established platforms (e.g., Mailchimp, SendGrid) with known privacy practices. Do not build custom user data collection unless necessary. Be transparent about data use in a privacy policy.

### Institutional Relationships and Authority

**Problem:** If a tool appears to represent the city but is not actually maintained by the city, there is risk of liability and trust damage if information is outdated or incorrect.

**Mitigation:** Tools should be clearly positioned as "civic tech prototypes" and include prominent disclaimers. If the city is willing to adopt or endorse a tool, that should be formalized and the tool should be maintained by city staff. Hackathon prototypes should be positioned as "proof of concept" or "starting points for city consideration" rather than as official city resources.

**Problem:** If a tool provides information about OMBD, SBDC, or other partner organizations, those organizations may have concerns about representation or be associated with the tool without having been consulted.

**Mitigation:** Engage partner organizations early; show prototypes; invite feedback. Clearly attribute information sources. If organizations want to be involved, include them; if not, make clear that information is publicly available and tool creators have no special relationship with those organizations.

---

## Recommendations for Hackathon Teams: Buildable Project Directions

Based on the landscape analysis, source inventory, feasibility assessment, and risk considerations, the following are recommended project directions for Hack for RVA teams focusing on Pillar 4 (Thriving Economy) and using the two anchor challenges of business registration simplification and procurement opportunity discovery.

### Recommended Project 1: Richmond Business Registration Assistant (Decision Tree Tool)

**Problem:** Emerging entrepreneurs in Richmond are confused about the sequence of steps required to register a business, don't know about the CZC prerequisite, discover requirements piecemeal, and waste time navigating multiple portals and forms.

**Solution:** An interactive web application that guides the user through a simple questionnaire (business type, industry, location, planned entity structure) and returns a personalized, step-by-step checklist of what they need to do, with clear links to relevant forms, city portals, support organizations, and estimated timelines.

**User Group:** First-time entrepreneurs, existing business owners expanding, immigrant entrepreneurs, people re-entering workforce as self-employed.

**Key Features:**
- Questionnaire interface with clear, simple questions (not legal jargon).
- Personalized output: "Here's your checklist for starting a [business type] in Richmond."
- Each step shows: (a) description of step, (b) required documents, (c) where to do it (link to form or portal), (d) estimated cost, (e) estimated time.
- Special section for industry-specific requirements (if food business, adds steps; if construction contractor, adds state licensing requirements).
- Links to support resources (SBDC, SCORE, BizWorks, nonprofits).
- "I'm stuck" feedback mechanism to flag steps people commonly get stuck on.

**Technical Implementation:**
- Frontend: React/Vue web app with branching logic (can be hosted on GitHub Pages, Netlify, or similar).
- Data: Manual encoding of business registration requirements from city FAQs and guides; stored as JSON or embedded in code.
- No backend database needed for MVP.
- Mobile-responsive design is essential.

**Data Sources:**
- City of Richmond BPOL FAQ and guide.
- Planning & Development Review CZC guide.
- Richmond City Health District food business guides.
- DPOR contractor licensing requirements.
- Virginia State Corporation Commission business formation requirements.
- All public sources.

**Success Metrics (Post-Hackathon):**
- Usage (how many businesses use the tool, do they find it helpful?).
- Reduction in BPOL rejection or rework rates (if city tracks this).
- Reduced calls to Department of Finance or RVA311 asking "what do I do first?"

**Estimated Effort:** 40–50 hours of development work (very feasible for a 2-person tech team in 48 hours if focused and scoped well).

---

### Recommended Project 2: Richmond Procurement Opportunity Explorer

**Problem:** Small and minority-owned businesses in Richmond want to work with the City but don't know what opportunities exist, are not aware of procurement until too late, and must monitor multiple websites to find out about bids.

**Solution:** A web application that aggregates Richmond City procurement opportunities, Virginia Business Opportunities, and (if feasible) federal opportunities from SAM.gov, displays them in a searchable, filterable interface, and allows users to filter by industry, contract size, SWaM/DBE set-asides, and timeline. A companion feature provides information about how to position a business for contracting (certification, insurance, bonding, financial readiness).

**User Group:** Minority-owned businesses, small contractors, small service providers (bookkeeping, HR, IT, marketing, facilities, transportation, etc.), emerging businesses looking for stable revenue.

**Key Features:**
- Opportunity listing: Display all current city procurement opportunities with contract details (title, description, contract value, deadline, contact, set-asides).
- Filtering: By industry (use NAICS codes or simpler categories), contract value range, set-asides (SWaM, DBE, local preference), deadline.
- Search: Keyword search for business type and opportunity.
- Opportunity detail: Full description, requirements, deadlines, how to submit bid, city contact.
- "How to bid" guide: For each opportunity or in general, explain requirements, insurance/bonding, bid submission, evaluation criteria.
- Comparison view: If desired, compare multiple opportunities side-by-side.
- Email notification: Allow users to subscribe to alerts for opportunities matching their profile (can be done via third-party service like Mailchimp).
- Resource links: To OMBD, SBDC, BizWorks, certification information.

**Technical Implementation:**
- Frontend: Web app (React/Vue) with filtering, search, and detail views.
- Data sources: 
  - City of Richmond Procurement page (web scraping or manual data entry).
  - Virginia Business Opportunities (VBO) API or scraping.
  - City Contracts open data (for historical context and to understand categories).
- Backend: Simple database or Airtable to manage opportunities; can be manually populated for MVP.
- Notifications: Third-party service (Mailchimp, SendGrid) or simple email signup with manual sending.

**Data Sources:**
- City of Richmond Procurement Services page.
- Virginia Business Opportunities (VBO).
- City Contracts open data (Socrata API or CSV download).
- SAM.gov (optional for MVP; complexity may defer to post-hackathon).

**Success Metrics (Post-Hackathon):**
- Usage (how many businesses sign up, how often do they check).
- Outcome (do businesses who use the tool actually bid? Do they win? Do they report it helped them identify opportunities?).
- Feedback from OMBD and support organizations on whether the tool helps their clients.

**Estimated Effort:** 50–60 hours for a complete MVP with notifications (feasible for a 2-3 person team in 48 hours if some features are deferred, such as notifications or advanced filtering).

---

### Recommended Project 3: Richmond Business Registration Information Hub (Static, Design-Focused)

**Problem:** Business registration information is scattered across city websites, documents, and portals. First-time entrepreneurs don't know where to start and feel lost navigating fragmented resources.

**Solution:** A visually appealing, well-organized information hub that consolidates all business registration information in one place with clear navigation, explaining the "what," "why," and "how" of each step, with links to official forms and portals.

**User Group:** First-time entrepreneurs, business owners new to Richmond, immigrants unfamiliar with US business registration.

**Key Features:**
- Clear welcome section: "You're starting a business in Richmond. Here's what you need to do."
- Step-by-step overview: Listed in correct order with dependencies noted.
- Detailed explanation of each step: Written in plain language (avoiding jargon), with diagrams if helpful.
- FAQ section: Addressing common confusion points (CZC prerequisite, why multiple portals, cost breakdown, timeline).
- Troubleshooting: "I'm stuck on [step], what do I do?"
- Industry-specific guidance: Separate sections for food businesses, contractors, retail, service providers, etc.
- Links to all relevant forms, portals, and contact information.
- Mobile-responsive design.
- Printable checklist.

**Technical Implementation:**
- Static website: HTML/CSS/JavaScript, or use a simple tool like Webflow, Carrd, or similar.
- No database or backend needed.
- Can be designed in Figma first, then coded.
- Can be hosted on GitHub Pages or city servers.

**Data Sources:**
- City of Richmond official guidance (BPOL FAQ, CZC guide, etc.).
- Contact information from city website.
- Timing and cost information (from city fees schedules).

**Success Metrics (Post-Hackathon):**
- Usage statistics (if hosted on city servers with analytics).
- Feedback from users and support organizations.
- Reduction in confused inquiries to city departments.
- Potential integration into official city website.

**Estimated Effort:** 30–40 hours for design and development of a polished prototype (very feasible for a 1-2 person team in 48 hours).

---

### Recommended Project 4: Minority Business Resources Navigator

**Problem:** Minority entrepreneurs are unaware of OMBD services, nonprofit support, SWaM/DBE certification, and how these resources interconnect. Each organization exists but visibility is low and connections between them are unclear.

**Solution:** A web application that functions as a directory and guide to Richmond's minority business support ecosystem, including OMBD services, local nonprofit support organizations (SBDC, BizWorks, JWC Foundation, Startup Virginia, SCORE, Activation Capital), and state/federal certification programs. The tool explains what each organization does, how they work together, and recommends resources based on the user's situation (just starting? growing? seeking contracts? seeking capital?).

**User Group:** Minority-owned business owners (especially Black entrepreneurs, given Richmond's strong Black business ownership rates and JWC Foundation focus), immigrant entrepreneurs, women entrepreneurs.

**Key Features:**
- Organization directory: Profiles of all major support organizations (OMBD, SBDC, SCORE, BizWorks, JWC Foundation, Startup Virginia, Activation Capital) with descriptions, services, contact info, website links.
- Service finder: "I need help with [X]. Which organization should I contact?" (e.g., "I need help writing a business plan → SBDC").
- Resource guides: Explanation of SWaM certification, DBE certification, OMBD vendor registration, how to navigate city procurement.
- Success stories or case studies: Examples of how support organizations have helped Richmond business owners.
- Timeline: "If I'm at stage [X] (just starting, growing, seeking contracts), which resources are most relevant?"
- Events and workshops: Calendar of upcoming events from support organizations.
- Feedback mechanism: "What other support would you like to see?"

**Technical Implementation:**
- Web app (React/Vue) with directory, filtering, and detail views.
- Backend: Simple database (Airtable, Firebase, or similar) to manage organization profiles, services, events.
- Can include event calendar integration (Google Calendar or similar).

**Data Sources:**
- Organization websites (OMBD, SBDC, BizWorks, JWC Foundation, etc.).
- Public information about services, contact info, hours.
- State SBSD information about SWaM/DBE certification.

**Success Metrics (Post-Hackathon):**
- Usage and referrals from minority business owners.
- Feedback from support organizations on whether tool drives inquiries.
- Potential adoption by OMBD or city as a referral tool.

**Estimated Effort:** 40–50 hours (feasible for a 2-person team).

---

### Recommended Project 5: Business Contracting "Readiness Check" Tool

**Problem:** Small businesses are interested in pursuing city contracts but don't understand what "contract-ready" means. They don't know whether they have adequate insurance, bonding, financial documentation, and compliance standards. This uncertainty leads to hesitation and missed opportunities.

**Solution:** An interactive self-assessment tool that guides a small business through a set of questions to evaluate whether they meet typical city contracting requirements (insurance, bonding, financial documentation, legal status, operational capacity, prior experience). For each area where they fall short, the tool provides guidance on what to do and connects them to relevant resources.

**User Group:** Small businesses interested in city and government contracting, contractors, emerging businesses seeking growth.

**Key Features:**
- Self-assessment questionnaire: Covers insurance (type, amount), bonding (surety bond requirements), financial documentation (accounting, tax returns, credit), legal status (business registration, licenses), operational history, prior government contracts, compliance with regulations (environmental, labor, accessibility).
- Readiness score: Visual indicator of current readiness (e.g., 60% ready for typical city contracts).
- Gap analysis: Prioritized list of what's missing and what needs attention.
- Action plan: For each gap, specific guidance on how to close it and resources to help (e.g., "Get commercial general liability insurance → here's how → here are Richmond insurance brokers").
- Resource links: To insurance providers, bonding companies, accounting services, SBDC, SCORE.
- FAQ: Common questions about insurance amounts, bonding costs, financial documentation needs.
- Disclaimer: "Readiness depends on specific opportunities; check each bid for specific requirements."

**Technical Implementation:**
- Web form with scoring logic.
- Backend: Simple scoring algorithm; results displayed in UI.
- Can use simple backend (Firebase, Airtable) or even embed scoring logic in frontend.

**Data Sources:**
- Research on typical city contracting requirements (from city procurement documents, vendors).
- Insurance and bonding information (general guidance; not specific insurance quotes).
- Resource links (SBDC, insurance brokers, accountants in Richmond).

**Success Metrics (Post-Hackathon):**
- Usage and user feedback.
- Referrals to insurance providers, accountants, and support organizations.
- Potential adoption by SBDC or OMBD as a tool for their clients.

**Estimated Effort:** 35–45 hours (feasible for a 2-person team).

---

## Unknowns to Validate with City Staff and Partners

The following gaps in knowledge should be validated through conversation with city staff, OMBD, Procurement Services, and nonprofit partners before committing significant post-hackathon resources to any of these projects.

### City-Level Questions

1. **CZC and BPOL Sequencing:** Is the CZC prerequisite universally required before BPOL registration, or are there exceptions? If exceptions, how do applicants know?

2. **BPOL Portal Adoption:** How widely known is the new RVA Business Portal (launched January 2025)? Are there early adoption metrics or user feedback?

3. **Industry-Specific Requirements:** Is there a centralized list (internal to city) of which industries require additional permitting (food, construction, etc.), or is this scattered?

4. **Zoning and Business Eligibility:** Can the zoning code and zoning map be provided in a machine-readable format to enable automated checking of "is my business type allowed at my location?"

5. **Procurement Forecasting:** Do city departments currently forecast procurement needs for the next quarter or year? If so, is this data available (or could it be made available) in a standardized format?

6. **Procurement Data Quality:** Can the city provide clarity on the City Contracts open data schema (e.g., what do the procurement type codes mean? are contract values reliably populated?) to improve tool usability?

7. **SWaM/DBE Set-Asides:** Which city procurement opportunities include SWaM or DBE set-asides? Is this data captured and could it be surfaced to prospective vendors?

8. **RVA311 Effectiveness:** What are the most common questions RVA311 receives related to business registration and contracting? Are there patterns indicating confusion points?

9. **Support Organization Capacity:** Are SBDC, OMBD, and nonprofits capacity-constrained? Could a tool that pre-screens questions or provides self-service guidance reduce their incoming inquiry volume?

10. **City Endorsement:** Would the city be willing to host, link to, or endorse a third-party tool if it met quality standards? What would that process look like?

### Data and Integration Questions

11. **CZC Data:** Is CZC approval data available or could it be queried to understand approval timelines and common rejection reasons?

12. **Business Registration Data:** Does the city track BPOL application rejection or rework rates? Are there patterns indicating specific confusion points?

13. **Procurement Trends:** What are the top categories of goods and services the city procures? Are there emerging needs or changing patterns?

14. **Vendor Diversity:** Does the city track vendor demographic data (minority-owned, women-owned, etc.) by contract or industry to identify underrepresented areas?

### Nonprofit and Partner Questions

15. **Support Organization Coordination:** Is there formal coordination between OMBD, SBDC, BizWorks, and JWC Foundation on referrals and resource sharing? Could a tool help coordinate these resources better?

16. **Common Client Questions:** What are the most common questions SBDC, BizWorks, and JWC Foundation receive from clients about business registration and contracting?

17. **Tool Hosting:** Would any of these organizations be interested in hosting, maintaining, or co-promoting a tool?

18. **Certification Barriers:** Do support organizations see barriers in the SWaM/DBE certification process that tools could address?

---

## Conclusion: Pathway to Prototype and Beyond

The landscape analysis reveals that Richmond has substantial institutional infrastructure—from the Office of Minority Business Development to the Capital Region SBDC to Startup Virginia to the JWC Foundation—dedicated to supporting business creation and growth. The city has made recent efforts to modernize business registration through the new RVA Business Portal and has published open data about city contracts. Yet, **the information architecture remains fragmented and the user experience of navigating business registration and procurement opportunities remains inefficient and confusing.**

The two anchor problems identified for Hack for RVA—simplifying business registration and empowering minority-owned businesses to discover and pursue procurement opportunities—are real, urgent, and addressable through software innovation **that does not require policy change, additional city budget, or replacement of existing systems**. Rather, the opportunity is to create **intelligence layers**—tools that make existing public information, forms, and processes more discoverable, legible, and navigable.

Five feasible hackathon projects are recommended, ordered by estimated impact and feasibility:

1. **Richmond Business Registration Assistant** (Decision Tree): Highest value per development effort. Addresses the most frequent source of confusion (sequencing and prerequisites) with a straightforward interactive tool.

2. **Richmond Procurement Opportunity Explorer**: High value for minority business support ecosystem. Addresses discovery and monitoring friction. Requires data aggregation and filtering but is technically straightforward.

3. **Richmond Business Registration Information Hub**: Strong design-focused project. Valuable even if not interactive; serves as reference for business owners and foundation for future tools.

4. **Minority Business Resources Navigator**: Addresses awareness and coordination within support ecosystem. High value for ecosystem visibility but narrower user base than first two projects.

5. **Business Contracting Readiness Check**: Addresses knowledge gap about what government contracting requires. Valuable for businesses interested in contracting but lower priority than discovery and registration tools.

Teams should validate unknowns with city staff, OMBD, and nonprofit partners early in the hackathon. The best prototype will emerge from close listening to actual user pain points, iteration based on feedback, and realistic scoping to ensure a functional prototype by Sunday evening.

The output of this hackathon—whether a prototype is adopted by the city or not—will also serve as concrete evidence that civic innovation focused on users, data, and existing institutions can improve the business ecosystem in Richmond and create a pathway for similar projects addressing other city challenges.