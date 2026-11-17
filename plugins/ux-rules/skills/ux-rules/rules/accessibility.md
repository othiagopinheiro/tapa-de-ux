# Accessibility

**How to review (applies to every rule):**
1. Also review what is hidden: open modals, menus and inactive tabs before measuring.
2. Measure contrast with a number, not by eye, and in both themes, if there are two.
3. With only a screenshot, contrast and touch targets are estimates; names, order and focus can’t be seen in a screenshot, and the review says they were left out.
4. First what blocks someone: a control with no name, contrast below the minimum, a target below the floor.

**Exceptions (apply to every rule):** a link in the middle of running text (touch target); logos and disabled controls (contrast); animation that is essential to what the screen does (motion).

The title marked in the code and the minimum text size are in the hierarchy rule (`hierarchy.md`).

## Touch target

**Rule:** everything that can be tapped has an area of at least 44 × 44 on iPhone and on the web, and 48 × 48 on Android. The drawing can be smaller; the area can’t. And one target’s area doesn’t overlap its neighbor’s.

**Why:** a finger isn’t a cursor. Small targets cause missed taps, and more so for people with tremors or who use their phone while walking.

**Severity:** below the target size is a warning. Below the floor is an error: 28 × 28 pt for Apple, 24 × 24px for WCAG.

**Wrong:** a 20px X with no area around it; 24px icons packed together in a bar.

**Right:** the X drawn at 20px inside a 44 area; icons side by side, each with 44, without overlapping.

**Sources:** Apple, Accessibility — 44 × 44 pt is the default size and 28 × 28 pt the minimum on iOS and iPadOS (https://developer.apple.com/design/human-interface-guidelines/accessibility). Android, 48 × 48dp (https://developer.android.com/guide/topics/ui/accessibility/apps). WCAG 2.5.8, 24px, level AA (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), and 2.5.5, 44px, level AAA (https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced).

## Contrast

**Rule:** text at 4.5:1 against its background. Large text (24px, or 18.7px bold) at 3:1. Icons, field borders and focus rings at 3:1. The measurement applies in both themes, over the background and over each surface, and includes the example text inside a field.

**Why:** with low contrast, people with low vision, older people and people in sunlight can’t read.

**Wrong:** a #999 caption on white (2.85:1); a field with a #E5E5E5 border (1.26:1), which is the only clue to where it is.

**Right:** #767676 is the lightest gray that passes on white (4.54:1). For the border, #949494 (3.03:1).

**Sources:** WCAG 1.4.3 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and 1.4.11 (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Never color alone

**Rule:** status, errors, warnings and selection have an icon or text besides color.

**Why:** people who can’t tell colors apart, or who see the screen through a color filter, lose the information.

**Wrong:** a field with an error marked only by the red border; an active tab shown only by a different color.

**Right:** red border, icon and the message “Enter a valid email address”; an active tab with color and weight.

**Sources:** WCAG 1.4.1 (https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Every control says what it is

**Rule:** every control has a name, role and state that a screen reader can read:
- an icon-only button has a name (“Close”, not “X”);
- an informative image has a description, and a decorative image is hidden from the screen reader;
- tabs and menus say whether they’re selected or open;
- the control is the native one: a real button, not a box that responds to taps.

**Why:** a screen reader reads the code, not the screen. An icon with no name becomes just “button”, or nothing.

**Wrong:** a trash icon with no name; a clickable box that isn’t a button; a selected tab announced like the others.

**Right:** “Delete movie, button”; “My movies, tab, selected”.

**Sources:** WCAG 1.1.1 (https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) and 4.1.2 (https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html).

## Visible focus, in order

**Rule:** everything clickable shows where focus is, with an outline at 3:1. Focus, and VoiceOver and TalkBack reading, move in the same order the screen is read.

**Why:** people who navigate by keyboard or screen reader need to know where they are. With the order scrambled, parts of the screen disappear.

**Wrong:** focus removed with nothing in its place; focus that jumps from the top to the footer and back.

**Right:** a 2 to 3px outline, with an offset, in the action color; the order the same as the screen’s.

**Sources:** WCAG 2.4.7 (https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) and 2.4.3 (https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html).

## Text grows without breaking

**Rule:** the app respects the text size chosen on the device — Dynamic Type on iPhone, font size on Android, 200% zoom in the browser — and nothing is lost: no cut-off text, no overlapping text, no sideways scrolling from 320px.

**Why:** people with low vision increase the device’s text size. A locked size ignores them, and a rigid layout cuts their text.

**Wrong:** a fixed size that ignores the setting; a fixed-height button that cuts the text at large sizes.

**Right:** sizes that follow the setting, and components that grow in height.

**Sources:** WCAG 1.4.4, 200% (https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), and 1.4.10, 320px (https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

## Motion under control

**Rule:** when people ask the device for less motion, movement animations stop or become a simple fade.

**Why:** large motion on screen causes nausea and dizziness in people with motion sensitivity.

**Wrong:** the screen slides and zooms even with “Reduce Motion” on.

**Right:** with the option on, screen changes happen without sliding, and smooth scrolling is off.

**Sources:** WCAG 2.3.3, level AAA (https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
