"""Generates the five door pages and the thanks page for designlab.fyi."""
import html, json, pathlib, sys

ROOT = pathlib.Path(sys.argv[1])
BOOKING = "https://calendar.proton.me/bookings#ZeXGK9n2clESe2hDfISa7DX1Gpitlw_yBewjGOE4DZk="
PRICE = "$49 a month for the whole firm"
TEST, COHORT, VARIANT = "door-v1", "architecture", "a"

DOORS = [
    dict(slug="billing", name="Billing",
         title="Billing for architecture firms: phase invoices and payment follow-up",
         desc="Send phase invoices on schedule, follow up on late payments, and see which fees are running over. Made for architecture firms of 1 to 20 people.",
         h1="Bill every phase on time, and get paid without chasing.",
         lead="Set up each project's fee once. Invoices go out on schedule, late payers get reminders, and you see when a phase is eating its fee before it's gone.",
         features=[
             ("Phase invoices that send themselves", "Enter the fee by phase and percent complete. Invoices go out on your billing day through QuickBooks or Xero."),
             ("Late payment follow-up", "Polite reminders at 7, 14 and 30 days past due, in your voice. You see who owes what without opening a spreadsheet."),
             ("Retainers applied automatically", "Collect a retainer at signing and credit it against the final invoice, so nobody has to remember."),
             ("Consultant pass-through billing", "Bill structural, MEP and other consultant invoices to the client with your markup, and see when they're paid."),
             ("Reimbursables on the invoice", "Printing, travel and permit fees get tagged to the project and added to the next invoice."),
             ("Fee alerts", "A short weekly email: which phases have used more fee than the work they've finished."),
             ("Change requests priced before you start", "Turn a client's \"can we also...\" email into a priced additional-services approval they sign before you do the work."),
         ]),
    dict(slug="records", name="Records",
         title="License, renewal and sign-off tracking for architecture firms",
         desc="Track licenses, continuing education, firm registrations, sealed sets and client sign-offs in one place. Made for architecture firms of 1 to 20 people.",
         h1="Every license, renewal and sign-off, on record.",
         lead="One place for the deadlines and paper trail a practice has to keep. You get reminded before something lapses, and you can find the record when someone asks.",
         features=[
             ("License and continuing education tracker", "Every architect's licenses, by state, with renewal dates and the education hours each one still needs."),
             ("Firm registrations by state", "Certificates of authorization and firm registrations, with renewal reminders before they lapse."),
             ("Seal register", "A log of which drawings were sealed, by whom, and which set went out. Useful when a question comes up years later."),
             ("Consultant insurance certificates", "Collect certificates from consultants and get a reminder before one expires."),
             ("Drawing transmittal log", "Which set went to whom, and when. Searchable, without digging through email."),
             ("Client decision log", "Clients approve decisions from a link, and each approval is saved with a date. A clear record if there's a dispute later."),
         ]),
    dict(slug="construction", name="Site",
         title="Client and construction tools for small architecture firms",
         desc="Client selections, status updates, site reports, bid comparison, RFIs and punch lists in one simple tool. Made for architecture firms of 1 to 20 people.",
         h1="Keep clients and contractors on the same page, from selections to punch list.",
         lead="The back-and-forth with clients and contractors, in one place a small firm can actually keep up with. Lighter than the tools built for general contractors.",
         features=[
             ("Selections portal", "Residential clients pick finishes and fixtures, see them against the allowance, and approve them online."),
             ("Client status updates", "A short update for each client, drafted from where the project stands, ready for you to send."),
             ("Site visit reports", "Take photos and notes on your phone at the site. They become a formatted report for the client and contractor."),
             ("Bid comparison", "Collect contractor bids in one format and compare them line by line."),
             ("RFI and submittal log", "Track questions and submittals from the contractor, with due dates. Sized for a small firm."),
             ("Punch list with sign-off", "Walk the site, list what's left, and get the contractor's sign-off when each item is done."),
         ]),
    dict(slug="new-work", name="Leads",
         title="Find public architecture projects and RFPs for small firms",
         desc="A weekly list of public architecture projects sized for small firms, plus help filling in qualification forms. Made for architecture firms of 1 to 20 people.",
         h1="Find public projects that fit your firm, and apply faster.",
         lead="Cities, school districts and agencies post small architecture projects on hundreds of separate sites. Get the ones that fit you in one weekly email, and reuse your project write-ups when you apply.",
         features=[
             ("Weekly public RFP list", "Requests for proposals and qualifications sized for small firms, filtered by your region and project types."),
             ("Qualification forms from your records", "Fill in forms like the federal SF330 from project descriptions and team details you've already written."),
             ("Inquiry screening", "Website and Houzz inquiries answer a few questions about budget and timing before you spend time on a call."),
             ("Lead source tracking", "See which channels bring in the clients who actually sign."),
             ("Proposal to contract to invoice", "A signed proposal becomes the contract and the billing schedule, without retyping."),
         ]),
    dict(slug="benchmarks", name="Benchmarks",
         title="Fee and hours benchmarks for small architecture firms",
         desc="See how many hours each phase really takes, price new projects from your past ones, and compare fees with other small firms. Made for architecture firms of 1 to 20 people.",
         h1="Price your next project from what your past ones actually took.",
         lead="Know how many hours each phase really took on your past projects, and how your fees compare with other small firms, before you send the next proposal.",
         features=[
             ("Hours estimator for proposals", "Estimates hours and fee by phase for a new project, based on similar projects you've done."),
             ("Automatic timesheets", "Time is logged from your CAD and Revit file activity, so the data exists even if nobody fills in a timesheet."),
             ("Fee benchmarks from small firms", "What share of the fee each phase takes at firms like yours, pooled anonymously from members."),
             ("Billing rate benchmarks", "Hourly rates and salaries at small firms in your region, pooled anonymously from members."),
         ]),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Design Lab</title>
  <meta name="description" content="{desc}" />
{extra_head}
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="/assets/favicon-180.png" />
  <link rel="preload" href="/assets/fonts/archivo-variable.woff2" as="font" type="font/woff2" crossorigin />
  <link href="/css/styles.css" rel="stylesheet" />
  <link href="/css/site.css" rel="stylesheet" />
</head>
<body>
  <a class="visually-hidden-focusable" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="wrap">
      <a class="wordmark" href="/">Design Lab</a>
{header_btn}
    </div>
  </header>
"""

FOOT = """
  <footer class="wrap site-foot">
    <div class="title-block">
      <div class="tb-name"><span class="wordmark">Design Lab</span><br><span class="pencil">Tools for small architecture firms</span></div>
      <div><small>Office</small>Design Strategy Lab LLC<br>New York</div>
      <div><small>Contact</small>hello@designlab.fyi</div>
      <div><small>Privacy</small><a href="/privacy/">How we handle your data</a></div>
      <div><small>Issued</small>2026</div>
    </div>
  </footer>
{script}</body>
</html>
"""

FORM_SCRIPT = """  <script>
    (function () {
      var f = document.getElementById('join-form');
      if (!f) return;
      f.t.value = Date.now();
      var q = new URLSearchParams(location.search);
      ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) { if (q.get(k)) f[k].value = q.get(k); });
      if (document.referrer && document.referrer.indexOf(location.host) === -1) f.ref.value = document.referrer;
      var err = q.get('error');
      if (err) {
        var box = document.getElementById('join-error');
        box.textContent = err === 'email' ? 'That email address doesn\\'t look right. Please check it and try again.' : 'Something went wrong on our end. Please try again, or email hello@designlab.fyi.';
        box.hidden = false;
      }
    })();
  </script>
