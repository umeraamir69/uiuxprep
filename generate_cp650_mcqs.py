#!/usr/bin/env python3
"""
Generate MCQs for CP650 Lectures 1–15 (slide-derived + analytical).
Outputs mcqs-data.js and mcqs-data.json next to this script.
"""
from __future__ import annotations

import json
import random
import subprocess
import sys
from pathlib import Path

from mcq_helpers import shuffle_options

ROOT = Path(__file__).resolve().parent
random.seed(42)


def guess_cat_from_text(q: str) -> str:
    s = q.lower()
    if any(
        k in s
        for k in (
            "scenario:",
            "a team",
            "you are ",
            "which threat",
            "most appropriate",
            "best next step",
            "critique",
            "trade-off",
            "tradeoff",
            "if participants",
            "a researcher",
            "stakeholders disagree",
        )
    ):
        return "analysis"
    if any(k in s for k in ("when ", "why might", "compared to", "least likely", "primarily")):
        return "application"
    return "recall"


def gen_lec1() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(12):
        mcqs.append(
            shuffle_options(
                f"[L1] Interaction design is best described as multidisciplinary because: (v{i + 1})",
                "It draws on psychology, social sciences, computing, engineering, ergonomics, informatics, and design practices",
                [
                    "It only uses graphic design rules",
                    "It excludes user research",
                    "It is identical to software engineering only",
                ],
                cat="recall",
            )
        )
    for i in range(10):
        mcqs.append(
            shuffle_options(
                f"[L1] Sharp, Rogers, and Preece define interaction design as: (v{i + 1})",
                "Designing interactive products to support how people communicate and interact in everyday and working lives",
                [
                    "Designing only hardware ergonomics",
                    "Writing marketing copy for products",
                    "Optimizing database schemas only",
                ],
                cat="recall",
            )
        )
    goals = [
        ("Develop usable products", ["Maximize lines of code", "Eliminate all user testing"]),
        ("Involve users in the design process", ["Hide prototypes from users", "Avoid iteration"]),
    ]
    for g, bad in goals * 8:
        mcqs.append(shuffle_options(f"[L1] A stated goal of interaction design includes:", g, bad + ["Focus only on aesthetics"], cat="recall"))

    mcqs.append(
        shuffle_options(
            "[L1] Scenario: Bottom-row elevator labels look like buttons but top row does not. Why are top-row mistakes less likely?",
            "Bottom-row labels and controls look the same, increasing confusion; top row is visually distinct from controls",
            [
                "Users always read top rows first",
                "Bottom rows are brighter by law",
                "Touch targets are larger on the bottom",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L1] Scenario: A vending machine requires pressing a button before inserting money, opposite of common mental models. The main issue is:",
            "Mismatch with a familiar interaction sequence (violates user expectations / learnability)",
            [
                "The machine is too colorful",
                "The screen resolution is low",
                "It lacks voice control",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L1] The TiVo remote is praised partly because:",
            "It uses a logical layout, distinctive/color-coded buttons, and a shape that fits the hand",
            [
                "It has the most buttons of any remote",
                "It removes all shortcuts",
                "It uses only voice input",
            ],
            cat="application",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L1] Garrett (2010) is cited to emphasize that:",
            "Every product used by someone has a user experience",
            [
                "UX applies only to websites",
                "UX is measurable only by revenue",
                "UX is the same as UI",
            ],
            cat="recall",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L1] Hassenzahl’s pragmatic vs hedonic distinction: pragmatic UX focuses on:",
            "How simple, practical, and obvious it is to achieve goals",
            [
                "How culturally controversial the brand is",
                "How many features are hidden",
                "Server uptime only",
            ],
            cat="application",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L1] Nielsen Norman Group describes helping companies enter the:",
            "Age of the consumer with human-centered products and services",
            [
                "Age of minimal documentation",
                "Age of waterfall-only development",
                "Age of hardware-only design",
            ],
            cat="recall",
        )
    )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L1] Usability goals include: (pick best set) (v{i + 1})",
                "Effective, efficient, safe, good utility, easy to learn, easy to remember",
                [
                    "Only fast graphics",
                    "Only low cost",
                    "Only brand color consistency",
                ],
                cat="recall",
            )
        )
    for i in range(15):
        mcqs.append(
            shuffle_options(
                f"[L1] Characteristics of Interaction Design include: (v{i + 1})",
                "Users involved throughout; specific usability/UX goals documented early; iteration through core activities",
                [
                    "Freeze requirements forever after week 1",
                    "Avoid documenting goals",
                    "Ship without evaluation",
                ],
                cat="recall",
            )
        )
    for i in range(10):
        mcqs.append(
            shuffle_options(
                f"[L1] Multidisciplinary teams can struggle because: (v{i + 1})",
                "Different backgrounds create communication and vocabulary differences",
                [
                    "They always have too few ideas",
                    "They cannot use prototypes",
                    "They must avoid user research",
                ],
                cat="application",
            )
        )
    return mcqs


