# Information hierarchy

Text and space show what matters most and what belongs together. The first rule covers text; the next six, space.

**How to review space (applies to the six spacing rules):**
1. Measure the actual spacing. In code, the margin, padding and gap values. If you can open the screens, measure at the width of the smallest phone the app supports. In a screenshot, measurements are estimates, and the review says so.
2. Sort the problems into four groups: alignment, grouping, repetition and values off the scale.
3. Propose the scale and, for each problem, from how much to how much.

**Exceptions to the spacing rules:** fixed-height parts that have already been measured, such as the bottom bar and the header; optical adjustment (a circle inside a pill sits in the center, even off the scale); the space at the end of a list so the floating button doesn’t cover the last item; tiny badges.

## One style per role

**Rule:** every piece of text has a role — title, subtitle, body or supporting text — and each role has one style, the same across the whole app. Sizes come from a scale, and two neighboring roles are at least one step or one weight apart. What looks like a title is also a title in the code.

**Why:** people read a screen by its shape before they read the words. Two titles of different sizes say one matters more than the other, when it doesn’t. A title and body text that look alike hide where each part begins. And screen reader users navigate by the headings marked in the code: a title that only looks like a title disappears for them.

**How to review:**
1. List the project’s text styles — font, size, weight, line height and color — and give each one its role.
2. Find out whether the project already has a scale: size variables, text styles or the platform’s scale. If it has one and it’s coherent, it stands; don’t replace a scale that works.
3. Point out:
   - the same role with different styles;
   - neighboring roles without a step or a weight of difference;
   - sizes off the scale;
   - supporting text below the platform’s minimum, when it has one (on iOS, 11 pt, according to Apple);
   - text that looks like a title but isn’t one in the code (on the web, h1 to h6; in a native app, the accessibility heading trait), or headings out of order.
4. Propose:
   - with no scale, build one with a modular scale: base at the body size and a 1.25 ratio. With a base of 16: supporting text 13, body 16, subtitle 20, title 25. In a native app, the platform’s scale;
   - the table with one role per row and the list of what changes and where.

**Wrong:** the Profile title at 24px and the Settings title at 22px; a 17px subtitle next to 16px body text, in the same weight; large bold text that is a plain paragraph in the code.

**Right:** every screen title the same, every subtitle the same, all body text the same, all supporting text the same; each level clearly different from the next; and the title marked as a heading in the code.

**Sources:** modular scale — Tim Brown, “More Meaningful Typography”, A List Apart, 2011 (https://alistapart.com/article/more-meaningful-typography). iOS sizes and minimum — Apple, Human Interface Guidelines, Typography (https://developer.apple.com/design/human-interface-guidelines/typography). Title marked in the code — WCAG 1.3.1, level A (https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html).

## One spacing scale

**Rule:** every space comes from a scale of multiples of 4, and each step has a role. If the project already has a coherent scale, it stands. If not, propose this one:

| Step | For |
|---|---|
| 4 | text and its supporting line (title and year) |
| 8 | siblings in a group: list items, tags, buttons side by side, icon and text, label and field |
| 12 | parts of a card (image and text); side padding of a list item |
| 16 | screen margin on phones; card padding; between groups in a section |
| 24 | before a section title; screen margin on tablets and computers |
| 32 | between large sections with no dividing line |

**Why:** with a scale, the same relationship gets the same space everywhere. Without one, 6, 7, 10 and 14px show up — differences nobody notices, but that make everything slightly crooked.

**Wrong:** 6px in 29 places, plus 3, 5, 7, 9, 10, 14 and 18px.

**Right:** only the scale’s six steps. 1 and 2px only for borders, focus rings and hairlines.

**Sources:** 8-point grid, with 4 for small parts — Material Design, Layout (https://m2.material.io/design/layout).

## Close means together

**Rule:** the space inside a group is always smaller than the space around it. A section title sits closer to its own content than to the block above: 24 above, 8 below.

**Why:** the eye groups what is close before it reads (the law of proximity). Equal spacing everywhere leaves the screen with no groups, and a title far from its own content seems to belong to the block above.

**Wrong:** a title 16 from the block above and 10 from its own list; a 60px gap for no reason.

**Right:** 24 before the title, 8 between the title and the list, 8 between items.

**Sources:** Nielsen Norman Group, “Proximity Principle in Visual Design” (https://www.nngroup.com/articles/gestalt-proximity/).

## One margin line

**Rule:** everything that is read or tapped starts and ends on the same margin: 16 on phones, 24 on larger screens. That includes the close X and the buttons over an image.

**Why:** the margin is the line the eye follows down the screen. A part outside it makes the screen look crooked, even if people can’t say why.

**Wrong:** the X 8px from the edge and the title at 16; buttons over the image at 12; a box that starts 4px further in.

**Right:** everything on the same 16 line.

**Sources:** Apple, margins of 16 or 20 pt depending on screen size (https://developer.apple.com/documentation/uikit/positioning-content-within-layout-margins); Material, 16 on phones and 24 from tablets up (summary from SAP Fiori, which follows Material: https://www.sap.com/design-system/fiori-design-android/v26-4/foundations/adaptive-layout/layout-basics).

## Same component, same spacing

**Rule:** a component that repeats has the same measurements everywhere and the same padding on both sides.

**Why:** people recognize a component by its shape. With different measurements, it looks like two different components, or a mistake.

**Wrong:** a card with 8 on one side and 12 on the other; tags in four sizes.

**Right:** large card with 16 all around; list item with 8 above and below and 12 on the sides; one tag size.

## A line or a space, not both

**Rule:** to separate two blocks, use a line or a space. Never both, and never two lines in a row.

**Why:** a line already separates. Adding another line or a large gap looks like a new section, or a mistake.

**Wrong:** tabs with their own line and, 16px below, the block’s line.

**Right:** a single line, with the same space on both sides.

## Align to the letter, not the box

**Rule:** what lines up is what you see — the letter, the icon, the star —, not the invisible box around it. A text-only button at the start of a line is pulled outward by the size of its own padding.

**Why:** the box doesn’t show. People see the text 8px further in and think it’s misaligned.

**Wrong:** “Not interested” starts 8px after the title; the stars sit 7px inside the label.

**Right:** the button’s text starts on the same line as the title.
