from pathlib import Path
import csv, random
rng=random.Random(1701);p=Path(__file__).resolve().parents[1]/'data'/'waiai_synthetic.csv';p.parent.mkdir(parents=True,exist_ok=True)
with p.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['synthetic_participant_id','opportunities','provided_usable','implementation_ratio','baseline_exhaustion','week16_exhaustion','employment_exit'])
 for i in range(1,241):
  n=rng.choice([0]+list(range(1,16)));k=rng.randint(0,n) if n else 0; ratio=round(k/n,3) if n else ''
  baseline=round(max(0,min(100,rng.gauss(48,15))),1)
  follow=round(max(0,min(100,.65*baseline+(.35*baseline if n==0 else 25*(1-k/n))+rng.gauss(0,10))),1)
  exited=int(rng.random()<(0.10+(follow/100)*.07))
  w.writerow([f'SYN-{i:04}',n,k,ratio,baseline,follow,exited])
print('Generated fictional data for methods demonstration:',p)
