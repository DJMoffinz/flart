# flart
flart is a programming language for describing workflows or processes. because of its conciceness and flexibility it can be used as is, or compiled to graphviz DOT (when i finish the compiler). i often use it when writing pseudocode, and in fact it has helped me write this compiler.

## how it works
flart programs can technically contain anything you like, although certain symbols (`:`, `&`, `|`, `@` and `;`) break them up and make them more useful.

anything that is not one of those symbols is **content**. this means that anything, including whitespace may exist inside a bit of content, although any whitespace following or trailing behind it is removed.

a `:` means that the previous bit of content is a **label**.

an `&` or a `|` means that the previous bit of content is a **branch condition**. anything between that and whichever of those we didn't encounter is **body**, which we'll get to later, as is anything between that and the next label or condition. the body following the `&` is the **true** branch, and the body following the `|` is the **false** branch.

an `@` means that the *following* bit of content is a label to **call**. think of calling like jumping to the label, wherever it is in the program, following the process inside it, and returning to where we came from.

a `;` means that the previous bit of content, if it exists, is just a bit of content separate from the following bit.

**body** is a list of ordinary bits of content and calls.

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
