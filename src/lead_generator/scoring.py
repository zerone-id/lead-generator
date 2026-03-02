"""Phase 1 scoring heuristics for lead prioritization."""

from .models import Lead, ScoredLead


def score_lead(lead: Lead) -> ScoredLead:
    """Compute a simple heuristic score for a lead.

    The Phase 1 approach favors larger organizations and higher revenue,
    with a small channel-based adjustment.
    """

    score = 0

    if lead.employee_count >= 500:
        score += 45
    elif lead.employee_count >= 100:
        score += 30
    else:
        score += 15

    if lead.annual_revenue_usd >= 100_000_000:
        score += 40
    elif lead.annual_revenue_usd >= 10_000_000:
        score += 25
    else:
        score += 10

    channel_bonus = {
        "referral": 15,
        "webinar": 10,
        "organic": 5,
    }
    score += channel_bonus.get(lead.inbound_channel.lower(), 0)

    return ScoredLead(lead=lead, score=score, qualified=score >= 60)


def rank_leads(leads: list[Lead]) -> list[ScoredLead]:
    """Score and rank leads from highest to lowest priority."""

    return sorted((score_lead(lead) for lead in leads), key=lambda item: item.score, reverse=True)
