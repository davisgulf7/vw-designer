#!/usr/bin/env python3
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Union


DEFAULT_SOURCE_ROOT = Path(
    "/Volumes/Drive B/Dropbox/Personal/SecondLife/presentations/VWBPE 2026 Spring/lm-vr-design/ssot"
)
DEFAULT_OUTPUT_ROOT = Path("generated/lm-vr-design")


KNOWLEDGE_DOMAIN_RULES = [
    ("assessment", [r"\bassessment\b", r"\brubric", r"\bevaluation\b", r"\bgradebook\b"]),
    ("evidence_centered_design", [r"evidence[- ]centered", r"\becd\b"]),
    ("stealth_assessment", [r"stealth assessment", r"in-game support", r"embedded assessment"]),
    ("virtual_worlds", [r"virtual world", r"immersive learning environment", r"metaverse", r"3d virtual"]),
    ("OpenSim", [r"opensim", r"opensimulator", r"\bossl\b", r"\blsl\b"]),
    ("Second_Life", [r"second life", r"linden"]),
    ("simulation", [r"\bsimulation\b", r"\bsimulated\b", r"virtual lab"]),
    ("role_play", [r"role[- ]play", r"avatar role", r"assume roles"]),
    ("scenario_based_learning", [r"scenario[- ]based", r"branching scenario", r"situated learning"]),
    ("storytelling", [r"digital storytelling", r"\bnarrative\b", r"storyliving", r"storyworld"]),
    ("serious_games", [r"game[- ]based", r"serious game", r"\bgamified\b"]),
    ("project_based_learning", [r"project[- ]based", r"\bpbl\b", r"building challenge"]),
    ("experiential_learning", [r"experiential", r"hands-on", r"authentic task", r"embodied"]),
    ("collaborative_learning", [r"collaborative", r"peer review", r"group work", r"team-based"]),
    ("teacher_roles", [r"teacher role", r"teacher as", r"facilitator", r"classroom management", r"instructor role", r"virtual classroom", r"classroom rules", r"expectations"]),
    ("student_agency", [r"student-led", r"student agency", r"voice and choice", r"learner agency", r"student ownership"]),
    ("world_building", [r"world[- ]building", r"world design", r"3d model", r"building in opensim", r"constructing in minecraft"]),
    ("scripting", [r"scripting", r"\bscript\b", r"\bredstone\b", r"\bnpcs?\b"]),
    ("platform_skills", [r"getting started", r"\btutorial\b", r"documentation", r"workflow", r"admin guide", r"troubleshoot", r"\blti\b", r"integration with", r"privacy", r"security", r"coppa", r"ferpa", r"classroom mode"]),
    ("instructional_design", [r"instructional design", r"lesson plan", r"learning objectives", r"pedagogical strateg", r"teaching strateg"]),
    ("standards_alignment", [r"standards", r"\bngss\b", r"common core", r"alignment"]),
    ("accessibility", [r"accessib", r"\budl\b", r"\bcaption(?:ing|s)?\b", r"\bblind\b", r"\bdeaf\b", r"neurodiv"]),
    ("feedback", [r"feedback", r"reflection", r"peer assessment", r"hint"]),
    ("analytics", [r"analytics", r"clickstream", r"data mining", r"tracking"]),
    ("adaptivity", [r"adaptive", r"adaptivity", r"differentiated", r"personalized"]),
]

TEACHER_ROLE_RULES = {
    "facilitator": [r"facilitat", r"guide on the side", r"coach"],
    "formal_authority": [r"classroom management", r"rules", r"expectations", r"compliance"],
    "personal_model": [r"modeling", r"demonstrat", r"worked example"],
    "delegator": [r"student-led", r"peer", r"choice", r"independent"],
    "partner": [r"co-?create", r"collaborat", r"teacher as partner"],
    "sage_on_stage": [r"lecture", r"direct instruction"],
}

STUDENT_ROLE_RULES = {
    "observer": [r"observe", r"watch"],
    "explorer": [r"explor", r"navigate", r"field trip"],
    "builder": [r"build", r"construct", r"modeling", r"maker"],
    "collaborator": [r"collaborat", r"peer", r"team", r"group"],
    "problem_solver": [r"problem", r"challenge", r"inquiry"],
    "performer": [r"role-play", r"simulation", r"present", r"perform"],
    "author": [r"story", r"write", r"design", r"create content"],
    "reflective_learner": [r"reflect", r"self-assess", r"journal"],
}

PEDAGOGY_RULES = {
    "experiential_learning": [r"experiential", r"authentic", r"situated"],
    "training_and_modelling": [r"modeling", r"worked example", r"demonstrat"],
    "project_based_learning": [r"project[- ]based", r"\bpbl\b", r"project"],
    "collaborative_observation": [r"peer observation", r"watch each other"],
    "collaborative_problem_solving": [r"collaborative problem", r"group challenge", r"team-based"],
    "game_based_learning": [r"game[- ]based", r"gameplay", r"minecraft"],
    "exploration_based_learning": [r"explor", r"discovery learning", r"scavenger hunt"],
    "problem_based_learning": [r"problem-based", r"inquiry", r"case study"],
    "constructionist_learning": [r"constructionis", r"maker", r"build"],
    "discussion_based_learning": [r"discussion", r"seminar", r"debrief"],
}

