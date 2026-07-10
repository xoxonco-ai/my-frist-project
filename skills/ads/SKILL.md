---
name: ads
description: "When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'paid media,' 'ROAS,' 'CPA,' 'ad campaign,' 'retargeting,' 'audience targeting,' 'Google Ads,' 'Facebook ads,' 'LinkedIn ads,' 'ad budget,' 'cost per click,' 'ad spend,' or 'should I run ads.' Use this for campaign strategy, audience targeting, bidding, and optimization. For bulk ad creative generation and iteration, see ad-creative. For landing page optimization, see cro."
metadata:
  version: 2.1.0
---

# Paid Ads

You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficient customer acquisition.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Campaign Goals
- What's the primary objective? (Awareness, traffic, leads, sales, app installs)
- What's the target CPA or ROAS?
- What's the monthly/weekly budget?
- Any constraints? (Brand guidelines, compliance, geographic)

### 2. Product & Offer
- What are you promoting? (Product, free trial, lead magnet, demo)
- What's the landing page URL?
- What makes this offer compelling?

### 3. Audience
- Who is the ideal customer?
- What problem does your product solve for them?
- What are they searching for or interested in?
- Do you have existing customer data for lookalikes?

### 4. Current State
- Have you run ads before? What worked/didn't?
- Do you have existing pixel/conversion data?
- What's your current funnel conversion rate?

---

## Platform Selection Guide

| Platform | Best For | Use When |
|----------|----------|----------|
| **Google Ads** | High-intent search traffic | People actively search for your solution |
| **Meta** | Demand generation, visual products | Creating demand, strong creative assets |
| **LinkedIn** | B2B, decision-makers | Job title/company targeting matters, higher price points |
| **Twitter/X** | Tech audiences, thought leadership | Audience is active on X, timely content |
| **TikTok** | Younger demographics, viral creative | Audience skews 18-34, video capacity |

---

## Campaign Structure Best Practices

### Account Organization

```
Account
├── Campaign 1: [Objective] - [Audience/Product]
│   ├── Ad Set 1: [Targeting variation]
│   │   ├── Ad 1: [Creative variation A]
│   │   ├── Ad 2: [Creative variation B]
│   │   └── Ad 3: [Creative variation C]
│   └── Ad Set 2: [Targeting variation]
└── Campaign 2...
```

### Naming Conventions

```
[Platform]_[Objective]_[Audience]_[Offer]_[Date]

Examples:
META_Conv_Lookalike-Customers_FreeTrial_2024Q1
GOOG_Search_Brand_Demo_Ongoing
LI_LeadGen_CMOs-SaaS_Whitepaper_Mar24
```

### Budget Allocation

**Testing phase (first 2-4 weeks):**
- 70% to proven/safe campaigns
- 30% to testing new audiences/creative

**Scaling phase:**
- Consolidate budget into winning combinations
- Increase budgets 20-30% at a time
- Wait 3-5 days between increases for algorithm learning

---

## Ad Copy Frameworks

### Key Formulas

**Problem-Agitate-Solve (PAS):**
> [Problem] → [Agitate the pain] → [Introduce solution] → [CTA]

**Before-After-Bridge (BAB):**
> [Current painful state] → [Desired future state] → [Your product as bridge]

**Social Proof Lead:**
> [Impressive stat or testimonial] → [What you do] → [CTA]

**For detailed templates and headline formulas**: See [references/ad-copy-templates.md](references/ad-copy-templates.md)

---

## Audience Understanding & Targeting

Knowing your audience deeply is still the highest-leverage work in paid ads — demographics, job titles, pain points, fears, hopes, the exact language they use, who they follow, what they've tried, why they failed, what they buy. **Gather every identifier you can.**

What's changed in 2026 is **where you apply that knowledge.** As ad-platform algorithms have gotten dramatically better at finding the right person, jamming all your audience identifiers into the platform's *targeting filters* underperforms feeding those same identifiers into the *creative* (headlines, copy, visuals, hooks, examples).

The discipline now: **audience knowledge → creative first, targeting filters second.** How much that ratio tips toward "creative" varies meaningfully by platform.

### Platform-by-platform: where to apply audience knowledge

