.. pysbml4j documentation master file, created by
   sphinx-quickstart on Tue Jun  8 13:51:14 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pysbml4j
========

.. toctree::
   :maxdepth: 2

   installing
   configuration
   connecting
   networks
   roadmap
   contributing
   



Pysbml4j is a python library to connect to a running SBML4j service and interact with it.

Requirements
------------

Pysbml4j requires Python3 and has been tested with Python 3.9.1 (should be 3.9.5).

Install with pip
----------------

The SBML4j python client library pysbml4j is available on the Python Package Index and can be installed using pip:

.. code-block:: bash
   
   pip3 install pysbml4j

Import pysbml4j
---------------

You can either import the whole package using

.. code-block:: python
   
   # Import the package in total
   import pysbml4j

Then you can access the Service with

.. code-block:: python

   client = pysbml4j.Sbml4j()

Alternatively you can import the parts individually using

.. code-block:: python

   # Import indiviual parts to use
   from pysbml4j import Sbml4j
   from pysbml4j import Configuration
   from pysbml4j import Network


Usage
-----

Here is a basic usage example for connecting to SBML4j,
listing all networks and retrieving a specific network in 
the GraphML format.

.. code-block:: python
   
   # Connect to local running instance on default settings
   client = Sbml4j()
   # List networks
   client.listNetworks()
   # Select network
   network = client.getNetworkByName("NetworkName")
   # retrieve network contents in GraphML
   netGraphML = network.graphML()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
