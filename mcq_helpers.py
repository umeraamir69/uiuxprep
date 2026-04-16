"""Shared helpers for CP650 MCQ generation."""
import json
import random
from pathlib import Path


def shuffle_options(question, correct_text, wrong_pool, k_wrong=3, cat="recall"):
    wrong = [w for w in wrong_pool if w != correct_text]
    random.shuffle(wrong)
    wrong = wrong[:k_wrong]
    options = [correct_text] + wrong
    random.shuffle(options)
    return {
        "q": question,
        "options": options,
        "correct": options.index(correct_text),
        "cat": cat,
    }


def expand_variants(stem, correct, wrong_pool, labels, cat="recall"):
    """Repeat same stem with different parenthetical labels for variety."""
    out = []
    for lab in labels:
        out.append(shuffle_options(f"{stem} ({lab})", correct, wrong_pool, cat=cat))
    return out


def tag_cat(cat: str, q):
    q = dict(q)
    q["cat"] = cat
    return q
