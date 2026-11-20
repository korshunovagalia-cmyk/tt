#!/usr/bin/env python3
"""
Tint & Sun — architectural window film site (content from brochure 2026).

Composes the shared chrome (utility bar, nav, mobile drawer, CTA band, footer)
with each page body and writes plain .html files to the project root.

    python3 build.py
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE = "+971 55 386 54 54"
PHONE_TEL = "+971553865454"
WA = "https://wa.me/971553865454"
EMAIL = "tintandsun.uae@gmail.com"
IG = "https://www.instagram.com/tint_and_sun/"

NAV = [
    ("HOME", "index.html", None),
    ("ABOUT US", "about.html", None),
    ("SOLUTIONS", "solar-films.html", [
        ("SOLAR CONTROL FILMS", "solar-films.html"),
        ("DAYTIME PRIVACY FILMS", "privacy-films.html"),
        ("DECORATIVE GLASS FILMS", "decorative.html"),
    ]),
    ("BRANDS", "brands.html", None),
    ("PROJECTS", "projects.html", None),
    ("CONTACT", "contact.html", None),
]

ARROW = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M3 8h9m0 0L8.5 4.5M12 8l-3.5 3.5" stroke="currentColor" '
         'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

CHEV = ('<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
        '<path d="M2 4l3 3 3-3" stroke="currentColor" stroke-width="1.5" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')

ICON_PHONE = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
              '<path d="M5.2 2.5 6.6 5 5.4 6.4a8.4 8.4 0 0 0 4.2 4.2L11 9.4l2.5 1.4v2.2c0 .6-.5 1-1.1 1'
              'C7 13.6 2.4 9 2.1 3.6c0-.6.4-1.1 1-1.1h2.1Z" stroke="currentColor" stroke-width="1.4" '
              'stroke-linejoin="round"/></svg>')

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.3A10 10 0 1 0 12 2Zm5.2 14c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .1-1.6-.1-.4-.1-.9-.3-1.5-.6a11 11 0 0 1-4.2-3.8c-.3-.5-.7-1.2-.7-2s.4-1.2.6-1.4c.2-.2.4-.3.6-.3h.4c.1 0 .3 0 .5.4l.7 1.6c0 .1.1.3 0 .4l-.3.5-.2.3c-.1.1-.2.2 0 .5.2.3.6 1 1.3 1.6.9.8 1.6 1 1.9 1.2.2.1.4.1.5-.1l.6-.7c.2-.2.3-.2.5-.1l1.5.7c.2.1.4.2.4.3.1.1.1.4 0 .8Z"/></svg>')

# line icons (stroke = currentColor) used for benefits / sectors
def ico(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % path)

I_THERMO = ico('<path d="M10 14.5V4a2 2 0 1 1 4 0v10.5a4 4 0 1 1-4 0Z"/><path d="M12 9v7"/>')
I_SUN = ico('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>')
I_SHIELD = ico('<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6L12 3Z"/>')
I_EYE = ico('<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>')
I_LEAF = ico('<path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15Z"/><path d="M5 19 13 11"/>')
I_GRID = ico('<rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/>')
I_HOUSE = ico('<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>')
I_TOWER = ico('<rect x="6" y="3" width="12" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>')
I_FRAME = ico('<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M9 9v11"/>')
I_PERSON = ico('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/>')


# --------------------------------------------------------------------------- chrome

def nav_html(active):
    items = []
    for label, href, sub in NAV:
        is_active = (active == href) or (sub and any(active == s[1] for s in sub))
        cls = ' class="is-active"' if is_active else ''
        if sub:
            drop = "".join(
                '<li><a href="%s"%s>%s</a></li>' %
                (h, ' class="is-active"' if active == h else '', t) for t, h in sub)
            items.append(
                '<li class="nav__item--has-drop"><a href="%s"%s>%s %s</a>'
                '<ul class="nav__drop">%s</ul></li>' % (href, cls, label, CHEV, drop))
        else:
            items.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
    return "".join(items)


def drawer_html(active):
    out = []
    for label, href, sub in NAV:
        if sub:
            out.append('<li><a href="%s">%s</a><ul class="drawer__sub">%s</ul></li>' % (
                href, label,
                "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in sub)))
        else:
            out.append('<li><a href="%s">%s</a></li>' % (href, label))
    return "".join(out)


HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v=2">"""


HEADER = """<div class="utility">
  <div class="wrap">
    <div class="utility__left">
      <span class="utility__tag">Solar control, privacy &amp; decorative window films &middot; Serving the UAE since 2012</span>
    </div>
    <div class="utility__right">
      <a href="{ig}" target="_blank" rel="noopener">Instagram</a>
      <a href="{wa}" target="_blank" rel="noopener">WhatsApp</a>
      <a href="tel:{phone_tel}">{phone}</a>
    </div>
  </div>
</div>

<header class="nav">
  <div class="wrap nav__inner">
    <a class="nav__logo" href="index.html" aria-label="Tint and Sun — home">
      <img src="assets/img/logo.png" alt="Tint and Sun">
    </a>
    <ul class="nav__menu">{nav}</ul>
    <div class="nav__actions">
      <a class="nav__phone" href="tel:{phone_tel}">{icon_phone}{phone}</a>
      <a class="btn btn--primary btn--sm" href="contact.html">Free consultation</a>
      <button class="nav__burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="drawer"><span></span></button>
    </div>
  </div>
</header>

<nav class="drawer" id="drawer" aria-label="Mobile">
  <ul>{drawer}</ul>
  <div class="drawer__cta">
    <a class="btn btn--primary" href="{wa}" target="_blank" rel="noopener">Free consultation on WhatsApp</a>
    <a class="btn btn--ghost" href="tel:{phone_tel}">Call {phone}</a>
  </div>
</nav>"""


