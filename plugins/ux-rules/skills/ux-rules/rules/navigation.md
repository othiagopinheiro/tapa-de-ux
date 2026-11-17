# Navigation

Touch targets are in accessibility (`accessibility.md`), and so is “never color alone”: the active item isn’t marked by color alone.

**How to review (applies to every rule):**
1. Draw the app’s map: the main sections, what’s inside each one and how each screen is reached.
2. Walk the most common paths from start to finish and count the steps. At each step, ask: do people know where they are and what comes next?
3. Test back on every screen: the app’s button, the device’s gesture and the browser’s back.

## Visible navigation

**Rule:** the main sections sit in an always-visible bar — at the bottom on phones, at the top or on the side on computers —, with three to five items, each with an icon and a name. A hidden menu (the three lines) only when there are too many sections for the bar, and never for the main ones.

**Why:** what’s in view gets used; what’s hidden gets forgotten. And an icon alone is guesswork: few icons are understood by everyone.

**Wrong:** the app’s four sections inside a three-line menu; a bar with icons only, no names.

**Right:** a bottom bar with “Map”, “My movies”, “Suggestions” and “Profile”, each with an icon and a name.

**Sources:** Material 3, a navigation bar with three to five destinations of equal importance (https://developer.android.com/develop/ui/compose/components/navigation-bar); Nielsen Norman Group, hidden navigation makes the experience worse (https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/) and an icon needs a name next to it (https://www.nngroup.com/articles/icon-usability/).

## You are here

**Rule:** people always know where they are. The current item in the bar is marked — by weight, background or shape, besides color —, and each screen has its own title, which says where it is.

**Why:** without that signal, people lose their way, especially when they arrive from a link or a notification.

**Wrong:** the active item only slightly darker; two different screens with the same title, “Details”.

**Right:** the active item with a heavier name and a background behind the icon; “My movies” as the title of the list and the movie’s name as the title of its screen.

**Sources:** Nielsen Norman Group, “Navigation: You Are Here” — highlight the current item and give each screen a title that describes it (https://www.nngroup.com/articles/navigation-you-are-here/).

## The bar goes to places, it doesn’t do actions

**Rule:** each item in the bar is a place in the app, not an action. Actions — adding, creating, publishing — get their own button, inside the screen. The bar is the same on every main screen.

**Why:** people use the bar to find their bearings. An item that opens an action instead of going to a place breaks that logic and takes away the “where am I”.

**Wrong:** a “+” in the middle of the bar that opens the add form; a bar whose items change from one screen to another.

**Right:** a bar with places only; “Add movie” as a floating button on the screens where it makes sense.

**Sources:** Apple, Tab bars — the bar is for navigation, not actions; hiding it makes people forget which part of the app they’re in (https://developer.apple.com/design/human-interface-guidelines/tab-bars); Material 3, the same bar on every main screen (https://developer.android.com/develop/ui/compose/components/navigation-bar).

## Back always works

**Rule:** back — through the app’s button, the device’s gesture or the browser — takes people to where they were, the way it was: the same position in the list, the same filters, what they typed. On the web, each screen has its own address, so that back, reload and share work.

**Why:** back is the emergency exit. When it loses the place, erases what was typed or closes the app, people become afraid to explore.

**Wrong:** going back from a movie and landing at the top of the list, without the filters; the browser’s back leaving the whole app; reloading the page and losing the screen.

**Right:** going back and finding the list at the same point, with the filters on.

**Sources:** Nielsen, heuristic 3, a clearly marked emergency exit (https://www.nngroup.com/articles/ten-usability-heuristics/); Nielsen Norman Group, people count on back to return to a known place (https://www.nngroup.com/articles/navigation-you-are-here/) and addresses that don’t change, to save and come back to (https://www.nngroup.com/articles/url-as-ui/).

## The name says what’s there

**Rule:** each menu item, tab and link anticipates the content on the other side, in the words of the people who use the app. No vague names — “More”, “Miscellaneous”, “Resources” — that force people to open them to find out.

**Why:** people choose the path by its name. A vague name makes them open and go back, open and go back, until they give up.

**Wrong:** “More” with half the app inside; “Center” without saying center of what.

**Right:** “Help”, “Settings”, “Account”, each in its place.

**Sources:** Nielsen Norman Group, “Information Scent: How Users Decide Where to Go Next” (https://www.nngroup.com/articles/information-scent/).

## A short path to what people do most

**Rule:** the most common tasks sit a few steps from the start, and each step shows people they’re on the right path. It isn’t about counting taps: it’s about each screen making the next step clear. What’s rare can live deeper.

**Why:** a task people do every day, hidden, becomes effort every day. And a step that doesn’t show where it leads makes people doubt and go back.

**Wrong:** adding a movie — the app’s most common action — hidden under Profile, Settings, List; a screen in the middle of the path with only a “Continue” button.

**Right:** “Add movie” one tap from any main screen.

**Sources:** Nielsen Norman Group, “Flat vs. Deep Website Hierarchies” — content buried many levels down is hard to find (https://www.nngroup.com/articles/flat-vs-deep-hierarchy/) and “The 3-Click Rule for Navigation Is False” — more than counting clicks, what matters is a clear path (https://www.nngroup.com/articles/3-click-rule/).

## Dialogs and sheets know how to close

**Rule:** every dialog and sheet that opens on top has an obvious way to close: the X (with a touch area), the swipe-down gesture, the device’s back or, on a computer, Esc. A sheet is for a quick choice without losing your place; a long task goes to its own screen. And never a dialog on top of another.

**Why:** a dialog that doesn’t close traps people. A dialog on top of a dialog makes them lose the way back.

**Wrong:** a sheet with no X and no gesture; a confirmation that opens on top of another dialog; a long form inside a small sheet.

**Right:** a sheet with a grabber, a title and an X, that closes when swiped down; the long form opening full screen.

**Sources:** Apple, Modality — always an obvious way to close, and close one dialog before opening another (https://developer.apple.com/design/human-interface-guidelines/modality); W3C, dialog pattern — Esc closes it (https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).