def gen_lec2() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L2] Accessibility focuses on: (v{i + 1})",
                "The extent a product can be accessed by as many people as possible, including people with disabilities",
                [
                    "Maximizing animation count",
                    "Designing only for expert users",
                    "Reducing security",
                ],
                cat="recall",
            )
        )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L2] Inclusiveness in design means: (v{i + 1})",
                "Accommodating the widest possible range of people across disability, age, education, income, etc.",
                [
                    "Designing only for the average user",
                    "Removing accessibility features",
                    "Targeting one persona only",
                ],
                cat="recall",
            )
        )
    impair = ["Sensory", "Physical", "Cognitive"]
    for i in range(15):
        mcqs.append(
            shuffle_options(
                f"[L2] Disability types discussed include: (v{i + 1})",
                "Sensory, physical, and cognitive impairments (each with varying capabilities)",
                [
                    "Only temporary disabilities",
                    "Only financial",
                    "Only cultural",
                ],
                cat="recall",
            )
        )
    for i in range(12):
        mcqs.append(
            shuffle_options(
                f"[L2] Impairment can be: (v{i + 1})",
                "Permanent, temporary, or situational (e.g., noisy environment affecting hearing)",
                [
                    "Only permanent",
                    "Only genetic",
                    "Only occupational",
                ],
                cat="application",
            )
        )
    principles = [
        ("Visibility: users can see state of device and possible actions", ["Invisibility of all affordances"]),
        ("Feedback: information returned about what happened (sound, highlight, animation)", ["Removing all confirmations"]),
        ("Constraints: limiting possible actions to prevent errors", ["Offering infinite undifferentiated choices"]),
    ]
    for p, w in principles * 7:
        mcqs.append(shuffle_options(f"[L2] Design principle:", p, w + ["Randomness"], cat="recall"))

    mcqs.append(
        shuffle_options(
            "[L2] Scenario: An elevator panel gives no visible cue that a room card must be inserted first. Which principle is violated most directly?",
            "Visibility (users cannot see what action is required)",
            ["Consistency across apps", "External consistency of keypads", "Snowball sampling"],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L2] Internal vs external consistency: external consistency refers to:",
            "Similarity of operations/interfaces across applications/devices",
            [
                "Consistency within one app only",
                "Consistency of statistical tests",
                "Consistency of participant payment",
            ],
            cat="application",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L2] Keypad number layout differs between phone and calculator. This illustrates:",
            "External inconsistency across devices",
            [
                "Internal inconsistency within one device",
                "A sampling bias",
                "A double-blind study",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L2] Mapping in interface design supports: (v{i + 1})",
                "Clear relationships between controls and their effects (e.g., adjacent mapping, color coding)",
                [
                    "Random placement of ports",
                    "Hiding all labels",
                    "Using identical icons for different actions",
                ],
                cat="application",
            )
        )
    return mcqs


