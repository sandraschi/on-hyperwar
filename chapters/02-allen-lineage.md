# II. Allen 2016–2024: What Survived Contact

**Status:** Draft 2026-09-09 (non-normative prose; facts cited inline).

## The doctrine before the models and before the war

In 2016, General John R. Allen — former commander of the International
Security Assistance Force in Afghanistan, former commander of United States
forces in the Middle East, and subsequently president of the Brookings
Institution — began writing about the future of combat with technologist Amir
Husain.

Their initial papers, published in the *United States Naval Institute
Proceedings* in 2017 under the title "On Hyperwar," and expanded in their 2019
book *Hyperwar: Conflict and Competition in the AI Century*, introduced a word
that the defense establishment has repeated ever since.

Allen and Husain did not argue that future wars would simply feature better
munitions, higher hypersonic velocities, or stealthier airframes. Their
thesis was structural:

> War was approaching an operational inflection point where the limiting factor
> on the battlefield would cease to be weapon range, explosive yield, or armor
> thickness, and become **the biological latency of human cognition**.

They defined hyperwar as algorithmic warfare: conflict waged at machine speed,
where artificial intelligence systems ingest sensor streams, identify
targets, calculate firing solutions, coordinate distributed strikes, and
execute combat maneuvers in fractions of a second. The traditional Boyd cycle
— Observe, Orient, Decide, Act (the OODA loop) — which had governed military
doctrine for half a century, was about to be compressed from minutes and
seconds into milliseconds.

In Allen’s formulation, human beings would transition rapidly from active
directors of tactical action to supervisors of autonomous swarms, operating
in high-velocity "human-machine teams." In their 2024 revised edition, Allen
and Husain added analyses of large language models, computer vision, and
generative planning, arguing that modern foundation models would serve as the
connective tissue of joint all-domain command and control.

Their directional intuition was entirely correct. Their specific operational
assumptions, however, were annihilated the moment their theory encountered an
actual peer land war.

Between 2022 and 2026, the battlefields of eastern Ukraine ran the empirical
experiment that General Allen could only model in think-tank wargames. The
results of that experiment confirm hyperwar's central prediction while
inverting virtually every institutional assumption on which Western defense
planning was built.

---

## What the war confirmed: The supremacy of the clock

The four-year crucible of the Russia-Ukraine war verified Allen’s primary
thesis with brutal mathematical clarity: **the clock speed is the weapon.**

In modern peer conflict, the combatant with the faster adaptation cycle
consistently destroys the combatant with the superior doctrinal manual. The
adaptation cycle between Ukrainian drone forces and Russian electronic warfare
units did not unfold across the five-year timelines of Western defense
acquisition programs. It unfolded on a **weekly tit-for-tat cadence**:

![The weekly combat adaptation cycle: field, jam, shift, sweep, fiber — then the next cycle](fig/weekly-cycle.svg)

No procurement committee can write a Statement of Work, solicit competitive
bids, conduct developmental testing, and award a cost-plus contract at that
speed. The traditional military-industrial acquisition apparatus is designed
to produce exquisite platforms over decades. It assumes a stationary adversary.
Against an adversary that modifies software weights, changes radio frequencies,
and alters gimbal dynamics every seven days, an acquisition process that
measures latency in years is not just slow; it is functionally dead.

Allen predicted that algorithmic speed would dominate tactical engagements.
The frontline demonstrated that algorithmic speed dominates tactical
*evolution*. The loop that matters is not merely sensor-to-shooter; it is
casualty-to-patch.

---

## The four empirical inversions

Where Allen and the peacetime defense establishment went wrong was in their
vision of the hardware, the industrial base, and the command hierarchy that
would deliver hyperwar. The war in Ukraine produced four radical inversions:

### 1. The Shenzhen Substrate (Commercial Dual-Use over Defense Primes)
Allen envisioned hyperwar as the product of major state defense programs:
expensive, classified, bespoke military platforms engineered by defense primes
like Lockheed Martin, Northrop Grumman, and BAE Systems.

The actual substrate of hyperwar turned out to be civilian consumer electronics
manufactured in the Pearl River Delta:

* **Airframes:** Off-the-shelf carbon fiber, composite plastics, and molded
  foam manufactured by consumer drone suppliers (DJI-class airframes, hobbyist
  quadcopters, agricultural sprayers).
* **Sensors:** Standard CMOS camera modules mass-produced for automotive
  backup systems, smartphones, and domestic security cameras.
* **Compute:** Commercial edge-AI accelerator modules — specifically the
  NVIDIA Jetson Orin Nano and Orin NX family — designed for commercial robotics
  and industrial automation, delivering 40 to 100 trillion operations per
  second (TOPS) at power envelopes between 10 and 25 watts, available on open
  wholesale markets for several hundred dollars.

The infrastructure of twentieth-century arms control — the International
Traffic in Arms Regulations (ITAR), the Missile Technology Control Regime
(MTCR), and the Wassenaar Arrangement — was designed around specialized
military arsenals. It assumed that weapons of strategic consequence require
rare, specialized materials, dedicated military foundries, and classified
machine tools.

When the primary kill engine of a peer conflict is assembled from consumer
brushless motors, open-source Betaflight flight controllers, and automotive
silicon purchased on Alibaba, arms control regimes written for military
arsenals become completely blind. You cannot embargo the components of
hyperwar without shutting down the global consumer electronics market.

