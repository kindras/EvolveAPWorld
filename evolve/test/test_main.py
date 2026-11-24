from .bases import EvolveTestBase

class TestMainLogic(EvolveTestBase):
    options={}

    def test_win_condition(self)->None:
        pass
        #Nothing happens right now because I need to implement items, and that is a work in progress.
        # with self.subTest("Test that the location 'loc-tech:mad' is required for Victory state"):
        #     misslesLaunched=self.world.get_location("Missles Launched")

            # self.assertAccessDependency(["Missles Launched"],[["loc-tech:mad"]])

    def test_windturbine_technology_location_name(self) -> None:
        self.assertRaises(KeyError, self.world.get_location, "loc-tech:wind_turbine")
        self.assertIsNotNone(self.world.get_location("loc-tech:windturbine"))
