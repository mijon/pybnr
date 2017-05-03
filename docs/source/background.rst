Actuarial Background
====================

Introduction
------------
This documentation contains background information on the actuarial concepts used by pyBNR. This has been separated out here in order to keep code documentation relevant and useful.

.. _triangles-background:

Triangles
---------

Triangles (also known as 'Triangulations') are a fairly common part of insurance reserving calculations.
They are tables showing claims development over time based on origin year and development period.

Historically these would be drawn on paper with the origin period (i.e. the year of account, underwriting year, etc) on the far left column in ascending order, and the development period increasing along the table from left to right. 
As a new origin year was opened, a new row would be added extending the triangle downwards. 
At the same time updated information would be received about the earlier origin years and this would be added to each row in the appropriate column.
This process of additions filles the table in a triangular fashion, diagonal by diagonal.

Any 

