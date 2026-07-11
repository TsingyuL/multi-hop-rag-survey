import os, math, textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon, Arc
from matplotlib.lines import Line2D
from matplotlib import colors as mcolors

OUT = Path(__file__).resolve().parents[1]
PDF = OUT/'pdf'; SVG = OUT/'svg'; PNG = OUT/'png'
for d in [PDF, SVG, PNG]: d.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.unicode_minus': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'svg.fonttype': 'none',
})

COL = {
    'obs':'#2F6BFF',      # blue
    'util':'#2CA25F',     # green
    'exp':'#F28E2B',      # orange
    'fus':'#7B61FF',      # purple
    'faith':'#D62728',    # red
    'dark':'#263238',
    'mid':'#60717F',
    'gray':'#AAB3C0',
    'light':'#F7F9FC',
    'latent':'#EFF3F8',
    'obsfill':'#FFFFFF',
    'edge':'#CBD3DF',
    'warn':'#FFE7E4',
    'ok':'#E8F6EE',
    'paper':'#FFFFFF',
}
EST = [
    ('obs','Observability'),
    ('util','Utility'),
    ('exp','Exposure'),
    ('fus','Fusion'),
    ('faith','Faithfulness'),
]


def setup(figsize=(7.2,4.2), xlim=(0,16), ylim=(0,10)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axis('off')
    fig.patch.set_facecolor('white'); ax.set_facecolor('white')
    return fig, ax


def save(fig, name):
    fig.savefig(PDF/f'{name}.pdf', bbox_inches='tight', pad_inches=0.02)
    fig.savefig(SVG/f'{name}.svg', bbox_inches='tight', pad_inches=0.02)
    fig.savefig(PNG/f'{name}.png', dpi=240, bbox_inches='tight', pad_inches=0.02)
    plt.close(fig)


def rounded(ax, xy, w, h, label='', fc='white', ec=None, lw=1.2, r=0.12, ls='solid', alpha=1, z=1, text_kw=None):
    ec = ec if ec is not None else COL['edge']
    patch = FancyBboxPatch(xy, w, h,
                           boxstyle=f"round,pad=0.035,rounding_size={r}",
                           facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, alpha=alpha, zorder=z)
    ax.add_patch(patch)
    if label:
        kw = dict(ha='center', va='center', fontsize=9, color=COL['dark'], zorder=z+1)
        if text_kw: kw.update(text_kw)
        ax.text(xy[0]+w/2, xy[1]+h/2, label, **kw)
    return patch


def arrow(ax, p1, p2, color=None, lw=1.5, style='-|>', rad=0.0, ls='solid', alpha=1, z=5, mutation_scale=12):
    color = color or COL['mid']
    arr = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=mutation_scale,
                          linewidth=lw, color=color, linestyle=ls,
                          connectionstyle=f"arc3,rad={rad}", alpha=alpha, zorder=z)
    ax.add_patch(arr)
    return arr


def badge(ax, x, y, key, text=None, w=None, h=0.32, fs=7.3):
    text = text if text is not None else key
    if w is None:
        w = 0.38 + 0.085*len(text)
    rounded(ax, (x,y), w, h, text, fc=mcolors.to_rgba(COL[key],0.10), ec=COL[key], lw=0.9, r=0.08,
            text_kw={'fontsize':fs,'color':COL[key],'fontweight':'bold'})
    return w


def title(ax, main, subtitle=None):
    ax.text(0.25, 9.7, main, fontsize=12.5, fontweight='bold', color=COL['dark'], ha='left', va='top')
    if subtitle:
        ax.text(0.25, 9.18, subtitle, fontsize=8.5, color=COL['mid'], ha='left', va='top')


def legend_estimands(ax, x=9.4, y=9.55, compact=False):
    fs = 7.2 if compact else 7.5
    gap = 1.22 if compact else 1.28
    for i,(k,lbl) in enumerate(EST):
        ax.add_patch(Circle((x+i*gap, y), 0.075, color=COL[k], zorder=10))
        ax.text(x+i*gap+0.12, y, lbl if not compact else lbl[:4]+'.', va='center', fontsize=fs, color=COL['mid'])


def label_box(ax, x, y, text, color=COL['mid'], fs=7.8, ha='center', va='center', weight=None):
    ax.text(x,y,text,fontsize=fs,color=color,ha=ha,va=va,fontweight=weight)

# F1

