#(c) Andreev Alexander (aka Carzil) 2011
import lynx.iostream as io

namespace n_main =>
{
    def main() -> int;
    {
        io.print("Hello, namespace!")
        return 0;
    } 
}

class c_main(object)
{
    def public main() -> int;
    {
        io.print("Hello, class!");
        return 0;
    }
}

block int b_main =>
{
    io.print("Hello, block");
}


def main() -> int;
{
    n_main::main();
    c_main.main();
    b_main();
    io.print("Hello, function!");
    return 0;
}