import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]


class IrisContentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = (ROOT / "index.html").read_text()
        cls.readme = (ROOT / "README.md").read_text()

    def test_iris_is_consistently_included_in_the_brief(self) -> None:
        self.assertIn("The eleven core protocols", self.html)
        self.assertIn("One borrower, ten routes", self.html)
        self.assertIn("Iris Credit", self.html)
        self.assertIn("Testnet live 11 Aug 2026", self.html)
        self.assertIn("TVL n/a", self.html)
        self.assertGreaterEqual(self.html.count("Iris Credit"), 10)

    def test_metadata_describes_eleven_protocols(self) -> None:
        self.assertIn(
            'content="Eleven ways to lock a borrowing rate. Ten live, '
            'Iris Credit next."',
            self.html,
        )

    def test_worked_example_and_taxonomy_include_solver_quotes(self) -> None:
        self.assertIn("gasless <strong>loan intent</strong>", self.html)
        self.assertIn("<strong>Solver RFQ</strong>", self.html)
        self.assertIn("solver bond covers negative carry", self.html)
        self.assertIn("a solver RFQ", self.readme)

    def test_cross_cutting_inventory_matches_six_lenses(self) -> None:
        self.assertIn("sliced <em>six ways</em>", self.html)
        self.assertIn("field sliced six ways", self.readme)

    def test_matrix_and_deep_dive_mark_iris_as_pre_public(self) -> None:
        self.assertIn("Venues and chains not yet announced", self.html)
        self.assertIn('<div class="num">11</div>', self.html)
        self.assertIn("no public TVL or mainnet launch date", self.html)

    def test_closing_summary_keeps_live_tvl_separate(self) -> None:
        self.assertIn("by net TVL the live DeFi-native field", self.html)
        self.assertIn("11</span></div><p>core protocols · 10 live, Iris next", self.html)

    def test_iris_source_is_linked_from_html_and_readme(self) -> None:
        source = "https://lens.iris.credit/posts/about-iris"
        self.assertGreaterEqual(self.html.count(source), 2)
        self.assertGreaterEqual(
            self.html.count(f'href="{source}" target="_blank" rel="noopener"'),
            2,
        )
        self.assertIn(source, self.readme)

    def test_readme_inventory_matches_the_brief(self) -> None:
        self.assertIn("## The eleven protocols", self.readme)
        self.assertIn("Iris Credit", self.readme)
        self.assertIn("Testnet live 11 Aug 2026 · mainnet pending · TVL n/a", self.readme)

    def test_editing_conventions_are_preserved(self) -> None:
        self.assertEqual(self.html.count("<section"), 14)
        em_dash = chr(0x2014)
        self.assertNotIn(em_dash, self.html)
        self.assertNotIn(em_dash, self.readme)


if __name__ == "__main__":
    unittest.main()
