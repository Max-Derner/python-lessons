

# This Python code is totally valid, it just doesn't adhere to PEP8 standards


class A: ...
class B(A): ...
class C(A): ...
class D(B): ...
class E(B, C): ...
class F(C): ...
class G(D, E): ...
class H(E, F): ...
class I(G, H): ...


print(I.mro())
