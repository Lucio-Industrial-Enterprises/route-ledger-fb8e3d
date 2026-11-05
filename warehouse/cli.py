"""Command-line shipping quote."""

import argparse
from .rates import SERVICES, shipping_quote


def main() -> None:
    parser = argparse.ArgumentParser(description="Quote shipping for an order")
    parser.add_argument("weight_kg", type=float)
    parser.add_argument("zone", choices=["local", "regional"])
    parser.add_argument(
        "--service",
        choices=sorted(SERVICES),
        default="standard",
        help="Service level (default: standard)",
    )
    args = parser.parse_args()
    print(f"${shipping_quote(args.weight_kg, args.zone, args.service):.2f}")


if __name__ == "__main__":
    main()