def gen_lec3() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L3] Interaction design as a process emphasizes: (v{i + 1})",
                "Discovering requirements, designing to fulfill them, prototyping, evaluating, trade-offs, and generating alternatives",
                [
                    "Writing code before any requirements",
                    "Avoiding prototypes",
                    "Single design with no alternatives",
                ],
                cat="recall",
            )
        )
    approaches = ["User-centered design", "Activity-centered design", "Systems design"]
    for i in range(12):
        mcqs.append(
            shuffle_options(
                f"[L3] Different approaches mentioned include: (v{i + 1})",
                "User-centered, activity-centered, and systems design approaches",
                [
                    "Only waterfall documentation",
                    "Only database-first design",
                    "Only marketing-led design",
                ],
                cat="recall",
            )
        )
    for i in range(12):
        mcqs.append(
            shuffle_options(
                f"[L3] User-centered approach includes: (v{i + 1})",
                "Early focus on users/tasks; empirical measurement; iterative design and retesting after fixes",
                [
                    "No user involvement",
                    "Big-bang release only",
                    "Ignoring task analysis",
                ],
                cat="recall",
            )
        )
    for i in range(15):
        mcqs.append(
            shuffle_options(
                f"[L3] Integrating ID with Agile is promising partly because: (v{i + 1})",
                "Agile emphasizes tight iterations, early/regular feedback, emergent requirements, and balancing flexibility with structure",
                [
                    "Agile forbids user testing",
                    "Agile requires fixed requirements upfront",
                    "Agile eliminates prototypes",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L3] Scenario: A team ships fast but UX problems accumulate release after release. This is closest to:",
            "UX / technical debt from expedient short-term trade-offs and neglected UX",
            [
                "Perfect external validity",
                "Snowball sampling failure",
                "Double-blind moderation",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L3] Choosing among alternatives may involve A/B testing, but it is noted as nontrivial because:",
            "You must set appropriate metrics and choose user groups carefully",
            [
                "A/B tests never need metrics",
                "A/B tests require infinite participants",
                "A/B tests only work for hardware",
            ],
            cat="application",
        )
    )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L3] Stakeholders help identify: (v{i + 1})",
                "Groups to include in design activities and clarify who is affected beyond a vague 'everybody' user",
                [
                    "Only developers",
                    "Only investors",
                    "Only competitors",
                ],
                cat="recall",
            )
        )
    for i in range(14):
        mcqs.append(
            shuffle_options(
                f"[L3] Degrees of user involvement include: (v{i + 1})",
                "Design team membership (full/part time), short-term involvement, face-to-face activities, online crowdsourcing, post-release feedback",
                [
                    "Only annual surveys",
                    "Only lab-only participation",
                    "No online participation",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec4() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L4] A proof of concept (PoC) helps teams: (v{i + 1})",
                "Conceptualize what the product will do and scrutinize feasibility, desirability, and usefulness",
                [
                    "Skip evaluation entirely",
                    "Replace all user research",
                    "Finalize marketing pricing",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L4] In the lecture, an assumption is defined as:",
            "Taking something for granted when it still needs investigation",
            [
                "A validated measurement",
                "A peer-reviewed theorem",
                "A completed usability test",
            ],
            cat="recall",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L4] A claim is:",
            "Stating something as true when it is still open to question",
            [
                "A synonym for requirement",
                "A finished statistical result",
                "A legal contract clause",
            ],
            cat="recall",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L4] A conceptual model is: (v{i + 1})",
                "A high-level description of how a system is organized and operates; supports coherent design before laying out widgets",
                [
                    "Only a database schema",
                    "Only a color palette",
                    "Only a marketing persona",
                ],
                cat="recall",
            )
        )
    types_it = ["Instructing", "Conversing", "Manipulating", "Exploring", "Responding"]
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L4] Interaction types include: (v{i + 1})",
                "Instructing, conversing, manipulating, exploring, and responding (system-initiated)",
                [
                    "Only typing and clicking",
                    "Only batch processing",
                    "Only printing",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L4] Scenario: A voice assistant misunderstands children frequently. This primarily illustrates a downside of:",
            "The conversing interaction model (misunderstandings / parsing failures)",
            [
                "Instructing-only tasks",
                "Manipulating physical levers",
                "Exploring a map without labels",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L4] Interface metaphors can be problematic because they may:",
            "Break cultural rules, over-constrain thinking, or transfer bad existing designs",
            [
                "Always guarantee learnability",
                "Eliminate need for labels",
                "Remove need for evaluation",
            ],
            cat="application",
        )
    )
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L4] Benefits of conceptualizing early include: (v{i + 1})",
                "Orientation, open-minded exploration, and common ground/shared terms for the team",
                [
                    "Eliminating the need for prototypes",
                    "Guaranteeing one correct design",
                    "Removing stakeholder disagreement",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec5() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(16):
        mcqs.append(
            shuffle_options(
                f"[L5] Cognition includes activities such as: (v{i + 1})",
                "Thinking, remembering, learning, decision-making, perception, reading, talking, writing",
                [
                    "Only muscle memory",
                    "Only typing speed",
                    "Only screen brightness",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L5] Norman (1993) contrasts experiential vs reflective cognition; Kahneman (2011) is associated with:",
            "Fast vs slow thinking",
            [
                "Color theory",
                "Network protocols",
                "Database normalization",
            ],
            cat="recall",
        )
    )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L5] Attention involves: (v{i + 1})",
                "Selecting what to focus on from competing stimuli; can be focused or divided",
                [
                    "Processing everything equally",
                    "Eliminating perception",
                    "Removing memory load",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L5] Tullis (1987) hotel search: same information density but faster search on one screen mainly because:",
            "Grouping/spacing: vertical categories vs bunched information improves scanning",
            [
                "Users preferred colors randomly",
                "One screen had fewer pixels",
                "Density was not the same",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L5] Using a phone while driving is risky partly because:",
            "Drivers’ reaction times to external events are longer when talking on the phone; conversation competes for attention",
            [
                "Hands-free removes all cognitive load",
                "Phones only distract visually, never cognitively",
                "Driving requires no attention",
            ],
            cat="analysis",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L5] Hands-free phones are not necessarily safer while driving because:",
            "Similar cognitive processing is involved in the conversation; the remote party cannot pause with road hazards like a front-seat passenger can",
            [
                "They eliminate all distraction",
                "They improve reaction time",
                "They only affect night driving",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L5] Design implications for attention include: (v{i + 1})",
                "Make key information salient when needed; avoid clutter; support switching and returning to tasks",
                [
                    "Always show everything at once",
                    "Remove all animations",
                    "Hide errors until logout",
                ],
                cat="application",
            )
        )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L5] Perception in HCI implies designing representations that are: (v{i + 1})",
                "Readily perceivable: legible text, distinguishable icons, good contrast",
                [
                    "As small as possible",
                    "Always monochrome",
                    "Identical to print books",
                ],
                cat="recall",
            )
        )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L5] Understanding cognition helps designers because it: (v{i + 1})",
                "Explains what users can/cannot do, diagnoses problems, and guides better interactive products",
                [
                    "Replaces user research",
                    "Guarantees perfect predictions",
                    "Eliminates need for prototypes",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec6() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L6] Social technologies differ in how they: (v{i + 1})",
                "Support social interaction—some encourage interaction, others may reduce quality of everyday conversation",
                [
                    "Always increase face-to-face time",
                    "Eliminate collaboration",
                    "Remove all etiquette",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L6] Sacks et al. (1978) conversation analysis Rule 1 is roughly:",
            "Current speaker can select next speaker via question/request/opinion",
            [
                "Only the loudest speaker talks",
                "No turn-taking exists",
                "Online chat has identical rules to F2F always",
            ],
            cat="recall",
        )
    )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L6] Turn-taking and back-channeling (uh-huh, umm) help: (v{i + 1})",
                "Coordinate conversation flow and signal continued engagement",
                [
                    "End conversations immediately",
                    "Replace all questions",
                    "Guarantee agreement",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L6] VideoWindow finding: people sometimes talked more to others in the same room than to the remote site, partly because:",
            "The setup made remote interaction awkward; proximity and local social norms dominated",
            [
                "Video always beats audio",
                "Remote users had no cameras",
                "Bandwidth was infinite",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L6] Telepresence robots can help by: (v{i + 1})",
                "Letting people attend events remotely with a physical proxy presence",
                [
                    "Replacing all travel permanently",
                "Eliminating privacy concerns",
                "Removing need for accessibility",
                ],
                cat="application",
            )
        )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L6] Remote conversation tools include: (v{i + 1})",
                "Email, IM, chatrooms, videoconferencing—may mimic or extend conversation patterns",
                [
                    "Only postal mail",
                    "Only spreadsheets",
                    "Only command-line shells",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec7() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L7] Don Norman’s three levels of design (visceral/behavioral/reflective): behavioral design aligns with: (v{i + 1})",
                "Use and traditional usability values",
                [
                    "Meaning and personal narrative only",
                    "Purely aesthetic look only",
                    "Only brand slogans",
                ],
                cat="recall",
            )
        )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L7] Visceral design focuses on: (v{i + 1})",
                "Immediate look/feel/sound attractiveness",
                [
                    "Long-term life stories only",
                    "Only task completion time",
                    "Only database performance",
                ],
                cat="recall",
            )
        )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L7] Reflective design concerns: (v{i + 1})",
                "Meaning, identity, and personal value of a product",
                [
                    "Only click counts",
                    "Only error rates",
                    "Only network latency",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L7] Scenario: Users tolerate slow downloads if the experience feels delightful. This suggests:",
            "Emotional/aesthetic qualities can influence willingness to endure friction (hedonic vs pragmatic trade-offs)",
            [
                "Speed never matters",
                "Aesthetics never affect usability",
                "Users never notice delays",
            ],
            cat="analysis",
        )
    )
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L7] Frustrating interfaces often arise when: (v{i + 1})",
                "Systems crash, violate expectations, give vague errors, require many steps then fail, or feel patronizing",
                [
                    "They use too many fonts",
                    "They are open source",
                    "They have dark mode",
                ],
                cat="application",
            )
        )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L7] Persuasive / affective computing topics include: (v{i + 1})",
                "Recognizing emotion, designing for motivation, anthropomorphism trade-offs",
                [
                    "Removing all feedback",
                    "Banning color",
                    "Eliminating sound",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec8() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L8] The lecture lists many interface types; an example category is: (v{i + 1})",
                "GUIs (WIMP), voice interfaces, touch, AR/VR, wearables, etc.",
                [
                    "Only CLI forever",
                    "Only paper forms",
                    "Only punch cards",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L8] Icon mapping types include similar, analogical, and:",
            "Arbitrary (e.g., X for delete)",
            [
                "Only photographic",
                "Only 3D models",
                "Only animated GIFs",
            ],
            cat="application",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L8] Scenario: A megamenu shows many options in a 2D layout. Compared to tiny drop-downs, it can:",
            "Improve scanability and navigation for large sites (when designed well)",
            [
                "Always reduce learnability",
                "Eliminate need for labels",
                "Guarantee accessibility without testing",
            ],
            cat="analysis",
        )
    )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L8] Command-line interfaces are often: (v{i + 1})",
                "Efficient for experts but have high learning overhead for commands",
                [
                "Impossible to script",
                "Always slower than GUIs for experts",
                "Never used in web dev",
                ],
                cat="application",
            )
        )
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"[L8] Multimedia interfaces combine: (v{i + 1})",
                "Graphics, text, video, sound, animation with interactivity",
                [
                    "Text only",
                    "Audio only",
                    "Static PDFs only",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec9() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L9] Five key planning issues for data gathering include: (v{i + 1})",
                "Goals, participants, relationship/consent, triangulation, pilot studies",
                [
                    "Only budget",
                    "Only branding",
                    "Only competitor logos",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L9] Triangulation means:",
            "Looking at data from more than one perspective and often multiple data types/methods",
            [
                "Using one method only",
                "Ignoring qualitative data",
                "Only quantitative surveys",
            ],
            cat="recall",
        )
    )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L9] Interview types include: (v{i + 1})",
                "Unstructured (rich, less replicable), structured (replicable, less rich), semi-structured (balance)",
                [
                    "Only phone books",
                    "Only census",
                    "Only A/B tests",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L9] Scenario: You ask “Why do you love our app?” This is problematic as:",
            "A leading question that assumes liking; better to ask neutrally and avoid assumptions",
            [
                "It is too short",
                "It is always illegal",
                "It improves response rate always",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L9] Running an interview often follows: intro/goals/ethics, warm-up, main body, cool-off, closure (v{i + 1})",
                "Yes—structure reduces anxiety and improves data quality",
                [
                    "Start with hardest questions",
                    "Never record consent",
                    "Skip thank-you",
                ],
                cat="application",
            )
        )
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L9] Focus groups typically: (v{i + 1})",
                "Involve ~3–10 participants, facilitated discussion, selected to represent target population",
                [
                    "Are always one-on-one",
                    "Never need facilitation",
                    "Are identical to surveys",
                ],
                cat="recall",
            )
        )
    return mcqs


