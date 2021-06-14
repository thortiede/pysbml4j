Configuration
=============

When instantiating Sbml4j with

.. code-block:: python

   client = Sbml4j()

pysbml4j will attempt to connect to an instance of SBML4j running at the default location

.. code-block:: bash

   http://localhost:8080/sbml4j

The port *8080* and the application-context */sbml4j* are the default configuration options for SBML4j.

In case you did change those default parameters on your personal installation of SBML4j, or if you want to use pysbml4j to connect to the SBML4j demonstration-instance running at::

   https://sbml4j.informatik.uni-tuebingen.de:8989

you can use the *Configuration* class to configure your python connector accordingly.


Import
------

You can import the Configuration class using:

.. code-block:: python

   from pysbml4j import Configuration

Constructor arguments
---------------------

The Constructor of the *Configuration* class allows the following arguments:

========== ========= ================
param-name data-type default-value
========== ========= ================
server     string    http://localhost
port       integer   8080
context    string    /sbml4j
user       string    sbml4j
========== ========= ================

If you omit any of these parameters the default-values will be used.


Setting the server
------------------

Create an instance of the Configuration and pass the server address:

.. code-block:: python

   conf = Configuration("https://sbml4j.informatik.uni-tuebingen.de:8989")

Pass this configuration to Sbml4j upon instantiation:

.. code-block:: python
   
   client = Sbml4j(conf)

or create the configuration in-line:

.. code-block:: python

   client = Sbml4j(Configuration("https://sbml4j.informatik.uni-tuebingen.de:8989"))



