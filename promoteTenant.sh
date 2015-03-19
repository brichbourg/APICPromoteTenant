#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: <TenantName_tobe_Copied> <TenantName_tobe_Created> <revisionValue>"
else
	echo "Copying existing Tenant " $1
	echo "New tenant " $2
	echo "Revision number is " $3

	read -p "About to apply the above values. Enter to continue. Ctrl+C to quit"

	cd acitoolkit/applications/multiSite
	python stageJson.py $1 $2 $3

	cd ../../../
	# This runs arya.py taking the generated json as input and creates a python script with Tenant details
	arya.py -f acitoolkit/applications/multiSite/$1.json  -i172.31.216.24 -u admin -p scotch123 > $1.py
	sed '7,10d' $1.py > modified$1.py

	# This pushes the new tenant to APIC
	python modified$1.py
fi

