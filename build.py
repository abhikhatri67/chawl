import json
SITE="https://chawl.in"
ICON={
'prod':'<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 22V12M3 7l9 5 9-5"/>',
'soft':'<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
'hw':'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
'iot':'<circle cx="12" cy="12" r="2"/><path d="M7.8 7.8a6 6 0 000 8.4M16.2 7.8a6 6 0 010 8.4M4.9 4.9a10 10 0 000 14.2M19.1 4.9a10 10 0 010 14.2"/>',
'ai':'<path d="M12 3a4 4 0 00-4 4 4 4 0 00-3 6 4 4 0 003 6 4 4 0 008 0 4 4 0 003-6 4 4 0 00-3-6 4 4 0 00-4-4z"/><path d="M12 3v18M8 9h4M12 15h4"/>',
'cons':'<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/><path d="M8 9h8M8 13h5"/>',
}
def ic(k): return f'<div class="ico"><svg viewBox="0 0 24 24">{ICON[k]}</svg></div>'
NAV=[('index.html','Home','/'),('about.html','About','/about'),('services.html','Services','/services'),('contact.html','Contact','/contact')]
def page(file,title,desc,body,schema=None,sub=True):
    url=SITE+('/' if file=='index.html' else '/'+file)
    links=''.join(f'<a href="{h if f!="index.html" else "/"}"{" class=on" if f==file else ""}>{n}</a>' for f,n,h in NAV).replace('href="/about"','href="/about.html"')
    links=''.join(f'<a href="{"/" if f=="index.html" else "/"+f}"{" class=on" if f==file else ""}>{n}</a>' for f,n,_ in NAV)
    ld=[{"@context":"https://schema.org","@type":"Organization","name":"Chawl","url":SITE,"logo":SITE+"/assets/favicon.svg","email":"hello@chawl.in","description":"Chawl builds products for companies and provides software, hardware, IoT and AI consultancy.","knowsAbout":["Software development","Hardware engineering","Internet of Things","Artificial Intelligence","Product engineering"]},
        {"@context":"https://schema.org","@type":"WebSite","name":"Chawl","url":SITE}]
    if schema: ld+=schema
    ldh=''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#07080d">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Chawl">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{ldh}
</head><body>
<div id="bar"></div><div id="glow"></div>
<header><nav class="wrap"><a class="logo" href="/" aria-label="Chawl home">chawl<span>.in</span></a>
<button id="burger" aria-label="Menu">☰</button>
<div class="links">{links}<a class="btn" href="/contact.html">Start a project</a></div></nav></header>
<main>
{body}
</main>
<footer><div class="wrap"><div class="fgrid">
<div><a class="logo" href="/">chawl<span>.in</span></a><p style="color:var(--mut);margin-top:14px;max-width:320px">We build products for companies and advise on software, hardware, IoT and AI.</p></div>
<div><h4>Company</h4><ul><li><a href="/about.html">About</a></li><li><a href="/services.html">Services</a></li><li><a href="/contact.html">Contact</a></li></ul></div>
<div><h4>Expertise</h4><ul><li>Product Engineering</li><li>IoT &amp; Hardware</li><li>AI &amp; ML</li><li>Consultancy</li></ul></div>
<div><h4>Say hello</h4><ul><li><a href="mailto:hello@chawl.in">hello@chawl.in</a></li><li>India · Working worldwide</li></ul></div>
</div><div class="copy"><span>© <script>document.write(new Date().getFullYear())</script> Chawl. All rights reserved.</span><span>chawl.in</span></div></div></footer>
<script src="/assets/main.js" defer></script>
</body></html>'''

def cta():
    return '''<section><div class="wrap"><div class="big-cta rv"><span class="eyebrow">Let's build</span><h2>Have an idea? Let's make it <span class="grad">real.</span></h2><p class="lead">Tell us what you're working on. We'll respond within one business day.</p><a class="btn" href="/contact.html">Contact us →</a></div></div></section>'''

# ---------- HOME
home=f'''
<section class="hero"><canvas id="net" aria-hidden="true"></canvas><div class="wrap">
<div class="pill rv"><i></i> Product studio &amp; technology consultancy</div>
<h1 class="rv d1">We build products for <span class="grad" id="word" data-words='["ambitious companies","IoT devices","AI-first teams","the real world"]'>ambitious companies</span></h1>
<p class="lead rv d2">Chawl is a product engineering studio. We design and ship software, hardware, IoT and AI products — and advise teams on getting the technology decisions right.</p>
<div class="cta rv d3"><a class="btn" href="/contact.html">Start a project →</a><a class="btn ghost" href="/services.html">Explore services</a></div>
</div><div class="scroll"></div></section>
<div class="marq" aria-hidden="true"><div class="track">{''.join('<span>'+t+'</span>' for t in ['Software','Hardware','Internet of Things','Artificial Intelligence','Product Strategy','Embedded Systems','Machine Learning','Cloud','Consultancy']*2)}</div></div>

