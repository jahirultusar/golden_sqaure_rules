
## Notes: 
We can actually use tests to structure our approach to programming. In doing this, we learn a way of programming that works within the limitations of our brains.

 What a 'normal' non-test-driven programming looks like:

## Freerunning Development

In this approach, we read the problem and think about it for a bit. Then we start writing code. we keep going and possibly running the code, seeing if we're getting closer to the solution and fixing our mistakes. Eventually our program does what we want.

This can be very thrilling and motivating when it is going well!

However, there is a problem: code gets complex. At some point it gets so complex that it won't fit in our brains any more. Then we start to feel overloaded and anxious. It can be very frustrating.

Freerunning Development is fine for small problems that stay small. However, when problems get bigger we start to see the limits of this approach.

Test-driven development is another approach. Let's look at that:

## Test-driven Development

In this approach, we read the problem and think about it for a bit.

Then you write a small example of how your code might be used in the form of a 'test' or 'specification' ('spec'). You run the test and see that it fails with an error. This is called the 'red' phase.

Then we write just enough of your program so that it can behave like the example (test) we wrote. Then we run the test again. If it still fails we fix it. Eventually we get it to pass. This is called the 'green' phase.

After this, we improve the readability, structure, and other qualities of the code we wrote without changing its behaviour. This is called the 'refactor' stage.

Then we write another small example, and continue in a cycle until our program is complete and we have a full set of examples to prove it.

This approach is much more structured and, at times, it can even feel boring. However because it forces us to break down large problems into clearly specified and small examples that we focus on one by one, it helps our brains manage the complexity of a codebase by taking things 'one at a time'.

The above is a simplified approach. Over time we will add more techniques to it.

Test-driven development is an approach to building software in the same way that Karate is an approach to combat. It structures everything we do. At first it will feel strange and we will want to resume our unstructured approach. However, it allows we to tackle much greater problems.

In the same way the discipline of a martial artist enables them to use their strength much more effectively, our discipline — both in test-driving and the other three practices — enables we to use our brain much more effectively.