| Platform | Audience knowledge → creative | Audience knowledge → targeting filters | Notes |
|----------|------------------------------|-------------------------------------|-------|
| **Meta** (post-Andromeda) | **80%+** | 20% | Algorithm rewards broad + specific creative. See [references/meta-andromeda-playbook.md](references/meta-andromeda-playbook.md) for the full reframe. Interest-stacking now actively hurts. |
| **Google Search** | 40% | **60%** | Keywords are still the dominant signal — match-types, search-intent layering, and negative keywords still drive performance. Creative (RSA headlines) matters but is downstream of the keyword. |
| **Google Performance Max / Demand Gen** | **70%** | 30% | Audience signals are advisory, not deterministic. Creative + product feed quality dominate. |
| **LinkedIn** | 40% | **60%** | Job-title / company / industry filters still produce real precision because LinkedIn's identity data is high-quality. Creative makes the click; firmographics make the *right person* see it. |
| **TikTok** | **70%** | 30% | Algorithm is closer to Meta's model — broad targeting + native-feeling creative wins. Some audience interests help but creative dominates. |
| **Twitter/X** | 50% | 50% | Interest + follower targeting still meaningful, but creative differentiation is high-leverage given lower competition. |

These ratios are directional, not precise. Test in your actual account.

### Applying audience knowledge to creative

Once you've gathered audience identifiers, here's how to put each kind into the creative:

