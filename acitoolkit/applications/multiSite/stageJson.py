import ast
import sys
from acitoolkit.acisession import Session
from credentials import *
import os
import json

# This gets the Json file with config-only and full subtree properties for a particular tenant.
def get_json_file_from_apic():

    session = Session(from_apic['URL'], from_apic['LOGIN'], from_apic['PASSWORD'])
    resp = session.login()
    if not resp.ok:
        print '%% Could not login to APIC'
        sys.exit()

    def get_json():
        class_query_url = '/api/node/class/fvTenant.json'
        ret = session.get(class_query_url)
        data = ret.json()['imdata']

        for ap in data:
            dn = ap['fvTenant']['attributes']['dn']
            tenant_name = sys.argv[1]
            ap_query_url = '/api/mo/uni/tn-%s.json?rsp-subtree=full&rsp-prop-include=config-only' % (tenant_name)
            ret = session.get(ap_query_url)
            if tenant_name == dn.split('/')[1][3:]:
               writeJson(ret.text)
    json_file = get_json()
    pass

# Writes the json content to <tenantName.json>               
def writeJson(text):
    filename = sys.argv[1] + ".json"
    print "Dumping tenant data to  " + os.path.realpath(filename)
    file = open(filename, 'w')
    file.write(text)
    file.close()

# Updates the fvTenant Name and dn to the new tenant name. Also updates fvTenant ownerTag with given value
def updateJsonFile():
    print "Modifying json with tagvalue " + sys.argv[3]
    with open(sys.argv[1]+".json",'r+') as file:
        json_data = json.load(file)
        print json_data['imdata'][0]['fvTenant']['attributes']['ownerTag']
        json_data['imdata'][0]['fvTenant']['attributes']['ownerTag'] = sys.argv[3]
        json_data['imdata'][0]['fvTenant']['attributes']['dn'] = "uni/tn-" + sys.argv[2]
        json_data['imdata'][0]['fvTenant']['attributes']['name'] = sys.argv[2]
        file.seek(0)
        file.write(json.dumps(json_data))
        file.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: stageJson.py <TenantName_tobe_Copied> <TenantName_tobe_Created> <tagValue>'
        sys.exit()
    else:
        get_json_file_from_apic()
        updateJsonFile()