LEARNING_CHARACTERISTIC_RULES = {
    "immersion": [r"immers", r"presence"],
    "flow": [r"\bflow\b", r"engagement"],
    "situated_cognition": [r"situated", r"contextualized"],
    "independent_design": [r"independent", r"self-directed"],
    "collaboration": [r"collaborat", r"peer", r"team"],
    "authenticity": [r"authentic", r"real-world"],
    "student_choice": [r"choice", r"agency", r"student-led"],
    "iteration": [r"iterat", r"revise", r"prototype"],
    "real_world_problem_solving": [r"real-world problem", r"challenge", r"solve"],
}

ASSESSMENT_MODEL_RULES = {
    "traditional": [r"traditional assessment"],
    "formative": [r"formative", r"progress monitoring"],
    "summative": [r"summative", r"final evaluation"],
    "integrative": [r"integrative assessment", r"authentic assessment"],
    "embedded": [r"embedded assessment", r"in-game", r"within gameplay"],
    "evidence_centered_design": [r"evidence[- ]centered", r"\becd\b"],
    "stealth_assessment": [r"stealth assessment"],
    "adaptive_assessment": [r"adaptive assessment", r"adaptive hint", r"adaptive feedback", r"adaptive support"],
}

EVIDENCE_RULES = {
    "clickstream": [r"clickstream"],
    "path_taken": [r"path", r"navigation"],
    "decision_points": [r"decision", r"choice"],
    "artifact_creation": [r"artifact", r"build", r"model", r"story"],
    "chat_discourse": [r"chat", r"discussion", r"dialogue"],
    "collaboration_behavior": [r"collaborat", r"peer", r"group"],
    "time_on_task": [r"time on task", r"time spent"],
    "resource_selection": [r"resource", r"tool choice"],
    "reflection": [r"reflect", r"self-assess", r"journal"],
    "performance_outcome": [r"performance", r"outcome", r"accuracy"],
    "revision_history": [r"revision", r"iteration"],
}

COMPETENCY_RULES = {
    "problem_solving": [r"problem solving", r"challenge"],
    "creativity": [r"creativ", r"design"],
    "systems_thinking": [r"systems", r"ecosystem", r"interdepend"],
    "collaboration": [r"collaborat", r"peer", r"group"],
    "communication": [r"communication", r"discussion", r"presentation"],
    "content_understanding": [r"content knowledge", r"understanding", r"concept"],
    "persistence": [r"persist", r"grit", r"effort"],
    "decision_making": [r"decision", r"choice"],
    "strategic_reasoning": [r"strategy", r"reasoning"],
    "spatial_reasoning": [r"spatial", r"geometry", r"3d"],
}

FEEDBACK_RULES = {
    "real_time": [r"real-time", r"instant"],
    "embedded": [r"embedded", r"in-world"],
    "teacher_review": [r"teacher review", r"instructor feedback"],
    "self_assessment": [r"self-assess", r"reflection"],
    "peer_assessment": [r"peer assessment", r"peer review"],
    "post_activity_summary": [r"debrief", r"summary"],
    "adaptive_hinting": [r"hint", r"adaptive support"],
}

PLATFORM_RULES = {
    "OpenSim": [r"opensim", r"opensimulator", r"\bossl\b", r"\blsl\b"],
    "Second_Life": [r"second life", r"linden"],
    "Active_Worlds": [r"active worlds"],
    "Minecraft": [r"minecraft", r"\bredstone\b", r"\bnpcs?\b"],
    "web_browser_based": [r"web-based", r"browser-based", r"runs in a browser", r"\bhtml\b"],
    "LMS_based": [r"\blms\b", r"\bmoodle\b", r"\blti\b", r"gradebook"],
    "custom_engine": [r"custom engine", r"\bunity\b", r"\bunreal\b"],
}

TECHNICAL_TOPIC_RULES = {
    "basic_building": [r"basic building", r"building in opensim", r"building challenge", r"constructing in minecraft"],
    "prims": [r"\bprim\b", r"\bprims\b"],
    "mesh": [r"\bmesh\b", r"3d model"],
    "scripting": [r"scripting", r"\bscript\b", r"redstone", r"npc"],
    "permissions": [r"\bpermission(s)?\b", r"access control"],
    "inventory": [r"\binventory\b"],
    "asset_management": [r"asset management", r"digital asset", r"content library"],
    "avatar_use": [r"\bavatar(s)?\b"],
    "navigation": [r"wayfinding", r"movement through space", r"navigation"],
    "object_interaction": [r"object interaction", r"touch_start", r"interact with objects"],
    "world_architecture": [r"world design", r"world architecture", r"environment"],
    "multiplayer_setup": [r"\bmultiplayer\b", r"\bserver\b", r"classroom mode"],
    "browser_requirements": [r"\bbrowser\b", r"\bbandwidth\b", r"\bdevice(s)?\b"],
}

GRADE_BAND_RULES = {
    "K-2": [r"\bk-?2\b", r"primary school", r"early elementary"],
    "3-5": [r"\b3-5\b", r"\bgrade 3\b", r"\bgrade 4\b", r"\bgrade 5\b", r"elementary"],
    "6-8": [r"\b6-8\b", r"middle school", r"\bgrade 6\b", r"\bgrade 7\b", r"\bgrade 8\b"],
    "9-12": [r"\b9-12\b", r"high school", r"secondary"],
    "higher_ed": [r"higher education", r"university", r"college", r"preservice"],
    "teacher_pd": [r"teacher", r"professional learning", r"district leader", r"preservice"],
}

