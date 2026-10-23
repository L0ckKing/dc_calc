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

# Result

Done. T-MUL-REAL1 passes, and so does everything else: all 29 tests pass, no failures.

What I changed

New file src/calc_functions/mul.py: it takes the top two values off the stack, multiplies them, and puts the result back. It's built the same way as add.py.
src/calc.py, two lines: it now imports mul and adds "mul": mul to operations, so the CLI recognises the mul command.
I didn't change the number parsing, the output formatting or any tests. I added the GREEN entry to prompts.md using the same Prompt/Result layout you set up.
One thing to watch out for
Because the rule said to implement only what this test needs, mul only multiplies the real parts and always sets the imaginary part to 0. For real numbers like 3 × -2 that's correct. For complex numbers it gives the wrong answer without any error: (1+j1) × (1+j1) should be 0+j2, but it would give 1+j0. That's normal TDD. Your next test, T-MUL-CPLX1, should fail on exactly this, and that's when the full complex formula goes in: (ac − bd) + j(ad + bc).

No surprises this time. It went smoothly.




## T-MUL-CPLX1 RED

# Prompt
TEST prompt (TDD red step) for: T-MUL-CPLX1 push 1+j2 push 3-j4 mul pop -> 11 + j2

Rules:
- Add exactly ONE new test for the case above. Name it after the test ID and follow the framework and style of the existing tests.
- Use the exact command input and expected output given above.
- Do NOT modify production code or any existing test.
- Run only the new test and show that it fails. Then stop. Do not try to make it pass.
- Append to prompts.md a heading "<TEST-ID> RED", the full text of this prompt with the arguments filled in, and one line summarizing the test you added.

Summary: Filled in the `test_T_MUL_CPLX1` placeholder in tests/test_mul.py with a unit check (`mul` on (1+j2) and (3-j4) gives (11, 2)) and a CLI check (`push 1+j2 push 3-j4 mul pop` prints `11+j2`); it fails because `mul` currently returns (3, 0), multiplying only the real parts.

# Result 

Red step done. The new test fails for exactly the reason we expected.

What I did

I first checked your expected value by hand: (1+j2) × (3−j4) = 3 − j4 + j6 + 8 = 11+j2. Your number is right.
I wrote test_T_MUL_CPLX1 in tests/test_mul.py the same way as the REAL1 test:
Engine test: multiply (1, 2) by (3, -4) and expect (11, 2).
CLI test: run push 1+j2 push 3-j4 mul pop and expect 11+j2.
I ran only this test and it failed with actual = (3.0, 0.0), expected = (11.0, 2.0). That's the shortcut from the last step showing up: mul currently multiplies only the real parts (1 × 3 = 3) and sets the imaginary part to 0. This is the failure we wanted.
I added the T-MUL-CPLX1 RED entry to prompts.md using your Prompt/Summary layout.
Same two notes as last time, nothing new

I filled in the existing pass placeholder rather than adding a second function with the same name.
The test expects 11+j2 with no spaces, because that's how your calculator prints numbers.
No production code changed. When you run /code_prompt T-MUL-CPLX1, the fix should be one line in mul.py: replace the real-only product with the full formula (ac − bd) + j(ad + bc).


## T-MUL-CPLX1 GREEN

# Prompt
CODE prompt (TDD green step) for: T-MUL-CPLX1

Rules:
- Make the smallest change to the production code that makes the failing test T-MUL-CPLX1 pass.
- Implement only what this test requires. Add nothing for future tests.
- Do NOT modify any test file.
- Reuse the existing output formatting and command parsing. Don't rewrite them unless this test needs it.
- Run the full test suite once. If anything fails, report which tests failed and stop. Do not attempt a fix.
- Append to prompts.md a heading "<TEST-ID> GREEN", the full text of this prompt with the arguments filled in, and one line summarizing the code change.

