from pathlib import Path
import csv,statistics,math
p=Path(__file__).resolve().parents[1]/'data'/'waiai_synthetic.csv'
with p.open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
usable=[r for r in rows if int(r['opportunities'])>0]
excluded=len(rows)-len(usable)
x=[float(r['implementation_ratio']) for r in usable];y=[float(r['week16_exhaustion']) for r in usable]
mx,my=statistics.mean(x),statistics.mean(y)
num=sum((a-mx)*(b-my) for a,b in zip(x,y));den=math.sqrt(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))
print('Fictional research records:',len(rows),'| scoreable:',len(usable),'| zero-opportunity:',excluded)
print('Demonstration raw correlation:',round(num/den,3) if den else 'undefined')
print('This relationship is built into the generator. It is NOT empirical validation or causal evidence.')