"""


# ---------- UI mockups, one per feature (keyed by feature heading) ----------
# Elements: ("row", label, value, tag, tag_style, sub) / ("total", label, value)
# ("bar", label, right_text, used_pct, done_pct, over) / ("note", text) / ("btn", text)
# ("photos", n) / ("check", text, done) / ("search", text)
def R(label, value="", tag=None, style="", sub=None): return ("row", label, value, tag, style, sub)

MOCKS = {
    # Billing
    "Phase invoices that send themselves": ("Invoice 1042", "Lin residence", [
        R("Design development", "$10,800", sub="60% of $18,000"),
        R("Previously billed", "-$7,200"),
        ("total", "This invoice", "$3,600"),
        ("btn", "Send Nov 1 via QuickBooks")]),
    "Late payment follow-up": ("Overdue", "3 invoices", [
        R("Hollis Cafe", "$4,200", "Final reminder", "red", "32 days late"),
        R("Park St. ADU", "$2,950", "2nd reminder", "", "15 days late"),
        R("Lin residence", "$3,600", "1st reminder", "", "8 days late")]),
    "Retainers applied automatically": ("Final invoice", "Ortega house", [
        R("Construction administration", "$7,140"),
        R("Retainer collected Mar 4", "-$5,000", "Applied", "ink"),
        ("total", "Amount due", "$2,140")]),
    "Consultant pass-through billing": ("Consultants", "Lin residence", [
        R("Aria Engineering", "$3,520", "Paid", "ink", "Structural, $3,200 + 10%"),
        R("Northline", "$2,695", "Billed", "", "MEP, $2,450 + 10%"),
        R("Grade Civil", "$1,210", "Not billed", "muted", "Civil, $1,100 + 10%")]),
    "Reimbursables on the invoice": ("Reimbursables", "October", [
        R("Plot prints, permit set", "$86"),
        R("Permit filing fee", "$450"),
        R("Site visit mileage", "$28", sub="42 miles"),
        ("note", "Added to invoice 1043")]),
    "Fee alerts": ("Fee alerts", "Week of Oct 26", [
        ("bar", "Hollis Cafe, DD", "82% used, 50% done", 82, 50, True),
        ("bar", "Lin residence, CD", "40% used, 45% done", 40, 45, False),
        ("bar", "Park St. ADU, SD", "65% used, 60% done", 65, 60, False)]),
    "Change requests priced before you start": ("Change request", "Ortega house", [
        ("note", "“Can we also look at a screened porch on the north side?”"),
        R("Additional services", "$2,450", sub="Estimate: 14 hours"),
        ("btn", "Send for approval")]),
    # Records
    "License and continuing education tracker": ("Licenses", "J. Ortega", [
        R("New Jersey", "Renews Feb 2027", "12 h needed", "red"),
        R("New York", "Renews Jun 2027", "6 h needed"),
        R("Connecticut", "Renews Jan 2028", "Done", "ink")]),
    "Firm registrations by state": ("Firm registrations", "3 states", [
        R("New Jersey", "Expires Dec 2026", "Renew now", "red"),
        R("New York", "Expires Mar 2027"),
        R("Connecticut", "Expires Jan 2028")]),
    "Seal register": ("Seal register", "Lin residence", [
        R("Permit set, A-101 to A-501", "Oct 3", sub="Sealed by J. Ortega"),
        R("Structural revision 2", "Oct 17", sub="Sealed by Aria Engineering"),
        R("Bid set", "Aug 28", sub="Sealed by J. Ortega")]),
    "Consultant insurance certificates": ("Insurance certificates", "4 consultants", [
        R("Aria Engineering", "Nov 15", "Expiring", "red", "General liability"),
        R("Northline", "Apr 2027", "On file", "", "Professional liability"),
        R("Grade Civil", "Missing", "Requested", "muted")]),
    "Drawing transmittal log": ("Transmittals", "All projects", [
        ("search", "Search sets, people, dates"),
        R("Permit set to building dept.", "Oct 3", sub="Lin residence"),
        R("DD set to client", "Sep 12", sub="Hollis Cafe"),
        R("Bid set to 3 contractors", "Aug 30", sub="Ortega house")]),
    "Client decision log": ("Decisions", "Lin residence", [
        R("Kitchen layout B", "Oct 2, 4:12 pm", "Approved", "ink"),
        R("Stair railing, steel", "Sep 20, 9:05 am", "Approved", "ink"),
        R("Window package", "Sent Oct 24", "Waiting", "muted"),
        ("btn", "Send for approval")]),
    # Construction
    "Selections portal": ("Selections", "Ortega house", [
        R("Kitchen faucet", "$640", "Over", "red", "Allowance $500"),
        R("Bath 2 tile", "$1,800", "Approved", "ink", "Allowance $2,000"),
        R("Pendant lights", "$720", "Waiting", "muted", "Allowance $900"),
        ("btn", "Approve selections")]),
    "Client status updates": ("Draft update", "To: the Lins", [
        ("note", "Construction documents are about halfway done. We expect to submit for permit the week of Nov 16. Next decision from you: the window package."),
        ("btn", "Send")]),
    "Site visit reports": ("Site visit 4", "Oct 24", [
        ("photos", 4),
        R("Framing at stair opening", "", "Fix", "red"),
        R("Window rough openings", "", "OK"),
        ("btn", "Send report")]),
    "Bid comparison": ("Bids", "Hollis Cafe", [
        R("Fieldstone", "$389,000", "Excludes HVAC", "red"),
        R("Bayside Builders", "$412,000"),
        R("Corner & Sons", "$438,500"),
        ("note", "Compared line by line across 14 divisions")]),
    "RFI and submittal log": ("RFIs and submittals", "Lin residence", [
        R("RFI 07, beam pocket depth", "Due Oct 30", "Overdue", "red"),
        R("RFI 08, tile substrate", "Due Nov 2", "Open"),
        R("Submittal 12, windows", "Oct 21", "Approved", "ink")]),
    "Punch list with sign-off": ("Punch list", "Ortega house", [
        ("check", "Touch up paint, stair wall", True),
        ("check", "Adjust door 104 closer", True),
        ("check", "Replace cracked tile, bath 2", False),
        R("Contractor sign-off", "2 of 3")]),
    # New work
    "Weekly public RFP list": ("This week", "6 matches", [
        R("Library renovation", "Due Nov 20", sub="Town of Ashford, est. $2M"),
        R("Fire station study", "Due Dec 4", sub="Village of Glen Park"),
        R("School ADA upgrades", "Due Nov 28", sub="Riverside School District")]),
    "Qualification forms from your records": ("SF330, Part II", "Draft", [
        R("Firm details", "", "Filled", "ink"),
        R("Key personnel", "4 of 4", "Filled", "ink"),
        R("Example projects", "3 of 5", "In progress"),
        ("btn", "Fill from your projects")]),
    "Inquiry screening": ("New inquiry", "From your website", [
        R("Project", "Kitchen and bath"),
        R("Budget", "$60,000 to $80,000"),
        R("Start", "Spring 2027", "Good fit", "ink"),
        ("btn", "Book a call")]),
    "Lead source tracking": ("Where clients come from", "Last 12 months", [
        R("Referrals", "4 signed", sub="6 inquiries"),
        R("Website", "2 signed", sub="5 inquiries"),
        R("Houzz", "1 signed", sub="14 inquiries")]),
    "Proposal to contract to invoice": ("Ortega house", "", [
        R("Proposal signed", "Oct 1", "Done", "ink"),
        R("Contract created", "Oct 1", "Done", "ink"),
        R("Billing schedule", "5 phases, $64,000", "Ready"),
        ("btn", "Send first invoice")]),
    # Benchmarks
    "Hours estimator for proposals": ("Estimate", "3,200 sq ft house", [
        R("Schematic design", "90 h"),
        R("Design development", "140 h"),
        R("Construction documents", "260 h"),
        ("note", "Based on 4 similar past projects")]),
    "Automatic timesheets": ("Today", "Logged from your files", [
        R("Lin residence", "2 h 40 m", sub="Revit"),
        R("Hollis Cafe", "1 h 15 m", sub="AutoCAD"),
        R("Ortega house", "35 m", sub="Revit"),
        ("btn", "Confirm day")]),
    "Fee benchmarks from small firms": ("Share of fee by phase", "You vs. firms your size", [
        ("bar", "Construction documents", "You 46%, median 40%", 46, 40, True),
        ("bar", "Design development", "You 18%, median 20%", 18, 20, False),
        ("bar", "Construction administration", "You 14%, median 18%", 14, 18, False)]),
    "Billing rate benchmarks": ("Hourly rates", "Firms of 1 to 20, Northeast", [
        R("Principal", "$185", "Median $175", "muted"),
        R("Project architect", "$135", "Median $140", "muted"),
        R("Designer", "$95", "Median $100", "muted")]),
}

def render_mock(spec):
    title, meta, items = spec
    out = []
    for it in items:
        k = it[0]
        if k == "row":
            _, label, value, tag, style, sub = it
            lab = e(label) + (f'<span class="ui-sub">{e(sub)}</span>' if sub else "")
            tg = f'<span class="ui-tag {style}">{e(tag)}</span>' if tag else ""
            out.append(f'<div class="ui-row"><span>{lab}</span><span class="v">{e(value)}{tg}</span></div>')
        elif k == "total":
            out.append(f'<div class="ui-row total"><span>{e(it[1])}</span><span class="v">{e(it[2])}</span></div>')
        elif k == "bar":
            _, label, right, used, done, over = it
            cls = "fill over" if over else "fill"
            rcls = ' class="red"' if over else ""
            out.append(f'<div class="ui-barrow"><div class="ui-meta"><span>{e(label)}</span><span{rcls}>{e(right)}</span></div>'
                       f'<div class="ui-bar"><span class="{cls}" style="width:{used}%"></span><span class="tick" style="left:{done}%"></span></div></div>')
        elif k == "note":
            out.append(f'<div class="ui-note">{e(it[1])}</div>')
        elif k == "btn":
            out.append(f'<span class="ui-btn">{e(it[1])}</span>')
        elif k == "photos":
            out.append('<div class="ui-photos">' + "<i></i>" * it[1] + "</div>")
        elif k == "check":
            out.append(f'<div class="ui-check{" done" if it[2] else ""}">{e(it[1])}</div>')
        elif k == "search":
            out.append(f'<div class="ui-search">{e(it[1])}</div>')
    head = f'<div class="ui-head"><b>{e(title)}</b><span>{e(meta)}</span></div>'
    return f'<div class="ui">{head}<div class="ui-body">{"".join(out)}</div></div>'


def e(s):
    return html.escape(s, quote=True)

def door(d):
    url = f"https://designlab.fyi/architecture/{d['slug']}/"
    extra = f"""  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Design Lab" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{e(d['h1'])}" />
  <meta property="og:description" content="{e(d['desc'])}" />"""
    btn = '      <a class="btn btn-outline btn-sm" href="#join">Get early access</a>'
    feats = "\n".join(
        f"""          <li>
            <div class="plate" aria-hidden="true">{render_mock(MOCKS[h])}</div>
            <h3>{e(h)}</h3>
            <p>{e(p)}</p>
          </li>""" for h, p in d["features"])
    body = f"""
  <main id="main">
    <section class="hero">
      <div class="wrap">
        <p class="for-whom">Design Lab {e(d['name'])}, for architecture firms of 1 to 20 people</p>
        <h1>{e(d['h1'])}</h1>
        <p class="lead">{e(d['lead'])}</p>
        <div class="cta">
          <a class="btn btn-primary btn-block" href="#join">Get early access</a>
          <p>{PRICE}. No demo or sales call.</p>
        </div>
      </div>
    </section>

    <section class="block block-flush-top" aria-labelledby="features-h">
      <div class="wrap">
        <h2 id="features-h">What it does</h2>
        <ul class="features">
{feats}
        </ul>
      </div>
    </section>

    <section class="block" id="join" aria-labelledby="join-h">
      <div class="wrap">
        <div class="trace">
          <h2 id="join-h">Get early access to Design Lab {e(d['name'])}</h2>
          <ul class="terms">
            <li><b>{PRICE}</b>, any number of people</li>
            <li><b>No demo or sales call</b> to get started</li>
            <li><b>Cancel any time</b></li>
          </ul>
          <form class="door-form" id="join-form" method="post" action="/join/submit.php">
            <label for="email">Work email</label>
            <input type="email" id="email" name="email" required autocomplete="email" placeholder="you@yourfirm.com" />
            <div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off" /></label></div>
            <input type="hidden" name="page" value="{d['slug']}" />
            <input type="hidden" name="cohort" value="{COHORT}" />
            <input type="hidden" name="test" value="{TEST}" />
            <input type="hidden" name="variant" value="{VARIANT}" />
            <input type="hidden" name="return" value="/architecture/{d['slug']}/" />
            <input type="hidden" name="utm_source" value="" />
            <input type="hidden" name="utm_medium" value="" />
            <input type="hidden" name="utm_campaign" value="" />
            <input type="hidden" name="ref" value="" />
            <input type="hidden" name="t" value="" />
            <p class="form-error" id="join-error" role="alert" hidden></p>
            <button class="btn btn-primary btn-block" type="submit">Get early access</button>
            <p class="fine">We'll only use your email for Design Lab {e(d['name'])}. <a href="/privacy/">Privacy</a></p>
          </form>
        </div>
      </div>
    </section>
  </main>
