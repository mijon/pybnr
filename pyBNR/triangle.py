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
        self.tri = None

    def __repr__(self):
        if self.tri is not None:
            # this required that the triangle object has the following colnames
            return str(self.tri.pivot(index='origin', columns='development',
                       values='value'))

    def read_csv(self, filename, cummulative=True, **kwargs):
        """
        Reads in a triangle contained in a csv file.

        The input triangle should be in long format.

        :param filename: csv filename location
        :type filename: str.
        :param cummulative: whether the provided triangle is cummulative.
        :type cummulative: bool.
        :returns: None"""
        self.tri = pd.read_csv(filename, **kwargs)

        if not cummulative:
            # adjust triangle to be cummulative
            self.tri = self._inc_to_cum(self.tri)

    def _cum_to_inc(triangle):
        """
        Change a given cummulative triangle into an incremental triangle.

        :param triangle: a triangle data.frame
        :type triangle: data.frame
        :returns: incremental triangle
        """
        pass

    def _inc_to_cum(triangle):
        """
        Change a given incremental triangle into an cummulative triangle.

        :param triangle: a triangle data.frame
        :type triangle: data.frame
        :returns: cummulativetriangle
        """
        pass