CTA_BAND = """<section class="cta-band">
  <div class="wrap">
    <div class="section-head--split section-head" style="margin-bottom:0">
      <div class="reveal">
        <h2>Let&rsquo;s find the right solution for your glass.</h2>
        <p>Send us the property location, photographs of the glass, approximate measurements and your priority &mdash; heat, privacy, UV or decoration. Free site inspection.</p>
      </div>
      <div class="btn-row reveal" style="margin-top:0">
        <a class="btn btn--primary" href="{wa}" target="_blank" rel="noopener">Free consultation on WhatsApp</a>
        <a class="btn btn--ghost" href="contact.html">Contact us</a>
      </div>
    </div>
  </div>
</section>"""


FOOTER = """<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="assets/img/logo.png" alt="Tint and Sun">
        <p>Tint and Sun Decoration Design LLC. Professional window film solutions &mdash; heat reduction, daytime privacy, UV protection and decorative finishes across the UAE since 2012.</p>
        <div class="footer__social">
          <a href="{ig}" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.8"/><circle cx="17" cy="7" r="1" fill="currentColor" stroke="none"/></svg></a>
          <a href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{wa_svg}</a>
        </div>
      </div>

      <div>
        <h4>Solutions</h4>
        <ul>
          <li><a href="solar-films.html">Solar control films</a></li>
          <li><a href="solar-films.html#transparent">Transparent solar films</a></li>
          <li><a href="privacy-films.html">Daytime privacy films</a></li>
          <li><a href="decorative.html">Decorative glass films</a></li>
        </ul>
      </div>

      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="brands.html">Brands we work with</a></li>
          <li><a href="projects.html">Selected projects</a></li>
          <li><a href="contact.html#standards">Our standards</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>

      <div>
        <h4>Find us</h4>
        <ul>
          <li>TAHA Business Center, office 303 B<br>Al Quoz 3, Dubai, UAE</li>
          <li><a href="tel:{phone_tel}">{phone}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li>Tue&ndash;Sun: 10am&ndash;7pm<br>Mon: Off</li>
        </ul>
      </div>
    </div>

    <div class="footer__bottom">
      <span>&copy; 2026 Tint and Sun Decoration Design LLC. All rights reserved.</span>
      <nav>
        <a href="solar-films.html">Solutions</a>
        <a href="projects.html">Projects</a>
        <a href="contact.html">Contact</a>
      </nav>
    </div>
  </div>
</footer>

<a class="fab" href="{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{wa_svg}</a>

<script src="assets/js/main.js"></script>"""


PAGE = """<!doctype html>
<html lang="en">
<head>
{head}
</head>
<body>
{header}
<main>
{body}
</main>
{cta}
{footer}
</body>
</html>
"""


# --------------------------------------------------------------------------- helpers

def T(tpl, **kw):
    """Token substitution: {{NAME}} -> value. Copy contains literal % signs."""
    for key, val in kw.items():
        tpl = tpl.replace("{{" + key + "}}", val)
    return tpl


def page_hero(crumb, title, lede, img=None):
    media = ('<div class="pagehero__media"><img src="%s" alt=""></div>' % img) if img else ""
    cls = "pagehero pagehero--img" if img else "pagehero"
    return """<section class="%s">
  %s
  <div class="wrap">
    <p class="pagehero__crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; %s</p>
    <h1>%s</h1>
    <p>%s</p>
  </div>
</section>""" % (cls, media, crumb, title, lede)


def head(eyebrow, title, sub="", link=None):
    right = ('<a class="link-arrow reveal" href="%s">%s %s</a>' % (link[1], link[0], ARROW)) if link else ""
    sub_html = ('<p class="h-sub">%s</p>' % sub) if sub else ""
    split = " section-head--split" if link else ""
    return """<div class="section-head%s">
      <div class="reveal">
        <p class="eyebrow">%s</p>
        <h2 class="h-section">%s</h2>
        %s
      </div>
      %s
    </div>""" % (split, eyebrow, title, sub_html, right)


# --------------------------------------------------------------------------- shared blocks

STATS = """<section class="stats">
  <div class="wrap">
    <div class="stats__grid stats__grid--6">
      <div class="stats__item reveal"><div class="stats__num">14+</div><div class="stats__label">years in Dubai</div></div>
      <div class="stats__item reveal" data-delay="60"><div class="stats__num">8000+</div><div class="stats__label">happy clients</div></div>
      <div class="stats__item reveal" data-delay="120"><div class="stats__num">99.9%</div><div class="stats__label">UV rays blocked (up to)</div></div>
      <div class="stats__item reveal" data-delay="180"><div class="stats__num">98%</div><div class="stats__label">IR rejection (up to)</div></div>
      <div class="stats__item reveal" data-delay="240"><div class="stats__num">21%</div><div class="stats__label">lower AC bills (up to)</div></div>
      <div class="stats__item reveal" data-delay="300"><div class="stats__num">8 yrs</div><div class="stats__label">warranty (up to)</div></div>
    </div>
  </div>
</section>"""


