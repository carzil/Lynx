#(c) Andreev Alexander (aka Carzil) 2011
import lynx.iostream as io
import lynx.lang

namespace n_main =>
{
    def int main()
    {
        io.print("Hello, namespace!")
        return 0;
    } 
}

class c_main(object)
{
    def int main() -> public;
    {
        io.print("Hello, class!");
        return 0;
    }
}

def int f_main()
{
    io.print("Hello, function!");
    return 0;
}

block int b_main =>
{
    io.print("Hello, block");
    return 0;
}

lynx.lang.set_main(&(b_main))
