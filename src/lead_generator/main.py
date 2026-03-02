"""CLI entry point for the Phase 1 lead generation scaffold."""

from .models import Lead
from .scoring import rank_leads


def main() -> None:
    """Execute a demo lead ranking run for Phase 1 review."""

    sample_leads = [
        Lead("Northwind", employee_count=850, annual_revenue_usd=180_000_000, inbound_channel="referral"),
        Lead("Contoso", employee_count=120, annual_revenue_usd=22_000_000, inbound_channel="webinar"),
        Lead("Tailspin", employee_count=35, annual_revenue_usd=3_500_000, inbound_channel="organic"),
    ]

    ranked = rank_leads(sample_leads)
    for idx, item in enumerate(ranked, start=1):
        status = "QUALIFIED" if item.qualified else "NURTURE"
        print(f"{idx}. {item.lead.company:<12} score={item.score:<3} status={status}")


if __name__ == "__main__":
    main()
