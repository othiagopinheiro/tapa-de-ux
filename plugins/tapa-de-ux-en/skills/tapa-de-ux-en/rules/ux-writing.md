# UX writing

This section looks at the app’s text as a whole: the same thing said the same way everywhere. As in hierarchy, the review compares the whole app, not one screen.

Button text is in buttons and actions (`buttons-and-actions.md`), the structure of errors and empty states in states (`states.md`) and sentence case in typography (`typography.md`).

**How to review (applies to every rule):**
1. Gather all the app’s text. In code, the string and translation files and the text inside components. In a screenshot, what appears — and the review says it applies only to those screens.
2. Build four lists: the names of things; the verbs of actions; the formats (date, time, money, numbers); the messages by type (confirmation, error, empty, warning).
3. In each list, point out where the same thing appears in two ways, with the location of each.
4. Propose a single way and the list of what changes and where. If the project already has a glossary or a voice guide, it stands.

## One name for each thing

**Rule:** each thing in the app — screen, list, feature, object — has one name, the same in the menu, the title, the button and the messages. The project keeps these names in a list.

**Why:** with another name, people think it’s another thing, and look for it twice.

**Wrong:** “My movies” in the menu, “My list” in the title and “Library” in the notice; “Watch later” on one screen and “Favorites” on another, for the same list.

**Right:** “Watch later” in the menu, in the title, on the “Add to Watch later” button and in the notice “3 movies in Watch later”.

**Sources:** Apple, Writing — keep a list of common terms (https://developer.apple.com/design/human-interface-guidelines/writing); Nielsen, heuristic 4, consistency and standards (https://www.nngroup.com/articles/ten-usability-heuristics/).

## One verb for each action

**Rule:** the same action uses the same verb across the whole app, and different verbs only for different results. If “Archive” takes something out of view and “Delete” erases it for good, that difference holds on every screen.

**Why:** a swapped verb makes people hesitate (“Is Store the same as Save?”) or hides a difference that matters: putting out of view or erasing forever.

**Wrong:** “Save”, “Store” and “Keep” for the same action; “Archive” on one screen and “Delete” on another, both erasing for good.

**Right:** “Save” everywhere; “Archive” and “Delete”, each with its own result, always.

**Sources:** Nielsen, heuristic 4, consistency and standards (https://www.nngroup.com/articles/ten-usability-heuristics/); Microsoft Writing Style Guide — don’t use a verb for removing to mean deleting (https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/r/remove).

## One voice across the app

**Rule:** the app’s voice is chosen once and holds on every screen: how it addresses the person (in English, “you”), how the app refers to itself — as “we” (“We found 3 movies”) or with no subject (“3 movies found”) — and how formal it is. If the app already has a defined voice, the review follows it and only points out where it changes.

**Why:** a voice that changes from screen to screen looks like an app made by several people who never talked to each other.

**Wrong:** “Can’t find it? Try another name.” on one screen and “The requested item could not be located.” on another; “I made your list” in the middle of “We found 3 movies”; one formal screen (“Dear valued customer”) and another full of slang.

**Right:** the same voice from start to finish — for example, “You don’t have any movies yet. Add the first one and we’ll light up its country on the map.”

**Sources:** Mailchimp, Voice and Tone — the voice barely changes; the tone changes all the time (https://styleguide.mailchimp.com/voice-and-tone/); Nielsen, heuristic 4 (https://www.nngroup.com/articles/ten-usability-heuristics/).

## One pattern for each kind of message

**Rule:** messages of the same kind follow the same pattern across the whole app. Every confirmation says what changed, with numbers; every error says what happened and what to do; every empty state says the state and the way forward. The tone adjusts to what the person is going through at that moment, but the same kind of message always has the same tone.

**Why:** when messages follow a pattern, people learn to read them at a glance. When each one is different, every message is news.

**Wrong:** “Movie saved!”, “Done, it worked 🎉” and “Operation completed successfully” for three identical confirmations; one error with a joke and another curt one.

**Right:** “Movie added.”, “3 movies added.”, “List deleted.” — always what changed, short, with a period.

**Sources:** Mailchimp, Voice and Tone — the tone changes with the reader’s emotional state (https://styleguide.mailchimp.com/voice-and-tone/); Nielsen Norman Group, “The Four Dimensions of Tone of Voice” (https://www.nngroup.com/articles/tone-of-voice-dimensions/).

## One format for each kind of data

**Rule:** date, time, money, number, unit and phone number are written one way across the whole app, in the standard of the reader’s country. Plurals are handled: “1 movie”, “5 movies”, never “movie(s)”.

**Why:** the same data in two formats makes people check twice, and sometimes misread.

**Wrong:** “21:00” on one screen and “9:00 PM” on another; “1 movie(s) added”.

**Right:** one format chosen and repeated everywhere — for example, “Mon, Sep 28”, “9:00 PM” and “$4.99”.

**Sources:** Nielsen, heuristic 4 (https://www.nngroup.com/articles/ten-usability-heuristics/); Android, strings with plurals (quantity strings) (https://developer.android.com/guide/topics/resources/string-resource).

## One way of writing: capitals and punctuation

**Rule:** the same writing choices across the whole app: sentence case in titles and buttons, or the platform’s style where it asks for another (see typography); a period at the end of a complete sentence, not in titles, buttons or labels; one kind of quotation mark; and emoji, if any, with the same rule everywhere.

**Why:** mismatched punctuation and capitals don’t stop anyone from reading, but they make the app look patched together.

**Wrong:** “Save Address” on one button and “Save address” on another; a title with a period on one screen and without one on another; emoji in one notice and in no other.

**Right:** the same choices, from the first text to the last.

**Sources:** Microsoft Writing Style Guide, Periods — a period in complete sentences, none in titles and interface text (https://learn.microsoft.com/en-us/style-guide/punctuation/periods); Apple, Writing — one capitalization style per element type (https://developer.apple.com/design/human-interface-guidelines/writing).

## People’s words, the important part first

**Rule:** the everyday words of the people who use the app, with no system jargon (sync, cache, token, error 500) and no company-internal names (acronyms, departments, systems). The information that decides comes in the first words of the title, the list item and the notice; if it can be said in fewer words, say it in fewer.

**Why:** plain language helps everyone, even experts. And on screen, people scan: in a list item, they tend to see only the first two words.

**Wrong:** “Cache sync failure”; “Here you can find the options to choose which notifications you want to receive”.

**Right:** “We couldn’t update your list right now”; “Notifications: choose which ones you get”.

**Sources:** Nielsen, heuristic 2, the words of the people who use it, not internal jargon (https://www.nngroup.com/articles/ten-usability-heuristics/); Nielsen Norman Group, “Plain Language Is for Everyone, Even Experts” (https://www.nngroup.com/articles/plain-language-experts/) and “First 2 Words: A Signal for the Scanning Eye” (https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/); Apple, Writing — avoid jargon and use fewer words (https://developer.apple.com/design/human-interface-guidelines/writing).
