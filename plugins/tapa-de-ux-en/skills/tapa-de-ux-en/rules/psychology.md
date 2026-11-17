# Applied psychology

Psychology laws that become checks in the review. The idea of each law is in the public domain; the text here is original, and the source is the original research. Several of them meet other sections: Fitts with touch targets (`accessibility.md`), isolation with the accent color (`color.md`) and the primary button (`buttons-and-actions.md`), Jakob with consistency (`ux-writing.md`), Tesler with forms (`forms.md`).

**How to review (applies to every rule):**
1. For each law, look on the screens for what the rule describes, one by one.
2. In the review, name the law only when it helps explain the problem; what matters is what changes on the screen.
3. A law isn’t a magic number: none of them says “at most 7 items” or “3 clicks”. If a review lands on a number like that, it’s a sign of a misapplied law.

## Jakob’s law

**What it says:** people spend most of their time in other apps; so they expect yours to work like the ones they already know.

**Rule:** where there is a known way — a magnifying glass to search, back in the top corner or by gesture, the account in the corner, pulling the list down to refresh —, the app follows it. Invent only when the gain is clear, and then explain it.

**Why:** each invention is something people have to learn. What they already know from other apps is learning for free.

**Wrong:** a heart for “save for later” and a star for “like”; search hidden inside Profile.

**Right:** a magnifying glass to search, a heart to like; the gestures and places the platform already teaches.

**Sources:** Jakob Nielsen, “End of Web Design”, 2000 (https://www.nngroup.com/articles/end-of-web-design/).

## Hick’s law

**What it says:** the more options people have to compare, the longer they take to decide.

**Rule:** at each moment, show the options for that decision, with the most likely one highlighted; group long choices or split them into steps. Hiding what people are looking for doesn’t count: in a list they know and that is in order — countries, contacts —, finding is quick, and search takes care of the length.

**Why:** twelve options of equal weight force people to read them all before choosing. Three clear ones, with one highlighted, are decided at a glance.

**Wrong:** a home screen with twelve identical buttons; a list of thirty settings with no grouping at all.

**Right:** the three most used actions in view, the main one highlighted; the settings grouped by topic, with clear names.

**Sources:** W. E. Hick, “On the rate of gain of information”, Quarterly Journal of Experimental Psychology, 1952; R. Hyman, “Stimulus information as a determinant of reaction time”, Journal of Experimental Psychology, 1953; the law’s limits (https://en.wikipedia.org/wiki/Hick%27s_law).

## Fitts’s law

**What it says:** the time to hit a target depends on the distance to it and on its size: close and large is fast; far and small is slow and misses more.

**Rule:** the most used action is large and sits close to where people already are — right below the last field, next to the item it affects. Frequent actions come first in lists and menus. And, by the same law in reverse, the action that deletes sits away from the common ones, so it isn’t tapped by mistake.

**Why:** every extra centimeter and every missing millimeter cost time and errors, every time people use the app.

**Wrong:** “Delete” right next to “Save”; a small submit button in the corner opposite the last field.

**Right:** a wide “Save”, right below the last field; “Delete” set apart, away from it.

**Sources:** Paul M. Fitts, “The information capacity of the human motor system in controlling the amplitude of movement”, Journal of Experimental Psychology, 1954; Nielsen Norman Group, “Fitts's Law and Its Applications in UX” (https://www.nngroup.com/articles/fitts-law/).

## Memory limits

**What it says:** short-term memory holds few things at once, and for a short time — Miller spoke of seven, plus or minus two, in 1956; later studies speak of about four chunks. Recognizing what’s in view is much easier than remembering.

**Rule:** the app doesn’t ask people to remember — it shows. What they need from the previous screen stays in view; choices appear summarized before confirming; what is being compared sits side by side; long numbers come in chunks. The limit doesn’t mean cutting a menu down to seven items: a menu is read, not memorized.

**Why:** each thing people have to keep in their head is a chance to make a mistake or to go back and check.

**Wrong:** the screen asks for the code that was on the previous screen; three plans to compare, each on its own screen.

**Right:** the code stays in view or is filled in automatically; the plans side by side; an order summary before confirming.

**Sources:** George A. Miller, “The Magical Number Seven, Plus or Minus Two”, Psychological Review, 1956; Nelson Cowan, “The magical number 4 in short-term memory”, Behavioral and Brain Sciences, 2001 (https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two); Nielsen Norman Group, “Short-Term Memory and Web Usability” — including on the seven-item menu myth (https://www.nngroup.com/articles/short-term-memory-and-web-usability/) and “Memory Recognition and Recall in User Interfaces” (https://www.nngroup.com/articles/recognition-and-recall/).

## Isolation effect

**What it says:** among similar things, the one that’s different is the one that gets noticed and remembered (the Von Restorff effect).

**Rule:** what matters most on the screen is the only thing that’s different — in color, size or shape, and not in color alone. If everything stands out, nothing does.

**Why:** emphasis works by contrast with the rest. Three highlights on the same screen cancel each other out.

**Wrong:** colored badges, banners and an orange button competing on the same screen; the recommended plan looking like the others.

**Right:** a single different element per screen — the primary button, or the recommended plan with a badge and a border.

**Sources:** Hedwig von Restorff, “Über die Wirkung von Bereichsbildungen im Spurenfeld”, Psychologische Forschung, 1933 (https://en.wikipedia.org/wiki/Von_Restorff_effect); WCAG 1.4.1, don’t rely on color alone (https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Peak-end rule

**What it says:** we judge an experience by its most intense moment and by its end, more than by the average.

**Rule:** find the peaks of each flow — the error at the tensest moment, the first result, placing the order — and take extra care with them and with the end. The end is designed with the same care as the beginning: a flow that ends on an empty screen or a curt error spoils the memory of everything that came before.

**Why:** a long, well-made experience is remembered by its worst moment and by its end. If the end is curt, that’s what sticks.

**Wrong:** a long import that ends on an empty screen; a curt error right when the order is placed.

**Right:** “Done: your map has 12 countries. Want to add the next movie?”; in the error, what happened, what was saved and how to carry on.

**Sources:** Daniel Kahneman, Barbara L. Fredrickson, Charles A. Schreiber and Donald A. Redelmeier, “When More Pain Is Preferred to Less: Adding a Better End”, Psychological Science, 1993; Nielsen Norman Group, “The Peak–End Rule” (https://www.nngroup.com/articles/peak-end-rule/).

## Tesler’s law

**What it says:** every task has a complicated part that can’t be eliminated; you can only decide who deals with it — the app or the person (conservation of complexity).

**Rule:** the app takes on as much of that part as it can: it fills in what it already knows, calculates what it can, picks a sensible default, accepts people’s format. Simplifying isn’t hiding: removing an option people need only passes the work on to them.

**Why:** everything the app leaves for people to do, they do every time. What the app does, it does once and for all.

**Wrong:** asking people to calculate their age, convert a currency or type in the system’s format; “simplifying” by removing the filter everyone uses.

**Right:** the age calculated from the date; the value converted on the spot; the most used filter in view, with a default already chosen.

**Sources:** Larry Tesler, at Xerox PARC, in the 1980s — the work of complexity should fall on whoever makes the app, not on whoever uses it (https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity).