TIERS = [
    ("01", "HP type film", "45% &ndash; 72%", "15% &ndash; 35%", "Dependable", "2 years", False),
    ("02", "Ceramic type film", "55% &ndash; 89%", "25% &ndash; 40%", "Dependable", "4 years", False),
    ("03", "Nano-ceramic type film", "72% &ndash; 99%", "40% &ndash; 70%", "Non dependable", "8 years", True),
]


def tier_cards():
    cards = []
    for i, (no, name, irr, tser, dep, war, feat) in enumerate(TIERS):
        cards.append("""<div class="price-card%s reveal" data-delay="%d">
        %s
        <p class="price-card__type">%s</p>
        <h3>%s</h3>
        <div class="price-card__amount">%s<small>heat resistance (IRR)</small></div>
        <dl class="spec">
          <div><dt>TSER</dt><dd>%s</dd></div>
          <div><dt>Heat rejection vs. tint darkness</dt><dd>%s</dd></div>
          <div><dt>UV block</dt><dd>99%%</dd></div>
          <div><dt>Warranty</dt><dd>%s</dd></div>
        </dl>
      </div>""" % (" price-card--featured" if feat else "", i * 90,
                   '<span class="price-card__badge">Best performance</span>' if feat else "",
                   no, name, irr, tser, dep, war))
    return '<div class="grid grid--3">%s</div>' % "".join(cards)


TIER_NOTE = """<div class="note-band reveal">
  <p><strong>99% UV block</strong> &mdash; not dependent on type of film or tint darkness level.</p>
  <p><strong>0% &ndash; 90% VLT</strong> (Visible Light Transmission or darkness) available in all types.</p>
  <p><strong>Daylight privacy</strong> (exterior privacy with clear visibility from inside) available in all options.</p>
  <p><strong>Available in 6 brands.</strong></p>
</div>"""


BENEFITS = [
    (I_THERMO, "Cooler indoors", "Reduces heat gain and lowers AC use."),
    (I_SUN, "Less glare", "More comfortable vision, better focus."),
    (I_SHIELD, "UV protection", "Protects your skin, furniture and interiors."),
    (I_EYE, "More privacy", "Keeps your space less visible from outside."),
    (I_LEAF, "Energy efficient", "Lower energy costs, more sustainable."),
    (I_GRID, "Lasting comfort", "A cooler, brighter and safer environment."),
]


def benefits():
    return '<div class="benefits">%s</div>' % "".join(
        '<div class="benefit reveal" data-delay="%d"><span class="benefit__icon">%s</span><h3>%s</h3><p>%s</p></div>'
        % (i * 60, ic, t, d) for i, (ic, t, d) in enumerate(BENEFITS))


BRANDS = [
    ("metamark.png", "Metamark"), ("3m.png", "3M"), ("konica-minolta.png", "Konica Minolta"),
    ("avery.png", "Avery"), ("johnson.png", "Johnson Window Films"), ("sungard.png", "SunGard"),
    ("suntek.png", "SunTek"), ("danube.png", "Danube"), ("decorative-wraps.png", "Decorative Wraps"),
    ("llumar.png", "LLumar"), ("nanocare.png", "Nano Care"), ("ecocool.png", "Eco Cool"),
]


def brand_grid(items=BRANDS):
    return '<div class="brands brands--logos">%s</div>' % "".join(
        '<div class="brand"><img src="assets/img/brands/%s" alt="%s" loading="lazy"></div>' % (f, n)
        for f, n in items)


PROJECTS = [
    ("clinic.jpg", "Commercial &mdash; Speciality hospital"),
    ("glass-hq.jpg", "Commercial &mdash; Glass façade HQ"),
    ("terrace.jpg", "Commercial &mdash; Restaurant terrace"),
    ("warehouse.jpg", "Commercial &mdash; Showroom glazing"),
    ("the-vibe.jpg", "Retail &mdash; The Vibe studio"),
    ("modern-villa.jpg", "Residential &mdash; Modern villa"),
    ("dr-roze.jpg", "Commercial &mdash; Dental clinic"),
    ("rx.jpg", "Retail &mdash; Pharmacy shopfront"),
    ("flower-power.jpg", "Retail &mdash; Flower Power"),
    ("harmony.jpg", "Commercial &mdash; Harmony building"),
    ("villa.jpg", "Residential &mdash; Villa terrace"),
]


def project_grid(count=None):
    items = PROJECTS[:count] if count else PROJECTS
    return '<div class="gal">%s</div>' % "".join(
        '<div class="gal__cell reveal" data-delay="%d"><img src="assets/img/projects/%s" alt="%s" loading="lazy"><span>%s</span></div>'
        % (i % 3 * 80, f, l.replace("&mdash;", "-"), l) for i, (f, l) in enumerate(items))


STEPS = [
    ("Assessment", "Send photos of your windows or book a site visit for a fast, accurate quote. For larger or commercial jobs, we assess access, glass type and site conditions in person."),
    ("Film specification", "Based on your priorities &mdash; heat, privacy, budget or appearance &mdash; we recommend the right film tier and shade, with samples available to view before you commit."),
    ("Installation", "Installed by an experienced team, with commercial and façade work scheduled to minimise disruption to your business or building."),
    ("Final inspection", "Every job is checked on completion for a clean, bubble-free, edge-to-edge finish before we consider it done."),
    ("Warranty &amp; quality control", "All work is backed by a manufacturer warranty (2 years to lifetime, depending on film tier) covering bubbling, discolouration and other film defects from the date of installation."),
]


