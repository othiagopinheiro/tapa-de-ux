# Buttons and actions

Touch targets are in accessibility (`accessibility.md`), and the accent color in color (`color.md`).

**How to review (applies to every rule):**
1. Make an inventory of everything clickable: how many kinds of button exist, where each one appears and how many times.
2. On each screen, say which action is the primary one and whether it really is the one that stands out most.
3. Read each button’s text out of context: can you tell what happens?
4. Check the actions that delete and the ones that take time: do they have undo or confirmation? Do they show they’re loading?

## One primary button per screen

**Rule:** each screen has one primary action — what the person came to do —, in a filled button in the accent color. The other actions weigh less than it. An action that deletes is never the primary one.

**Why:** with two identical buttons side by side, people stop to think. With one, they know where to go.

**Wrong:** “Watch later” and “Seen it” in the same size and color; “Delete” in filled blue, as the primary.

**Right:** “Seen it” filled, “Watch later” outlined, “Not interested” as text only.

**Sources:** Apple, Buttons — one or two prominent buttons per screen, and a destructive action never in the primary role (https://developer.apple.com/design/human-interface-guidelines/buttons).

## Four button types, few sizes

**Rule:** four types, each with a role:
- primary: filled, in the accent color;
- secondary: outlined;
- subtle: text only, for a light action or a way out;
- destructive: red, only for what deletes.

And few sizes — for example, large in the footer, regular (44) and small (36, inside a list, with a touch area around it). The same action looks the same across the whole app.

**Why:** each new type is a new question (“is this more important?”). With four, people learn the weight of each action from its shape.

**Wrong:** 17 kinds of button in the same app; “Watch later” looking one way on Home and another way in the list.

**Right:** four types and three sizes, each with a defined use.

## Buttons look like buttons; tags don’t

**Rule:** a button has a fill or an outline; text alone only for the lowest-weight action. A tag — a badge, a status — has no border and isn’t clickable. What looks clickable is clickable, and the other way around.

**Why:** people decide where to tap by shape. A button that doesn’t look like one isn’t even seen; a tag that looks like a button gets tapped and does nothing.

**Wrong:** “Not interested” in light gray on light gray, with no border, looking like a tag; the “Only you” tag with a border, looking like a button.

**Right:** actions with a fill or an outline; tags with no border and no tap.

## The button says what it does

**Rule:** the button text is a verb with its object: “Save address”, “Delete account”, “Keep editing”. Never a bare “OK”, “Yes”, “No” or “Click here”. In a dialog, both buttons say what happens. The same action has the same name across the whole app.

**Why:** many people read only the button. “Yes” forces them back to the question; “Delete movie” explains itself.

**Exception:** “OK” in a notice that only informs.

**Wrong:** “Are you sure?” with “Yes” and “No”; “Save” on one screen and “Store” on another.

**Right:** “Delete movie” and “Keep movie”.

**Sources:** Apple, Alerts — verbs on buttons, and “OK” only in an alert that informs (https://developer.apple.com/design/human-interface-guidelines/alerts); Nielsen Norman Group, buttons that sum up what will happen (https://www.nngroup.com/articles/confirmation-dialog/); WCAG 2.4.4, the link text says where it leads, level A (https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html).

## Deleting: undo or confirm

**Rule:** an action that deletes or loses something has a way out.
- For routine — removing an item from a list —, undo: a notice with “Undo” for a few seconds.
- For what is serious and can’t be reversed — deleting the account, erasing everything —, confirmation: the dialog says what will be lost, the safe action is the primary one, and the one that deletes is red, without emphasis.

**Why:** confirmation on everything becomes a habit, and people click without reading. Undo doesn’t interrupt and still rescues the mistake.

**Wrong:** “Are you sure?” for every item removed from the list; deleting the account with one tap, with no way back.

**Right:** “Movie removed. Undo”. And “Delete your account? Your 120 movies will be erased.”, with “Keep account” as the primary and “Delete account” in red.

**Sources:** Nielsen Norman Group, “Confirmation Dialogs Can Prevent User Errors — If Not Overused” (https://www.nngroup.com/articles/confirmation-dialog/); Apple, Alerts (https://developer.apple.com/design/human-interface-guidelines/alerts).

## As easy to leave as to enter

**Rule:** cancel, decline, skip and “Not now” are visible, at most two taps away, with no fine print and no faded color. When the app asks for consent — cookies, notifications, a subscription —, declining weighs the same as accepting.

**Why:** hiding the way out traps people and breaks their trust in the app.

**Wrong:** “No thanks, I’d rather pay more” in small gray text; canceling the subscription hidden five screens away.

**Right:** “Accept” and “Decline” in the same size; “Cancel subscription” in Profile, two taps away.

**Sources:** Nielsen, heuristic 3, user control and freedom (https://www.nngroup.com/articles/ten-usability-heuristics/); the “I’d rather pay more” has a name: confirmshaming (https://www.deceptive.design/types/confirmshaming).

## Every action responds

**Rule:**
- the button changes when tapped;
- what takes time shows “loading” on the button itself and doesn’t accept a second tap;
- the result shows up on screen: success, short and saying what changed (“3 movies added”), or the real failure, with what to do;
- a disabled button says what’s missing.

**Why:** with no response, people tap again — and the request goes out twice — or think it worked when it didn’t.

**Wrong:** “Save” with no feedback at all; “Place order” that accepts two taps; a faded “Continue” that doesn’t say why.

**Right:** “Saving…” on the button, then “Address saved.”; an active “Continue” that, when tapped, shows the missing field.

**Sources:** Nielsen, heuristic 1, the system shows what’s going on (https://www.nngroup.com/articles/ten-usability-heuristics/); Smashing Magazine, “Usability Pitfalls of Disabled Buttons, and How To Avoid Them” (https://www.smashingmagazine.com/2021/08/frustrating-design-patterns-disabled-buttons/).