def load_lec10_from_json() -> list[dict]:
    path = ROOT / "lec10-mcqs.json"
    if not path.exists():
        gen = ROOT / "generate_lec10_mcqs.py"
        if gen.exists():
            subprocess.run([sys.executable, str(gen)], check=False)
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for item in data:
        q = item["q"].replace("[L10]", "[L10]").strip()
        if not q.startswith("[L10]"):
            q = "[L10] " + q
        cat = guess_cat_from_text(q)
        out.append({"q": q, "options": item["options"], "correct": item["correct"], "cat": cat})
    return out


def gen_lec11() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L11] Qualitative data often includes: (v{i + 1})",
                "Words/images: descriptions, quotes, vignettes, photos; can be coded but not always meaningfully reduced to numbers",
                [
                    "Only Likert scales",
                    "Only timestamps",
                    "Only CPU usage",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L11] Thematic analysis involves:",
            "Tagging observations/quotes with codes and identifying themes that recur across data",
            [
                "Only calculating means",
                "Only t-tests",
                "Only random sampling formulas",
            ],
            cat="recall",
        )
    )
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L11] Software tools for qualitative analysis (examples) include: (v{i + 1})",
                "NVivo, MAXQDA, Dedoose, Dovetail, EnjoyHQ, Delve, Aurelius (trade-offs: cost, learning curve)",
                [
                    "Only Microsoft Paint",
                    "Only Excel pivot tables exclusively",
                    "Only git diff",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L11] Scenario: Two coders apply a code differently. A good response aligned with rigorous qualitative practice is:",
            "Clarify code definitions, train together, reconcile, and document (reliability/consistency)",
            [
                "Keep silent disagreements",
                "Delete all disagreeing data",
                "Always pick the senior researcher arbitrarily",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L11] Video analysis often starts with: (v{i + 1})",
                "A full watch-through with a high-level narrative and noting interesting events/timecodes",
                [
                    "Random frame sampling only",
                    "Deleting audio",
                    "Skipping transcription always",
                ],
                cat="application",
            )
        )
    return mcqs


