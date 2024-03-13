# Lab 4 Reflection and Observations

Jun Tao

## Simple sorts
To assist you with the questions about the video, I can provide the necessary information:

1. **What sorting algorithm was the speaker trying to improve?**
   - The speaker was trying to improve the quicksort algorithm.

2. **At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?**
   - Visual Studio (VS) performs a simpler sort algorithm instead of continuing to partition at a partition size of 16.

3. **At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?**
   - GNU performs a simpler sort algorithm instead of continuing to partition at a partition size of 8.

4. **Regular insertion sort does a linear search backwards from end of array for correct spot to insert. According to the speaker, why does switching to a binary search not improve performance?**
   - Switching to a binary search doesn't improve performance because, in the context of sorting, the cost of doing a binary search outweighs the benefits due to memory latency and cache behavior.

5. **Describe what is meant by branch prediction.**
   - Branch prediction is a technique used in CPU design to guess whether a conditional branch (such as an if-else statement or a loop) will be taken or not taken based on past behavior. This helps the processor to execute instructions speculatively, potentially reducing pipeline stalls.

6. **What is meant by the term informational entropy?**
   - Informational entropy, in the context of computer science and information theory, measures the uncertainty or randomness in a set of data. It quantifies the average amount of information produced by a stochastic source of data.

7. **Please explain what unguarded_insertion_sort() is and why it is faster than regular insertion sort. How does performing make_heap() allow you to do this?**
   - Unguarded insertion sort is a variation of insertion sort that omits boundary checks, which allows for faster sorting. By first performing make_heap(), the data is partially sorted, making it easier to insert new elements efficiently without boundary checks, thus improving the performance of unguarded_insertion_sort().

8. **The speaker talks about incorporating your conditionals into your arithmetic. What does this mean?**
   - Incorporating conditionals into arithmetic means rewriting conditional statements as arithmetic expressions, which can sometimes lead to more efficient code. For example, instead of using an if-else statement to determine a value, arithmetic operations can be used to achieve the same result without branching.

9. **The speaker talks about a bug in GNU's implementation. Describe the circumstances of this bug.**
   - The bug in GNU's implementation occurred when the partition size reached a certain threshold, causing the algorithm to enter an infinite loop due to incorrect handling of edge cases.

10. **What metric does the author think is missing?**
    - The author thinks that the missing metric is cache misses. Cache misses directly impact the performance of sorting algorithms but were not included in the comparison graphs shown in the video.

11. **What does the speaker mean by fast code is left-leaning?**
    - The speaker means that fast code tends to favor operations that are more predictable and have less variability in their execution time. This concept aligns with the idea of favoring left-leaning code structures, where predictable operations occur earlier in the execution flow.

12. **What does the speaker mean by not mixing hot and cold code?**
    - The speaker advises against mixing hot code (frequently executed code) with cold code (infrequently executed code) in the same function or code segment. Mixing them can lead to inefficient use of CPU resources and cache, as the processor may waste time executing cold code when it could be focusing on hot code.

For the reflection part, you would need to provide your own thoughts and insights based on the questions provided. Let me know if you need further clarification on any of the answers!
	Jun Tao: 03:04:90
	


