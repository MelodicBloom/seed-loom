#!/usr/bin/env python3
"""Validate prompt coverage, typed links, ranges, units, and mutation sensitivity.

The pass boundary is specification/compiler integrity, never rendered material
fidelity or completed workshop routes. Negative controls must actually fail.
"""
from __future__ import annotations
import copy
import hashlib
import json
import math
import os
import re
from pathlib import Path
from generate_textile_workshop import BASE, CORE, GROUPS, ROOT, SOURCE, compile_outputs, dependencies, records

def require(condition, message):
    """Fail closed without relying on Python assertions that -O can disable."""
    if not condition:raise ValueError(message)

def validate(data):
    """Reject incomplete records, invalid ranges, fabricated status and bad links."""
    require(set(data)=={'global','lightPresets','sources','surfaces','components','scenes','assets','methods','rules','implementations','experiments','gaps','integration'},'unexpected root field set')
    require(data['global']['coordinates']['metersPerMm']==.001,'unit conversion must be explicit')
    require(data['global']['render']['packageVersion']=='0.187.0','renderer recipe version drift')
    items=list(records(data)); ids=[i['id'] for _,i in items]
    require(len(ids)==len(set(ids)) and len(ids)>0,'empty or duplicate record IDs')
    known=set(ids); sources={s['sourceId'] for s in data['sources']}
    require(len(sources)==len(data['sources']),'duplicate source IDs')
    for group,item in items:
        require(bool(item['name']),'empty record name')
        for dep in dependencies(item):require(dep in known,f'{item["id"]}: unknown dependency {dep}')
        for src in item.get('sourceIds',['S00']):require(src in sources,f'unknown source {src}')
        require('implemented' not in item.get('status','') or item.get('status')=='implemented-unverified','unsupported implementation promotion')
    normalized=['roughness','metalness','specularIntensity','sheen','sheenRoughness','anisotropy','alphaCutoff','opacity','transmission','clearcoat','clearcoatRoughness','iridescence']
    for s in data['surfaces']:
        require(s['topology'] in ['woven','woven-coated','ribbed-woven','knitted','openwork','pile','quilted','thread','felt','solid'],'unknown topology')
        for key in normalized:
            n=s['pbr'][key];require(type(n) in [int,float] and math.isfinite(n) and 0<=n<=1,f'{s["id"]}.{key}: outside 0..1')
        p=s['pbr']; c=s['construction']; t=s['textureContract']
        require(p['iridescenceThicknessMinNm']<=p['iridescenceThicknessMaxNm'],'inverted optical thickness')
        require(c['thicknessMm']>0 and c['fuzzLengthMm']>=0 and 0<=c['openAreaRatio']<1,'invalid dimensions')
        require(p['alphaMode'] in ['OPAQUE','MASK','BLEND'],'invalid coverage mode')
        require(len(t['tileSizeMm'])==2 and min(t['tileSizeMm'])>0,'invalid tile dimensions')
        require(set(t['requiredMaps'])=={'baseColor','normal','orm','height','sheenColor','sheenRoughness','anisotropy','coverage'},'map contract incomplete')
        require(t['requiredMaps']['baseColor']['colorSpace']=='sRGB','albedo color space')
        require(t['requiredMaps']['normal']['colorSpace']=='non-color','normal must be non-color')
        require(t['requiredMaps']['sheenRoughness']['channels'].startswith('A='),'sheen roughness must occupy alpha')
    for a in data['assets']:
        require(a['status']=='planned-not-produced','asset availability needs a separate evidence promotion')
        require(a['receipt']['sha256']=='not-produced','planned asset must not invent a hash')
    for e in data['experiments']:
        require(e['status']=='planned','trial outcome requires separate execution evidence')
        for key in ['hypothesis','independentVariable','measurement','acceptanceThreshold','falsifier','stopRule','rollback']:
            require(bool(e[key]),'incomplete trial '+key)
    core=next(c for c in data['components'] if c['id']=='C25')
    require((ROOT/core['runtimeBinding']['existingPath']).is_file(),'Core consumer does not resolve')
    require(data['integration']['coreSemanticId'] in (ROOT/data['integration']['coreReference']).read_text(),'Core semantic anchor absent')
    for key in ['coreTokenAuthority','coreCompiler','suiteCompiler','suiteValidator','browserVerifier','ciWorkflow']:
        require((ROOT/data['integration'][key]).is_file(),'missing executable integration '+key)
    workflow=(ROOT/data['integration']['ciWorkflow']).read_text()
    for command in ['scripts/generate_textile_workshop.py --check','scripts/verify_textile_workshop.py','scripts/verify_textile_visual.py','scripts/verify_textile_evidence_failure.py','needs: validate-textile-interface']:
        require(command in workflow,'CI wiring missing '+command)
    return len(items)