def gen_lec12() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L12] Field observation advantages include: (v{i + 1})",
                "See real multitasking, distractions, environment constraints not visible in a lab",
                [
                    "Always faster than lab",
                    "Eliminates ethics",
                    "Guarantees representative sampling automatically",
                ],
                cat="recall",
            )
        )
    models = [
        ("Master/Apprentice: user as expert, researcher learns by observing", ["Researcher solves all tasks for user"]),
        ("Partnership: joint discovery, surface problems as they arise", ["Researcher remains silent forever"]),
        ("Interviewer/Interviewee: draw out experience, avoid only factual Q&A", ["Only yes/no allowed"]),
        ("Expert/Novice: observe problems without fixing them to learn workflow pain", ["Researcher must fix bugs immediately"]),
    ]
    for name, wrong in models * 6:
        mcqs.append(shuffle_options(f"[L12] Field observation relationship model:", name, wrong + ["Only surveys"], cat="application"))
    mcqs.append(
        shuffle_options(
            "[L12] Discourse analysis differs from simple content frequency partly because it:",
            "Focuses on how language constructs meaning in dialogue (nuanced interpretation)",
            [
                "Only counts word frequencies",
                "Ignores context",
                "Only works for numbers",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L12] Conversation analysis can examine: (v{i + 1})",
                "Fine-grained semantics and turn structure (e.g., family–Alexa interactions)",
                [
                    "Only stock prices",
                    "Only pixel colors",
                    "Only SQL queries",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec13() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L13] Requirements specify: (v{i + 1})",
                "What the intended product should do or how it should perform (many forms/abstractions)",
                [
                    "Only marketing slogans",
                    "Only office rent",
                    "Only font files",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L13] A common user story format is:",
            "As a <role>, I want <behavior> so that <benefit>",
            [
                "Given <bug> when <crash>",
                "SELECT * FROM users",
                "TODO: fix later",
            ],
            cat="recall",
        )
    )
    kinds = [
        ("Functional requirements", ["Only office furniture"]),
        ("Data requirements", ["Only paint colors"]),
        ("Environment/context (physical/social/org/technical)", ["Only CPU GHz"]),
        ("User characteristics and experience levels", ["Only company revenue"]),
        ("Usability and UX goals", ["Only legal incorporation date"]),
    ]
    for k, w in kinds * 5:
        mcqs.append(shuffle_options(f"[L13] Requirement kind discussed:", k, w + ["Only git branches"], cat="application"))
    mcqs.append(
        shuffle_options(
            "[L13] Scenario: Stakeholders disagree on ‘quality.’ The lecture suggests:",
            "Different stakeholder groups can have different quality thresholds—clarify criteria tied to usability/UX goals",
            [
                "Always pick the cheapest option",
                "Quality is only about pixels",
                "Ignore novices",
            ],
            cat="analysis",
        )
    )
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L13] Data gathering for requirements may combine: (v{i + 1})",
                "Interviews, observation, questionnaires, documentation review, competitive products—often multiple methods",
                [
                    "Only one method ever",
                    "Only guessing",
                    "Only automated scraping without ethics",
                ],
                cat="application",
            )
        )
    return mcqs


