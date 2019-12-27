#include "Foo.h"
#include <iostream>

Foo::Foo(int nb)
{
    nbits = nb;
};

void Foo::bar()
{
    std::cout << nbits << std::endl;
};

extern "C"
{
    DLLEXPORT Foo* Foo_new(int nbits){ return new Foo(nbits);}
    DLLEXPORT void Foo_bar(Foo* foo){ foo->bar();}
}
