# Tapa de UX

Ever been asked to “just slap some UX on it”? In Brazil, that’s a *tapa de UX*, a “UX slap”: a quick screen at the end, as if UX were a coat of paint. This skill is the opposite: UX rules, each with its source, for your AI to review apps. You ask “review this app” or “review this screen”, and your AI applies the rules on its own, without you having to call the skill by name.

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
/plugin marketplace add othiagopinheiro/tapa-de-ux
/plugin install tapa-de-ux-en@tapa-de-ux
```

Or in the terminal:

```
claude plugin marketplace add othiagopinheiro/tapa-de-ux
claude plugin install tapa-de-ux-en@tapa-de-ux
```

If your computer has no SSH key registered on GitHub, use the full address in the first command:

```
/plugin marketplace add https://github.com/othiagopinheiro/tapa-de-ux.git
```

Install one language only: `tapa-de-ux-en` (English) or `tapa-de-ux` (Portuguese). With both, the same review would show up twice.

### Getting new rules

New rules come in over time. Claude Code doesn’t update third-party skills on its own: turn it on once in `/plugin` → Marketplaces → tapa-de-ux → Enable auto-update. Or update by hand:

```
claude plugin marketplace update tapa-de-ux
claude plugin update tapa-de-ux-en@tapa-de-ux
```

## Use in Claude (claude.ai)

1. Download [dist/tapa-de-ux-en.zip](dist/tapa-de-ux-en.zip).
2. In Claude, open Customize → Skills → “+” → Upload a skill and choose the ZIP.

Here, new rules don’t arrive on their own: download the ZIP again and upload it once more.

## Use in other tools

The skill follows the open [Agent Skills](https://agentskills.io/) standard, which other tools also read, such as [Codex](https://learn.chatgpt.com/docs/build-skills), [Cursor](https://cursor.com/docs/skills), [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) and [Gemini CLI](https://geminicli.com/docs/cli/skills/). In those tools:

1. Download [dist/tapa-de-ux-en.zip](dist/tapa-de-ux-en.zip).
2. Unzip it into the `.agents/skills` folder: the one in your home folder works for every project; the one inside a project, for that project only. In the terminal, for every project:

   ```
   mkdir -p ~/.agents/skills
   unzip ~/Downloads/tapa-de-ux-en.zip -d ~/.agents/skills
   ```

3. Restart the tool.

In [Antigravity CLI](https://antigravity.google/docs/skills), the home folder is different: `~/.gemini/config/skills`.

Here too, new rules don’t arrive on their own: delete the `tapa-de-ux-en` folder, download the ZIP again and unzip it. The skill was tested in Claude. In other tools the rules are the same, but how each one uses the skill may vary.

## How to use

- “Review the interface of this app.”
- “Review this screenshot of the sign-up screen.”
- “Build the settings screen following the UX rules.”

The review points out each problem with the rule’s name, where it is and what right looks like, from what gets in the way most to the finishing touches. It proposes and changes nothing unless you ask. Your project’s design system comes before the rules: if a rule clashes with it, the review follows the project and tells you.

## Credit and license

Rules by Thiago Pinheiro, UX designer. The laws and numbers cited have their original source next to each rule. The Portuguese version is the original; this one is adapted from it.

Licensed under [CC BY 4.0](LICENSE): you may copy, adapt and share the rules, including in paid work, as long as you credit Thiago Pinheiro, link to the license and say what you changed.
