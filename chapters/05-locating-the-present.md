# V. Locating the Present (living, revision-dated)

**Revision date: 2026-09-09.** Update on every dated fact; never rewrite old entries, append. Every claim below carries its date; undated assertions are methodological errors.

`[construction: Figure 5.1 — the referenced FLIR image was never committed. Render from the caption art brief below, or cut.]`
*Figure 5.1: Simulated long-range multispectral FLIR capture of forward positions (Rungs 21–25). Autonomous loitering FPV airframes and quadruped ground sensors loiter over uninhabited parapets. Telemetry bounding boxes indicate automated target acquisition without human line-of-sight.*

## The Placement

As of September 2026, the Ukraine-Russia theater sits squarely in Band II transitioning inexorably into Band III (Rungs 13 through 22). The line between human-guided remote violence and autonomous machine execution is no longer an intellectual debating point; it has dissolved into operational millisecond latencies.

Human approval still nominally gates kinetic release in doctrine manuals and diplomatic briefings, but that gate is functionally an operational fiction. When closing velocities reach 140 km/h and electronic warfare denies the radio-frequency spectrum across entire operational sectors, keeping a human in the guidance loop ensures interception, jamming, or total airframe loss.

The transition from Band II (Assisted) to Band III (Supervised) was not driven by doctrinal foresight. It was forced from below by the physics of counter-measures, the collapse of radio links, and the sheer volume of loitering munitions.

---

## 1. The Fiber-Optic Spool and Spectrum Denial (2025–2026)

The standard model of drone warfare assumed electronic warfare (EW) would remain the decisive asymmetric counter: saturate the 900 MHz, 1.2 GHz, 2.4 GHz, and 5.8 GHz bands, sever the analog or digital video feed, break the control uplink, and drop the munition harmlessly into the chernozem.

By late 2024, Russian and Ukrainian electronic warfare complexes had rendered frontline radio-frequency links intermittently unviable across 10-to-20-kilometer depth belts. The response was not a cessation of strikes, but two rapid parallel mutations:

1. **Physical Spooled Fiber-Optic Links (Fielded Q1 2025–2026):** Micro-coaxial glass fiber spools (10 to 20 km in length, weighing under 1.2 kg) unspool from the rear of the airframe during flight. The physical glass link delivers unjammable, zero-latency 4K digital telemetry back to the dugout and accepts control inputs impervious to EW jammers. Units operating spooled fiber airframes systematically penetrated layered jamming bubbles around command posts and air defense batteries.
2. **Terminal Machine Autonomy (Fielded mid-2025–2026):** Because fiber spools snag on forest canopies, power lines, and sharp debris, the alternative mutation proved far more scalable: edge compute boards (such as Rockchip RV1126 or NVIDIA Jetson Orin Nano modules mounted directly on the drone frame) running lightweight convolutional neural networks. The human pilot navigates the munition toward an approximate sector. Once inside the EW bubble where the video signal deteriorates, the pilot locks a bounding box onto a vehicle or trench line. From that millisecond forward, onboard vision-based auto-tracking drives the flight surfaces. The radio link dies; the strike lands.

The shift is decisive: the human is no longer flying the weapon into the target. The human is delegating terminal tracking to an onboard tensor processor.

---

## 2. DIY Strategic Cruise Missiles: The 1/100th Cost Inversion

In early 2026, Ukrainian deep-strike operations against oil refineries, ammunition depots, and airbases surrounding Moscow demonstrated the complete inversion of strategic strike economics.

A legacy Western long-range cruise munition (such as Storm Shadow, SCALP-EG, or Tomahawk) carries an institutional procurement cost between \$1,800,000 and \$3,200,000 per unit, produced on multi-year delivery cycles governed by defense-prime quality assurance and export clearances. 

The Ukrainian domestic strike inventory (represented by systems like the Liutyi, Bober, and subsequent modular airframes) achieved 1,000-to-1,500-kilometer operational reach using:
- Piston engines commercially sourced from light aviation and drone catalogs (\$8,000–\$15,000).
- Molded fiberglass and carbon-composite airframes fabricated in decentralized light-industrial workshops.
- Multi-constellation GNSS receivers coupled with commercial-grade MEMS inertial measurement units and optical terrain-matching camera feeds.
- Unit cost: \$35,000 to \$80,000 per airframe.

When fifty such airframes are launched in a single coordinated wave toward an oil refinery in the Yaroslavl or Ryazan oblasts, the air defense calculus collapses. Defending a strategic site requires expending interceptor missiles from systems like the S-400 or Patriot PAC-2/PAC-3. A single Patriot interceptor costs between \$4,000,000 and \$5,500,000. An S-400 48N6DM interceptor costs approximately \$2,500,000.

Firing three \$4,000,000 interceptors to destroy three \$40,000 airframes leaves the defender with an \$11,880,000 economic deficit per salvo—and an empty launch canister that requires 18 to 24 months of industrial retooling to reload. If ten airframes slip through because the missile battery runs out of interceptors, a \$500,000,000 catalytic cracking unit is incinerated.

