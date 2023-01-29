import os
import sys
import json
import time


features2 = ['fpu','vme', 'de', 'pse', 'tsc', 'msr', 'pae', 'mce', 'cx8','apic', 'reserved', 'sep', 'mtrr', 'pge', 'mca', 'cmov', 'pat', 'pse-36', 'psn', 'clfsh', 'reserved', 'ds', 'acpi', 'mmx', 'fxsr', 'sse', 'sse2', 'ss', 'htt', 'tm', 'ia64', 'pbe']
features1 = ['sse3', 'pclmulqdq', 'dtes64', 'monitor', 'ds-cpl','vmx', 'smx', 'est', 'tm2', 'ssse3', 'cnxt-id', 'sdbg','fma', 'cx16', 'xtpr', 'pdcm', 'reserved', 'pcid', 'dca', 'sse4.1', 'sse4.2', 'x2apic', 'movbe','popcnt', 'tsc-deadline', 'aes', 'xsave', 'osxsave', 'avx', 'f16c', 'rdrnd', 'hypervisor']

tab = []

for i in range(32):
    if sys.argv[1][i] == '1':
        tab.append(features1[-i-1])


for a in range(32):
    if sys.argv[2][i] == '1':
        tab.append(features2[-a-1])


os.system('mkdir -p /home/postgres/resultats_tests')

os.system('cp /etc/xen/myvm.cfg /etc/xen/myvm.cfg.alt')


for fea in tab:
    
    os.system('rm /etc/xen/myvm.cfg')
    os.system('cp /etc/xen/myvm.cfg.alt /etc/xen/myvm.cfg')
    file = open('/etc/xen/myvm.cfg')
    file.write("\n")
    string = 'cpuid="host,{}=0"'        
    file.write(string.format(fea))
    file.close()
    os.system('xl create -c /etc/xen/myvm.cfg')

    lastTime = time.time()
    while not (os.path.exists('/home/postgres/resultats_tests/test')):
        if (time.time()-lastTime > 5):
            lastTime = time.time()
            os.system('xl list -l > state.json')
            f = open('state.json')
            state = json.load(f)
            f.close()
            bool = False
            for vm in state:
                if vm['config']['c_info']['name'] == "myvm":
                    id = vm['domid']
                    bool = True
            if not bool:
                feature = 'echo {} >> /home/postgres/resultats_tests/featuresUtile'
                os.system(feature.format(fea))
                break

    if os.path.exists('/home/postgres/resultats_tests/test'):
        res = 'cp /home/postgres/resultats_tests/test /home/postgres/resultats_tests/test_{}'
        os.system(res.format(fea))
        os.system('rm /home/postgres/resultats_tests/test')
        os.system('xl destroy myvm')
        time.sleep(10)