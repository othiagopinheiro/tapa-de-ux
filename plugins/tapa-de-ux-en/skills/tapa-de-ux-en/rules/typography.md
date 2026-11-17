# Typography

The size scale and the title marked in the code are in hierarchy (`hierarchy.md`). This file covers the font itself: which one, how many weights, at what size, with what spacing and alignment.

**How to review (applies to every rule):**
1. List the fonts in use. In code, by name, by font files and by theme. In a screenshot, by category — serif, sans serif, monospace, script — and by the likely family, given as a guess (“looks like …”).
2. Look for fonts that slipped in by accident. On the web, buttons and form fields don’t inherit the page font and render in the system font; and a font that failed to load is replaced by the fallback.

## One font family

**Rule:** one family across the app, using its weights. If there is a second one, it has the same structure — same proportions, same x-height — and a clear role, such as titles only. Never two near-identical fonts on the same screen.

**Why:** each font is a voice. With several, the screen looks like a collage. With two near-identical ones, it looks like one failed to load.

**Wrong:** titles in one font, body in another and buttons in a third (the system font, by accident).

**Right:** one family for everything; or SF Pro Text for body and SF Pro Display for titles, the same Apple family in two cuts.

## Few weights, and the right one for reading

**Rule:** two or three weights in the app, each with a role — for example, regular for body, semibold for titles and highlights, bold for large numbers. Running text in regular. Thin strokes (light, thin) only at large sizes.

**Why:** many weights become noise and dilute emphasis. A thin stroke at a small size fades away, more so with low contrast or in sunlight.

**Wrong:** five weights in the same app; running text in 14px light; a whole paragraph in bold.

**Right:** regular, semibold and bold, each in its role.

## Reading size

**Rule:** running text at least 16px on the web and on Android, and 17 pt on iPhone. On the web, a form field under 16px makes the iPhone zoom in when someone taps it. An older audience needs more.

**Why:** that is the size the platforms themselves use for body text. Below it, long reading tires people out.

**Wrong:** running text at 14px on a phone; a 14px search field that zooms in on tap.

**Right:** text and fields at 16px or more.

**Sources:** Apple, Body at 17 pt at the default size (https://developer.apple.com/design/human-interface-guidelines/typography); Material 3, body large at 16 (reproduction of the scale: https://matraic.github.io/m3e/styles/typography.html).

## Line height and text spacing

**Rule:**
- line height of about 1.5 in running text, tighter in titles;
- the font’s own letter spacing in text; slightly open in all caps;
- more space between paragraphs than between lines;
- up to 80 characters per line;
- the layout holds when people increase these spacings.

**Why:** with tight line height, lines tangle. With long lines, the eye gets lost going back to the start of the next one. And a title with body line height looks like two titles.

**Wrong:** a paragraph with 1.1 line height; text spanning the full width of a desktop screen; a two-line title that looks like two.

**Right:** text at 1.5; titles with tight line height; lines of up to 80 characters.

**Sources:** WCAG 1.4.8, up to 80 characters per line and line spacing of 1.5, level AAA (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation); WCAG 1.4.12, nothing is lost when people increase text spacing, level AA (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Text alignment

**Rule:**
- running text aligns left;
- centered only in blocks of up to two or three lines, such as the title and sentence of an empty state or a short notice;
- justified, never;
- one alignment per block;
- numbers in a column align right, with equal-width (tabular) figures;
- different sizes side by side align on the baseline, the line the letters sit on.

**Why:** the eye always goes back to the same point to start a line; in centered text, each line starts somewhere else, and reading gets tiring from the third line on. Justified text opens uneven gaps between words, worse on phones, where few words fit per line. And right-aligned numbers put ones under ones, to compare at a glance.

**Wrong:** a five-line paragraph centered; justified text on a phone; a centered title and left-aligned text in the same card; prices aligned left ($9.90 above $120.00); a large “$25” and a small “/month” aligned at the top.

**Right:** running text on the left; centered only for the title and the short sentence of an empty state; values on the right, decimal point under decimal point; “$25” and “/month” sitting on the same line.

**Sources:** WCAG 1.4.8, text not justified, level AAA (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation).

## Sentence case

**Rule:** titles, buttons and menus in sentence case: a capital only on the first letter and on proper nouns. All caps only in a short label of one or two words.

**Why:** sentence case is how people read all the rest of the text, so it flows. A capital on every word breaks the reading, and all caps everywhere weighs the screen down, reads like shouting and erases the emphasis of what needs it.

**Exception:** follow the platform’s convention. In English, Apple asks for title-style capitalization in buttons (“Add Movie”) and in alert titles that aren’t complete sentences. Whatever the style, it is one per element type, the same everywhere.

**Wrong:** “MY MOVIES” as a title; “See All Movies” on one button and “See all movies” on the next.

**Right:** “My movies”; “See all movies”; “NEW” as a short label.

**Sources:** Microsoft Writing Style Guide, Capitalization — sentence case as the default (https://learn.microsoft.com/en-us/style-guide/capitalization); Apple, Writing — one capitalization style per element type, always the same (https://developer.apple.com/design/human-interface-guidelines/writing); Apple, Alerts — in English, title-style capitalization in button titles (https://developer.apple.com/design/human-interface-guidelines/alerts).

## The font fits the product

**Rule:** the font’s personality fits the product’s goal and tone. The review doesn’t decide this alone: it identifies the font, says what tone it conveys and asks whether that’s the tone the product wants. For the small interface text — buttons, labels, numbers —, the font is always one made for screens.

**How to review:**
1. Identify the font: the exact name from the code, or the category and a guess from a screenshot.
2. Say in one sentence the tone it conveys: traditional, technical, friendly, sophisticated, childlike.
3. If the person hasn’t said what the product’s goal is, ask before judging.
4. If it doesn’t fit, suggest one or two alternatives, without changing anything on your own.

**Why:** the font speaks before the text. A classic serif in a gym app conveys an old-fashioned tone, and that may be on purpose or a mistake. Only the people who make the product know.

**Wrong:** rejecting a serif without asking; letting a wedding-invitation script in a work to-do app pass without comment.

**Right:** “The titles look like Playfair Display, a classic serif that conveys a traditional, sophisticated tone. Is that the tone of the app? If the idea is to sound modern and direct, a sans serif like Inter would do that.”
