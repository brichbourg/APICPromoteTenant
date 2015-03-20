# APIC Promote Tenant

###Authors:

Koorapati, Sahaja <Sahaja.Koorapati@nexusis.com>

Richbourg, Brantley <Brantley.Richbourg@NexusIS.com>

Sanchez, Milo <milo.sanchez@nexusis.com>

# Description

This program is designed to allow Cisco APIC users the ability to copy settings from one tenant to another tenant in a fashion that is simular to how application developers promote code from DEV --> QA --> PROD.

The idea is that each tenant in APIC is an application environment.  We will use the following environments in our example: Prod, QA, and Dev.

Changes made to the Dev tenant manually in the APIC GUI can be promoted via a series of bash and Python scripts.  The changes will also have a version assigned to them so that you can track what version the environment is running at.  Those versions can be queried with a future Python script.

The version information is stored in the MIT (Management Information Tree) of the APIC controller in a property called ownerTag under the fvTenant object class for the tenant being pushing into the APIC by the script.  In other words, it is stored in a placed not modifiable in the APIC GUI.


# Installation

## Environment Required

* Python 2.7+
* Git
* Cisco COBRA (https://github.com/datacenter/corba - NOTE: the version used in this script is not publicly available as of 03/19/15)
* Cisco ACI Toolkit (https://github.com/datacenter/acitoolkit)
* Cisco ARYA (https://github.com/datacenter/arya)

## How to install

Clone APICPromoteTenant from GitHub:

	git clone https://github.com/brichbourg/APICPromoteTenant.git

Clone Cobra from Githib & Install:

	git clone https://github.com/datacenter/cobra.git
	cd cobra
	sudo python setup.py install


Install the ACI Toolkit (from the APICPromoteTenant dir):

	cd acitoolkit
	sudo python setup.py install


Install the AYRA Tooklit (from the APICPromoteTenant dir):

	cd arya
	sudo python setup.py install


# How to run

## Command Syntax
	./promoteTenant.sh <source_tenant> <dest_tenant> <revision_num>

## Example
	./promoteTenant.sh DEV QA 1.1 