def fig1():
    fig, ax = setup((7.5,4.5))
    title(ax, 'F1. Latent evidence-chain inference, not another RAG pipeline',
          'Observable modules are noisy projections of an unobserved support chain.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # layer backgrounds
    rounded(ax,(0.25,5.75),15.5,2.85,'',fc=COL['latent'],ec='#D6DEE8',lw=1.0,r=0.15,ls='dashed',z=0)
    rounded(ax,(0.25,1.15),15.5,3.7,'',fc='white',ec='#D6DEE8',lw=1.0,r=0.15,z=0)
    ax.text(0.48,8.30,'latent target',fontsize=8.5,color=COL['mid'],fontweight='bold')
    ax.text(0.48,4.50,'observable system trace',fontsize=8.5,color=COL['mid'],fontweight='bold')
    # latent chain
    xs=[2.0,5.0,8.0,11.0]
    labs=[r'$e^\star_1$\nbiography',r'$e^\star_2$\nbridge',r'$e^\star_3$\nidentity',r'$e^\star_4$\nanswer unit']
    for i,x in enumerate(xs):
        rounded(ax,(x-0.55,6.75),1.1,0.75,labs[i],fc='white',ec=COL['gray'],lw=1.2,r=0.18,ls='dashed',text_kw={'fontsize':8})
        if i>0:
            arrow(ax,(xs[i-1]+0.58,7.12),(x-0.58,7.12),color=COL['gray'],lw=1.4,ls='dashed')
    ax.text(12.2,7.12,r'$C^\star=(e^\star_1,\ldots,e^\star_m)$',fontsize=10,color=COL['dark'],va='center')
    # observable pipeline
    steps=[('q\nquestion',1.15,3.10,1.25,0.75),
           (r'$L_N$\nretrieved pool',3.4,2.9,1.7,1.15),
           (r'$E_K$\nbudgeted context',6.2,2.9,1.8,1.15),
           (r'$\pi(E_K)$\nreader ordering',9.1,2.9,1.8,1.15),
           (r'$\hat a$\ngenerated answer',12.1,2.9,1.8,1.15)]
    for label,x,y,w,h in steps:
        rounded(ax,(x,y),w,h,label,fc='white',ec=COL['edge'],lw=1.25,r=0.18,text_kw={'fontsize':8.5})
    arrows=[((2.42,3.48),(3.38,3.48),'obs',r'$R_N$'),
            ((5.12,3.48),(6.18,3.48),'util',r'$S_K$'),
            ((8.02,3.48),(9.08,3.48),'exp',r'order'),
            ((10.92,3.48),(12.08,3.48),'fus',r'$G$')]
    for p1,p2,k,lab in arrows:
        arrow(ax,p1,p2,color=COL[k],lw=2.0)
        ax.text((p1[0]+p2[0])/2,(p1[1]+p2[1])/2+0.28,lab,fontsize=8,color=COL[k],ha='center',fontweight='bold')
    # vertical noisy projections
    projections=[(4.25,6.72,4.08,'obs','chain appears in pool'),
                 (7.1,6.72,4.08,'util','chain survives budget'),
                 (10.0,6.72,4.08,'exp','chain is accessible'),
                 (13.0,6.72,4.08,'faith','answer uses chain')]
    for x,y1,y2,k,txt in projections:
        arrow(ax,(x,y1),(x,y2),color=COL[k],lw=1.2,ls='dotted',style='-|>',mutation_scale=10)
        badge(ax,x-0.58,y2-0.62,k,k,fs=7)
        ax.text(x+0.13,y2-0.47,txt,fontsize=7.2,color=COL['mid'],ha='left',va='center')
    # bottleneck notes
    note_x=[3.2,5.9,8.8,11.6]
    note_txt=['absence\nmissing bridge','selection bias\nunder K','lost-in-middle\n/ diffusion','post-hoc\nrationalization']
    note_col=['obs','util','exp','faith']
    for x,t,k in zip(note_x,note_txt,note_col):
        rounded(ax,(x,1.55),1.75,0.72,t,fc=mcolors.to_rgba(COL[k],0.07),ec=mcolors.to_rgba(COL[k],0.45),lw=0.9,r=0.12,text_kw={'fontsize':7.2,'color':COL['dark']})
    # small equation strip
    rounded(ax,(0.55,0.28),14.85,0.55,
            r'$P(\hat a=a^\star) \approx P(P)P(S|P)P(O|S)P(U|O)P(T|U)$',fc='#FBFCFE',ec='#E5EAF2',lw=0.8,r=0.12,
            text_kw={'fontsize':9.2,'color':COL['dark']})
    save(fig,'F1_latent_chain_pipeline')

# F2

def fig2():
    fig, ax = setup((7.5,4.3))
    title(ax, 'F2. Bottleneck coupling among the five estimands',
          'A single weak factor can dominate the end-to-end success probability.')
    legend_estimands(ax, 9.2, 9.55, compact=True)
    # flow base
    theta=[0.82,0.67,0.74,0.51,0.63]
    keys=['obs','util','exp','fus','faith']
    names=['pool\nobservability','conditional\nutility','reader\nexposure','fusion\nreliability','causal\nfaithfulness']
    xs=np.linspace(2.0,12.7,5)
    prod=1.0
    ytop=7.2
    ybottom=3.0
    prev=(0.9,ytop)
    ax.text(0.8,7.35,'start\n1.00',fontsize=8,color=COL['mid'],ha='center')
    for i,(x,t,k,nm) in enumerate(zip(xs,theta,keys,names)):
        h=3.1*t
        rounded(ax,(x-0.58,3.10),1.16,3.25,'',fc='#FFFFFF',ec='#D8E0EA',lw=0.9,r=0.12)
        ax.add_patch(FancyBboxPatch((x-0.44,3.22),0.88,h,boxstyle='round,pad=0.02,rounding_size=0.10',
                                    facecolor=mcolors.to_rgba(COL[k],0.78),edgecolor=COL[k],linewidth=0.8,zorder=3))
        ax.text(x,6.75,rf'$\theta_{{{k}}}$',fontsize=10,ha='center',color=COL[k],fontweight='bold')
        ax.text(x,3.00,f'{t:.2f}',fontsize=9,ha='center',color=COL['dark'],fontweight='bold')
        ax.text(x,2.25,nm,fontsize=7.6,ha='center',color=COL['mid'])
        curr_prod=prod*t
        # product path
        y_cur=7.3-4.4*(1-curr_prod)
        arrow(ax,prev,(x-0.62,y_cur),color=COL[k],lw=1.5,alpha=0.95,rad=0.02)
        ax.add_patch(Circle((x-0.72,y_cur),0.055,color=COL[k],zorder=6))
        ax.text(x-0.52,y_cur+0.23,f'{curr_prod:.2f}',fontsize=7,color=COL['mid'])
        prev=(x+0.62,y_cur)
        prod=curr_prod
    arrow(ax,prev,(15.0,7.3-4.4*(1-prod)),color=COL['dark'],lw=1.6)
    rounded(ax,(13.95,4.48),1.6,1.0,f'final\n{prod:.2f}',fc='#FBFCFE',ec=COL['dark'],lw=1.0,r=0.15,text_kw={'fontsize':9,'fontweight':'bold'})
    # theorem inset
    rounded(ax,(0.8,0.47),14.7,1.15,'',fc='#FAFBFD',ec='#DDE5EF',lw=0.9,r=0.16)
    ax.text(1.1,1.23,'Theorem 1 visualized',fontsize=8.5,fontweight='bold',color=COL['dark'])
    ax.text(4.0,1.22,r'$P(\hat a=a^\star)\ \leq\ \min_i\ \theta_i$',fontsize=11,color=COL['dark'],ha='center',va='center')
    ax.text(9.2,1.22,r'$\partial P(\hat a=a^\star)/\partial\theta_i\ \leq\ \prod_{j\ne i}\theta_j$',fontsize=11,color=COL['dark'],ha='center',va='center')
    ax.text(13.6,1.20,'fusion is the\nvisible bottleneck',fontsize=8,color=COL['fus'],ha='center',va='center',fontweight='bold')
    # highlight fusion column
    rounded(ax,(xs[3]-0.8,1.95),1.6,5.35,'',fc='none',ec=COL['fus'],lw=1.2,r=0.15,ls='dashed',z=0)
    save(fig,'F2_estimand_bottleneck_flow')

# Helper lane drawing

def method_pill(ax,x,y,w,label,key=None,fs=7.2):
    fc='#FFFFFF'; ec=COL['edge'] if key is None else mcolors.to_rgba(COL[key],0.55)
    rounded(ax,(x,y),w,0.52,label,fc=fc,ec=ec,lw=0.9,r=0.12,text_kw={'fontsize':fs,'color':COL['dark']})
    if key:
        ax.add_patch(Circle((x+0.15,y+0.26),0.045,color=COL[key],zorder=5))

# F3

def fig3():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F3. Graph-based methods as chain-structure estimators',
          'Graphs improve observability through expansion and fusion through path constraints.')
    legend_estimands(ax, 9.0, 9.55, compact=True)
    # miniature graph at left
    rounded(ax,(0.55,1.1),2.2,7.2,'',fc='#F7FAFF',ec='#DDE6F3',lw=0.9,r=0.18)
    ax.text(1.65,7.95,'chain prior',fontsize=8.3,fontweight='bold',color=COL['mid'],ha='center')
    nodes=[(1.15,6.8,'q'),(1.9,5.9,'v1'),(0.95,4.9,'v2'),(2.1,4.35,'v3'),(1.45,3.1,'ans')]
    for x,y,l in nodes:
        ax.add_patch(Circle((x,y),0.23,facecolor='white',edgecolor=COL['obs'],linewidth=1.0))
        ax.text(x,y,l,fontsize=7,ha='center',va='center',color=COL['dark'])
    for a,b in [(0,1),(1,2),(1,3),(2,4),(3,4)]:
        arrow(ax,(nodes[a][0],nodes[a][1]),(nodes[b][0],nodes[b][1]),color=COL['gray'],lw=1.0,style='-',mutation_scale=1)
    arrow(ax,(1.15,6.8),(1.45,3.1),color=COL['obs'],lw=2.2,rad=-0.18)
    ax.text(1.6,2.05,'path/subgraph\ncan be audited',fontsize=7.6,color=COL['mid'],ha='center')
    # lanes
    lanes=[('Question-specific heterogeneous graphs','GRAFT-Net','PullNet','DFGN / HGN','SAE / HDE'),
           ('LM-GNN coupled reasoners','QA-GNN','GreaseLM','UniKGQA','ReaRev / NSM'),
           ('LLM-built and LLM-traversed graphs','ToG / ToG 2.0','RoG','GraphRAG','HippoRAG / LightRAG')]
    ys=[7.0,4.85,2.7]
    for li,(title_lane,*methods) in enumerate(lanes):
        y=ys[li]
        rounded(ax,(3.05,y-0.58),12.4,1.38,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.15)
        ax.text(3.25,y+0.40,title_lane,fontsize=8.2,fontweight='bold',color=COL['dark'],ha='left')
        x0=3.35
        for j,m in enumerate(methods):
            method_pill(ax,x0+j*2.75,y-0.25,2.1,m,key=['obs','fus','fus','faith'][min(j,3)])
            if j>0:
                arrow(ax,(x0+j*2.75-0.28,y+0.01),(x0+j*2.75-0.70,y+0.01),color=COL['gray'],style='<|-',lw=0.8,mutation_scale=7)
        # right badges
        bx=13.1
        if li==0:
            badge(ax,bx,y+0.12,'obs','obs',fs=6.8)
            badge(ax,bx+0.65,y+0.12,'fus','fus',fs=6.8)
        elif li==1:
            badge(ax,bx,y+0.12,'fus','fus',fs=6.8)
            badge(ax,bx+0.65,y+0.12,'faith','faith',fs=6.8)
        else:
            badge(ax,bx,y+0.12,'obs','obs',fs=6.8)
            badge(ax,bx+0.65,y+0.12,'faith','faith',fs=6.8)
    rounded(ax,(3.05,0.65),12.4,0.65,
            'Takeaway: graph quality is an upstream bottleneck - missing nodes or noisy links cap every downstream gain.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.8,'color':COL['dark']})
    save(fig,'F3_graph_methods_lineage')

# F4

def fig4():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F4. Retrieval methods along an adaptivity frontier',
          'Higher adaptivity increases bridge observability, but also raises noise, latency, and attribution cost.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # axes
    ax.add_line(Line2D([1.0,14.7],[1.1,1.1],color=COL['gray'],lw=1.0))
    ax.add_line(Line2D([1.0,1.0],[1.1,8.2],color=COL['gray'],lw=1.0))
    arrow(ax,(1.0,1.1),(14.9,1.1),color=COL['gray'],lw=1.0)
    arrow(ax,(1.0,1.1),(1.0,8.4),color=COL['gray'],lw=1.0)
    ax.text(14.85,0.65,'adaptivity / control',fontsize=8,color=COL['mid'],ha='right')
    ax.text(0.45,8.4,'chain observability',fontsize=8,color=COL['mid'],rotation=90,ha='center',va='top')
    # frontier curve
    pts=np.array([[1.7,2.0],[4.7,3.6],[8.0,5.2],[11.1,6.2],[14.1,6.9]])
    for i in range(len(pts)-1): arrow(ax,pts[i],pts[i+1],color=COL['obs'],lw=2.0,rad=0.02)
    # noise/cost shadow
    ax.add_patch(Polygon([[1.5,1.1],[14.6,1.1],[14.6,3.4],[11.0,2.7],[7.8,2.1],[4.5,1.55]],closed=True,
                         facecolor='#FFF4E8',edgecolor='none',alpha=0.9,zorder=0))
    ax.text(11.6,2.05,'noise + cost grow',fontsize=8,color=COL['exp'],ha='center')
    # method clusters
    clusters=[('single-shot\nproposal pool',2.5,2.25,['BM25','DPR','ColBERT','BGE'],['obs','obs','obs','obs']),
              ('iterative / interleaved\nbridge discovery',5.7,3.85,['MDR','Baleen','IRCoT','FLARE'],['obs','util','obs','util']),
              ('hierarchical / long-context\ngranularity shift',9.0,5.35,['RAPTOR','LongRAG','HyDE','HiQA'],['exp','exp','obs','exp']),
              ('agentic / RL search\npolicy learning',12.35,6.45,['Search-R1','DeepRAG','RAG-Gym','PAR-RAG'],['obs','obs','util','faith'])]
    for title_c,x,y,methods,ks in clusters:
        rounded(ax,(x-1.35,y-0.95),2.7,1.85,'',fc='white',ec=mcolors.to_rgba(COL['obs'],0.35),lw=1.0,r=0.17)
        ax.text(x,y+0.64,title_c,fontsize=7.5,fontweight='bold',ha='center',color=COL['dark'])
        for i,m in enumerate(methods):
            xx=x-1.05+(i%2)*1.1; yy=y+0.05-(i//2)*0.46
            method_pill(ax,xx,yy,0.95,m,key=ks[i],fs=6.4)
    # diagnostics strip
    rounded(ax,(1.15,8.05),13.7,0.62,
            'Report both sides of the tradeoff: pool support/path recall at Top-N  +  distractor ratio / calls / latency.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.7,'color':COL['dark']})
    save(fig,'F4_retrieval_adaptivity_frontier')

# F5

def fig5():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F5. Decomposition as variance reduction for utility and fusion',
          'A plan makes hidden bridge variables explicit, but bad intermediate states propagate.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # complex query to planner
    rounded(ax,(0.7,6.3),2.55,1.15,'complex query\n$q$',fc='#FBFCFE',ec=COL['edge'],r=0.18,text_kw={'fontsize':8.5})
    rounded(ax,(4.0,6.25),2.2,1.25,'planner /\ndecomposer',fc=mcolors.to_rgba(COL['util'],0.08),ec=COL['util'],r=0.18,text_kw={'fontsize':8.5,'color':COL['dark'],'fontweight':'bold'})
    arrow(ax,(3.27,6.88),(3.98,6.88),color=COL['util'],lw=2)
    # subquestions
    subx=[7.2,9.0,10.8,12.6]
    for i,x in enumerate(subx):
        rounded(ax,(x-0.65,6.55),1.3,0.78,fr'$q_{i+1}$',fc='white',ec=COL['util'],lw=1.0,r=0.16,text_kw={'fontsize':9,'color':COL['util'],'fontweight':'bold'})
        arrow(ax,(6.22,6.88),(x-0.68,6.88),color=COL['util'],lw=1.2,rad=0.06*(i-1.5))
    ax.text(10.0,7.55,'lower-variance retrieval targets',fontsize=7.8,color=COL['util'],ha='center')
    # retrieval/evidence units
    for i,x in enumerate(subx):
        rounded(ax,(x-0.72,4.65),1.44,0.75,fr'$e^\star_{i+1}$',fc=mcolors.to_rgba(COL['obs'],0.06),ec=COL['obs'],lw=1.0,r=0.16,text_kw={'fontsize':9,'color':COL['obs']})
        arrow(ax,(x,6.52),(x,5.42),color=COL['obs'],lw=1.4)
    rounded(ax,(7.05,2.65),6.3,1.05,'composer / reader\n$G(q,\pi(E_K))$',fc=mcolors.to_rgba(COL['fus'],0.07),ec=COL['fus'],lw=1.1,r=0.18,text_kw={'fontsize':8.8,'color':COL['dark'],'fontweight':'bold'})
    for x in subx:
        arrow(ax,(x,4.62),(9.8,3.72),color=COL['fus'],lw=1.1,rad=0.05*(x-9.8))
    rounded(ax,(8.95,1.28),2.45,0.75,'answer',fc='white',ec=COL['faith'],lw=1.1,r=0.16,text_kw={'fontsize':8.8,'color':COL['faith'],'fontweight':'bold'})
    arrow(ax,(10.2,2.63),(10.2,2.05),color=COL['faith'],lw=1.5)
    # method panels
    rounded(ax,(0.7,3.0),5.0,1.35,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(0.95,4.05,'Representative mechanisms',fontsize=8.3,fontweight='bold',color=COL['dark'])
    for i,m in enumerate(['DecompRC','Self-Ask','BREAK','Least-to-Most','PoT / PAL','Faithful CoT']):
        method_pill(ax,0.95+(i%3)*1.52,3.35-(i//3)*0.48,1.28,m,key=['util','util','util','fus','fus','faith'][i],fs=6.4)
    # error cascade
    rounded(ax,(0.7,1.1),5.0,1.35,'',fc='#FFF8F7',ec=mcolors.to_rgba(COL['faith'],0.35),lw=0.8,r=0.16)
    ax.text(0.95,2.13,'Cascading-error channel',fontsize=8.3,fontweight='bold',color=COL['dark'])
    ax.text(1.0,1.70,r'wrong $q_i$  $\rightarrow$ wrong retrieval  $\rightarrow$ biased fusion',fontsize=7.5,color=COL['mid'])
    # highlight actual estimands
    badge(ax,6.5,1.43,'util','utility',fs=7)
    badge(ax,7.55,1.43,'fus','fusion',fs=7)
    badge(ax,8.58,1.43,'faith','faithfulness',fs=7)
    ax.text(9.95,1.60,'Decomposition helps only when the plan is itself grounded.',fontsize=7.7,color=COL['mid'],ha='left')
    save(fig,'F5_decomposition_variance_reduction')

# F6

def fig6():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F6. LLM reasoning topologies as reader-fusion estimators',
          'The topology changes how evidence is composed, sampled, executed, or hidden.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # central reader
    rounded(ax,(6.35,4.1),3.3,1.25,'reader fusion\n$G(q,\pi(E_K))$',fc=mcolors.to_rgba(COL['fus'],0.08),ec=COL['fus'],lw=1.2,r=0.18,text_kw={'fontsize':9,'fontweight':'bold','color':COL['dark']})
    # topologies around
    blocks=[('Linear CoT','CoT, Zero-shot CoT\nAuto-CoT',1.0,6.65,'fus'),
            ('Diverse samples','Self-Consistency\nmajority over traces',5.15,6.9,'fus'),
            ('Branching search','Tree/Graph-of-Thought\nLATS, planning',10.15,6.65,'fus'),
            ('Executable reasoning','PoT, PAL\nFaithful CoT',1.0,2.0,'faith'),
            ('Latent reasoning','Quiet-STaR, Coconut\npause-token variants',10.15,2.0,'fus')]
    for head,body,x,y,k in blocks:
        rounded(ax,(x,y),4.0,1.15,'',fc='white',ec=mcolors.to_rgba(COL[k],0.55),lw=1.0,r=0.18)
        ax.text(x+0.25,y+0.82,head,fontsize=8.3,fontweight='bold',color=COL[k],ha='left')
        ax.text(x+0.25,y+0.37,body,fontsize=7.2,color=COL['mid'],ha='left',va='center')
        # arrows to center
        cx=x+2; cy=y+0.55
        arrow(ax,(cx,cy),(8.0,4.72),color=COL[k],lw=1.15,alpha=0.75,rad=0.08 if x<6 else -0.08)
    # mini topologies diagrams
    # linear chain
    for i in range(4):
        ax.add_patch(Circle((1.55+i*0.42,6.35),0.07,facecolor=COL['fus'],edgecolor='none'))
        if i>0: ax.add_line(Line2D([1.55+(i-1)*0.42,1.55+i*0.42],[6.35,6.35],color=COL['fus'],lw=1))
    # samples
    for j in range(3):
        ax.add_line(Line2D([6.0,7.0],[6.35+0.13*j,6.05+0.13*j],color=COL['fus'],lw=1.0))
    # branch
    ax.add_line(Line2D([11.0,11.45],[6.35,6.55],color=COL['fus'],lw=1)); ax.add_line(Line2D([11.0,11.45],[6.35,6.15],color=COL['fus'],lw=1))
    ax.add_patch(Circle((11.0,6.35),0.06,color=COL['fus'])); ax.add_patch(Circle((11.45,6.55),0.06,color=COL['fus'])); ax.add_patch(Circle((11.45,6.15),0.06,color=COL['fus']))
    # right eval strip
    rounded(ax,(5.85,1.05),4.25,1.28,'',fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(6.08,2.03,'Diagnostic split',fontsize=8.3,fontweight='bold',color=COL['dark'])
    ax.text(6.08,1.63,'Oracle-evidence EM/F1 -> fusion',fontsize=7.4,color=COL['fus'])
    ax.text(6.08,1.34,'Deletion/counterfactual -> faithfulness',fontsize=7.4,color=COL['faith'])
    save(fig,'F6_llm_reasoning_topologies')

# F7

def fig7():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F7. Agentic RAG as an MDP over evidence acquisition actions',
          'The policy moves bottlenecks around; diagnostics must attribute which estimand improved.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # loop components
    rounded(ax,(1.0,5.7),3.0,1.35,r'state $s_t$\n$(q,h_t,L_t,M_t)$',fc='#FFFFFF',ec=COL['edge'],lw=1.1,r=0.18,text_kw={'fontsize':9,'color':COL['dark']})
    rounded(ax,(6.15,5.72),3.3,1.32,r'policy $\pi(u_t|s_t)$\nLLM / planner / controller',fc=mcolors.to_rgba(COL['fus'],0.07),ec=COL['fus'],lw=1.1,r=0.18,text_kw={'fontsize':8.7,'color':COL['dark'],'fontweight':'bold'})
    rounded(ax,(11.6,5.72),3.1,1.32,'environment\nknowledge store $K$',fc=mcolors.to_rgba(COL['obs'],0.06),ec=COL['obs'],lw=1.1,r=0.18,text_kw={'fontsize':8.7,'color':COL['dark']})
    arrow(ax,(4.02,6.37),(6.12,6.37),color=COL['fus'],lw=1.6)
    arrow(ax,(9.48,6.37),(11.58,6.37),color=COL['obs'],lw=1.6)
    arrow(ax,(11.95,5.70),(3.25,5.68),color=COL['obs'],lw=1.2,rad=-0.35)
    ax.text(7.2,4.82,'transition: retrieved evidence, scratchpad, verifier output',fontsize=7.5,color=COL['mid'],ha='center')
    # action menu
    actions=[('rewrite query','obs'),('retrieve','obs'),('graph expand','obs'),('compress / select','util'),('reorder / pack','exp'),('verify','faith'),('final answer','fus')]
    rounded(ax,(2.0,2.2),12.0,2.2,'',fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.18)
    ax.text(2.25,4.05,'action space',fontsize=8.3,fontweight='bold',color=COL['dark'])
    for i,(a,k) in enumerate(actions):
        x=2.35+(i%4)*2.8; y=3.35-(i//4)*0.65
        method_pill(ax,x,y,2.15,a,key=k,fs=7.0)
    # reward equation
    rounded(ax,(0.92,0.67),14.5,0.95,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(1.2,1.18,r'$R_T=\mathbf{1}\{\hat a=a^\star\}-\lambda_c\sum_t cost(u_t)-\lambda_f\mathbf{1}\{\hat a\not\leftarrow C^\star\}$',fontsize=10.2,color=COL['dark'],ha='left',va='center')
    # attribution warning
    rounded(ax,(10.3,7.75),4.9,0.92,'accuracy gain is not enough:\nattribute gain by P/S/O/U/T',fc='#FFF8F7',ec=mcolors.to_rgba(COL['faith'],0.45),lw=0.9,r=0.16,text_kw={'fontsize':7.5,'color':COL['dark']})
    save(fig,'F7_agentic_rag_mdp')

# F8

def fig8():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F8. Faithfulness as causal evidence use',
          'A citation is not enough: the answer must respond to interventions on the support chain.')
    legend_estimands(ax, 9.1, 9.55, compact=True)
    # causal chain
    labels=[r'$W$',r'$K$',r'$C^\star$',r'$L_N$',r'$E_K$',r'$\pi(E_K)$',r'$\hat a$']
    sub=['world','store','support\nchain','pool','context','ordering','answer']
    xs=np.linspace(1.2,13.2,7); y=6.55
    for i,(x,l,s) in enumerate(zip(xs,labels,sub)):
        rounded(ax,(x-0.55,y-0.48),1.1,0.96,l+'\n'+s,fc='white',ec=COL['edge'],lw=1.0,r=0.15,text_kw={'fontsize':7.8})
        if i>0:
            arrow(ax,(xs[i-1]+0.57,y),(x-0.57,y),color=COL['mid'],lw=1.2)
    # parametric memory shortcut
    rounded(ax,(11.1,8.0),2.25,0.72,r'$\Theta$  parametric memory',fc='#FFF7EF',ec=COL['exp'],lw=1.0,r=0.14,text_kw={'fontsize':7.8,'color':COL['dark']})
    arrow(ax,(12.15,8.0),(13.15,7.07),color=COL['exp'],lw=1.3,ls='dashed',rad=-0.18)
    ax.text(13.42,7.55,'shortcut / leakage',fontsize=7.2,color=COL['exp'],ha='left')
    # interventions
    rounded(ax,(1.05,3.55),4.2,1.35,'Deletion test\nremove $e^\star_b$ and measure answer change',fc=mcolors.to_rgba(COL['faith'],0.07),ec=COL['faith'],lw=1.0,r=0.18,text_kw={'fontsize':8.2,'color':COL['dark']})
    rounded(ax,(6.05,3.55),4.45,1.35,'Counterfactual bridge\nswap bridge value; answer should shift',fc=mcolors.to_rgba(COL['faith'],0.07),ec=COL['faith'],lw=1.0,r=0.18,text_kw={'fontsize':8.2,'color':COL['dark']})
    rounded(ax,(11.25,3.55),3.45,1.35,'Citation audit\nnecessary but not sufficient',fc='#FAFBFD',ec='#E0E6EF',lw=0.9,r=0.18,text_kw={'fontsize':8.2,'color':COL['dark']})
    arrow(ax,(3.15,4.9),(3.75,6.05),color=COL['faith'],lw=1.1,rad=-0.1)
    arrow(ax,(8.2,4.9),(6.6,6.05),color=COL['faith'],lw=1.1,rad=0.05)
    # three signals table
    rounded(ax,(1.05,1.05),13.65,1.55,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.18)
    ax.text(1.3,2.15,'Separate three signals',fontsize=8.5,fontweight='bold',color=COL['dark'])
    cols=[('answer correct?',COL['fus']),('citation valid?',COL['util']),('causally used?',COL['faith'])]
    for i,(c,k) in enumerate(cols):
        x=4.1+i*3.25
        rounded(ax,(x,1.38),2.8,0.58,c,fc=mcolors.to_rgba(k,0.08),ec=k,lw=0.8,r=0.12,text_kw={'fontsize':7.6,'color':COL['dark'],'fontweight':'bold'})
    ax.text(1.3,1.55,'Faithfulness claim requires the third column, not just the first two.',fontsize=7.8,color=COL['mid'])
    save(fig,'F8_faithfulness_causal_use')

# F9

def fig9():
    fig, ax = setup((7.6,5.3), xlim=(0,16), ylim=(0,11))
    title(ax, 'F9. Benchmark-estimand alignment matrix',
          'Benchmarks are diagnostic instruments; they do not all test the same latent event.')
    # matrix
    rows=['Supporting-fact QA\nHotpotQA, 2Wiki, IIRC',
          'Shortcut-resistant QA\nMuSiQue, MoreHopQA',
          'Path / process QA\nEntailmentBank, eQASC',
          'Heterogeneous evidence\nHybridQA, MultiModalQA',
          'Long-context multi-hop\nLongBench, NovelHopQA',
          'Fact verification\nFEVER, HoVer, SciFact',
          'RAG-specific diagnostics\nFRAMES, MultiHop-RAG',
          'Counterfactual QA\nCofCA variants',
          'Agentic / tool-use\nToolBench, WebArena']
    cols=[('obs','Observability'),('util','Selection\nutility'),('exp','Exposure'),('fus','Fusion'),('faith','Faithfulness')]
    M=np.array([
        [3,2,1,1,1],
        [3,2,1,1,1],
        [1,2,1,3,2],
        [1,2,1,3,1],
        [1,1,3,2,1],
        [1,1,1,2,3],
        [2,2,2,2,2],
        [1,1,1,2,3],
        [2,2,1,2,2],
    ])
    x0,y0=4.35,1.0
    cw,ch=2.15,0.82
    # column headers
    for j,(k,c) in enumerate(cols):
        x=x0+j*cw
        rounded(ax,(x,y0+len(rows)*ch+0.25),cw-0.08,0.7,c,fc=mcolors.to_rgba(COL[k],0.12),ec=COL[k],lw=0.9,r=0.12,text_kw={'fontsize':7.5,'color':COL['dark'],'fontweight':'bold'})
    # cells
    for i,row in enumerate(rows):
        y=y0+(len(rows)-1-i)*ch
        ax.text(0.45,y+ch/2,row,fontsize=7.2,color=COL['dark'],ha='left',va='center')
        for j,(k,c) in enumerate(cols):
            v=M[i,j]
            alpha=[0.04,0.14,0.32,0.58][v]
            fc=mcolors.to_rgba(COL[k],alpha)
            ec=mcolors.to_rgba(COL[k],0.45 if v>=2 else 0.20)
            ax.add_patch(Rectangle((x0+j*cw,y),cw-0.08,ch-0.06,facecolor=fc,edgecolor=ec,linewidth=0.55))
            txt={0:'',1:'low',2:'med',3:'high'}[v]
            ax.text(x0+j*cw+(cw-0.08)/2,y+(ch-0.06)/2,txt,fontsize=7.0,color=COL['dark'],ha='center',va='center')
    # grid frame
    rounded(ax,(x0-0.12,y0-0.10),len(cols)*cw+0.05,len(rows)*ch+1.05,'',fc='none',ec='#DDE5EF',lw=0.8,r=0.10)
    # note
    rounded(ax,(0.45,0.22),14.95,0.5,'Strong empirical coverage should include at least one observability/shortcut benchmark and one faithfulness or counterfactual diagnostic.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.5,'color':COL['dark']})
    save(fig,'F9_benchmark_estimand_alignment')

# F10

def fig10():
    fig, ax = setup((7.6,4.9), xlim=(0,16), ylim=(0,10.5))
    title(ax, 'F10. Running example: bridge-dependent evidence chain',
          'Relation labels make the chain dependency auditable rather than a decorative pipeline.')
    legend_estimands(ax, 9.0, 9.95, compact=True)
    # question
    rounded(ax,(0.65,8.35),14.7,0.8,'Question: Which scientist discovered the chemical element named after the country where the author of Cien años de soledad was born?',
            fc='#FAFBFD',ec='#DDE5EF',lw=0.9,r=0.14,text_kw={'fontsize':7.6,'color':COL['dark']})
    # latent chain nodes
    y=6.35
    nodes=[('Cien años\nde soledad',1.25,'q'),('Gabriel García\nMárquez',4.05,'author'),('Colombia',6.85,'bridge'),('columbium /\nniobium',9.65,'element'),('Charles\nHatchett',12.55,'answer')]
    for idx,(lab,x,kind) in enumerate(nodes):
        color=[COL['mid'],COL['obs'],COL['obs'],COL['util'],COL['faith']][idx]
        rounded(ax,(x-0.78,y-0.45),1.56,0.9,lab,fc='white',ec=color,lw=1.15,r=0.15,text_kw={'fontsize':7.7,'color':COL['dark']})
    rels=['author of','born in','named after\n(historical name)','discovered by']
    for i,rel in enumerate(rels):
        x1=nodes[i][1]+0.82; x2=nodes[i+1][1]-0.82
        arrow(ax,(x1,y),(x2,y),color=COL['dark'] if i<2 else COL['util'] if i==2 else COL['faith'],lw=1.5)
        ax.text((x1+x2)/2,y+0.55,rel,fontsize=7.0,color=COL['mid'],ha='center')
    # hidden vs surface visibility band
    rounded(ax,(0.65,4.35),14.7,1.0,'',fc=COL['latent'],ec='#DDE5EF',lw=0.8,r=0.14,ls='dashed')
    ax.text(0.95,5.05,'surface-visible from original query',fontsize=7.3,color=COL['mid'],ha='left')
    ax.text(0.95,4.62,'bridge-dependent after intermediate resolution',fontsize=7.3,color=COL['mid'],ha='left')
    ax.add_patch(Rectangle((3.75,4.55),2.05,0.25,facecolor=mcolors.to_rgba(COL['obs'],0.25),edgecolor='none'))
    ax.add_patch(Rectangle((6.45,4.55),6.95,0.25,facecolor=mcolors.to_rgba(COL['util'],0.25),edgecolor='none'))
    ax.text(4.78,4.2,'retriever can find this first',fontsize=7.0,color=COL['obs'],ha='center')
    ax.text(9.9,4.2,'later evidence becomes queryable only after the bridge is resolved',fontsize=7.0,color=COL['util'],ha='center')
    # observable pool / selected context
    rounded(ax,(0.65,1.0),14.7,2.35,'',fc='#FFFFFF',ec='#DDE5EF',lw=0.9,r=0.15)
    ax.text(0.95,2.98,'Observable trace',fontsize=8.3,fontweight='bold',color=COL['dark'])
    # pool items
    pool=[('bio: García Márquez',COL['obs'],'kept'),('Colombian geography\ndistractor',COL['gray'],'drop'),('element: columbium\n= niobium',COL['util'],'bridge'),('discovery: Hatchett',COL['faith'],'answer')]
    px=[2.25,5.35,8.65,12.0]
    for (lab,c,tag),x in zip(pool,px):
        rounded(ax,(x-1.0,1.55),2.0,0.8,lab,fc=mcolors.to_rgba(c,0.06) if c!=COL['gray'] else '#F7F7F7',ec=c,lw=1.0,r=0.13,text_kw={'fontsize':7.0,'color':COL['dark']})
        ax.text(x,1.32,tag,fontsize=6.8,color=c,ha='center',fontweight='bold')
    arrow(ax,(3.25,1.95),(4.35,1.95),color=COL['gray'],lw=0.8)
    arrow(ax,(6.35,1.95),(7.65,1.95),color=COL['util'],lw=1.2)
    arrow(ax,(9.65,1.95),(11.0,1.95),color=COL['faith'],lw=1.2)
    # failure callouts
    rounded(ax,(13.5,5.75),1.8,0.75,'answer',fc=mcolors.to_rgba(COL['faith'],0.08),ec=COL['faith'],lw=0.9,r=0.14,text_kw={'fontsize':8,'color':COL['faith'],'fontweight':'bold'})
    arrow(ax,(13.18,6.35),(13.45,6.12),color=COL['faith'],lw=1.0)
    rounded(ax,(0.65,0.25),14.7,0.5,'Key reviewer check: every arrow carries a bridge relation; remove any middle relation and the answer is no longer identifiable.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.5,'color':COL['dark']})
    save(fig,'F10_running_example_chain')



# --- final pass overrides: cleaner ACM-ready layouts ---
def title(ax, main, subtitle=None):
    ax.text(0.25, 9.68, main, fontsize=10.8, fontweight='bold', color=COL['dark'], ha='left', va='top')
    if subtitle:
        ax.text(0.25, 9.20, subtitle, fontsize=7.8, color=COL['mid'], ha='left', va='top')

def legend_estimands(ax, *args, **kwargs):
    # Legends are encoded through column headers / badges to avoid title collisions in ACM-width figures.
    return None

def mini_legend(ax, x, y):
    gap=1.28
    for i,(k,lbl) in enumerate(EST):
        ax.add_patch(Circle((x+i*gap,y),0.07,color=COL[k],zorder=10))
        ax.text(x+i*gap+0.12,y,lbl,fontsize=6.7,color=COL['mid'],va='center')

def fig1():
    fig, ax = setup((7.5,4.5))
    title(ax, 'F1. Latent evidence-chain inference view',
          'Observable RAG objects are noisy projections of an unobserved support chain.')
    # legend strip
    mini_legend(ax, 8.45, 9.05)
    rounded(ax,(0.30,5.95),15.4,2.45,'',fc=COL['latent'],ec='#D6DEE8',lw=1.0,r=0.15,ls='dashed',z=0)
    rounded(ax,(0.30,1.30),15.4,3.45,'',fc='white',ec='#D6DEE8',lw=1.0,r=0.15,z=0)
    ax.text(0.55,8.12,'latent target',fontsize=8.6,color=COL['mid'],fontweight='bold')
    ax.text(0.55,4.48,'observable trace',fontsize=8.6,color=COL['mid'],fontweight='bold')
    xs=[2.0,4.9,7.8,10.7]
    labs=['$e^\\star_1$\nbiography','$e^\\star_2$\nbridge','$e^\\star_3$\nidentity','$e^\\star_4$\nanswer unit']
    for i,x in enumerate(xs):
        rounded(ax,(x-0.62,6.75),1.24,0.72,labs[i],fc='white',ec=COL['gray'],lw=1.15,r=0.16,ls='dashed',text_kw={'fontsize':7.6})
        if i>0:
            arrow(ax,(xs[i-1]+0.64,7.11),(x-0.64,7.11),color=COL['gray'],lw=1.35,ls='dashed')
    ax.text(12.15,7.08,'$C^\\star=(e^\\star_1,\\ldots,e^\\star_m)$',fontsize=9.8,color=COL['dark'],va='center')
    # observable modules
    modules=[('q\nquestion',0.95,3.18,1.18,0.72),('$L_N$\npool',3.05,3.02,1.45,0.95),('$E_K$\ncontext',5.75,3.02,1.55,0.95),('$\\pi(E_K)$\nordering',8.55,3.02,1.65,0.95),('$\\hat a$\nanswer',11.55,3.02,1.55,0.95)]
    for label,x,y,w,h in modules:
        rounded(ax,(x,y),w,h,label,fc='white',ec=COL['edge'],lw=1.15,r=0.16,text_kw={'fontsize':8.0})
    flow=[((2.14,3.55),(3.02,3.55),'obs','$R_N$'),((4.52,3.55),(5.72,3.55),'util','$S_K$'),((7.33,3.55),(8.52,3.55),'exp','order'),((10.22,3.55),(11.52,3.55),'fus','$G$')]
    for p1,p2,k,lab in flow:
        arrow(ax,p1,p2,color=COL[k],lw=1.8)
        ax.text((p1[0]+p2[0])/2,3.88,lab,fontsize=7.8,color=COL[k],ha='center',fontweight='bold')
    # vertical colored diagnostics
    proj=[(3.75,6.74,4.00,'obs','pool contains chain'),(6.52,6.74,4.00,'util','budget preserves chain'),(9.38,6.74,4.00,'exp','reader can access'),(12.32,6.74,4.00,'faith','answer uses chain')]
    for x,y1,y2,k,txt in proj:
        arrow(ax,(x,y1),(x,y2),color=COL[k],lw=1.2,ls='dotted',style='-|>',mutation_scale=10)
        badge(ax,x-0.50,y2-0.55,k,k,fs=6.7)
        ax.text(x+0.10,y2-0.40,txt,fontsize=6.8,color=COL['mid'],ha='left')
    # failure notes
    notes=[('absence\nmissing bridge',2.5,'obs'),('selection bias\nunder K',5.55,'util'),('lost-in-middle\n/ diffusion',8.65,'exp'),('post-hoc\nrationalization',11.85,'faith')]
    for text,x,k in notes:
        rounded(ax,(x-0.85,1.78),1.7,0.66,text,fc=mcolors.to_rgba(COL[k],0.10),ec=mcolors.to_rgba(COL[k],0.45),lw=0.8,r=0.11,text_kw={'fontsize':6.9,'color':COL['dark']})
    rounded(ax,(0.55,0.28),14.85,0.55,
            '$P(\\hat a=a^\\star) \\approx P(P)P(S|P)P(O|S)P(U|O)P(T|U)$',fc='#FBFCFE',ec='#E5EAF2',lw=0.8,r=0.12,
            text_kw={'fontsize':9.0,'color':COL['dark']})
    save(fig,'F1_latent_chain_pipeline')

def fig2():
    fig, ax = setup((7.5,4.45))
    title(ax, 'F2. Bottleneck coupling among estimands',
          'A single weak factor caps end-to-end success even when other modules are strong.')
    theta=[0.82,0.67,0.74,0.51,0.63]
    keys=['obs','util','exp','fus','faith']
    names=['pool\nobservability','conditional\nutility','reader\nexposure','fusion\nreliability','causal\nfaithfulness']
    xs=np.linspace(1.75,12.5,5)
    prod=1.0
    prev=(0.72,7.25)
    ax.text(0.65,7.55,'start\n1.00',fontsize=7.7,color=COL['mid'],ha='center')
    for i,(x,t,k,nm) in enumerate(zip(xs,theta,keys,names)):
        rounded(ax,(x-0.52,3.28),1.04,2.85,'',fc='#FFFFFF',ec='#D8E0EA',lw=0.9,r=0.12)
        h=2.60*t
        ax.add_patch(FancyBboxPatch((x-0.36,3.40),0.72,h,boxstyle='round,pad=0.02,rounding_size=0.09',
                                    facecolor=mcolors.to_rgba(COL[k],0.72),edgecolor=COL[k],linewidth=0.8,zorder=3))
        ax.text(x,6.48,rf'$\theta_{{{k}}}$',fontsize=9.6,ha='center',color=COL[k],fontweight='bold')
        ax.text(x,3.10,f'{t:.2f}',fontsize=8.8,ha='center',color=COL['dark'],fontweight='bold')
        ax.text(x,2.40,nm,fontsize=7.1,ha='center',color=COL['mid'])
        prod*=t
        y_cur=7.25-3.95*(1-prod)
        arrow(ax,prev,(x-0.55,y_cur),color=COL[k],lw=1.5,alpha=0.95,rad=0.02)
        ax.add_patch(Circle((x-0.58,y_cur),0.055,color=COL[k],zorder=6))
        ax.text(x-0.42,y_cur+0.22,f'{prod:.2f}',fontsize=6.9,color=COL['mid'])
        prev=(x+0.55,y_cur)
    arrow(ax,prev,(14.0,7.25-3.95*(1-prod)),color=COL['dark'],lw=1.4)
    rounded(ax,(14.1,4.55),1.25,0.85,f'final\n{prod:.2f}',fc='#FBFCFE',ec=COL['dark'],lw=1.0,r=0.15,text_kw={'fontsize':8.5,'fontweight':'bold'})
    # fusion highlight
    rounded(ax,(xs[3]-0.70,2.15),1.40,4.62,'',fc='none',ec=COL['fus'],lw=1.1,r=0.15,ls='dashed',z=0)
    ax.text(xs[3],1.86,'visible bottleneck',fontsize=7.2,color=COL['fus'],ha='center',fontweight='bold')
    # theorem strip - separated cells
    rounded(ax,(0.62,0.45),14.85,0.92,'',fc='#FAFBFD',ec='#DDE5EF',lw=0.9,r=0.16)
    ax.text(0.92,1.06,'Theorem 1',fontsize=8.2,fontweight='bold',color=COL['dark'])
    ax.text(4.9,0.90,'$P(\\hat a=a^\\star) \\leq \\min_i\\theta_i$',fontsize=10.0,color=COL['dark'],ha='center',va='center')
    ax.text(10.9,0.90,'$\\partial P / \\partial\\theta_i \\leq \\prod_{j\\ne i}\\theta_j$',fontsize=10.0,color=COL['dark'],ha='center',va='center')
    save(fig,'F2_estimand_bottleneck_flow')

def fig5():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F5. Decomposition as utility and fusion control',
          'A plan exposes bridge variables, but intermediate errors propagate downstream.')
    # top flow
    rounded(ax,(0.70,6.45),2.20,1.00,'complex query\n$q$',fc='#FBFCFE',ec=COL['edge'],r=0.18,text_kw={'fontsize':8.2})
    rounded(ax,(3.55,6.38),2.05,1.14,'planner /\ndecomposer',fc='#EAF6EF',ec=COL['util'],r=0.18,text_kw={'fontsize':8.2,'color':COL['dark'],'fontweight':'bold'})
    arrow(ax,(2.92,6.95),(3.52,6.95),color=COL['util'],lw=1.8)
    subx=[6.95,8.65,10.35,12.05]
    for i,x in enumerate(subx):
        rounded(ax,(x-0.52,6.55),1.04,0.68,fr'$q_{i+1}$',fc='white',ec=COL['util'],lw=1.0,r=0.14,text_kw={'fontsize':8.7,'color':COL['util'],'fontweight':'bold'})
        arrow(ax,(5.62,6.95),(x-0.55,6.90),color=COL['util'],lw=1.1,rad=0.05*(i-1.5))
    ax.text(9.55,7.55,'sub-questions reduce utility-estimation variance',fontsize=7.2,color=COL['util'],ha='center')
    for i,x in enumerate(subx):
        rounded(ax,(x-0.55,4.70),1.10,0.65,fr'$e^\star_{i+1}$',fc='#EEF4FF',ec=COL['obs'],lw=1.0,r=0.14,text_kw={'fontsize':8.5,'color':COL['obs'],'fontweight':'bold'})
        arrow(ax,(x,6.53),(x,5.38),color=COL['obs'],lw=1.35)
    rounded(ax,(6.55,2.85),6.05,0.95,'composer / reader\n$G(q,\\pi(E_K))$',fc='#F0ECFF',ec=COL['fus'],lw=1.1,r=0.18,text_kw={'fontsize':8.4,'color':COL['dark'],'fontweight':'bold'})
    for x in subx:
        arrow(ax,(x,4.66),(9.55,3.82),color=COL['fus'],lw=1.0,rad=0.05*(x-9.55))
    rounded(ax,(8.45,1.55),2.20,0.68,'answer',fc='#FFF4F4',ec=COL['faith'],lw=1.0,r=0.14,text_kw={'fontsize':8.2,'color':COL['faith'],'fontweight':'bold'})
    arrow(ax,(9.55,2.85),(9.55,2.25),color=COL['faith'],lw=1.4)
    # left panels
    rounded(ax,(0.70,3.25),4.95,1.25,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(0.95,4.20,'Mechanism families',fontsize=8.2,fontweight='bold',color=COL['dark'])
    for i,m in enumerate(['DecompRC','Self-Ask','BREAK','Least-to-Most','PoT / PAL','Faithful CoT']):
        method_pill(ax,0.95+(i%3)*1.52,3.55-(i//3)*0.43,1.28,m,key=['util','util','util','fus','fus','faith'][i],fs=6.4)
    rounded(ax,(0.70,1.30),4.95,1.25,'',fc='#FFF8F7',ec=mcolors.to_rgba(COL['faith'],0.50),lw=0.8,r=0.16)
    ax.text(0.95,2.25,'Cascading-error channel',fontsize=8.2,fontweight='bold',color=COL['dark'])
    ax.text(0.95,1.78,'wrong sub-question -> wrong retrieval -> biased fusion',fontsize=7.2,color=COL['mid'])
    rounded(ax,(6.30,0.62),7.25,0.60,'Evaluation should report both plan accuracy and oracle-evidence fusion, not answer F1 alone.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.4,'color':COL['dark']})
    save(fig,'F5_decomposition_variance_reduction')

def fig7():
    fig, ax = setup((7.5,4.8))
    title(ax, 'F7. Agentic RAG as controlled evidence acquisition',
          'Policy learning changes when and how latent-chain evidence becomes observable.')
    rounded(ax,(1.0,5.85),3.0,1.20,'state $s_t$\n$q, h_t, L_t, M_t$',fc='#FFFFFF',ec=COL['edge'],lw=1.1,r=0.18,text_kw={'fontsize':8.4,'color':COL['dark']})
    rounded(ax,(6.15,5.85),3.3,1.20,'policy $\\pi(u_t|s_t)$\nLLM / planner',fc='#F0ECFF',ec=COL['fus'],lw=1.1,r=0.18,text_kw={'fontsize':8.3,'color':COL['dark'],'fontweight':'bold'})
    rounded(ax,(11.5,5.85),3.25,1.20,'environment\nknowledge store $K$',fc='#EEF4FF',ec=COL['obs'],lw=1.1,r=0.18,text_kw={'fontsize':8.3,'color':COL['dark']})
    arrow(ax,(4.04,6.45),(6.12,6.45),color=COL['fus'],lw=1.5)
    arrow(ax,(9.48,6.45),(11.48,6.45),color=COL['obs'],lw=1.5)
    arrow(ax,(12.05,5.84),(3.25,5.82),color=COL['obs'],lw=1.2,rad=-0.35)
    ax.text(7.40,4.95,'transition returns retrieved evidence, verifier output, and updated scratchpad',fontsize=7.3,color=COL['mid'],ha='center')
    # action panel
    rounded(ax,(1.80,2.30),12.55,2.10,'',fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.18)
    ax.text(2.10,4.08,'action space',fontsize=8.2,fontweight='bold',color=COL['dark'])
    actions=[('rewrite query','obs'),('retrieve','obs'),('graph expand','obs'),('compress / select','util'),('reorder / pack','exp'),('verify','faith'),('final answer','fus')]
    for i,(a,k) in enumerate(actions):
        x=2.20+(i%4)*2.85; y=3.36-(i//4)*0.63
        method_pill(ax,x,y,2.18,a,key=k,fs=6.9)
    rounded(ax,(10.35,7.60),4.75,0.88,'Accuracy gain is unattributed unless\nyou report P/S/O/U/T diagnostics.',fc='#FFF8F7',ec=COL['faith'],lw=0.9,r=0.16,text_kw={'fontsize':7.5,'color':COL['dark']})
    rounded(ax,(0.92,0.70),14.5,0.90,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(1.2,1.15,'$R_T=\\mathbf{1}\{\\hat a=a^\\star\}-\\lambda_c\\sum_t cost(u_t)-\\lambda_f\\mathbf{1}\{\\hat a\\not\\leftarrow C^\\star\}$',fontsize=9.0,color=COL['dark'],ha='left',va='center')
    save(fig,'F7_agentic_rag_mdp')

def fig8():
    fig, ax = setup((7.5,4.9), xlim=(0,16), ylim=(0,10.2))
    title(ax, 'F8. Faithfulness as causal evidence use',
          'The answer must respond to interventions on the support chain, not merely cite it.')
    labels=[('$W$','world'),('$K$','store'),('$C^\\star$','chain'),('$L_N$','pool'),('$E_K$','context'),('$\\pi(E_K)$','ordering'),('$\\hat a$','answer')]
    xs=np.linspace(1.2,13.4,7); y=6.45
    for i,(l,sb) in enumerate(labels):
        x=xs[i]
        rounded(ax,(x-0.52,y-0.42),1.04,0.84,l+'\n'+sb,fc='white',ec=COL['edge'],lw=1.0,r=0.14,text_kw={'fontsize':7.5})
        if i>0:
            arrow(ax,(xs[i-1]+0.55,y),(x-0.55,y),color=COL['mid'],lw=1.1)
    # memory shortcut
    rounded(ax,(10.65,8.15),2.6,0.62,'$\\Theta$ parametric memory',fc='#FFF7EF',ec=COL['exp'],lw=1.0,r=0.14,text_kw={'fontsize':7.7,'color':COL['dark']})
    arrow(ax,(12.0,8.14),(13.25,6.90),color=COL['exp'],lw=1.2,ls='dashed',rad=-0.12)
    ax.text(13.45,7.40,'shortcut / leakage',fontsize=7.0,color=COL['exp'],ha='left')
    # intervention cards separate
    cards=[('Deletion test','remove a support unit;\nanswer should change',1.0,3.6),
           ('Counterfactual bridge','swap bridge value;\nanswer should shift',5.6,3.6),
           ('Citation audit','check entailment;\nnecessary, not sufficient',10.5,3.6)]
    for i,(h,b,x0,y0) in enumerate(cards):
        ec=COL['faith'] if i<2 else '#D9E1EC'; fc='#FFF8F7' if i<2 else '#FAFBFD'
        rounded(ax,(x0,y0),3.8,1.15,'',fc=fc,ec=ec,lw=0.9,r=0.16)
        ax.text(x0+0.20,y0+0.78,h,fontsize=8.1,fontweight='bold',color=COL['dark'],ha='left')
        ax.text(x0+0.20,y0+0.35,b,fontsize=7.3,color=COL['mid'],ha='left',va='center')
    arrow(ax,(2.9,4.75),(3.4,6.02),color=COL['faith'],lw=1.0,rad=-0.12)
    arrow(ax,(7.5,4.75),(6.5,6.02),color=COL['faith'],lw=1.0,rad=0.10)
    # three signals
    rounded(ax,(1.0,1.05),14.0,1.35,'',fc='#FFFFFF',ec='#E0E6EF',lw=0.8,r=0.16)
    ax.text(1.25,2.02,'Separate three signals',fontsize=8.4,fontweight='bold',color=COL['dark'])
    for i,(txt,k) in enumerate([('Correct?', 'fus'),('Citation valid?', 'util'),('Causal use?', 'faith')]):
        rounded(ax,(5.45+i*3.05,1.38),2.40,0.55,txt,fc=mcolors.to_rgba(COL[k],0.12),ec=COL[k],lw=0.8,r=0.12,text_kw={'fontsize':6.9,'color':COL['dark'],'fontweight':'bold'})
    save(fig,'F8_faithfulness_causal_use')



# --- second final pass for F1 and F10 ---
def fig1():
    fig, ax = setup((7.5,4.5))
    title(ax, 'F1. Latent evidence-chain inference view',
          'Observable RAG objects are noisy projections of an unobserved support chain.')
    # latent/observable layers
    rounded(ax,(0.30,5.80),15.4,2.55,'',fc=COL['latent'],ec='#D6DEE8',lw=1.0,r=0.15,ls='dashed',z=0)
    rounded(ax,(0.30,1.25),15.4,3.55,'',fc='white',ec='#D6DEE8',lw=1.0,r=0.15,z=0)
    ax.text(0.55,8.10,'latent target',fontsize=8.5,color=COL['mid'],fontweight='bold')
    ax.text(0.55,4.48,'observable trace',fontsize=8.5,color=COL['mid'],fontweight='bold')
    # estimand legend inside latent layer, not title
    xleg=10.25; yleg=8.08
    for i,(k,lbl) in enumerate([('obs','obs'),('util','util'),('exp','exp'),('fus','fus'),('faith','faith')]):
        ax.add_patch(Circle((xleg+i*0.84,yleg),0.055,color=COL[k],zorder=4))
        ax.text(xleg+i*0.84+0.09,yleg,lbl,fontsize=6.4,color=COL['mid'],va='center')
    # latent chain nodes
    xs=[1.85,4.65,7.45,10.25]
    labs=['$e^\\star_1$\nbiography','$e^\\star_2$\nbridge','$e^\\star_3$\nidentity','$e^\\star_4$\nanswer']
    for i,x in enumerate(xs):
        rounded(ax,(x-0.58,6.67),1.16,0.74,labs[i],fc='white',ec=COL['gray'],lw=1.1,r=0.16,ls='dashed',text_kw={'fontsize':7.3})
        if i>0:
            arrow(ax,(xs[i-1]+0.60,7.04),(x-0.60,7.04),color=COL['gray'],lw=1.3,ls='dashed')
    ax.text(12.0,7.02,'$C^\\star=(e^\\star_1,\\ldots,e^\\star_m)$',fontsize=9.2,color=COL['dark'],va='center')
    # projection arrows with labels on top of observable layer
    proj=[(3.50,'obs','$\\theta_{obs}$','pool'),(6.25,'util','$\\theta_{util}$','budget'),(9.10,'exp','$\\theta_{exp}$','ordering'),(12.05,'faith','$\\theta_{faith}$','causal use')]
    for x,k,t,lab in proj:
        arrow(ax,(x,6.66),(x,4.58),color=COL[k],lw=1.15,ls='dotted',style='-|>',mutation_scale=9)
        ax.text(x,4.30,t+'  '+lab,fontsize=6.9,color=COL[k],ha='center',fontweight='bold')
    # observable pipeline modules
    modules=[('q\nquestion',0.95,3.12,1.08,0.70),('$L_N$\npool',3.00,3.02,1.32,0.86),('$E_K$\ncontext',5.75,3.02,1.42,0.86),('$\\pi(E_K)$\nordering',8.60,3.02,1.52,0.86),('$\\hat a$\nanswer',11.65,3.02,1.42,0.86)]
    for label,x,y,w,h in modules:
        rounded(ax,(x,y),w,h,label,fc='white',ec=COL['edge'],lw=1.15,r=0.16,text_kw={'fontsize':7.8})
    flow=[((2.05,3.47),(2.98,3.47),'obs','$R_N$'),((4.35,3.47),(5.72,3.47),'util','$S_K$'),((7.20,3.47),(8.57,3.47),'exp','order'),((10.15,3.47),(11.62,3.47),'fus','$G$')]
    for p1,p2,k,lab in flow:
        arrow(ax,p1,p2,color=COL[k],lw=1.7)
        ax.text((p1[0]+p2[0])/2,3.78,lab,fontsize=7.2,color=COL[k],ha='center',fontweight='bold')
    notes=[('absence\nmissing bridge',2.1,'obs'),('selection bias\nunder K',5.1,'util'),('lost-in-middle\n/ diffusion',8.35,'exp'),('post-hoc\nrationalization',11.65,'faith')]
    for text,x,k in notes:
        rounded(ax,(x-0.80,1.74),1.60,0.64,text,fc=mcolors.to_rgba(COL[k],0.10),ec=mcolors.to_rgba(COL[k],0.45),lw=0.8,r=0.11,text_kw={'fontsize':6.7,'color':COL['dark']})
    rounded(ax,(0.55,0.28),14.85,0.55,
            '$P(\\hat a=a^\\star) \\approx P(P)P(S|P)P(O|S)P(U|O)P(T|U)$',fc='#FBFCFE',ec='#E5EAF2',lw=0.8,r=0.12,
            text_kw={'fontsize':8.8,'color':COL['dark']})
    save(fig,'F1_latent_chain_pipeline')

def fig10():
    fig, ax = setup((7.6,4.9), xlim=(0,16), ylim=(0,10.5))
    title(ax, 'F10. Running example: bridge-dependent evidence chain',
          'Every arrow carries a bridge relation; remove a middle relation and the answer is not identifiable.')
    # question card with wrapped text
    qtext='Which scientist discovered the chemical element named after the country\nwhere the author of Cien años de soledad was born?'
    rounded(ax,(1.05,7.95),13.9,0.95,'Question:  '+qtext,fc='#FAFBFD',ec='#DDE5EF',lw=0.9,r=0.14,text_kw={'fontsize':7.4,'color':COL['dark']})
    # chain
    y=6.28
    nodes=[('Cien años\nde soledad',1.40,COL['mid']),('Gabriel García\nMárquez',4.00,COL['obs']),('Colombia',6.55,COL['obs']),('columbium /\nniobium',9.25,COL['util']),('Charles\nHatchett',12.25,COL['faith'])]
    for lab,x,c in nodes:
        rounded(ax,(x-0.70,y-0.43),1.40,0.86,lab,fc='white',ec=c,lw=1.15,r=0.14,text_kw={'fontsize':7.3,'color':COL['dark']})
    rels=[('author of',2.10,3.30,COL['dark']),('born in',4.70,5.85,COL['dark']),('named after\n(historical name)',7.25,8.55,COL['util']),('discovered by',9.95,11.55,COL['faith'])]
    for rel,x1,x2,c in rels:
        arrow(ax,(x1,y),(x2,y),color=c,lw=1.45)
        ax.text((x1+x2)/2,y+0.50,rel,fontsize=6.9,color=COL['mid'],ha='center')
    rounded(ax,(13.20,5.87),1.45,0.80,'answer',fc='#FFF4F4',ec=COL['faith'],lw=1.0,r=0.13,text_kw={'fontsize':7.3,'color':COL['faith'],'fontweight':'bold'})
    arrow(ax,(12.98,y),(13.18,6.28),color=COL['faith'],lw=1.0)
    # visible/hidden strip
    rounded(ax,(1.05,4.35),13.9,1.05,'',fc=COL['latent'],ec='#DDE5EF',lw=0.8,r=0.14,ls='dashed')
    ax.text(1.35,5.07,'surface-visible from original query',fontsize=7.2,color=COL['mid'],ha='left')
    ax.text(1.35,4.66,'bridge-dependent after intermediate resolution',fontsize=7.2,color=COL['mid'],ha='left')
    ax.add_patch(Rectangle((3.75,4.55),1.80,0.20,facecolor=mcolors.to_rgba(COL['obs'],0.20),edgecolor='none'))
    ax.add_patch(Rectangle((6.05,4.55),6.65,0.20,facecolor=mcolors.to_rgba(COL['util'],0.22),edgecolor='none'))
    ax.text(9.35,4.16,'later evidence becomes queryable only after the bridge is resolved',fontsize=6.9,color=COL['util'],ha='center')
    # observable trace
    rounded(ax,(1.05,1.10),13.9,2.35,'',fc='#FFFFFF',ec='#DDE5EF',lw=0.9,r=0.15)
    ax.text(1.35,3.10,'Observable trace',fontsize=8.0,fontweight='bold',color=COL['dark'])
    pool=[('bio: García Márquez',COL['obs'],'kept'),('Colombian geography\ndistractor',COL['gray'],'drop'),('element: columbium\n= niobium',COL['util'],'bridge'),('discovery: Hatchett',COL['faith'],'answer')]
    px=[2.45,5.50,8.75,12.0]
    for (lab,c,tag),x in zip(pool,px):
        fill={'kept':'#EEF4FF','drop':'#F7F7F7','bridge':'#EAF6EF','answer':'#FFF4F4'}[tag]
        rounded(ax,(x-0.92,1.72),1.84,0.78,lab,fc=fill,ec=c,lw=1.0,r=0.13,text_kw={'fontsize':6.9,'color':COL['dark']})
        ax.text(x,1.45,tag,fontsize=6.8,color=c,ha='center',fontweight='bold')
    arrow(ax,(3.38,2.10),(4.55,2.10),color=COL['gray'],lw=0.9)
    arrow(ax,(6.43,2.10),(7.78,2.10),color=COL['util'],lw=1.1)
    arrow(ax,(9.68,2.10),(11.04,2.10),color=COL['faith'],lw=1.1)
    rounded(ax,(1.05,0.30),13.9,0.47,'This example visualizes the latent chain C* versus the retrieved pool, selected context, and answer-bearing evidence.',
            fc='#FAFBFD',ec='#E0E6EF',lw=0.8,r=0.12,text_kw={'fontsize':7.0,'color':COL['dark']})
    save(fig,'F10_running_example_chain')

if __name__ == '__main__':
    for fn in [fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10]:
        fn()
    print('Generated figures in', OUT)
