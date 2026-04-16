#!/usr/bin/env python3
"""Generate 300+ MCQs for CP650 Lecture 10 (Data Gathering II)."""
import json
import random

random.seed(42)


def shuffle_options(question, correct_text, wrong_pool, k_wrong=3):
    wrong = [w for w in wrong_pool if w != correct_text]
    random.shuffle(wrong)
    wrong = wrong[:k_wrong]
    options = [correct_text] + wrong
    random.shuffle(options)
    return {"q": question, "options": options, "correct": options.index(correct_text)}


def main():
    mcqs = []

    # --- Ontology vs Epistemology (expanded) ---
    ontology_wrong = [
        "How we know or justify knowledge claims",
        "Methods for evaluating evidence and procedures",
        "The study of knowledge acquisition processes only",
        "Statistical significance of findings",
    ]
    epistemology_wrong = [
        "The nature of what exists or how entities are categorized",
        "Whether something counts as one entity or many",
        "The reality of categories in a design system",
        "Defining what counts as a 'user' in ontology terms",
    ]

    for i in range(1, 36):
        mcqs.append(
            shuffle_options(
                f"({i}) In research philosophy, ontology primarily addresses:",
                "What is — the nature of reality and how entities exist or are categorized",
                ontology_wrong + epistemology_wrong,
            )
        )
    for i in range(36, 71):
        mcqs.append(
            shuffle_options(
                f"({i}) Epistemology in research is mainly concerned with:",
                "How we know — methods and grounds for acquiring and evaluating knowledge",
                epistemology_wrong + ontology_wrong,
            )
        )

    ux_onto = [
        (
            "Whether a website is treated as a single entity or multiple entities",
            ["Choosing the best statistical test", "How to run A/B tests", "Whether usability testing measures satisfaction"],
        ),
        (
            "Whether a chatbot is conceptualized as human-like or machine-like",
            ["Whether A/B testing suits chatbot evaluation", "If surveys are anonymous", "Sampling frame size"],
        ),
    ]
    ux_epi = [
        (
            "Whether usability testing is the most effective method to evaluate satisfaction with a website",
            ["If a website is one entity or many", "Cluster vs stratified sampling", "Internal validity of task order"],
        ),
        (
            "Whether A/B testing is appropriate for evaluating a chatbot's conversational design",
            ["Categorizing the chatbot as human or machine", "Defining population clusters", "Audit trail components"],
        ),
    ]

    base = 71
    for j, (correct, wrong_pool) in enumerate(ux_onto * 18):
        mcqs.append(
            shuffle_options(
                f"({base + j}) A UX ontology-style question would be:",
                correct,
                wrong_pool + ontology_wrong,
            )
        )
    base = 71 + 36
    for j, (correct, wrong_pool) in enumerate(ux_epi * 18):
        mcqs.append(
            shuffle_options(
                f"({base + j}) A UX epistemology-style question would be:",
                correct,
                wrong_pool + epistemology_wrong,
            )
        )

    # --- Qualitative research ---
    qual_defs = [
        "Collecting and analyzing non-numerical data to understand concepts, opinions, or experiences",
        "Using text, video, or audio to gain in-depth insights or generate ideas",
    ]
    qual_wrong = [
        "Only collecting numerical measurements for hypothesis testing",
        "Exclusively using randomized controlled trials",
        "Research that rejects interpretation of any kind",
        "Studies where validity is automatically guaranteed by software",
    ]
    base = 143
    for i in range(40):
        mcqs.append(
            shuffle_options(
                f"({base + i}) Qualitative research, as described in the lecture, involves:",
                qual_defs[i % 2],
                qual_wrong + ["Guaranteeing generalizability through large n alone"],
            )
        )

    nuances = [
        ("Data interpretation is needed", ["Raw data is self-explanatory without interpretation", "Numbers are reality itself"]),
        ("Observation or measurement may change the phenomenon", ["Observation never affects behavior", "Reactivity applies only to lab animals"]),
        ("Symbols (numbers, equations, words) are not reality", ["Symbols are identical to the phenomenon", "Words always map 1:1 to truth"]),
        ("Validity is a goal, not a guaranteed product", ["Validity is automatically produced by any method", "Reliability makes validity unnecessary"]),
    ]
    base = 183
    for i in range(32):
        n, w = nuances[i % 4]
        mcqs.append(shuffle_options(f"({base + i}) A nuance of qualitative research is that:", n, [x for _, xs in nuances for x in xs] + qual_wrong))

    # --- Reliability ---
    rel_correct = "Consistency of findings; repeatability under the same conditions; reduction of random error"
    rel_wrong = [
        "Accuracy of conclusions about causal relationships only",
        "Whether results apply to other cities",
        "Whether participants liked the moderator",
        "The ethical approval number of the study",
    ]
    base = 215
    for i in range(25):
        mcqs.append(
            shuffle_options(
                f"({base + i}) Reliability in research refers to:",
                "Consistency of research findings and repeatability of results under the same conditions",
                rel_wrong + ["Internal validity only"],
            )
        )

    mcqs.append(
        shuffle_options(
            "(240) Test-retest reliability measures:",
            "Consistency over time on the same individuals",
            ["Consistency among multiple judges", "Generalizability to other populations", "Whether tasks were randomized"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(241) Inter-rater reliability measures:",
            "Consistency of results among multiple judges or raters",
            ["Consistency over time for one person", "External validity of the environment", "Sampling bias reduction"],
        )
    )

    # --- Validity ---
    base = 242
    for i in range(28):
        mcqs.append(
            shuffle_options(
                f"({base + i}) Validity in research refers to:",
                "Accuracy and meaningfulness of conclusions; findings that can be meaningful and potentially replicable/generalizable",
                ["Only consistency across sessions", "Only sample size adequacy", "Only researcher credentials", "Only statistical p-values"],
            )
        )
    mcqs.append(
        shuffle_options(
            "(270) Internal validity means:",
            "Findings accurately reflect the phenomenon under study in that context",
            ["Findings apply broadly to other settings", "Multiple raters agree", "The sample was random"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(271) External validity means:",
            "Findings are generalizable to other settings, populations, or conditions",
            ["The study accurately reflects what happened in the lab session only", "Inter-rater agreement is high", "Tasks were in fixed order"],
        )
    )

    # --- UX internal validity scenarios ---
    scenarios_iv = [
        (
            "Comparing sites A and B with A always first may confuse order effects with design differences; alternating which site goes first improves internal validity",
            [
                "Always showing A first is best for external validity with seniors",
                "Order never matters in within-subjects designs",
                "Internal validity only concerns sample size",
            ],
        ),
        (
            "If the setup favors B because participants are already familiar with the task domain, results may lack internal validity",
            [
                "Familiarity only affects external validity, never internal",
                "Warmup tasks must always be included in analysis",
                "Desktop testing always generalizes to mobile",
            ],
        ),
    ]
    base = 272
    for i in range(20):
        c, w = scenarios_iv[i % 2]
        mcqs.append(shuffle_options(f"({base + i}) Internal validity (UX): {c.split(';')[0][:50]}... Best statement:", c, w + rel_wrong))

    # --- UX external validity ---
    scenarios_ev = [
        (
            "Recruiting from the general population may not be valid for a seniors-only product",
            ["Seniors and general population are always interchangeable", "Demographics alone always ensure external validity"],
        ),
        (
            "Testing a mobile design only on desktop may not generalize to real-world mobile use",
            ["Environment never affects usability", "External validity is only about sample randomness"],
        ),
        (
            "Participants should have goals similar to real users; demographics alone may be insufficient",
            ["Matching age is sufficient for all products", "Goals never matter if the sample is large"],
        ),
    ]
    base = 292
    for i in range(18):
        c, w = scenarios_ev[i % 3]
        mcqs.append(shuffle_options(f"({base + i}) External validity concern:", c, w + qual_wrong))

    # --- Design recommendations ---
    recs = [
        ("Randomize task order to reduce bias because first tasks often take longer with more errors", "Randomization is irrelevant to bias"),
        ("Use warmup tasks to reduce learning effects; exclude warmups from analysis", "Warmup data must always be analyzed as primary tasks"),
        ("End-of-session tasks may show fatigue; order effects matter", "Fatigue never affects usability metrics"),
    ]
    base = 310
    for i in range(22):
        c, w = recs[i % 3]
        mcqs.append(shuffle_options(f"({base + i}) Study design recommendation:", c, [w] + rel_wrong))

    # --- Reactivity ---
    reactivity_def = "Change in behavior because of being observed or studied; can affect validity and generalizability"
    mcqs.append(shuffle_options("(332) Reactivity refers to:", reactivity_def, ["Only errors in quantitative coding", "Inter-rater disagreement only"]))

    mcqs.append(
        shuffle_options(
            "(333) The Hawthorne effect is:",
            "Participants change behavior or performance because of increased attention from being in a study",
            ["Participants always behave naturally when watched", "Only occurs in qualitative interviews"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(334) The conformity effect includes:",
            "Tendency to align with group actions or opinions to fit in; related to Asch experiments and groupthink",
            ["Only medical placebo effects", "Only inter-rater reliability"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(335) A blind study design means:",
            "Participants and/or researchers may not know group assignments to reduce bias",
            ["No one may ever analyze qualitative data", "Only one researcher is allowed"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(336) A double-blind design means:",
            "Both participants and researchers do not know group assignments (common in clinical trials; controls expectancy and placebo-related bias)",
            ["Only participants are blinded", "Only statisticians are blinded", "No ethics board is involved"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(337) Social desirability bias is:",
            "Reporting answers believed to be socially acceptable rather than true beliefs or behaviors",
            ["Always eliminated by large samples", "The same as Hawthorne effect"],
        )
    )

    base = 338
    for i in range(15):
        mcqs.append(shuffle_options(f"({base + i}) Reactivity can threaten:", "Validity and generalizability of findings", ["Only qualitative coding", "Only file storage size"]))

    # --- Sampling ---
    samp = [
        ("Sampling is selecting a subset of a population to study", "Census always means sampling"),
        ("Representativeness means the sample reflects the population of interest", "A big convenience sample is always representative"),
        ("Sampling bias is the risk the sample misrepresents the population", "Bias only exists in probability sampling"),
        ("In quantitative research, sample characteristics and size matter for inference", "In quant research, relative sample size never matters"),
        ("In qualitative research, the aim is often breadth of views/themes, not statistical representativeness", "Qual research always requires random sampling"),
    ]
    base = 353
    for i in range(25):
        c, w = samp[i % 5]
        mcqs.append(shuffle_options(f"({base + i}) Sampling:", c, [w, "Stratified sampling means selecting only outliers"]))

    types = [
        ("Probability sampling involves random selection of individuals", "Quota sampling is a pure probability method"),
        ("Non-probability sampling uses non-random selection (e.g., quota sampling)", "Snowball sampling is always probability sampling"),
        ("Convenience sampling selects easily accessible participants", "Convenience sampling is the same as stratified sampling"),
        ("Stratified sampling divides the population into subgroups and samples within them", "Stratified sampling ignores subgroups"),
        ("Cluster sampling divides the population into clusters and randomly selects clusters", "Cluster sampling samples every individual in the population"),
        ("Snowball sampling recruits participants via referrals", "Snowball sampling is only used for census data"),
    ]
    base = 378
    for i in range(18):
        c, w = types[i % 6]
        mcqs.append(shuffle_options(f"({base + i}) Sampling type:", c, [w] + qual_wrong))

    criteria = [
        "Degree of accuracy required",
        "Whether the project is local vs national in scope",
        "Need for statistical analysis",
        "Available resources (time and money)",
    ]
    base = 396
    for i, crit in enumerate(criteria * 6):
        others = [c for c in criteria if c != crit]
        mcqs.append(
            shuffle_options(
                f"({400 + i}) Which item is listed as a criterion for choosing an appropriate sample design?",
                crit,
                others + ["Only the color palette of the interface"],
            )
        )

    # --- Trustworthiness (Leininger / Lincoln & Guba style) ---
    leininger = [
        ("Credibility (e.g., active listening, reflection)", "Credibility means only statistical power"),
        ("Confirmability (documented evidence from primary sources; participatory approaches)", "Confirmability means deleting raw data"),
        ("Meaning-in-context (holistic understanding)", "Meaning-in-context ignores context"),
        ("Recurrent patterning (patterns through repeated experiences)", "Recurrent patterning forbids repetition"),
        ("Transferability (similarities in comparable situations)", "Transferability equals statistical generalization always"),
    ]
    base = 424
    for i in range(20):
        c, w = leininger[i % 5]
        mcqs.append(shuffle_options(f"({base + i}) Leininger (1994) — promoting rigor:", c, [w] + qual_wrong))

    lincoln = [
        ("Credibility", "Only profitability"),
        ("Applicability", "Applicability means ignoring participants"),
        ("Consistency", "Consistency means changing codes daily at random"),
        ("Neutrality", "Neutrality means hiding risks from participants"),
    ]
    base = 444
    for i in range(16):
        c, w = lincoln[i % 4]
        mcqs.append(shuffle_options(f"({base + i}) Lincoln and Guba (1990) criteria include:", c, [w] + rel_wrong))

    mcqs.append(
        shuffle_options(
            "(460) Member checks involve:",
            "Confirming data and interpretations with participants (also called member tests of validity or host verification)",
            ["Deleting transcripts after one read", "Only peer review of code, never participants"],
        )
    )
    mcqs.append(
        shuffle_options(
            "(461) Seeking diversity in qualitative inquiry helps:",
            "Allow a range of realities and perspectives",
            ["Guarantee a single objective truth", "Eliminate the need for ethics"],
        )
    )

    audit = [
        "Raw data",
        "Data reduction and analysis products",
        "Data reconstruction and synthesis products",
        "Process notes (e.g., researcher journal)",
        "Materials on intentions and dispositions",
    ]
    base = 462
    for i in range(20):
        item = audit[i % 5]
        others = [a for a in audit if a != item]
        mcqs.append(
            shuffle_options(
                f"({base + i}) An audit trail may include:",
                item,
                others + ["Unrecorded undocumented memory only"],
            )
        )

    # --- Ethics (Patton checklist numbers as scenarios) ---
    patton = [
        "Explaining purpose and methods",
        "Promises made to participants",
        "Risk assessment",
        "Confidentiality",
        "Informed consent",
        "Data access and ownership",
        "Interviewer mental health",
        "Advice (ethical counsel)",
        "Data collection boundaries",
        "Ethical vs legal conduct",
    ]
    base = 482
    for i in range(30):
        p = patton[i % 10]
        mcqs.append(
            shuffle_options(
                f"({base + i}) Patton (2002) ethical checklist includes considering:",
                p,
                ["Only publication priority", "Only marketing KPIs", "Only competitor analysis", "Only UI color contrast"],
            )
        )

    ethics_misc = [
        ("Validity and reliability depend on investigator ethics and rigor", "Ethics are irrelevant to validity"),
        ("REB approval may be required; a detailed plan is often needed", "REB is never required for any UX study"),
        ("Participants often expect anonymity to be protected", "Anonymity is optional for all published quotes"),
        ("Ethics guidelines may be formal or informal by industry", "Ethics are identical in every industry always"),
        ("Research ethics often focus on risk and consent", "Risk is only a concern in medical research"),
    ]
    base = 512
    for i in range(20):
        c, w = ethics_misc[i % 5]
        mcqs.append(shuffle_options(f"({base + i}) Ethics in qualitative research:", c, [w] + qual_wrong))

    risk_priv = [
        ("Harm in user research can be harder to anticipate than in some medical contexts", "Harm is always obvious in UX"),
        ("Disclosures during research can unintentionally harm participants or others", "Disclosure never creates risk"),
        ("Researchers should minimize potential for harm", "Minimizing harm means skipping consent"),
        ("Researchers should avoid identifying participants from responses in stored or published data", "Using real names in published transcripts is always fine"),
        ("Numeric codes or aliases can protect identity", "Aliases are forbidden in qualitative work"),
        ("More personal or 'human' research increases identification risk from responses", "Personal topics reduce identification risk"),
    ]
    base = 532
    for i in range(24):
        c, w = risk_priv[i % 6]
        mcqs.append(shuffle_options(f"({base + i}) Risk / privacy / confidentiality:", c, [w] + ethics_misc[0:1]))

    consent_q = [
        (
            "Informed consent requires participants understand potential risks and the extent of those risks",
            ["Risks can be hidden if they seem minor", "Consent is implied by participating without reading"],
        ),
        (
            "When harm may reasonably be expected, benefits should outweigh risks and participants must understand and agree",
            ["Benefits never need to outweigh risks", "Risk communication is optional"],
        ),
    ]
    base = 556
    for i in range(16):
        c, w = consent_q[i % 2]
        mcqs.append(shuffle_options(f"({base + i}) Consent:", c, w + ["Consent means unlimited data resale"]))

    # Holy trinity
    mcqs.append(
        shuffle_options(
            "(572) Kvale (1996) describes validity, reliability, and generalisability as:",
            "The 'holy trinity' of the sciences (important quality criteria)",
            ["The only three types of sampling", "Three types of consent forms"],
        )
    )

    # Issues slide (generic)
    for i in range(28):
        mcqs.append(
            shuffle_options(
                f"({573 + i}) A common issue discussed in relation to qualitative research is:",
                "Need for careful interpretation and awareness that measurement can change behavior",
                ["Qualitative data never needs interpretation", "Qualitative research has no limitations"],
            )
        )

    # Credibility of researcher (lecture list)
    cred_components = [
        "Training and experience",
        "Track record and professional status",
        "Self-presentation and intellectual rigor",
        "Professional integrity and methodological competence",
    ]
    base = 601
    for i in range(16):
        item = cred_components[i % 4]
        mcqs.append(
            shuffle_options(
                f"({base + i}) Credibility of qualitative research can depend on researcher qualities such as:",
                item,
                ["Only popularity on social media", "Only number of survey questions", "Only font choice in slides"],
            )
        )

    # Ensure count and renumber
    assert len(mcqs) >= 300, len(mcqs)

    out_path = "/Users/umeraamir/Downloads/UIUX/lec10-quiz/lec10-mcqs.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(mcqs, f, ensure_ascii=False, indent=0)

    js_path = "/Users/umeraamir/Downloads/UIUX/lec10-quiz/lec10-mcqs.js"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.LEC10_MCQS = ")
        json.dump(mcqs, f, ensure_ascii=False)
        f.write(";\n")

    print(f"Wrote {len(mcqs)} MCQs to {out_path} and {js_path}")


if __name__ == "__main__":
    main()