<section><div class="wrap"><span class="eyebrow rv">What we do</span><h2 class="rv">Two ways we <span class="grad">work with you</span></h2>
<p class="lead rv">Hand us the whole product, or bring us in for expert guidance. Either way you work directly with senior engineers.</p>
<div class="grid g2">
<a href="/services.html#products" class="card rv">{ic('prod')}<h3>Product Development</h3><p>End-to-end builds for companies — from first sketch to production launch and beyond.</p><ul><li>Web &amp; mobile applications</li><li>Connected devices &amp; hardware</li><li>AI-powered features and platforms</li></ul></a>
<a href="/services.html#consulting" class="card rv d1">{ic('cons')}<h3>Technology Consultancy</h3><p>Independent advice across software, hardware, IoT and AI to de-risk your roadmap.</p><ul><li>Architecture &amp; technical due diligence</li><li>Feasibility, prototyping &amp; vendor selection</li><li>Team enablement &amp; audits</li></ul></a>
</div></div></section>

<section class="stats"><div class="wrap"><div class="grid g4" style="margin-top:0">
<div class="stat rv"><div class="num grad" data-to="4" data-suf="">0</div><p>Core domains</p></div>
<div class="stat rv d1"><div class="num grad" data-to="100" data-suf="%">0</div><p>Ownership of your IP</p></div>
<div class="stat rv d2"><div class="num grad" data-to="24" data-suf="h">0</div><p>Response time</p></div>
<div class="stat rv d3"><div class="num grad" data-to="1" data-suf="">0</div><p>Team, idea to production</p></div>
</div></div></section>

<section><div class="wrap"><span class="eyebrow rv">Domains</span><h2 class="rv">Deep expertise where <span class="grad">tech meets reality</span></h2>
<div class="grid g4">
<div class="card rv">{ic('soft')}<h3>Software</h3><p>Scalable web, mobile and cloud platforms.</p></div>
<div class="card rv d1">{ic('hw')}<h3>Hardware</h3><p>Electronics, PCB design and embedded firmware.</p></div>
<div class="card rv d2">{ic('iot')}<h3>IoT</h3><p>Sensors, gateways and cloud dashboards that talk.</p></div>
<div class="card rv d3">{ic('ai')}<h3>AI</h3><p>LLMs, vision and ML that solve real business problems.</p></div>
</div><div style="text-align:center;margin-top:48px" class="rv"><a class="btn ghost" href="/services.html">See all services</a></div></div></section>

