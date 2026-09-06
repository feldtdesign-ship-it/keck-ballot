#!/usr/bin/env python3
"""Turn Dan's emailed ballot into decisions.json.
Usage: python3 parse_reply.py <dans-email.txt>  ->  writes decisions.json next to it."""
import sys,re,json,os
raw=open(sys.argv[1],encoding='utf8',errors='replace').read()
out={"version":None,"date":None,"answers":{},"unanswered":[]}
m=re.search(r'^version:\s*(\S+)',raw,re.M);  out["version"]=m.group(1) if m else None
m=re.search(r'^date:\s*(\S+)',raw,re.M);     out["date"]=m.group(1) if m else None
blocks=re.split(r'^\[([A-Za-z0-9]+)\]\s*(.*)$',raw,flags=re.M)[1:]
for i in range(0,len(blocks),3):
    aq,head,rest=blocks[i],blocks[i+1].strip(),blocks[i+2]
    d=re.search(r'^\s*decision:\s*(.*)$',rest,re.M)
    n=re.search(r'^\s*note:\s*([\s\S]*?)(?=\n\s*\n|\Z)',rest,re.M)
    dec=(d.group(1).strip() if d else "")
    out["answers"][aq]={"heading":head,"decision":dec,
        "note":re.sub(r'\n\s{8}','\n',n.group(1)).strip() if n else ""}
    if dec.upper()=="NOT ANSWERED" or not dec: out["unanswered"].append(aq)
p=os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])),"decisions.json")
json.dump(out,open(p,"w"),indent=2,ensure_ascii=False)
print(f"parsed {len(out['answers'])} answers, {len(out['unanswered'])} unanswered -> {p}")
for aq in out["unanswered"]: print("  still open:",aq)
