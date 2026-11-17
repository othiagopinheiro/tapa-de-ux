# Color

Contrast is in accessibility (`accessibility.md`), and so is the “never color alone” rule. This file covers the role of each color.

**How to review (applies to every rule):**
1. List every color in use. In code, each loose value and each variable. In a screenshot, the colors that appear, given as estimates.
2. Merge the near-identical ones, those nobody can tell apart side by side.
3. Give each color a role: background, surface, border, text, supporting text, accent, error, success, warning. A color with no role is a candidate to go.

## One accent color

**Rule:** one accent color per screen, used on what matters most — the primary button, the active item. The action color goes only on what can be tapped: text that isn’t clickable doesn’t use it. Most of the screen stays neutral. As a reference, the 60-30-10 rule: about 60% neutral, 30% supporting color and 10% accent — it’s a guide, not a measurement.

**Why:** emphasis on everything is emphasis on nothing. And when the action color shows up on plain text, people tap and nothing happens.

**Wrong:** orange on the button, the icons, the titles and the badges of the same screen; a blue title like the links, that isn’t a link.

**Right:** orange only on the primary button and on the active item in the bar; titles and icons in neutral.

**Sources:** the 60-30-10 rule comes from interior design and is used in interfaces as a rule of thumb, with no screen study behind it (https://bootcamp.uxdesign.cc/the-60-30-10-color-rule-for-ui-design-32695d04a7c2).

## A status color has one meaning

**Rule:** red is error, loss or an action that deletes; green is success; yellow or amber is warning. A status color is never decoration, and a color doesn’t have two meanings in the same app. If the brand color matches a status color — a red brand, for example —, the status gets an icon and text so they aren’t confused.

**Why:** people learn color as a signal. Decorative red looks like an error, and green on a delete button invites the wrong tap.

**Wrong:** a red “New” badge; “Delete account” in green; the same blue for “selected” and for “information”.

**Right:** “New” in the accent color or in neutral; “Delete account” in red, with confirmation; each status with color, icon and text.

**Sources:** Apple, Color — avoid using the same color for different things (https://developer.apple.com/design/human-interface-guidelines/color).

## A closed palette

**Rule:** every color in the app comes from a short palette, and each color is named by its role. A loose color in the code becomes a palette color or goes. Near-identical colors become one.

**Why:** three near-identical blacks change nothing for the people looking, but they make the app look patched together — and every future adjustment has to be made in several places.

**Wrong:** 23 loose colors in the code, among them #333333, #343434 and #2F2F2F.

**Right:** a short palette, each color named by its role: background, surface, border, text, accent, error…

## Few grays, each with a role

**Rule:** text and supporting text are enough in most apps; a third text gray only if it passes 4.5:1. No gray lighter than the last text gray gets text — those are for borders, dividers and backgrounds.

**Why:** grays are where palettes bloat. Many text grays become a hierarchy nobody notices, and the lighter ones fail contrast.

**Wrong:** five text grays, two of them below 4.5:1.

**Right:** text and supporting text; the other grays only on borders and backgrounds.

## Both themes count the same

**Rule:** if the app has a light and a dark theme, each color is redefined for dark — not just inverted —, and contrast is measured again in both, and in high-contrast mode when the platform has one. A dark block inside the light theme — the header, a highlight card, a floating notice — switches its text, small text, divider and error together.

**Why:** a color that works on white disappears on black. The most common mistake is a dark block inheriting the dark text and becoming unreadable.

**Wrong:** dark red error text on a dark background; a dark card with its divider still dark; text that disappears in the dark theme because its color was hard-coded.

**Right:** each color with a light and a dark pair, and contrast checked in both.

**Sources:** Apple, Color — the app’s colors work in light, dark and high contrast (https://developer.apple.com/design/human-interface-guidelines/color).

## No decoration

**Rule:** gradients, shadows and glows only when they say something. Shadows are for what floats — sheets, menus, floating buttons. The background is flat. If a gradient seems to belong to the brand, the review asks before saying to remove it.

**Why:** decoration competes for attention with the content and with the accent. Shadows on everything erase the difference between what floats and what sits on the page.

**Wrong:** a purple and pink gradient on the background of every screen; a shadow on every card.

**Right:** flat background; cards with a thin border; a shadow only on the sheet that slides up.

## Palette harmony

**Rule:** the palette’s colors have a clear relationship on the color wheel — analogous (neighbors, calm tone), complementary (opposites, strong contrast, good for the accent), triadic or monochromatic (one hue in several shades). Supporting and status colors have saturation and lightness similar to the brand’s, and the grays lean slightly toward its hue. Two saturated opposite colors never sit one on top of the other.

**How to review:**
1. Say which relationship the palette follows, or that it follows none.
2. Point out the color that clashes and the pair that vibrates.
3. Propose the adjustment. The brand color isn’t up for debate; the rest of the palette adjusts to it. To generate options, Adobe Color builds palettes from these relationships, starting from the brand color.

**Why:** colors with no relationship make the app look assembled from pieces. A loud status color steals attention from the accent. And red text on blue tires the eyes and seems to shimmer, because the two colors seem to sit at different depths (chromostereopsis).

**Severity:** a vibrating pair is an error, because it gets in the way of reading. The rest is a suggestion.

**Wrong:** a sober navy brand with a neon lime-green success color; pure red text on a pure blue background; neutral, cool grays next to a warm orange brand.

**Right:** a blue brand, orange (its complement) only on the primary button, slightly bluish grays, and green and red status colors with the same strength as the blue.

**Sources:** color harmony (https://en.wikipedia.org/wiki/Color_harmony); red and blue together tire the eyes — Susan Weinschenk, “100 Things Every Designer Needs to Know About People”, item 50.
