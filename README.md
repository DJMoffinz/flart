# flart
flart is a programming language for describing workflows or processes. because of its conciceness and flexibility it can be used as is, or compiled to graphviz DOT (when i finish the compiler). i often use it when writing pseudocode, and in fact it has helped me write this compiler.

## how it works
flart programs can technically contain anything you like, although certain symbols (`:`, `&`, `|`, `@` and `;`) break them up and make them more useful.

anything that is not one of those symbols is content. if you think of the parser like a switch statement (it actually is), this is the "default" case.

a `:` means that the previous bit of content is a label.

an `&` or a `|` means that the previous bit of content is a condition. Anything between that and whichever of those we didn't encounter is body, which we'll get to later, as is anything between that and the next label or condition.

an `@` means that the *following* bit of content is a label to jump to. Curently code following this is allowed, but it will never be reached. The compiler will probably warn users about this eventually.

a `;` means that the previous bit of content, if it exists, is just a bit of content separate from the following bit.

body is a list of ordinary bits of content and jumps. if it were defined more rigorously it would be a list of ordinary bits of content that may or may not end in a jump, but it isn't.

## compiler
the flart compiler is contained in main.py, which currently is not in a working state. the current licencing is such that prs are not possible, so i do not hope to see any. eventually i hope to be able to do so, and plan to licence the software Freely, but for now i am going to work on it on my own.