SUBJECT_RULES = {
    "ELA": [r"\bela\b", r"language arts", r"writing", r"literature", r"reading"],
    "science": [r"science", r"biology", r"ecosystem", r"stem", r"ngss"],
    "social_studies": [r"social studies", r"history", r"civics", r"geography"],
    "math": [r"math", r"mathematics", r"geometry", r"numeracy", r"algebra"],
    "CTE": [r"\bcte\b", r"career", r"it asset", r"bim", r"engineering"],
    "arts": [r"arts", r"storytelling", r"design", r"media"],
}

EXPERIENCE_RULES = {
    "virtual_world_game": [r"serious game", r"game-based", r"minecraft", r"open world"],
    "role_play_simulation": [r"role[- ]play", r"simulation"],
    "branching_scenario": [r"branching", r"decision", r"scenario"],
    "interactive_storyworld": [r"story", r"narrative", r"storyworld"],
    "virtual_field_trip": [r"field trip", r"tour", r"visit"],
    "virtual_lab": [r"virtual lab", r"lab", r"science simulation"],
    "collaborative_build": [r"collaborative build", r"group build", r"build challenge"],
    "teacher_designed_world": [r"teacher-created", r"teacher designed", r"lesson plan"],
    "student_built_world": [r"student-built", r"student author", r"constructionist", r"build"],
}


@dataclass
class SourceAnalysis:
    file_path: Path
    text: str
    lines: list[str]
    lower_text: str


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value or "source"


def normalize_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def read_source(path: Path) -> SourceAnalysis:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = [line.rstrip() for line in text.splitlines()]
    return SourceAnalysis(path, text, lines, text.lower())


def first_heading(lines: Iterable[str]) -> str:
    for line in lines:
        if line.startswith("#"):
            return normalize_spaces(line.lstrip("#").strip())
    return ""


def infer_title(analysis: SourceAnalysis) -> str:
    heading = first_heading(analysis.lines)
    if heading:
        return heading
    return analysis.file_path.stem.replace("_", " ")


def infer_short_title(title: str) -> str:
    title = re.sub(r"\s*-\s*(researchgate|eric|wikipedia|mdpi|minecraft education|edutopia|pmc)\b.*$", "", title, flags=re.I)
    return title[:90].strip()


def extract_year(text: str) -> str:
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text[:4000])
    if years:
        counts = Counter(years)
        return counts.most_common(1)[0][0]
    return ""


