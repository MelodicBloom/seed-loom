#!/usr/bin/env python3
"""Compile the workshop consumer specification into prompts and traceable adapters.

This compiler produces specifications. It does not render cloth or establish
material fidelity. Core runtime tokens retain their existing authority.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'initiatives/textile-interface/workshop'
SOURCE = BASE / 'registry.json'
CORE = ROOT / 'initiatives/textile-interface/tokens/textile.tokens.json'
GROUPS = ('surfaces','components','scenes','assets','methods','rules','implementations','experiments','gaps')
FENCE = chr(96)*3

def dump(value):
    """Use one deterministic JSON representation for every generated output."""
    return json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n'

def records(data):
    """Yield typed registry records in their stable authored order."""
    for group in GROUPS:
        for item in data[group]:
            yield group,item

def material_options(surface):
    """Translate authored fields into named Three.js r187 construction options.

    A colored albedo texture must use a white material color factor. Numeric
    maps multiply the factors below. Geometry dimensions remain separate.
    """
    p=surface['pbr']
    return {'materialId':surface['id'],'status':'recipe-not-rendered','package':'three@0.187.0',
      'optionsWithoutTextures':{'color':p['baseColorHex'],'roughness':p['roughness'],'metalness':p['metalness'],'ior':p['ior'],'specularIntensity':p['specularIntensity'],'sheen':p['sheen'],'sheenColor':p['sheenColorHex'],'sheenRoughness':p['sheenRoughness'],'anisotropy':p['anisotropy'],'anisotropyRotation':p['anisotropyRotationRad'],'normalScale':p['normalScaleXY'],'displacementScale':p['displacementScaleMm']*.001,'displacementBias':p['displacementBiasMm']*.001,'alphaTest':p['alphaCutoff'] if p['alphaMode']=='MASK' else 0,'transparent':p['alphaMode']=='BLEND','opacity':p['opacity'],'transmission':p['transmission'],'clearcoat':p['clearcoat'],'clearcoatRoughness':p['clearcoatRoughness'],'iridescence':p['iridescence'],'iridescenceIOR':p['iridescenceIOR'],'iridescenceThicknessMinimum':p['iridescenceThicknessMinNm'],'iridescenceThicknessMaximum':p['iridescenceThicknessMaxNm'],'side':'DoubleSide' if p['doubleSided'] else 'FrontSide'},
      'textureBindings':{'baseColor':'map; color becomes #FFFFFF when the authored full-color albedo is bound','normal':'normalMap; Vector2(normalScaleXY)','orm':'aoMap reads R; roughnessMap G; metalnessMap B; AO UV compatibility must be checked','height':'displacementMap; numeric normalization matches declared mm amplitude','sheenColor':'sheenColorMap RGB; sRGB','sheenRoughness':'sheenRoughnessMap A; NoColorSpace','anisotropy':'anisotropyMap RG direction B strength; NoColorSpace','coverage':'alphaMap reads G; white=covered; NoColorSpace'},
      'construction':surface['construction'],'mapContract':surface['textureContract']}

def leaf_rows(value, path=''):
    """Enumerate every named field, retaining empty arrays as explicit values."""
    if isinstance(value,dict):
        for key,item in value.items():
            yield from leaf_rows(item,path+'.'+key if path else key)
    elif isinstance(value,list) and value:
        for item in value: yield from leaf_rows(item,path+'[]')
    else: yield path,value

def field_meaning(path):
    """Name units and the actual current or planned consumer for each field."""
    end=path.split('.')[-1].replace('[]','')
    units='none; string, boolean, enum, or metadata'
    for suffix,unit in [('Micrometers','micrometers'),('Seconds','seconds'),('MPerN','meters per newton'),('NPerM','newtons per meter'),('NsPerM','newton seconds per meter'),('Mps2','meters per second squared'),('Mps','meters per second'),('Mm','millimeters'),('Nm','nanometers'),('Px','CSS pixels unless texture/image resolution'),('Rad','radians'),('Deg','degrees'),('Ms','milliseconds'),('Kg','kilograms'),('KiB','1024 bytes'),('MiB','1048576 bytes'),('Hz','hertz'),('DbfsMax','dBFS peak ceiling'),('PercentCases','percent'),('Ch','approximate character width'),('M','meters')]:
        if end.endswith(suffix): units=unit; break
    if end in ['normalScaleXY','flatteningZ','openAreaRatio','fuzzCoverageRatio','maxDpr','exposure','canvasAspectRatio','bodyLineHeight','labelLineHeight','opacity','runtimeGain','safeInsetRatio']:
        units='dimensionless factor'
    if end in ['fiberDiameterMicrometers']:units='micrometers'
    if end=='plyTwistTurnsPerMm':units='turns per millimeter'
    if end in ['minimum','maximum','initialValue']:units='declared progress unit or selection value; see owning record'
    if end in ['bitDepth']:units='bits per channel'
    if end in ['viewBox']:units='SVG user units'
    if end in ['neutralValue']:units='declared map-channel encoding; bytes for 8-bit maps, normalized scalar for height'
    if end in ['curveSamplesPerMm','cssPxPerMmAtOneX']:units='samples or CSS pixels per millimeter as named'
    if end.endswith('Ratio') or end.endswith('Intensity') or end in ['roughness','metalness','sheen','sheenRoughness','opacity','transmission','clearcoat','clearcoatRoughness','anisotropy','alphaCutoff']:
        units='dimensionless authored factor; inspect declared range'
    if path.startswith('surfaces[].pbr.'):
        consumer='material_options compiler -> generated/material-options.json -> future Three.js material importer I07; renderer not implemented'
    elif path.startswith('surfaces[].construction.'):
        consumer='fully resolved surface prompt and material-options construction -> future geometry builder I02/I03/I04/I05'
    elif 'textureContract' in path:
        consumer='asset author/export/import prompt -> I07/I13; validated metadata, unproduced textures'
    elif path.startswith('components'):
        consumer='resolved component prompt and graph; only C25 has an existing Core runtime binding'
    elif path.startswith('methods'):
        consumer='method prompt and design-to-code documentation; illustrative snippets, not shipped renderer functions'
    elif path.startswith('experiments'):
        consumer='planned trial contract and acceptance reviewer; execution status remains planned'
    elif path.startswith('gaps'):
        consumer='gap/fix prompt and promotion boundary; CI rejects broken references, not unresolved planned work'
    elif path.startswith('sources'):
        consumer='prompt source list and SOURCES.md; evidence provenance only'
    else:
        consumer='prompt compiler, traceability validator, and named future implementation contract'
    return units,consumer

def dependencies(item):
    """Collect typed links that the validator must resolve."""
    result=[]
    for key in ('materialIds','componentIds','assetIds','dependencyIds','methodIds','verificationIds','affectedIds'):
        result.extend(item.get(key,[]))
    if item.get('methodId'):result.append(item['methodId'])
    return list(dict.fromkeys(result))

def compile_outputs(data, core, standalone=False):
    """Compile all consumer documents without mutating either canonical input."""
    all_records=list(records(data)); by_id={v['id']:v for _,v in all_records}
    source_by_id={s['sourceId']:s for s in data['sources']}
    core_rows=[{'path':path,'value':value} for path,value in leaf_rows(core) if path.endswith('.$value') or '.$value[]' in path]
    common={**data['global'],'integration':data['integration'],'coreTokenValues':core_rows}
    instructions={
      'surfaces':'Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.',
      'components':'Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.',
      'scenes':'Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.',
      'assets':'Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.',
      'methods':'Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.',
      'rules':'Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.',
      'implementations':'Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.',
      'experiments':'Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.',
      'gaps':'Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.'}
    prompt_sections={g:[] for g in GROUPS}; index=[]; nodes=[]
    for group,item in all_records:
        pid='P-'+item['id']; deps=dependencies(item)
        closure=[]; queue=list(deps)
        while queue:
            dep=queue.pop(0)
            if dep==item['id'] or dep in closure:continue
            closure.append(dep);queue.extend(dependencies(by_id[dep]))
        resolved=[{'id':i,'specification':by_id[i]} for i in closure]
        refs=list(dict.fromkeys(s for record in [item,*[by_id[i] for i in closure]] for s in record.get('sourceIds',['S00'])))
        payload={'promptId':pid,'task':instructions[group],'specification':item,'returnContract':{'required':['resultStatus','selectedValuesUsed','changedFilesOrAssets','implementationMapping','testsExecuted','evidence','openGaps','interpretations'],'permittedResultStatus':['specified','implemented-unverified','pass','fail','blocked','inconclusive'],'rules':['Keep source facts, design choices, interpretations and measurements distinct.','No invented specimen data, licenses, hashes, successful tests, or deployments.','Do not silently change values; propose and justify a versioned change.','No unrelated refactor, force push, merge, publication, or message to another person.']}}
        if standalone:
            payload.update(globalContract=common,resolvedDependencies=resolved,relevantLightPresets=data['lightPresets'] if group in ['surfaces','scenes','implementations','experiments'] else {},sources=[source_by_id[s] for s in refs])
        else:
            payload.update(globalContractRef='../../registry.json#/global',dependencyIds=closure,sourceIds=refs,standaloneCommand='python scripts/generate_textile_workshop.py --prompt '+pid)
        direction='Copy the entire JSON contract into the agent or production tool.' if standalone else 'For a self-contained copy with all dependency values, run the standaloneCommand in this contract.'
        text='<a id="'+pid.lower()+'"></a>\n\n## '+pid+' '+item['name']+'\n\n'+direction+' For image-only tools, use appearance fields while retaining the concept-only boundary.\n\n'+FENCE+'json\n'+dump(payload)+FENCE+'\n'
        prompt_sections[group].append(text)
        index.append({'promptId':pid,'recordId':item['id'],'category':group,'name':item['name'],'anchor':(pid+' '+item['name']).lower().replace(' ','-')})
        nodes.append({'id':item['id'],'category':group,'promptId':pid,'dependsOn':deps,'sourceIds':refs,'status':item.get('status','specified-method'),'runtimeConsumer':data['integration']['coreReference'] if item['id']=='C25' else 'planned; inspect specification','contractTest':'scripts/verify_textile_workshop.py','runtimeTest':'scripts/verify_textile_visual.py' if item['id']=='C25' else 'planned; no runtime acceptance claimed','ciWorkflow':data['integration']['ciWorkflow'],'contractCiJob':'validate-textile-interface','runtimeCiJob':'textile-visual-evidence' if item['id']=='C25' else 'not implemented','evidenceBoundary':'structural contract and compiler evidence only' if item['id']!='C25' else 'Core Chromium checks; exact-head result required'})
    prompt_index='# Textile workshop prompt suite\n\n'+str(len(index))+' '+('fully resolved prompts' if standalone else 'versioned prompts with standalone export')+'. These are specifications and implementation tasks, not completed assets. Research checked '+data['global']['date']+'.\n\n'
    prompt_index+='| Prompt | Category | Subject |\n|---|---|---|\n'+''.join('| ['+i['promptId']+'](prompts/'+i['category']+'.md#'+i['promptId'].lower()+') | '+i['category']+' | '+i['name']+' |\n' for i in index)+'\n'
    fields={}
    for path,value in leaf_rows(data):
        if path not in fields:
            unit,consumer=field_meaning(path)
            if type(value) in [int,float] and unit.startswith('none;'):unit='dimensionless scalar or count; semantic meaning is the named owning field'
            fields[path]={'field':path,'type':type(value).__name__,'units':unit,'valueAuthority':'API/standards constraint where cited; otherwise design-selected or status metadata','consumer':consumer,'selectedExamples':[],'allSelectedValues':[]}
        fields[path]['allSelectedValues'].append(value)
        if value not in fields[path]['selectedExamples'] and len(fields[path]['selectedExamples'])<4: fields[path]['selectedExamples'].append(value)
    mats=[material_options(s) for s in data['surfaces']]
    css=['/* GENERATED consumer tokens. These do not implement the enhanced renderer. */',':root {']
    for key,value in data['global']['palette'].items():css.append('  --workshop-'+key+': '+value+';')
    for s in data['surfaces']:
        prefix='--workshop-'+s['id'].lower()
        css += [f'  {prefix}-color: {s["pbr"]["baseColorHex"]};',f'  {prefix}-roughness: {s["pbr"]["roughness"]};',f'  {prefix}-yarn-mm: {s["construction"]["yarnDiameterWarpMm"]};']
    css.append('}')
    for field in fields.values():
        values=field.pop('allSelectedValues')
        field['occurrenceCount']=len(values)
        field['orderedValuesSha256']=hashlib.sha256(dump(values).encode()).hexdigest()
    trace={'version':data['global']['version'],'integration':data['integration'],'nodes':nodes,'coreSourceBindings':core_rows,'feedbackLoop':'intent -> registry -> resolved prompt/adapter -> runtime or planned consumer -> test -> evidence -> experiment/reviewer -> versioned correction','statusBoundary':'Contract completeness is not runtime completeness or visual acceptance.'}
    source_md='# Research sources and interpretations\n\nValues in the registry are authored starting points unless explicitly identified as API/standards constraints. No source is claimed to validate these selected material values. Research checked '+data['global']['date']+'.\n\n'
    for s in data['sources']:
        source_md+='## '+s['sourceId']+' '+s['title']+'\n\n'+s['finding']+'\n\nInterpretation: '+s['interpretation']+'\n\n'+('Source: '+s['url'] if s['sourceId']!='S00' else 'Source: supplied attachment snapshot. Original source not refreshed or edited. Snapshot SHA-256: '+s['snapshotSha256'])+'\n\n'
    methods_md='# Design intent to code translation\n\nThese snippets are implementation recipes. The current PR ships the specification compiler and Core reference fixes; it does not ship these enhanced-renderer functions.\n\n'
    for m in data['methods']:
        methods_md+='## '+m['id']+' '+m['name']+'\n\nSignature: '+m['signature']+'\n\nFormula: '+m['formula']+'\n\nSelected example:\n\n'+FENCE+'json\n'+dump(m['selectedExample'])+FENCE+'\n\n'+FENCE+('glsl' if m['id']=='F09' else 'js')+'\n'+m['code']+'\n'+FENCE+'\n\nBoundary: '+m['scope']+'\n\n'
    out={BASE/'generated/PROMPTS.md':prompt_index,BASE/'generated/prompt-index.json':dump(index),BASE/'generated/field-dictionary.json':dump(list(fields.values())),BASE/'generated/traceability.json':dump(trace),BASE/'generated/material-options.json':dump(mats),BASE/'generated/workshop.tokens.css':'\n'.join(css)+'\n',BASE/'generated/SOURCES.md':source_md,BASE/'generated/METHODS.md':methods_md}
    out.update({BASE/'generated/prompts'/(''+group+'.md'):'# '+group.title()+' prompt contracts\n\n'+'\n'.join(parts) for group,parts in prompt_sections.items()})
    return out

def main():
    """Generate outputs or reject any missing, stale, or unexpected output file."""
    parser=argparse.ArgumentParser(); mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--check',action='store_true');mode.add_argument('--prompt');mode.add_argument('--export-directory',type=Path)
    args=parser.parse_args()
    data=json.loads(SOURCE.read_text()); core=json.loads(CORE.read_text()); out=compile_outputs(data,core,standalone=bool(args.prompt or args.export_directory))
    if args.prompt:
        ident=args.prompt.upper();ident=ident if ident.startswith('P-') else 'P-'+ident
        row=next((r for r in json.loads(out[BASE/'generated/prompt-index.json']) if r['promptId']==ident),None)
        if not row:parser.error('Unknown prompt ID '+ident)
        section=out[BASE/'generated/prompts'/(''+row['category']+'.md')].split('<a id="'+ident.lower()+'"></a>',1)[1]
        print(section.split(FENCE+'json\n',1)[1].split('\n'+FENCE,1)[0]);return 0
    if args.export_directory:
        export=args.export_directory.resolve()
        if export==BASE or BASE in export.parents:parser.error('Export outside the canonical workshop directory')
        for path,content in out.items():
            dest=export/path.relative_to(BASE/'generated');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content)
        print(f'Exported {len(out)} standalone documents.');return 0
    stale=[]
    for path,content in out.items():
        if args.check:
            if not path.is_file() or path.read_text()!=content:stale.append(str(path.relative_to(ROOT)))
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
    expected={p.relative_to(BASE/'generated').as_posix() for p in out}; actual={p.relative_to(BASE/'generated').as_posix() for p in (BASE/'generated').rglob('*') if p.is_file()}
    if args.check and actual!=expected:stale.append('unexpected or absent generated file set')
    if stale:print('FAIL stale workshop outputs: '+', '.join(stale));return 1
    print(('Checked' if args.check else 'Generated')+f' {len(out)} workshop outputs; {sum(1 for _ in records(data))} indexed prompts.');return 0

if __name__=='__main__': raise SystemExit(main())
