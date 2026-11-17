---
name: tapa-de-ux-en
description: UX review for apps and screens — hierarchy, typography, accessibility, color, buttons, forms, states, UX writing and navigation. Use when reviewing, building or fixing an interface.
license: CC-BY-4.0
---

# UX rules

Rules for reviewing apps and for building screens that are right from the start. Each topic lives in a file in `rules/`. Open only the topics the task needs; in a general review (“review my app”), go through all of them, in the order of the table.

## Topics

| File | Open when the task involves |
|---|---|
| [rules/hierarchy.md](rules/hierarchy.md) | titles and text of different sizes, spacing, margins, alignment, grouping |
| [rules/typography.md](rules/typography.md) | fonts, weights, reading size, line height, text alignment, capitalization |
| [rules/accessibility.md](rules/accessibility.md) | touch targets, contrast, screen readers, focus, text that grows, animation |
| [rules/color.md](rules/color.md) | palette, accent color, status colors, dark theme, shadows and gradients |
| [rules/buttons-and-actions.md](rules/buttons-and-actions.md) | buttons, actions, confirmations, deleting, canceling, response to a tap |
| [rules/forms.md](rules/forms.md) | fields, labels, keyboard, input errors, choices |
| [rules/states.md](rules/states.md) | empty screen, loading, error, offline, success, missing data |
| [rules/ux-writing.md](rules/ux-writing.md) | interface text: names, verbs, voice, formats, punctuation |
| [rules/navigation.md](rules/navigation.md) | menus, navigation bar, back, dialogs and sheets |
| [rules/psychology.md](rules/psychology.md) | applied psychology laws: Jakob, Hick, Fitts, memory, isolation, peak-end, Tesler |

## How to review

1. See what you have: the project’s code, a few screens or a screenshot. Review everything you have and say what wasn’t reviewed. Never say you looked at the whole app if you saw one screen.
2. Open the files for the task’s topics and follow each one’s “How to review”.
3. Compare the whole app, not just the screen: the same thing done two ways is a problem.
4. List the problems in order of how much they get in people’s way: first what stops someone from using the app, then what confuses, then the finish. For each one: the rule’s name, where it is (file and line, or the screen), what’s wrong and what right looks like.
5. Propose; don’t change. Only change the app if the person asks.
6. The project’s design system and the explicit request of the person you’re working with come before these rules. If a rule clashes with them, follow the project and flag the conflict in one sentence.
7. When a rule says to ask — the tone of a font, a gradient that may belong to the brand —, ask before judging.
8. Answer in the language of the conversation. The examples are in English; in an app in another language, apply the same rule with that language’s conventions.

## When building or changing a screen

Follow the rules of the topics the task touches, without needing to cite them.
