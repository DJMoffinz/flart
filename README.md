# flart
flart is a programming language for describing workflows or processes. because of its conciceness and flexibility it can be used as is, or compiled to graphviz DOT (when i finish the compiler). i often use it when writing pseudocode, and in fact it has helped me write this compiler.

## how it works
flart programs can technically contain anything you like, although certain symbols (`:`, `&`, `|`, `@` and `;`) break them up and make them more useful.

anything that is not one of those symbols is **content**. this means that anything, including whitespace may exist inside a bit of content, although any whitespace following or trailing behind it is removed.

a `:` means that the previous bit of content is a **label**.

an `&` or a `|` means that the previous bit of content is a **branch condition**. Anything between that and whichever of those we didn't encounter is **body**, which we'll get to later, as is anything between that and the next label or condition. The body following the `&` is the **true** branch, and the body following the `|` is the **false** branch.

an `@` means that the *following* bit of content is a label to jump to. Curently code following this is allowed, but it will never be reached. The compiler will probably warn users about this eventually.

a `;` means that the previous bit of content, if it exists, is just a bit of content separate from the following bit.

**body** is a list of ordinary bits of content and jumps. if it were defined more rigorously it would be a list of ordinary bits of content that may or may not end in a jump, but it isn't.

## example
a program that demonstrates all of flart's features might look something like this:

    lamp doesnt work:
      lamp plugged in? |
      plug in lamp &
      bulb burnt out? &
      @replace bulb |
      repair lamp;

    replace bulb:
      remove bulb;
      dispose of bulb responsibly;
      install replacement bulb;

note that whitespace or indentation between symbols is irrelevant and you are free to write the program however you like.

## compiler
the flart compiler is contained in main.py, which currently is not in a working state, and i am not accepting prs. when i am happier with the state of the project, perhaps i will.