"""
    page = HEAD.format(title=e(d["title"]), desc=e(d["desc"]), extra_head=extra, header_btn=btn) + body + FOOT.format(script=FORM_SCRIPT)
    out = ROOT / "architecture" / d["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return out

def thanks():
    names = {d["slug"]: d["name"] for d in DOORS}
    extra = '  <meta name="robots" content="noindex" />'
    body = f"""
  <main id="main">
    <section class="hero">
      <div class="wrap">
        <h1>You're on the list.</h1>
        <p class="lead"><span id="product">Design Lab</span> is still being built. We're opening it to a small group of firms first, and we'd like to shape it around how you work.</p>
        <p class="lead">If you have 15 minutes, tell us what you'd use it for first. Founding firms get the first invites.</p>
        <div class="cta">
          <a class="btn btn-primary btn-block" href="{BOOKING}">Book a 15-minute call</a>
          <p>Rather write? hello@designlab.fyi</p>
        </div>
      </div>
    </section>
  </main>
"""
    script = f"""  <script>
    (function () {{
      var names = {json.dumps(names)};
      var p = new URLSearchParams(location.search).get('p');
      if (names[p]) document.getElementById('product').textContent = 'Design Lab ' + names[p];
    }})();
  </script>
"""
    page = HEAD.format(title="You're on the list", desc="Thanks for signing up for early access.", extra_head=extra, header_btn="") + body + FOOT.format(script=script)
    out = ROOT / "join" / "thanks" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return out

for d in DOORS:
    print(door(d))
print(thanks())