def gen_lec14() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L14] Data at scale (big data) can include: (v{i + 1})",
                "Numbers, images, conversations, video, sensor streams, etc.—requires careful analysis and communication",
                [
                    "Only CSV files under 1MB",
                    "Only paper surveys",
                    "Only manual tally marks",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L14] FATE principles include fairness, accountability, transparency, explainability—and often privacy is added:",
            "Yes—ethical use of large-scale data and algorithmic decisions",
            [
                "FATE ignores privacy",
                "FATE only applies to hardware",
                "FATE forbids visualization",
            ],
            cat="recall",
        )
    )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L14] Sentiment analysis can infer: (v{i + 1})",
                "Positive/negative tone and sometimes finer emotions from text/social data (with limitations)",
                [
                    "Exact household income always",
                    "Private keys",
                    "Medical diagnoses with certainty",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L14] Scenario: Combining datasets (airport tracking + social data) can:",
            "Increase insights but also increase privacy harms if people can be re-identified",
            [
                "Always guarantee anonymity",
                "Eliminate need for ethics review",
                "Remove all bias automatically",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L14] Social network analysis can reveal: (v{i + 1})",
                "Structures/relationships between entities (e.g., voting similarities), not just individual stats",
                [
                    "Only CPU temperature",
                    "Only font sizes",
                    "Only monitor refresh rate",
                ],
                cat="recall",
            )
        )
    return mcqs


