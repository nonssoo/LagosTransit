# Skills Documentation

## Overview
This project includes two custom Agent Skills for Claude Code, following 
the open SKILL.md standard.

## Skills

### `analysis`
**Location:** `.claude/skills/analysis/SKILL.md`  
**Purpose:** Examines text/data to extract patterns, themes, sentiment, 
or key insights, with quantified findings.  
**Triggers on:** requests to analyze, summarize findings, or extract insights.

### `transformation`
**Location:** `.claude/skills/transformation/SKILL.md`  
**Purpose:** Converts data from one format/structure to another 
(e.g. messy → clean, unstructured → structured), while preserving 
and validating information.  
**Triggers on:** requests to convert, transform, reformat, or restructure data.

## How Skills work
Claude automatically loads a skill's short description at the start of a 
session (cheap, low token cost). When a request matches a skill's described 
purpose, Claude loads the full SKILL.md body into context and follows its 
instructions. Skills can also be invoked directly with `/analysis` or 
`/transformation`.

## Testing
Each skill was tested against:
- A prompt clearly matching its purpose (should activate)
- A prompt clearly outside its purpose (should NOT activate)