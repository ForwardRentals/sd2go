# Generates both design options from one set of copy. Run: python build.py
#   Option 1 (bold black + red)  -> site root
#   Option 2 (light + clean)     -> option-2/
import os

BASE = "https://forwardrentals.github.io/sd2go/"
EMAIL = "info@sd2go.com"
NAV = [("index.html", "Home"), ("accounting.html", "Accounting"), ("computers.html", "Computers"), ("about.html", "About")]

OPTIONS = {
    "": {"css": "styles.css", "fonts": "family=Archivo:wght@700;800;900&family=Inter:wght@400;600;700", "label": "Option 1", "other": ("option-2/", "See option 2")},
    "option-2/": {"css": "styles-2.css", "fonts": "family=Fraunces:opsz,wght@9..144,600;9..144,700&family=DM+Sans:wght@400;500;700", "label": "Option 2", "other": ("../", "See option 1")},
}


def head(title, desc, page, opt, up):
    o = OPTIONS[opt]
    links = "".join(
        f'<a href="{href}"{" aria-current=page" if href == page else ""}>{name}</a>' for href, name in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}images/repair.jpg">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{o['fonts']}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}{o['css']}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"SD2GO","description":"Small business accounting and income tax, plus computer sales and service, in Surrey, BC.","email":"{EMAIL}","url":"{BASE}","founder":{{"@type":"Person","name":"David Officer"}},"address":{{"@type":"PostalAddress","addressLocality":"Surrey","addressRegion":"BC","addressCountry":"CA"}},"areaServed":"Surrey, BC"}}
</script>
</head>
<body>
<div class="preview-bar">Website preview: <strong>{o['label']}</strong> <a href="{o['other'][0]}{page if page != 'index.html' else ''}">{o['other'][1]} &rarr;</a></div>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap head-row">
    <a class="logo" href="index.html" aria-label="SD2GO home">SD<span>2</span>GO</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-red" href="contact.html">Get a quote</a></nav>
  </div>
</header>
<main id="main">
"""


def foot(up):
    links = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in NAV) + '<li><a href="contact.html">Contact</a></li>'
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html">SD<span>2</span>GO</a>
        <p style="margin-top:14px">Small business accounting and computer sales &amp; service in Surrey, BC.</p>
      </div>
      <div><h3>Pages</h3><ul>{links}</ul></div>
      <div><h3>Contact</h3><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="contact.html">Request a quote</a></li><li>Surrey, BC</li></ul></div>
    </div>
    <div class="foot-base">
      <span>&copy; <span id="yr">2026</span> SD2GO. All rights reserved.</span>
      <span>Built by <a href="https://freesitecompany.com">FreeSiteCompany.com</a></span>
    </div>
    <p class="credits">Photos via Wikimedia Commons:
      <a href="https://commons.wikimedia.org/wiki/File:Computer_repair_in_progress.jpg">Vintechcomputerservices</a> (CC BY-SA 4.0),
      <a href="https://commons.wikimedia.org/wiki/File:Laptop_Repair.jpg">Augustin Wafflart</a> (CC BY 4.0),
      <a href="https://commons.wikimedia.org/wiki/File:Aurora_electronic_calculator_DT210_08.jpg">Coyau</a> (CC BY-SA 3.0).</p>
  </div>
</footer>
<script src="{up}site.js"></script>
</body>
</html>
"""


CTA = """<section class="cta"><div class="wrap">
  <h2>Tell us what you need and we'll send you a quote.</h2>
  <div class="hero-actions" style="margin:0"><a class="btn btn-dark" href="contact.html">Request a quote</a><a class="btn btn-ghost" href="mailto:info@sd2go.com">Email us</a></div>
</div></section>
"""


