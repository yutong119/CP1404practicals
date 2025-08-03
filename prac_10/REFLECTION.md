# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

The time I estimate is usually shorter than the time I actually practice

### How did your estimate accuracy improve or change during the course of the subject?

Depending on my level of concentration, and if it's something I've learned before, 
I usually do it faster, but if it's new knowledge, I'll be slower

### What did you learn from doing these estimates?

I have learned that estimates can give me a sense of mastery over the knowledge I have learned and make me more confident.

## Code Reviews

### What have you learned from being reviewed by other people?

There are some knowledge points I missed. 
I can make up for them by looking at others' code. The work of others is indeed more concise and efficient than mine

### What have you learned from doing code reviews of other people?

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

Sort class use key= attrgetter("priority") rather than key=lambda x: x.priority

### Explanation

attrgetter can directly obtain object properties through property names, avoiding the need to manually write lambda functions or customize access logic

### Good Code Review 2

guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))  

parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)

### Explanation

Avoid repetition to make the code more concise

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

What's the difference between spending more time explaining grammar knowledge in person rather than watching videos and taking online classes

### What did you do really well for practicals in this subject?

reviewed some knowledge weekly