Summary: Replaced the real-only product in src/calc_functions/mul.py with the full complex product (ac - bd) + j(ad + bc); full suite 29 passed.

# Result

Done. T-MUL-CPLX1 now passes, and the full suite is still green: 29 passed, nothing failed.

What I changed
It was a one-line change in src/calc_functions/mul.py. The real-only shortcut from last time:


engine.push((a[0] * b[0], 0.0))
is now the full complex multiplication, (ac − bd) + j(ad + bc):


engine.push((a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]))
Nothing else needed to change. mul was already registered as a command, and the existing code already reads 1+j2 and prints 11+j2 correctly. I didn't touch any tests, and I added the T-MUL-CPLX1 GREEN entry to prompts.md.

Did REAL1 survive?
Yes. With real numbers the imaginary parts are 0, so the new formula gives 3 × -2 − 0 = -6 with imaginary part 0. That's the same answer as before, so T-MUL-REAL1 still passes.

No surprises this round. Multiplication now works correctly for complex numbers too. The only empty placeholder left in test_mul.py is T-MUL-ERR1, probably the stack-underflow case (for example, mul with only one number on the stack).



## T-MUL-ERR1 RED

# Prompt
TEST prompt (TDD red step) for: T-MUL-ERR1 mul -> Error: stack underflow

Rules:
- Add exactly ONE new test for the case above. Name it after the test ID and follow the framework and style of the existing tests.
- Use the exact command input and expected output given above.
- Do NOT modify production code or any existing test.
- Run only the new test and show that it fails. Then stop. Do not try to make it pass.
- Append to prompts.md a heading "<TEST-ID> RED", the full text of this prompt with the arguments filled in, and one line summarizing the test you added.

Summary: Filled in the `test_T_MUL_ERR1` placeholder in tests/test_mul.py with a unit check (`mul` on an empty stack raises IndexError) and a CLI check (`mul` prints `Error: stack underflow` to stderr); it PASSED on first run (no red) because `pop` already raises IndexError and main.py already turns that into the underflow message.


# Result
I wrote the test, but it passed the first time I ran it, so this "red" step never went red. Nothing is broken; it's actually good news, but it's a break from the usual TDD routine.

What I did
I wrote test_T_MUL_ERR1 in tests/test_mul.py in two parts:

Engine test: calling mul on an empty stack should raise IndexError.
CLI test: typing mul should print Error: stack underflow, and the program should still exit normally (code 0).
Why it passed straight away
Your existing code already covers this case:

mul starts with engine.pop(), and pop already raises IndexError when the stack is empty.
main.py already catches IndexError and prints Error: stack underflow.
So mul handled this error from the moment you registered it, with no extra code. I didn't rig the test to make it fail, because a fake red tells you nothing. In prompts.md I logged it as "PASSED on first run (no red)" so the record is accurate.

One problem I hit along the way

None of the other error tests are written yet. Every other ERR1 test is still an empty pass, so there was no example to copy.
The test helper can't see error messages. run_cli only returns normal output (stdout), but the calculator prints errors to a separate stream (stderr). Since I wasn't allowed to change the helper, I imported the test runner and app directly into test_mul.py and checked result.stderr.
Suggestion: every other ERR test will need the same thing, so it may be worth extending run_cli to return stderr too. That would change a shared test file, though, so it's your call.
What next?
There's nothing to fix, so /code_prompt T-MUL-ERR1 would just run the suite and find it passing. You can skip it, or run it for a GREEN entry in the log. If your course expects to see a red result, you could mention in your write-up that this behaviour came for free from pop.
## T-DIV-REAL1 RED

# Prompt
TEST prompt (TDD red step) for: T-DIV-REAL1 push 8 push 2 div pop -> 4 + j0

Rules:
- Add exactly ONE new test for the case above. Name it after the test ID and follow the framework and style of the existing tests.
- Use the exact command input and expected output given above.
- Do NOT modify production code or any existing test.
- Run only the new test and show that it fails. Then stop. Do not try to make it pass.
- Append to prompts.md a heading "<TEST-ID> RED", the full text of this prompt with the arguments filled in, and one line summarizing the test you added.

