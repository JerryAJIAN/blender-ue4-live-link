class Foo
{
    public:
        int bar(int x, int y, int z)
        {
            return x + y + z;
        }
};

DLLEXPORT Foo* Foo_new()
{
    return new Foo();
}

DLLEXPORT int Foo_bar(Foo* foo, int x, int y, int z)
{
    return foo->bar(x, y, z);
}
