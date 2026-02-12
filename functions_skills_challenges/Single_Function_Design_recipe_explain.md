# Design Recipe

In the exercise, you were given a design for a function, wrote some tests, and then implemented the behaviour to make those tests pass.

However, in industry an engineer will rarely be given a design. They will instead be given a problem to solve. They will then have to decide how to design their program to solve the problem.

To support you in growing towards this, we will use the idea of Design Recipes. You might use different design recipes for different kinds of program. We will start off with a simple one for a single-function program.

Here is a template for you to use. Steps 1 and 2 are new, and steps 3 and 4 are what you did in the last exercise.

## Single-Function Programs Design Recipe

1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

2. Design the Function Signature
The signature of a function includes:

The name of the function.
What parameters it takes, their names and data types.
What it returns and the data type of that value.
Any other side effects it might have.
Steps 3 and 4 then operate as a cycle.

3. Create Examples as Tests
These are examples of the function being called with particular arguments, and what the function should return in each situation.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the function to return the right value for the given arguments.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.