def steps():
    return '<ol class="steps">%s</ol>' % "".join(
        '<li class="step reveal" data-delay="%d"><span class="step__no">%02d</span><h3>%s</h3><p>%s</p></li>'
        % (i * 70, i + 1, t, d) for i, (t, d) in enumerate(STEPS))


CONTACT_INFO = """<div>
  <div class="info-block">
    <h3>Company</h3>
    <p>Tint and Sun Decoration Design LLC</p>
  </div>
  <div class="info-block">
    <h3>Office</h3>
    <p>TAHA Business Center, office 303 B<br>Al Quoz 3, Dubai, UAE</p>
  </div>
  <div class="info-block">
    <h3>Tel / WhatsApp</h3>
    <a href="tel:{phone_tel}">{phone}</a>
  </div>
  <div class="info-block">
    <h3>E-mail</h3>
    <a href="mailto:{email}">{email}</a>
  </div>
  <div class="info-block">
    <h3>Instagram</h3>
    <a href="{ig}" target="_blank" rel="noopener">tint_and_sun</a>
  </div>
  <div class="info-block">
    <h3>Work hours</h3>
    <p>Tue &ndash; Sun: 10am &ndash; 7pm<br>Mon: Off</p>
  </div>
  <div class="info-block">
    <h3>Service area</h3>
    <p>Dubai and across the UAE</p>
  </div>
</div>"""


CONTACT_FORM = """<form class="form" novalidate>
  <div class="form__row">
    <div class="field"><input id="f-name" type="text" placeholder=" " required><label for="f-name">Your name</label></div>
    <div class="field"><input id="f-phone" type="tel" placeholder=" "><label for="f-phone">Phone / WhatsApp</label></div>
  </div>
  <div class="form__row">
    <div class="field"><input id="f-email" type="email" placeholder=" " required><label for="f-email">E-mail</label></div>
    <div class="field"><input id="f-loc" type="text" placeholder=" "><label for="f-loc">Property location</label></div>
  </div>
  <div class="field"><textarea id="f-msg" placeholder=" " required></textarea><label for="f-msg">Approximate measurements and your priority: heat, privacy, UV or decoration</label></div>
  <div class="form__ok">Thank you &mdash; we&rsquo;ll be in touch shortly.</div>
  <div class="btn-row" style="margin-top:4px">
    <button class="btn btn--primary" type="submit">Send request</button>
    <a class="btn btn--ghost" href="{wa}" target="_blank" rel="noopener">Send photos on WhatsApp</a>
  </div>
  <p class="form__note">For the fastest quote, send photographs of the glass on WhatsApp. Sample viewings available upon booking.</p>
</form>"""


# --------------------------------------------------------------------------- pages

def home():
    return T("""<section class="hero hero--dark">
  <div class="hero__media"><img src="assets/img/hero.jpg" alt="Contemporary white villa with floor-to-ceiling glazing" fetchpriority="high"></div>
  <div class="wrap hero__inner">
    <div class="hero__content">
      <p class="hero__eyebrow">Tint and Sun &middot; Dubai, UAE</p>
      <h1 class="hero__title">Professional Windows Film Solutions</h1>
    </div>
    <div class="hero__bottom">
      <p class="hero__tags">Heat reduction &bull; Daytime privacy &bull; UV protection &bull; Decorative finishes</p>
      <p class="hero__note">Residential, commercial and specialist installations across the UAE since 2012.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="{{WA}}" target="_blank" rel="noopener">Get free consultation</a>
        <a class="btn btn--ghost-light" href="solar-films.html">Explore films</a>
      </div>
    </div>
  </div>
</section>

{{STATS}}

<section class="section" id="solutions">
  <div class="wrap">
    {{HEAD1}}
    <div class="grid grid--4">
      <a class="photo-tile reveal" href="solar-films.html">
        <img src="assets/img/science.jpg" alt="" loading="lazy">
        <div><p class="eyebrow">01</p><h3>Solar control films</h3><p>Block solar heat, glare and harmful UV rays for a cooler, brighter space.</p><span class="link-arrow">Explore {{ARROW}}</span></div>
      </a>
      <a class="photo-tile reveal" data-delay="80" href="privacy-films.html">
        <img src="assets/img/privacy-outside.jpg" alt="" loading="lazy">
        <div><p class="eyebrow">02</p><h3>Daytime privacy films</h3><p>One-way daytime privacy while retaining your outward views.</p><span class="link-arrow">Explore {{ARROW}}</span></div>
      </a>
      <a class="photo-tile reveal" data-delay="160" href="solar-films.html#transparent">
        <img src="assets/img/transparent.jpg" alt="" loading="lazy">
        <div><p class="eyebrow">03</p><h3>Transparent solar films</h3><p>Virtually clear protection that preserves architectural appearance.</p><span class="link-arrow">Explore {{ARROW}}</span></div>
      </a>
      <a class="photo-tile reveal" data-delay="240" href="decorative.html">
        <img src="assets/img/decor/gradient.jpg" alt="" loading="lazy">
        <div><p class="eyebrow">04</p><h3>Decorative glass films</h3><p>Frosting, gradients, mirror, graphics and architectural wraps.</p><span class="link-arrow">Explore {{ARROW}}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    {{HEAD2}}
    {{TIERS}}
    {{NOTE}}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">About us</p>
        <h2 class="h-section">A trusted Dubai tinting company.</h2>
        <p class="h-sub">Serving the UAE since 2012, Tint and Sun specialises in solar control window films, decorative finishes and customised graphics for vehicles, homes and commercial spaces.</p>
        <p class="h-sub">We combine technical assessment, tailored film selection, precise installation and dedicated warranty support to enhance comfort, privacy and appearance.</p>
        <ul class="sectors">
          <li>{{I_HOUSE}}Residential</li><li>{{I_TOWER}}Commercial</li><li>{{I_FRAME}}Decorative</li><li>{{I_PERSON}}Owner led</li>
        </ul>
        <div class="btn-row">
          <a class="btn btn--primary" href="about.html">Read our story</a>
          <a class="btn btn--ghost" href="contact.html#standards">Our standards</a>
        </div>
      </div>
      <div class="split__media reveal" data-delay="120">
        <img src="assets/img/team1.jpg" alt="Tint and Sun team installing window film on a commercial glass façade from a boom lift" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    {{HEAD3}}
    {{PROJECTS}}
  </div>
</section>

<section class="section">
  <div class="wrap">
    {{HEAD4}}
    {{BRANDS}}
  </div>
</section>""",
        WA=WA, ARROW=ARROW, STATS=STATS, TIERS=tier_cards(), NOTE=TIER_NOTE,
        I_HOUSE=I_HOUSE, I_TOWER=I_TOWER, I_FRAME=I_FRAME, I_PERSON=I_PERSON,
        PROJECTS=project_grid(6), BRANDS=brand_grid(),
        HEAD1=head("Solutions", "Window film for every kind of glass.",
                   "Residential, commercial and specialist installations &mdash; tailored to your priorities.",
                   ("All solutions", "solar-films.html")),
        HEAD2=head("Film tiers", "Three tiers of solar control performance.",
                   "Every tier blocks 99% of UV rays and is available from 0% to 90% VLT.",
                   ("The science behind it", "solar-films.html")),
        HEAD3=head("Our work", "Selected projects.", "", ("View all projects", "projects.html")),
        HEAD4=head("Partners", "World known brands.",
                   "3M, Johnson, LLumar, Armolan, Konica Minolta, Scorpion, Sun Guard and other specialist film brands.",
                   ("Brands we work with", "brands.html")))


