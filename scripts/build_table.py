"""Merge coding tables into master table + per-community coverage stats."""
import re, json, collections
import os
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','coding')+os.sep
rows=[]
def parse(path, community_of):
    for line in open(base+path):
        if not line.startswith('| ') or line.startswith('| Key') : continue
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(c)<15: continue
        key=c[0].replace('†','').strip()
        rows.append(dict(key=key, work=c[1], year=c[2], R=c[3:11], A=c[11], B=c[12], C=c[13], D=c[14], comm=community_of(key)))
sec1=set('stone2010adhoc mirsky2022survey hu2020otherplay carroll2019overcooked strouse2021fcp wang2024naht wang2025matnaht wang2025shapley bard2020hanabi zhang2024proagent agashe2023llmcoord shi2023avalon liu2024heteroaht wallace2025recollab hayler2026zsc qu2026riskaversion'.split())
sec2=set('smith1980contractnet lewis2017dealnodeal fair2022cicero bianchi2024negotiationarena abdelnabi2024stakeholders davidson2024agency bansal2025marketplace qu2026bgt'.split())
proto=set('anthropic2024mcp google2025a2a beeai2025acp chang2025anp ehtesham2025survey sander2026taxonomy krishnan2026unified du2025internet qian2026mpac kang2026governance'.split())
gov=set('dafoe2020open hammond2025multiagent sourbut2024delegation tomasev2025virtual tomasev2026intelligent ruan2026agentcity yang2026multiuser hu2025regulatory'.split())
data=set('alonsoruiz2026bridging zhong2025agentodrl ren2026gatemem johnson2026aim shukla2025multiagent'.split())
def comm(k):
    if k in sec1: return 'AHT/ZSC'
    if k in sec2: return 'Negotiation'
    if k in proto: return 'Protocols'
    if k in gov: return 'Governance/CoopAI'
    if k in data: return 'Data ecosystems'
    return None
parse('coding_part1.md', lambda k: comm(k) or 'LLM-MAS frameworks/benchmarks')
parse('coding_part2.md', lambda k: comm(k) or 'Security/identity/delegation')
parse('coding_part3.md', lambda k: 'Negotiation' if k=='zhu2025riskygame' else 'Security/identity/delegation')
# Key papers from deep reads (notes/key_papers.md)
rows += [
 dict(key='qian2026mpac',work='MPAC',year='2026',R='◐ ◐ ○ ◐ ◐ ● ◐ ◐'.split(),A='protocol-mediated',B='multiple principals',C='centralized (coordinator, credential profiles)',D='self-play (Claude only) + enforcement unit tests',comm='Protocols'),
 dict(key='veski2026capmas',work='CAPMAS',year='2026',R='○ ○ ○ ● ○ ○ ● ◐'.split(),A='n/a (authorization layer)',B='single principal / single trust domain',C='capability-based (macaroons)',D='micro-benchmarks; no attack eval',comm='Security/identity/delegation'),
 dict(key='kang2026governance',work='Governance Gaps',year='2026',R='○ ○ ○ ○ ◐ ◐ ◐ ○'.split(),A='protocol analysis',B='multiple principals (conceptual)',C='n/a',D='none (spec analysis)',comm='Protocols'),
]
# dedupe (qu2026bgt is a version of qu2026riskaversion -> drop bgt)
rows=[r for r in rows if r['key']!='qu2026bgt']
seen=set(); out=[]
for r in rows:
    if r['key'] in seen: continue
    seen.add(r['key']); out.append(r)
rows=out
n=len(rows)
print('TOTAL',n)
cnt={f'R{i+1}':collections.Counter(r['R'][i] for r in rows) for i in range(8)}
for k,v in cnt.items(): print(k, dict(v))
both=[r['key'] for r in rows if r['R'][0]=='●' and r['R'][7]=='●']
print('R1●&R8●:',both)
r1r8half=[r['key'] for r in rows if r['R'][0]!='○' and r['R'][7]!='○']
print('R1≠○ & R8≠○:',r1r8half)
# per community coverage: fraction of works with ● or ◐ per req
comms=collections.defaultdict(list)
for r in rows: comms[r['comm']].append(r)
lines=['| Community | n | '+' | '.join(f'R{i}' for i in range(1,9))+' |','|---|---|'+'---|'*8]
for c,rs in sorted(comms.items()):
    cells=[]
    for i in range(8):
        f=sum(r['R'][i]=='●' for r in rs); p=sum(r['R'][i]=='◐' for r in rs)
        cells.append(f'{f}/{p}')
    lines.append(f'| {c} | {len(rs)} | '+' | '.join(cells)+' |')
open(base+'coverage_by_community.md','w').write('\n'.join(lines)+'\n')
print('\n'.join(lines))
# full appendix table
full=['| Work | Year | Community | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | B (trust) | D (evaluation) |','|---|---|---|'+'---|'*10]
for r in sorted(rows,key=lambda r:(r['comm'],r['year'])):
    full.append(f"| {r['work']} [@{r['key']}] | {r['year']} | {r['comm']} | "+' | '.join(r['R'])+f" | {r['B']} | {r['D']} |")
open(base+'master_table.md','w').write('\n'.join(full)+'\n')
json.dump(rows,open(base+'master.json','w'),ensure_ascii=False,indent=1)
