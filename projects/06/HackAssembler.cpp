#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>

int main(){
    std::ifstream assemblyCode;
    char c;
    char goods[50];
    assemblyCode.open("add/Add.asm");    //default ios mode is in because used ifstream constructor
    if(assemblyCode.is_open()){
        int i = 0;
        while(assemblyCode.get(c)){
            goods[i] = c;
            i++;
        }
        std::cout << (goods) << std::endl;
        assemblyCode.close();
    }
    else std::cout << "No work :(" << std::endl;

    // std::cout << (goods) << std::endl;
    std::cout << typeid(goods).name() << std::endl;
    // std::cout << "Printing, Printing, Printing" << std::endl;

    return 0;
}