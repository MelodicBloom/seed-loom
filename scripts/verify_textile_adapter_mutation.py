#!/usr/bin/env python3
"""Verify that Textile token mutation propagates into every generated adapter."""
import copy
import json
from generate_textile_adapters import SOURCE, outputs

def token_paths(node, prefix=()):
    """Enumerate token leaves, excluding metadata such as version."""
    for key,value in node.items():
        if isinstance(value,dict) and '$value' in value:yield prefix+(key,)
        elif isinstance(value,dict):yield from token_paths(value,prefix+(key,))

def main():
    """Mutate every leaf independently; require all four exports to respond."""
    original_bytes=SOURCE.read_bytes();tokens=json.loads(original_bytes);original=outputs(tokens)
    for path,content in original.items():
        if not path.is_file() or path.read_text()!=content:raise ValueError('Missing/stale adapter '+str(path))
    if original!=outputs(tokens):raise ValueError('nondeterministic compiler')
    count=0
    for keys in token_paths(tokens):
        mutated=copy.deepcopy(tokens);node=mutated
        for key in keys:node=node[key]
        val=node['$value']
        if isinstance(val,list):node['$value']=[val[0]+.01,*val[1:]]
        elif isinstance(val,str) and val.startswith('#'):node['$value']='#123456' if val!='#123456' else '#654321'
        elif isinstance(val,(int,float)):node['$value']=val+.01
        else:raise ValueError('Unsupported token mutation '+str(keys))
        changed=outputs(mutated)
        if sum(original[p]!=changed[p] for p in original)!=4:raise ValueError('/'.join(keys)+' does not reach every adapter')
        count+=1
    if SOURCE.read_bytes()!=original_bytes or any(path.read_text()!=content for path,content in original.items()):raise ValueError('mutation changed original files')
    print(f'PASS: {count} canonical token mutations reach all four adapters; {count*4} propagation checks; originals unchanged.')
    return 0

if __name__=='__main__':raise SystemExit(main())