def about():
    return page_hero(
        "About us",
        "A trusted Dubai tinting company",
        "Serving the UAE since 2012 &mdash; solar control window films, decorative finishes and customised graphics for vehicles, homes and commercial spaces.",
        "assets/img/hero.jpg",
    ) + "\n\n" + STATS + T("""

<section class="section">
  <div class="wrap">
    <div class="founder">
      <figure class="founder__media reveal">
        <img src="assets/img/founder.jpg" alt="Oksana L., Founder and CEO of Tint and Sun">
        <figcaption><strong>Oksana L.</strong>Founder &amp; CEO<br>Architectural Solar Control Film Expert</figcaption>
      </figure>
      <div class="founder__text reveal" data-delay="100">
        <p class="eyebrow">Our founder</p>
        <h2 class="h-section">Personal accountability on every project.</h2>
        <p>Serving the UAE since 2012, Tint and Sun specialises in solar control window films, decorative finishes and customised graphics for vehicles, homes and commercial spaces.</p>
        <p>We combine technical assessment, tailored film selection, precise installation and dedicated warranty support to enhance comfort, privacy and appearance.</p>
        <p>At the heart of the business is Oksana L., Owner and Solar Control Film Specialist. Progressing from customer care through marketing to managing partner and sole owner, she brings extensive industry experience, technical expertise and personal accountability to every project.</p>
        <p>Her leadership has also developed corporate relationships and staff programmes spanning:</p>
        <ul class="chips">
          <li>Emirates Airlines</li><li>BMW Group Middle East</li><li>Etihad Airways</li><li>Australian Consulate-General Dubai</li>
          <li>American University in Dubai (AUD)</li><li>Neuron LLC</li><li>Dubai Aviation Corporation</li><li>Foilx Custom Workshops</li><li>ULB Fine</li>
        </ul>
        <p>Customer satisfaction and the continued confidence of our partners remain our foremost priorities. This commitment to quality, attentive service and lasting relationships has shaped our reputation across the UAE.</p>
        <p class="lead-strong">Backed by 14 years of UAE experience, we are committed to dependable service, lasting quality and your continued confidence.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What we do</p>
      <h2 class="h-section">Residential, commercial and decorative.</h2>
    </div>
    <div class="grid grid--3">
      <div class="dark-card reveal"><span class="benefit__icon">{{I_HOUSE}}</span><h3>Residential</h3><p>Villas and apartments &mdash; cooler rooms, daytime privacy and protection for furniture and interiors.</p></div>
      <div class="dark-card reveal" data-delay="80"><span class="benefit__icon">{{I_TOWER}}</span><h3>Commercial</h3><p>Offices, clinics, showrooms and façades &mdash; scheduled to minimise disruption to your business.</p></div>
      <div class="dark-card reveal" data-delay="160"><span class="benefit__icon">{{I_FRAME}}</span><h3>Decorative</h3><p>Frosting, bespoke graphics and architectural wraps for privacy, branding and design.</p></div>
    </div>
    <div class="facts reveal">
      <div><strong>Free</strong>site inspection</div>
      <div><strong>Up to 8 years</strong>warranty</div>
      <div><strong>Wide range</strong>of materials from world known brands</div>
    </div>
  </div>
</section>""", I_HOUSE=I_HOUSE, I_TOWER=I_TOWER, I_FRAME=I_FRAME)