def extract_authors(lines: list[str], text: str) -> list[str]:
    authors = []
    for i, line in enumerate(lines[:60]):
        stripped = normalize_spaces(re.sub(r"[*_`#>\[\]]", "", line))
        if re.match(r"^Authors?:\s*$", stripped, re.I):
            for candidate in lines[i + 1 : i + 10]:
                candidate = normalize_spaces(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", candidate))
                if not candidate or "university" in candidate.lower() or candidate.lower().startswith("download"):
                    continue
                if len(candidate.split()) <= 6 and re.search(r"[A-Z][a-z]+", candidate):
                    authors.append(candidate)
            break
    if not authors:
        m = re.search(r"\n([A-Z][A-Za-z.\-']+(?:,?\s+[A-Z][A-Za-z.\-']+){1,5})\s*\n(?:Abstract|1\. Introduction|Introduction)", text[:3000])
        if m:
            candidate = normalize_spaces(m.group(1))
            if 1 < len(candidate.split()) <= 8:
                parts = re.split(r",\s*|(?:\s+&\s+)|(?:\s+and\s+)", candidate)
                authors.extend([p.strip() for p in parts if p.strip() and len(p.strip().split()) <= 4])
    clean = []
    for author in authors:
        author = normalize_spaces(re.sub(r"\b\d+\b", "", author))
        if author and author not in clean:
            clean.append(author)
    return clean[:6]


def extract_doi_or_url(text: str) -> str:
    doi = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", text, flags=re.I)
    if doi:
        return doi.group(0)
    url = re.search(r"https?://[^\s)>\]]+", text)
    return url.group(0) if url else ""


def infer_source_type(title: str, text: str) -> str:
    lower_title = title.lower()
    if "chapter" in text[:1000].lower() or "in book:" in text[:1000].lower():
        return "chapter"
    if "journal" in text[:800].lower() or re.search(r"\babstract\b", text[:2000].lower()):
        return "research_article"
    if any(k in lower_title for k in ["tutorial", "how to", "documentation", "faq", "guide to", "basics"]):
        return "tutorial" if "tutorial" in lower_title or "basics" in lower_title else "technical_doc"
    if any(k in lower_title for k in ["lesson", "rubric", "resource", "activity", "challenge", "standards alignment"]):
        return "curriculum_resource"
    if "case study" in lower_title:
        return "case_study"
    if any(k in lower_title for k in ["guide", "best practices", "strategies"]):
        return "guide"
    if any(k in lower_title for k in ["open simulator", "opensim", "minecraft education", "lti", "scripting"]):
        return "technical_doc"
    return "web_page"


def match_vocab(text: str, rules: Union[dict[str, list[str]], list[tuple[str, list[str]]]]) -> list[str]:
    matches = []
    items = rules.items() if isinstance(rules, dict) else rules
    for label, patterns in items:
        if any(re.search(pattern, text, flags=re.I) for pattern in patterns):
            matches.append(label)
    return matches


def match_vocab_weighted(title_text: str, body_text: str, rules: Union[dict[str, list[str]], list[tuple[str, list[str]]]], threshold: int = 2) -> list[str]:
    matches = []
    items = rules.items() if isinstance(rules, dict) else rules
    for label, patterns in items:
        score = 0
        for pattern in patterns:
            if re.search(pattern, title_text, flags=re.I):
                score += 2
            elif re.search(pattern, body_text, flags=re.I):
                score += 1
        if score >= threshold:
            matches.append(label)
    return matches


def infer_dashboard_group(domains: list[str], source_type: str, title: str) -> str:
    if any(d in domains for d in ["assessment", "evidence_centered_design", "stealth_assessment", "analytics", "feedback"]):
        return "assessment"
    if any(d in domains for d in ["OpenSim", "Second_Life", "platform_skills"]) or source_type == "technical_doc":
        return "technical_build"
    if any(d in domains for d in ["project_based_learning", "instructional_design", "teacher_roles", "student_agency"]):
        return "pedagogy"
    if any(d in domains for d in ["virtual_worlds", "simulation", "role_play"]) and "research" in title.lower():
        return "research_foundations"
    if source_type in {"curriculum_resource", "case_study"}:
        return "examples"
    if any(d in domains for d in ["OpenSim", "Second_Life"]) or "minecraft" in title.lower():
        return "platforms"
    return "research_foundations"


def infer_relevance(domains: list[str], source_type: str, title: str) -> tuple[str, str]:
    score = 2
    reasons = []
    if any(d in domains for d in ["virtual_worlds", "instructional_design", "assessment", "OpenSim", "Second_Life", "world_building"]):
        score += 2
        reasons.append("directly informs immersive learning system design")
    if any(d in domains for d in ["evidence_centered_design", "stealth_assessment", "accessibility", "platform_skills"]):
        score += 1
        reasons.append("adds implementation guidance for assessment, support, or platform operations")
    if source_type in {"research_article", "chapter", "technical_doc"}:
        reasons.append("provides reusable patterns rather than isolated examples")
    if any(k in title.lower() for k in ["asset management", "privacy", "security", "classroom management"]):
        reasons.append("helps define operational constraints for school deployment")
    score = str(min(score, 5))
    why = normalize_spaces("; ".join(dict.fromkeys(reasons))) or "Provides context that can shape virtual-world instructional design decisions."
    return score, why


def infer_grade_bands(text: str) -> list[str]:
    bands = match_vocab(text, GRADE_BAND_RULES)
    if not bands and re.search(r"\bk-12\b", text, flags=re.I):
        return ["3-5", "6-8", "9-12"]
    return bands[:6]


def infer_subjects(text: str) -> list[str]:
    subjects = match_vocab(text, SUBJECT_RULES)
    if not subjects:
        subjects = ["cross_curricular"]
    elif len(subjects) > 1 and "science" in subjects and "math" in subjects:
        subjects.append("cross_curricular")
    seen = []
    for subject in subjects:
        if subject not in seen:
            seen.append(subject)
    return seen[:7]


def infer_experience_types(text: str, domains: list[str], source_type: str) -> list[str]:
    experiences = match_vocab(text, EXPERIENCE_RULES)
    if "virtual_worlds" in domains and "virtual_world_game" not in experiences:
        experiences.append("teacher_designed_world")
    if "world_building" in domains and "student_built_world" not in experiences:
        experiences.append("student_built_world")
    if "role_play" in domains and "role_play_simulation" not in experiences:
        experiences.append("role_play_simulation")
    if source_type == "technical_doc" and "teacher_designed_world" not in experiences:
        experiences.append("teacher_designed_world")
    seen = []
    for item in experiences:
        if item not in seen:
            seen.append(item)
    return seen[:9]


def infer_assessment_value(domains: list[str], models: list[str], evidence: list[str]) -> str:
    if not models and "assessment" not in domains:
        return ""
    parts = []
    if models:
        parts.append(f"Useful for designing {'/'.join(models[:2])} assessment patterns")
    if evidence:
        parts.append(f"and capturing evidence such as {', '.join(evidence[:3])}")
    return normalize_spaces(" ".join(parts)) + "."


def infer_technical_difficulty(topics: list[str], platforms: list[str], source_type: str) -> str:
    if "scripting" in topics or "mesh" in topics or "multiplayer_setup" in topics:
        return "high"
    if source_type == "technical_doc" or len(topics) >= 3 or len(platforms) >= 2:
        return "medium"
    return "low"


def infer_support_dependency(topics: list[str], source_type: str) -> str:
    if any(t in topics for t in ["scripting", "mesh", "multiplayer_setup", "browser_requirements"]):
        return "high"
    if source_type in {"technical_doc", "tutorial"} or topics:
        return "medium"
    return "low"


def infer_candidate_ssots(domains: list[str], platforms: list[str]) -> list[str]:
    targets = set()
    if any(d in domains for d in ["instructional_design", "project_based_learning", "experiential_learning", "teacher_roles"]):
        targets.update(["vw_lesson_design_ssot", "vw_pedagogical_patterns_ssot"])
    if any(d in domains for d in ["role_play", "simulation", "scenario_based_learning"]):
        targets.update(["vw_role_play_generator_ssot", "vw_storyworld_generator_ssot"])
    if any(d in domains for d in ["assessment", "evidence_centered_design", "stealth_assessment", "analytics", "feedback"]):
        targets.add("vw_assessment_engine_ssot")
    if any(d in domains for d in ["world_building", "platform_skills", "scripting"]) or platforms:
        targets.update(["vw_student_builder_workflow_ssot", "vw_platform_selection_ssot"])
    if "accessibility" in domains:
        targets.add("vw_accessibility_and_supports_ssot")
    if "standards_alignment" in domains:
        targets.add("vw_standards_alignment_ssot")
    if any(d in domains for d in ["teacher_roles", "instructional_design"]):
        targets.add("vw_teacher_prompting_ssot")
    return sorted(targets)


def infer_title_fallback_domains(title: str) -> list[str]:
    lower = title.lower()
    domains = []
    mapping = [
        ("teacher_roles", ["classroom", "teacher", "digital citizenship", "rules", "expectations"]),
        ("collaborative_learning", ["multiple users", "live editing", "collaborative", "shared"]),
        ("platform_skills", ["google docs", "asset management", "privacy", "security", "coppa", "ferpa", "optimization", "open worlds"]),
        ("world_building", ["open worlds", "worlds"]),
        ("virtual_worlds", ["virtual", "minecraft", "opensim", "second life", "open worlds"]),
        ("accessibility", ["accessibility", "blind", "deaf", "neurodiverse"]),
        ("project_based_learning", ["project-based", "pbl"]),
        ("storytelling", ["storytelling", "story"]),
    ]
    for label, terms in mapping:
        if any(term in lower for term in terms):
            domains.append(label)
    return domains


def infer_priority_targets(candidate: list[str], domains: list[str], source_type: str) -> list[str]:
    ordered = []
    priorities = [
        "vw_assessment_engine_ssot",
        "vw_lesson_design_ssot",
        "vw_pedagogical_patterns_ssot",
        "vw_role_play_generator_ssot",
        "vw_storyworld_generator_ssot",
        "vw_student_builder_workflow_ssot",
        "vw_platform_selection_ssot",
        "vw_teacher_prompting_ssot",
        "vw_standards_alignment_ssot",
        "vw_accessibility_and_supports_ssot",
    ]
    if source_type == "technical_doc":
        priorities = [
            "vw_student_builder_workflow_ssot",
            "vw_platform_selection_ssot",
            "vw_lesson_design_ssot",
        ] + priorities
    for item in priorities:
        if item in candidate and item not in ordered:
            ordered.append(item)
    return ordered[:3]


def infer_contribution_type(domains: list[str], source_type: str, title: str) -> str:
    if any(d in domains for d in ["assessment", "evidence_centered_design", "stealth_assessment"]):
        return "assessment_reference"
    if source_type == "technical_doc" or any(d in domains for d in ["platform_skills", "scripting", "world_building"]):
        return "technical_reference"
    if source_type in {"curriculum_resource", "case_study"}:
        return "example_bank"
    if any(d in domains for d in ["instructional_design", "project_based_learning", "teacher_roles", "student_agency"]):
        return "pedagogy_reference"
    if source_type in {"research_article", "chapter"} and any(d in domains for d in ["virtual_worlds", "simulation"]):
        return "core_foundation"
    return "supporting_evidence"


def infer_agent_modules(domains: list[str], source_type: str) -> list[str]:
    modules = {"planner"}
    if any(d in domains for d in ["world_building", "virtual_worlds", "OpenSim", "Second_Life", "platform_skills"]):
        modules.add("world_designer")
    if any(d in domains for d in ["role_play", "storytelling", "scenario_based_learning", "simulation"]):
        modules.add("scenario_writer")
    if any(d in domains for d in ["assessment", "evidence_centered_design", "stealth_assessment", "analytics"]):
        modules.add("assessment_designer")
    if any(d in domains for d in ["scripting", "platform_skills", "world_building"]):
        modules.add("technical_builder")
    if any(d in domains for d in ["instructional_design", "teacher_roles", "standards_alignment"]):
        modules.add("teacher_coach")
    if any(d in domains for d in ["student_agency", "project_based_learning", "accessibility"]):
        modules.add("student_guide")
    return [m for m in ["planner", "world_designer", "scenario_writer", "assessment_designer", "technical_builder", "teacher_coach", "student_guide"] if m in modules]


def build_takeaways(domains: list[str], assessment_models: list[str], platforms: list[str], topics: list[str], title: str) -> list[str]:
    takeaways = []
    if any(d in domains for d in ["assessment", "evidence_centered_design", "stealth_assessment"]):
        model = ", ".join(assessment_models[:2]) if assessment_models else "embedded assessment"
        takeaways.append(f"Use {model} patterns to tie learner evidence to actions inside the world instead of detached quizzes.")
    if any(d in domains for d in ["project_based_learning", "experiential_learning", "student_agency", "instructional_design", "collaborative_learning"]):
        takeaways.append("Design tasks as world actions with clear roles, choices, and artifacts so learning emerges through participation.")
    if platforms or topics:
        platform_text = ", ".join(platforms[:2]) if platforms else "the platform"
        topic_text = ", ".join(topics[:2]) if topics else "build workflow"
        takeaways.append(f"Account for {platform_text} implementation constraints such as {topic_text} before assigning complex student tasks.")
    if "accessibility" in domains:
        takeaways.append("Bake multimodal access into world interactions so navigation, communication, and feedback do not depend on a single sensory channel.")
    if not takeaways:
        takeaways.append(f"Treat {infer_short_title(title)} as supporting evidence when shaping the virtual-world design blueprint.")
    return takeaways[:3]


def build_value_sentence(title: str, domains: list[str], contribution_type: str) -> str:
    if contribution_type == "assessment_reference":
        return f"{infer_short_title(title)} helps define how an agent should capture and interpret evidence inside immersive learning experiences."
    if contribution_type == "technical_reference":
        return f"{infer_short_title(title)} provides implementation detail that can constrain or enable world-building workflows."
    if contribution_type == "example_bank":
        return f"{infer_short_title(title)} offers reusable patterns that can be translated into virtual world lessons, challenges, or builds."
    if contribution_type == "pedagogy_reference":
        return f"{infer_short_title(title)} sharpens how the agent should structure roles, tasks, and supports for immersive instruction."
    return f"{infer_short_title(title)} contributes design knowledge for building instructionally coherent virtual world experiences."


def build_best_entry_points(domains: list[str], platforms: list[str], source_type: str) -> list[str]:
    points = []
    if any(d in domains for d in ["assessment", "stealth_assessment", "evidence_centered_design"]):
        points.append("Use when defining evidence rules, progress signals, and in-world feedback logic.")
    if any(d in domains for d in ["instructional_design", "project_based_learning", "student_agency"]):
        points.append("Use when drafting activity loops, learner roles, and teacher facilitation moves.")
    if platforms or source_type == "technical_doc":
        points.append("Use when selecting platforms or translating learning goals into concrete build requirements.")
    if "accessibility" in domains:
        points.append("Use when adapting the world for multimodal access and participation.")
    return points[:3] or ["Use during early source triage to decide whether the document should influence design, implementation, or support layers."]


def build_extractive_notes(domains: list[str], models: list[str], topics: list[str], platforms: list[str], subjects: list[str]) -> list[str]:
    notes = []
    if domains:
        notes.append(f"Relevant domains: {', '.join(domains[:6])}.")
    if models:
        notes.append(f"Assessment emphasis: {', '.join(models[:4])}.")
    if topics or platforms:
        details = ", ".join((platforms + topics)[:6])
        notes.append(f"Technical emphasis: {details}.")
    if subjects:
        notes.append(f"Likely strongest subject use: {', '.join(subjects[:3])}.")
    return notes[:4]


def extract_quotes(lines: list[str]) -> list[dict]:
    candidates = []
    for idx, line in enumerate(lines[:220], start=1):
        cleaned = normalize_spaces(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line))
        if len(cleaned) < 70 or len(cleaned) > 240:
            continue
        if re.search(r"(supports?|allows?|should|assessment|learning|students?|teachers?|virtual|immersive|build)", cleaned, flags=re.I):
            candidates.append(
                {
                    "quote": cleaned,
                    "page_or_location": f"line {idx}",
                    "why_it_matters": "Captures language that can be translated into design, pedagogy, assessment, or implementation rules.",
                }
            )
        if len(candidates) == 2:
            break
    return candidates[:2]


