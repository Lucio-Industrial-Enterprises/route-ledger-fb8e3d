# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in US dollars.

| Parameter   | Values                      | Notes                      |
|-------------|-----------------------------|----------------------------|
| `weight_kg` | positive float              | Parcel weight in kilograms |
| `zone`      | `"local"`, `"regional"`     | Delivery zone              |
| `service`   | `"standard"`, `"express"`   | Defaults to `"standard"`   |

Express shipping costs **$7 more** than the standard rate for the same zone and
weight. Unknown zones or service levels raise `ValueError`.

### Rates

| Zone       | Base  | Per-kg | Express surcharge |
|------------|-------|--------|-------------------|
| `local`    | $5.00 | $1.50  | +$7.00            |
| `regional` | $8.00 | $1.50  | +$7.00            |

### CLI

The command-line entry point accepts an optional `--service` flag:

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                   # $8.00
python -m warehouse.cli 2 local --service express # $15.00
```