This is not a temporary tactical advantage; it is the mathematical bankruptcy of Cold War air defense architectures.

---

## 3. Quadruped Ground Robotics and the Emptied Trenches (2025–2026)

By early 2026, the forward 5 kilometers of the line of contact had become entirely unlivable for biological infantry. Thermal reconnaissance drones, loitering day and night on overlapping rotational orbits, made any human silhouette walking upright detectable within 90 seconds and targeted within 180 seconds.

Infantry moved entirely subterranean, residing in deeply buried bunkers and communicating through buried wire. In this environment, ground-based robotic systems ceased being speculative science fiction:

```
+-------------------------------------------------------------------------+
|                  FORWARD PERIMETER RECONNAISSANCE                       |
|                                                                         |
|   [Subterranean Dugout]                                                 |
|          | (Buried fiber)                                               |
|   [Surface Antenna / Relay]                                             |
|          | (Short-range encrypted mesh)                                 |
|          +---> [Unitree/Spot-class Quadruped Sensor Platform]           |
|                     - Emplaced in crater lip                            |
|                     - Acoustic sniper triangulation                     |
|                     - Stabilized optical gimbal & thermal sight         |
|                     - 12-hour low-power stationary watch                |
+-------------------------------------------------------------------------+
```

- **Unitree Go2 / B2 and Custom Quadruped Derivatives:** Deployed by Ukrainian units (including the 28th Separate Mechanized Brigade) in trench clearing, forward listening posts, and urban reconnaissance in Toretsk and Chasiv Yar.
- **Weaponized Mountings:** Commercial four-legged chassis outfitted with stabilized recoil-damped mounts carrying Kalashnikov-pattern rifles, anti-tank mines, or explosive breaching charges.
- **Stationary Overwatch:** Quadrupeds walk autonomously into crater lips, sit flat in low-power standby mode for up to 14 hours, and act as silent perimeter alarm trips. When their acoustic microphones detect personnel movement or weapon discharge, they wake their optical turret, transmit targeting coordinates, and return to sleep.

The biological soldier is pushed out of the observation trench entirely. The human remains 800 meters to the rear, staring at a split-screen dashboard.

---

## 4. The UN Volker Türk Reaction and the Denial Pattern (September 2026)

During the week of September 8, 2026, United Nations High Commissioner for Human Rights Volker Türk issued an explicit public warning expressing horror at field reports indicating that fully autonomous lethal drones were operating in active combat zones in Eastern Europe.

The institutional reaction from combatant states adhered strictly to the classic denial pattern:
1. **Public Denial of Lethal Autonomy:** Official military press offices from both Kyiv and Moscow issued prompt statements insisting that all weapons systems remain under strict human control, reiterating adherence to International Humanitarian Law (IHL).
2. **The "Human-in-the-Loop" Fiction:** Where autonomous tracking algorithms and automated terminal homing were documented in captured wreckage and telemetry logs, military spokespersons reframed the mechanism as "operator-assisted guidance" or "automated stabilization."
3. **Operational Reality:** On the zero line, the human operator in the loop has an effective intervention window of 200 to 400 milliseconds before a dive begins. The operator does not aim; the operator merely declines to abort. An approval mechanism that defaults to release unless canceled within 300 milliseconds is an autonomous weapon with an institutional liability buffer.

---

## 5. Empirical Rung Assessment

| Date | Theater Fact / Telemetry | Rung Manifested | Status |
|---|---|---|---|
| **2024-Q3** | Widespread deployment of optical edge-AI tracking on FPV airframes (autotargeting terminal lock). | **Rung 10** (Sensor-Fused Nomination) | Confirmed public telemetry |
| **2025-Q1** | Deployment of spooled-fiber FPV drones up to 15 km to bypass broadband EW jamming belts. | **Rung 11** (Bandwidth-Choked Machine Delegation) | Fielded, captured units cataloged |
| **2025-Q3** | Autonomous quadruped robotics employed in forward trench reconnaissance and acoustic overwatch. | **Rung 16** (Persistent Station-Keeping Hunters) | Video & unit documentation verified |
| **2026-Q1** | Massed DIY long-range composite cruise airframes saturating strategic air defense perimeters. | **Rung 14** (Asymmetric Strategic Munition Salvo) | Confirmed strikes in Russian rear |
| **2026-09** | UN Volker Türk statement on autonomous killbots; public denial paired with sub-second approval loops. | **Rungs 18–20** (Batch Nomination & Rubber-Stamp Delegation) | Institutional admission via crisis reaction |
| **2026-09** | Anthropic Frontier Red Team + Threat Intel Sept 2026: reports lab evals show AI substitution for scarce find/fix labor and sim GNC iteration; reports observed misuse in surveillance and drone work; deploys request classifiers; notes open-weights behind frontier but concerning. | **Rungs 10 / 18-20 context** (lab signal, not fielded) | Tier 2 lab report, institutional fact only - no method |

The present is located at the precipice of Band III. The operational constraints of modern combat have rendered the single-human, single-weapon model obsolete. What comes next is the automated coordination of swarms.