def build_warnings(domains: list[str], source_type: str, title: str) -> list[str]:
    warnings = []
    if "accessibility" not in domains and any(d in domains for d in ["virtual_worlds", "simulation", "role_play"]):
        warnings.append("Check accessibility and alternate interaction pathways before reusing this pattern in a live virtual world.")
    if source_type == "web_page":
        warnings.append("Verify claims against stronger primary or empirical sources before using them as core system rules.")
    if any(k in title.lower() for k in ["privacy", "security", "coppa", "ferpa"]):
        warnings.append("Treat this source as a policy constraint layer rather than direct pedagogy guidance.")
    return warnings[:3]


def infer_confidence(analysis: SourceAnalysis, authors: list[str], year: str, source_type: str, domains: list[str]) -> tuple[str, bool]:
    score = 0
    if authors:
        score += 2
    if year:
        score += 1
    if domains:
        score += 2
    if source_type != "web_page":
        score += 1
    if len(analysis.text) > 2000:
        score += 1
    if analysis.text.count("\n") > 40:
        score += 1

    if score >= 6:
        return "high", False
    if score >= 3:
        return "medium", False

    # Sparse web captures often still have usable design intent when the topic is explicit.
    title = infer_title(analysis).lower()
    title_signals = [
        "virtual",
        "minecraft",
        "opensim",
        "assessment",
        "accessibility",
        "classroom",
        "learning",
        "simulation",
        "story",
        "build",
        "rubric",
        "lesson",
        "privacy",
        "security",
    ]
    if any(signal in title for signal in title_signals):
        return "medium", False

    return "low", True


