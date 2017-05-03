"""
This module contains the Triangle class.

For theoretical background, refer to :ref:`triangles-background`
"""
import pandas as pd


class Triangle():
    """This class provides a claims triangle object.

    The way triangles are stored in this class is in 'long' format.
    """

    def __init__(self):
        self.cum = None
        self.inc = None

    def __repr__(self):
        if self.cum is not None:
            # this required that the triangle object has the following colnames
            return str(self.cum.unstack())

    def read_csv(self, filename, cummulative=True, **kwargs):
        """
        Reads in a triangle contained in a csv file.

        The input triangle should be in long format.

        :param filename: csv filename location
        :type filename: str.
        :param cummulative: whether the provided triangle is cummulative.
        :type cummulative: bool.
        :returns: None"""
        tri = pd.read_csv(filename, dtype={'value':'float'}, **kwargs)

        # TODO add controls on column names
        tri = tri.set_index(['origin', 'development'])

        # depending on whether the provided file is cummulative or
        # incremental, we need to generate the other one
        if cummulative:
            self.cum = tri
            self.inc = self._cum_to_inc(self.cum)
        elif not cummulative:
            self.inc = tri
            self.cum = self._inc_to_cum(self.inc)


    def _inc_to_cum(self, triangle):
        """
        Helper function to translate incremental trianlges into cummulative
        """
        triangle = triangle.unstack()
        triangle = triangle.cumsum(axis=1)
        return triangle.stack()

    def _cum_to_inc(self, triangle):
        """
        Helper function to translate cummulative trianlges into incremental
        """
        triangle = triangle.unstack()
        shifted = triangle.shift(1, axis=1)
        shifted['value', 1].fillna(0, inplace=True)
        triangle = triangle - shifted
        return triangle.stack()
