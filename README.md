# APIC Promote Tenant

###Authors:

Koorapati, Sahaja <Sahaja.Koorapati@nexusis.com>

Brantley Richbourg <Brantley.Richbourg@NexusIS.com>

Sanchez, Milo <milo.sanchez@nexusis.com>

# Description

This program is designed to allow Cisco APIC users the ability to copy settings from one tenant to another tenant in a fashion that is simular to how application developers promote code from DEV --> QA --> PROD.

The idea is that each tenant in APIC is an application environment.  We will use the following environments in our example: Prod, QA, and Dev.

Changes made to the Dev tenant manually in the APIC GUI can be promoted via a series of bash and Python scripts.  The changes will also have a version assigned to them so that you can track what version the environment is running at.  Those versions can be queired with a Python script.


# Installation

## Environment Required

* Python 2.7+
* Git
* Cisco ACI Toolkit
* Cisco ARYA

## How to install

Clone the ACI Toolkit from GitHub

	git clone https://github.com/datacenter/acitoolkit.git

Install the ACI Toolkit

	sudo python setup.py install

Clone the ARYA Toolkit from GitHub

	git clone https://github.com/datacenter/arya.git

Install the AYRA Tooklit

	sudo python setup.py install

Clone APICPromoteTenant from GitHub

	git clone https://github.com/SahajaKoorapati/APICPromoteTenant.git

# How to run