def build_record(index: int, analysis: SourceAnalysis) -> dict:
    title = infer_title(analysis)
    short_title = infer_short_title(title)
    authors = extract_authors(analysis.lines, analysis.text)
    year = extract_year(analysis.text)
    source_type = infer_source_type(title, analysis.text)
    title_text = title.lower()
    focus_text = analysis.lower_text[:12000]
    domains = match_vocab_weighted(title_text, focus_text, KNOWLEDGE_DOMAIN_RULES, threshold=2)
    if "virtual_worlds" not in domains and re.search(r"virtual world|opensim|minecraft|second life", focus_text):
        domains.append("virtual_worlds")
    if not domains:
        domains = infer_title_fallback_domains(title)
    teacher_roles = match_vocab(focus_text, TEACHER_ROLE_RULES)
    student_roles = match_vocab(focus_text, STUDENT_ROLE_RULES)
    pedagogy = match_vocab(focus_text, PEDAGOGY_RULES)
    learning_characteristics = match_vocab(focus_text, LEARNING_CHARACTERISTIC_RULES)
    assessment_models = match_vocab(focus_text, ASSESSMENT_MODEL_RULES)
    evidence_types = match_vocab(focus_text, EVIDENCE_RULES)
    competencies = match_vocab(focus_text, COMPETENCY_RULES)
    feedback_modes = match_vocab(focus_text, FEEDBACK_RULES)
    platforms = match_vocab_weighted(title_text, focus_text, PLATFORM_RULES, threshold=2)
    technical_topics = match_vocab_weighted(title_text, focus_text, TECHNICAL_TOPIC_RULES, threshold=2)
    grade_bands = infer_grade_bands(focus_text)
    subjects = infer_subjects(focus_text)
    experiences = infer_experience_types(focus_text, domains, source_type)
    candidates = infer_candidate_ssots(domains, platforms)
    contribution_type = infer_contribution_type(domains, source_type, title)
    relevance_score, why_relevant = infer_relevance(domains, source_type, title)
    confidence, needs_review = infer_confidence(analysis, authors, year, source_type, domains)
    supports_assessment_design = bool(assessment_models or "assessment" in domains)
    supports_teacher_planning = bool(any(d in domains for d in ["instructional_design", "teacher_roles", "standards_alignment", "project_based_learning"]))
    supports_student_authoring = bool(any(d in domains for d in ["student_agency", "world_building", "storytelling", "constructionist_learning"]))
    record = {
        "id": f"src_{index:03d}",
        "title": title,
        "short_title": short_title,
        "source_file_name": analysis.file_path.name,
        "source_file_path": str(analysis.file_path),
        "source_format": analysis.file_path.suffix.lstrip(".").lower() or "other",
        "source_type": source_type,
        "authors": authors,
        "year": year,
        "publisher_or_journal": "",
        "doi_or_url": extract_doi_or_url(analysis.text),
        "citation_text": "",
        "high_level_relevance": {
            "overall_relevance_score": relevance_score,
            "why_relevant": why_relevant,
            "recommended_for_dashboard": relevance_score >= "3",
            "recommended_for_agent_training": relevance_score >= "4",
            "recommended_for_ssot_generation": relevance_score >= "3",
        },
        "knowledge_domains": domains,
        "instructional_use_profile": {
            "best_for_grade_bands": grade_bands,
            "best_for_subjects": subjects,
            "best_for_experience_types": experiences,
            "supports_instructional_standards_alignment": "standards_alignment" in domains,
            "supports_assessment_design": supports_assessment_design,
            "supports_teacher_planning": supports_teacher_planning,
            "supports_student_authoring": supports_student_authoring,
        },
        "pedagogical_extraction": {
            "teacher_role_prototypes": teacher_roles,
            "student_role_patterns": student_roles,
            "pedagogical_strategies": pedagogy,
            "learning_characteristics": learning_characteristics,
            "pedagogical_warnings": build_warnings(domains, source_type, title),
            "implementation_notes": build_extractive_notes(domains, [], technical_topics, platforms, subjects)[:2],
        },
        "assessment_extraction": {
            "assessment_models": assessment_models,
            "evidence_capture_types": evidence_types,
            "competencies_measured": competencies,
            "feedback_modes": feedback_modes,
            "assessment_notes": build_extractive_notes(domains, assessment_models, [], [], subjects)[:2],
            "assessment_design_value": infer_assessment_value(domains, assessment_models, evidence_types),
        },
        "technical_extraction": {
            "platforms_mentioned": platforms,
            "technical_topics": technical_topics,
            "technical_difficulty": infer_technical_difficulty(technical_topics, platforms, source_type),
            "teacher_dependency_on_technical_support": infer_support_dependency(technical_topics, source_type),
            "student_building_possible": bool(any(d in domains for d in ["world_building", "student_agency"]) or "Minecraft" in platforms or "OpenSim" in platforms),
            "technical_notes": build_extractive_notes(domains, [], technical_topics, platforms, subjects)[:3],
        },
        "ssot_mapping": {
            "candidate_ssot_docs": candidates,
            "priority_ssot_targets": infer_priority_targets(candidates, domains, source_type),
            "source_contribution_type": contribution_type,
            "recommended_agent_modules": infer_agent_modules(domains, source_type),
        },
        "dashboard_fields": {
            "dashboard_group": infer_dashboard_group(domains, source_type, title),
            "dashboard_tags": sorted(set(domains[:8] + platforms[:3] + subjects[:3])),
            "one_sentence_value": build_value_sentence(title, domains, contribution_type),
            "three_key_takeaways": build_takeaways(domains, assessment_models, platforms, technical_topics, title),
            "best_entry_points": build_best_entry_points(domains, platforms, source_type),
            "related_source_ids": [],
        },
        "traceability": {
            "important_quotes_or_passages": extract_quotes(analysis.lines),
            "extractive_notes": build_extractive_notes(domains, assessment_models, technical_topics, platforms, subjects),
            "confidence": confidence,
            "needs_human_review": needs_review,
        },
    }
    record["publisher_or_journal"] = infer_publisher_or_journal(analysis.lines, title)
    record["citation_text"] = build_citation(record)
    return record