def gen_lec15() -> list[dict]:
    mcqs: list[dict] = []
    for i in range(22):
        mcqs.append(
            shuffle_options(
                f"[L15] A prototype in interaction design can be: (v{i + 1})",
                "Sketches, storyboards, slideshows, videos, cardboard models, limited software—anything stakeholders can interact with",
                [
                    "Only final shipped code",
                    "Only legal contracts",
                    "Only marketing brochures",
                ],
                cat="recall",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L15] Wizard-of-Oz prototyping means:",
            "User believes they interact with a system, but a human simulates system intelligence/responses",
            [
                "Users write all code",
                "No humans involved",
                "Only hardware sensors",
            ],
            cat="recall",
        )
    )
    for i in range(18):
        mcqs.append(
            shuffle_options(
                f"[L15] Low-fidelity prototypes are useful because they are: (v{i + 1})",
                "Fast, cheap, easy to change (paper, post-its, storyboards)",
                [
                    "Always identical to final UI",
                    "Impossible to test with users",
                    "Legally binding",
                ],
                cat="application",
            )
        )
    mcqs.append(
        shuffle_options(
            "[L15] Horizontal vs vertical compromise: a horizontal prototype tends to:",
            "Show a wide range of functions with shallow detail",
            [
                "Show one feature very deeply end-to-end",
                "Show no features",
                "Ship to production",
            ],
            cat="application",
        )
    )
    mcqs.append(
        shuffle_options(
            "[L15] Scenario: Users see a polished high-fidelity prototype and assume the product is nearly done. The risk is:",
            "Misaligned expectations about completeness/stability (classic HF prototype pitfall)",
            [
                "They will always be correct",
                "Fidelity never affects expectations",
                "Users ignore visuals",
            ],
            cat="analysis",
        )
    )
    for i in range(20):
        mcqs.append(
            shuffle_options(
                f"[L15] Why prototype? (v{i + 1})",
                "Enable evaluation, communication, testing ideas, reflection, and choosing between alternatives",
                [
                    "Avoid all feedback",
                    "Replace requirements",
                    "Eliminate iteration",
                ],
                cat="recall",
            )
        )
    return mcqs