SCIENCE_SVG = """<svg class="science__svg" viewBox="0 0 720 330" role="img" aria-label="Diagram: visible light, heat and UV pass straight through plain glass; glass with solar control film lets softened light through while reflecting heat and UV">
  <defs>
    <linearGradient id="gL" x1="0" x2="1"><stop offset="0" stop-color="#f6b73c" stop-opacity=".15"/><stop offset="1" stop-color="#f6b73c"/></linearGradient>
    <linearGradient id="gH" x1="0" x2="1"><stop offset="0" stop-color="#ee7a2a" stop-opacity=".15"/><stop offset="1" stop-color="#ee7a2a"/></linearGradient>
    <linearGradient id="gU" x1="0" x2="1"><stop offset="0" stop-color="#8b6cd1" stop-opacity=".15"/><stop offset="1" stop-color="#8b6cd1"/></linearGradient>
    <marker id="aH" viewBox="0 0 10 10" refX="3" refY="5" markerUnits="userSpaceOnUse" markerWidth="22" markerHeight="22" orient="auto"><path d="M0 0 10 5 0 10z" fill="#ee7a2a"/></marker>
    <marker id="aU" viewBox="0 0 10 10" refX="3" refY="5" markerUnits="userSpaceOnUse" markerWidth="22" markerHeight="22" orient="auto"><path d="M0 0 10 5 0 10z" fill="#8b6cd1"/></marker>
  </defs>
  <g font-family="inherit" font-size="13" font-weight="600" fill="#5b6f7c">
  <!-- left: plain glass, everything passes -->
  <text x="20" y="84">Visible light</text>
  <rect x="20" y="93.0" width="262" height="14" rx="7.0" fill="url(#gL)" opacity="1"/><path d="M280 85l22 15-22 15z" fill="#f6b73c" opacity="1"/>
  <text x="20" y="159">Heat (IR)</text>
  <rect x="20" y="168.0" width="262" height="14" rx="7.0" fill="url(#gH)" opacity="1"/><path d="M280 160l22 15-22 15z" fill="#ee7a2a" opacity="1"/>
  <text x="20" y="234">UV rays</text>
  <rect x="20" y="243.0" width="262" height="14" rx="7.0" fill="url(#gU)" opacity="1"/><path d="M280 235l22 15-22 15z" fill="#8b6cd1" opacity="1"/>
  <path d="M150 52 192 30v262l-42 22z" fill="#e3ebf0" stroke="#9aa6ae" stroke-width="2" opacity=".6"/>
  <text x="171" y="320" text-anchor="middle" font-weight="500" font-size="12" fill="#8b9aa5">Heat, glare and UV come straight in</text>
  <!-- right: filmed glass -->
  <text x="400" y="84">Visible light</text>
  <rect x="400" y="93" width="148" height="14" rx="7" fill="url(#gL)"/>
  <text x="400" y="159">Heat (IR)</text>
  <rect x="400" y="168" width="148" height="14" rx="7" fill="url(#gH)"/>
  <text x="400" y="234">UV rays</text>
  <rect x="400" y="243" width="148" height="14" rx="7" fill="url(#gU)"/>
  <rect x="590" y="95.0" width="78" height="10" rx="5.0" fill="#f6b73c" opacity="0.55"/><path d="M666 89l16 11-16 11z" fill="#f6b73c" opacity="0.55"/>
  <text x="590" y="126" font-size="12" font-weight="500" fill="#8b9aa5">Softer, glare-free light</text>
  <path d="M544 175 490 135" stroke="#ee7a2a" stroke-width="9" stroke-linecap="round" fill="none" marker-end="url(#aH)"/>
  <rect x="590" y="172" width="40" height="6" rx="3" fill="#ee7a2a" opacity=".15"/>
  <text x="590" y="199" font-size="12" font-weight="500" fill="#8b9aa5">Up to 99% heat rejected</text>
  <path d="M544 250 490 210" stroke="#8b6cd1" stroke-width="9" stroke-linecap="round" fill="none" marker-end="url(#aU)"/>
  <rect x="590" y="247" width="40" height="6" rx="3" fill="#8b6cd1" opacity=".15"/>
  <text x="590" y="274" font-size="12" font-weight="500" fill="#8b9aa5">Up to 99% UV blocked</text>
  <path d="M548 52 590 30v262l-42 22z" fill="#6b7c88" stroke="#3d4c56" stroke-width="2"/>
  <path d="M584 33 590 30v262l-6 3z" fill="#3d4c56"/>
  <text x="569" y="320" text-anchor="middle" font-weight="500" font-size="12" fill="#8b9aa5">Film reflects and absorbs</text>
  </g>
</svg>"""