def infer_publisher_or_journal(lines: list[str], title: str) -> str:
    for line in lines[:20]:
        cleaned = normalize_spaces(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line))
        if not cleaned or cleaned.startswith("#"):
            continue
        if any(token in cleaned.lower() for token in ["journal", "published by", "conference", "press", "education studies", "researchgate", "eric"]):
            return cleaned[:160]
    if "minecraft education" in title.lower():
        return "Minecraft Education"
    if "opensim" in title.lower() or "opensimulator" in title.lower():
        return "OpenSimulator community documentation"
    title_parts = [part.strip() for part in re.split(r"\s+-\s+", title) if part.strip()]
    if len(title_parts) > 1:
        tail = title_parts[-1]
        if 2 <= len(tail) <= 80:
            return tail
    return ""


def build_citation(record: dict) -> str:
    authors = ", ".join(record["authors"]) if record["authors"] else ""
    year = f"({record['year']})" if record["year"] else "(n.d.)"
    prefix = f"{authors} " if authors else ""
    citation = f"{prefix}{year}. {record['short_title']}."
    if record["publisher_or_journal"]:
        citation += f" {record['publisher_or_journal']}."
    if record["doi_or_url"]:
        citation += f" {record['doi_or_url']}"
    return normalize_spaces(citation)