GENERATORS = {
    1: gen_lec1,
    2: gen_lec2,
    3: gen_lec3,
    4: gen_lec4,
    5: gen_lec5,
    6: gen_lec6,
    7: gen_lec7,
    8: gen_lec8,
    9: gen_lec9,
    10: None,  # special
    11: gen_lec11,
    12: gen_lec12,
    13: gen_lec13,
    14: gen_lec14,
    15: gen_lec15,
}


def build_all() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for n in range(1, 16):
        if n == 10:
            lec10 = load_lec10_from_json()
            if not lec10:
                raise FileNotFoundError(
                    "lec10-mcqs.json missing. Run generate_lec10_mcqs.py first."
                )
            out["10"] = lec10
            continue
        gen = GENERATORS[n]
        assert gen is not None
        out[str(n)] = gen()
    return out


def main():
    data = build_all()
    counts = {k: len(v) for k, v in data.items()}
    js_path = ROOT / "mcqs-data.js"
    json_path = ROOT / "mcqs-data.json"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    with js_path.open("w", encoding="utf-8") as f:
        f.write("window.CP650_MCQS_BY_LECTURE = ")
        json.dump(data, f, ensure_ascii=False)
        f.write(";\n")
        f.write("window.CP650_LECTURE_COUNTS = ")
        json.dump(counts, f, ensure_ascii=False)
        f.write(";\n")
    print("Wrote", json_path, "and", js_path)
    print("Counts:", counts)
    print("Total:", sum(counts.values()))


if __name__ == "__main__":
    main()
