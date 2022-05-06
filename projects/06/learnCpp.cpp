#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>


int main(){
    std::ifstream assemblyCode;
    char goods[500] = {"stuff inside the goods array"};
    std::cout << typeid(goods).name() << std::endl;

    return 0;
}