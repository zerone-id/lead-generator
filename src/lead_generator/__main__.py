"""CLI entrypoint for Lead Generator."""

from .app import get_app_status


def main() -> None:
    status = get_app_status()
    print(
        f"{status['name']} | {status['phase']} | {status['status']}"
    )


if __name__ == "__main__":
    main()