def solar():
    swatches = [("0%", "89%"), ("10%", "92%"), ("15%", "85%"), ("20%", "72%")]
    sw = "".join(
        '<div class="swatch reveal" data-delay="%d"><div class="swatch__glass" style="--tint:%.2f"></div><strong>%s</strong><span>%s VLT</span></div>'
        % (i * 60, 1 - int(v.rstrip('%')) / 100, d, v) for i, (d, v) in enumerate(swatches))
    return page_hero(
        "Solar control films",
        "The Science Behind Your Comfort",
        "How solar control films work: they block solar heat, glare and harmful UV rays, keeping your space cooler, brighter and more comfortable.",
    ) + T("""

<section class="section">
  <div class="wrap">
    <div class="science reveal">
      <div class="science__labels">
        <div><h3>Glass without solar control film</h3><p>Solar energy passes through, causing heat, glare and UV exposure.</p></div>
        <div><h3>Glass with solar control film</h3><p>Film blocks, reflects and absorbs heat, glare and UV rays.</p></div>
      </div>
      {{SVG}}
    </div>
    <div class="grid grid--3 metrics">
      <div class="metric reveal"><span>Visible light <em>(what you see)</em></span><strong>5% &ndash; 95% blocked</strong><p>Reduces glare and controls brightness.</p></div>
      <div class="metric reveal" data-delay="80"><span>Solar heat <em>(IRR)</em></span><strong>Up to 99% blocked</strong><p>Cuts solar heat for a cooler space.</p></div>
      <div class="metric reveal" data-delay="160"><span>UV rays <em>(harmful)</em></span><strong>Up to 99% blocked</strong><p>Blocks harmful UV rays.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    {{HEAD_B}}
    {{BENEFITS}}
  </div>
</section>

<section class="section">
  <div class="wrap">
    {{HEAD_T}}
    {{TIERS}}
    {{NOTE}}
  </div>
</section>

<section class="section section--alt" id="transparent">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Transparent solar control films</p>
        <h2 class="h-section">Exceptional protection, discreetly integrated.</h2>
        <p class="h-sub">An elegant choice for residences and especially commercial properties where preserving architectural appearance is essential.</p>
        <p class="h-sub">Our virtually clear films maintain natural light and open views with minimal visible change to interiors or façades, while blocking 99% of UV rays and delivering up to 96% infrared rejection (IRR), depending on the film selected.</p>
      </div>
      <div class="split__media reveal" data-delay="120"><img src="assets/img/transparent.jpg" alt="Clear floor-to-ceiling glass overlooking the Dubai skyline" loading="lazy"></div>
    </div>
    <div class="swatches swatches--4">{{SW}}</div>
  </div>
</section>""", SVG=SCIENCE_SVG, BENEFITS=benefits(), TIERS=tier_cards(), NOTE=TIER_NOTE, SW=sw,
        HEAD_B=head("Benefits", "Comfort you can feel."),
        HEAD_T=head("Film types", "HP, Ceramic and Nano-Ceramic.",
                    "Choose the tier that matches your heat, privacy and budget priorities."))


def privacy():
    shades = [("30%", "70%"), ("50%", "50%"), ("60%", "40%"), ("70%", "30%"),
              ("80%", "20%"), ("90%", "10%"), ("95%", "0.5%")]
    sw = "".join(
        '<div class="swatch reveal" data-delay="%d"><div class="swatch__glass" style="--tint:%.3f"></div><strong>%s</strong><span>%s VLT</span></div>'
        % (i * 50, 1 - float(v.rstrip('%')) / 100, d, v) for i, (d, v) in enumerate(shades))
    return page_hero(
        "Daytime privacy films",
        "Daytime One-side Privacy Films",
        "Enjoy enhanced daytime privacy while retaining outward views. Available in HP, Ceramic and Nano-Ceramic films, with a choice of shades and infrared rejection (IRR) levels.",
    ) + T("""

<section class="section">
  <div class="wrap">
    <div class="compare">
      <figure class="compare__item reveal"><img src="assets/img/privacy-outside.jpg" alt="Villa from outside — tinted glass appears dark and private" loading="lazy"><figcaption>Outside</figcaption></figure>
      <figure class="compare__item reveal" data-delay="100"><img src="assets/img/privacy-inside.jpg" alt="View from inside the villa — clear outward view to the pool and garden" loading="lazy"><figcaption>Inside</figcaption></figure>
    </div>
    <p class="callout reveal">Privacy is strongest when the exterior is brighter than the interior; curtains or blinds are needed at night when indoor lights are on.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    {{HEAD}}
    <div class="swatches">{{SW}}</div>
    <p class="form__note reveal" style="margin-top:24px">Note: final appearance may vary depending on glass type, exterior lighting and interior lighting.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {{HEAD_T}}
    {{TIERS}}
  </div>
</section>""", SW=sw, TIERS=tier_cards(),
        HEAD=head("Daylight privacy tint shades", "Choose your shade.",
                  "Explore our range of tinted films for one-way daytime privacy."),
        HEAD_T=head("Available in every tier", "Privacy with performance.",
                    "Pick the shade you like, then the heat rejection level that suits you."))


def decorative():
    items = [
        ("frosted.jpg", "White matt frosted film", "Soft, elegant privacy for bathrooms, offices and meeting rooms."),
        ("blackout.jpg", "Black out film", "Complete light and view blocking where full opacity is needed."),
        ("gradient.jpg", "Gradient film", "A graduated frost for privacy at eye level with light above."),
        ("mirror.jpg", "Mirror film", "Reflective finish for a striking, private façade."),
        ("sticker.jpg", "Customized sticker", "Bespoke graphics and branding cut to your design."),
        ("wrap.jpg", "Interior wraps film", "Architectural wraps that refresh surfaces without replacement."),
    ]
    cards = "".join(
        '<figure class="decor reveal" data-delay="%d"><img src="assets/img/decor/%s" alt="%s example" loading="lazy"><figcaption><h3>%s</h3><p>%s</p></figcaption></figure>'
        % (i % 3 * 80, f, t, t, d) for i, (f, t, d) in enumerate(items))
    return page_hero(
        "Decorative glass films",
        "Decorative Glass Films",
        "Transform glass and interior surfaces with tailored solutions for privacy, branding and design. From elegant frosting and bespoke graphics to architectural wraps, we enhance existing spaces without the need for full replacement.",
    ) + """

<section class="section">
  <div class="wrap">
    <div class="decor-grid">%s</div>
  </div>
</section>""" % cards


