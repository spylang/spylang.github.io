---
title: "SPy: a statically compilable variant of Python"
description: SPy is a variant of Python designed to be statically compilable while retaining many of the useful dynamic parts of Python. Interpreter and compiler, to native and WebAssembly.
---

::::: hero

![SPy logo](logo.svg)

# Python, made statically compilable

{.lead}
SPy is a variant of Python designed to be compiled ahead of time
**while** keeping many of the useful dynamic parts of Python.
Run it in an interpreter while you develop, compile it to native code or
WebAssembly when you need speed.

:::: buttons
[Try it in your browser](spy/){.btn .primary}
[Read the docs](docs/){.btn}
[View on GitHub](https://github.com/spylang/spy){.btn}
::::

:::::

:::::: grid

::::: card
### Interpreter and compiler
Keep the quick, interactive Python workflow, then compile the same code for speed.
:::::

::::: card
### Native and WebAssembly
Generate C and build native executables, or target WASI and Emscripten, so SPy runs in the browser.
:::::

::::: card
### Metaprogramming at compile time
Blue functions compute types and code ahead of time, which is how generics and many "dynamic" features stay fast.
:::::

::::: card
### High level and low level
Write Python-like code, and drop down to structs, pointers and raw memory when you need control.
:::::

::::::

::::::: split

:::::: col

## It looks like Python

SPy code is Python code with type annotations, and every program has a
`main` function as its entry point. The same file runs in the
interpreter or goes through the compiler.

::::: status
SPy is under heavy development: the language and the
documentation are still evolving.
:::::

::::::

:::::: col

```python
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def main() -> None:
    print(fib(10))
```

```console
$ spy fib.spy
55
$ spy build fib.spy --target native
$ ./build/fib
55
```

::::::

:::::::

## Start here

::::::: split

:::::: doc-links

- [Getting started](docs/dev/tutorials/getting-started/)\
  Install SPy and run your first program.
- [Examples](docs/dev/examples/1_high_level/)\
  From high-level code to raw memory access.
- [Reference](docs/dev/reference/python_builtins/)\
  Builtins, types, the CLI and scoping rules.
- [Contributing](docs/dev/contributing/)\
  Set up your machine and send your first pull request.

::::::

:::::: doc-links

- [Inside SPy, part 1: Motivations and Goals](https://antocuni.eu/2025/10/29/inside-spy-part-1-motivations-and-goals/)\
  Why SPy exists and what it tries to achieve.
- [Inside SPy, part 2: Language semantics](https://antocuni.eu/2026/03/25/inside-spy-part-2-language-semantics/)\
  How the language works.
- [PyCon Italy 2025 talk](https://youtu.be/W-8tgZDgYmw)\
  Recording of the talk introducing SPy.
- [Roadmap](https://github.com/spylang/spy/blob/main/ROADMAP.md)\
  What is planned next.

::::::

:::::::

## Community

Join the [Discord server](https://discord.gg/wRb29FGZpP) and the
monthly community call, on the first Wednesday of the month at 17:30 CET
([calendar](https://calendar.app.google/5qMsCibGVH8kAkcs7)).
Contributions of every kind are welcome.
