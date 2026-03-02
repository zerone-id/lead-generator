"""Domain models for lead generation and qualification."""

from dataclasses import dataclass


@dataclass(slots=True)
class Lead:
    """Represents a single inbound lead candidate."""

    company: str
    employee_count: int
    annual_revenue_usd: int
    inbound_channel: str


@dataclass(slots=True)
class ScoredLead:
    """Lead with computed priority score and qualification status."""

    lead: Lead
    score: int
    qualified: bool