def brands():
    return page_hero(
        "Brands",
        "Brands we work with",
        "Quality begins with the materials we select. We work with specialist film brands to offer solutions tailored to each project&rsquo;s performance, appearance and budget requirements.",
    ) + """

<section class="section">
  <div class="wrap">
    <div class="split split--text">
      <p class="reveal">Our expertise connects the right product with precise installation and dependable aftercare &mdash; giving you confidence in both the material and the team behind it.</p>
      <p class="reveal" data-delay="80">Throughout our 14-year journey in the UAE, we have worked with these and other specialist brands, selecting films according to each client&rsquo;s preferences, desired finish, performance requirements and glass type. Our experience ensures every recommendation balances appearance, comfort and technical suitability.</p>
    </div>
    <div style="margin-top:clamp(32px,4vw,56px)">%s</div>
  </div>
</section>""" % brand_grid()


def projects():
    return page_hero(
        "Projects",
        "Selected Projects",
        "Clinics, showrooms, shopfronts, offices and villas across Dubai and the UAE &mdash; a selection of our window film installations.",
    ) + """

<section class="section">
  <div class="wrap">%s</div>
</section>""" % project_grid()


def contact():
    return page_hero(
        "Contact",
        "Let&rsquo;s find the right solution for your glass.",
        "Get a free consultation by WhatsApp &mdash; or visit us at TAHA Business Center, Al Quoz 3, Dubai. Tue&ndash;Sun, 10am&ndash;7pm.",
    ) + T("""

<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <div class="reveal">{{INFO}}</div>
      <div class="reveal" data-delay="100">
        <div class="sendus">
          <h3>Send us</h3>
          <ul class="checklist">
            <li>Property location</li>
            <li>Photographs of the glass</li>
            <li>Approximate measurements</li>
            <li>Your priority: heat, privacy, UV or decoration</li>
          </ul>
        </div>
        {{FORM}}
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="standards">
  <div class="wrap">
    {{HEAD}}
    {{STEPS}}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="map reveal">
      <iframe title="Tint and Sun office, Al Quoz 3, Dubai" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=TAHA%20Business%20Center%20Al%20Quoz%203%20Dubai&output=embed"></iframe>
    </div>
  </div>
</section>""", INFO=CONTACT_INFO, FORM=CONTACT_FORM, STEPS=steps(),
        HEAD=head("Our standards", "5 steps to perfection.", "What to expect when you work with us."))


PAGES = [
    ("index.html", "Window Film Solutions Dubai | Tint and Sun",
     "Professional window film solutions in Dubai: heat reduction, daytime privacy, UV protection and decorative finishes since 2012.", home),
    ("about.html", "About Us | Tint and Sun Dubai",
     "A trusted Dubai tinting company since 2012, led by founder Oksana L., architectural solar control film expert.", about),
    ("solar-films.html", "Solar Control Window Films | Tint and Sun Dubai",
     "How solar control films work: HP, Ceramic and Nano-Ceramic films blocking up to 99% heat and UV. Transparent films with up to 96% IRR.", solar),
    ("privacy-films.html", "Daytime Privacy Window Films | Tint and Sun Dubai",
     "One-side daytime privacy films in shades from 70% to 0.5% VLT, available in HP, Ceramic and Nano-Ceramic.", privacy),
    ("decorative.html", "Decorative Glass Films | Tint and Sun Dubai",
     "Frosted, blackout, gradient, mirror, custom sticker and interior wrap films for privacy, branding and design.", decorative),
    ("brands.html", "Brands We Work With | Tint and Sun Dubai",
     "Specialist window film brands: 3M, LLumar, Konica Minolta, Johnson, SunGard, Avery, SunTek, Metamark and more.", brands),
    ("projects.html", "Selected Projects | Tint and Sun Dubai",
     "Selected window film projects across Dubai: clinics, showrooms, shopfronts, offices and villas.", projects),
    ("contact.html", "Contact | Tint and Sun Dubai",
     "Free consultation: TAHA Business Center office 303 B, Al Quoz 3, Dubai. Tel/WhatsApp +971 55 386 54 54.", contact),
]


def main():
    fmt = dict(phone=PHONE, phone_tel=PHONE_TEL, wa=WA, email=EMAIL, ig=IG,
               icon_phone=ICON_PHONE, wa_svg=WA_SVG)
    cta = CTA_BAND.format(**fmt)
    footer = FOOTER.format(**fmt)

    for filename, title, desc, builder in PAGES:
        header = HEADER.format(nav=nav_html(filename), drawer=drawer_html(filename), **fmt)
        body = builder()
        for k in ("wa", "email", "phone_tel", "phone", "ig"):
            body = body.replace("{%s}" % k, fmt[k])
        html = PAGE.format(
            head=HEAD.format(title=title, desc=desc),
            header=header, body=body, cta=cta, footer=footer)
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", filename)


if __name__ == "__main__":
    main()