### 2. The Radical Cost Inversion
Twentieth-century military doctrine was governed by the Lanchester power laws,
which implicitly assumed that weapon cost was positively correlated with
combat effectiveness. A cruise missile was an exquisite instrument: a Tomahawk
Block V or a Storm Shadow costs between 1.5 million and 3 million dollars.
Because each munition represented a substantial fraction of a battalion’s
budget, launch authority was rigorously guarded. Releasing a two-million-dollar
missile required target confirmation, collateral damage assessments, legal
review, and the explicit authorization of a flag officer.

The Ukrainian workshop ecosystem inverted this cost structure by two to three
orders of magnitude:

* A one-way FPV attack drone carrying a 1.5-kilogram shaped charge costs
  between $400 and $700.
* A long-range DIY cruise missile (such as the *Liutyi* or *Trembita*),
  capable of navigating over one thousand kilometers into Russian airspace to
  strike oil refineries and ammunition depots in the Moscow oblast, costs
  between $20,000 and $50,000.

This cost inversion broke the command architecture. When a munition costs
$500, holding the release authority at the level of a colonel or brigadier
general is an operational absurdity. Authorization devolves instantly to the
platoon sergeant, the squad leader, and ultimately to the software running on
the ground control tablet.

Cheap weapons make release authority cheap. And cheap release authority does
not pause for human consensus.

### 3. The Physical Pivot (The Spooled Fiber FPV)
Peacetime doctrine assumed that the primary barrier to autonomous tactical
weapons was the electronic warfare environment. Western planners believed that
intense Russian GPS spoofing and radio frequency jamming would isolate
unmanned systems, forcing militaries to choose between retreating or deploying
fully autonomous, uncommunicative killer robots.

The battlefield delivered an answer that no think tank anticipated. In the
summer of 2026, Ukrainian drone teams introduced the mass fielding of
**fiber-spooled FPV drones**.

The engineering was radically simple: an uncrewed airframe carrying a spool
containing ten to fifteen kilometers of hair-thin, weightless optical fiber.
The drone unspools the fiber behind it as it penetrates the battlespace:

* **Zero RF Emission:** The system emits no radio frequency signals, rendering
  direction-finding and electronic counter-surveillance completely ineffective.
* **Immunity to Jamming:** Terawatt-class electronic warfare jammers have zero
  physical impact on photons traveling through glass.
* **Uncompressed Telemetry:** The operator and the onboard edge compute receive
  uncompressed, zero-latency, high-definition video feeds all the way to the
  moment of impact.

The spooled fiber solved the hardest theoretical problem of modern autonomous
warfare — contested communications — by simply rejecting the radio spectrum
entirely. It enabled a hybrid control regime where machine-vision models
perform sub-second terminal guidance while a human operator in a bunker ten
kilometers away maintains a continuous, unjammable visual link.

### 4. The Tactical-to-Strategic Collapse
In classical military doctrine, the battlefield is stratified into three
hermetic levels: tactical, operational, and strategic. Tactical units fought
for trenches; operational headquarters maneuvered divisions; strategic command
targeted national centers of gravity.

Hyperwar collapsed these boundaries into a single continuous plane. A tactical
drone unit operating from a concealed cellar in Kharkiv, utilizing commercial
satellite connectivity and edge AI targeting models, executes direct strikes
against strategic Russian early-warning radar installations (such as the
*Voronezh-DM* over-the-horizon radar sites) and strategic aviation bases two
thousand kilometers away.

Workshop engineering produced strategic effects without passing through
operational headquarters. The decision chain was flattened by the speed of
the software.

---

## What failed in Allen’s framework

When Allen’s published doctrine is compared against the physical record of
2022–2026, two load-bearing assumptions fail:

1. **The Assumption of State Monopoly:** Allen wrote from within the mindset
   of the United States defense establishment, assuming that hyperwar would be
   wielded by sovereign states with structured defense budgets, formal doctrine
   directorates, and unified chains of command. In reality, hyperwar was
   democratized. It was built by decentralized volunteer networks, civic tech
   foundations, and tactical workshops operating on Discord and Signal. State
   ministries of defense were consistently the slowest entities in the
   adaptation loop, often arriving months after tactical units had already
   fielded, tested, and discarded three generations of autonomous software.
2. **The Illusion of the Persistent Human Gate:** Allen assumed that the
   United States and its allies could maintain strict "human-in-the-loop"
   controls through policy directives (such as Department of Defense Directive
   3000.09). This assumption holds only as long as both combatants agree to
   fight at human speeds.

In an existential war of national survival, the moment an adversary fields an
algorithmic terminal strike loop that resolves in 300 milliseconds, any
combatant that mandates a six-second human approval confirmation loses the
artillery piece, the trench, and the crew.

The imperative of physical survival strips away the procedural gate. The
doctrine of the "human-in-the-loop" does not survive contact with an adversary
who has automated the trigger.

---

## What survives: The question Allen left open

What survives Allen’s work is the foundational premise: **hyperwar is
inevitable because latency is fatal.**

What Allen did not provide — and what his military lineage prevented him from
writing — is the ladder of control loss. Allen described how machines would
assist soldiers; he did not describe where the soldier permanently leaves the
equation. He showed how teaming would make armies faster; he did not map the
forty-four rungs through which human command authority becomes a purely
ceremonial fiction.

That is the task of Chapter IV. We turn now from the lineage of military
theory to the observable, physical architecture of the empty battlefield.
