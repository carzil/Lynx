#(c) Andreev Alexander (aka Carzil)
import lynx.iostrem as io
from lynx.big import *

typedef hello => 
struct hi
{
    BigInt one;
    string two;
    int three;
}

def int main()
{
    hello a;
    a.one = 12312319513946513974539761;
    a.two = "Hello!";
    a.three = 1;
    io.print("1: " + a.one);
    io.print("2: " + a.two);
    io.print("3: " + a.three);
    return 0;
       
}