def pages(img):
    return {
"index.html": ("SD2GO | Small Business Accounting & Computer Service in Surrey, BC",
 "SD2GO helps Surrey small businesses with accounting, income tax, and computer sales and service. Email or request a quote.",
f"""<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Surrey, BC</span>
    <h1>Your books <span>and</span> your computers, handled.</h1>
    <p class="lead">SD2GO helps small businesses with accounting and income tax, and with the computers that keep them running.</p>
    <div class="hero-actions">
      <a class="btn btn-red" href="contact.html">Request a quote</a>
      <a class="btn btn-ghost" href="mailto:info@sd2go.com">Email us</a>
    </div>
  </div>
  <div class="hero-photo"><img src="{img}repair.jpg" width="1600" height="1060" alt="Hands working on the inside of a laptop during a repair"></div>
</div></section>

<section><div class="wrap">
  <div class="section-head">
    <h2>Two services, one contact.</h2>
    <p>Most small businesses juggle a bookkeeper and a separate computer person. With SD2GO you deal with one person for both.</p>
  </div>
  <div class="split">
    <article class="card">
      <img src="{img}calculator.jpg" width="1400" height="700" alt="Close-up of an electronic calculator display" loading="lazy">
      <div class="card-body">
        <span class="tag">Accounting</span>
        <h3>Small business accounting &amp; income tax</h3>
        <p>Keep your numbers in order through the year and get your taxes done right.</p>
        <ul><li>Small business accounting</li><li>Income tax</li></ul>
        <a class="btn btn-dark" href="accounting.html">Accounting services</a>
      </div>
    </article>
    <article class="card">
      <img src="{img}laptop.jpg" width="900" height="1200" alt="Open laptop on a desk with its battery and memory exposed for service" loading="lazy">
      <div class="card-body">
        <span class="tag">Computers</span>
        <h3>Computer sales &amp; service</h3>
        <p>Need a new machine, or need the one you have working properly again? Get in touch.</p>
        <ul><li>Computer sales</li><li>Computer service</li></ul>
        <a class="btn btn-dark" href="computers.html">Computer services</a>
      </div>
    </article>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><h2>Why small businesses call SD2GO</h2></div>
  <div class="why">
    <div><h3>One point of contact</h3><p>Your accounting and your computers, handled by the same person.</p></div>
    <div><h3>Local to Surrey</h3><p>A Surrey, BC business working with small businesses in the area.</p></div>
    <div><h3>Quote first</h3><p>Tell us what you need and you'll get a quote before any work starts.</p></div>
  </div>
</div></section>
""" + CTA),

"accounting.html": ("Small Business Accounting & Income Tax in Surrey, BC | SD2GO",
 "Small business accounting and income tax from SD2GO in Surrey, BC. Request a quote by email.",
f"""<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Accounting</span>
  <h1>Small business accounting &amp; income tax</h1>
  <p>Accounting and income tax for small businesses in Surrey, BC.</p>
</div></section>

<section><div class="wrap feature">
  <img src="{img}calculator.jpg" width="1400" height="700" alt="Close-up of an electronic calculator display">
  <div>
    <h2>Numbers you can count on</h2>
    <p>Running a small business is enough work without the paperwork. SD2GO looks after your accounting and your income tax so you can focus on your customers.</p>
    <ul class="list-grid">
      <li>Small business accounting</li>
      <li>Income tax</li>
    </ul>
    <p style="margin-top:24px"><a class="btn btn-red" href="contact.html?service=Accounting">Request an accounting quote</a></p>
  </div>
</div></section>
""" + CTA),

"computers.html": ("Computer Sales & Service in Surrey, BC | SD2GO",
 "Computer sales and service from SD2GO in Surrey, BC. Request a quote.",
f"""<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Computers</span>
  <h1>Computer sales &amp; service</h1>
  <p>Buying a computer or getting one fixed, in Surrey, BC.</p>
</div></section>

<section><div class="wrap feature">
  <div>
    <h2>Get the right machine, and keep it running</h2>
    <p>Whether you need a new computer or the one you rely on needs attention, SD2GO can help. Tell us what you're working with and what you need.</p>
    <ul class="list-grid">
      <li>Computer sales</li>
      <li>Computer service</li>
    </ul>
    <p style="margin-top:24px"><a class="btn btn-red" href="contact.html?service=Computers">Request a computer quote</a></p>
  </div>
  <img src="{img}laptop.jpg" width="900" height="1200" alt="Open laptop on a desk with its battery and memory exposed for service" class="tall">
</div></section>

<section class="alt"><div class="wrap">
  <div class="feature">
    <img src="{img}repair.jpg" width="1600" height="1060" alt="Hands working on the inside of a laptop during a repair" loading="lazy">
    <div>
      <h2>Not sure what's wrong?</h2>
      <p>That's fine. Describe what the computer is doing in the quote form and we'll follow up by email.</p>
      <a class="btn btn-dark" href="contact.html?service=Computers">Describe the problem</a>
    </div>
  </div>
</div></section>
""" + CTA),

"about.html": ("About SD2GO | Surrey, BC",
 "SD2GO is run by David Officer in Surrey, BC, offering small business accounting and computer sales and service.",
f"""<section class="page-hero"><div class="wrap">
  <span class="eyebrow">About</span>
  <h1>About SD2GO</h1>
  <p>A Surrey, BC business run by David Officer.</p>
</div></section>

<section><div class="wrap feature">
  <div>
    <h2>Accounting and computers, under one roof</h2>
    <p>SD2GO is run by David Officer in Surrey, BC. It brings together two things every small business needs: well-kept books and computers that work.</p>
    <p>Instead of hunting down a bookkeeper and a separate tech person, you can reach out to one place for both.</p>
    <div class="hero-actions"><a class="btn btn-red" href="contact.html">Get in touch</a></div>
  </div>
  <img src="{img}repair.jpg" width="1600" height="1060" alt="Hands working on the inside of a laptop during a repair">
</div></section>
""" + CTA),

"contact.html": ("Contact SD2GO | Request a Quote",
 "Email SD2GO or request a quote for small business accounting or computer sales and service in Surrey, BC.",
"""<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Contact</span>
  <h1>Request a quote</h1>
  <p>Tell us a bit about what you need. We'll reply by email.</p>
</div></section>

<section><div class="wrap contact-grid">
  <aside class="contact-box">
    <h2>Email us directly</h2>
    <p>Prefer email? Write any time.</p>
    <p class="big"><a href="mailto:info@sd2go.com">info@sd2go.com</a></p>
    <p style="margin:24px 0 0">Based in Surrey, BC.</p>
  </aside>
  <form action="https://formsubmit.co/info@sd2go.com" method="POST">
    <input type="hidden" name="_subject" value="New quote request from the SD2GO website">
    <input type="hidden" name="_next" value="https://forwardrentals.github.io/sd2go/thanks.html">
    <input type="hidden" name="_template" value="table">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="row2">
      <label>Name<input name="name" autocomplete="name" required></label>
      <label>Email<input type="email" name="email" autocomplete="email" required></label>
    </div>
    <div class="row2">
      <label>Business (optional)<input name="business" autocomplete="organization"></label>
      <label>What do you need?
        <select name="service" id="service">
          <option>Accounting</option><option>Income tax</option><option>Computers</option><option>Accounting and computers</option><option>Something else</option>
        </select>
      </label>
    </div>
    <label>Details<textarea name="message" required placeholder="What do you need help with?"></textarea></label>
    <button class="btn btn-red" type="submit">Send quote request</button>
    <p class="form-note">We'll reply to the email you enter. No phone number needed.</p>
  </form>
</div></section>
"""),

"thanks.html": ("Thanks | SD2GO", "Your request was sent to SD2GO.",
"""<section class="page-hero thanks"><div class="wrap">
  <span class="eyebrow">Sent</span>
  <h1>Thanks, we got it.</h1>
  <p>Your request is on its way. We'll reply by email.</p>
  <div class="hero-actions"><a class="btn btn-red" href="index.html">Back to home</a></div>
</div></section>
"""),
    }


here = os.path.dirname(os.path.abspath(__file__))
for opt in OPTIONS:
    up = "../" if opt else ""
    out = os.path.join(here, opt)
    os.makedirs(out, exist_ok=True)
    for name, (title, desc, body) in pages(up + "images/").items():
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(head(title, desc, name, opt, up) + body + foot(up))

with open(os.path.join(here, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{BASE}{'' if n == 'index.html' else n}</loc></url>\n" for n, _ in NAV + [("contact.html", "")])
            + "</urlset>\n")
with open(os.path.join(here, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nDisallow: /\n# Preview only. At launch: Allow: / and Sitemap: {BASE}sitemap.xml\n")
print("built option 1 + option 2")
