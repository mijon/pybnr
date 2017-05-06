import pandas as pd
from pyBNR.triangle import Triangle

class Test_incremental_cummulative_equality():
    """
    This tests whether a triangle initiated as a cummulative triangle
    gives equivalent inc and cum attributes as a triangle which is
    initiated as an incremental triangle
    """

    def setup_method(self):
        self.tri_cum = Triangle()
        self.tri_inc = Triangle()

        self.tri_cum.read_csv('tests/test_data/test_tri_cum.csv')
        self.tri_inc.read_csv('tests/test_data/test_tri_inc.csv', cummulative=False)

    def teardown_method(self):
        self.tri_cum = None
        self.tri_inc = None

    def test_cum_equality_long(self):
        print(self.tri_cum.cum)
        print(self.tri_inc.cum)
        assert self.tri_cum.cum.equals(self.tri_inc.cum) == True

    def test_inc_equality_long(self):
        assert self.tri_cum.inc.equals(self.tri_inc.inc) == True
