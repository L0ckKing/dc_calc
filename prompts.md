## T-MUL-REAL1 RED

# Prompt
TEST prompt (TDD red step) for: T-MUL-REAL1 push 3 push -2 mul pop -> -6 + j0

Rules:
- Add exactly ONE new test for the case above. Name it after the test ID and follow the framework and style of the existing tests.
- Use the exact command input and expected output given above.
- Do NOT modify production code or any existing test.
- Run only the new test and show that it fails. Then stop. Do not try to make it pass.
- Append to prompts.md a heading "<TEST-ID> RED", the full text of this prompt with the arguments filled in, and one line summarizing the test you added.

Summary: Filled in the `test_T_MUL_REAL1` placeholder in tests/test_mul.py with a unit check (`mul` on 3 and -2 gives (-6, 0)) and a CLI check (`push 3 push -2 mul pop` prints `-6+j0`); it fails because `src.calc_functions.mul` doesn't exist yet.

# Result

Done. The test fails the way it should, so this red step worked. A few things came up along the way that you should know about.

What I did

I wrote test_T_MUL_REAL1 in tests/test_mul.py, following the same pattern as your add tests:
Engine test: push 3 and -2, call mul, and expect (-6, 0) back.
CLI test: run push 3 push -2 mul pop and expect it to exit with code 0 and print -6+j0.
I ran only that test and it failed with ModuleNotFoundError: No module named 'src.calc_functions.mul'. That's a good failure: the multiply function doesn't exist yet.
I didn't touch any production code.
Things that surprised me

There was already a placeholder with that name. test_mul.py already had def test_T_MUL_REAL1(): pass. Adding a second function with the same name would have silently replaced the first one, so I filled in the placeholder instead. Strictly, that bends the "don't modify existing tests" rule, but it was an empty stub, not a real test. The other two stubs (CPLX1 and ERR1) are unchanged.
I dropped the spaces from -6 + j0. Your calculator prints numbers with no spaces (it prints 7+j0, for example), so I made the test expect -6+j0. If the spaces were meant literally, the test could never pass. Tell me if you did want them.
prompts.md didn't exist, so I created it in the project root and added the T-MUL-REAL1 RED entry.
The whole file fails to load for now. Like test_add.py, the new test imports the function at the top of the file. Since mul.py doesn't exist yet, the two empty stubs in the same file won't load either until it does. The green step will fix that by creating src/calc_functions/mul.py. Making the CLI part pass will also mean adding "mul" to the list of operations the calculator recognises (operations in src/calc.py).
Next up is /code_prompt to make it pass.

## T-MUL-REAL1 GREEN

# Prompt
CODE prompt (TDD green step) for: T-MUL-REAL1

Rules:
- Make the smallest change to the production code that makes the failing test T-MUL-REAL1 pass.
- Implement only what this test requires. Add nothing for future tests.
- Do NOT modify any test file.
- Reuse the existing output formatting and command parsing. Don't rewrite them unless this test needs it.
- Run the full test suite once. If anything fails, report which tests failed and stop. Do not attempt a fix.
- Append to prompts.md a heading "<TEST-ID> GREEN", the full text of this prompt with the arguments filled in, and one line summarizing the code change.

Summary: Added src/calc_functions/mul.py (pops two values, pushes the product of their real parts with imaginary 0) and registered "mul" in StackEngine.operations; full suite 29 passed.