<section style="background:var(--bg2);border-block:1px solid var(--line)"><div class="wrap split">
<div><span class="eyebrow rv">How we work</span><h2 class="rv">A simple process, <span class="grad">no surprises</span></h2>
<div style="margin-top:40px">
<div class="step rv"><b>1 · Discover</b><p>We learn your market, users and constraints, then define what success looks like.</p></div>
<div class="step rv"><b>2 · Design &amp; prototype</b><p>Rapid prototypes — on screen or on a bench — to validate before we scale.</p></div>
<div class="step rv"><b>3 · Build</b><p>Short iterations, weekly demos and transparent progress.</p></div>
<div class="step rv"><b>4 · Launch &amp; evolve</b><p>Deployment, monitoring and support as your product grows.</p></div></div></div>
<div class="orbit rv" aria-hidden="true"><i></i><i></i><i></i><b>chawl</b></div>
</div></section>
{cta()}
'''

# ---------- SERVICES
svc=[('soft','Software Engineering','Web apps, mobile apps, APIs and cloud-native platforms built to scale.',['React / Next.js, Node, Python','iOS, Android &amp; cross-platform','Cloud, DevOps &amp; CI/CD']),
('hw','Hardware Design','From schematic to certified product: electronics, PCBs and embedded firmware.',['PCB design &amp; prototyping','Embedded C/C++, RTOS','Design for manufacturing']),
('iot','IoT Solutions','Connected devices with secure connectivity, fleet management and live dashboards.',['MQTT, BLE, LoRa, Wi-Fi, cellular','Edge computing &amp; OTA updates','Data pipelines &amp; analytics']),
('ai','AI &amp; Machine Learning','Practical AI: LLM apps, computer vision, forecasting and automation.',['LLM agents &amp; RAG systems','Computer vision &amp; edge AI','MLOps &amp; model evaluation'])]
cards=''.join(f'<div class="card rv {["","d1"][i%2]}">{ic(k)}<h3>{t}</h3><p>{d}</p><ul>{"".join("<li>"+x+"</li>" for x in l)}</ul></div>' for i,(k,t,d,l) in enumerate(svc))
services=f'''
<section class="sub-hero"><div class="wrap"><span class="eyebrow rv">Services</span><h1 class="rv d1">Products &amp; consultancy across <span class="grad">software, hardware, IoT and AI</span></h1>
<p class="lead rv d2">One partner for the whole stack — so your app, your device and your intelligence work as one product.</p></div></section>
<section id="products" style="padding-top:40px"><div class="wrap"><span class="eyebrow rv">Build</span><h2 class="rv">Product development for companies</h2>
<p class="lead rv">We take full ownership of delivery, or embed with your team. You keep 100% of the IP.</p><div class="grid g2">{cards}</div></div></section>
<section id="consulting" style="background:var(--bg2);border-block:1px solid var(--line)"><div class="wrap"><span class="eyebrow rv">Advise</span><h2 class="rv">Technology consultancy</h2>
<p class="lead rv">Independent, senior-level advice when the decisions are expensive to reverse.</p>
<div class="grid g3">
<div class="card rv">{ic('cons')}<h3>Strategy &amp; Roadmaps</h3><p>Translate business goals into a pragmatic technical plan with clear milestones.</p></div>
<div class="card rv d1">{ic('soft')}<h3>Architecture &amp; Audits</h3><p>Review of code, systems, security and scalability — with an actionable fix list.</p></div>
<div class="card rv d2">{ic('hw')}<h3>Feasibility &amp; Prototyping</h3><p>Prove it works before you commit: proof-of-concepts for hardware, IoT and AI.</p></div>
</div>
<div class="tags rv"><span>Technical due diligence</span><span>Vendor selection</span><span>Make vs. buy</span><span>Sensor selection</span><span>AI readiness</span><span>Team mentoring</span><span>Cost optimisation</span></div></div></section>
<section><div class="wrap"><span class="eyebrow rv">FAQ</span><h2 class="rv">Common questions</h2><div style="margin-top:30px;max-width:820px">
<details class="rv"><summary>Which industries do you work with?</summary><p>We work with companies of all sizes — manufacturing, logistics, energy, agriculture, healthcare, retail and SaaS — wherever technology can create a product advantage.</p></details>
<details class="rv"><summary>Can you handle both hardware and software?</summary><p>Yes. That's our edge. A single team designs the device, firmware, cloud and app so everything fits together.</p></details>
<details class="rv"><summary>Do you offer consulting without a build engagement?</summary><p>Absolutely. Many clients start with a short consulting sprint or audit and decide afterwards whether we build.</p></details>
<details class="rv"><summary>Who owns the IP?</summary><p>You do. All code, designs and documentation are transferred to you.</p></details>
<details class="rv"><summary>How do we get started?</summary><p>Send us a note through the contact page. We'll set up a free discovery call within one business day.</p></details>
</div></div></section>{cta()}'''
faq=[("Which industries do you work with?","We work with companies of all sizes — manufacturing, logistics, energy, agriculture, healthcare, retail and SaaS."),("Can you handle both hardware and software?","Yes. A single team designs the device, firmware, cloud and app."),("Do you offer consulting without a build engagement?","Yes. Many clients start with a consulting sprint or audit."),("Who owns the IP?","You do. All code, designs and documentation are transferred to you.")]
svc_schema=[{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]+[{"@context":"https://schema.org","@type":"Service","name":t.replace("&amp;","&"),"provider":{"@type":"Organization","name":"Chawl"},"description":d} for _,t,d,_ in svc]

# ---------- ABOUT
about=f'''
<section class="sub-hero"><div class="wrap"><span class="eyebrow rv">About Chawl</span><h1 class="rv d1">A small team building <span class="grad">serious technology</span></h1>
<p class="lead rv d2">Chawl is a product and consultancy company. We exist to help businesses turn ideas into working products — across software, hardware, IoT and AI.</p></div></section>
<section style="padding-top:40px"><div class="wrap split">
<div><span class="eyebrow rv">Our story</span><h2 class="rv">Where the digital meets the physical</h2>
<p class="lead rv" style="margin-bottom:16px">Most products today live in both worlds: a device in the field, software in the cloud, intelligence in between. Few teams can build all three.</p>
<p class="lead rv">We started Chawl to be that team — engineers who are as comfortable with a soldering iron as with a Kubernetes cluster and a language model.</p></div>
<div class="orbit rv" aria-hidden="true"><i></i><i></i><i></i><b>chawl</b></div></div></section>
<section style="background:var(--bg2);border-block:1px solid var(--line)"><div class="wrap"><span class="eyebrow rv">Mission &amp; values</span><h2 class="rv">What we stand for</h2>
<div class="grid g3">
<div class="card rv"><h3>Build to last</h3><p>Clean architecture, tested code and documented hardware — products that survive contact with reality.</p></div>
<div class="card rv d1"><h3>Honest advice</h3><p>If something isn't feasible or isn't worth it, we'll tell you — before you spend the money.</p></div>
<div class="card rv d2"><h3>Your success, your IP</h3><p>Transparent pricing, full ownership and knowledge transfer on every engagement.</p></div>
</div></div></section>
<section><div class="wrap"><span class="eyebrow rv">Company details</span><h2 class="rv">At a glance</h2>
<div class="grid g2"><div class="card rv"><h3>Who we are</h3><ul><li>Name: Chawl</li><li>Website: chawl.in</li><li>Based in: India, serving clients worldwide</li><li>Email: hello@chawl.in</li></ul></div>
<div class="card rv d1"><h3>What we offer</h3><ul><li>Product development for companies</li><li>Software &amp; hardware consultancy</li><li>IoT and AI solutions</li></ul></div></div>
<div class="tags rv"><span>Python</span><span>TypeScript</span><span>React</span><span>Node.js</span><span>C / C++</span><span>Rust</span><span>ESP32</span><span>STM32</span><span>Raspberry Pi</span><span>MQTT</span><span>AWS / GCP</span><span>PyTorch</span><span>LLMs</span><span>OpenCV</span></div></div></section>{cta()}'''

# ---------- CONTACT
contact='''
<section class="sub-hero"><div class="wrap"><span class="eyebrow rv">Contact</span><h1 class="rv d1">Let's talk about <span class="grad">your project</span></h1>
<p class="lead rv d2">Share a few details and we'll get back within one business day.</p></div></section>
<section style="padding-top:30px"><div class="wrap split" style="align-items:start">
<form id="cform" class="rv" novalidate>
<div class="row"><input name="name" placeholder="Your name" required autocomplete="name" aria-label="Your name"><input name="email" type="email" placeholder="Email" required autocomplete="email" aria-label="Email"></div>
<div class="row"><input name="company" placeholder="Company" autocomplete="organization" aria-label="Company"><select name="topic" aria-label="Interest"><option>Product development</option><option>Software consultancy</option><option>Hardware consultancy</option><option>IoT</option><option>AI</option><option>Something else</option></select></div>
<textarea name="message" placeholder="Tell us about your project" required aria-label="Message"></textarea>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn" type="submit">Send message →</button><p id="fmsg" role="status"></p></form>
<div class="info rv d1">
<div class="card"><h3>Email</h3><a href="mailto:hello@chawl.in">hello@chawl.in</a></div>
<div class="card"><h3>Website</h3><a href="https://chawl.in">chawl.in</a></div>
<div class="card"><h3>Location</h3><p>India · Remote-first, working with clients worldwide</p></div>
<div class="card"><h3>Hours</h3><p>Mon–Sat, 10:00–19:00 IST</p></div>
</div></div></section>'''
contact_schema=[{"@context":"https://schema.org","@type":"ContactPage","name":"Contact Chawl","url":SITE+"/contact.html"}]

pages=[('index.html','Chawl — Product Development & Software, Hardware, IoT, AI Consultancy','Chawl builds products for companies and provides software, hardware, IoT and AI consultancy. Start your project with our product engineering studio.',home,None),
('services.html','Services — Product Development & Software, Hardware, IoT, AI Consulting | Chawl','Explore Chawl services: end-to-end product development, software engineering, hardware design, IoT solutions, AI/ML and technology consultancy.',services,svc_schema),
('about.html','About Chawl — Product Studio for Software, Hardware, IoT & AI','Learn about Chawl, a product engineering and technology consultancy company building software, hardware, IoT and AI solutions for businesses.',about,None),
('contact.html','Contact Chawl — Start Your Product or Consultancy Project','Contact Chawl to discuss product development or software, hardware, IoT and AI consultancy. We reply within one business day.',contact,contact_schema)]
for f,t,d,b,s in pages: open(f,'w').write(page(f,t,d,b,s))
open('404.html','w').write(page('404.html','Page not found | Chawl','Page not found.','<section class="sub-hero"><div class="wrap"><h1>404 — <span class="grad">lost in space</span></h1><p class="lead">That page doesn\'t exist.</p><br><a class="btn" href="/">Back home</a></div></section>'))
urls=['/','/services.html','/about.html','/contact.html']
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}{u}</loc><changefreq>monthly</changefreq><priority>{"1.0" if u=="/" else "0.8"}</priority></url>\n' for u in urls)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
open('assets/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#00e5c3"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="#07080d"/><text x="32" y="45" font-family="Arial" font-weight="700" font-size="40" text-anchor="middle" fill="url(#g)">c</text></svg>')
open('assets/og.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><defs><linearGradient id="g"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#00e5c3"/></linearGradient></defs><rect width="1200" height="630" fill="#07080d"/><text x="80" y="300" font-family="Arial" font-weight="700" font-size="120" fill="url(#g)">chawl.in</text><text x="80" y="400" font-family="Arial" font-size="42" fill="#e8eaf2">Products &amp; consultancy: Software · Hardware · IoT · AI</text></svg>')
open('CNAME','w').write('chawl.in\n')
