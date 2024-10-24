## [<- GO BACK](../03_complex_inheritance.md#predicting-the-mro)


Given we've still got the following inheritance nonsense:

```
      A
     / \
    B   C
   / \ / \
  D   E   F
   \ / \ /
    G   H
     \ /
      I
```
and that in Python, we've implemented that as:
```python
class A: ...
class B(A): ...
class C(A): ...
class D(B): ...
class E(B, C): ...
class F(C): ...
class G(D, E): ...
class H(E, F): ...
class I(G, H): ...
```

So the way that the MRO is constructed is like so:  

| Currently looking at | Action | MRO so far |
|----------------------|--------|------------|
| I | add and move on |I |
| G | add and move on | I, G |
| D | add and move on | I, G, D |
| B | add and move on | I, G, D, B |
| A | add and backtrack | I, G, D, B, A |
| B | backtrack | I, G, D, B, A |
| D | backtrack | I, G, D, B, A |
| G | inspect unexplored parent | I, G, D, B, A |
| E | add and move on | I, G, D, B, A, E |
| B | move to end of MRO and move on | I, G, D, A, E, B |
| A | move to end of MRO and backtrack | I, G, D, E, B, A |
| B | backtrack | I, G, D, E, B, A |
| E | inspect unexplored parent | I, G, D, E, B, A |
| C | add and move on | I, G, D, E, B, A, C |
| A | moveto end of MRO and backtrack | I, G, D, E, B, C, A |
| C | backtrack | I, G, D, E, B, C, A |
| E | backtrack | I, G, D, E, B, C, A |
| G | backtrack | I, G, D, E, B, C, A |
| I | inspect unexplored parent | I, G, D, E, B, C, A |
| H | add and move on | I, G, D, E, B, C, A, H |
| E | move to end of MRO and move on | I, G, D, B, C, A, H, E |
| B | move to end of MRO and move on | I, G, D, C, A, H, E, B |
| A | move to end of MRO and backtrack | I, G, D, C, H, E, B, A |
| B | backtrack | I, G, D, C, H, E, B, A |
| E | resolve parent being too early in MRO | I, G, D, C, H, E, B, A |
| C | move to end of MRO and move on | I, G, D, H, E, B, A, C |
| A | move to end of MRO and backtrack | I, G, D, H, E, B, C, A |
| C | backtrack | I, G, D, H, E, B, C, A |
| E | backtrack | I, G, D, H, E, B, C, A |
| H | inspect unexplored parent | I, G, D, H, E, B, C, A |
| F | add and move on | I, G, D, H, E, B, C, A, F |
| C | move to end of MRO and move on | I, G, D, H, E, B, A, F, C |
| A | move to end of MRO and backtrack | I, G, D, H, E, B, F, C, A |
| C | backtrack | I, G, D, H, E, B, F, C, A |
| F | backtrack | I, G, D, H, E, B, F, C, A |
| H | backtrack | I, G, D, H, E, B, F, C, A |
| I | backtrack (No more parents to search, so finish) | I, G, D, H, E, B, F, C, A |

## [<- GO BACK](../03_complex_inheritance.md#predicting-the-mro)