Summary: Filled in the `test_T_DIV_REAL1` placeholder in tests/test_div.py with a unit check (`div` on 8 and 2 gives (4, 0)) and a CLI check (`push 8 push 2 div pop` prints `4+j0`); it fails because `src.calc_functions.div` doesn't exist yet.

# Result

Red step done. It's the same pattern as T-MUL-REAL1, and this time it actually went red.

What I did

I filled in the test_T_DIV_REAL1 placeholder in tests/test_div.py, following the same style as the add and mul tests:
Engine test: push 8 and 2, call div, and expect (4, 0).
CLI test: run push 8 push 2 div pop and expect 4+j0, with no spaces, since that's how your calculator prints numbers.
I ran only that test and got ModuleNotFoundError: No module named 'src.calc_functions.div'. That's the failure we want, because the divide function doesn't exist yet.
I added the T-DIV-REAL1 RED entry to prompts.md, and I didn't touch any production code.
Same small side effects as with mul

The other two placeholders in that file, CPLX1 and ERR1, can't load until div.py exists, because the import at the top of the file fails.
For the green step

Order matters: with push 8 push 2 div, the 8 goes in first. So div should compute "first pushed ÷ second pushed" (a / b), the same way add and mul name them a and b.
Possible repeat of the mul error test: main.py already catches ZeroDivisionError and prints Error: division by zero. If T-DIV-ERR1 turns out to be divide-by-zero, it may pass on its first run, like T-MUL-ERR1 did. Whether that happens depends on how div gets written.



## T-DIV-REAL1 GREEN

# Prompt
CODE prompt (TDD green step) for: T-DIV-REAL1

Rules:
- Make the smallest change to the production code that makes the failing test T-DIV-REAL1 pass.
- Implement only what this test requires. Add nothing for future tests.
- Do NOT modify any test file.
- Reuse the existing output formatting and command parsing. Don't rewrite them unless this test needs it.
- Run the full test suite once. If anything fails, report which tests failed and stop. Do not attempt a fix.
- Append to prompts.md a heading "<TEST-ID> GREEN", the full text of this prompt with the arguments filled in, and one line summarizing the code change.

Summary: Added src/calc_functions/div.py (pops two values, pushes the quotient of their real parts, a/b, with imaginary 0) and registered "div" in StackEngine.operations; full suite 29 passed.

# Result

T-DIV-REAL1 now passes, and so do all 29 tests in the suite. No failures and no surprises this round.

What I changed

New file src/calc_functions/div.py: it takes the top two values off the stack and pushes a / b, where a is the first number you pushed. So push 8 push 2 div gives 4, not 0.25.
src/calc.py, two lines: it now imports div and adds "div": div to operations, so the CLI recognises the command.
I didn't change any tests or the parsing and formatting code, and I added the GREEN entry to prompts.md.
Same deliberate shortcut as with mul
Because the rules say to implement only what this test needs, div divides only the real parts and always sets the imaginary part to 0. That's correct for 8 ÷ 2, but it gives wrong answers for complex numbers without any error. T-DIV-CPLX1 should catch that. Proper complex division is a bit harder than multiplication: you divide by the denominator's squared size (c² + d²), so (a+jb)/(c+jd) = ((ac + bd) + j(bc − ad)) / (c² + d²).

What to expect for T-DIV-ERR1
If that test is divide-by-zero, it will probably pass on its first run, like T-MUL-ERR1 did:

a[0] / b[0] with b = 0 makes Python raise ZeroDivisionError automatically.
main.py already catches that error and prints Error: division by zero.
There's a catch, though: once the complex formula goes in, that division by c² + d² is what will raise the error instead. That still works, since a value of 0 means both parts are 0, but it's worth knowing that the source of the error moves.


