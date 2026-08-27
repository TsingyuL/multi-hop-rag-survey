from __future__ import annotations
import csv,gzip,hashlib,json,math,os,random,sys,time
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import date,datetime,timedelta,timezone
from pathlib import Path
import requests
OUT=Path('tmp_a_share_delivery_20260827'); OUT.mkdir(exist_ok=True)
CAP=datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125 Safari/537.36'
H={'User-Agent':UA,'Referer':'https://data.eastmoney.com/'}
def rq(method,url,params=None,payload=None,headers=None,retries=5,timeout=30):
    hh=dict(H); hh.update(headers or {}); last=None
    for i in range(retries):
        try:
            r=requests.request(method,url,params=params,json=payload,headers=hh,timeout=timeout)
            if r.status_code in (429,500,502,503,504): raise RuntimeError(f'HTTP {r.status_code}')
            r.raise_for_status(); return r.json(),r.url
        except Exception as e:
            last=e; time.sleep((1.45**i)+random.random())
    raise RuntimeError(f'{method} {url}: {last}')
def dr(a,b):
    while a<=b: yield a; a+=timedelta(days=1)
def writegz(p,rows,fields):
    with gzip.open(p,'wt',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()
def mainboard(c): return c.startswith(('000','001','002','003','600','601','603','605'))
def suffix(sc):
    s=str(sc or '').upper()
    if s.startswith('SH') and len(s)>=8:return s[2:8]+'.SH'
    if s.startswith('SZ') and len(s)>=8:return s[2:8]+'.SZ'
    if len(s)==6 and s.isdigit():return s+('.SH' if s.startswith('6') else '.SZ')
    return s
ANN=['notice_date','stock_code','short_name','market_code','ann_type','art_code','title','column_codes','column_names','display_time','sort_date','source_type','requested_date','captured_at','available_at','source','historical_backfill']
def ann_day(d):
    ds=d.isoformat(); url='https://np-anotice-stock.eastmoney.com/api/security/ann'; q={'sr':'-1','page_size':'100','page_index':'1','ann_type':'A','client_source':'web','f_node':'0','s_node':'0','begin_time':ds,'end_time':ds}
    j,u=rq('GET',url,params=q,headers={'Referer':'https://data.eastmoney.com/notices/hsa/5.html'}); total=int((j.get('data')or{}).get('total_hits')or 0); pages=max(1,math.ceil(total/100)); its=list((j.get('data')or{}).get('list')or[]); raw=[{'requested_date':ds,'page':1,'request_url':u,'response':j}]
    for p in range(2,pages+1):
        qq=dict(q);qq['page_index']=p;jj,uu=rq('GET',url,params=qq,headers={'Referer':'https://data.eastmoney.com/notices/hsa/5.html'});its.extend((jj.get('data')or{}).get('list')or[]);raw.append({'requested_date':ds,'page':p,'request_url':uu,'response':jj})
    rows=[]
    for it in its:
        cols=it.get('columns')or[];cc='|'.join(str(x.get('column_code','')) for x in cols if isinstance(x,dict));cn='|'.join(str(x.get('column_name','')) for x in cols if isinstance(x,dict));codes=it.get('codes')or[{}]
        for c in codes:
            if not isinstance(c,dict):continue
            rows.append({'notice_date':it.get('notice_date'),'stock_code':c.get('stock_code'),'short_name':c.get('short_name'),'market_code':c.get('market_code'),'ann_type':c.get('ann_type'),'art_code':it.get('art_code'),'title':it.get('title'),'column_codes':cc,'column_names':cn,'display_time':it.get('display_time'),'sort_date':it.get('sort_date'),'source_type':it.get('source_type'),'requested_date':ds,'captured_at':CAP,'available_at':CAP,'source':'eastmoney_announcement_history','historical_backfill':True})
    return ds,rows,raw,total
def announcements():
    dates=list(dr(date(2026,4,15),date(2026,8,26))); rows=[]; counts={};errs={};rp=OUT/'eastmoney_announcements_raw_20260415_20260826.jsonl.gz'
    with gzip.open(rp,'wt',encoding='utf-8') as rf,ThreadPoolExecutor(max_workers=5) as ex:
        fs={ex.submit(ann_day,d):d for d in dates}
        for i,f in enumerate(as_completed(fs),1):
            d=fs[f]
            try:
                ds,rr,raw,total=f.result();rows.extend(rr);counts[ds]={'rows':len(rr),'total_hits':total,'pages':len(raw)}
                for x in raw:rf.write(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
            except Exception as e:errs[d.isoformat()]=repr(e)
            if i%10==0:print('ann',i,len(rows),len(errs),flush=True)
    rows.sort(key=lambda r:(r['requested_date'],r.get('art_code')or'',r.get('stock_code')or''));p=OUT/'eastmoney_announcements_20260415_20260826.csv.gz';writegz(p,rows,ANN);return {'rows':len(rows),'dates':len(dates),'counts':counts,'errors':errs,'file':p.name,'raw':rp.name}
META=['availability_basis','available_at','captured_at','decision_usable_after','historical_backfill','observed_at','source','survivorship_risk','trade_date']
def lhb_day(d):
    ds=d.isoformat();url='https://datacenter-web.eastmoney.com/api/data/v1/get';q={'sortColumns':'SECURITY_CODE,TRADE_DATE','sortTypes':'1,-1','pageSize':'500','pageNumber':'1','reportName':'RPT_DAILYBILLBOARD_DETAILSNEW','columns':'ALL','source':'WEB','client':'WEB','filter':f"(TRADE_DATE='{ds}')"}
    j,u=rq('GET',url,params=q,headers={'Referer':'https://data.eastmoney.com/stock/tradedetail.html'});res=j.get('result')or{};pages=int(res.get('pages')or1);rows=list(res.get('data')or[]);raw=[{'trade_date':ds,'page':1,'request_url':u,'response':j}]
    for p in range(2,pages+1):
        qq=dict(q);qq['pageNumber']=str(p);jj,uu=rq('GET',url,params=qq,headers={'Referer':'https://data.eastmoney.com/stock/tradedetail.html'});rows.extend((jj.get('result')or{}).get('data')or[]);raw.append({'trade_date':ds,'page':p,'request_url':uu,'response':jj})
    for r in rows:r.update({'availability_basis':'historical_backfill','available_at':CAP,'captured_at':CAP,'decision_usable_after':CAP,'historical_backfill':True,'observed_at':ds,'source':'eastmoney_lhb_history_backfill','survivorship_risk':False,'trade_date':ds})
    return ds,rows,raw
def lhb():
    dates=list(dr(date(2026,7,17),date(2026,8,25)));rows=[];counts={};errs={};rp=OUT/'eastmoney_lhb_raw_20260717_20260825.jsonl.gz'
    with gzip.open(rp,'wt',encoding='utf-8') as rf,ThreadPoolExecutor(max_workers=6) as ex:
        fs={ex.submit(lhb_day,d):d for d in dates}
        for f in as_completed(fs):
            d=fs[f]
            try:
                ds,rr,raw=f.result();rows.extend(rr);counts[ds]=len(rr)
                for x in raw:rf.write(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
            except Exception as e:errs[d.isoformat()]=repr(e)
    fields=[];seen=set()
    for r in rows:
        for k in r:
            if k not in seen and k not in META:seen.add(k);fields.append(k)
    fields+=META;rows.sort(key=lambda r:(r['trade_date'],str(r.get('SECURITY_CODE')or''),str(r.get('TRADE_ID')or'')));p=OUT/'eastmoney_lhb_detail_20260717_20260825.csv.gz';writegz(p,rows,fields);return {'rows':len(rows),'counts':counts,'errors':errs,'columns':fields,'file':p.name,'raw':rp.name}
def universe():
    url='https://push2.eastmoney.com/api/qt/clist/get';q={'pn':'1','pz':'10000','po':'1','np':'1','ut':'bd1d9ddb04089700cf9c27f6f7426281','fltt':'2','invt':'2','fid':'f3','fs':'m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23','fields':'f12,f14'};j,u=rq('GET',url,params=q,headers={'Referer':'https://quote.eastmoney.com/center/gridlist.html'},timeout=40);diff=(j.get('data')or{}).get('diff')or[];codes=[]
    for x in diff:
        c=str(x.get('f12')or'')
        if len(c)==6 and mainboard(c):codes.append(c+('.SH' if c.startswith('6') else '.SZ'))
    return sorted(set(codes)),{'request_url':u,'response':j}
def heat_one(code):
    sc='SH'+code[:6] if code.endswith('.SH') else 'SZ'+code[:6];url='https://emappdata.eastmoney.com/stockrank/getHisList';pl={'appId':'appId01','globalId':'786e4c21-70dc-435a-93bb-38','marketType':'','srcSecurityCode':sc,'yearType':'5'};j,u=rq('POST',url,payload=pl,headers={'Referer':'https://guba.eastmoney.com/rank/'},timeout=35);rows=[]
    for it in j.get('data')or[]:
        if not isinstance(it,dict):continue
        dt=it.get('calcTime')or it.get('date')or it.get('time')or it.get('ct');rk=it.get('rank') if 'rank'in it else it.get('rk');ds=str(dt)[:10]
        if '2026-07-18'<=ds<='2026-08-26':
            try:rk=int(float(rk))
            except:continue
            rows.append({'asof_date':ds,'source':'eastmoney_guba_rank_history','code':code,'rank':rk,'captured_at':CAP,'available_at':CAP,'source_timestamp':ds,'historical_backfill':True})
    return code,rows,{'code':code,'srcSecurityCode':sc,'request_url':u,'response':j}
def heat():
    codes,uraw=universe();(OUT/'heat_universe_current_20260827.txt').write_text('\n'.join(codes)+'\n',encoding='utf-8');rows=[];errs={};rp=OUT/'eastmoney_heat_getHisList_raw_20260718_20260826.jsonl.gz'
    with gzip.open(rp,'wt',encoding='utf-8') as rf:
        rf.write(json.dumps({'kind':'universe','capture':uraw},ensure_ascii=False,separators=(',',':'))+'\n')
        with ThreadPoolExecutor(max_workers=10) as ex:
            fs={ex.submit(heat_one,c):c for c in codes}
            for i,f in enumerate(as_completed(fs),1):
                c=fs[f]
                try:
                    _,rr,raw=f.result();rows.extend(rr);rf.write(json.dumps(raw,ensure_ascii=False,separators=(',',':'))+'\n')
                except Exception as e:errs[c]=repr(e)
                if i%250==0:print('heat',i,len(codes),len(rows),len(errs),flush=True)
    rows.sort(key=lambda r:(r['asof_date'],r['code']));p=OUT/'heat_rank_daily_pit_eastmoney_20260718_20260826.csv.gz';fields=['asof_date','source','code','rank','captured_at','available_at','source_timestamp','historical_backfill'];writegz(p,rows,fields);keys=set();dups=0;by={}
    for r in rows:
        k=(r['asof_date'],r['code']);dups+=k in keys;keys.add(k);by[r['asof_date']]=by.get(r['asof_date'],0)+1
    return {'rows':len(rows),'current_codes':len(codes),'per_date':by,'duplicate_keys':dups,'errors':errs,'file':p.name,'raw':rp.name,'universe_file':'heat_universe_current_20260827.txt'}
def manifest(summary):
    arts={}
    for p in OUT.iterdir():
        if p.is_file():arts[p.name]={'bytes':p.stat().st_size,'sha256':sha(p)}
    m={'captured_at':CAP,'summary':summary,'artifacts':arts};(OUT/'BACKFILL_MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
def main():
    s={}
    for n,fn in [('announcements',announcements),('lhb',lhb),('heat',heat)]:
        print('===',n,'===',flush=True)
        try:s[n]=fn()
        except Exception as e:s[n]={'fatal_error':repr(e)}
    manifest(s);print(json.dumps(s,ensure_ascii=False,indent=2),flush=True)
    bad=[]
    for n in s:
        if s[n].get('fatal_error')or s[n].get('errors'):bad.append(n)
    if bad:sys.exit(2)
if __name__=='__main__':main()