def rejects(candidate):
    """A negative control succeeds only when the validator rejects it."""
    try:validate(candidate)
    except (ValueError,KeyError,TypeError):return True
    return False

def main():
    """Run synchronization, determinism and falsification checks; emit a receipt."""
    checks=[]
    def record(name,condition):
        require(condition,name);checks.append({'name':name,'passed':True})
    data=json.loads(SOURCE.read_text());core=json.loads(CORE.read_text())
    count=validate(data);record('complete typed registry',count==sum(len(data[g]) for g in GROUPS))
    expected=compile_outputs(data,core)
    record('all generated outputs synchronized',all(p.is_file() and p.read_text()==s for p,s in expected.items()))
    record('compiler deterministic',expected==compile_outputs(data,core))
    changed=copy.deepcopy(data); denim=next(s for s in changed['surfaces'] if s['id']=='M14');denim['construction']['yarnDiameterWarpMm']+=.05
    mutated=compile_outputs(changed,core)
    for name in ['prompts/surfaces.md','field-dictionary.json','material-options.json']:
        p=BASE/'generated'/name;record('denim mutation reaches '+name,expected[p]!=mutated[p])
    bad=copy.deepcopy(data);bad['components'][0]['materialIds']=['MISSING']
    record('reject unknown graph edge',rejects(bad))
    bad=copy.deepcopy(data);bad['surfaces'][0]['pbr']['roughness']=1.2
    record('reject material range violation',rejects(bad))
    bad=copy.deepcopy(data);bad['assets'][0]['receipt']['sha256']='a'*64
    record('reject fabricated planned-asset receipt',rejects(bad))
    bad=copy.deepcopy(data);bad['experiments'][0]['status']='pass'
    record('reject unexecuted experiment promotion',rejects(bad))
    bad=copy.deepcopy(data);del bad['surfaces'][0]['textureContract']['requiredMaps']['normal']
    record('reject missing numeric map contract',rejects(bad))
    bad=copy.deepcopy(data);bad['global']['coordinates']['metersPerMm']=1
    record('reject mixed units',rejects(bad))
    index=json.loads((BASE/'generated/prompt-index.json').read_text())
    trace=json.loads((BASE/'generated/traceability.json').read_text())
    record('one prompt and trace node per specification',len(index)==count==len(trace['nodes']))
    standalone=compile_outputs(data,core,standalone=True)
    payloads=[json.loads(block) for p,s in standalone.items() if p.parent.name=='prompts' for block in re.findall(r'```json\n(.*?)\n```',s,re.S)]
    record('standalone exports contain every prompt and selected global values',len(payloads)==count and {p['promptId'] for p in payloads}=={i['promptId'] for i in index} and all(p['globalContract']['coordinates']['metersPerMm']==.001 for p in payloads))
    require(all(p.read_text()==s for p,s in expected.items()),'mutation touched original files')
    record('mutation leaves canonical and generated files untouched',json.loads(SOURCE.read_text())==data)
    report={'kind':'workshop specification/compiler checks; not rendered realism evidence','status':'complete','github_sha':os.environ.get('GITHUB_SHA','local-source-digests-only'),'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [SOURCE,CORE,Path(__file__),ROOT/'scripts/generate_textile_workshop.py']},'counts':{g:len(data[g]) for g in GROUPS},'checks':checks,'summary':{'passed':len(checks),'failed':0},'openGapIds':[g['id'] for g in data['gaps']]}
    out=ROOT/'artifacts/textile-workshop';out.mkdir(parents=True,exist_ok=True);(out/'contract-evidence.json').write_text(json.dumps(report,indent=2)+'\n')
    for c in checks:print('PASS: '+c['name'])
    print(f'{len(checks)} contract checks; {count} prompts. Runtime and visual gaps remain explicit.');return 0

if __name__=='__main__':raise SystemExit(main())
