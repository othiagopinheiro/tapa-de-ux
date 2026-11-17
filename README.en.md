# ux-rules

UX rules for Claude to review apps. You ask “review this app” or “review this screen”, and Claude applies the rules on its own, without you having to call the skill by name.

*[Versão em português](README.md). The rules are the same in both languages; the skill answers in the language you write in.*

## What’s inside

70 rules in 10 topics. Each rule says what to do, why, a wrong example, a right one and where it comes from.

| Topic | What the review looks at |
|---|---|
| Information hierarchy | one style per text role, the size scale and the spacing scale |
| Typography | family, weights, reading size, line height, alignment, capitals, the tone of the font |
| Accessibility | touch targets, contrast, color, screen readers, focus, text that grows, motion |
| Color | accent, status colors, palette, grays, dark theme, decoration, harmony |
| Buttons and actions | primary button, button types, names, deleting, leaving, response to a tap |
| Forms | labels, required fields, keyboard, formats, errors, order, choices |
| States | empty screen, waiting, errors, offline, success, missing data |
| UX writing | consistent names, verbs, voice, messages, formats and writing |
| Navigation | the bar, where am I, back, names, paths, dialogs |
| Applied psychology | the laws of Jakob, Hick and Fitts, memory, isolation, peak-end, Tesler |

## Install in Claude Code

Inside Claude Code:

```
/plugin marketplace add othiagopinheiro/ux-rules
/plugin install ux-rules@ux-rules
```

Or in the terminal:

```
claude plugin marketplace add othiagopinheiro/ux-rules
claude plugin install ux-rules@ux-rules
```

If your computer has no SSH key registered on GitHub, use the full address in the first command:

```
/plugin marketplace add https://github.com/othiagopinheiro/ux-rules.git
```

Install one language only: `ux-rules` (English) or `regras-ux` (Portuguese). With both, the same review would show up twice.

### Getting new rules

New rules come in over time. Claude Code doesn’t update third-party skills on its own: turn it on once in `/plugin` → Marketplaces → ux-rules → Enable auto-update. Or update by hand:

```
claude plugin marketplace update ux-rules
claude plugin update ux-rules@ux-rules
```

## Use in Claude (claude.ai)

1. Download [dist/ux-rules.zip](dist/ux-rules.zip).
2. In Claude, open Customize → Skills → “+” → Upload a skill and choose the ZIP.

Here, new rules don’t arrive on their own: download the ZIP again and upload it once more.

## How to use

- “Review the interface of this app.”
- “Review this screenshot of the sign-up screen.”
- “Build the settings screen following the UX rules.”

The review points out each problem with the rule’s name, where it is and what right looks like, from what gets in the way most to the finishing touches. It proposes and changes nothing unless you ask. Your project’s design system comes before the rules: if a rule clashes with it, the review follows the project and tells you.

## Credit

Rules by Thiago Pinheiro, UX designer. The laws and numbers cited have their original source next to each rule. The Portuguese version is the original; this one is adapted from it.

[license to be decided before the repository is opened]