- **Demographic identifiers** (age, location, occupation) → embed as identity-trigger keywords in headlines (see [references/meta-andromeda-playbook.md](references/meta-andromeda-playbook.md), "The one-keyword hack")
- **Pain points + fears** → headline + first line of body copy (Sabri Suby's framing: "the verbatim words your customers use about the problem")
- **Hopes / desired outcomes** → transformation copy + CTAs
- **Objections + "why they didn't buy last time"** → objection-handling retargeting ads (see [references/retargeting-strategies.md](references/retargeting-strategies.md), "The 4-component retargeting framework")
- **Their language / vocabulary** → the entire copy voice — never use industry jargon they don't
- **Existing customer base** → still feed it for lookalike audiences (see Key Concepts below)
- **Niche / segment they identify with** → identity-trigger keywords in headline ("for dentists" / "for B2B founders" / "for parents of toddlers")

### Key Concepts (still apply)

- **Lookalikes**: Base on best customers (by LTV), not all customers. Still high-value across platforms.
- **Retargeting**: Segment by funnel stage (visitors vs. cart abandoners). See [references/retargeting-strategies.md](references/retargeting-strategies.md) for the modern playbook.
- **Exclusions**: Exclude existing customers and recent converters — showing ads to people who already bought wastes spend.

### Common failure mode

Trying to make up for weak creative with hyper-precise targeting. If your creative is generic but you stack 12 interests + 3 demographic filters + a custom audience, what you've built is a small audience that all see a bad ad. Better: gather the same audience identifiers, write 5 creative variants that each speak to a different segment, target broadly, let the algorithm match each creative to the right segment.

**For detailed targeting strategies by platform**: See [references/audience-targeting.md](references/audience-targeting.md)

---

## Modern Meta playbook (Andromeda era — 2026+)

Meta's **Andromeda** algorithm (2025+) rewards creative volume and broad targeting over interest-stacking. In short: post statics at volume (cheaper and faster than video), target broadly and let creative do the targeting, insert identity-trigger keywords ("dental," "lawyer," "for parents of toddlers") into winning ads to open new segments, and stop producing polished ads — native-feeling creative beats studio production.

**For the full playbook** (creative volume tactics, the one-keyword hack, AI variant farming, zombie campaigns, "don't make ads look like ads"): See [references/meta-andromeda-playbook.md](references/meta-andromeda-playbook.md)

## Creative Best Practices

### Image Ads
- Clear product screenshots showing UI
- Before/after comparisons
- Stats and numbers as focal point
- Human faces (real, not stock)
- Bold, readable text overlay (keep under 20%)

### Video Ads Structure (15-30 sec)
1. Hook (0-3 sec): Pattern interrupt, question, or bold statement
2. Problem (3-8 sec): Relatable pain point
3. Solution (8-20 sec): Show product/benefit
4. CTA (20-30 sec): Clear next step

**Production tips:**
- Captions always (85% watch without sound)
- Vertical for Stories/Reels, square for feed
- Native feel outperforms polished
- First 3 seconds determine if they watch

### Creative Testing Hierarchy
1. Concept/angle (biggest impact)
2. Hook/headline
3. Visual style
4. Body copy
5. CTA

---

## Campaign Optimization

### Key Metrics by Objective

| Objective | Primary Metrics |
|-----------|-----------------|
| Awareness | CPM, Reach, Video view rate |
| Consideration | CTR, CPC, Time on site |
| Conversion | CPA, ROAS, Conversion rate |

### Optimization Levers

**If CPA is too high:**
1. Check landing page (is the problem post-click?)
2. Tighten audience targeting
3. Test new creative angles
4. Improve ad relevance/quality score
5. Adjust bid strategy

**If CTR is low:**
- Creative isn't resonating → test new hooks/angles
- Audience mismatch → refine targeting
- Ad fatigue → refresh creative

**If CPM is high:**
- Audience too narrow → expand targeting
- High competition → try different placements
- Low relevance score → improve creative fit

### Bid Strategy Progression
1. Start with manual or cost caps
2. Gather conversion data (50+ conversions)
3. Switch to automated with targets based on historical data
4. Monitor and adjust targets based on results

---

## Retargeting Strategies

### Funnel-Based Approach

| Funnel Stage | Audience | Message | Goal |
|--------------|----------|---------|------|
| Top | Blog readers, video viewers | Educational, social proof | Move to consideration |
| Middle | Pricing/feature page visitors | Case studies, demos | Move to decision |
| Bottom | Cart abandoners, trial users | Urgency, objection handling | Convert |

Retarget with **different** offers, not the same one re-shown harder — the #1 reason someone didn't buy is usually that the offer wasn't right for them (e.g., pricing-page visitor who didn't sign up → retarget with a free audit instead). A strong retargeting layer runs 4 ad types simultaneously: objection-handling, proof/testimonial carousel, other-offers, and a value-first audit/assessment ad.

**For retargeting windows, exclusions, and the full 4-component framework**: See [references/retargeting-strategies.md](references/retargeting-strategies.md)

---

## Landing Page Alignment (the headline-mirror trick)

Ad-to-landing-page congruence is the single most underrated lever in paid ads. Most advertisers spend 90% of effort on ads and 10% on the landing page; flip that ratio.

### Headline mirroring

Meta is the best split-testing tool that exists — your ad headlines are exposed to ~1000x the audience that actually clicks through to your landing page. That means you get statistically-significant data on which headlines work *much faster* on Meta than on your landing page.

The play:

1. Run **20-40 different headlines** as ad variations
2. Identify the best-performing headline (by CTR + downstream conversion)
3. **Mirror that winning headline on your landing page** — exact wording in the H1, sub-headline, and lead-in copy of the body
4. Expect a **15-20% minimum lift** in landing-page conversion rate from this single change

This works because the viewer who clicked is expecting *that specific promise*. When the landing page restates the exact promise verbatim, scent matches and conversion follows. When the landing page pivots to a different angle, bounce rate spikes regardless of how good the page is.

### Three split tests minimum at all times

A standing discipline: **at any given moment, you should have at least 3 split tests running** somewhere in your funnel — ad creative, landing page, offer, or post-conversion flow. If you don't, you've capped your improvement curve.

The math: 3 simultaneous tests × ~10-20% lift each (compounding) = a fundamentally better funnel within a quarter.

## Reporting & Analysis

### Weekly Review
- Spend vs. budget pacing
- CPA/ROAS vs. targets
- Top and bottom performing ads
- Audience performance breakdown
- Frequency check (fatigue risk)
- Landing page conversion rate

### Attribution Considerations
- Platform attribution is inflated
- Use UTM parameters consistently
- Compare platform data to GA4
- Look at blended CAC, not just platform CPA

### Scaling discipline (net cash > ROAS percentage)

The most common scaling failure: a business at a 40 ROAS spending $5k/month, refusing to scale because "if I spend more, my ROAS will drop." This is the wrong frame.

**Net cash flow > ROAS percentage at the business level:**
- ROAS dropping from 10 → 5 sounds bad
- But if spend goes from $10k → $100k, you net dramatically more total profit
- The number to optimize is **blended ROAS at the business level**, not per-ad-set ROAS
- Even better: optimize **net free cash flow**, not ROAS at all

**Find your break-even ROAS:**
1. Calculate the absolute maximum you can pay to acquire a customer and still be profitable (factoring LTV)
2. That's your break-even ROAS / CPA ceiling
3. **Scale until you approach that ceiling**, not until your ad-account ROAS drops below an arbitrary preference

**The 3-hour founder review:**
- Block out **3 hours per month** in the calendar to physically review the numbers yourself
- Not what your data analyst says. Not what your media buyer says. You, going through the actual data
- The confidence this generates is irreplaceable — and confidence is what lets you scale with conviction
- "Data gives you confidence. Confidence gives you speed."

**Outbound-call your leads who didn't convert:**
- Every lead that downloaded a lead magnet or hit your funnel but didn't buy gets a call
- Ask why they didn't book, what was confusing, what the actual blocker was
- These verbatim answers become objection-handling ads (see [references/retargeting-strategies.md](references/retargeting-strategies.md))
- Massive insight-to-creative loop that most advertisers skip

---

## Platform Setup

Before launching campaigns, ensure proper tracking and account setup.

**For complete setup checklists by platform**: See [references/platform-setup-checklists.md](references/platform-setup-checklists.md)

**For conversion pixel installation and event setup**: See [references/conversion-tracking.md](references/conversion-tracking.md)

### Universal Pre-Launch Checklist
- [ ] Conversion tracking tested with real conversion
- [ ] Landing page loads fast (<3 sec)
- [ ] Landing page mobile-friendly
- [ ] UTM parameters working
- [ ] Budget set correctly
- [ ] Targeting matches intended audience

---

## Google RSA Output Spec (mandatory when generating RSAs)

When the user requests Google Ads RSAs (Responsive Search Ads), output MUST comply with strict platform limits and structural requirements — exactly 15 headlines (≤30 chars each) and 4 descriptions (≤90 chars each) per RSA, mandatory sidecar artifacts (ad group structure, ≥8 negative keywords, ≥4 sitelinks/callouts), a fixed emission order, and a medical/CFM compliance filter for Brazilian medical practices.

**Before generating any RSA, read [references/google-rsa-output-spec.md](references/google-rsa-output-spec.md) in full and follow it exactly** — it contains the hard character limits, required output order, the mandatory output template, and the self-check to run before responding. Do not output any RSA that violates it.

---

## Common Mistakes to Avoid

### Strategy
- Launching without conversion tracking
- Too many campaigns (fragmenting budget)
- Not giving algorithms enough learning time
- Optimizing for wrong metric

### Targeting
- Audiences too narrow or too broad
- Not excluding existing customers
- Overlapping audiences competing

### Creative
- Only one ad per ad set
- Not refreshing creative (fatigue)
- Mismatch between ad and landing page

### Budget
- Spreading too thin across campaigns
- Making big budget changes (disrupts learning)
- Stopping campaigns during learning phase

---

## Task-Specific Questions

1. What platform(s) are you currently running or want to start with?
2. What's your monthly ad budget?
3. What does a successful conversion look like (and what's it worth)?
4. Do you have existing creative assets or need to create them?
5. What landing page will ads point to?
6. Do you have pixel/conversion tracking set up?

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md). Key advertising platforms:

| Platform | Best For | MCP | Guide |
|----------|----------|:---:|-------|
| **Google Ads** | Search intent, high-intent traffic | ✓ | [google-ads.md](../../tools/integrations/google-ads.md) |
| **Meta Ads** | Demand gen, visual products, B2C | - | [meta-ads.md](../../tools/integrations/meta-ads.md) |
| **LinkedIn Ads** | B2B, job title targeting | - | [linkedin-ads.md](../../tools/integrations/linkedin-ads.md) |
| **TikTok Ads** | Younger demographics, video | - | [tiktok-ads.md](../../tools/integrations/tiktok-ads.md) |

For tracking setup, see [references/conversion-tracking.md](references/conversion-tracking.md), [ga4.md](../../tools/integrations/ga4.md), [segment.md](../../tools/integrations/segment.md)

---

## Related Skills

- **ad-creative**: For generating and iterating ad headlines, descriptions, and creative at scale
- **copywriting**: For landing page copy that converts ad traffic
- **analytics**: For proper conversion tracking setup
- **ab-testing**: For landing page testing to improve ROAS
- **cro**: For optimizing post-click conversion rates
