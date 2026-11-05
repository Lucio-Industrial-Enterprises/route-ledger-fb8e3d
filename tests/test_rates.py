import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (existing behaviour preserved)
    # ------------------------------------------------------------------

    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        """Passing service='standard' explicitly must match the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    # ------------------------------------------------------------------
    # Express service (new – $7 surcharge over standard)
    # ------------------------------------------------------------------

    def test_express_local(self):
        # standard local = 5 + 1.5*2 = 8.00  →  express = 8 + 7 = 15.00
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional = 8 + 1.5*2 = 11.00  →  express = 11 + 7 = 18.00
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven_dollars(self):
        """Express must always cost exactly $7 more than standard."""
        for zone in ("local", "regional"):
            with self.subTest(zone=zone):
                std = shipping_quote(5, zone, service="standard")
                exp = shipping_quote(5, zone, service="express")
                self.assertAlmostEqual(exp - std, 7.0)

    def test_express_fractional_weight(self):
        # local: 5 + 1.5*1.5 + 7 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_weight_negative(self):
        with self.assertRaises(ValueError):
            shipping_quote(-1, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