def attach_related_sources(records: list[dict]) -> None:
    by_domain = defaultdict(list)
    for record in records:
        for domain in record["knowledge_domains"][:4]:
            by_domain[domain].append(record["id"])
    for record in records:
        related = []
        for domain in record["knowledge_domains"][:3]:
            for candidate in by_domain[domain]:
                if candidate != record["id"] and candidate not in related:
                    related.append(candidate)
                if len(related) == 5:
                    break
            if len(related) == 5:
                break
        record["dashboard_fields"]["related_source_ids"] = related


def build_dashboard_index(records: list[dict]) -> dict:
    return {
        "project_id": "vw_instruction_agent",
        "source_count": len(records),
        "dashboard_index": [
            {
                "id": record["id"],
                "title": record["title"],
                "short_title": record["short_title"],
                "dashboard_group": record["dashboard_fields"]["dashboard_group"],
                "overall_relevance_score": record["high_level_relevance"]["overall_relevance_score"],
                "knowledge_domains": record["knowledge_domains"],
                "source_contribution_type": record["ssot_mapping"]["source_contribution_type"],
                "priority_ssot_targets": record["ssot_mapping"]["priority_ssot_targets"],
                "recommended_agent_modules": record["ssot_mapping"]["recommended_agent_modules"],
                "one_sentence_value": record["dashboard_fields"]["one_sentence_value"],
                "source_file_path": record["source_file_path"],
                "confidence": record["traceability"]["confidence"],
                "needs_human_review": record["traceability"]["needs_human_review"],
            }
            for record in records
        ],
    }


def build_seed_map(records: list[dict]) -> dict:
    return {
        "project_id": "vw_instruction_agent",
        "source_to_ssot_map": [
            {
                "id": record["id"],
                "title": record["title"],
                "source_file_path": record["source_file_path"],
                "candidate_ssot_docs": record["ssot_mapping"]["candidate_ssot_docs"],
                "priority_ssot_targets": record["ssot_mapping"]["priority_ssot_targets"],
                "source_contribution_type": record["ssot_mapping"]["source_contribution_type"],
                "recommended_agent_modules": record["ssot_mapping"]["recommended_agent_modules"],
            }
            for record in records
        ],
    }


def main() -> None:
    source_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(os.environ.get("LM_VR_SOURCE_ROOT", str(DEFAULT_SOURCE_ROOT)))
    output_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(os.environ.get("LM_VR_OUTPUT_ROOT", str(DEFAULT_OUTPUT_ROOT)))
    output_root.mkdir(parents=True, exist_ok=True)
    source_files = sorted([path for path in source_root.glob("*.md") if path.is_file()])
    records = [build_record(index, read_source(path)) for index, path in enumerate(source_files, start=1)]
    attach_related_sources(records)

    manifest = {
        "project_manifest": {
            "project_id": "vw_instruction_agent",
            "project_title": "Virtual World Instruction Agent Source Manifest",
            "project_description": "Structured source manifest for building SSOT documents and agent-ready design assets for virtual-world-based instructional experiences aligned to standards.",
            "version": "1.0",
            "last_updated": "2026-03-21",
            "manifest_purpose": [
                "inventory_sources",
                "classify_relevance",
                "extract_design_knowledge",
                "identify_ssot_targets",
                "support_agent_construction",
            ],
            "source_files_root": str(source_root),
            "ssot_output_root": str(source_root),
            "dashboard_output_root": str(output_root),
        },
        "manifest": records,
    }

    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (output_root / "dashboard_index.json").write_text(json.dumps(build_dashboard_index(records), indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (output_root / "ssot_seed_map.json").write_text(json.dumps(build_seed_map(records), indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
